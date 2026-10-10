"""Provenance and borrowed terms mean one thing each (core 0.7.0).

- ``hasReference`` is where data came from: under ``prov:wasDerivedFrom``, range
  ``Reference``, never system topology (``linksComponent``);
- ``hasSource`` is only the flow property: under ``linksComponent``, never provenance;
- ``basedOn`` (scenario lineage) is provenance; its old twin ``derivedFrom`` is a
  deprecated alias of it, and ``hasDataSource`` one of ``hasReference``;
- the QUDT terms carry no Digicities domain or parent.
"""
from pathlib import Path

import rdflib
from rdflib import OWL, RDFS, URIRef

CORE_TTL = Path(__file__).parent.parent / "core" / "dici_onto_core.ttl"
DICI = rdflib.Namespace("https://digicities.info/ontology#")
PROV = rdflib.Namespace("http://www.w3.org/ns/prov#")
QUDT = rdflib.Namespace("http://qudt.org/schema/qudt/")

G = rdflib.Graph().parse(CORE_TTL, format="turtle")


def _supers(prop: URIRef) -> set:
    return set(G.transitive_objects(prop, RDFS.subPropertyOf))


def test_has_reference_is_provenance_to_a_reference():
    assert PROV.wasDerivedFrom in _supers(DICI.hasReference)
    assert DICI.linksComponent not in _supers(DICI.hasReference)
    assert set(G.objects(DICI.hasReference, RDFS.range)) == {DICI.Reference}


def test_has_source_is_flow_topology_only():
    assert DICI.linksComponent in _supers(DICI.hasSource)
    assert PROV.wasDerivedFrom not in _supers(DICI.hasSource)
    assert set(G.objects(DICI.hasSource, RDFS.domain)) == {DICI.Flow}


def test_based_on_is_provenance():
    assert PROV.wasDerivedFrom in _supers(DICI.basedOn)


def test_old_names_are_deprecated_aliases_of_the_new_ones():
    for alias, target in ((DICI.derivedFrom, DICI.basedOn),
                          (DICI.hasDataSource, DICI.hasReference)):
        assert (alias, OWL.deprecated, rdflib.Literal(True)) in G
        assert set(G.objects(alias, OWL.equivalentProperty)) == {target}
        assert target in _supers(alias)


def test_qudt_terms_carry_no_digicities_meaning():
    for term in (QUDT.unit, QUDT.value, QUDT.numericValue):
        assert not set(G.objects(term, RDFS.domain)), term
        assert not set(G.objects(term, RDFS.subPropertyOf)), term

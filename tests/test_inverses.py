"""Every property's owl:inverseOf partner is its own.

When two properties share an inverse, inference makes them imply each other:
`locationOf` used to be the inverse of both `hasLocation` and `locatedIn`, so
`hasLocation(a, b)` gave `locationOf(b, a)` and then `locatedIn(a, b)`. Choosing
one of the two predicates then meant nothing once a reasoner had run.
"""

from collections import defaultdict
from pathlib import Path

import rdflib
from rdflib.namespace import OWL

CORE_TTL = Path(__file__).parent.parent / "core" / "dici_onto_core.ttl"
DICI = rdflib.Namespace("https://digicities.info/ontology#")


def _partners(g: rdflib.Graph) -> dict:
    partners = defaultdict(set)
    for a, b in g.subject_objects(OWL.inverseOf):
        partners[a].add(b)
        partners[b].add(a)
    return partners


def test_no_property_shares_an_inverse():
    g = rdflib.Graph().parse(CORE_TTL, format="turtle")
    shared = {p: sorted(q) for p, q in _partners(g).items() if len(q) > 1}
    assert not shared, f"properties sharing an inverse partner: {shared}"


def test_located_in_and_has_location_have_distinct_inverses():
    g = rdflib.Graph().parse(CORE_TTL, format="turtle")
    partners = _partners(g)
    assert partners[DICI.locatedIn] == {DICI.locationContains}
    assert partners[DICI.hasLocation] == {DICI.locationOf}

"""Smoke tests: every TTL parses and the core ontology has the expected shape."""

from pathlib import Path

import rdflib
from rdflib.namespace import OWL, RDF


CORE_DIR = Path(__file__).parent.parent / "core"
CORE_TTL = CORE_DIR / "dici_onto_core.ttl"
QUDT_UNITS = CORE_DIR / "qudt_units.txt"

DICI = rdflib.Namespace("https://digicities.info/ontology#")


def _load_core() -> rdflib.Graph:
    g = rdflib.Graph()
    g.parse(CORE_TTL, format="turtle")
    return g


def test_core_parses():
    g = _load_core()
    assert len(g) > 1000, f"core ontology smaller than expected: {len(g)} triples"


def test_core_declares_ontology():
    g = _load_core()
    onto_iri = rdflib.URIRef("https://digicities.info/ontology")
    assert (onto_iri, RDF.type, OWL.Ontology) in g, "missing owl:Ontology declaration"


def test_attribute_root_class_present():
    g = _load_core()
    assert (DICI.Attribute, RDF.type, OWL.Class) in g, "dici_onto:Attribute missing"


def test_expected_attribute_subclasses_present():
    g = _load_core()
    expected = {
        "PhysicalAttribute",
        "SimpleCostAttribute",
        "UnitBasedCostAttribute",
        "CategoricalAttribute",
        "EventAttribute",
        "ComponentAttribute",
        "CurveAttribute",
        "CustomPhysicalRatioAttribute",
        "SimpleValueAttribute",
        "GeospatialAttribute",
    }
    missing = [
        name for name in expected if (DICI[name], RDF.type, OWL.Class) not in g
    ]
    assert not missing, f"missing attribute classes: {missing}"


def test_qudt_units_list_nonempty():
    assert QUDT_UNITS.exists(), "qudt_units.txt missing"
    lines = [
        line.strip()
        for line in QUDT_UNITS.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert len(lines) > 100, f"qudt_units.txt too small: {len(lines)} non-empty lines"

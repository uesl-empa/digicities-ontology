"""A categorical attribute's value is an IRI: hasCategoricalValue is an object
property pointing at the category (a named individual of the attribute class)."""

from pathlib import Path

from rdflib import OWL, RDF, RDFS, Graph, Namespace

DICI = Namespace("https://digicities.info/ontology#")
CORE = Path(__file__).resolve().parents[1] / "core" / "dici_onto_core.ttl"


def test_has_categorical_value_is_an_object_property():
    g = Graph().parse(CORE, format="turtle")
    assert (DICI.hasCategoricalValue, RDF.type, OWL.ObjectProperty) in g
    assert (DICI.hasCategoricalValue, RDF.type, OWL.DatatypeProperty) not in g
    # an object property cannot sit under the datatype property hasAttributeValue
    assert (DICI.hasCategoricalValue, RDFS.subPropertyOf, DICI.hasAttributeValue) not in g
    assert (DICI.hasCategoricalValue, RDFS.domain, DICI.CategoricalAttribute) in g

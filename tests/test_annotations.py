"""Annotation coverage: the core vocabulary must stay agent-mappable.

Agents onboarding new usecases map domain concepts (e.g. a WindPark) onto
core classes via descriptions, synonyms and examples — not names. These
tests keep that surface from regressing:

- every dici_onto term carries `rdfs:label` and `rdfs:comment`;
- every mapping-decision class (the Component subtree roots and the
  attribute kinds) carries `skos:definition` or `dici_onto:definition`,
  and at least one `skos:example`;
- the generated `docs/term-index.json` is not stale.
"""

import json
import subprocess
import sys
from pathlib import Path

import rdflib
from rdflib.namespace import OWL, RDF, RDFS, SKOS

REPO_ROOT = Path(__file__).parent.parent
CORE_TTL = REPO_ROOT / "core" / "dici_onto_core.ttl"
DOCS_DIR = REPO_ROOT / "docs"

DICI = rdflib.Namespace("https://digicities.info/ontology#")

# Classes where agents make parent-class mapping decisions: the direct
# children of Component plus the attribute kinds and cross-cutting roots.
# Every one of these must carry a definition and an example.
MAPPING_DECISION_CLASSES = [
    "Component",
    "Location",
    "Network",
    "Junction",
    "Actor",
    "Device",
    "Converter",
    "Storage",
    "EnergyConsumer",
    "EnergyGenerator",
    "EnergyCarrier",
    "Flow",
    "Process",
    "Resource",
    "Material",
    "Attribute",
    "PhysicalAttribute",
    "CategoricalAttribute",
    "DynamicAttribute",
    "CurveAttribute",
    "GeospatialAttribute",
    "TimeSeries",
    "Scenario",
    "Service",
    "ServiceRequirement",
]


def _load_core() -> rdflib.Graph:
    g = rdflib.Graph()
    g.parse(CORE_TTL, format="turtle")
    return g


def _dici_terms(g: rdflib.Graph) -> list[rdflib.URIRef]:
    terms = set()
    for rdf_type in (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty):
        for s in g.subjects(RDF.type, rdf_type):
            if isinstance(s, rdflib.URIRef) and str(s).startswith(str(DICI)):
                terms.add(s)
    return sorted(terms)


def test_every_term_has_label_and_comment():
    g = _load_core()
    missing_label = []
    missing_comment = []
    for term in _dici_terms(g):
        if not list(g.objects(term, RDFS.label)):
            missing_label.append(str(term))
        if not list(g.objects(term, RDFS.comment)):
            missing_comment.append(str(term))
    assert not missing_label, f"terms missing rdfs:label: {missing_label}"
    assert not missing_comment, f"terms missing rdfs:comment: {missing_comment}"


def test_mapping_decision_classes_have_definition_and_example():
    g = _load_core()
    missing_def = []
    missing_example = []
    for name in MAPPING_DECISION_CLASSES:
        cls = DICI[name]
        assert (cls, RDF.type, OWL.Class) in g, f"expected core class missing: {name}"
        has_def = list(g.objects(cls, SKOS.definition)) or list(g.objects(cls, DICI.definition))
        if not has_def:
            missing_def.append(name)
        if not list(g.objects(cls, SKOS.example)):
            missing_example.append(name)
    assert not missing_def, f"mapping-decision classes missing a definition: {missing_def}"
    assert not missing_example, f"mapping-decision classes missing skos:example: {missing_example}"


def test_location_carries_site_synonym():
    """Regression anchor for the WindPark→Location mapping failure."""
    g = _load_core()
    alt_labels = {str(o) for o in g.objects(DICI.Location, SKOS.altLabel)}
    assert "Site" in alt_labels, f"Location lost its 'Site' synonym; altLabels: {alt_labels}"


def test_legacy_annotation_properties_bridge_to_skos():
    g = _load_core()
    assert (DICI.definition, RDFS.subPropertyOf, SKOS.definition) in g
    assert (DICI.Synonymous, RDFS.subPropertyOf, SKOS.altLabel) in g
    assert (DICI.abbreviation, RDFS.subPropertyOf, SKOS.altLabel) in g


def test_term_index_is_fresh(tmp_path):
    """docs/term-index.{json,md} must match a regeneration from the TTL."""
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools" / "generate_term_index.py"), "--out", str(tmp_path)],
        check=True,
        capture_output=True,
    )
    for fname in ("term-index.json", "term-index.md"):
        committed = (DOCS_DIR / fname).read_text(encoding="utf-8")
        regenerated = (tmp_path / fname).read_text(encoding="utf-8")
        assert committed == regenerated, (
            f"docs/{fname} is stale — run `python tools/generate_term_index.py` and commit the result"
        )


def test_term_index_json_shape():
    payload = json.loads((DOCS_DIR / "term-index.json").read_text(encoding="utf-8"))
    terms = {t["name"]: t for t in payload["terms"]}
    assert len(terms) > 200
    loc = terms["Location"]
    assert "Site" in loc["altLabels"]
    assert loc["parentChainToRoot"] == ["Component"]
    assert terms["Turbine"]["parentChainToRoot"] == ["EnergyConverter", "Converter", "Component"]

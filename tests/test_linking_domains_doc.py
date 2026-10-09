"""docs/LINKING_DOMAINS.md only names Digicities terms that exist in the core.

The page's worked examples put a core class on the Digicities side of every
mapping. If a class is renamed or removed in a later core release, this test
fails and the page is updated with it. Its Turtle and SPARQL blocks must parse.
"""

import re
from pathlib import Path

import rdflib
from rdflib.namespace import OWL, RDF

ROOT = Path(__file__).parent.parent
CORE_TTL = ROOT / "core" / "dici_onto_core.ttl"
DOC = ROOT / "docs" / "LINKING_DOMAINS.md"
DICI = "https://digicities.info/ontology#"

_TERM = re.compile(r"\bdici_onto:([A-Za-z][A-Za-z0-9_]*)")
_BLOCK = re.compile(r"```(turtle|sparql)\n(.*?)```", re.S)


def _core_terms() -> set:
    g = rdflib.Graph().parse(CORE_TTL, format="turtle")
    kinds = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
    return {str(s)[len(DICI):] for kind in kinds for s in g.subjects(RDF.type, kind)
            if str(s).startswith(DICI)}


def test_every_digicities_term_on_the_page_is_in_the_core():
    named = set(_TERM.findall(DOC.read_text(encoding="utf-8")))
    assert named, "the page names no dici_onto: terms"
    missing = sorted(named - _core_terms())
    assert not missing, f"LINKING_DOMAINS.md names terms not in core: {missing}"


def test_the_pages_code_blocks_parse():
    blocks = _BLOCK.findall(DOC.read_text(encoding="utf-8"))
    assert {lang for lang, _ in blocks} == {"turtle", "sparql"}
    for lang, body in blocks:
        if lang == "turtle":
            rdflib.Graph().parse(data=body, format="turtle")
        else:
            rdflib.Graph().query(body)

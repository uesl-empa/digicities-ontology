"""The core is built, not edited: these tests hold the build to its promises.

- the committed ``core/dici_onto_core.ttl`` is exactly what ``tools/build_core.py``
  produces from ``core/bare_core.ttl`` + ``core/scaffold_instructions.json``;
- the core follows the Entity-Attribute-Relation pattern (the platform's
  ``check_pattern`` finds nothing);
- no term of the previous release disappears silently: it is still there, a
  deprecated alias of its replacement, or listed as removed in the CHANGELOG;
- labels and comments of the terms that stayed are unchanged;
- README, ``owl:versionInfo`` and the CHANGELOG name the same version.

The build and pattern tests need a digicities-platform checkout (the Ontology
Manager lives there): set ``DIGICITIES_PLATFORM_DIR``. Without it they skip and
say so; CI sets it.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest
import rdflib
from rdflib import OWL, RDF, RDFS, URIRef
from rdflib.compare import isomorphic, graph_diff

REPO_ROOT = Path(__file__).parent.parent
CORE_TTL = REPO_ROOT / "core" / "dici_onto_core.ttl"
DICI = rdflib.Namespace("https://digicities.info/ontology#")
ONTOLOGY_IRI = URIRef("https://digicities.info/ontology")
# The release before the scaffold was built through the Ontology Manager.
PREVIOUS_RELEASE = "cae6166"
# Terms of the previous release removed on purpose (no replacement exists).
REMOVED = {DICI.hasEnergyCarrierEnergyCostAttribute}

PLATFORM = os.environ.get("DIGICITIES_PLATFORM_DIR")
needs_platform = pytest.mark.skipif(
    not PLATFORM, reason="set DIGICITIES_PLATFORM_DIR to a digicities-platform checkout")


def _core() -> rdflib.Graph:
    return rdflib.Graph().parse(CORE_TTL, format="turtle")


def _previous() -> rdflib.Graph:
    try:
        text = subprocess.run(
            ["git", "show", f"{PREVIOUS_RELEASE}:core/dici_onto_core.ttl"], cwd=REPO_ROOT,
            capture_output=True, text=True, encoding="utf-8", check=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        pytest.skip(f"previous release {PREVIOUS_RELEASE} not in this clone ({e}); "
                    "fetch the full history")
    return rdflib.Graph().parse(data=text, format="turtle")


def _terms(g: rdflib.Graph):
    return {s for t in (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty,
                        OWL.AnnotationProperty)
            for s in g.subjects(RDF.type, t)
            if isinstance(s, URIRef) and s.startswith(str(DICI))}


@needs_platform
def test_build_reproduces_the_committed_core(tmp_path):
    sys.path.insert(0, str(REPO_ROOT / "tools"))
    from build_core import build
    built = build(tmp_path / "core.ttl", PLATFORM)
    committed = _core()
    if not isomorphic(built, committed):
        _, only_built, only_committed = graph_diff(built, committed)
        pytest.fail("the committed core is not what the build produces; run "
                    "tools/build_core.py.\nonly in the build: "
                    + "\n".join(map(str, list(only_built)[:10]))
                    + "\nonly committed: " + "\n".join(map(str, list(only_committed)[:10])))


@needs_platform
def test_core_follows_the_pattern():
    if PLATFORM not in sys.path:
        sys.path.insert(0, PLATFORM)
    from backend.ontology_scaffold import check_pattern
    assert check_pattern(_core()) == []


def test_no_term_of_the_previous_release_disappears_silently():
    old, new = _previous(), _core()
    gone = []
    for term in sorted(_terms(old) - _terms(new)):
        if term in REMOVED:
            continue
        gone.append(term)
    assert not gone, f"terms gone without a deprecated alias: {gone}"
    already = set(old.subjects(OWL.deprecated, None))
    for alias in set(new.subjects(OWL.deprecated, None)) - already:
        targets = set(new.objects(alias, OWL.equivalentClass)) \
            | set(new.objects(alias, OWL.equivalentProperty))
        assert len(targets) == 1, f"{alias} must point at exactly one replacement"
        assert next(iter(targets)) in _terms(new), f"{alias} points at a missing term"


def test_labels_and_comments_of_kept_terms_are_unchanged():
    old, new = _previous(), _core()
    deprecated = set(new.subjects(OWL.deprecated, None))
    changed = []
    for term in sorted((_terms(old) & _terms(new)) - deprecated):
        for prop in (RDFS.label, RDFS.comment):
            if set(old.objects(term, prop)) != set(new.objects(term, prop)):
                changed.append(f"{term} {prop}")
    assert not changed, "annotations changed:\n" + "\n".join(changed)


def test_version_is_the_same_everywhere():
    g = _core()
    versions = {str(v) for v in g.objects(ONTOLOGY_IRI, OWL.versionInfo)}
    assert len(versions) == 1, f"owl:versionInfo: {versions}"
    version = versions.pop()
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    first = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.M)
    assert first and first.group(1) == version, \
        f"CHANGELOG's latest release {first and first.group(1)} != owl:versionInfo {version}"
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    named = set(re.findall(r"\bv(\d+\.\d+\.\d+)\b", readme))
    assert named == {version}, f"README names {named}, the core is {version}"

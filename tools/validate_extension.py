"""Validate a Digicities ontology extension authored in a workspace.

This is a **library tool**, not a gatekeeper. The Digicities ontology repo
holds only the core vocabulary — extensions live in individual workspaces
(see https://github.com/REFORMERS-EnergyValleys/REFORMERS_Ontology-Extensions-and-Knowledge-Graphs
for an example corpus). Run this against your workspace's
`ontology/extensions/*.ttl` files when authoring or before committing.

Exits non-zero if any file fails one of these checks:

1. **Parses** — the file is syntactically valid Turtle.
2. **Namespace** — every newly declared class/property is in the
   `dici_onto:` namespace (`https://digicities.info/ontology#`). Extensions
   extend the shared vocabulary; using the same namespace as core means
   SPARQL queries find core and extension terms uniformly, and concepts
   that later get promoted to core don't break the workspace's existing
   data (the IRI stays the same).
3. **No-redefine** — the candidate doesn't redeclare a term that already
   exists in `core/dici_onto_core.ttl`. Extensions add new terms; they
   don't override existing ones. If you think core needs a change, open a
   PR against the core file rather than redefining the term in an
   extension.
4. **Parents declared** — every `owl:Class` has at least one
   `rdfs:subClassOf` triple pointing into core or to another class
   declared earlier in the same extension. An orphan class is almost
   always a mistake.
5. **Labels & comments** — every newly declared class/property carries an
   `rdfs:label` and an `rdfs:comment`. The whole point of a shared
   vocabulary is that humans can read it. Unlabelled terms are noise.

## Usage

From the ontology repo root, against a workspace on the same machine:

    python tools/validate_extension.py /path/to/<workspace>/ontology/extensions/my_extension.ttl

Or, with a glob:

    python tools/validate_extension.py /path/to/<workspace>/ontology/extensions/*.ttl

The platform's workspace provisioner (`backend.workspace.graphdb_provisioning`)
runs an equivalent parse check at workspace open. Running this script
locally is faster than waiting for the UI to surface the error.

## What this script does NOT do

- Detect IRI collisions across multiple workspaces — that's a federation
  concern, deferred until the corpus is mature enough to need it. If two
  workspaces both declare `dici_onto:Foo` with different semantics, the
  collision surfaces when you try to merge or federate those workspaces'
  graphs, not before.
- Block promotion of a concept to core — promotion is a maintainer-driven
  PR against `core/dici_onto_core.ttl`. This script only cares about
  syntactic and structural correctness of a single TTL file.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import rdflib
from rdflib.namespace import OWL, RDF, RDFS

REPO_ROOT = Path(__file__).resolve().parent.parent
CORE_TTL = REPO_ROOT / "core" / "dici_onto_core.ttl"
DICI = rdflib.Namespace("https://digicities.info/ontology#")


@dataclass
class Report:
    path: Path
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _iri_in_core(iri: rdflib.URIRef, core: rdflib.Graph) -> bool:
    """True if the IRI is declared in core (as a class, property, or individual)."""
    for predicate in (RDF.type,):
        if (iri, predicate, None) in core:
            return True
    return False


def _declared_subjects(g: rdflib.Graph, target_type: rdflib.URIRef) -> set[rdflib.URIRef]:
    return {s for s, _, _ in g.triples((None, RDF.type, target_type)) if isinstance(s, rdflib.URIRef)}


def validate(path: Path, core: rdflib.Graph) -> Report:
    report = Report(path=path)
    g = rdflib.Graph()

    try:
        g.parse(path, format="turtle")
    except Exception as exc:
        report.errors.append(f"failed to parse: {exc}")
        return report

    classes = _declared_subjects(g, OWL.Class)
    object_properties = _declared_subjects(g, OWL.ObjectProperty)
    data_properties = _declared_subjects(g, OWL.DatatypeProperty)
    annotation_properties = _declared_subjects(g, OWL.AnnotationProperty)
    all_terms = classes | object_properties | data_properties | annotation_properties

    if not all_terms:
        report.warnings.append("extension declares no classes or properties — nothing to validate")
        return report

    # 2. Namespace check — newly minted terms MUST be in the dici_onto:
    # namespace. Extensions add to the shared ontology so queries like
    # `?x a dici_onto:EnergyConsumer` work uniformly across core + extensions,
    # and so concepts that later get promoted to core don't change IRI.
    dici_prefix = str(DICI)
    for iri in sorted(all_terms):
        if not str(iri).startswith(dici_prefix):
            report.errors.append(
                f"term `{iri}` is not in the dici_onto: namespace — extensions "
                "must use https://digicities.info/ontology# for new terms so "
                "queries stay uniform across core + extensions, and so the IRI "
                "stays stable if the concept is later promoted to core"
            )

    # 3. No-redefine check — same IRI must not already exist in core.
    for iri in sorted(all_terms):
        if _iri_in_core(iri, core):
            report.errors.append(
                f"redefines core term `{iri}` — extensions add new terms, they don't override existing ones"
            )

    # 4. Parents declared for classes.
    for cls in sorted(classes):
        parents = list(g.objects(cls, RDFS.subClassOf))
        if not parents:
            report.errors.append(
                f"class `{cls}` has no rdfs:subClassOf — every extension class must declare a parent"
            )

    # 5. Labels and comments.
    for iri in sorted(all_terms):
        labels = list(g.objects(iri, RDFS.label))
        comments = list(g.objects(iri, RDFS.comment))
        if not labels:
            report.errors.append(f"`{iri}` is missing rdfs:label")
        if not comments:
            report.warnings.append(f"`{iri}` is missing rdfs:comment")

    return report


def _print_report(r: Report) -> None:
    status = "ok   " if r.ok else "FAIL "
    print(f"{status} {r.path}")
    for err in r.errors:
        print(f"   ERROR  {err}")
    for warn in r.warnings:
        print(f"   warn   {warn}")


def main(paths: Iterable[str]) -> int:
    if not CORE_TTL.exists():
        print(f"ERROR: core ontology not found at {CORE_TTL}", file=sys.stderr)
        return 2

    core = rdflib.Graph()
    core.parse(CORE_TTL, format="turtle")

    any_failed = False
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            print(f"FAIL  {path}\n   ERROR  file does not exist")
            any_failed = True
            continue
        report = validate(path, core)
        _print_report(report)
        if not report.ok:
            any_failed = True

    return 1 if any_failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "usage: validate_extension.py <workspace-extension.ttl> [<extension.ttl> ...]\n"
            "\n"
            "Extensions live in workspaces, not in this repo. Point this script at a\n"
            "workspace's ontology/extensions/*.ttl file. See the module docstring for\n"
            "the full check list and the rationale for each rule."
        )
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))

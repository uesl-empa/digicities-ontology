"""Generate the agent-facing term index from the Digicities ontology.

Reads the core ontology (plus any workspace extension TTLs passed on the
command line) and emits two derived artifacts under ``docs/``:

- **term-index.json** — one record per ``dici_onto:`` term with everything
  an agent needs to map a domain concept onto the vocabulary: label,
  parent chain to the root, description, definition, synonyms
  (``skos:altLabel``), examples, scope notes, domain/range for properties,
  and default unit / quantity kind for attribute classes.
- **term-index.md** — the same data as a greppable card catalog, grouped
  by hierarchy.

These files are **generated — never edit them by hand**. The TTL is the
single source of truth; regenerate after any change to core:

    python tools/generate_term_index.py

To build a *combined* index for a workspace (core + its extensions), pass
the extension files and an output directory:

    python tools/generate_term_index.py --out /path/to/workspace/docs \\
        /path/to/workspace/ontology/extensions/*.ttl

Output is deterministic (sorted by IRI) so CI can regenerate and diff to
catch a stale committed index.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import rdflib
from rdflib.namespace import OWL, RDF, RDFS, SKOS

REPO_ROOT = Path(__file__).resolve().parent.parent
CORE_TTL = REPO_ROOT / "core" / "dici_onto_core.ttl"
DOCS_DIR = REPO_ROOT / "docs"

DICI = rdflib.Namespace("https://digicities.info/ontology#")

KINDS = {
    OWL.Class: "class",
    OWL.ObjectProperty: "objectProperty",
    OWL.DatatypeProperty: "dataProperty",
    OWL.AnnotationProperty: "annotationProperty",
}

GENERATED_NOTE = (
    "GENERATED FILE - do not edit. Regenerate with: python tools/generate_term_index.py"
)


def _local(iri: rdflib.URIRef) -> str:
    s = str(iri)
    return s.split("#")[-1] if "#" in s else s.rsplit("/", 1)[-1]


def _literals(g: rdflib.Graph, s: rdflib.URIRef, p: rdflib.URIRef) -> list[str]:
    return sorted({str(o) for o in g.objects(s, p) if isinstance(o, rdflib.Literal)})


def _first(g: rdflib.Graph, s: rdflib.URIRef, p: rdflib.URIRef) -> str | None:
    vals = _literals(g, s, p)
    return vals[0] if vals else None


def _uri_objects(g: rdflib.Graph, s: rdflib.URIRef, p: rdflib.URIRef) -> list[str]:
    return sorted({str(o) for o in g.objects(s, p) if isinstance(o, rdflib.URIRef)})


def _parent_chain(g: rdflib.Graph, s: rdflib.URIRef, pred: rdflib.URIRef) -> list[str]:
    """Follow the first URI parent transitively to the root; cycle-safe."""
    chain: list[str] = []
    seen = {s}
    node = s
    while True:
        parents = [o for o in g.objects(node, pred) if isinstance(o, rdflib.URIRef) and o not in seen]
        # prefer dici_onto: parents so the chain stays inside the vocabulary
        parents.sort(key=lambda o: (not str(o).startswith(str(DICI)), str(o)))
        if not parents:
            return chain
        node = parents[0]
        seen.add(node)
        chain.append(_local(node))
        if len(chain) > 30:  # defensive; hierarchy is shallow
            return chain


def build_records(g: rdflib.Graph) -> list[dict]:
    records = []
    for rdf_type, kind in KINDS.items():
        for s in g.subjects(RDF.type, rdf_type):
            if not (isinstance(s, rdflib.URIRef) and str(s).startswith(str(DICI))):
                continue
            hier_pred = RDFS.subClassOf if kind == "class" else RDFS.subPropertyOf
            parents = [
                _local(o)
                for o in g.objects(s, hier_pred)
                if isinstance(o, rdflib.URIRef)
            ]
            definitions = _literals(g, s, SKOS.definition) + _literals(g, s, DICI.definition)
            rec = {
                "iri": str(s),
                "name": _local(s),
                "kind": kind,
                "label": _first(g, s, RDFS.label),
                "parents": sorted(parents),
                "parentChainToRoot": _parent_chain(g, s, hier_pred),
                "comment": _first(g, s, RDFS.comment),
                "definition": definitions[0] if definitions else None,
                "altLabels": sorted(
                    set(_literals(g, s, SKOS.altLabel) + _literals(g, s, DICI.Synonymous))
                ),
                "examples": _literals(g, s, SKOS.example),
                "scopeNote": _first(g, s, SKOS.scopeNote),
            }
            if kind in ("objectProperty", "dataProperty"):
                rec["domain"] = [_local(rdflib.URIRef(u)) for u in _uri_objects(g, s, RDFS.domain)]
                rec["range"] = [_local(rdflib.URIRef(u)) for u in _uri_objects(g, s, RDFS.range)]
            if kind == "class":
                unit = _uri_objects(g, s, DICI.hasDefaultUnit)
                qk = _uri_objects(g, s, DICI.hasQuantityKind)
                if unit:
                    rec["defaultUnit"] = _local(rdflib.URIRef(unit[0]))
                if qk:
                    rec["quantityKind"] = _local(rdflib.URIRef(qk[0]))
            records.append(rec)
    records.sort(key=lambda r: (r["kind"], r["iri"]))
    return records


def render_markdown(records: list[dict]) -> str:
    lines = [
        "# Digicities term index",
        "",
        f"<!-- {GENERATED_NOTE} -->",
        "",
        "One card per term in the `dici_onto:` namespace, generated from the",
        "ontology TTL. Use this file to map a domain concept onto the existing",
        "vocabulary: grep for your concept's name and its synonyms, then check",
        "the parent chain, examples and scope notes before deciding a parent",
        "class. See [`AGENT_MAPPING_GUIDE.md`](AGENT_MAPPING_GUIDE.md) for the",
        "mapping procedure.",
        "",
    ]
    sections = [
        ("class", "Classes"),
        ("objectProperty", "Object properties"),
        ("dataProperty", "Data properties"),
        ("annotationProperty", "Annotation properties"),
    ]
    for kind, title in sections:
        subset = [r for r in records if r["kind"] == kind]
        if not subset:
            continue
        lines += [f"## {title}", ""]
        for r in subset:
            chain = " > ".join(reversed(r["parentChainToRoot"])) if r["parentChainToRoot"] else "(root)"
            lines.append(f"### {r['name']}")
            lines.append("")
            if r["label"]:
                lines.append(f"- **Label:** {r['label']}")
            lines.append(f"- **Hierarchy:** {chain} > **{r['name']}**" if chain != "(root)" else "- **Hierarchy:** (root)")
            if r["comment"]:
                lines.append(f"- **Description:** {r['comment']}")
            if r["definition"]:
                lines.append(f"- **Definition:** {r['definition']}")
            if r["altLabels"]:
                lines.append(f"- **Synonyms:** {', '.join(r['altLabels'])}")
            if r["examples"]:
                for ex in r["examples"]:
                    lines.append(f"- **Examples:** {ex}")
            if r["scopeNote"]:
                lines.append(f"- **Scope:** {r['scopeNote']}")
            if r.get("domain"):
                lines.append(f"- **Domain:** {', '.join(r['domain'])}")
            if r.get("range"):
                lines.append(f"- **Range:** {', '.join(r['range'])}")
            if r.get("defaultUnit"):
                lines.append(f"- **Default unit:** {r['defaultUnit']}")
            if r.get("quantityKind"):
                lines.append(f"- **Quantity kind:** {r['quantityKind']}")
            lines.append("")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("extensions", nargs="*", help="optional workspace extension TTLs to merge with core")
    parser.add_argument("--out", type=Path, default=DOCS_DIR, help="output directory (default: docs/)")
    args = parser.parse_args(argv)

    g = rdflib.Graph()
    g.parse(CORE_TTL, format="turtle")
    for ext in args.extensions:
        g.parse(ext, format="turtle")

    records = build_records(g)

    args.out.mkdir(parents=True, exist_ok=True)
    json_path = args.out / "term-index.json"
    md_path = args.out / "term-index.md"

    payload = {"_note": GENERATED_NOTE, "terms": records}
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    md_path.write_text(render_markdown(records), encoding="utf-8", newline="\n")

    print(f"wrote {json_path} ({len(records)} terms)")
    print(f"wrote {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

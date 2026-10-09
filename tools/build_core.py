"""Build core/dici_onto_core.ttl from its two sources.

The core is not edited by hand. It is built by replaying
``core/scaffold_instructions.json`` through the Digicities platform's Ontology
Manager (the same executor that builds every workspace extension) onto
``core/bare_core.ttl``:

- ``bare_core.ttl`` holds what is authored by hand: the top classes and
  branches, ``Component`` itself, ``Attribute`` and the value kinds,
  ``ComponentAttribute``, ``hasAttribute`` / ``hasComponentAttribute`` /
  ``hasIdentifier``, the ``linksComponent`` tree, the value and datatype
  properties, units and individuals.
- ``scaffold_instructions.json`` adds every component class, in hierarchy
  order, with its annotations. The Ontology Manager gives each its category
  (``<X>Attribute``) and general predicate (``has<X>Attribute``, range = the
  category), links the core's attributes, and keeps deprecated aliases for
  renamed terms.

So the core follows the Entity-Attribute-Relation pattern by construction,
exactly as an extension does.

Usage::

    DIGICITIES_PLATFORM_DIR=/path/to/digicities-platform python tools/build_core.py
    python tools/build_core.py --platform /path/to/digicities-platform --out other.ttl

A refused instruction fails the build with the executor's reasons.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

import rdflib

REPO_ROOT = Path(__file__).resolve().parent.parent
BARE_CORE = REPO_ROOT / "core" / "bare_core.ttl"
INSTRUCTIONS = REPO_ROOT / "core" / "scaffold_instructions.json"
CORE_TTL = REPO_ROOT / "core" / "dici_onto_core.ttl"


class BuildError(RuntimeError):
    """An instruction was refused, or the platform could not be found."""


def _platform_dir(given: str | None) -> Path:
    found = given or os.environ.get("DIGICITIES_PLATFORM_DIR")
    if not found:
        raise BuildError("the platform checkout is needed to build the core: pass --platform "
                         "or set DIGICITIES_PLATFORM_DIR")
    path = Path(found).resolve()
    if not (path / "backend" / "ontology_manager" / "instructions.py").is_file():
        raise BuildError(f"{path} is not a digicities-platform checkout")
    return path


def build(out: Path = CORE_TTL, platform: str | None = None) -> rdflib.Graph:
    """Replay the instructions onto the bare core; write and return the result."""
    platform_dir = _platform_dir(platform)
    if str(platform_dir) not in sys.path:
        sys.path.insert(0, str(platform_dir))
    with tempfile.TemporaryDirectory() as tmp:
        core_dir = Path(tmp) / "core"
        core_dir.mkdir()
        shutil.copy(BARE_CORE, core_dir / "dici_onto_core.ttl")
        previous = os.environ.get("ONTOLOGY_DIR")
        os.environ["ONTOLOGY_DIR"] = str(core_dir)
        try:
            from backend.ontology_manager.instructions import apply_extension_instructions
            from backend.workspace.storage import WorkspaceStorage

            workspace = Path(tmp) / "workspace"
            workspace.mkdir()
            report = apply_extension_instructions(
                json.loads(INSTRUCTIONS.read_text(encoding="utf-8")),
                storage=WorkspaceStorage.local(str(workspace)), upload=False)
        finally:
            if previous is None:
                os.environ.pop("ONTOLOGY_DIR", None)
            else:
                os.environ["ONTOLOGY_DIR"] = previous
        refused = [r for r in report["results"] if r["status"] != "applied"]
        if refused:
            raise BuildError("instructions not applied:\n" + "\n".join(
                f"  {r['op']} {r['target']}: {r['status']} {r['message']}" for r in refused))
        built = rdflib.Graph()
        built.parse(core_dir / "dici_onto_core.ttl", format="turtle")
    bare = rdflib.Graph().parse(BARE_CORE, format="turtle")
    for prefix, ns in bare.namespaces():
        built.bind(prefix, ns, override=True)
    built.serialize(out, format="turtle")
    return built


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--platform", help="digicities-platform checkout (or DIGICITIES_PLATFORM_DIR)")
    ap.add_argument("--out", type=Path, default=CORE_TTL, help="where to write the core")
    args = ap.parse_args()
    # The platform's progress lines carry symbols a Windows console code page lacks.
    sys.stdout.reconfigure(errors="backslashreplace")
    try:
        g = build(args.out, args.platform)
    except BuildError as e:
        print(e, file=sys.stderr)
        return 1
    print(f"built {args.out} ({len(g)} triples)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

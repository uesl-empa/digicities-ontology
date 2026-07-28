# Digicities ontology

An open OWL/RDF ontology (CC BY 4.0) for describing **anything as a component with attributes** aiming to connect those who publish, model or build services requiring data about those things.

Its core commitment is deliberately general: whatever you're describing, e.g. a building, a turbine, a district, a sensor, a market, a material, a process, is a *modelled as a component with attributes*. Because every party names the world the same way, the ontology becomes a shared language across a whole value chain:

- **Data publishers** describe things and release trustworthy, self-describing data about them.
- **Modelers** assemble those same things into digital replicas of real systems.
- **Developers** specify requirements and build services that act on them.

Define a thing once, and it can be published, replicated, and built upon without translation at each handoff — so value flows along the chain instead of stalling between the people who produce data, model it, and put it to work. Energy systems are where this began and where it's proven, not the boundary.

Concretely, the ontology defines a small set of upper-level classes (`Component`, `Process`, `Flow`, `Resource`, `Network`, `Location`, ...), a domain vocabulary (energy carriers, converters, storage, sensors, meters, controllers), and the **15 attribute types** used to attach values to instances (physical, cost, categorical, event, geospatial, time-series, ...). It's the schema layer that powers the [Digicities platform](https://github.com/uesl-empa/digicities-platform), but the TTL is usable standalone with any RDF tool.

## Structure

```
core/
├── dici_onto_core.ttl   # the ontology itself (~2.7k lines, ~143 classes)
└── qudt_units.txt       # QUDT unit list referenced by Physical/Cost attributes
docs/
├── overview.md          # scope, design principles, namespaces
├── attribute-types.md   # the 15 attribute-type classes and what they model
├── class-hierarchy.md   # full class list grouped by upper concept
├── CORE_EVOLUTION.md    # how workspace extensions become core
├── AGENT_MAPPING_GUIDE.md  # mapping procedure + decision tree for onboarding agents
├── term-index.json      # generated agent-facing term lookup (labels, comments, SKOS)
└── term-index.md        # human-readable rendering of the term index
tools/
├── validate_extension.py    # library for partners to validate their workspace's extensions
└── generate_term_index.py   # regenerates docs/term-index.{json,md} from the TTL
tests/
├── test_parses.py       # rdflib smoke parse + sanity-check triple count
└── test_annotations.py  # annotation coverage + stale-term-index guard
```

## Managing Ontology Extensions

This repo holds **only the core ontology**, versioned and released. Extensions (new classes and properties your project needs) are authored in the Digicities workspace that uses them, in the workspace's own `ontology/extensions/*.ttl` files and also the workspace graph. Extensions use the same `dici_onto:` namespace as core. Two reasons:

- SPARQL queries find core and extension terms uniformly. No UNION over multiple namespaces.
- Concepts that later get promoted into core don't change IRI. Workspace data and queries keep working unchanged.

See [`docs/CORE_EVOLUTION.md`](docs/CORE_EVOLUTION.md) for the full model: the three-stage workspace → multi-workspace → core lifecycle, the service compatibility contract, and what's deferred until the corpus matures.

When you've drafted an extension TTL in your workspace, validate it locally:

```bash
python tools/validate_extension.py /path/to/<workspace>/ontology/extensions/<your_extension>.ttl
```

(The platform's workspace provisioner runs an equivalent parse check at workspace open. Running the script locally is faster.)

## Quick start (Python / rdflib)

```bash
pip install rdflib
```

```python
import rdflib
g = rdflib.Graph()
g.parse("core/dici_onto_core.ttl", format="turtle")
print(len(g), "triples")
```

## Quick start

Drop `core/dici_onto_core.ttl` into your triplestore as a named graph. The platform uses `<http://classes_and_attributes>`. The ontology declares itself as `<https://digicities.info/ontology>` and uses the `dici_onto:` prefix (`https://digicities.info/ontology#`).

## Namespace

Canonical prefix: `dici_onto: <https://digicities.info/ontology#>`

The ontology re-uses QUDT for units and quantity kinds (`http://qudt.org/schema/qudt/`, `http://qudt.org/vocab/unit/`) and QUDT currencies (`http://qudt.org/vocab/currency/`) for monetary values.

## Versioning

Semver. The current release is **v0.2.0**, the annotation release: every term carries `rdfs:label` + `rdfs:comment` (mapping-decision classes also SKOS annotations), the TTL declares `owl:versionInfo`, and the generated `docs/term-index.{json,md}` gives agents a lookup surface. See [`CHANGELOG.md`](CHANGELOG.md).

Downstream consumers (notably the Digicities platform) vendor a tagged copy of `core/dici_onto_core.ttl` rather than depending on this repo at build time. The platform records the vendored version in its own `services/graphdb/ontology/VERSION` file.

## Contributing

Issues and PRs welcome. For new classes or attribute types, please:

1. Add a clear `rdfs:label` and `rdfs:comment` in English.
2. Pick the right parent class. Most domain classes inherit from `Component`, `Process`, `Flow`, or `Resource`.
3. Run `pytest` to confirm the file still parses.

## Funding & acknowledgements

Digicities was funded through the SFOE P+D program under the ERA-Net Smart Energy Systems joint initiative *Digital Transformation for the Energy Transition*, grant agreement No 88397.

The authors thank all Digicities project collaborators and contributors who helped guide the development of the platform and the ontology.

The open-source release of this project (repository split, license audit, CI scaffolding, deployment documentation) was prepared with the assistance of [Claude Code](https://claude.com/claude-code).

## How to cite

If you use the Digicities ontology in published work, please cite it:

```bibtex
@dataset{digicities-ontology,
  title  = {Digicities Ontology},
  author = {Allan, James},
  year   = {2026},
  url    = {https://github.com/uesl-empa/digicities-ontology},
}
```

Or in prose: *"... modelled using the Digicities ontology (https://github.com/uesl-empa/digicities-ontology)."*

If you also use the platform, please cite it separately. See [`digicities-platform`](https://github.com/uesl-empa/digicities-platform#how-to-cite).

## License

[Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may use, redistribute, and adapt the ontology for any purpose, including commercial, as long as you give appropriate credit.

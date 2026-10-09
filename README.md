# Digicities ontology

Digicities is a requirements-driven semantic layer that connects models to the data they need: each model states its inputs as requirements against a shared ontology, and the platform finds, checks and delivers that data from a knowledge graph.

This repository holds that shared ontology (OWL/RDF, CC BY 4.0). It is the vocabulary both sides use. People who hold data describe their system with it, as components with attributes: a building, a turbine, a district, a sensor, a process. People who build models state what their model needs in the same terms, for example `WindTurbine.HubHeight`. Because both sides use the same terms, the [Digicities platform](https://github.com/uesl-empa/digicities-platform) can match a model's requirements to the data without a hand-written translation for each pair.

Concretely, the ontology defines a small set of upper-level classes (`Component`, `Process`, `Flow`, `Resource`, `Network`, `Location`, ...), a domain vocabulary (energy carriers, converters, storage, sensors, meters, controllers), and the attribute types used to attach values to instances (physical, cost, categorical, event, curve, data path, identifier, ...; see [`docs/attribute-types.md`](docs/attribute-types.md)). Energy systems are where it started, not its limit. The TTL works on its own with any RDF tool.

## Structure

```
core/
├── dici_onto_core.ttl          # the ontology itself: BUILT, never edited by hand
├── bare_core.ttl               # the hand-authored part (top classes, value kinds, link and value properties)
├── scaffold_instructions.json  # Ontology Manager ops that add every component class and its scaffold
└── qudt_units.txt              # QUDT unit list referenced by Physical/Cost attributes
docs/
├── overview.md          # scope, design principles, namespaces
├── attribute-types.md   # the attribute-type classes and what they model
├── class-hierarchy.md   # full class list grouped by upper concept
├── CORE_EVOLUTION.md    # how workspace extensions become core
├── AGENT_MAPPING_GUIDE.md  # mapping procedure + decision tree for onboarding agents
├── term-index.json      # generated agent-facing term lookup (labels, comments, SKOS)
└── term-index.md        # human-readable rendering of the term index
tools/
├── build_core.py            # builds core/dici_onto_core.ttl through the platform's Ontology Manager
├── validate_extension.py    # library for partners to validate their workspace's extensions
└── generate_term_index.py   # regenerates docs/term-index.{json,md} from the TTL
tests/
├── test_parses.py       # rdflib smoke parse + sanity-check triple count
├── test_annotations.py  # annotation coverage + stale-term-index guard
├── test_build_core.py   # rebuild == committed core; the pattern holds; versions agree
└── test_inverses.py     # no two properties share an inverse
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

Drop `core/dici_onto_core.ttl` into your triplestore as a named graph. The platform loads it (with the workspace's extensions) into `<http://ontology_dici_onto>`; instance data goes to `<http://classes_and_attributes>`. The ontology declares itself as `<https://digicities.info/ontology>` and uses the `dici_onto:` prefix (`https://digicities.info/ontology#`).

## Namespace

Canonical prefix: `dici_onto: <https://digicities.info/ontology#>`

The ontology re-uses QUDT for units and quantity kinds (`http://qudt.org/schema/qudt/`, `http://qudt.org/vocab/unit/`), QUDT currencies (`http://qudt.org/vocab/currency/`) for monetary values, SKOS for mapping annotations, PROV-O for the one provenance link it has today (`derivedFromCatalogue`), and Dublin Core terms for its own metadata. The full table is in [`docs/overview.md`](docs/overview.md#namespaces).

## Versioning

Semver. The current release is **v0.6.0**, the scaffold release: the core is built by replaying `core/scaffold_instructions.json` through the Digicities platform's Ontology Manager onto `core/bare_core.ttl`, so every component class has its category and general predicate by construction (range = the category), exactly like a workspace extension. Renamed terms stay one release as `owl:deprecated` aliases. See [`CHANGELOG.md`](CHANGELOG.md).

To change the core, edit `bare_core.ttl` or `scaffold_instructions.json`, then rebuild:

```
DIGICITIES_PLATFORM_DIR=/path/to/digicities-platform python tools/build_core.py
```

`tests/test_build_core.py` fails when the committed core differs from what the build produces.

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
  title   = {Digicities Ontology},
  author  = {Allan, James},
  year    = {2026},
  version = {0.6.0},
  url     = {https://github.com/uesl-empa/digicities-ontology},
}
```

The same metadata is in [`CITATION.cff`](CITATION.cff) ("Cite this repository" on GitHub). A Zenodo DOI per release will be added once the Zenodo integration is enabled for this repository.

Or in prose: *"... modelled using the Digicities ontology (https://github.com/uesl-empa/digicities-ontology)."*

If you also use the platform, please cite it separately. See [`digicities-platform`](https://github.com/uesl-empa/digicities-platform#how-to-cite).

## License

[Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may use, redistribute, and adapt the ontology for any purpose, including commercial, as long as you give appropriate credit.

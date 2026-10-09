# Ontology overview

Digicities is a requirements-driven semantic layer that connects models to the data they need: each model states its inputs as requirements against a shared ontology, and the platform finds, checks and delivers that data from a knowledge graph.

The Digicities ontology (`dici_onto:`) is that shared ontology. Data holders use it to describe their systems as components with attributes (a replica). Model builders use it to state what their model needs. The [Digicities platform](https://github.com/uesl-empa/digicities-platform) matches the two. Energy systems in districts, neighbourhoods and buildings are where it started, and most of its domain vocabulary comes from there.

## Scope

What the ontology covers:

- **Physical infrastructure**: components (energy converters, storage, sensors, meters, controllers, actuators, switches, valves, junctions) and the networks that connect them.
- **Energy and material flows**: electricity, heat, gas, liquid fuels, solid fuels, materials, with carrier-specific subclasses.
- **Resources**: renewable and non-renewable, including solar and wind.
- **Processes**: conversion, storage, transport.
- **Location and geospatial context**: instances can be located in a `Location` and carry `GeospatialAttribute`s.
- **Time-series data**: historic, live, and future series, attached to any attribute.
- **Costs**: simple monetary values and per-unit costs, in any QUDT currency.
- **Provenance**: today one link. `derivedFromCatalogue` (a sited instance to the catalogue entry it was specified from) is a sub-property of `prov:wasDerivedFrom`. References to sources (`Reference`, `ReferenceType`) exist as classes, but the core has no dedicated provenance property for them yet. Note that `hasSource` is not provenance: it is the flow property (the component a `Flow` comes from). A separate provenance property (`hasReference` under `prov:wasDerivedFrom`) is planned.
- **Scenarios and assumptions**: first-class classes for what-if analysis.
- **Services and their configuration**: the models that consume scenarios, and the settings they run with (`ServiceConfiguration` profiles of `ConfigurationAttribute` values). A value that sets a boundary condition of a model run is configuration, not a property of a component.
- **Dataset statistics**: derived sets of attribute values with descriptive statistics, optionally grouped by the components the values sit on (Collections).

What it deliberately does **not** cover (out of scope, defer to specialist ontologies):

- Detailed building geometry (use BOT, IFC, or CityGML).
- Full electrical-grid topology and protection (use CIM).
- Occupant modelling and behavioural data.
- Market and pricing models beyond `SimpleCostAttribute` / `UnitBasedCostAttribute`.

Link to those ontologies with SKOS mappings rather than modelling them again. [LINKING_DOMAINS.md](LINKING_DOMAINS.md) explains how, with a checked example for OEO, Brick, SAREF, BOT, IFC and CIM.

## Design principles

1. **Attribute-as-class.** Every measurable property is an *instance* of an attribute class (`PhysicalAttribute`, `CategoricalAttribute`, etc.), not a datatype property. This lets attributes carry their own units, provenance, time-series, and uncertainty without losing the link to the parent component.

2. **Dual-typing for instances.** A real-world entity is typed both as its concrete domain class (e.g. `EnergyConsumer`) and as a *data-shape* class (e.g. `BuildingA` typed `dici_onto:Building`). This is what lets the Replica Builder UI render forms generically.

3. **Path-style URIs.** Attribute URIs follow `https://<project>/<instance>/<attribute>` (e.g. `BuildingA/floorArea`). This makes them self-describing in SPARQL results and avoids URI minting ceremony.

4. **Re-use over re-invention.** Units and quantity kinds come from QUDT, currencies from QUDT, mapping annotations from SKOS, ontology metadata from Dublin Core terms, basic typing from RDFS/OWL. PROV-O is used for one link so far (`derivedFromCatalogue` under `prov:wasDerivedFrom`); more provenance will follow the same route. The ontology only defines what its own users need that these vocabularies do not cover.

5. **Small core, extensions for projects.** The core is compact (181 classes in v0.6.0). Project-specific extensions live in separate TTL files in each workspace and use the same `dici_onto:` namespace. The core itself is built, not hand-edited: `tools/build_core.py` replays `core/scaffold_instructions.json` through the platform's Ontology Manager onto `core/bare_core.ttl`, so core and extensions follow the same component, category and link pattern.

6. **Terms describe themselves.** Every term carries `rdfs:label` + `rdfs:comment`, and mapping-decision classes additionally carry `skos:definition`, `skos:altLabel` (synonyms), `skos:example`, and `skos:scopeNote`. This is what lets onboarding agents map domain concepts (a `WindPark` → `Location`) semantically instead of by name. See the [mapping guide](AGENT_MAPPING_GUIDE.md) and the generated [term index](term-index.md).

## Namespaces

| Prefix          | URI                                                                                | Purpose                                  |
|-----------------|------------------------------------------------------------------------------------|------------------------------------------|
| `dici_onto:`    | `https://digicities.info/ontology#`                                                | This ontology                            |
| `qudt:`         | `http://qudt.org/schema/qudt/`                                                     | QUDT schema (units, quantity kinds)      |
| `unit:`         | `http://qudt.org/vocab/unit/`                                                      | QUDT unit instances                      |
| `cur:`          | `http://qudt.org/vocab/currency/`                                                  | QUDT currency codes                      |
| `skos:`         | `http://www.w3.org/2004/02/skos/core#`                                             | Mapping annotations (definition, altLabel, example, scopeNote) |
| `prov:`         | `http://www.w3.org/ns/prov#`                                                       | Provenance (`derivedFromCatalogue` is a sub-property of `prov:wasDerivedFrom`) |
| `dcterms:`      | `http://purl.org/dc/terms/`                                                        | Ontology metadata (license, source)      |
| `rdf:`          | `http://www.w3.org/1999/02/22-rdf-syntax-ns#`                                      | RDF                                      |
| `rdfs:`         | `http://www.w3.org/2000/01/rdf-schema#`                                            | RDF Schema (labels, comments, sub-class and sub-property) |
| `owl:`          | `http://www.w3.org/2002/07/owl#`                                                   | OWL (classes, properties, inverses, deprecation) |
| `xsd:`          | `http://www.w3.org/2001/XMLSchema#`                                                | Datatypes                                |

## Class hierarchy at a glance

```
Component          ← physical things (Converter, Storage, Sensor, Meter, ...)
Process            ← transformations (ConversionProcess, StorageProcess, TransportProcess)
Flow               ← what moves through the system (ElectricityFlow, HeatFlow, GasFlow, ...)
Resource           ← sources (RenewableResource, NonRenewableResource, SolarResource, ...)
Network            ← connectivity (energy networks, info networks)
Location           ← spatial context
Attribute          ← properties with values (value kinds and categories, see attribute-types.md)
TimeSeries         ← Historic / Live / Future variants
Reference          ← citation entries
Scenario           ← what-if container
Assumption         ← single or series assumptions feeding scenarios
Service            ← an external model; its ServiceConfiguration profiles hold the settings it runs with
Collection         ← derived sets and statistics over attribute values (Set, GroupedSet)
```

See [class-hierarchy.md](class-hierarchy.md) for the full list.

## Versioning

Semver. Breaking changes (renaming or removing a class, changing a domain/range) bump the major version. Additive changes (new classes, new attribute types) bump the minor. Pure annotation or comment fixes bump the patch. Before 1.0.0, a minor bump may break: a breaking 0.x release says so at the top of its CHANGELOG entry, and renamed terms stay one release as `owl:deprecated` aliases.

Downstream consumers should pin a specific tag. The Digicities platform vendors the TTL and tracks the version in its own `services/graphdb/ontology/VERSION` file.

# Ontology overview

The Digicities ontology (`dici_onto:`) is an OWL/RDF vocabulary for **city-scale energy systems**. It's designed to be the schema layer for digital-twin replicas of districts, neighbourhoods, and individual buildings. With enough structure to drive a generic UI (the [Digicities platform](https://github.com/uesl-empa/digicities-platform)) and enough precision to back analytical and simulation workflows.

## Scope

What the ontology covers:

- **Physical infrastructure**: components (energy converters, storage, sensors, meters, controllers, actuators, switches, valves, junctions) and the networks that connect them.
- **Energy and material flows**: electricity, heat, gas, liquid fuels, solid fuels, materials, with carrier-specific subclasses.
- **Resources**: renewable and non-renewable, including solar and wind.
- **Processes**: conversion, storage, transport.
- **Location and geospatial context**: instances can be located in a `Location` and carry `GeospatialAttribute`s.
- **Time-series data**: historic, live, and future series, attached to any attribute.
- **Costs**: simple monetary values and per-unit costs, in any QUDT currency.
- **Provenance**: references and citations via `prov:wasDerivedFrom`.
- **Scenarios and assumptions**: first-class classes for what-if analysis.

What it deliberately does **not** cover (out of scope, defer to specialist ontologies):

- Detailed building geometry (use BOT, IFC, or CityGML).
- Full electrical-grid topology and protection (use CIM).
- Occupant modelling and behavioural data.
- Market and pricing models beyond `SimpleCostAttribute` / `UnitBasedCostAttribute`.

## Design principles

1. **Attribute-as-class.** Every measurable property is an *instance* of an attribute class (`PhysicalAttribute`, `CategoricalAttribute`, etc.), not a datatype property. This lets attributes carry their own units, provenance, time-series, and uncertainty without losing the link to the parent component.

2. **Dual-typing for instances.** A real-world entity is typed both as its concrete domain class (e.g. `EnergyConsumer`) and as a *data-shape* class (e.g. `BuildingA` typed `dici_onto:Building`). This is what lets the Replica Builder UI render forms generically.

3. **Path-style URIs.** Attribute URIs follow `https://<project>/<instance>/<attribute>` (e.g. `BuildingA/floorArea`). This makes them self-describing in SPARQL results and avoids URI minting ceremony.

4. **Re-use over re-invention.** Units come from QUDT, currencies from QUDT, provenance from PROV-O, basic typing from RDFS/OWL. The ontology only defines what's specific to city-scale energy.

5. **Small core, extensible periphery.** The core TTL is intentionally compact (~130 classes). Project-specific extensions live in separate TTL files loaded by downstream tools as named graphs.

6. **Terms describe themselves.** Every term carries `rdfs:label` + `rdfs:comment`, and mapping-decision classes additionally carry `skos:definition`, `skos:altLabel` (synonyms), `skos:example`, and `skos:scopeNote`. This is what lets onboarding agents map domain concepts (a `WindPark` → `Location`) semantically instead of by name. See the [mapping guide](AGENT_MAPPING_GUIDE.md) and the generated [term index](term-index.md).

## Namespaces

| Prefix          | URI                                                                                | Purpose                                  |
|-----------------|------------------------------------------------------------------------------------|------------------------------------------|
| `dici_onto:`    | `https://digicities.info/ontology#`                                                | This ontology                            |
| `qudt:`         | `http://qudt.org/schema/qudt/`                                                     | QUDT schema (units, quantity kinds)      |
| `unit:`         | `http://qudt.org/vocab/unit/`                                                      | QUDT unit instances                      |
| `cur:`          | `http://qudt.org/vocab/currency/`                                                  | QUDT currency codes                      |
| `skos:`         | `http://www.w3.org/2004/02/skos/core#`                                             | Mapping annotations (definition, altLabel, example, scopeNote) |
| `rdf:`, `rdfs:`, `owl:`, `xsd:` | standard W3C namespaces                                            | ...                                      |

## Class hierarchy at a glance

```
Component          ← physical things (Converter, Storage, Sensor, Meter, ...)
Process            ← transformations (ConversionProcess, StorageProcess, TransportProcess)
Flow               ← what moves through the system (ElectricityFlow, HeatFlow, GasFlow, ...)
Resource           ← sources (RenewableResource, NonRenewableResource, SolarResource, ...)
Network            ← connectivity (energy networks, info networks)
Location           ← spatial context
Attribute          ← measurable properties (15 subclasses, see attribute-types.md)
TimeSeries         ← Historic / Live / Future variants
Reference          ← citation entries
Scenario           ← what-if container
Assumption         ← single or series assumptions feeding scenarios
```

See [class-hierarchy.md](class-hierarchy.md) for the full list.

## Versioning

Semver. Breaking changes (renaming or removing a class, changing a domain/range) bump the major version. Additive changes (new classes, new attribute types) bump the minor. Pure annotation or comment fixes bump the patch.

Downstream consumers should pin a specific tag. The Digicities platform vendors the TTL and tracks the version in its own `services/graphdb/ontology/VERSION` file.

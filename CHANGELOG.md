# Changelog

All notable changes to the Digicities ontology are recorded here. The project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] — 2026-10-09

**BREAKING (pre-1.0 minor).** Scaffold release: the core is no longer edited by hand. It is built by replaying `core/scaffold_instructions.json` through the Digicities platform's Ontology Manager onto `core/bare_core.ttl` (`tools/build_core.py`), so the core follows the same Entity-Attribute-Relation pattern as every workspace extension, by construction. Hand edits had left the pattern broken in 49 places (missing ranges, duplicate predicates, categories named unlike their component, components without a scaffold).

### Changed
- **`rdfs:range` of every `has<X>Attribute` is `<X>Attribute`, the component's category, and nothing else.** 19 general predicates had no range; they now state it. Tools read a component's category from this range, never from a name.
- `hasComponentAttribute` states `rdfs:domain Component` and `rdfs:range ComponentAttribute` (the root of the pattern).
- The core's attributes go through the same operations as an extension's: each has a value kind and one link predicate `has<Component><Attribute>Attribute`. Kinds: `ActuatorPosition`, `MeasurementAccuracy`, `SamplingRate`, `FlowCapacity`, `FlowRate`, `Efficiency`, `ProcessCapacity`, `StateOfCharge`, `StorageCapacity` are `PhysicalAttribute` (with their existing default units); `SetPoint` is `SimpleValueAttribute`; `MeterReading` and `MeasurementValue` are `DynamicAttribute`; `SwitchState` is `CategoricalAttribute`.
- The predicates under the old short duplicates now hang under the full ones (e.g. `hasSolarResourceAttribute ⊑ hasRenewableResourceAttribute`).
- **`locatedIn` has its own inverse, `locationContains`.** `locationOf` was the inverse of both `hasLocation` and `locatedIn`, so under inference `hasLocation(a, b)` gave `locationOf(b, a)` and then `locatedIn(a, b)`: the two predicates always appeared together and choosing one meant nothing. `locationOf` is now the inverse of `hasLocation` only. A test keeps every property's inverse partner unshared.

### Added
- Every component class has its own category and general predicate: the 14 leaf classes (`CircuitBreaker`, `Damper`, `Valve`, `ElectricityFlow`, `GasFlow`, `HeatFlow`, `LiquidFuelFlow`, `ElectricityMeter`, `GasMeter`, `HeatMeter`, `FlowSensor`, `PowerSensor`, `PressureSensor`, `TemperatureSensor`) and the observation family (`hasObservationAttribute`, `hasWeatherObservationAttribute`, `hasCompositeWeatherObservationAttribute`), which had categories but no predicates.
- 13 link predicates for the core's attributes (`hasConversionProcessEfficiencyAttribute`, ...).
- **`DataPathAttribute`** (subclass of `Attribute`): the value kind of an attribute whose value is a path or reference to a data file, read through `hasDataPath`. Before, `ResourceAttribute` did this job AND was the category of the `Resource` component; it is now only that category. A data-path attribute is typed `DataPathAttribute`.
- **`IdentifierAttribute`** (subclass of `Attribute`): the value kind of an attribute whose value identifies the thing it belongs to, reached through `hasIdentifier`. Identifier attribute classes (`BuildingId`, `BacnetId`, ...) were filed under the component's category with no value kind, which broke the pattern check.
- `locationContains` (inverse of `locatedIn`).
- `core/bare_core.ttl`, `core/scaffold_instructions.json`, `tools/build_core.py`, `tests/test_build_core.py` (reproducible build, pattern check, no silent term loss, unchanged annotations, one version everywhere).

### Deprecated (aliases kept for one release, `owl:deprecated true` + `owl:equivalentClass` / `owl:equivalentProperty`)
- Renamed to the Ontology Manager's naming rule: `LiquidFuelCarrierAttribute` → `LiquidFuelAttribute`, `SolidFuelCarrierAttribute` → `SolidFuelAttribute`, `WindResourceAttribute` → `WindAttribute`, `hasElectricityAttribute` → `hasElectricityCarrierAttribute`, `hasFuelAttribute` → `hasFuelCarrierAttribute`, `hasGaseousFuelAttribute` → `hasGaseousFuelCarrierAttribute`, `hasSolarAttribute` → `hasSolarResourceAttribute`.
- Duplicates of a full predicate with the same domain: `hasColdAttribute` → `hasColdCarrierAttribute`, `hasHeatAttribute` → `hasHeatCarrierAttribute`, `hasThermalEnergyAttribute` → `hasThermalEnergyCarrierAttribute`, `hasRenewableAttribute` → `hasRenewableResourceAttribute`, `hasNonRenewableAttribute` → `hasNonRenewableResourceAttribute`.
- A property alias is also `rdfs:subPropertyOf` its replacement, so data still using it is found under `hasAttribute`.

### Removed
- `hasEnergyCarrierEnergyCostAttribute`: no domain, no range, and its class (`EnergyCostAttribute`) was removed in an earlier hand edit.

### Docs
- `overview.md` versioning: before 1.0.0 a minor bump may break; breaking 0.x releases say so and keep deprecated aliases one release.

## [0.5.0] — 2026-10-02

Configuration release: settings a model needs to run get their own place, owned by the service, and the catalogue provenance the platform already relies on is declared in core.

### Added
- **`ConfigurationAttribute`** (subclass of `Attribute`): marker for a value that exists for a model or service to operate rather than as an observation or behaviour of a component. The test: **a value that sets a boundary condition of the model run is configuration** — a model or algorithm choice, a calibration constant, a run name or frequency, a stream address. Orthogonal to the value kind: an attribute class is a `ConfigurationAttribute` *and* e.g. a `CategoricalAttribute`.
- **`ServiceConfiguration`**: a configuration profile owned by one `Service` (typically one config file or run setup). Deliberately **not** a `Component`. Properties: `hasConfiguration` (Service → profile) with inverse `configures`, `appliesTo` (profile → the components it is tuned for; not system topology), `hasConfigurationParameter` (profile → its `ConfigurationAttribute` values). Profiles keep two services that configure the same component from colliding on it.
- **`derivedFromCatalogue`** (object property, Component → Component, `⊑ prov:wasDerivedFrom`, not a `linksComponent` subproperty) and **`isCatalogueEntry`** (boolean): catalogue provenance the platform explorer and the onboarding agent have used since 0.3/0.4, previously declared per workspace extension (`derivedFromCatalogue`) or not at all (`isCatalogueEntry`). Promoted because every catalogue onboarding (wind, solar, the technology database) uses them.
- `prov:` prefix in the core header.
- Annotation guard: both new classes are mapping-decision classes (definition + example required); a new test keeps configuration and catalogue terms outside system topology.

### Docs
- `attribute-types.md` and `AGENT_MAPPING_GUIDE.md`: the boundary-condition test and the wind example (simulation config and stream addresses become a service configuration profile, never a component).

## [0.4.0] — 2026-08-28

Observation release: pure observations as first-class components. Some inputs are observed data with no modelled sensor or equipment behind them; until now they had to be forced onto a device class or dropped.

### Added
- **`Observation`** (subclass of `Component`): an observed phenomenon or measurement record that stands on its own. Use it when only the observed data matters; if the observing device is part of the model, the data still belongs on that device (`Sensor`, `Meter`), and a single measured property of an existing component stays an `Attribute`.
- **`WeatherObservation`** (subclass of `Observation`): observed weather conditions at a place, independent of weather-station equipment.
- **`CompositeWeatherObservation`** (subclass of `WeatherObservation`): several weather variables bundled into one artefact, typically a weather file (EPW, TMY) referenced from an attribute via `hasDataPath`.
- Matching typing markers `ObservationAttribute`, `WeatherObservationAttribute`, `CompositeWeatherObservationAttribute` following the per-class attribute-group convention.

## [0.3.0] — 2026-08-18

Collections release: dataset-level analysis — aggregate attribute instances into sets with descriptive statistics, and partition one attribute type by another — or by the component instances its owners are linked to (GROUP BY analogue).

### Added
- **Collections vocabulary**: `Collection` (abstract), `Set`, `GroupedSet`, `DescriptiveStatistics`, `Distribution`, `DistributionBin` classes; `aggregatedIn` (domain `Attribute`) with `hasMember` inverse, `hasSet`/`derivedFromDataSet` (data-source provenance), `ofAttributeType`/`groupedBy` (class-as-value), `hasGroup`, `groupComponent` (component-grouped Sets name their container instance), `hasDescriptiveStatistics`, `hasDistribution`, `hasBin` object properties; `groupKey`, the statistics data properties (`count`, `mean`, `standardDeviation`, `minValue`, `maxValue`, `median`, `sum`, `distinctCount`, `mode`), bin data properties (`binLabel`, `binLowerBound`, `binUpperBound`, `binFrequency`), and `computedAt`/`computedBy` provenance. Collections are **derived, recomputable artefacts** materialized by the platform's `backend/collections` into a dedicated named graph — never authored data. `minValue`/`maxValue` deliberately carry no `rdfs:range` (numeric sets hold `xsd:double`, temporal sets `xsd:dateTime`).

## [0.2.0] — 2026-07-24

Annotation release: the vocabulary now describes itself, so onboarding agents can map domain concepts semantically instead of by name.

### Added
- **SKOS mapping annotations** across the core: every `dici_onto:` term now carries `rdfs:label` + `rdfs:comment`; mapping-decision classes (Component subtree, attribute kinds, Scenario/Service/TimeSeries) additionally carry `skos:definition`, `skos:altLabel` (synonyms such as "Site" on `Location`), `skos:example`, and `skos:scopeNote` for sibling disambiguation.
- Legacy annotation properties bridged to SKOS: `dici_onto:definition ⊑ skos:definition`, `dici_onto:Synonymous ⊑ skos:altLabel`, `dici_onto:abbreviation ⊑ skos:altLabel`.
- `tools/generate_term_index.py` — generates the agent-facing lookup `docs/term-index.json` / `docs/term-index.md` from the TTL (optionally merged with workspace extension TTLs).
- `docs/AGENT_MAPPING_GUIDE.md` — the mapping procedure and decision tree for onboarding agents, with a worked wind-forecasting example.
- `tests/test_annotations.py` — annotation-coverage tests and a stale-index guard (CI fails if `term-index.*` doesn't match the TTL).
- **20 platform terms promoted into core** (previously minted only in the platform's vendored copy): scenario/registry provenance data properties (`assumptionApplied`, `assumptionId`, `assumptionType`, `builtForService`, `cost`, `createdInWorkspace`, `generatedBy`, `linkType`, `modificationType`, `modifiedComponents`, `sourceCatalog`, `sourceType`, `sourceWorkspace`), the `TemporalPrecision` class with its `Year`/`YearMonth`/`Date`/`DateTime`/`Unknown` individuals, and `linksInputyEntityTo` — the historical misspelling the platform scenario tooling writes — added as a **deprecated `rdfs:subPropertyOf linksInputEntityTo`** so semantic queries via the canonical name find the data.
- **Second promotion sweep — every remaining term the platform writes or requires is now declared in core** (closed by the 2026-07-28 cross-repo audit): `supersedesAttribute` + `basedOn` (thin-scenario override and scenario-derivation links), `hasDefaultTemporalPrecision` (class-level default for event attribute classes, mirroring `hasDefaultUnit`), `AnnotationAttribute` + `hasAnnotationValue` (free-text annotation attributes the data-product parser requires), and the provenance vocabulary `Reference` / `ReferenceType` / `hasReferenceType` with the `DOI` individual (written from the ingestion template's Reference sheet).
- `owl:versionInfo "0.2.0"` + `owl:versionIRI` on the ontology header — the self-describing vocabulary now states its own version.

### Fixed
- `hasDataPath` domain loosened from `CurveAttribute` to `Attribute` — the platform also uses data paths on resource attributes, and the old conjunction of domains mis-typed those nodes.
- `hasDataPoints` was declared twice — as an `owl:ObjectProperty` (with label/comment) *and* a bare `owl:DatatypeProperty` — illegal punning in OWL DL that produced duplicate term-index entries. Merged into a single fully-annotated `owl:DatatypeProperty` (`⊑ hasAttributeValue`, domain `CurveAttribute`, range `rdf:JSON`).

### Changed
- `tools/validate_extension.py`: a missing `rdfs:comment` is now an **error** (was a warning); missing `skos:definition`/`altLabel`/`example` on classes warn.
- Promotion criteria (`docs/CORE_EVOLUTION.md`, `CONTRIBUTING.md`): terms entering core must carry the full annotation set and regenerate the term index.

## [0.1.0] — 2026-05-19

Initial public release. Snapshot extracted from the pre-public Digicities monorepo.

### Added
- `core/dici_onto_core.ttl` — the core ontology (~133 classes, ~1.9k Turtle lines).
- `core/qudt_units.txt` — QUDT unit list referenced by `Physical`, `UnitBasedCost`, `Curve`, `CustomPhysicalRatio`, and time-series attributes.
- 15 attribute-type classes: `PhysicalAttribute`, `SimpleCostAttribute`, `UnitBasedCostAttribute`, `CategoricalAttribute`, `EventAttribute`, `ComponentAttribute` (a.k.a. ClassObject), `CurveAttribute`, `CustomPhysicalRatioAttribute`, `SimpleValueAttribute`, `StaticAttribute`, `DynamicAttribute`, `GeospatialAttribute`, plus the three time-series subclasses (`HistoricTimeSeries`, `LiveTimeSeries`, `FutureTimeSeries`).
- Upper concepts: `Component`, `Process`, `Flow`, `Resource`, `Network`, `Location`, `Scenario`, `Assumption`, `Reference`.
- Domain coverage for energy carriers (electricity, heat, gas, liquid fuel, solid fuel), converters, storage, sensors, meters, controllers, and actuators.

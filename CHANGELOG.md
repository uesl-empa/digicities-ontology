# Changelog

All notable changes to the Digicities ontology are recorded here. The project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — 2026-05-19

Initial public release. Snapshot extracted from the pre-public Digicities monorepo.

### Added
- `core/dici_onto_core.ttl` — the core ontology (~133 classes, ~1.9k Turtle lines).
- `core/qudt_units.txt` — QUDT unit list referenced by `Physical`, `UnitBasedCost`, `Curve`, `CustomPhysicalRatio`, and time-series attributes.
- 15 attribute-type classes: `PhysicalAttribute`, `SimpleCostAttribute`, `UnitBasedCostAttribute`, `CategoricalAttribute`, `EventAttribute`, `ComponentAttribute` (a.k.a. ClassObject), `CurveAttribute`, `CustomPhysicalRatioAttribute`, `SimpleValueAttribute`, `StaticAttribute`, `DynamicAttribute`, `GeospatialAttribute`, plus the three time-series subclasses (`HistoricTimeSeries`, `LiveTimeSeries`, `FutureTimeSeries`).
- Upper concepts: `Component`, `Process`, `Flow`, `Resource`, `Network`, `Location`, `Scenario`, `Assumption`, `Reference`.
- Domain coverage for energy carriers (electricity, heat, gas, liquid fuel, solid fuel), converters, storage, sensors, meters, controllers, and actuators.

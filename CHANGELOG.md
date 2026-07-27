# Changelog

All notable changes to the Digicities ontology are recorded here. The project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] — 2026-07-24

Annotation release: the vocabulary now describes itself, so onboarding agents can map domain concepts semantically instead of by name.

### Added
- **SKOS mapping annotations** across the core: every `dici_onto:` term now carries `rdfs:label` + `rdfs:comment`; mapping-decision classes (Component subtree, attribute kinds, Scenario/Service/TimeSeries) additionally carry `skos:definition`, `skos:altLabel` (synonyms such as "Site" on `Location`), `skos:example`, and `skos:scopeNote` for sibling disambiguation.
- Legacy annotation properties bridged to SKOS: `dici_onto:definition ⊑ skos:definition`, `dici_onto:Synonymous ⊑ skos:altLabel`, `dici_onto:abbreviation ⊑ skos:altLabel`.
- `tools/generate_term_index.py` — generates the agent-facing lookup `docs/term-index.json` / `docs/term-index.md` from the TTL (optionally merged with workspace extension TTLs).
- `docs/AGENT_MAPPING_GUIDE.md` — the mapping procedure and decision tree for onboarding agents, with a worked wind-forecasting example.
- `tests/test_annotations.py` — annotation-coverage tests and a stale-index guard (CI fails if `term-index.*` doesn't match the TTL).
- **20 platform terms promoted into core** (previously minted only in the platform's vendored copy): scenario/registry provenance data properties (`assumptionApplied`, `assumptionId`, `assumptionType`, `builtForService`, `cost`, `createdInWorkspace`, `generatedBy`, `linkType`, `modificationType`, `modifiedComponents`, `sourceCatalog`, `sourceType`, `sourceWorkspace`), the `TemporalPrecision` class with its `Year`/`YearMonth`/`Date`/`DateTime`/`Unknown` individuals, and `linksInputyEntityTo` — the historical misspelling the platform scenario tooling writes — added as a **deprecated `rdfs:subPropertyOf linksInputEntityTo`** so semantic queries via the canonical name find the data.

### Fixed
- `hasDataPath` domain loosened from `CurveAttribute` to `Attribute` — the platform also uses data paths on resource attributes, and the old conjunction of domains mis-typed those nodes.

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

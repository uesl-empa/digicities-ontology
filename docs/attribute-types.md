# Attribute types

Every measurable property of a `Component`, `Process`, `Flow`, or `Resource` instance is itself an instance of an `Attribute` subclass. This page lists the 15 attribute-type classes the ontology defines, what they model, and how downstream tools serialise them.

The Excel-importer convention in the Digicities platform mirrors these classes — the spreadsheet header row that picks an attribute type literally names the class (`Physical`, `SimpleCost`, etc.).

| Class                              | Purpose                                                              | Typical output triples                                                                  |
|------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `PhysicalAttribute`                | A number with a QUDT unit and quantity kind.                          | `qudt:value 4800.0 ; qudt:unit unit:KiloW-HR`                                            |
| `SimpleCostAttribute`              | A monetary value in a specific currency.                              | `qudt:value 250.0 ; dici_onto:currency cur:CHF`                                          |
| `UnitBasedCostAttribute`           | A per-unit cost (e.g. CHF per kWh). Combines unit + currency.        | adds a `qudt:unit` triple on top of `SimpleCostAttribute`                                |
| `CategoricalAttribute`             | A value drawn from a closed vocabulary.                               | `dici_onto:hasCategoricalValue dici_onto:SingleFamilyHouse`                              |
| `EventAttribute`                   | A point-in-time event (year, date, or datetime — auto-detected).      | `dici_onto:hasTemporalValue "1970"^^xsd:gYear`                                           |
| `ComponentAttribute` (ClassObject) | A typed link to another instance (the foreign-key analogue).          | `dici_onto:locatedIn <…/Location/AlpineValley>`                                          |
| `CurveAttribute`                   | An x/y curve with units on each axis.                                  | `dici_onto:hasDataPoints """[(0,0);(1,2);…]"""`                                          |
| `CustomPhysicalRatioAttribute`     | A ratio of two physical quantities (numerator/denominator units).     | `qudt:value 0.25 ; dici_onto:hasUnitLabel "CHF/KiloW-HR"`                                |
| `SimpleValueAttribute`             | A bare string or number, no unit.                                     | `dici_onto:hasAttributeValue "BLDG-A-001"`                                               |
| `StaticAttribute`                  | Marker mixin for time-invariant properties.                            | (intersected with `Physical`/`Categorical`/etc.)                                         |
| `DynamicAttribute`                 | Marker mixin for properties that vary over time.                       | (typically combined with a `TimeSeries` link)                                            |
| `GeospatialAttribute`              | Latitude/longitude or full GeoSPARQL geometry.                         | implementation depends on the geo-vocabulary chosen                                      |
| `HistoricTimeSeries` (`Historic`)  | Past observations attached to an attribute.                            | `dici_onto:hasHistoricTimeSeries <…/series>`                                             |
| `LiveTimeSeries` (`Live`)          | Streaming/live observations.                                           | `dici_onto:hasLiveTimeSeries <…/series>`                                                 |
| `FutureTimeSeries` (`Future`)      | Forecasts or scenario projections.                                     | `dici_onto:hasFutureTimeSeries <…/series>`                                               |

In the ontology TTL, every class above inherits (directly or transitively) from `dici_onto:Attribute`.

## How attributes attach to instances

Each instance has a path-style attribute URI. For a building with a floor area of 120 m²:

```turtle
<https://example.org/proj/BuildingA>
    a dici_onto:EnergyConsumer ;
    dici_onto:hasAttribute <https://example.org/proj/BuildingA/floorArea> .

<https://example.org/proj/BuildingA/floorArea>
    a dici_onto:PhysicalAttribute ;
    rdfs:label "floorArea" ;
    qudt:value 120.0 ;
    qudt:unit unit:M2 ;
    qudt:hasQuantityKind quantitykind:Area .
```

The path-style URI (`BuildingA/floorArea`) is the recommended convention but not enforced by the ontology itself — projects can mint their own URI shapes.

## Provenance

Any attribute can carry a citation via the standard PROV-O property:

```turtle
<…/BuildingA/floorArea>
    prov:wasDerivedFrom <https://example.org/proj/Reference/swiss_energy_atlas_2024> .

<https://example.org/proj/Reference/swiss_energy_atlas_2024>
    a dici_onto:Reference ;
    rdfs:label "Swiss Energy Atlas (2024)" ;
    dcterms:source "https://example.swiss/atlas/2024" .
```

## Picking the right type

- **Has a numeric value + a unit?** → `PhysicalAttribute`. If the unit is per-X, use `CustomPhysicalRatioAttribute`.
- **Money?** → `SimpleCostAttribute` if a total; `UnitBasedCostAttribute` if a rate (e.g. CHF/kWh).
- **One of a fixed list of choices?** → `CategoricalAttribute`. The choice values themselves should be `dici_onto:` instances.
- **A pointer to another instance?** → `ComponentAttribute` (a.k.a. ClassObject in the Excel importer). Pick the predicate that names the relationship (`locatedIn`, `installedAt`, `partOf`, …).
- **A point in time?** → `EventAttribute`. The serialiser auto-detects year vs. date vs. datetime.
- **A function (load profile, efficiency curve, …)?** → `CurveAttribute`.
- **A bare string or untyped number?** → `SimpleValueAttribute`. Use sparingly — units and categories are more useful for downstream tooling.
- **A time-varying signal?** → `HistoricTimeSeries` / `LiveTimeSeries` / `FutureTimeSeries`. Attach via `dici_onto:hasHistoricTimeSeries` etc.

When in doubt, prefer the most specific type the data fits — generic `SimpleValueAttribute` is a fallback, not a default.

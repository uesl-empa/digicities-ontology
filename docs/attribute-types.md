# Attribute types

Every property of a `Component`, `Process`, `Flow`, or `Resource` instance that carries a value is itself an instance of an `Attribute` subclass. This page lists the attribute classes the ontology defines (the value kinds, the marker classes and the per-component categories), what they model, and how the platform writes them.

The Excel importer in the Digicities platform uses the same names: the header row that picks an attribute type names the value kind (`Physical`, `SimpleCost`, ...).

| Class                              | Purpose                                                              | Typical output triples                                                                  |
|------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `PhysicalAttribute`                | A number with a QUDT unit and quantity kind.                          | `qudt:value 4800.0 ; qudt:unit unit:KiloW-HR`                                            |
| `SimpleCostAttribute`              | A monetary value in a specific currency.                              | `qudt:value 250.0 ; dici_onto:currency cur:CHF`                                          |
| `UnitBasedCostAttribute`           | A per-unit cost (e.g. CHF per kWh). Combines unit + currency.        | adds a `qudt:unit` triple on top of `SimpleCostAttribute`                                |
| `CategoricalAttribute`             | A value drawn from a closed vocabulary.                               | `dici_onto:hasCategoricalValue dici_onto:SingleFamilyHouse`                              |
| `EventAttribute`                   | A point-in-time event (year, date, or datetime, detected from the value). | `dici_onto:hasTemporalValue "1970"^^xsd:gYear`                                           |
| `ComponentAttribute`               | The root of the per-component categories. Every component class has one (`TurbineAttribute`, `SensorAttribute`, ...), and its attributes are filed under it. Not a value kind. | `dici_onto:HubHeight rdfs:subClassOf dici_onto:TurbineAttribute`                         |
| `CurveAttribute`                   | An x/y curve with units on each axis.                                  | `dici_onto:hasDataPoints """[(0,0);(1,2);…]"""`                                          |
| `CustomPhysicalRatioAttribute`     | A ratio of two physical quantities (numerator/denominator units).     | `qudt:value 0.25 ; dici_onto:hasUnitLabel "CHF/KiloW-HR"`                                |
| `SimpleValueAttribute`             | A bare string or number, no unit.                                     | `dici_onto:hasAttributeValue "BLDG-A-001"`                                               |
| `DataPathAttribute`                | A path or reference to a data file (a weather file, a dataset).       | `dici_onto:hasDataPath "weather/vienna.epw"`                                            |
| `IdentifierAttribute`              | A value that identifies its owner (an asset id, a BACnet id).         | `dici_onto:identifierValue "BLDG-A-001"` via `dici_onto:hasIdentifier`                  |
| `StaticAttribute`                  | Marker mixin for time-invariant properties.                            | (intersected with `Physical`/`Categorical`/etc.)                                         |
| `DynamicAttribute`                 | Marker mixin for properties that vary over time.                       | (typically combined with a `TimeSeries` link)                                            |
| `GeospatialAttribute`              | Latitude/longitude or full GeoSPARQL geometry.                         | implementation depends on the geo-vocabulary chosen                                      |
| `AggregateAttribute`               | A derived statistic (a mean, a count) of a group of attribute values, written onto the group's component by the platform. Never authored. | `qudt:value 84.5` on e.g. `<…/WindPark/A/HubHeightMean>`                                 |
| `ConfigurationAttribute`           | Marker mixin: a setting a model needs to run (a boundary condition), not a property of a component. | (intersected with `Categorical`/`Physical`/etc.; attached to a `ServiceConfiguration`)   |

In the ontology TTL, every class above inherits from `dici_onto:Attribute`.

Two things are deliberately not attribute types:

- **Time series.** `HistoricTimeSeries`, `LiveTimeSeries` and `FutureTimeSeries` are subclasses of `TimeSeries`, not of `Attribute`. An attribute points at a series (`hasHistoricTimeSeries`) or at the series' address (`hasHistoricTimeSeriesReference`, `hasLiveTimeSeriesReference`, `hasFutureTimeSeriesReference`). A live data stream, such as a weather feed, belongs to the component that produces it: it is the `hasLiveTimeSeriesReference` of one of that component's attributes. The Excel importer's `Historic`, `Live` and `Future` columns create these.
- **Links to another instance.** A turbine in a wind park is a link, not an attribute: an object property under `linksComponent` (`partOf`, `locatedIn`, `hasLocation`, ...). The Excel importer calls such a column `ClassObject`.

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

The path-style URI (`BuildingA/floorArea`) is the recommended convention. The ontology does not enforce it, so projects can mint their own URI shapes.

## Provenance

The core declares one provenance property so far: `derivedFromCatalogue` (a sub-property of `prov:wasDerivedFrom`), from a sited instance to the catalogue entry it was specified from. To cite a source for a value, use PROV-O directly, as below. A dedicated core property for this (`hasReference`) is planned; see the platform's `docs/KNOWN_LIMITATIONS.md`.

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
- **A pointer to another instance?** Not an attribute: a link. Use an object property under `linksComponent` that names the relationship (`locatedIn`, `hasLocation`, `partOf`, ...). In the Excel importer this is a `ClassObject` column.
- **A point in time?** → `EventAttribute`. The serialiser auto-detects year vs. date vs. datetime.
- **A function (load profile, efficiency curve, …)?** → `CurveAttribute`.
- **A path or reference to a data file?** → `DataPathAttribute` (value in `dici_onto:hasDataPath`).
- **A bare string or untyped number?** → `SimpleValueAttribute`. Use it sparingly: units and categories are more useful to the tools that read the data.
- **An identifier (an asset id, a BACnet id)?** → `IdentifierAttribute`, linked with `hasIdentifier`.
- **A time-varying signal?** → a `DynamicAttribute` whose values are a time series: point it at the series with `hasHistoricTimeSeries` / `hasFutureTimeSeries`, or at a live stream with `hasLiveTimeSeriesReference` (the stream address).

- **A setting the model needs to run, not something true of the component?** → mark the class `ConfigurationAttribute` as well as its value kind, and attach its values to a `ServiceConfiguration` profile of the service (`hasConfigurationParameter`), not to the component. The test: **if the value is a boundary condition of the model run, it is configuration**: a model or algorithm choice, a calibration constant (a wake decay constant), a run name or frequency. A live data stream that delivers a component's values is not configuration: it belongs to that component, as the `hasLiveTimeSeriesReference` of one of its attributes. A profile names the components it is tuned for with `appliesTo`.

When in doubt, prefer the most specific type the data fits. `SimpleValueAttribute` is a fallback, not a default.

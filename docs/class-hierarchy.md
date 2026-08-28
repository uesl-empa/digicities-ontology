# Class hierarchy

Full list of classes defined in `core/dici_onto_core.ttl`, grouped by upper concept. For per-term descriptions, synonyms and examples (the annotations agents map new concepts with), see the generated [term index](term-index.md) and the [mapping guide](AGENT_MAPPING_GUIDE.md). To regenerate this list, run:

```python
import rdflib
g = rdflib.Graph()
g.parse("core/dici_onto_core.ttl", format="turtle")
for s, _, _ in g.triples((None, rdflib.RDF.type, rdflib.OWL.Class)):
    if str(s).startswith("https://digicities.info/ontology#"):
        print(str(s).split("#")[1])
```

## Top-level concepts

- `Component` — physical infrastructure entities
- `Process` — transformations and operations
- `Flow` — what moves through the system
- `Resource` — sources of energy or material
- `Network` — connectivity layer
- `Location` — spatial context
- `Attribute` — measurable properties (see [attribute-types.md](attribute-types.md))
- `Reference` — citation entries (`ReferenceType` value set, e.g. the `DOI` individual)
- `Scenario` — what-if container
- `Assumption` — `AssumptionSingle` and `AssumptionSeries` variants
- `TimeSeries` — `HistoricTimeSeries`, `LiveTimeSeries`, `FutureTimeSeries`
- `Actor`, `Service`, `ServiceRequirement` — system-actor concepts
- `TemporalPrecision` — value set (named individuals `Year`, `YearMonth`, `Date`, `DateTime`, `Unknown`) for event-attribute temporal granularity
- `Observation` — observed data with no modelled equipment behind it (see Observations below)

## Components

Physical things in the world.

- `Component`
  - `Converter`, `EnergyConverter`, `MaterialConverter`, `Turbine`
  - `Storage`, `EnergyStorage`, `MaterialStorage`
  - `Sensor`, `FlowSensor`, `PowerSensor`, `PressureSensor`, `TemperatureSensor`
  - `Meter`, `ElectricityMeter`, `GasMeter`, `HeatMeter`
  - `Controller`, `Actuator`, `Switch`, `Valve`, `Damper`, `CircuitBreaker`
  - `EnergyConsumer`, `EnergyGenerator`
  - `Device` — generic catch-all
  - `Junction` — connection nodes
  - `ComponentLink` — connectivity edges
  - `ComponentAttributeRequirement`, `ComponentComponentRequirement` — schema constraints

## Observations

Observed phenomena that stand on their own — use when only the observed data matters and no sensor or equipment is part of the model. If the observing device IS modelled, attach the data to it (`Sensor`, `Meter`) instead.

- `Observation`
  - `WeatherObservation` — observed weather conditions at a place
    - `CompositeWeatherObservation` — many weather variables in one artefact, typically a weather file (EPW/TMY) referenced via `hasDataPath`

## Processes

What happens inside or between components.

- `Process`
  - `ConversionProcess`
  - `StorageProcess`
  - `TransportProcess`

## Flows

Stuff that moves.

- `Flow`
  - `ElectricityFlow`
  - `HeatFlow`
  - `GasFlow`
  - `LiquidFuelFlow`
  - `MaterialFlow`
  - `InformationFlow`
  - `EnergyCarrierFlow`

## Energy carriers

- `EnergyCarrier`
  - `ElectricityCarrier`
  - `HeatCarrier`, `ColdCarrier`, `ThermalEnergyCarrier`
  - `FuelCarrier`
    - `GaseousFuelCarrier`, `LiquidFuel`, `SolidFuel`

## Resources

Where energy/material comes from.

- `Resource`
  - `RenewableResource`
    - `SolarResource`, `Wind`
  - `NonRenewableResource`

## Networks

- `Network` — physical or logical connectivity layer

## Attribute classes

See [attribute-types.md](attribute-types.md) for full descriptions.

- `Attribute`
  - `PhysicalAttribute`, `SimpleCostAttribute`, `UnitBasedCostAttribute`
  - `CategoricalAttribute`, `EventAttribute`, `ComponentAttribute`
  - `CurveAttribute`, `CustomPhysicalRatioAttribute`, `AnnotationAttribute`
  - `SimpleValueAttribute`, `StaticAttribute`, `DynamicAttribute`
  - `GeospatialAttribute`
  - Domain-specific `…Attribute` subclasses for each component/flow/resource class (e.g. `EnergyConsumerAttribute`, `ConverterAttribute`, `MeterAttribute`, …) — used as a typing marker so SPARQL queries can filter "all attributes of an X".

## Time series

- `TimeSeries`
  - `HistoricTimeSeries`
  - `LiveTimeSeries`
  - `FutureTimeSeries`

## Capacities, ratings, states

- `FlowCapacity`, `FlowRate`
- `ProcessCapacity`
- `StorageCapacity`, `StateOfCharge`
- `SwitchState`, `ActuatorPosition`, `SetPoint`
- `Efficiency`, `SamplingRate`, `MeasurementAccuracy`, `MeasurementValue`, `MeterReading`

## Scenarios & assumptions

- `Scenario`
- `Assumption`
  - `AssumptionSingle`, `AssumptionSeries`

## Materials

- `Material`, `MaterialAttribute`

## System actors

- `Actor`, `ActorAttribute`
- `Service`, `ServiceRequirement`

---

If a class you need is missing, the standard pattern is:

1. Create an extension TTL with the new class as a subclass of the most specific existing parent.
2. Load it as a separate named graph in your triplestore.
3. If the class is genuinely reusable across projects, open a PR against this repo.

# Digicities term index

<!-- GENERATED FILE - do not edit. Regenerate with: python tools/generate_term_index.py -->

One card per term in the `dici_onto:` namespace, generated from the
ontology TTL. Use this file to map a domain concept onto the existing
vocabulary: grep for your concept's name and its synonyms, then check
the parent chain, examples and scope notes before deciding a parent
class. See [`AGENT_MAPPING_GUIDE.md`](AGENT_MAPPING_GUIDE.md) for the
mapping procedure.

## Classes

### Actor

- **Label:** Actor
- **Hierarchy:** Component > **Actor**
- **Description:** Human or organizational agent that owns, operates, or regulates components
- **Definition:** Actors represent stakeholders in the energy system including operators, regulators, consumers, and policy makers
- **Synonyms:** Operator, Organisation, Owner, Stakeholder
- **Examples:** A utility company, a grid operator, a municipality, a household, a regulator
- **Scope:** Use for humans and organisations that own, operate or regulate components. Automatic acting equipment is a Device (Actuator, Controller), not an Actor.

### ActorAttribute

- **Label:** Actor Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **ActorAttribute**
- **Description:** Typing marker grouping attributes that apply to a Actor; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Actuator

- **Label:** Actuator
- **Hierarchy:** Component > Device > **Actuator**
- **Description:** Device that converts control signals into physical action
- **Definition:** Actuators are devices that produce motion or control mechanisms based on input signals
- **Examples:** Valve actuator, damper motor, relay

### ActuatorAttribute

- **Label:** Actuator Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > **ActuatorAttribute**
- **Description:** Typing marker grouping attributes that apply to a Actuator; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### ActuatorPosition

- **Label:** Actuator Position
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > ActuatorAttribute > **ActuatorPosition**
- **Description:** Current position or state of an actuator
- **Default unit:** PERCENT

### AggregateAttribute

- **Label:** Aggregate Attribute
- **Hierarchy:** Thing > Attribute > **AggregateAttribute**
- **Description:** A DERIVED attribute node projecting one statistic of a component-grouped Set onto the group's component instance (e.g. FloorAreaMean on a District), in the exact shape authored attributes take (hasAttribute edge, has<Component><Name>Attribute predicate, qudt:value + qudt:unit) — so services request it as Component.attribute with no special handling. Written by the collections materializer into the collections graph; never authored.

### AnnotationAttribute

- **Label:** Annotation Attribute
- **Hierarchy:** Thing > Attribute > **AnnotationAttribute**
- **Description:** Attribute carrying free-text notes or commentary about a component, with its content in hasAnnotationValue
- **Synonyms:** Comment, Note
- **Examples:** Data-quality remark, operator note

### Assumption

- **Label:** Assumption
- **Hierarchy:** (root)
- **Description:** A modification rule applied to attributes when deriving a scenario
- **Synonyms:** Modifier, What-if Change

### AssumptionSeries

- **Label:** Assumption (series)
- **Hierarchy:** Assumption > **AssumptionSeries**
- **Description:** Assumption modifying a series of values over time

### AssumptionSingle

- **Label:** Assumption (single value)
- **Hierarchy:** Assumption > **AssumptionSingle**
- **Description:** Assumption modifying a single scalar attribute value

### Attribute

- **Label:** Attribute
- **Hierarchy:** Thing > **Attribute**
- **Description:** Root class for measurable or descriptive properties attached to Components
- **Definition:** An Attribute is a typed property-value node attached to a Component via dici_onto:hasAttribute (or a subproperty); the value itself is carried by qudt:value or another hasAttributeValue subproperty.
- **Synonyms:** Characteristic, Field, Parameter, Property, Variable
- **Examples:** Rated power, floor area, insulation class, electricity demand profile
- **Scope:** Concrete attribute classes subclass BOTH a kind (PhysicalAttribute, CategoricalAttribute, DynamicAttribute, ...) AND the owning component's attribute-group class (e.g. TurbineAttribute).

### CategoricalAttribute

- **Label:** Categorical Attribute
- **Hierarchy:** Thing > Attribute > **CategoricalAttribute**
- **Description:** Attribute whose value is one of an enumerated set of categories
- **Definition:** An attribute whose value is drawn from a closed set of named categories; the allowed values are declared as subclasses of the attribute class.
- **Examples:** Insulation class (Poor / Average / Good), tariff type (Flat / Variable / Dual)
- **Scope:** Declare the allowed values as subclasses of the concrete attribute class.

### CircuitBreaker

- **Label:** Circuit Breaker
- **Hierarchy:** Component > Device > Switch > **CircuitBreaker**
- **Description:** Switch that automatically interrupts electrical flow for safety

### ColdCarrier

- **Label:** Cold Carrier
- **Hierarchy:** Component > EnergyCarrier > ThermalEnergyCarrier > **ColdCarrier**
- **Description:** Thermal energy carrier delivering cooling
- **Examples:** Chilled water, brine

### ColdCarrierAttribute

- **Label:** Cold Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > ThermalEnergyCarrierAttribute > **ColdCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Cold Carrier; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Collection

- **Label:** Collection
- **Hierarchy:** (root)
- **Description:** Abstract grouping of attribute instances derived from a dataset. Superclass of Set and GroupedSet. Collections are derived, recomputable artefacts — not authored data.

### Component

- **Label:** Component
- **Hierarchy:** (root)
- **Description:** Root class for every entity that can appear in a digital replica: infrastructure, places, actors, resources, flows and processes
- **Definition:** The universal base class for things that exist in a modelled system. Every domain concept that represents an entity (rather than a measurable property) must be a direct or indirect subclass of Component.
- **Synonyms:** Asset, Entity, System Element
- **Examples:** Buildings, turbines, districts, pipes, energy carriers, grid operators
- **Scope:** Every new component type in an extension must be rdfs:subClassOf* Component or it will not appear in the platform UI. Measurable properties are NOT Components - subclass Attribute instead.

### ComponentAttribute

- **Label:** Component Attribute
- **Hierarchy:** Thing > Attribute > **ComponentAttribute**
- **Description:** Typing marker grouping attributes that apply to a Component; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### ComponentAttributeRequirement

- **Label:** Component-Attribute Requirement
- **Hierarchy:** ServiceRequirement > **ComponentAttributeRequirement**
- **Description:** Service requirement demanding that a component carries a given attribute

### ComponentComponentRequirement

- **Label:** Component-Component Requirement
- **Hierarchy:** ServiceRequirement > **ComponentComponentRequirement**
- **Description:** Service requirement demanding that two components are linked

### ComponentLink

- **Label:** Component Link
- **Hierarchy:** (root)
- **Description:** Reified edge connecting two components in a scenario, via hasInputEntity and linksInputEntityTo

### Controller

- **Label:** Controller
- **Hierarchy:** Component > Device > **Controller**
- **Description:** Device that manages and coordinates other devices or processes
- **Definition:** Controllers implement control logic and coordinate the operation of other system components
- **Synonyms:** BMS, Building Management System, Control Unit
- **Examples:** Thermostat, building management system, SCADA controller

### ControllerAttribute

- **Label:** Controller Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > **ControllerAttribute**
- **Description:** Typing marker grouping attributes that apply to a Controller; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### ConversionProcess

- **Label:** Conversion Process
- **Hierarchy:** Component > Process > **ConversionProcess**
- **Description:** Process that converts one form of energy to another
- **Examples:** Gas to heat in a boiler; electricity to heat in a heat pump

### ConversionProcessAttribute

- **Label:** Conversion Process Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ProcessAttribute > **ConversionProcessAttribute**
- **Description:** Typing marker grouping attributes that apply to a Conversion Process; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Converter

- **Label:** Converter
- **Hierarchy:** Component > **Converter**
- **Description:** Component that transforms an input into a different output form (energy or material)
- **Definition:** A machine or installation that converts energy from one form or carrier to another, or transforms materials. The equipment is the Converter; the transformation activity it performs is a ConversionProcess.
- **Synonyms:** Conversion Unit, Transformer
- **Examples:** Heat pump, boiler, electrolyser, turbine, inverter

### ConverterAttribute

- **Label:** Converter Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **ConverterAttribute**
- **Description:** Typing marker grouping attributes that apply to a Converter; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### CurveAttribute

- **Label:** Curve Attribute
- **Hierarchy:** Thing > Attribute > **CurveAttribute**
- **Description:** Attribute represented by x-y coordinate pairs forming a curve
- **Definition:** An attribute represented by a set of x,y coordinate pairs forming a curve
- **Examples:** Heat pump COP as a function of outdoor temperature

### CustomPhysicalRatioAttribute

- **Label:** Custom Physical Ratio Attribute
- **Hierarchy:** Thing > Attribute > **CustomPhysicalRatioAttribute**
- **Description:** An attribute whose unit is a ratio of two QUDT units (numerator/denominator). The ratio is expressed as a human-readable string via dici_onto:hasUnitLabel (e.g. 'KWh/yr'). The constituent units are constrained by dici_onto:hasRatioUnits on the subclass definition. Unlike Physical attributes, no qudt:unit IRI is emitted for this type — dici_onto:hasUnitLabel is the sole unit representation.

### Damper

- **Label:** Damper
- **Hierarchy:** Component > Device > Actuator > **Damper**
- **Description:** Actuator that controls air flow

### DescriptiveStatistics

- **Label:** Descriptive Statistics
- **Hierarchy:** (root)
- **Description:** Aggregate statistics computed over the members of a Set. Which properties are populated depends on the datatype family of the Set's attribute type (numeric, categorical, temporal, boolean); inapplicable properties are absent, never null.

### Device

- **Label:** Device
- **Hierarchy:** Component > **Device**
- **Description:** Physical or virtual devices that monitor, control, or measure components in the energy system
- **Definition:** Devices are components that provide sensing, actuation, measurement, or control capabilities within the energy system
- **Synonyms:** Equipment, Instrument
- **Examples:** Sensors, meters, controllers, switches, actuators
- **Scope:** Use for monitoring, control and measurement equipment. Machinery that converts or stores energy belongs under Converter or Storage, not Device.

### DeviceAttribute

- **Label:** Device Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **DeviceAttribute**
- **Description:** Typing marker grouping attributes that apply to a Device; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Distribution

- **Label:** Distribution
- **Hierarchy:** (root)
- **Description:** Binned/frequency representation of the values in a Set: histogram bins for numeric values, category frequencies for categorical values.

### DistributionBin

- **Label:** Distribution Bin
- **Hierarchy:** (root)
- **Description:** One bin of a Distribution: a label, optional numeric bounds, and a frequency.

### DynamicAttribute

- **Label:** Dynamic Attribute
- **Hierarchy:** Thing > Attribute > **DynamicAttribute**
- **Description:** Attribute whose value varies over time and is backed by time series data
- **Definition:** An attribute whose value is a function of time rather than a single number; its data lives in linked TimeSeries nodes or external time series references.
- **Examples:** Electricity demand profile, wind speed series, outdoor temperature
- **Scope:** Link the data via hasTimeSeries or the time-series reference properties; forecasts use FutureTimeSeries, measurements HistoricTimeSeries.

### Efficiency

- **Label:** Efficiency
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ProcessAttribute > ConversionProcessAttribute > **Efficiency**
- **Description:** Conversion efficiency of a process
- **Default unit:** PERCENT

### ElectricityCarrier

- **Label:** Electricity Carrier
- **Hierarchy:** Component > EnergyCarrier > **ElectricityCarrier**
- **Description:** Energy carrier for electrical energy
- **Examples:** Grid electricity, self-generated PV electricity

### ElectricityCarrierAttribute

- **Label:** Electricity Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > **ElectricityCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Electricity Carrier; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### ElectricityDemandProfile

- **Label:** Electricity Demand Profile
- **Hierarchy:** Thing > Attribute > DynamicAttribute > **ElectricityDemandProfile**
- **Description:** A dynamic attribute representing the electricity demand over time
- **Default unit:** KiloW
- **Quantity kind:** Power

### ElectricityFlow

- **Label:** Electricity Flow
- **Hierarchy:** Component > Flow > EnergyCarrierFlow > **ElectricityFlow**
- **Description:** Flow of electrical energy between components
- **Default unit:** KiloW

### ElectricityMeter

- **Label:** Electricity Meter
- **Hierarchy:** Component > Device > Meter > **ElectricityMeter**
- **Description:** Meter recording cumulative electrical energy consumption or production
- **Default unit:** KiloW-HR

### EnergyCarrier

- **Label:** Energy Carrier
- **Hierarchy:** Component > **EnergyCarrier**
- **Description:** The medium or commodity form in which energy is stored, transported and consumed
- **Definition:** An energy vector: the commodity that carries energy through the system, independent of the infrastructure that moves it.
- **Synonyms:** Energy Commodity, Energy Vector
- **Examples:** Electricity, district heat, natural gas, hydrogen, biomass
- **Scope:** EnergyCarrier is the commodity (what), Flow is its movement (the transfer), Network is the infrastructure it moves through.

### EnergyCarrierAttribute

- **Label:** Energy Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **EnergyCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Energy Carrier; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### EnergyCarrierFlow

- **Label:** Energy Carrier Flow
- **Hierarchy:** Component > Flow > **EnergyCarrierFlow**
- **Description:** Flow of energy carriers between components
- **Examples:** Electricity flow, heat flow, gas flow

### EnergyCarrierFlowAttribute

- **Label:** Energy Carrier Flow Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > FlowAttribute > **EnergyCarrierFlowAttribute**
- **Description:** Typing marker grouping attributes that apply to a Energy Carrier Flow; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### EnergyConsumer

- **Label:** Energy Consumer
- **Hierarchy:** Component > **EnergyConsumer**
- **Description:** Component whose primary role is to consume energy
- **Definition:** A component that takes energy out of the system for an end use. Consumers are the demand side: they receive flows but do not transform them into another carrier.
- **Synonyms:** Demand, Energy Sink, Load
- **Examples:** A building heating load, an EV charging station, an industrial process line
- **Scope:** Use for demand-side entities. A component that transforms energy onward rather than consuming it is a Converter.

### EnergyConsumerAttribute

- **Label:** Energy Consumer Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **EnergyConsumerAttribute**
- **Description:** Typing marker grouping attributes that apply to a Energy Consumer; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### EnergyConverter

- **Label:** Energy Converter
- **Hierarchy:** Component > Converter > **EnergyConverter**
- **Description:** Converter transforming energy between carriers or forms
- **Examples:** Heat pump, boiler, fuel cell, inverter, wind turbine generator

### EnergyConverterAttribute

- **Label:** Energy Converter Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ConverterAttribute > **EnergyConverterAttribute**
- **Description:** Typing marker grouping attributes that apply to a Energy Converter; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### EnergyGenerator

- **Label:** Energy Generator
- **Hierarchy:** Component > **EnergyGenerator**
- **Description:** Component whose primary role is to produce energy
- **Definition:** A component that injects energy into the system. Generators are the supply side: the equipment that produces an energy carrier from a resource or fuel.
- **Synonyms:** Energy Source, Generator, Power Plant, Producer
- **Examples:** PV plant, diesel genset, CHP unit
- **Scope:** The generating equipment is an EnergyGenerator (or a Converter subclass such as Turbine); the site it stands on (e.g. a wind park as a place) is a Location.

### EnergyGeneratorAttribute

- **Label:** EnergyGenerator Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **EnergyGeneratorAttribute**
- **Description:** Typing marker grouping attributes that apply to a Energy Generator; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### EnergyStorage

- **Label:** Energy Storage
- **Hierarchy:** Component > Storage > **EnergyStorage**
- **Description:** Storage holding energy for later use
- **Examples:** Battery, thermal storage tank, hydrogen storage

### EnergyStorageAttribute

- **Label:** Energy Storage Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > StorageAttribute > **EnergyStorageAttribute**
- **Description:** Typing marker grouping attributes that apply to a Energy Storage; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### EventAttribute

- **Label:** Event Attribute
- **Hierarchy:** Thing > Attribute > **EventAttribute**
- **Description:** Attribute describing discrete events in time
- **Examples:** Outage event, maintenance window

### Flow

- **Label:** Flow
- **Hierarchy:** Component > **Flow**
- **Description:** Represents the movement or transfer of energy, materials, or information between components
- **Definition:** A flow captures the dynamic transfer of entities (energy carriers, materials, etc.) between system components, including quantity, direction, and temporal characteristics
- **Synonyms:** Stream, Transfer
- **Examples:** Electricity flow from the grid to a building; heat flow from a plant into a district network
- **Scope:** A Flow connects a source Component to a destination Component (hasSource / hasDestination) and carries a Resource or EnergyCarrier (carriesResource). Use the typed subclasses (ElectricityFlow, HeatFlow, ...) where one fits.

### FlowAttribute

- **Label:** Flow Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **FlowAttribute**
- **Description:** Typing marker grouping attributes that apply to a Flow; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### FlowCapacity

- **Label:** Flow Capacity
- **Hierarchy:** Thing > Attribute > ComponentAttribute > FlowAttribute > **FlowCapacity**
- **Description:** Maximum flow rate capacity
- **Default unit:** KiloW

### FlowRate

- **Label:** Flow Rate
- **Hierarchy:** Thing > Attribute > ComponentAttribute > FlowAttribute > **FlowRate**
- **Description:** Rate of flow over time
- **Default unit:** KiloW

### FlowSensor

- **Label:** Flow Sensor
- **Hierarchy:** Component > Device > Sensor > **FlowSensor**
- **Description:** Sensor measuring volumetric or mass flow rate
- **Default unit:** M3-PER-SEC

### FuelCarrier

- **Label:** Fuel Carrier
- **Hierarchy:** Component > EnergyCarrier > **FuelCarrier**
- **Description:** Combustible energy carrier
- **Synonyms:** Fuel
- **Examples:** Natural gas, heating oil, wood pellets, hydrogen

### FuelCarrierAttribute

- **Label:** Fuel Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > **FuelCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Fuel Carrier; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### FutureTimeSeries

- **Label:** Future Time Series
- **Hierarchy:** TimeSeries > **FutureTimeSeries**
- **Description:** Time series data representing forecasted or projected future values
- **Synonyms:** Forecast, Prediction, Projection
- **Scope:** A wind, weather or demand forecast attaches to a DynamicAttribute via hasFutureTimeSeries.

### GasFlow

- **Label:** Gas Flow
- **Hierarchy:** Component > Flow > EnergyCarrierFlow > **GasFlow**
- **Description:** Flow of gaseous fuel between components
- **Default unit:** M3-PER-SEC

### GasMeter

- **Label:** Gas Meter
- **Hierarchy:** Component > Device > Meter > **GasMeter**
- **Description:** Meter recording cumulative gas volume consumed
- **Default unit:** M3

### GaseousFuelCarrier

- **Label:** Gaseous Fuel Carrier
- **Hierarchy:** Component > EnergyCarrier > FuelCarrier > **GaseousFuelCarrier**
- **Description:** Fuel carrier in gaseous form
- **Examples:** Natural gas, biogas, hydrogen

### GaseousFuelCarrierAttribute

- **Label:** Gaseous Fuel Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > FuelCarrierAttribute > **GaseousFuelCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Gaseous Fuel Carrier; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### GeospatialAttribute

- **Label:** Geospatial Attribute
- **Hierarchy:** Thing > Attribute > **GeospatialAttribute**
- **Description:** Attribute holding geographic data such as coordinates or geometries
- **Definition:** An attribute whose value is geographic: coordinates, geometries or other spatial references locating a component on a map.
- **Examples:** Latitude and longitude of a site; a boundary polygon

### GroupedSet

- **Label:** Grouped Set
- **Hierarchy:** Collection > **GroupedSet**
- **Description:** A partition of an attribute type over the distinct values of a grouping attribute type on the same components (SQL GROUP BY analogue). Members are Sets, one per group key.

### HeatCarrier

- **Label:** Heat Carrier
- **Hierarchy:** Component > EnergyCarrier > ThermalEnergyCarrier > **HeatCarrier**
- **Description:** Thermal energy carrier delivering heat
- **Examples:** District heating water, steam

### HeatCarrierAttribute

- **Label:** Heat Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > ThermalEnergyCarrierAttribute > **HeatCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Heat Carrier; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### HeatFlow

- **Label:** Heat Flow
- **Hierarchy:** Component > Flow > EnergyCarrierFlow > **HeatFlow**
- **Description:** Flow of thermal energy between components
- **Default unit:** KiloW

### HeatMeter

- **Label:** Heat Meter
- **Hierarchy:** Component > Device > Meter > **HeatMeter**
- **Description:** Meter recording cumulative thermal energy delivered
- **Default unit:** KiloW-HR

### HistoricTimeSeries

- **Label:** Historic Time Series
- **Hierarchy:** TimeSeries > **HistoricTimeSeries**
- **Description:** Time series data representing past measurements or observations
- **Synonyms:** Historical Data, Measured Data

### InformationFlow

- **Label:** Information Flow
- **Hierarchy:** Component > Flow > **InformationFlow**
- **Description:** Flow of information or control signals between components
- **Examples:** Sensor readings sent to a controller; a control signal sent to an actuator

### InformationFlowAttribute

- **Label:** Information Flow Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > FlowAttribute > **InformationFlowAttribute**
- **Description:** Typing marker grouping attributes that apply to a Information Flow; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Junction

- **Label:** Junction
- **Hierarchy:** Component > **Junction**
- **Description:** Component where multiple flows meet or diverge
- **Definition:** Junctions represent nodes where flows can be split, merged, or redirected without transformation
- **Synonyms:** Bus, Connection Point, Node
- **Examples:** Electrical busbar, pipe tee, district-heating manifold

### JunctionAttribute

- **Label:** Junction Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **JunctionAttribute**
- **Description:** Typing marker grouping attributes that apply to a Junction; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### LiquidFuel

- **Label:** Liquid Fuel Carrier
- **Hierarchy:** Component > EnergyCarrier > FuelCarrier > **LiquidFuel**
- **Description:** Fuel carrier in liquid form
- **Examples:** Heating oil, diesel, biofuel

### LiquidFuelCarrierAttribute

- **Label:** Liquid Fuel Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > FuelCarrierAttribute > **LiquidFuelCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Liquid Fuel; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### LiquidFuelFlow

- **Label:** Liquid Fuel Flow
- **Hierarchy:** Component > Flow > EnergyCarrierFlow > **LiquidFuelFlow**
- **Description:** Flow of liquid fuel between components
- **Default unit:** L-PER-SEC

### LiveTimeSeries

- **Label:** Live Time Series
- **Hierarchy:** TimeSeries > **LiveTimeSeries**
- **Description:** Time series data representing real-time or near real-time measurements
- **Synonyms:** Live Feed, Real-time Data

### Location

- **Label:** Location
- **Hierarchy:** Component > **Location**
- **Description:** Spatial entity representing geographic areas or specific sites
- **Definition:** Locations provide spatial context for components and flows, enabling geographic analysis and constraints
- **Synonyms:** Area, District, Place, Region, Site, Zone
- **Examples:** A wind park, a city district, a campus, a building plot, a municipality
- **Scope:** Use as the parent for spatial grouping concepts: a WindPark or a Campus is a Location. Do not use Network (connectivity infrastructure) or Junction (flow nodes) for spatial grouping. Components attach to a Location via dici_onto:locatedAt.

### LocationAttribute

- **Label:** Location Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **LocationAttribute**
- **Description:** Typing marker grouping attributes that apply to a Location; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Material

- **Label:** Material
- **Hierarchy:** Component > **Material**
- **Description:** Physical substance handled by the system that is not primarily an energy carrier
- **Definition:** A physical substance moved, stored or processed by the system - water, waste, feedstock - as opposed to an EnergyCarrier, whose role is to carry energy.
- **Examples:** Water, waste, construction material, industrial feedstock

### MaterialAttribute

- **Label:** Material Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **MaterialAttribute**
- **Description:** Typing marker grouping attributes that apply to a Material; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### MaterialConverter

- **Label:** Material Converter
- **Hierarchy:** Component > Converter > **MaterialConverter**
- **Description:** Converter transforming material inputs into different material outputs
- **Examples:** Waste incinerator, biogas digester, recycling plant

### MaterialConverterAttribute

- **Label:** Material Converter Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ConverterAttribute > **MaterialConverterAttribute**
- **Description:** Typing marker grouping attributes that apply to a Material Converter; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### MaterialFlow

- **Label:** Material Flow
- **Hierarchy:** Component > Flow > **MaterialFlow**
- **Description:** Flow of materials between components
- **Examples:** Waste stream, water supply, feedstock delivery

### MaterialFlowAttribute

- **Label:** Material Flow Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > FlowAttribute > **MaterialFlowAttribute**
- **Description:** Typing marker grouping attributes that apply to a Material Flow; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### MaterialStorage

- **Label:** Material Storage
- **Hierarchy:** Component > Storage > **MaterialStorage**
- **Description:** Storage holding materials
- **Examples:** Water reservoir, silo, warehouse, fuel depot

### MaterialStorageAttribute

- **Label:** Material Storage Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > StorageAttribute > **MaterialStorageAttribute**
- **Description:** Typing marker grouping attributes that apply to a Material Storage; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### MeasurementAccuracy

- **Label:** Measurement Accuracy
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > **MeasurementAccuracy**
- **Description:** Accuracy specification of a measuring device
- **Default unit:** PERCENT

### MeasurementValue

- **Label:** Measurement Value
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > SensorAttribute > **MeasurementValue**
- **Description:** Current measured value from a sensor

### Meter

- **Label:** Meter
- **Hierarchy:** Component > Device > **Meter**
- **Description:** Device that measures and records consumption or production of resources
- **Definition:** Meters measure cumulative quantities like energy consumption, flow volumes, or resource usage over time
- **Synonyms:** Metering Device
- **Examples:** Electricity meter, gas meter, heat meter
- **Scope:** Meters record cumulative consumption or production over time; instantaneous physical quantities are measured by Sensors.

### MeterAttribute

- **Label:** Meter Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > **MeterAttribute**
- **Description:** Typing marker grouping attributes that apply to a Meter; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### MeterReading

- **Label:** Meter Reading
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > MeterAttribute > **MeterReading**
- **Description:** Cumulative measurement from a meter

### Network

- **Label:** Network
- **Hierarchy:** Component > **Network**
- **Description:** Infrastructure for transporting energy carriers or materials
- **Definition:** Networks represent the physical infrastructure that enables flows between components, such as electrical grids, gas pipelines, or district heating networks
- **Synonyms:** Distribution Network, Grid, Infrastructure Network
- **Examples:** Electricity distribution grid, gas pipeline network, district heating network
- **Scope:** Network is the connective infrastructure through which flows move; the moving quantity itself is a Flow, and spatial grouping is a Location.

### NetworkAttribute

- **Label:** Network Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **NetworkAttribute**
- **Description:** Typing marker grouping attributes that apply to a Network; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### NonRenewableResource

- **Label:** Non Renewable Resource
- **Hierarchy:** Component > Resource > **NonRenewableResource**
- **Description:** Finite resource that does not replenish on a human timescale
- **Examples:** Coal, crude oil, natural gas reserves

### NonRenewableResourceAttribute

- **Label:** Non Renewable Resource Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ResourceAttribute > **NonRenewableResourceAttribute**
- **Description:** Typing marker grouping attributes that apply to a Non Renewable Resource; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### PhysicalAttribute

- **Label:** Physical Attribute
- **Hierarchy:** Thing > Attribute > **PhysicalAttribute**
- **Description:** Attribute holding a numeric physical quantity with a unit
- **Definition:** An attribute whose value is a single numeric quantity carrying a QUDT unit, e.g. a rated power in kilowatts or an area in square metres.
- **Examples:** Rated power (kW), rotor diameter (m), floor area (m2)
- **Scope:** Use when the value is a number with a QUDT unit. Enumerated values are CategoricalAttribute; time-varying values are DynamicAttribute.

### PowerSensor

- **Label:** Power Sensor
- **Hierarchy:** Component > Device > Sensor > **PowerSensor**
- **Description:** Sensor measuring instantaneous electrical or thermal power
- **Default unit:** KiloW

### PressureSensor

- **Label:** Pressure Sensor
- **Hierarchy:** Component > Device > Sensor > **PressureSensor**
- **Description:** Sensor measuring pressure
- **Default unit:** PA

### Process

- **Label:** Process
- **Hierarchy:** Component > **Process**
- **Description:** A process that transforms, transports, or modifies flows of energy or materials
- **Definition:** A process represents any activity or operation that has input and output flows, including energy conversion, material transformation, or transport operations
- **Synonyms:** Activity, Operation
- **Examples:** Space heating, combustion in a boiler, charging a battery
- **Scope:** A Process is the activity; the equipment performing it is a Component subclass (Converter, Storage, ...).

### ProcessAttribute

- **Label:** Process Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **ProcessAttribute**
- **Description:** Typing marker grouping attributes that apply to a Process; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### ProcessCapacity

- **Label:** Process Capacity
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ProcessAttribute > **ProcessCapacity**
- **Description:** Maximum processing capacity
- **Default unit:** KiloW

### Reference

- **Label:** Reference
- **Hierarchy:** (root)
- **Description:** A citable information source (report, paper, dataset, website) that replica or scenario data points to as provenance. Instances are created from the Reference sheet of the ingestion template
- **Synonyms:** Citation, Source
- **Examples:** A journal article identified by DOI backing an efficiency value

### ReferenceType

- **Label:** Reference Type
- **Hierarchy:** (root)
- **Description:** Kind of citable source a Reference is; the allowed values are its named individuals
- **Examples:** DOI

### RenewableResource

- **Label:** Renewable Resource
- **Hierarchy:** Component > Resource > **RenewableResource**
- **Description:** Resource that replenishes naturally on a human timescale
- **Examples:** Wind, solar irradiation, hydro, geothermal heat

### RenewableResourceAttribute

- **Label:** Renewable Resource Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ResourceAttribute > **RenewableResourceAttribute**
- **Description:** Typing marker grouping attributes that apply to a Renewable Resource; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Resource

- **Label:** Resource
- **Hierarchy:** Component > **Resource**
- **Description:** Primary source of energy or material drawn from the environment
- **Definition:** A natural or primary resource that the system harvests, extracts or depends on, as distinct from the processed energy carriers derived from it.
- **Synonyms:** Natural Resource, Primary Resource
- **Examples:** Wind, solar irradiation, groundwater, coal deposit
- **Scope:** The wind blowing over a site is a Resource; the electricity generated from it is an ElectricityCarrier; the machine converting it is a Turbine.

### ResourceAttribute

- **Label:** Resource Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **ResourceAttribute**
- **Description:** Typing marker grouping attributes that apply to a Resource; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### SamplingRate

- **Label:** Sampling Rate
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > SensorAttribute > **SamplingRate**
- **Description:** Frequency of measurements or readings
- **Default unit:** HZ

### Scenario

- **Label:** Scenario
- **Hierarchy:** (root)
- **Description:** A what-if container: a named snapshot of replica components with attribute overrides
- **Definition:** A named what-if case built from a digital replica: it references the replica components involved and carries only the attribute values that differ from the replica baseline.
- **Synonyms:** Case, Simulation Case, Variant
- **Examples:** A baseline scenario; a heat-pump-retrofit scenario derived from it with modified heating attributes
- **Scope:** Scenarios are thin: they reference the replica's components and carry only superseding attributes marked with usedInScenario.

### Sensor

- **Label:** Sensor
- **Hierarchy:** Component > Device > **Sensor**
- **Description:** Device that measures physical quantities and converts them to signals
- **Definition:** Sensors detect and respond to inputs from the physical environment, providing data for monitoring and control
- **Synonyms:** Detector, Measuring Device, Probe
- **Examples:** Temperature sensor, pressure sensor, anemometer, pyranometer

### SensorAttribute

- **Label:** Sensor Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > **SensorAttribute**
- **Description:** Typing marker grouping attributes that apply to a Sensor; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Service

- **Label:** Service
- **Hierarchy:** (root)
- **Description:** An external model or tool (simulator, optimizer, forecaster) that consumes scenarios and returns results
- **Definition:** An external computational model reachable from the platform - a simulator, optimizer or forecaster - that consumes a converted scenario payload and returns results.
- **Synonyms:** External Service, Model, Tool
- **Examples:** Energy simulator, flexibility optimizer, wind power forecaster

### ServiceRequirement

- **Label:** Service Requirement
- **Hierarchy:** (root)
- **Description:** Declares an input a Service requires from a scenario: a component, an attribute, or a link between components
- **Definition:** A machine-readable statement of one input a Service needs from a scenario: a component of a given type, an attribute on it, or a link between two components.
- **Examples:** A wind power forecaster requiring a Location with a wind speed DynamicAttribute

### Set

- **Label:** Set
- **Hierarchy:** Collection > **Set**
- **Description:** A collection of attribute instances of a single attribute type, drawn from one workspace replica (optionally restricted to one data source), or one partition of a GroupedSet. Carries descriptive statistics.

### SetPoint

- **Label:** Set Point
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > ControllerAttribute > **SetPoint**
- **Description:** Target value for a controller

### SimpleCostAttribute

- **Label:** Simple Cost Attribute
- **Hierarchy:** Thing > Attribute > **SimpleCostAttribute**
- **Description:** Attribute holding a plain monetary value
- **Examples:** Investment cost in EUR

### SimpleValueAttribute

- **Label:** Simple Value Attribute
- **Hierarchy:** Thing > Attribute > **SimpleValueAttribute**
- **Description:** Attribute holding a plain literal value without unit semantics

### SolarResource

- **Label:** Solar Resource
- **Hierarchy:** Component > Resource > RenewableResource > **SolarResource**
- **Description:** Solar irradiation as a harvestable renewable energy resource
- **Synonyms:** Insolation, Solar Irradiation

### SolarResourceAttribute

- **Label:** Solar Resource Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ResourceAttribute > RenewableResourceAttribute > **SolarResourceAttribute**
- **Description:** Typing marker grouping attributes that apply to a Solar Resource; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### SolidFuel

- **Label:** Solid Fuel Carrier
- **Hierarchy:** Component > EnergyCarrier > FuelCarrier > **SolidFuel**
- **Description:** Fuel carrier in solid form
- **Examples:** Wood chips, pellets, coal

### SolidFuelCarrierAttribute

- **Label:** Solid Fuel Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > FuelCarrierAttribute > **SolidFuelCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Solid Fuel; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### StateOfCharge

- **Label:** State of Charge
- **Hierarchy:** Thing > Attribute > ComponentAttribute > StorageAttribute > EnergyStorageAttribute > **StateOfCharge**
- **Description:** Current state of charge as percentage of capacity
- **Default unit:** PERCENT

### StaticAttribute

- **Label:** Static Attribute
- **Hierarchy:** Thing > Attribute > **StaticAttribute**
- **Description:** Attribute whose value does not change over the modelled time horizon

### Storage

- **Label:** Storage
- **Hierarchy:** Component > **Storage**
- **Description:** Component that stores energy or materials over time
- **Definition:** Storage components accumulate and release energy or materials, providing temporal flexibility to the system
- **Synonyms:** Buffer, Reservoir, Store
- **Examples:** Battery, hot water tank, pumped hydro reservoir, hydrogen store

### StorageAttribute

- **Label:** Storage Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > **StorageAttribute**
- **Description:** Typing marker grouping attributes that apply to a Storage; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### StorageCapacity

- **Label:** Storage Capacity
- **Hierarchy:** Thing > Attribute > ComponentAttribute > StorageAttribute > **StorageCapacity**
- **Description:** Maximum storage capacity
- **Default unit:** KiloW-HR

### StorageProcess

- **Label:** Storage Process
- **Hierarchy:** Component > Process > **StorageProcess**
- **Description:** Process that stores and releases energy or materials over time
- **Examples:** Charging and discharging a battery; filling a thermal store

### StorageProcessAttribute

- **Label:** Storage Process Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ProcessAttribute > **StorageProcessAttribute**
- **Description:** Typing marker grouping attributes that apply to a Storage Process; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Switch

- **Label:** Switch
- **Hierarchy:** Component > Device > **Switch**
- **Description:** Device that can interrupt or divert the flow of energy or materials
- **Definition:** Switches control the routing or interruption of flows in the system
- **Examples:** Relay, circuit breaker, transfer switch

### SwitchAttribute

- **Label:** Switch Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > **SwitchAttribute**
- **Description:** Typing marker grouping attributes that apply to a Switch; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### SwitchState

- **Label:** Switch State
- **Hierarchy:** Thing > Attribute > ComponentAttribute > DeviceAttribute > SwitchAttribute > **SwitchState**
- **Description:** Current state of a switch (open/closed, on/off)

### TemperatureSensor

- **Label:** Temperature Sensor
- **Hierarchy:** Component > Device > Sensor > **TemperatureSensor**
- **Description:** Sensor measuring temperature
- **Default unit:** DEG_C

### TemporalPrecision

- **Label:** Temporal Precision
- **Hierarchy:** (root)
- **Description:** Granularity of an event attribute temporal value; the allowed values are its named individuals
- **Examples:** Year, Year-Month, Date, Date-Time, Unknown

### ThermalEnergyCarrier

- **Label:** Thermal Energy Carrier
- **Hierarchy:** Component > EnergyCarrier > **ThermalEnergyCarrier**
- **Description:** Energy carrier transporting thermal energy (heat or cold)

### ThermalEnergyCarrierAttribute

- **Label:** Thermal Energy Carrier Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > EnergyCarrierAttribute > **ThermalEnergyCarrierAttribute**
- **Description:** Typing marker grouping attributes that apply to a Thermal Energy Carrier; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### TimeSeries

- **Label:** Time Series
- **Hierarchy:** (root)
- **Description:** A sequence of data points indexed in time order, typically used to represent dynamic attributes over time
- **Definition:** A time series is a series of data points indexed (or listed or graphed) in time order. Time series data is used to track changes over time for dynamic attributes.
- **Synonyms:** Data Series, Profile, Timeseries
- **Examples:** Hourly electricity demand for 2024; a 48-hour wind speed forecast

### TransportProcess

- **Label:** Transport Process
- **Hierarchy:** Component > Process > **TransportProcess**
- **Description:** Process that transports energy or materials without transformation
- **Examples:** Pumping water through a pipe; transmitting electricity over a line

### TransportProcessAttribute

- **Label:** Transport Process Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ProcessAttribute > **TransportProcessAttribute**
- **Description:** Typing marker grouping attributes that apply to a Transport Process; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### Turbine

- **Label:** Turbine
- **Hierarchy:** Component > Converter > EnergyConverter > **Turbine**
- **Description:** Rotary energy converter extracting mechanical work from a moving fluid
- **Synonyms:** Gas Turbine, Hydro Turbine, Steam Turbine, Wind Turbine
- **Examples:** A wind turbine in a wind park; a steam turbine in a CHP plant
- **Scope:** A WindTurbine extension class belongs here (under Turbine), while the wind park it stands in is a Location and the wind it harvests is a Wind resource.

### TurbineAttribute

- **Label:** Turbine Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ConverterAttribute > EnergyConverterAttribute > **TurbineAttribute**
- **Description:** Typing marker grouping attributes that apply to a Turbine; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

### UnitBasedCostAttribute

- **Label:** Unit Based Cost Attribute
- **Hierarchy:** Thing > Attribute > **UnitBasedCostAttribute**
- **Description:** Attribute holding a cost per unit of some quantity
- **Examples:** Energy price in EUR per kWh

### Valve

- **Label:** Valve
- **Hierarchy:** Component > Device > Actuator > **Valve**
- **Description:** Actuator that controls fluid flow

### Wind

- **Label:** Wind Resource
- **Hierarchy:** Component > Resource > RenewableResource > **Wind**
- **Description:** The wind as a harvestable renewable energy resource
- **Synonyms:** Wind Energy, Wind Potential
- **Examples:** The wind resource at a wind park site, characterised by speed and direction profiles
- **Scope:** Use for the wind resource itself. A wind park (the site) maps to Location; a wind turbine (the machine) maps to Turbine; forecast wind speeds are DynamicAttributes with a FutureTimeSeries.

### WindResourceAttribute

- **Label:** Wind Resource Attribute
- **Hierarchy:** Thing > Attribute > ComponentAttribute > ResourceAttribute > RenewableResourceAttribute > **WindResourceAttribute**
- **Description:** Typing marker grouping attributes that apply to a Wind; lets SPARQL select all attributes of one component type via rdfs:subClassOf*

## Object properties

### actuates

- **Label:** actuates
- **Hierarchy:** linksComponent > controls > **actuates**
- **Description:** Actuator physically controls a component
- **Domain:** Actuator
- **Range:** Component

### aggregateOf

- **Label:** aggregate of
- **Hierarchy:** (root)
- **Description:** Links a projected aggregate attribute node back to the group Set it summarizes — the Set carries the full statistics and membership.
- **Domain:** AggregateAttribute
- **Range:** Set

### aggregatedIn

- **Label:** aggregated in
- **Hierarchy:** (root)
- **Description:** Links an attribute instance to a Set it is a member of. The materializer asserts only this direction; query the other with ^aggregatedIn.
- **Domain:** Attribute
- **Range:** Set

### assumptionObjectProperty

- **Label:** assumption object property
- **Hierarchy:** (root)
- **Description:** Root property for links from an Assumption to its targets

### basedOn

- **Label:** based on
- **Hierarchy:** (root)
- **Description:** Links a derived scenario to the baseline scenario it was derived from. Scenario-provenance link written by the platform assumptions tooling
- **Domain:** Scenario
- **Range:** Scenario

### carriesEnergyCarrier

- **Label:** carries energy carrier
- **Hierarchy:** carriesResource > **carriesEnergyCarrier**
- **Description:** The energy carrier being transported by the flow
- **Domain:** EnergyCarrierFlow
- **Range:** EnergyCarrier

### carriesResource

- **Label:** carries resource
- **Hierarchy:** (root)
- **Description:** The resource (energy carrier or material) being transported by the flow
- **Domain:** Flow
- **Range:** Resource

### contains

- **Label:** contains
- **Hierarchy:** linksComponent > **contains**
- **Description:** A component spatially or logically contains another component

### controls

- **Label:** controls
- **Hierarchy:** linksComponent > **controls**
- **Description:** Device controls another component
- **Domain:** Device
- **Range:** Component

### currency

- **Label:** currency
- **Hierarchy:** topObjectProperty > **currency**
- **Description:** Currency unit of a cost attribute
- **Range:** CurrencyUnit

### derivedFrom

- **Label:** derived from
- **Hierarchy:** (root)
- **Description:** Scenario provenance: this scenario was derived from another scenario
- **Domain:** Scenario
- **Range:** Scenario

### derivedFromDataSet

- **Label:** derived from data set
- **Hierarchy:** (root)
- **Description:** Provenance link from a Collection back to the data source (Reference) it was restricted to. Absent when the Collection covers the whole workspace replica.
- **Domain:** Collection

### fedBy

- **Label:** fed by
- **Hierarchy:** linksComponent > **fedBy**
- **Description:** Supply relationship: this component is fed by another component
- **Domain:** Component
- **Range:** Component

### feeds

- **Label:** feeds
- **Hierarchy:** linksComponent > **feeds**
- **Description:** Supply relationship: this component feeds another component

### flowsThrough

- **Label:** flows through
- **Hierarchy:** linksComponent > **flowsThrough**
- **Description:** Locations traversed by a flow
- **Domain:** Flow
- **Range:** Location

### groupComponent

- **Label:** group component
- **Hierarchy:** (root)
- **Description:** The component instance whose linked components this group's members belong to. Present only on Sets of a component-grouped GroupedSet.
- **Domain:** Set

### groupedBy

- **Label:** grouped by
- **Hierarchy:** (root)
- **Description:** What partitions the members: an attribute class whose values are the group keys (class-as-value, e.g. dici_onto:PostalCode), or a component class whose instances are the groups — each member's owner is linked to that instance via a linksComponent-family edge (e.g. dici_onto:WindPark for per-park turbine statistics).
- **Domain:** GroupedSet

### hasActorAttribute

- **Label:** has actor attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasActorAttribute**
- **Description:** Attaches a Actor attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Actor
- **Range:** ActorAttribute

### hasActuatorAttribute

- **Label:** has actuator attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasDeviceAttribute > **hasActuatorAttribute**
- **Description:** Attaches a Actuator attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Actuator
- **Range:** ActuatorAttribute

### hasAttribute

- **Label:** has Attribute
- **Hierarchy:** (root)
- **Description:** Attaches an Attribute node to a Component; root of the has-attribute property hierarchy
- **Domain:** Component
- **Range:** Attribute

### hasBin

- **Label:** has bin
- **Hierarchy:** (root)
- **Description:** One bin of this Distribution.
- **Domain:** Distribution
- **Range:** DistributionBin

### hasColdAttribute

- **Label:** has cold attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > hasThermalEnergyAttribute > **hasColdAttribute**
- **Description:** Attaches a Cold attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** ColdCarrier

### hasColdCarrierAttribute

- **Label:** has cold carrier attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > hasThermalEnergyCarrierAttribute > **hasColdCarrierAttribute**
- **Description:** Attaches a Cold Carrier attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** ColdCarrier
- **Range:** ColdCarrierAttribute

### hasComponentAttribute

- **Label:** has component attribute
- **Hierarchy:** hasAttribute > **hasComponentAttribute**
- **Description:** Attaches a component attribute to a Component; parent of the per-component-type attachment properties

### hasControllerAttribute

- **Label:** has controller attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasDeviceAttribute > **hasControllerAttribute**
- **Description:** Attaches a Controller attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Controller
- **Range:** ControllerAttribute

### hasConversionProcessAttribute

- **Label:** has conversion process attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasProcessAttribute > **hasConversionProcessAttribute**
- **Description:** Attaches a Conversion Process attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** ConversionProcess
- **Range:** ConversionProcessAttribute

### hasConverterAttribute

- **Label:** has converter attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasConverterAttribute**
- **Description:** Attaches a Converter attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Converter

### hasDescriptiveStatistics

- **Label:** has descriptive statistics
- **Hierarchy:** (root)
- **Description:** The aggregate statistics computed over this Set's members.
- **Domain:** Set
- **Range:** DescriptiveStatistics

### hasDestination

- **Label:** has destination
- **Hierarchy:** linksComponent > **hasDestination**
- **Description:** The component to which the flow is directed
- **Domain:** Flow
- **Range:** Component

### hasDeviceAttribute

- **Label:** has device attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasDeviceAttribute**
- **Description:** Attaches a Device attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Device
- **Range:** DeviceAttribute

### hasDistribution

- **Label:** has distribution
- **Hierarchy:** (root)
- **Description:** The binned/frequency representation of this Set's values.
- **Domain:** Set
- **Range:** Distribution

### hasElectricityAttribute

- **Label:** has electricity attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > **hasElectricityAttribute**
- **Description:** Attaches a Electricity attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** ElectricityCarrier

### hasEnergyCarrierAttribute

- **Label:** has energy carrier attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasEnergyCarrierAttribute**
- **Description:** Attaches a Energy Carrier attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** EnergyCarrier

### hasEnergyCarrierEnergyCostAttribute

- **Label:** has energy carrier energy cost attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > **hasEnergyCarrierEnergyCostAttribute**
- **Description:** Attaches a Energy Carrier Energy Cost attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute

### hasEnergyCarrierFlowAttribute

- **Label:** has energy carrier flow attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasFlowAttribute > **hasEnergyCarrierFlowAttribute**
- **Description:** Attaches a Energy Carrier Flow attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** EnergyCarrierFlow
- **Range:** EnergyCarrierFlowAttribute

### hasEnergyConsumerAttribute

- **Label:** has energy consumer attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasEnergyConsumerAttribute**
- **Description:** Attaches a Energy Consumer attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** EnergyConsumer

### hasEnergyConverterAttribute

- **Label:** has energy converter attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasConverterAttribute > **hasEnergyConverterAttribute**
- **Description:** Attaches a Energy Converter attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** EnergyConverter

### hasEnergyGeneratorAttribute

- **Label:** has energy generator attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasEnergyGeneratorAttribute**
- **Description:** Attaches a Energy Generator attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** EnergyGenerator

### hasEnergyStorageAttribute

- **Label:** has energy storage attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasStorageAttribute > **hasEnergyStorageAttribute**
- **Description:** Attaches a Energy Storage attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** EnergyStorage
- **Range:** EnergyStorageAttribute

### hasFlowAttribute

- **Label:** has flow attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasFlowAttribute**
- **Description:** Attaches a Flow attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Flow
- **Range:** FlowAttribute

### hasFuelAttribute

- **Label:** has fuel attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > **hasFuelAttribute**
- **Description:** Attaches a Fuel attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** FuelCarrier

### hasFutureTimeSeries

- **Label:** has future time series
- **Hierarchy:** hasTimeSeries > **hasFutureTimeSeries**
- **Description:** Links a dynamic attribute to forecast time series data

### hasGaseousFuelAttribute

- **Label:** has gaseous fuel attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > hasFuelAttribute > **hasGaseousFuelAttribute**
- **Description:** Attaches a Gaseous Fuel attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** GaseousFuelCarrier

### hasGroup

- **Label:** has group
- **Hierarchy:** (root)
- **Description:** Links a GroupedSet to one member Set per distinct group key.
- **Domain:** GroupedSet
- **Range:** Set

### hasHeatAttribute

- **Label:** has heat attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > hasThermalEnergyAttribute > **hasHeatAttribute**
- **Description:** Attaches a Heat attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** HeatCarrier

### hasHeatCarrierAttribute

- **Label:** has heat carrier attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > hasThermalEnergyCarrierAttribute > **hasHeatCarrierAttribute**
- **Description:** Attaches a Heat Carrier attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** HeatCarrier
- **Range:** HeatCarrierAttribute

### hasHistoricTimeSeries

- **Label:** has historic time series
- **Hierarchy:** hasTimeSeries > **hasHistoricTimeSeries**
- **Description:** Links a dynamic attribute to measured historical time series data

### hasIdentifier

- **Label:** has identifier
- **Hierarchy:** hasAttribute > **hasIdentifier**
- **Description:** Attaches an identifier attribute to a component

### hasInformationFlowAttribute

- **Label:** has information flow attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasFlowAttribute > **hasInformationFlowAttribute**
- **Description:** Attaches a Information Flow attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** InformationFlow
- **Range:** InformationFlowAttribute

### hasInput

- **Label:** has input
- **Hierarchy:** linksComponent > **hasInput**
- **Description:** Links a component to one of its inputs

### hasInputAttribute

- **Label:** has input attribute
- **Hierarchy:** (root)
- **Description:** A ServiceRequirement names the attribute it requires
- **Domain:** ServiceRequirement
- **Range:** Attribute

### hasInputEntity

- **Label:** has input entity
- **Hierarchy:** (root)
- **Description:** A ComponentLink or ServiceRequirement points at its source component
- **Domain:** ComponentLink, ServiceRequirement
- **Range:** Component

### hasInputFlow

- **Label:** has input flow
- **Hierarchy:** linksComponent > **hasInputFlow**
- **Description:** Links a component to its input flows
- **Domain:** Component
- **Range:** Flow

### hasJunctionAttribute

- **Label:** has junction attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasJunctionAttribute**
- **Description:** Attaches a Junction attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Junction
- **Range:** JunctionAttribute

### hasLiquidFuelAttribute

- **Label:** has liquid fuel attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > hasFuelAttribute > **hasLiquidFuelAttribute**
- **Description:** Attaches a Liquid Fuel attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** LiquidFuel
- **Range:** LiquidFuelCarrierAttribute

### hasLiveTimeSeries

- **Label:** has live time series
- **Hierarchy:** hasTimeSeries > **hasLiveTimeSeries**
- **Description:** Links a dynamic attribute to a real-time time series feed

### hasLocation

- **Label:** has location
- **Hierarchy:** linksComponent > **hasLocation**
- **Description:** Links a component to the Location it belongs to

### hasLocationAttribute

- **Label:** has location attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasLocationAttribute**
- **Description:** Attaches a Location attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Location
- **Range:** LocationAttribute

### hasMaterialAttribute

- **Label:** has material attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasMaterialAttribute**
- **Description:** Attaches a Material attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Material

### hasMaterialConverterAttribute

- **Label:** has material converter attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasConverterAttribute > **hasMaterialConverterAttribute**
- **Description:** Attaches a Material Converter attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** MaterialConverter

### hasMaterialFlowAttribute

- **Label:** has material flow attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasFlowAttribute > **hasMaterialFlowAttribute**
- **Description:** Attaches a Material Flow attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** MaterialFlow
- **Range:** MaterialFlowAttribute

### hasMaterialStorageAttribute

- **Label:** has material storage attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasStorageAttribute > **hasMaterialStorageAttribute**
- **Description:** Attaches a Material Storage attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** MaterialStorage
- **Range:** MaterialStorageAttribute

### hasMember

- **Label:** has member
- **Hierarchy:** (root)
- **Description:** Convenience inverse of aggregatedIn. Not asserted by the materializer — the collections graph is not closure-materialized; use ^aggregatedIn in queries.

### hasMeterAttribute

- **Label:** has meter attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasDeviceAttribute > **hasMeterAttribute**
- **Description:** Attaches a Meter attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Meter
- **Range:** MeterAttribute

### hasNetworkAttribute

- **Label:** has network attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasNetworkAttribute**
- **Description:** Attaches a Network attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Network
- **Range:** NetworkAttribute

### hasNonRenewableAttribute

- **Label:** has non renewable attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasResourceAttribute > **hasNonRenewableAttribute**
- **Description:** Attaches a Non Renewable attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** NonRenewableResource

### hasNonRenewableResourceAttribute

- **Label:** has non renewable resource attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasResourceAttribute > **hasNonRenewableResourceAttribute**
- **Description:** Attaches a Non Renewable Resource attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** NonRenewableResource
- **Range:** NonRenewableResourceAttribute

### hasOutputFlow

- **Label:** has output flow
- **Hierarchy:** linksComponent > **hasOutputFlow**
- **Description:** Links a component to its output flows
- **Domain:** Component
- **Range:** Flow

### hasPart

- **Label:** has part
- **Hierarchy:** linksComponent > **hasPart**
- **Description:** Whole-part composition: this component has another component as a part

### hasProcessAttribute

- **Label:** has process attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasProcessAttribute**
- **Description:** Attaches a Process attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Process
- **Range:** ProcessAttribute

### hasReferenceType

- **Label:** has reference type
- **Hierarchy:** (root)
- **Description:** The kind of citable source a Reference is (e.g. the DOI individual). Written from the ReferenceType column of the ingestion template's Reference sheet
- **Domain:** Reference
- **Range:** ReferenceType

### hasRenewableAttribute

- **Label:** has renewable attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasResourceAttribute > **hasRenewableAttribute**
- **Description:** Attaches a Renewable attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** RenewableResource

### hasRenewableResourceAttribute

- **Label:** has renewable resource attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasResourceAttribute > **hasRenewableResourceAttribute**
- **Description:** Attaches a Renewable Resource attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** RenewableResource
- **Range:** RenewableResourceAttribute

### hasResourceAttribute

- **Label:** has resource attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasResourceAttribute**
- **Description:** Attaches a Resource attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Resource

### hasSensorAttribute

- **Label:** has sensor attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasDeviceAttribute > **hasSensorAttribute**
- **Description:** Attaches a Sensor attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Sensor
- **Range:** SensorAttribute

### hasSet

- **Label:** has set
- **Hierarchy:** (root)
- **Description:** Links a data source (a Reference) to a Collection derived from it. Only asserted when a Collection was restricted to one data source.
- **Range:** Collection

### hasSolarAttribute

- **Label:** has solar attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasResourceAttribute > hasRenewableAttribute > **hasSolarAttribute**
- **Description:** Attaches a Solar attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** SolarResource

### hasSolidFuelAttribute

- **Label:** has solid fuel attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > hasFuelAttribute > **hasSolidFuelAttribute**
- **Description:** Attaches a Solid Fuel attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** SolidFuel

### hasSource

- **Label:** has source
- **Hierarchy:** linksComponent > **hasSource**
- **Description:** The component from which the flow originates
- **Domain:** Flow
- **Range:** Component

### hasStorageAttribute

- **Label:** has storage attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > **hasStorageAttribute**
- **Description:** Attaches a Storage attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Storage
- **Range:** StorageAttribute

### hasStorageProcessAttribute

- **Label:** has storage process attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasProcessAttribute > **hasStorageProcessAttribute**
- **Description:** Attaches a Storage Process attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** StorageProcess
- **Range:** StorageProcessAttribute

### hasSwitchAttribute

- **Label:** has switch attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasDeviceAttribute > **hasSwitchAttribute**
- **Description:** Attaches a Switch attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Switch
- **Range:** SwitchAttribute

### hasTemporalPrecision

- **Label:** has temporal precision
- **Hierarchy:** hasUnit > **hasTemporalPrecision**
- **Description:** Unit expressing the temporal precision of an attribute

### hasThermalEnergyAttribute

- **Label:** has thermal energy attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > **hasThermalEnergyAttribute**
- **Description:** Attaches a Thermal Energy attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** ThermalEnergyCarrier

### hasThermalEnergyCarrierAttribute

- **Label:** has thermal energy carrier attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasEnergyCarrierAttribute > **hasThermalEnergyCarrierAttribute**
- **Description:** Attaches a Thermal Energy Carrier attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** ThermalEnergyCarrier
- **Range:** ThermalEnergyCarrierAttribute

### hasTimeSeries

- **Label:** has time series
- **Hierarchy:** (root)
- **Description:** Links a dynamic attribute to its associated time series data
- **Domain:** DynamicAttribute
- **Range:** TimeSeries

### hasTransportProcessAttribute

- **Label:** has transport process attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasProcessAttribute > **hasTransportProcessAttribute**
- **Description:** Attaches a Transport Process attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** TransportProcess
- **Range:** TransportProcessAttribute

### hasTurbineAttribute

- **Label:** has turbine attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasConverterAttribute > hasEnergyConverterAttribute > **hasTurbineAttribute**
- **Description:** Attaches a Turbine attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Turbine
- **Range:** TurbineAttribute

### hasUnit

- **Label:** has unit
- **Hierarchy:** (root)
- **Description:** Links an attribute to its QUDT unit
- **Domain:** Attribute
- **Range:** Unit

### hasWindAttribute

- **Label:** has wind attribute
- **Hierarchy:** hasAttribute > hasComponentAttribute > hasResourceAttribute > hasRenewableAttribute > **hasWindAttribute**
- **Description:** Attaches a Wind attribute to its component; part of the has-attribute property hierarchy under dici_onto:hasAttribute
- **Domain:** Wind

### isAttributeOf

- **Label:** is attribute of
- **Hierarchy:** (root)
- **Description:** An attribute is required by a ServiceRequirement (inverse of hasInputAttribute)
- **Domain:** Attribute
- **Range:** ServiceRequirement

### isDestinationOf

- **Label:** is destination of
- **Hierarchy:** linksComponent > **isDestinationOf**
- **Description:** The component receives a flow (inverse of hasDestination)
- **Domain:** Component
- **Range:** Flow

### isEntityOf

- **Label:** is entity of
- **Hierarchy:** (root)
- **Description:** A component is the subject entity of a ServiceRequirement
- **Domain:** Component
- **Range:** ServiceRequirement

### isFutureTimeSeriesOf

- **Label:** is future time series of
- **Hierarchy:** isTimeSeriesOf > **isFutureTimeSeriesOf**
- **Description:** A forecast time series describes a dynamic attribute
- **Domain:** FutureTimeSeries
- **Range:** DynamicAttribute

### isHistoricTimeSeriesOf

- **Label:** is historic time series of
- **Hierarchy:** isTimeSeriesOf > **isHistoricTimeSeriesOf**
- **Description:** A historical time series describes a dynamic attribute
- **Domain:** HistoricTimeSeries
- **Range:** DynamicAttribute

### isLiveTimeSeriesOf

- **Label:** is live time series of
- **Hierarchy:** isTimeSeriesOf > **isLiveTimeSeriesOf**
- **Description:** A live time series describes a dynamic attribute
- **Domain:** LiveTimeSeries
- **Range:** DynamicAttribute

### isRequiredBy

- **Label:** is required by
- **Hierarchy:** (root)
- **Description:** A ServiceRequirement belongs to a Service (inverse of requires)
- **Domain:** ServiceRequirement
- **Range:** Service

### isSourceOf

- **Label:** is source of
- **Hierarchy:** linksComponent > **isSourceOf**
- **Description:** The component originates a flow (inverse of hasSource)
- **Domain:** Component
- **Range:** Flow

### isTimeSeriesOf

- **Label:** is time series of
- **Hierarchy:** (root)
- **Description:** Links a time series to the dynamic attribute it represents
- **Domain:** TimeSeries
- **Range:** DynamicAttribute

### linksComponent

- **Label:** links component
- **Hierarchy:** (root)
- **Description:** Root symmetric property for any component-to-component relationship
- **Domain:** Component
- **Range:** Component

### linksInputEntityTo

- **Label:** links input entity to
- **Hierarchy:** (root)
- **Description:** A ComponentLink points at its target component
- **Domain:** ComponentLink
- **Range:** Component

### linksInputyEntityTo

- **Label:** links input entity to (historical spelling)
- **Hierarchy:** linksInputEntityTo > **linksInputyEntityTo**
- **Description:** Historical misspelling of linksInputEntityTo that the platform scenario tooling writes in ComponentLink data. Declared a subproperty of the canonical property so semantic queries via linksInputEntityTo still find the data under RDFS inference. Do not use in new vocabularies or code
- **Domain:** ComponentLink
- **Range:** Component

### locatedAt

- **Label:** located at
- **Hierarchy:** linksComponent > **locatedAt**
- **Description:** Physical location of a component
- **Domain:** Component
- **Range:** Location

### locatedIn

- **Label:** located in
- **Hierarchy:** linksComponent > **locatedIn**
- **Description:** A Location is spatially contained within another Location
- **Domain:** Location

### locationOf

- **Label:** location of
- **Hierarchy:** linksComponent > **locationOf**
- **Description:** A Location hosts a component (inverse of the location attachment properties)

### measures

- **Label:** measures
- **Hierarchy:** (root)
- **Description:** Device measures a specific attribute
- **Domain:** Device
- **Range:** Attribute

### monitors

- **Label:** monitors
- **Hierarchy:** linksComponent > **monitors**
- **Description:** Device monitors another component
- **Domain:** Device
- **Range:** Component

### occursDuring

- **Label:** occurs during
- **Hierarchy:** linksComponent > **occursDuring**
- **Description:** Temporal association: one component or process occurs during another

### ofAttributeType

- **Label:** of attribute type
- **Hierarchy:** (root)
- **Description:** The attribute class whose instances this collection aggregates (class-as-value, e.g. dici_onto:RotorDiameter).
- **Domain:** Collection

### operates

- **Label:** operates
- **Hierarchy:** linksComponent > **operates**
- **Description:** Operational control relationship
- **Domain:** Actor
- **Range:** Component

### owns

- **Label:** owns
- **Hierarchy:** linksComponent > **owns**
- **Description:** Ownership relationship between actors and components
- **Domain:** Actor
- **Range:** Component

### partOf

- **Label:** part of
- **Hierarchy:** linksComponent > **partOf**
- **Description:** Whole-part composition: this component is part of another component

### realTimeSource

- **Label:** real-time source
- **Hierarchy:** (root)
- **Description:** Reference to a real-time data source for live dynamic attributes
- **Domain:** DynamicAttribute

### requires

- **Label:** requires
- **Hierarchy:** (root)
- **Description:** A Service requires a ServiceRequirement to be satisfied by the submitted scenario
- **Domain:** Service
- **Range:** ServiceRequirement

### supersedesAttribute

- **Label:** supersedes attribute
- **Hierarchy:** (root)
- **Description:** A thin-scenario override attribute points at the replica attribute it replaces. Consumers materialize a scenario by taking the replica and swapping in every attribute that supersedes one of its attributes
- **Scope:** Written by the platform scenario tooling together with usedInScenario; the override carries the new value while the superseded replica attribute keeps the baseline value.
- **Domain:** Attribute
- **Range:** Attribute

### targetAttribute

- **Label:** target attribute
- **Hierarchy:** assumptionObjectProperty > **targetAttribute**
- **Description:** The attribute an Assumption modifies
- **Domain:** Assumption
- **Range:** Attribute

### targetComponent

- **Label:** target component
- **Hierarchy:** assumptionObjectProperty > **targetComponent**
- **Description:** The component an Assumption applies to
- **Domain:** Assumption
- **Range:** Component

### usedInScenario

- **Label:** used in scenario
- **Hierarchy:** (root)
- **Description:** Marks a component, attribute or link as belonging to a Scenario
- **Domain:** Attribute, Component, ComponentLink
- **Range:** Scenario

### xAttribute

- **Label:** x attribute
- **Hierarchy:** (root)
- **Description:** Quantity kind of the x axis of a curve attribute
- **Domain:** CurveAttribute
- **Range:** QuantityKind

### xUnit

- **Label:** x unit
- **Hierarchy:** hasUnit > **xUnit**
- **Description:** Unit of the x axis of a curve attribute
- **Domain:** CurveAttribute
- **Range:** Unit

### yAttribute

- **Label:** y attribute
- **Hierarchy:** (root)
- **Description:** Quantity kind of the y axis of a curve attribute
- **Domain:** CurveAttribute
- **Range:** QuantityKind

### yUnit

- **Label:** y unit
- **Hierarchy:** hasUnit > **yUnit**
- **Description:** Unit of the y axis of a curve attribute
- **Domain:** CurveAttribute
- **Range:** Unit

## Data properties

### assumptionApplied

- **Label:** assumption applied
- **Hierarchy:** (root)
- **Description:** Name of an assumption applied when deriving this scenario. Scenario-provenance metadata written by the platform tooling
- **Domain:** Scenario
- **Range:** string

### assumptionDataProperty

- **Label:** assumption data property
- **Hierarchy:** (root)
- **Description:** Root data property for values carried by an Assumption

### assumptionId

- **Label:** assumption id
- **Hierarchy:** (root)
- **Description:** Identifier of an assumption applied when deriving this scenario. Scenario-provenance metadata
- **Domain:** Scenario
- **Range:** string

### assumptionTimesteps

- **Label:** assumption timesteps
- **Hierarchy:** assumptionDataProperty > **assumptionTimesteps**
- **Description:** The timesteps at which an assumption series applies
- **Domain:** AssumptionSeries

### assumptionType

- **Label:** assumption type
- **Hierarchy:** (root)
- **Description:** Kind of assumption applied when deriving this scenario (e.g. single value or series). Scenario-provenance metadata
- **Domain:** Scenario
- **Range:** string

### binFrequency

- **Label:** bin frequency
- **Hierarchy:** (root)
- **Description:** How many of the Set's values fall in this bin.
- **Range:** integer

### binLabel

- **Label:** bin label
- **Hierarchy:** (root)
- **Description:** Human-readable bin identity: a numeric range like [300, 400) or a category value.

### binLowerBound

- **Label:** bin lower bound
- **Hierarchy:** (root)
- **Description:** Inclusive lower bound of a numeric histogram bin.
- **Range:** double

### binUpperBound

- **Label:** bin upper bound
- **Hierarchy:** (root)
- **Description:** Exclusive upper bound of a numeric histogram bin (the last bin is closed).
- **Range:** double

### builtForService

- **Label:** built for service
- **Hierarchy:** (root)
- **Description:** Name of the service a scenario was assembled for. Scenario-provenance metadata
- **Domain:** Scenario
- **Range:** string

### computedAt

- **Label:** computed at
- **Hierarchy:** (root)
- **Description:** When this Collection was materialized. A Collection older than its workspace's last data load is stale.
- **Range:** dateTime

### computedBy

- **Label:** computed by
- **Hierarchy:** (root)
- **Description:** Identifier/version of the service that materialized this Collection.

### cost

- **Label:** cost
- **Hierarchy:** (root)
- **Description:** Monetary cost literal attached to an attribute node by the scenario tooling. For modelled costs prefer the cost attribute classes (SimpleCostAttribute, UnitBasedCostAttribute)
- **Domain:** Attribute

### count

- **Label:** count
- **Hierarchy:** (root)
- **Description:** How many values the Set aggregates.
- **Range:** integer

### createdInWorkspace

- **Label:** created in workspace
- **Hierarchy:** (root)
- **Description:** Identifier of the workspace a scenario was created in. Scenario-provenance metadata
- **Domain:** Scenario
- **Range:** string

### denominatorUnit

- **Label:** denominator unit
- **Hierarchy:** (root)
- **Description:** Denominator unit of a custom physical ratio attribute

### distinctCount

- **Label:** distinct count
- **Hierarchy:** (root)
- **Description:** How many distinct values occur in the Set.
- **Range:** integer

### endTime

- **Label:** end time
- **Hierarchy:** (root)
- **Description:** The ending timestamp of the time series data
- **Domain:** TimeSeries
- **Range:** dateTime

### futureTimeSeriesOf

- **Label:** future time series of
- **Hierarchy:** timeSeriesReferenceOf > **futureTimeSeriesOf**
- **Description:** Inverse-direction reference: forecast data describing an attribute

### generatedBy

- **Label:** generated by
- **Hierarchy:** (root)
- **Description:** Tool or module that generated the scenario. Scenario-provenance metadata
- **Domain:** Scenario
- **Range:** string

### groupKey

- **Label:** group key
- **Hierarchy:** (root)
- **Description:** The raw value of the grouping attribute — or the label of the grouping component instance — for this partition. Present only on Sets that are members of a GroupedSet.
- **Domain:** Set

### hasAnnotationValue

- **Label:** has annotation value
- **Hierarchy:** hasAttributeValue > **hasAnnotationValue**
- **Description:** The free-text content of an annotation attribute
- **Domain:** AnnotationAttribute
- **Range:** string

### hasAttributeValue

- **Label:** has attribute value
- **Hierarchy:** (root)
- **Description:** Root data property carrying the literal value of an attribute
- **Domain:** Attribute

### hasCategoricalValue

- **Label:** has categorical value
- **Hierarchy:** hasAttributeValue > **hasCategoricalValue**
- **Description:** The selected category value of a categorical attribute

### hasDataPath

- **Label:** has data path
- **Hierarchy:** hasAttributeValue > **hasDataPath**
- **Description:** Path to an external data file backing an attribute value (e.g. a curve or a weather file)
- **Domain:** Attribute
- **Range:** string

### hasDataPoints

- **Label:** has data points
- **Hierarchy:** hasAttributeValue > **hasDataPoints**
- **Description:** The x-y data points of a curve attribute, as JSON
- **Domain:** CurveAttribute
- **Range:** JSON

### hasFileName

- **Label:** has file name
- **Hierarchy:** (root)
- **Description:** The filename of the time series data file
- **Domain:** TimeSeries
- **Range:** string

### hasFutureTimeSeriesReference

- **Label:** has future time series reference
- **Hierarchy:** hasTimeSeriesReference > **hasFutureTimeSeriesReference**
- **Description:** Reference from an attribute to external forecast time series data

### hasHistoricTimeSeriesReference

- **Label:** has historic time series reference
- **Hierarchy:** hasTimeSeriesReference > **hasHistoricTimeSeriesReference**
- **Description:** Reference from an attribute to external historical time series data

### hasLiveTimeSeriesReference

- **Label:** has live time series reference
- **Hierarchy:** hasTimeSeriesReference > **hasLiveTimeSeriesReference**
- **Description:** Reference from an attribute to an external live time series feed

### hasTemporalValue

- **Label:** has temporal value
- **Hierarchy:** hasAttributeValue > **hasTemporalValue**
- **Description:** The temporal literal value of an attribute (e.g. a duration)

### hasTimeSeriesReference

- **Label:** has time series reference
- **Hierarchy:** (root)
- **Description:** Root property referencing external time series data from an attribute

### hasUnitLabel

- **Label:** has unit label
- **Hierarchy:** (root)
- **Description:** A human-readable string label for the unit of an attribute instance (e.g. 'KWh', 'KWh/yr', 'm2'). Used alongside qudt:unit (ObjectProperty) to provide a string representation that applications can consume directly. For CustomPhysicalRatioAttribute instances this is the primary unit expression; for Physical, UnitBasedCost, Curve, Geospatial and TimeSeries attributes it is emitted in addition to the qudt:unit IRI for backwards compatibility.
- **Domain:** Attribute
- **Range:** string

### historicTimeSeriesReferenceOf

- **Label:** historic time series reference of
- **Hierarchy:** timeSeriesReferenceOf > **historicTimeSeriesReferenceOf**
- **Description:** Inverse-direction reference: historical data describing an attribute

### identifierValue

- **Label:** identifier value
- **Hierarchy:** hasAttributeValue > **identifierValue**
- **Description:** Literal value of an identifier attribute

### linkType

- **Label:** link type
- **Hierarchy:** (root)
- **Description:** Kind of relationship a ComponentLink represents (e.g. contains, feeds)
- **Domain:** ComponentLink
- **Range:** string

### liveTimeSeriesReferenceOf

- **Label:** live time series reference of
- **Hierarchy:** timeSeriesReferenceOf > **liveTimeSeriesReferenceOf**
- **Description:** Inverse-direction reference: live data describing an attribute

### maxValue

- **Label:** maximum value
- **Hierarchy:** (root)
- **Description:** Largest value in the Set: xsd:double for numeric sets, xsd:dateTime (latest) for temporal sets — hence no fixed range.

### mean

- **Label:** mean
- **Hierarchy:** (root)
- **Description:** Arithmetic mean of a numeric Set's values.
- **Range:** double

### median

- **Label:** median
- **Hierarchy:** (root)
- **Description:** Median of a numeric Set's values.
- **Range:** double

### minValue

- **Label:** minimum value
- **Hierarchy:** (root)
- **Description:** Smallest value in the Set: xsd:double for numeric sets, xsd:dateTime (earliest) for temporal sets — hence no fixed range.

### mode

- **Label:** mode
- **Hierarchy:** (root)
- **Description:** Most frequent value in a categorical Set. Repeated when several values tie.

### modificationType

- **Label:** modification type
- **Hierarchy:** (root)
- **Description:** Kind of modification a derived scenario applies relative to its parent. Scenario-provenance metadata
- **Domain:** Scenario
- **Range:** string

### modifiedComponents

- **Label:** modified components
- **Hierarchy:** (root)
- **Description:** Number of components modified in a derived scenario. Scenario-provenance metadata
- **Domain:** Scenario
- **Range:** integer

### modifier

- **Label:** modifier
- **Hierarchy:** assumptionDataProperty > **modifier**
- **Description:** Kind of modification an assumption applies (e.g. multiply, replace)

### modifierValue

- **Label:** modifier value
- **Hierarchy:** assumptionDataProperty > **modifierValue**
- **Description:** The numeric value used by an assumption's modifier

### numeratorUnit

- **Label:** numerator unit
- **Hierarchy:** topDataProperty > **numeratorUnit**
- **Description:** Numerator unit of a custom physical ratio attribute

### populationInfluenced

- **Label:** population influenced
- **Hierarchy:** assumptionDataProperty > **populationInfluenced**
- **Description:** Share or count of the population affected by an assumption

### sourceCatalog

- **Label:** source catalog
- **Hierarchy:** (root)
- **Description:** Catalog a service definition or template was sourced from. Registry-provenance metadata
- **Range:** string

### sourceType

- **Label:** source type
- **Hierarchy:** (root)
- **Description:** Kind of source a workspace artefact came from. Registry-provenance metadata
- **Range:** string

### sourceWorkspace

- **Label:** source workspace
- **Hierarchy:** (root)
- **Description:** Workspace an artefact was copied or imported from. Registry-provenance metadata
- **Range:** string

### standardDeviation

- **Label:** standard deviation
- **Hierarchy:** (root)
- **Description:** Sample standard deviation. Absent when the Set has fewer than two members.
- **Range:** double

### startTime

- **Label:** start time
- **Hierarchy:** (root)
- **Description:** The starting timestamp of the time series data
- **Domain:** TimeSeries
- **Range:** dateTime

### statisticUsed

- **Label:** statistic used
- **Hierarchy:** (root)
- **Description:** Which statistic of the underlying Set this aggregate attribute's value is (mean, median, sum, minValue, maxValue, count, standardDeviation).
- **Domain:** AggregateAttribute

### storedAt

- **Label:** stored at
- **Hierarchy:** (root)
- **Description:** The location or path where the time series data is stored
- **Domain:** TimeSeries
- **Range:** string

### sum

- **Label:** sum
- **Hierarchy:** (root)
- **Description:** Sum of a numeric Set's values.
- **Range:** double

### temporalResolution

- **Label:** temporal resolution
- **Hierarchy:** (root)
- **Description:** The time interval between data points in the time series (e.g., PT1H for hourly, PT15M for 15-minute intervals)
- **Domain:** TimeSeries
- **Range:** duration

### timeSeriesReferenceOf

- **Label:** time series reference of
- **Hierarchy:** (root)
- **Description:** Root inverse-direction property for time series references

### timeSeriesType

- **Label:** time series type
- **Hierarchy:** (root)
- **Description:** The type of time series: 'Historic', 'Live', or 'Future'
- **Domain:** TimeSeries
- **Range:** string

### xUnitLabel

- **Label:** x unit label
- **Hierarchy:** hasUnitLabel > **xUnitLabel**
- **Description:** String label for the x-axis unit of a CurveAttribute (e.g. 'DEG_C'). Emitted alongside dici_onto:xUnit IRI for backwards compatibility.
- **Domain:** CurveAttribute
- **Range:** string

### yUnitLabel

- **Label:** y unit label
- **Hierarchy:** hasUnitLabel > **yUnitLabel**
- **Description:** String label for the y-axis unit of a CurveAttribute (e.g. 'PERCENT'). Emitted alongside dici_onto:yUnit IRI for backwards compatibility.
- **Domain:** CurveAttribute
- **Range:** string

## Annotation properties

### Author

- **Label:** author
- **Hierarchy:** (root)
- **Description:** Provenance annotation naming the author of a term or graph

### Collaborator

- **Label:** collaborator
- **Hierarchy:** (root)
- **Description:** Provenance annotation naming a collaborator on a term or graph

### Institution

- **Label:** institution
- **Hierarchy:** (root)
- **Description:** Provenance annotation naming the institution behind a term or graph

### Synonymous

- **Label:** synonymous
- **Hierarchy:** altLabel > **Synonymous**
- **Description:** Legacy synonym annotation; prefer skos:altLabel for new terms

### abbreviation

- **Label:** abbreviation
- **Hierarchy:** altLabel > **abbreviation**
- **Description:** Legacy abbreviation annotation; prefer skos:altLabel for new terms

### definition

- **Label:** definition
- **Hierarchy:** definition > **definition**
- **Description:** Legacy definition annotation; prefer skos:definition for new terms

### hasDefaultTemporalPrecision

- **Label:** has default temporal precision
- **Hierarchy:** (root)
- **Description:** Annotation on an event attribute class giving the default temporal precision (a TemporalPrecision individual) for its instances. Class-level counterpart of hasTemporalPrecision, mirroring hasDefaultUnit

### hasDefaultUnit

- **Label:** has default unit
- **Hierarchy:** (root)
- **Description:** Annotation on an attribute class giving the default QUDT unit for its instances

### hasQuantityKind

- **Label:** has quantity kind
- **Hierarchy:** (root)
- **Description:** Annotation on an attribute class giving the QUDT quantity kind its values measure


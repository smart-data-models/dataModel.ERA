# dataModel.ERA
Subject direct mapping of the ERA ontology https://data-interop.era.europa.eu/era-vocabulary/. Adaptaded to NGSI systems by adding the type to all data models and some general attributes.

### List of data models

The following entity types are available:
- [Certificate](https://github.com/smart-data-models/dataModel.ERA/blob/master/Certificate/README.md). 

- [ContactLineSystem](https://github.com/smart-data-models/dataModel.ERA/blob/master/ContactLineSystem/README.md). System that is used to transmit electrical energy to road or rail vehicles.

- [ETCSLevel](https://github.com/smart-data-models/dataModel.ERA/blob/master/ETCSLevel/README.md). ERTMS / ETCS application level related to the track side equipment.

- [Feature](https://github.com/smart-data-models/dataModel.ERA/blob/master/Feature/README.md). Class that encompasses the features that are part of the physical infrastructure (class InfrastructureObject) and the topological objects (class TopologicalObject). It is a subclass of the geographical Feature class that has a spatial representation.

- [FrenchTrainDetectionSystemLimitation](https://github.com/smart-data-models/dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/README.md). Specific for route compatibility check on French network. Sections with: 
-1 Tonnage circulated per track is inferior to 15000 tons/day/track 
-2 Directional Interlocking 
-3 45-second delay for directional interlocking 
-4 Installation with track circuit announcement 
-5 Absence of a shunting assistance pedal in the normal direction of circulation for non-reversible double track lines 
-6 Absence of a shunting assistance pedal regardless of the direction of traffic for single track lines and tracks for two way working 
-7 Absence of a pedal announcement mechanism 
-8 45-second delay for specific announcement reset devices

- [InfrastructureManager](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureManager/README.md). The infrastructure manager owns and operates the railway network and related infrastructure.

- [InfrastructureObject](https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/README.md). This class encompasses all those classes that represent features that are  implemented in the European railway infrastructure. It is a subclass of the ERA Feature that has a spatial representation. It covers tracks, platforms, signals, tunnels, operational points, and sections of line.
A feature that belongs to the infrastructure can be abstracted (hasAbstraction) as a topological object. It also is related to the infrastructure manager through the property infrastructureMgr.

- [LineReference](https://github.com/smart-data-models/dataModel.ERA/blob/master/LineReference/README.md). Railway location

- [LoadCapability](https://github.com/smart-data-models/dataModel.ERA/blob/master/LoadCapability/README.md). This class together with properties loadCapabilityLineCategory and loadCapabilitySpeed replaces the previous loadCapability SKOS property.

- [Manufacturer](https://github.com/smart-data-models/dataModel.ERA/blob/master/Manufacturer/README.md). A company or organization that manufactures vehicles.

- [MaximumMagneticField](https://github.com/smart-data-models/dataModel.ERA/blob/master/MaximumMagneticField/README.md). The maximum magnetic field limits allowed for axle counters (in dBµA/m) for a defined frequency band.
It should be provided in 3 directions.

- [MaximumSpeedAndCantDeficiency](https://github.com/smart-data-models/dataModel.ERA/blob/master/MaximumSpeedAndCantDeficiency/README.md). Combination of maximum speed and maximum cant deficiency for which the vehicle was assessed.

- [MinAxleLoadVehicleCategory](https://github.com/smart-data-models/dataModel.ERA/blob/master/MinAxleLoadVehicleCategory/README.md). Deprecated according to the ammendment to the Regulation (EU) 2019/777. Represents information that indicates the load given in tons depending of the category of vehicle. Its properties are minAxleLoadVehicleCategory and minAxleLoad.

- [NationalRailwayLine](https://github.com/smart-data-models/dataModel.ERA/blob/master/NationalRailwayLine/README.md). Railway line within a member state.

- [NetElement](https://github.com/smart-data-models/dataModel.ERA/blob/master/NetElement/README.md). Base class for defining nodes in the connectivity graph representing the topological network.

- [NetRelation](https://github.com/smart-data-models/dataModel.ERA/blob/master/NetRelation/README.md). Base class for defining edges in the connectivity graph representing the topological network.

- [OperationalPoint](https://github.com/smart-data-models/dataModel.ERA/blob/master/OperationalPoint/README.md). An operational point (OP) means any location for train service operations, where train services may begin and end or change route, and where passenger or freight services may be provided; operational point also means any location at boundaries between Member States or infrastructure managers.
In https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.2 Principal locations (stations, yards, junctions, freight terminals).

- [PhaseInfo](https://github.com/smart-data-models/dataModel.ERA/blob/master/PhaseInfo/README.md). Indication of required several information on phase separation.

- [Platform](https://github.com/smart-data-models/dataModel.ERA/blob/master/Platform/README.md). Platform for the purpose of RINF is understood as a platform edge. A platform concerns only the part of the structure neighbouring to the track (interfaced with trains).

- [RaisedPantographsDistanceAndSpeed](https://github.com/smart-data-models/dataModel.ERA/blob/master/RaisedPantographsDistanceAndSpeed/README.md). Indication of maximum number of raised pantographs per train allowed and minimum spacing centre line to centre line of adjacent pantograph heads, expressed in metres, at the given speed.
Each track can have several raised pantographs per train allowed (structured) values, and each one has values for number of pantographs, minimum distance between pantographs, in metres, and speed considered in km/h.

- [SectionOfLine](https://github.com/smart-data-models/dataModel.ERA/blob/master/SectionOfLine/README.md). A section of line means the part of line between adjacent operational points and may consist of several tracks.
In https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.1 Line sections.

- [Siding](https://github.com/smart-data-models/dataModel.ERA/blob/master/Siding/README.md). Sidings are all those tracks where running trains in service movements ends and which are not used for operational routing of a train.

- [Signal](https://github.com/smart-data-models/dataModel.ERA/blob/master/Signal/README.md). A railway signal is an installation next to the railway track for signalling the maximum allowed speed in the next block section to the train driver.
Definition RSM: Apparatus by means of which a conventional visual or acoustic indication is given, generally concerning the movements of railway vehicles.

- [SpecialArea](https://github.com/smart-data-models/dataModel.ERA/blob/master/SpecialArea/README.md). Encompasses all those areas or sections such as safe areas, restricted areas (non-stopping areas or industrial risk locations).

- [SpecialTunnelArea](https://github.com/smart-data-models/dataModel.ERA/blob/master/SpecialTunnelArea/README.md). Area or location within a tunnel where  there is a walkway, evacuation and rescue points.

- [SubsetWithCommonCharacteristics](https://github.com/smart-data-models/dataModel.ERA/blob/master/SubsetWithCommonCharacteristics/README.md). Subset of items shared by sections of lines and/or operational points of a member state. For the purposes of the register of infrastructure, each infrastructure manager shall describe its railway network at least by sections of line and operational points and optionally via common characteristic subsets.

- [SystemSeparationInfo](https://github.com/smart-data-models/dataModel.ERA/blob/master/SystemSeparationInfo/README.md). Indication of required several information on system separation.

- [TopologicalObject](https://github.com/smart-data-models/dataModel.ERA/blob/master/TopologicalObject/README.md). Top level class for the the track network described as a topological node edge model

- [Track](https://github.com/smart-data-models/dataModel.ERA/blob/master/Track/README.md). A running track that is used for train service movements.

- [TrainDetectionSystem](https://github.com/smart-data-models/dataModel.ERA/blob/master/TrainDetectionSystem/README.md). System used to detect the position of vehicles in the railway track.

- [Tunnel](https://github.com/smart-data-models/dataModel.ERA/blob/master/Tunnel/README.md). A railway tunnel is an excavation or a construction around the track provided to allow the railway to pass for example higher land, buildings or water.

- [Vehicle](https://github.com/smart-data-models/dataModel.ERA/blob/master/Vehicle/README.md). A specific vehicle or wagon able to operate over railway lines.

- [VehicleKeeper](https://github.com/smart-data-models/dataModel.ERA/blob/master/VehicleKeeper/README.md). A company or organization that owns or operates a certain vehicle.

- [VehicleType](https://github.com/smart-data-models/dataModel.ERA/blob/master/VehicleType/README.md). A vehicle type that has been authorized to operate on the EU railway infrastructure.



### Contributors
[Link](https://github.com/smart-data-models/dataModel.ERA/blob/master/CONTRIBUTORS.yaml) to the 9 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.ERA/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.ERA/pulls) on existing data models

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    Track = 'Track'


class Track(BaseModel):
    IdPhoneErtmsRadioBlockCenter: Optional[str] = Field(
        None, description='ID and phone number of ERTMS/ETCS Radio Block Center'
    )
    TSIMagneticFields: Optional[AnyUrl] = Field(
        None,
        description='Existence and TSI compliance of rules for magnetic fields emitted by a vehicle',
    )
    TSITractionHarmonics: Optional[AnyUrl] = Field(
        None,
        description='Existence and TSI compliance of limits in harmonics in the traction current of vehicles',
    )
    accelerationLevelCrossing: Optional[str] = Field(
        None, description='Acceleration allowed at level crossing'
    )
    additionalBrakingInformationDocument: Optional[str] = Field(
        None,
        description='Documents available by the IM relating to braking performance',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    atoCommunicationSystem: Optional[AnyUrl] = Field(
        None, description='ATO communication system'
    )
    atoErrorCorrectionsOnboard: Optional[str] = Field(
        None, description='ATO error corrections required for the on-board'
    )
    atoGradeAutomation: Optional[AnyUrl] = Field(
        None, description='ATO Grade of Automation'
    )
    atoSystemVersion: Optional[AnyUrl] = Field(None, description='ATO System version')
    automaticDroppingDeviceRequired: Optional[bool] = Field(
        None, description='Automatic dropping device required'
    )
    bigMetalMass: Optional[bool] = Field(None, description='Big metal mass')
    bridge: Optional[bool] = Field(None, description='Is bridge')
    cantDeficiency: Optional[float] = Field(None, description='Cant deficiency')
    cantDeficiencyBasicSSP: Optional[AnyUrl] = Field(
        None, description='Cant Deficiency used for the basic SSP'
    )
    compatibilityProcedureDocument: Optional[str] = Field(
        None,
        description='Document with the procedure(s) for static and dynamic route compatibility checks',
    )
    conditionsSwitchClassBSystems: Optional[str] = Field(
        None,
        description='Special technical conditions required to switch over between ERTMS/ETCS and Class B systems',
    )
    conditionsSwitchTrainProtectionSystems: Optional[str] = Field(
        None,
        description='Special conditions to switch over between different class B train protection, control and warning systems',
    )
    conditionsUseReflectivePlates: Optional[AnyUrl] = Field(
        None, description='Conditions for use of reflective plates'
    )
    contactLineSystem: Optional[AnyUrl] = Field(None, description='Contact line system')
    contactStripMaterial: Optional[AnyUrl] = Field(
        None, description='Permitted contact strip material'
    )
    contactStripMaterialMetallicContent: Optional[float] = Field(
        None, description='Contact strip material metallic content'
    )
    dNvovtrp: Optional[float] = Field(None, description='D_NVOVTRP')
    dNvpotrp: Optional[float] = Field(None, description='D_NVPOTRP')
    dNvroll: Optional[float] = Field(None, description='D_NVROLL')
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dataRadioCompatible: Optional[AnyUrl] = Field(
        None, description='Radio system compatibility data'
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    demonstrationENE: Optional[str] = Field(
        None, description='EI declaration of demonstration for track (ENE)'
    )
    demonstrationINF: Optional[str] = Field(
        None, description='EI declaration of demonstration for track/siding [INF]'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    distSignToPhaseEnd: Optional[float] = Field(
        None, description='Distance between signboard and phase separation ending'
    )
    documentRestrictionPositionContactLineSeparation: Optional[str] = Field(
        None,
        description='Document with restriction related to the position of Multiple Traction unit(s) to comply with contact line separation',
    )
    documentRestrictionPowerConsumption: Optional[str] = Field(
        None,
        description='Document with restriction related to power consumption of specific electric traction unit(s)',
    )
    eddyCurrentBraking: Optional[AnyUrl] = Field(
        None, description='Use of eddy current brakes'
    )
    eddyCurrentBrakingConditionsDocument: Optional[str] = Field(
        None,
        description='Document with the conditions for the use of eddy current brakes',
    )
    etcsDegradedSituation: Optional[AnyUrl] = Field(
        None, description='ETCS level for degraded situation'
    )
    etcsErrorCorrectionsOnboard: Optional[str] = Field(
        None, description='ETCS error corrections required for the on-board'
    )
    etcsImplementsLevelCrossingProcedure: Optional[bool] = Field(
        None,
        description='ETCS trackside implements level crossing procedure or an equivalent solution',
    )
    etcsInfill: Optional[AnyUrl] = Field(
        None, description='ETCS infill installed lineside'
    )
    etcsInfillLineAccess: Optional[bool] = Field(
        None, description='ETCS infill necessary for line access'
    )
    etcsLevel: Optional[AnyUrl] = Field(None, description='Etcs level')
    etcsMVersion: Optional[AnyUrl] = Field(None, description='ETCS M_version')
    etcsNationalPacket44: Optional[bool] = Field(
        None, description='ETCS national packet 44 application implemented'
    )
    etcsOptionalFunctions: Optional[str] = Field(
        None, description='ETCS optional functions'
    )
    etcsSystemCompatibility: Optional[AnyUrl] = Field(
        None, description='ETCS system compatibility'
    )
    etcsSystemFunctionalitiesNextFiveYears: Optional[str] = Field(
        None,
        description='ETCS system version 2.2 or 3.0 functionalities to be required in the next 5 years',
    )
    etcsTransmitsTrackConditions: Optional[bool] = Field(
        None,
        description='Is the ETCS trackside engineered to transmit Track Conditions',
    )
    etcsTransmittedTrackConditions: Optional[AnyUrl] = Field(
        None, description='Track conditions which can be transmitted'
    )
    flangeLubeForbidden: Optional[bool] = Field(
        None, description='Use of flange lubrication forbidden'
    )
    freightCorridor: Optional[AnyUrl] = Field(
        None, description='Part of a Railway freight corridor'
    )
    gaugingCheckLocation: Optional[str] = Field(
        None,
        description='Railway location of particular points requiring specific checks',
    )
    gaugingProfile: Optional[AnyUrl] = Field(None, description='Gauging')
    gaugingTransversalDocument: Optional[str] = Field(
        None,
        description='Document with the transversal section of the particular points requiring specific checks',
    )
    gprsForETCS: Optional[bool] = Field(None, description='GPRS for ETCS')
    gprsImplementationArea: Optional[str] = Field(
        None, description='Area of implementation of GPRS'
    )
    gradientProfile: Optional[str] = Field(None, description='Gradient profile')
    gsmRActiveMobiles: Optional[AnyUrl] = Field(
        None,
        description='Number of active GSM-R mobiles (EDOR) or simultaneous communication session on-board for ETCS Level 2 (or level 3) needed to perform radio block centre handovers without having an operational disruption',
    )
    gsmRAdditionalInfo: Optional[str] = Field(
        None, description='Additional information on network characteristics'
    )
    gsmRNoCoverage: Optional[bool] = Field(None, description='No GSM-R coverage')
    gsmROptionalFunctions: Optional[AnyUrl] = Field(
        None, description='Optional GSM-R functions'
    )
    gsmRVersion: Optional[AnyUrl] = Field(None, description='GSM-R version')
    gsmrConstraintsOperateOnlyInCircuitSwitch: Optional[AnyUrl] = Field(
        None,
        description='Specific constraints imposed by the GSM-R network operator on ETCS on-board units only able to operate in circuit-switch',
    )
    gsmrErrorCorrectionsOnboard: Optional[str] = Field(
        None, description='GSM-R error corrections required for the on-board'
    )
    gsmrForcedDeregistrationFunctionalNumber: Optional[bool] = Field(
        None,
        description='GSM-R network is configured to allow forced de-registration of a functional number by another driver',
    )
    gsmrNetworkCoverage: Optional[AnyUrl] = Field(
        None, description='GSM-R networks covered by a roaming agreement'
    )
    hasAdditionalBrakingInformation: Optional[bool] = Field(
        None, description='Availability by the IM of additional information'
    )
    hasBallast: Optional[bool] = Field(None, description='Existence of ballast')
    hasETCSRestrictionsConditions: Optional[bool] = Field(
        None, description='Existence of operating restrictions or conditions'
    )
    hasHotAxleBoxDetector: Optional[bool] = Field(
        None, description='Existence of trackside hot axle box detector (HABD)'
    )
    hasLevelCrossings: Optional[bool] = Field(
        None, description='Existence of level crossings'
    )
    hasOtherTrainProtection: Optional[bool] = Field(
        None,
        description='Existence of other train protection, control and warning systems installed',
    )
    hasSevereWeatherConditions: Optional[bool] = Field(
        None, description='Existence of severe climatic conditions'
    )
    hasSystemSeparation: Optional[bool] = Field(None, description='System separation')
    hasTSITrainDetection: Optional[bool] = Field(
        None,
        description='Existence of train detection system fully compliant with the TSI',
    )
    highSpeedLoadModelCompliance: Optional[bool] = Field(
        None,
        description='Compliance of structures with the High Speed Load Model (HSLM) dynamic load model',
    )
    hotAxleBoxDetectorDirection: Optional[AnyUrl] = Field(
        None, description='Hot axle box detector direction'
    )
    hotAxleBoxDetectorGeneration: Optional[str] = Field(
        None, description='Generation of trackside HABD'
    )
    hotAxleBoxDetectorIdentification: Optional[str] = Field(
        None, description='Identification of trackside HABD'
    )
    hotAxleBoxDetectorLocation: Optional[float] = Field(
        None, description='Railway location of trackside HABD'
    )
    hotAxleBoxDetectorTSICompliant: Optional[bool] = Field(
        None, description='Trackside HABD TSI compliant'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    instructionsSwitchRadioSystems: Optional[str] = Field(
        None,
        description='Special instructions to switch over between different radio systems',
    )
    isQuietRoute: Optional[bool] = Field(
        None, description='Belonging to a quieter route'
    )
    legacyRadioSystem: Optional[AnyUrl] = Field(
        None, description='Other radio systems installed (Radio Legacy Systems)'
    )
    lineCategory: Optional[AnyUrl] = Field(None, description='Category of line')
    linesideDistanceIndicationAppearance: Optional[AnyUrl] = Field(
        None, description='Lineside distance indication appearance'
    )
    linesideDistanceIndicationFrequency: Optional[float] = Field(
        None, description='Lineside distance indication frequency'
    )
    linesideDistanceIndicationPositioning: Optional[AnyUrl] = Field(
        None, description='Lineside distance indication positioning'
    )
    loadCapability: Optional[AnyUrl] = Field(None, description='Load Capability')
    localRulesOrRestrictions: Optional[bool] = Field(
        None,
        description='Existence of rules and restrictions of a strictly local nature.',
    )
    localRulesOrRestrictionsDoc: Optional[str] = Field(
        None,
        description='Documents regarding the rules or restrictions of a strictly local nature available by the IM',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mNvcontact: Optional[AnyUrl] = Field(None, description='M_NVCONTACT')
    mNvderun: Optional[bool] = Field(None, description='M_NVDERUN')
    magneticBraking: Optional[AnyUrl] = Field(
        None, description='Use of magnetic brakes'
    )
    magneticBrakingConditionsDocument: Optional[str] = Field(
        None, description='Document with the conditions for the use of magnetic brakes'
    )
    maximumAltitude: Optional[float] = Field(None, description='Maximum altitude')
    maximumBrakingDistance: Optional[float] = Field(
        None, description='Maximum braking distance requested'
    )
    maximumContactWireHeight: Optional[float] = Field(
        None, description='Maximum contact wire height'
    )
    maximumPermittedSpeed: Optional[float] = Field(
        None, description='Maximum permitted speed'
    )
    maximumTemperature: Optional[float] = Field(
        None, description='Temperature range (maximum)'
    )
    maximumTrainDeceleration: Optional[float] = Field(
        None, description='Maximum train deceleration'
    )
    minDistConsecutiveAxles: Optional[float] = Field(
        None, description='Minimum permitted distance between two consecutive axles'
    )
    minDistFirstLastAxle: Optional[float] = Field(
        None, description='Minimum permitted distance between first and last axle'
    )
    minFlangeHeight: Optional[float] = Field(
        None, description='Minimum permitted height of the flange'
    )
    minFlangeThickness: Optional[float] = Field(
        None, description='Minimum permitted thickness of the flange'
    )
    minRimWidth: Optional[float] = Field(
        None, description='Minimum permitted width of the rim'
    )
    minWheelDiameter: Optional[float] = Field(
        None, description='Minimum permitted wheel diameter'
    )
    minimumContactWireHeight: Optional[float] = Field(
        None, description='Minimum contact wire height'
    )
    minimumHorizontalRadius: Optional[float] = Field(
        None, description='Minimum radius of horizontal curve'
    )
    minimumTemperature: Optional[float] = Field(
        None, description='Temperature range (minimum)'
    )
    minimumWheelDiameter: Optional[float] = Field(
        None, description='Minimum wheel diameter for fixed obtuse crossings'
    )
    multipleTrainProtectionRequired: Optional[bool] = Field(
        None,
        description='Need for more than one train protection, control and warning system required on board',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nationalLoadCapability: Optional[str] = Field(
        None, description='National classification for load capability'
    )
    nationalValuesBrakeModel: Optional[str] = Field(
        None, description='National Values used for the brake model'
    )
    osmClass: Optional[AnyUrl] = Field(None, description='Open street map class')
    otherCantDeficiencyBasicSSP: Optional[AnyUrl] = Field(
        None,
        description='Other Cant Deficiency train categories for which the ETCS trackside is configured to provide SSP',
    )
    otherPantographHead: Optional[AnyUrl] = Field(
        None, description='Accepted other pantograph heads'
    )
    otherTrainProtection: Optional[AnyUrl] = Field(
        None,
        description='Other train protection, control and warning systems for degraded situation',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    passesThroughTunnel: Optional[AnyUrl] = Field(
        None, description='Passes through tunnel'
    )
    permitUseReflectivePlates: Optional[bool] = Field(
        None, description='Permit of use of reflective plates'
    )
    permittedContactForce: Optional[str] = Field(
        None, description='Contact force permitted'
    )
    phaseInfo: Optional[str] = Field(
        None, description='Information on phase separation'
    )
    phaseSeparation: Optional[bool] = Field(None, description='Phase separation')
    platform: Optional[AnyUrl] = Field(None, description='Platform')
    profileNumberSemiTrailers: Optional[AnyUrl] = Field(
        None, description='Standard combined transport profile number for semi-trailers'
    )
    profileNumberSwapBodies: Optional[AnyUrl] = Field(
        None, description='Standard combined transport profile number for swap bodies'
    )
    protectionLegacySystem: Optional[AnyUrl] = Field(
        None, description='Train protection legacy system'
    )
    publicNetworkRoaming: Optional[bool] = Field(
        None, description='GSM-R existence of roaming to public networks'
    )
    publicNetworkRoamingDetails: Optional[str] = Field(
        None, description='GSM-R details on roaming to public networks'
    )
    qNvdriverAdhes: Optional[AnyUrl] = Field(None, description='Q_NVDRIVER_ADHES')
    qNvemrrls: Optional[AnyUrl] = Field(None, description='Q_NVEMRRLS')
    qNvsbtsmperm: Optional[bool] = Field(None, description='Q_NVSBTSMPERM')
    radioNetworkId: Optional[float] = Field(None, description='Radio Network ID')
    railInclination: Optional[AnyUrl] = Field(None, description='Rail inclination')
    raisedPantographsDistanceAndSpeed: Optional[str] = Field(
        None,
        description='Requirements for number of raised pantographs and spacing between them, at the given speed',
    )
    reasonsEtcsRadioBlockCenterReject: Optional[AnyUrl] = Field(
        None,
        description='Reasons for which an ETCS Radio Block Center can reject a train',
    )
    redLightsRequired: Optional[bool] = Field(
        None, description='Steady red lights required'
    )
    safeConsistLengthInformationNecessary: Optional[AnyUrl] = Field(
        None,
        description='Safe consist length information from on-board necessary for access the line and SIL',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    specificInformation: Optional[str] = Field(None, description='Specific information')
    standardCombinedTransporRollerUnits: Optional[AnyUrl] = Field(
        None, description='Standard combined transport profile number for roller units'
    )
    standardCombinedTransportContainers: Optional[AnyUrl] = Field(
        None, description='Standard combined transport profile number for containers'
    )
    structureCheckLocation: Optional[float] = Field(
        None, description='Railway location of structures requiring specific checks'
    )
    switchProtectControlWarning: Optional[bool] = Field(
        None,
        description='Existence of switch over between different protection, control and warning systems while running',
    )
    switchRadioSystem: Optional[bool] = Field(
        None, description='Existence of switch over between different radio systems'
    )
    systemSeparationInfo: Optional[str] = Field(
        None, description='Information on system separation'
    )
    tNvcontact: Optional[float] = Field(None, description='T_NVCONTACT')
    tNvovtrp: Optional[float] = Field(None, description='T_NVOVTRP')
    temperatureRange: Optional[AnyUrl] = Field(None, description='Temperature range')
    tenClassification: Optional[AnyUrl] = Field(
        None, description='TEN classification (of track, of platform, of siding)'
    )
    tenGISId: Optional[str] = Field(None, description='TEN GIS identity')
    tiltingSupported: Optional[bool] = Field(
        None, description='Indication whether tilting functions are supported by ETCS'
    )
    trackDirection: Optional[AnyUrl] = Field(
        None, description='Normal running direction'
    )
    trackId: Optional[str] = Field(None, description='Identification of track')
    trackLoadCapability: Optional[AnyUrl] = Field(
        None, description='Track load capability'
    )
    trackPhaseInfo: Optional[AnyUrl] = Field(None, description='Track phase info')
    trackRaisedPantographsDistanceAndSpeed: Optional[AnyUrl] = Field(
        None, description='Track raised pantograph distance and speed'
    )
    trackSystemSeparationInfo: Optional[AnyUrl] = Field(
        None, description='Track system separation info'
    )
    trainDetectionSystem: Optional[AnyUrl] = Field(
        None, description='Train detection system'
    )
    trainIntegrityOnBoardRequired: Optional[bool] = Field(
        None,
        description='Train integrity confirmation from on-board (not from driver) necessary for line access',
    )
    tsiPantographHead: Optional[AnyUrl] = Field(
        None, description='Accepted TSI compliant pantograph heads'
    )
    tsiSwitchCrossing: Optional[bool] = Field(
        None,
        description='TSI compliance of in service values for switches and crossings',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI data type. It has to be Track'
    )
    usesGroup555: Optional[bool] = Field(None, description='GSM-R use of group 555')
    vNvallowovtrp: Optional[float] = Field(None, description='V_NVALLOWOVTRP')
    vNvsupovtrp: Optional[float] = Field(None, description='V_NVSUPOVTRP')
    vehicleTypesCompatibleTrafficLoad: Optional[str] = Field(
        None,
        description='List of vehicle types already identified as compatible with Traffic load and load carrying capacity of infrastructure and train detection systems',
    )
    vehiclesCompatibleTrafficLoad: Optional[str] = Field(
        None,
        description='List of vehicles already identified as compatible with Traffic load and load carrying capacity of infrastructure and train detection systems',
    )
    verificationCCS: Optional[str] = Field(
        None, description='EC declaration of verification for track (CCS)'
    )
    verificationENE: Optional[str] = Field(
        None, description='EC declaration of verification for track (ENE)'
    )
    verificationINF: Optional[str] = Field(
        None, description='EC declaration of verification for track/siding [INF]'
    )
    voiceRadioCompatible: Optional[AnyUrl] = Field(
        None, description='Radio system compatibility voice'
    )
    wheelSetGauge: Optional[AnyUrl] = Field(None, description='Nominal track gauge')

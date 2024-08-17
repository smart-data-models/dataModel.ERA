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
    VehicleType = 'VehicleType'


class VehicleType(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    alternativeName: Optional[str] = Field(None, description='Alternative name')
    altitudeRange: Optional[str] = Field(None, description='Altitude range')
    altitudeRangeDetail: Optional[float] = Field(
        None, description='Altitude range detail'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    authorizedCountry: Optional[AnyUrl] = Field(None, description='Authorized country')
    axleBearingConditionMonitoring: Optional[AnyUrl] = Field(
        None, description='Axle bearing condition monitoring'
    )
    axleSpacing: Optional[str] = Field(None, description='Axle spacing')
    boardingAids: Optional[str] = Field(None, description='Boarding aids')
    brakeWeightPercentage: Optional[str] = Field(
        None, description='Brake weight percentage'
    )
    cantDefficiency: Optional[float] = Field(None, description='Cant defficiency')
    category: Optional[AnyUrl] = Field(None, description='Vehicle category')
    catenaryMaxRatedCurrent: Optional[float] = Field(
        None, description='Catenary max rated current'
    )
    certificate: Optional[AnyUrl] = Field(None, description='Certificate')
    conditionsTrainFormation: Optional[str] = Field(
        None, description='Conditions train formation'
    )
    contactStripMaterial: Optional[AnyUrl] = Field(
        None, description='Permitted contact strip material'
    )
    dangerousGoodsTankCode: Optional[str] = Field(
        None, description='Dangerous goods tank code'
    )
    dataGSMRNetwork: Optional[AnyUrl] = Field(None, description='Data GSM-R network')
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
    description: Optional[str] = Field(None, description='A description of this item')
    designMassExceptionalPayload: Optional[float] = Field(
        None, description='Design mass under exceptional payload'
    )
    designMassNormalPayload: Optional[float] = Field(
        None, description='Design mass under normal payload'
    )
    designMassWorkingOrder: Optional[float] = Field(
        None, description='Design mass in working order'
    )
    drivingCabs: Optional[float] = Field(None, description='Driving cabs')
    eddyCurrentBrakePrevention: Optional[bool] = Field(
        None, description='Eddy current brake prevention'
    )
    eddyCurrentBrakingFitted: Optional[bool] = Field(
        None, description='Eddy current braking fitted'
    )
    emergencyBrake: Optional[str] = Field(None, description='Emergency braking')
    endCouplingType: Optional[AnyUrl] = Field(None, description='End coupling type')
    energyMeterInstalled: Optional[bool] = Field(
        None, description='Energy meter installed'
    )
    energySupplyMaxPower: Optional[float] = Field(
        None, description='Energy supply max power'
    )
    energySupplySystem: Optional[AnyUrl] = Field(
        None, description='Energy supply system'
    )
    etcsBaseline: Optional[AnyUrl] = Field(None, description='ETCS baseline')
    etcsDataCommApp: Optional[str] = Field(
        None, description='ETCS data communication application'
    )
    etcsEquipmentOnBoardLevel: Optional[AnyUrl] = Field(
        None, description='ETCS equipment level'
    )
    etcsInfill: Optional[AnyUrl] = Field(
        None, description='ETCS infill installed lineside'
    )
    etcsNationalApplications: Optional[str] = Field(
        None, description='ETCS national applications'
    )
    etcsOnBoardImplementation: Optional[str] = Field(
        None, description='ETCS on-board implementation'
    )
    etcsSystemCompatibility: Optional[AnyUrl] = Field(
        None, description='ETCS system compatibility'
    )
    ferromagneticWheelMaterial: Optional[bool] = Field(
        None, description='Ferromagnetic wheel material'
    )
    fireSafetyCategory: Optional[AnyUrl] = Field(
        None, description='Fire safety category'
    )
    fixedSeats: Optional[str] = Field(None, description='Fixed seats')
    flangeLubricationFitted: Optional[bool] = Field(
        None, description='Flange lubrication fitted'
    )
    gaugingProfile: Optional[AnyUrl] = Field(None, description='Gauging')
    gsmRRadioDataCommunication: Optional[AnyUrl] = Field(
        None, description='GSM-R radio data communication'
    )
    gsmRSetsInDrivingCab: Optional[float] = Field(
        None, description='GSM-R sets in driving cab'
    )
    gsmRVersion: Optional[AnyUrl] = Field(None, description='GSM-R version')
    hasAutomaticDroppingDevice: Optional[bool] = Field(
        None, description='Has automatic dropping device'
    )
    hasCantDefficiencyCompensation: Optional[bool] = Field(
        None, description='Has cant defficiency compensation'
    )
    hasCurrentLimitation: Optional[bool] = Field(
        None, description='Has current limitation'
    )
    hasLubricationDevicePrevention: Optional[bool] = Field(
        None, description='Has lubrication device prevention'
    )
    hasParkingBrake: Optional[bool] = Field(None, description='Has parking brake')
    hasRegenerativeBrake: Optional[bool] = Field(
        None, description='Permission for regenerative braking'
    )
    hasSandingPrevention: Optional[bool] = Field(
        None, description='Has sanding prevention'
    )
    hasShuntingRestrictions: Optional[bool] = Field(
        None, description='Has shunting restrictions'
    )
    hasTrainIntegrityConfirmation: Optional[bool] = Field(
        None, description='Has train integrity confirmation'
    )
    hasWheelSlideProtectionSystem: Optional[bool] = Field(
        None, description='Has wheel slide protection system'
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
    legacyRadioSystem: Optional[AnyUrl] = Field(
        None, description='Other radio systems installed (Radio Legacy Systems)'
    )
    letterMarking: Optional[str] = Field(None, description='Letter marking')
    loadingPlatformHeight: Optional[float] = Field(
        None, description='Loading platform height'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    magneticBrakePrevention: Optional[bool] = Field(
        None, description='Magnetic brake prevention'
    )
    magneticBrakingFitted: Optional[bool] = Field(
        None, description='Magnetic braking fitted'
    )
    manufacturer: Optional[AnyUrl] = Field(None, description='Manufacturer')
    manufacturingCountry: Optional[AnyUrl] = Field(
        None, description='Manufacturing country'
    )
    massPerWheel: Optional[float] = Field(None, description='Mass per wheel')
    maxCurrentStandstillPantograph: Optional[float] = Field(
        None, description='Maximum current at standstill per pantograph'
    )
    maxDistConsecutiveAxles: Optional[float] = Field(
        None,
        description='Maximum permitted distance between two consecutive axles in case of TSI non-compliance',
    )
    maxFlangeHeight: Optional[float] = Field(
        None, description='Maximum permitted height of the flange'
    )
    maxImpedanceWheelset: Optional[float] = Field(
        None,
        description='Maximum permitted impedance between opposite wheels of a wheelset when not TSI compliant',
    )
    maxLengthVehicleNose: Optional[float] = Field(
        None, description='Maximum length vehicle nose'
    )
    maximumAverageDeceleration: Optional[float] = Field(
        None, description='Maximum average deceleration'
    )
    maximumBrakeThermalEnergyCapacity: Optional[float] = Field(
        None, description='Maximum brake thermal energy capacity'
    )
    maximumContactWireHeight: Optional[float] = Field(
        None, description='Maximum contact wire height'
    )
    maximumDesignSpeed: Optional[float] = Field(
        None, description='Maximum design speed'
    )
    maximumLocomotivesCoupled: Optional[float] = Field(
        None, description='Maximum locomotives coupled'
    )
    maximumServiceBrake: Optional[str] = Field(
        None, description='Maximum service break'
    )
    maximumSpeedAndCantDeficiency: Optional[str] = Field(
        None, description='Maximum speed and cant deficiency'
    )
    maximumSpeedEmpty: Optional[float] = Field(None, description='Maximum speed empty')
    maximumTemperature: Optional[float] = Field(
        None, description='Temperature range (maximum)'
    )
    meetsRequirementVehicleAuthorisation: Optional[str] = Field(
        None, description='Meets requirement vehicle authorization'
    )
    minAxleLoad: Optional[float] = Field(
        None, description='Minimum permitted axle load'
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
    minVehicleImpedance: Optional[str] = Field(None, description='Vehicle impedance')
    minWheelDiameter: Optional[float] = Field(
        None, description='Minimum permitted wheel diameter'
    )
    minimumConcaveVerticalRadius: Optional[float] = Field(
        None, description='Minimum concave vertical radius'
    )
    minimumContactWireHeight: Optional[float] = Field(
        None, description='Minimum contact wire height'
    )
    minimumConvexVerticalRadius: Optional[float] = Field(
        None, description='Minimum convex vertical radius'
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
    name: Optional[str] = Field(None, description='The name of this item')
    nonCodedRestrictions: Optional[str] = Field(
        None, description='Non coded restrictions'
    )
    numberElementsRakeFreightWagons: Optional[float] = Field(
        None, description='Number elements rake freight wagons'
    )
    numberOfPantographsInContactWithOCL: Optional[float] = Field(
        None, description='Number of pantographs in contact with OCL'
    )
    numberOfToilets: Optional[float] = Field(None, description='Number of toilets')
    oclType: Optional[str] = Field(None, description='Ocl type')
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
    parkingBrake: Optional[bool] = Field(None, description='Parking brake')
    parkingBrakeMandatory: Optional[bool] = Field(
        None, description='Parking brake mandatory'
    )
    parkingBrakeMaximumGradient: Optional[float] = Field(
        None, description='Parking brake maximum gradient'
    )
    parkingBrakeType: Optional[AnyUrl] = Field(None, description='Parking brake type')
    passByNoiseLevel: Optional[float] = Field(None, description='Pass-by noise level')
    permissiblePayload: Optional[str] = Field(None, description='Permissible payload')
    portableBoardingAids: Optional[str] = Field(
        None, description='Portable boarding aids'
    )
    preventRegenerativeBrakeUse: Optional[bool] = Field(
        None, description='Prevent regenerative brake use'
    )
    previousVehicleType: Optional[AnyUrl] = Field(
        None, description='Previous vehicle type'
    )
    prioritySeats: Optional[str] = Field(None, description='Priority seats')
    prmAccessibleToilets: Optional[float] = Field(
        None, description='Prm accessible toilets'
    )
    protectionLegacySystem: Optional[AnyUrl] = Field(
        None, description='Train protection legacy system'
    )
    quasiStaticGuidingForce: Optional[float] = Field(
        None, description='Quasi static guiding force'
    )
    radioSwitchOverSpecialConditions: Optional[str] = Field(
        None, description='Radio switch over special conditions'
    )
    railInclination: Optional[AnyUrl] = Field(None, description='Rail inclination')
    referencePassByNoiseLevel: Optional[bool] = Field(
        None, description='Reference pass-by noise level'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shortestDistanceBetweenPantographsInContactWithOCL: Optional[str] = Field(
        None, description='Shortest distance between pantographs in contact with OCL'
    )
    sleepingPlaces: Optional[str] = Field(None, description='Sleeping places')
    snowIceHailConditions: Optional[AnyUrl] = Field(
        None, description='Snow ice hail conditions'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startingNoiseLevel: Optional[float] = Field(
        None, description='Starting noise level'
    )
    staticAxleLoadExceptionalPayload: Optional[float] = Field(
        None, description='Static axle load under exceptional payload'
    )
    staticAxleLoadNormalPayload: Optional[float] = Field(
        None, description='Static axle load under normal payload'
    )
    staticAxleLoadWorkingOrder: Optional[float] = Field(
        None, description='Static axle load in working order'
    )
    stationaryNoiseLevel: Optional[float] = Field(
        None, description='Stationary noise level'
    )
    structuralCategory: Optional[str] = Field(None, description='Structural category')
    subCategory: Optional[AnyUrl] = Field(None, description='Vehicle subcategory')
    supportedPlatformHeight: Optional[AnyUrl] = Field(
        None, description='Supported platform height'
    )
    thermalCapacityDistance: Optional[float] = Field(
        None, description='Thermal capacity distance'
    )
    thermalCapacityGradient: Optional[float] = Field(
        None, description='Thermal capacity gradient'
    )
    thermalCapacitySpeed: Optional[float] = Field(
        None, description='Thermal capacity speed'
    )
    thermalCapacityTSIReference: Optional[AnyUrl] = Field(
        None, description='Thermal capacity TSI reference'
    )
    thermalCapacityTime: Optional[float] = Field(
        None, description='Thermal capacity time'
    )
    totalVehicleMass: Optional[float] = Field(None, description='Total vehicle mass')
    trainControlSwitchOverSpecialConditions: Optional[str] = Field(
        None, description='Train control switch over special conditions'
    )
    trainDetectionSystemType: Optional[AnyUrl] = Field(
        None, description='Type of train detection system'
    )
    transportableOnFerry: Optional[bool] = Field(
        None, description='Transportable on ferry'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI data type. It has to be VehicleType'
    )
    typeVersionId: Optional[AnyUrl] = Field(None, description='Type version id')
    typeVersionNumber: Optional[str] = Field(None, description='Type version number')
    usesGroup555: Optional[bool] = Field(None, description='GSM-R use of group 555')
    vehicleContactForce: Optional[float] = Field(
        None, description='Vehicle contact force'
    )
    vehicleKinematicGaugeOther: Optional[str] = Field(
        None, description='Vehicle kinematic gauge other'
    )
    vehicleMaxSandingOutput: Optional[str] = Field(
        None, description='Vehicle max sanding output'
    )
    vehiclePantographHead: Optional[str] = Field(
        None, description='Vehicle pantograph head'
    )
    vehicleTypeMaximumSpeedAndCantDeficiency: Optional[AnyUrl] = Field(
        None, description='Vehicle type maximum speed and cant deficiency'
    )
    vehiclesComposingFixedFormation: Optional[float] = Field(
        None, description='Vehicles composing fixed formation'
    )
    voiceGSMRNetwork: Optional[AnyUrl] = Field(None, description='Voice GSM-R network')
    voiceOperationalCommImpl: Optional[str] = Field(
        None, description='Voice operational communication implementation'
    )
    voiceRadioCompatible: Optional[AnyUrl] = Field(
        None, description='Radio system compatibility voice'
    )
    wheelSetGauge: Optional[AnyUrl] = Field(None, description='Nominal track gauge')
    wheelSetGaugeChangeoverFacility: Optional[AnyUrl] = Field(
        None, description='Wheelset gauge changeover facility'
    )
    wheelSetGaugeTransformationMethod: Optional[str] = Field(
        None, description='Wheel set gauge transformation method'
    )
    wheelchairSleepingPlaces: Optional[str] = Field(
        None, description='Wheelchair sleeping spaces'
    )
    wheelchairSpaces: Optional[float] = Field(None, description='Wheelchair spaces')

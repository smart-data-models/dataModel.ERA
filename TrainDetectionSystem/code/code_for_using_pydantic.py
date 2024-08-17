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
    TrainDetectionSystem = 'TrainDetectionSystem'


class TrainDetectionSystem(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
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
    flangeLubeRules: Optional[bool] = Field(
        None, description='Existence of rules on on-board flange lubrication'
    )
    frenchTrainDetectionSystemLimitation: Optional[AnyUrl] = Field(
        None,
        description='Section with train detection limitation, only for the French network',
    )
    frequencyBandsForDetection: Optional[AnyUrl] = Field(
        None, description='Frequency bands for detection'
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
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxDistConsecutiveAxles: Optional[float] = Field(
        None,
        description='Maximum permitted distance between two consecutive axles in case of TSI non-compliance',
    )
    maxDistEndTrainFirstAxle: Optional[float] = Field(
        None, description='Maximum distance between end of train and first axle'
    )
    maxFlangeHeight: Optional[float] = Field(
        None, description='Maximum permitted height of the flange'
    )
    maxImpedanceWheelset: Optional[float] = Field(
        None,
        description='Maximum permitted impedance between opposite wheels of a wheelset when not TSI compliant',
    )
    maxSandingOutput: Optional[AnyUrl] = Field(
        None, description='Maximum amount of sand'
    )
    maximumInterferenceCurrent: Optional[float] = Field(
        None, description='Maximum interference current'
    )
    minVehicleImpedance: Optional[str] = Field(None, description='Vehicle impedance')
    name: Optional[str] = Field(None, description='The name of this item')
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
    requiredSandingOverride: Optional[bool] = Field(
        None, description='Sanding override by driver required'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    tdsFrenchTrainDetectionSystemLimitation: Optional[AnyUrl] = Field(
        None,
        description='Section with train detection limitation, only for the French network',
    )
    tdsMaximumMagneticField: Optional[AnyUrl] = Field(
        None, description='Train detection system maximum magnetic field'
    )
    tdsMinAxleLoadVehicleCategory: Optional[AnyUrl] = Field(
        None, description='Train detection system min axle load vehicle category'
    )
    trainDetectionSystemSpecificCheck: Optional[AnyUrl] = Field(
        None, description='Type of track circuits to which specific checks are needed'
    )
    trainDetectionSystemSpecificCheckDocument: Optional[str] = Field(
        None,
        description='Document with the procedure(s) related to the type of train detection systems declared in 1.2.1.1.6.1',
    )
    trainDetectionSystemType: Optional[AnyUrl] = Field(
        None, description='Type of train detection system'
    )
    tsiCompliantCompositeBrakeBlocks: Optional[AnyUrl] = Field(
        None, description='TSI compliance of rules on the use of composite brake blocks'
    )
    tsiCompliantFerromagneticWheel: Optional[AnyUrl] = Field(
        None,
        description='TSI compliance of Ferromagnetic characteristics of wheel material required',
    )
    tsiCompliantMaxDistConsecutiveAxles: Optional[AnyUrl] = Field(
        None,
        description='TSI compliance of maximum permitted distance between two consecutive axles',
    )
    tsiCompliantMaxImpedanceWheelset: Optional[AnyUrl] = Field(
        None,
        description='TSI compliance of maximum permitted impedance between opposite wheels of a wheelset',
    )
    tsiCompliantMetalConstruction: Optional[AnyUrl] = Field(
        None, description='TSI compliance of rules for vehicle metal construction'
    )
    tsiCompliantMetalFreeSpace: Optional[AnyUrl] = Field(
        None, description='TSI compliance of rules for metal-free space around wheels'
    )
    tsiCompliantRSTShuntImpedance: Optional[AnyUrl] = Field(
        None,
        description='TSI compliance of rules on combination of RST characteristics influencing shunting impedance',
    )
    tsiCompliantSandCharacteristics: Optional[AnyUrl] = Field(
        None, description='TSI Compliance of rules on sand characteristics'
    )
    tsiCompliantSanding: Optional[AnyUrl] = Field(
        None, description='TSI compliance of sanding'
    )
    tsiCompliantShuntDevices: Optional[AnyUrl] = Field(
        None, description='TSI compliance of rules on shunt assisting devices'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI data type. It has to be TrainDetectionSystem'
    )

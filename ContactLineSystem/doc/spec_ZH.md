<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：联系热线系统    
=========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/ContactLineSystem/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**用于向公路或铁路车辆传输电能的**系统。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 在公共街道上标识特定房产的编号      
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `conditionalRegenerativeBrake[boolean]`: 再生制动许可  - `conditionsAppliedRegenerativeBraking[string]`: 适用于再生制动的条件  - `conditionsChargingElectricEnergyStorage[string]`: 在静止状态下为牵引用蓄电池充电的允许条件  - `contactLineSystemType[uri]`: 接触线系统类型  - `currentLimitationRequired[boolean]`: 需要对电路板进行电流或功率限制  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `energySupplySystem[uri]`: 能源供应系统  - `energySupplySystemTSICompliant[boolean]`: 能源供应系统符合 TSI 标准  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxCurrentStandstillPantograph[number]`: 每个受电弓静止时的最大电流  - `maxTrainCurrent[number]`: 列车最大电流  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `permissionChargingElectricEnergyTractionStandstill[boolean]`: 允许在静止状态下为牵引用蓄电装置充电  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 数据类型。必须是 ContactLineSystem  - `umax2[number]`: 法规 (EU)1301/2014 第 7.4.2.2.1 节和第 7.4.2.11.1 节所述生产线的 Umax2。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
从 ERA 本体映射的数据模型 https://data-interop.era.europa.eu/era-vocabulary（欧盟铁路局）    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ContactLineSystem:      
  description: System that is used to transmit electrical energy to road or rail vehicles.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    conditionalRegenerativeBrake:      
      description: Permission for regenerative braking      
      type: boolean      
      x-ngsi:      
        type: Property      
    conditionsAppliedRegenerativeBraking:      
      description: Conditions applying in regards to regenerative braking      
      type: string      
      x-ngsi:      
        type: Property      
    conditionsChargingElectricEnergyStorage:      
      description: Permitted conditions for charging electric energy storage for traction purposes at standstill      
      type: string      
      x-ngsi:      
        type: Property      
    contactLineSystemType:      
      description: Type of contact line system      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    currentLimitationRequired:      
      description: Current or power limitation on board required      
      type: boolean      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    energySupplySystem:      
      description: Energy supply system      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    energySupplySystemTSICompliant:      
      description: Energy supply system TSI compliant      
      type: boolean      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - Point      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
            type:      
              enum:      
                - Polygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPoint      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiLineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    items:      
                      type: number      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPolygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    maxCurrentStandstillPantograph:      
      description: Maximum current at standstill per pantograph      
      type: number      
      x-ngsi:      
        type: Property      
    maxTrainCurrent:      
      description: Maximum train current      
      type: number      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    permissionChargingElectricEnergyTractionStandstill:      
      description: Permission for charging electric energy storage for traction purposes at standstill      
      type: boolean      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be ContactLineSystem      
      enum:      
        - ContactLineSystem      
      type: string      
      x-ngsi:      
        type: Property      
    umax2:      
      description: Umax2 for lines referred to in sections 7.4.2.2.1 and 7.4.2.11.1 of Regulation (EU)1301/2014.      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/ContactLineSystem      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/ContactLineSystem/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json      
  x-model-tags: 'ERA vocabulary, railway, train'      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### ContactLineSystem NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 ContactLineSystem 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:ORAF:23996206",  
  "dateCreated": "2018-03-08T03:23:31Z",  
  "dateModified": "2021-08-20T12:07:54Z",  
  "source": "Eat election thought team pressure. Tend page true affect politics shoulder provide. Life message important cost night itself event.",  
  "name": "Southern no country without man white when. Let",  
  "alternateName": "Arm detail soon day wait our open number. Society argue a learn identify.",  
  "description": "Girl main model democratic.",  
  "dataProvider": "Sort watch here letter choice down nature. ",  
  "owner": [  
    "urn:ngsi-ld:ContactLineSystem:items:OPHQ:68569337",  
    "urn:ngsi-ld:ContactLineSystem:items:AWZO:22775427"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:ContactLineSystem:items:CXFY:92898664"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      16.1310075,  
      131.493498  
    ]  
  },  
  "address": {  
    "streetAddress": "Nor when wall inside. Discussion experience include rest rather form large.",  
    "addressLocality": "Wife significant think simply author thus town. Sort purpose style discover study. Again themse",  
    "addressRegion": "Political star worker bar. Land if war nothing year with easy. Section other national new eye tree. Thus fine skin address hour imagine.",  
    "addressCountry": "Hour relationship apply practice this development hotel. Any economy score none join including others.",  
    "postalCode": "Present why Mrs former almost black. Officer concern natural federal ",  
    "postOfficeBoxNumber": "Subject yourself remain seek ability energy",  
    "streetNr": "Their staff check TV break. Cup person all air. Show explain maintain ",  
    "district": "Enjoy record as yeah discuss. Even own itself."  
  },  
  "areaServed": "Throughout month dark figure add ago small. Point and financial mu",  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": true,  
  "conditionsAppliedRegenerativeBraking": "Never understand could change arrive. Senior change can surface language.",  
  "conditionsChargingElectricEnergyStorage": "Vo",  
  "currentLimitationRequired": false,  
  "energySupplySystemTSICompliant": false,  
  "maxCurrentStandstillPantograph": 615.8,  
  "maxTrainCurrent": 864,  
  "permissionChargingElectricEnergyTractionStandstill": false,  
  "umax2": 864,  
  "contactLineSystemType": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:PLSG:66048764",  
  "energySupplySystem": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:WZTE:82421948"  
}  
```  
</details>    
#### ContactLineSystem NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的 ContactLineSystem 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:ORAF:23996206",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2018-03-08T03:23:31Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-08-20T12:07:54Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Eat election thought team pressure. Tend page true affect politics shoulder provide. Life message important cost night itself event."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Southern no country without man white when. Let"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Arm detail soon day wait our open number. Society argue a learn identify."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Girl main model democratic."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Sort watch here letter choice down nature. "  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:OPHQ:68569337",  
      "urn:ngsi-ld:ContactLineSystem:items:AWZO:22775427"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:CXFY:92898664"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        16.1310075,  
        131.493498  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Nor when wall inside. Discussion experience include rest rather form large.",  
      "addressLocality": "Wife significant think simply author thus town. Sort purpose style discover study. Again themse",  
      "addressRegion": "Political star worker bar. Land if war nothing year with easy. Section other national new eye tree. Thus fine skin address hour imagine.",  
      "addressCountry": "Hour relationship apply practice this development hotel. Any economy score none join including others.",  
      "postalCode": "Present why Mrs former almost black. Officer concern natural federal ",  
      "postOfficeBoxNumber": "Subject yourself remain seek ability energy",  
      "streetNr": "Their staff check TV break. Cup person all air. Show explain maintain ",  
      "district": "Enjoy record as yeah discuss. Even own itself."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Throughout month dark figure add ago small. Point and financial mu"  
  },  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": {  
    "type": "Boolean",  
    "value": true  
  },  
  "conditionsAppliedRegenerativeBraking": {  
    "type": "Text",  
    "value": "Never understand could change arrive. Senior change can surface language."  
  },  
  "conditionsChargingElectricEnergyStorage": {  
    "type": "Text",  
    "value": "Vo"  
  },  
  "currentLimitationRequired": {  
    "type": "Boolean",  
    "value": false  
  },  
  "energySupplySystemTSICompliant": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Number",  
    "value": 615.8  
  },  
  "maxTrainCurrent": {  
    "type": "Number",  
    "value": 864  
  },  
  "permissionChargingElectricEnergyTractionStandstill": {  
    "type": "Boolean",  
    "value": false  
  },  
  "umax2": {  
    "type": "Number",  
    "value": 864  
  },  
  "contactLineSystemType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:PLSG:66048764"  
  },  
  "energySupplySystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:WZTE:82421948"  
  }  
}  
```  
</details>    
#### ContactLineSystem NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 ContactLineSystem 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:ORAF:23996206",  
  "dateCreated": "2018-03-08T03:23:31Z",  
  "dateModified": "2021-08-20T12:07:54Z",  
  "source": "Eat election thought team pressure. Tend page true affect politics shoulder provide. Life message important cost night itself event.",  
  "name": "Southern no country without man white when. Let",  
  "alternateName": "Arm detail soon day wait our open number. Society argue a learn identify.",  
  "description": "Girl main model democratic.",  
  "dataProvider": "Sort watch here letter choice down nature. ",  
  "owner": [  
    "urn:ngsi-ld:ContactLineSystem:items:OPHQ:68569337",  
    "urn:ngsi-ld:ContactLineSystem:items:AWZO:22775427"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:ContactLineSystem:items:CXFY:92898664"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      16.1310075,  
      131.493498  
    ]  
  },  
  "address": {  
    "streetAddress": "Nor when wall inside. Discussion experience include rest rather form large.",  
    "addressLocality": "Wife significant think simply author thus town. Sort purpose style discover study. Again themse",  
    "addressRegion": "Political star worker bar. Land if war nothing year with easy. Section other national new eye tree. Thus fine skin address hour imagine.",  
    "addressCountry": "Hour relationship apply practice this development hotel. Any economy score none join including others.",  
    "postalCode": "Present why Mrs former almost black. Officer concern natural federal ",  
    "postOfficeBoxNumber": "Subject yourself remain seek ability energy",  
    "streetNr": "Their staff check TV break. Cup person all air. Show explain maintain ",  
    "district": "Enjoy record as yeah discuss. Even own itself."  
  },  
  "areaServed": "Throughout month dark figure add ago small. Point and financial mu",  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": true,  
  "conditionsAppliedRegenerativeBraking": "Never understand could change arrive. Senior change can surface language.",  
  "conditionsChargingElectricEnergyStorage": "Vo",  
  "currentLimitationRequired": false,  
  "energySupplySystemTSICompliant": false,  
  "maxCurrentStandstillPantograph": 615.8,  
  "maxTrainCurrent": 864,  
  "permissionChargingElectricEnergyTractionStandstill": false,  
  "umax2": 864,  
  "contactLineSystemType": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:PLSG:66048764",  
  "energySupplySystem": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:WZTE:82421948",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### ContactLineSystem NGSI-LD 标准化示例    
下面是一个以 JSON-LD 格式规范化的 ContactLineSystem 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:YUFG:14034194",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1989-01-20T05:58:09Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1972-01-07T08:46:29Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Pick red ability information. Positive development policy financial learn career. Nothing firm at memory."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Face response pass cut perform easy. Discuss couple think no difference singl"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Trade international loss friend every sing available because. Per agent stock call manage share."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Worry certain if our thought it resource. Everyone blood commercial respond face take probably. Culture their concern trade crime."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Including future politics return table mention section. Together year agency know. Manager image positive suffer perform enough."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:GYWA:00643390",  
      "urn:ngsi-ld:ContactLineSystem:items:WEEM:69764788"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:WMLL:21052726"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        88.082114,  
        -116.450812  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Role even option. Push play firm may. City grow director audience body reduce.",  
      "addressLocality": "Report yet sit hundred use political his. Build special recently make.",  
      "addressRegion": "Floor someone tend. News fight against fall television. Writer full bed official concern small.",  
      "addressCountry": "Lead consider hundred offer look hit future. Fly appear remain pattern wall goal.",  
      "postalCode": "Suddenly our visit that field. Trip fi",  
      "postOfficeBoxNumber": "Current wha",  
      "streetNr": "Page effort station.",  
      "district": "Next respond oil important guy leave capital. Provide street good create range growth war. Visit across media consumer land spring total well."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "White laugh space discussion. Throw international continue while senior gas pro"  
  },  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": {  
    "type": "Property",  
    "value": false  
  },  
  "conditionsAppliedRegenerativeBraking": {  
    "type": "Property",  
    "value": "Design hard short dream cost entire year. Better consumer recently. Population rich recent tough environmental rock image speech."  
  },  
  "conditionsChargingElectricEnergyStorage": {  
    "type": "Property",  
    "value": "Force inside tell. Daughter miss true member voice thus. Dream many which church strong "  
  },  
  "currentLimitationRequired": {  
    "type": "Property",  
    "value": true  
  },  
  "energySupplySystemTSICompliant": {  
    "type": "Property",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Property",  
    "value": 773.8  
  },  
  "maxTrainCurrent": {  
    "type": "Property",  
    "value": 68  
  },  
  "permissionChargingElectricEnergyTractionStandstill": {  
    "type": "Property",  
    "value": false  
  },  
  "umax2": {  
    "type": "Property",  
    "value": 756  
  },  
  "contactLineSystemType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:JNYV:94337272"  
  },  
  "energySupplySystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:BFQY:01787468"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

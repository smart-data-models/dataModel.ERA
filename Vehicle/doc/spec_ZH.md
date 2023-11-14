<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：车辆  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/Vehicle/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**能够在铁路线上行驶的特定车辆或货车。  
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
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `compositeBrakeBlockRetrofitted[boolean]`: 加装复合制动块  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `manufacturingCountry[uri]`: 制造业国家  - `name[string]`: 该项目的名称  - `operationalRestriction[uri]`: 运行限制  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `quieterRoutesExemptedCountry[uri]`: 更安静的路线豁免国家  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 数据类型。必须是车辆  - `vehicleKeeper[uri]`: 车辆保管员  - `vehicleNumber[string]`: 车辆编号  - `vehicleSeries[string]`: 车辆系列  - `vehicleType[uri]`: 车辆类型  <!-- /30-PropertiesList -->  
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
Vehicle:    
  description: A specific vehicle or wagon able to operate over railway lines.    
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
    compositeBrakeBlockRetrofitted:    
      description: Composite brake block retrofitted    
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
    manufacturingCountry:    
      description: Manufacturing country    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operationalRestriction:    
      description: Operational restriction    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    quieterRoutesExemptedCountry:    
      description: Quieter route exempted country    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
      description: NGSI data type. It has to be Vehicle    
      enum:    
        - Vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleKeeper:    
      description: Vehicle keeper    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    vehicleNumber:    
      description: Vehicle number    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleSeries:    
      description: Vehicle series    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: Vehicle type    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Vehicle    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Vehicle/LICENSE.md    
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
#### 车辆 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的车辆示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": "1981-05-29T06:37:15Z",  
  "dateModified": "2007-08-18T15:43:14Z",  
  "source": "Visit research power especially ",  
  "name": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door",  
  "alternateName": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research",  
  "description": "Morning continue help p",  
  "dataProvider": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half.",  
  "owner": [  
    "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
    "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      20.376035,  
      172.96204  
    ]  
  },  
  "address": {  
    "streetAddress": "Lay agree media everyone. Ability because cover.",  
    "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
    "addressRegion": "Se",  
    "addressCountry": "Course down what maybe physical. Memory dev",  
    "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
    "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
    "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
    "district": "Order teacher yes head. Report partner without government discuss shoulder."  
  },  
  "areaServed": "Great office person",  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": true,  
  "vehicleNumber": "Of light force police. Indicate best need.",  
  "vehicleSeries": "High article bill ",  
  "manufacturingCountry": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975",  
  "operationalRestriction": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720",  
  "quieterRoutesExemptedCountry": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691",  
  "vehicleKeeper": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099",  
  "vehicleType": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377"  
}  
```  
</details>  
#### 车辆 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的车辆示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1981-05-29T06:37:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2007-08-18T15:43:14Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Visit research power especially "  
  },  
  "name": {  
    "type": "Text",  
    "value": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Morning continue help p"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
      "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          20.376035,  
          172.96204  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Lay agree media everyone. Ability because cover."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Se"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Course down what maybe physical. Memory dev"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "To bit provide individual. Drug let bed v"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Order teacher yes head. Report partner without government discuss shoulder."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Great office person"  
  },  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleNumber": {  
    "type": "Text",  
    "value": "Of light force police. Indicate best need."  
  },  
  "vehicleSeries": {  
    "type": "Text",  
    "value": "High article bill "  
  },  
  "manufacturingCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975"  
  },  
  "operationalRestriction": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720"  
  },  
  "quieterRoutesExemptedCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691"  
  },  
  "vehicleKeeper": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099"  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377"  
  }  
}  
```  
</details>  
#### 车辆 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的车辆示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": "1981-05-29T06:37:15Z",  
  "dateModified": "2007-08-18T15:43:14Z",  
  "source": "Visit research power especially ",  
  "name": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door",  
  "alternateName": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research",  
  "description": "Morning continue help p",  
  "dataProvider": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half.",  
  "owner": [  
    "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
    "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      20.376035,  
      172.96204  
    ]  
  },  
  "address": {  
    "streetAddress": "Lay agree media everyone. Ability because cover.",  
    "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
    "addressRegion": "Se",  
    "addressCountry": "Course down what maybe physical. Memory dev",  
    "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
    "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
    "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
    "district": "Order teacher yes head. Report partner without government discuss shoulder."  
  },  
  "areaServed": "Great office person",  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": true,  
  "vehicleNumber": "Of light force police. Indicate best need.",  
  "vehicleSeries": "High article bill ",  
  "manufacturingCountry": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975",  
  "operationalRestriction": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720",  
  "quieterRoutesExemptedCountry": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691",  
  "vehicleKeeper": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099",  
  "vehicleType": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 车辆 NGSI-LD 标准化示例  
下面是一个以 JSON-LD 格式规范化的车辆示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:RFYH:06883935",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-06-19T07:24:12Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1998-03-27T15:27:54Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Project option account government. Ask company grow."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Part matter sh"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nearly alone the when together. Whole sure would require mission."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Church exactly remain situation training effect resource. Movie describe concern single as population moment. Director stage range professional fast. Sell talk onto whom question job decid"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Place teacher support teach practice son pay college. Sit certain near short area by decision. Stand size guy reason rese"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:EBYW:72457592",  
      "urn:ngsi-ld:Vehicle:items:MJUB:28310670"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:WNSX:51918079"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -37.542901,  
        -116.836751  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Rich thousand authority beat best white free. Tend season get prevent wind. Catch door foot wrong citizen miss develop.",  
      "addressLocality": "Test growth another. Be easy painting human. College ",  
      "addressRegion": "Nice pay pattern sense education game. Tonight yourself spring though participant threat majority.",  
      "addressCountry": "Purpose case eight just. Cause discussion technology sing.",  
      "postalCode": "Yeah conference push determine I tough.",  
      "postOfficeBoxNumber": "Sea also cell office force letter week. Total create as onto people. Full wall address early lose everything kid.",  
      "streetNr": "Why rise PM mother bank light. Ha",  
      "district": "Responsibility blue increase. Newspaper remain else"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Make own mother news film PM some. All arrive than put cold five stand."  
  },  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": {  
    "type": "Property",  
    "value": false  
  },  
  "vehicleNumber": {  
    "type": "Property",  
    "value": "Sure stock standard child goal in. Option hand parent piece no."  
  },  
  "vehicleSeries": {  
    "type": "Property",  
    "value": "Public story thus wind whether. Sometimes attorney couple person hand green. Within seek sid"  
  },  
  "manufacturingCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:manufacturingCountry:YUHQ:94193670"  
  },  
  "operationalRestriction": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:operationalRestriction:HSZJ:08079193"  
  },  
  "quieterRoutesExemptedCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:HKQL:88249057"  
  },  
  "vehicleKeeper": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZJDS:72987137"  
  },  
  "vehicleType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:vehicleType:KUTI:03320913"  
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

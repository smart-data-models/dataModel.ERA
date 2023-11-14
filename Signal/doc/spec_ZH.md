<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：信号  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/Signal/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**铁路信号是铁路轨道旁的一个装置，用于向火车司机发出下一个区间的最高允许速度信号。  
定义 RSM：通过常规视觉或听觉指示的装置，通常与铁路车辆的移动有关。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一标识  - `relativeDistanceDangerPoint[number]`: 危险点的相对距离  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `signalId[string]`: 信号名称  - `signalOrientation[uri]`: 信号方向  - `signalType[uri]`: 信号类型  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `track[uri]`: 轨道  - `type[string]`: NGSI 数据类型。必须是信号  <!-- /30-PropertiesList -->  
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
Signal:    
  description: |-    
    A railway signal is an installation next to the railway track for signalling the maximum allowed speed in the next block section to the train driver.    
    Definition RSM: Apparatus by means of which a conventional visual or acoustic indication is given, generally concerning the movements of railway vehicles.    
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
    relativeDistanceDangerPoint:    
      description: Relative distance of the danger point    
      type: number    
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
    signalId:    
      description: Name of signal    
      type: string    
      x-ngsi:    
        type: Property    
    signalOrientation:    
      description: Signal orientation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    signalType:    
      description: Type of signal    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    track:    
      description: Track    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI data type. It has to be Signal    
      enum:    
        - Signal    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Signal    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Signal/LICENSE.md    
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
#### 信号 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的信号示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
}  
```  
</details>  
#### 信号 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的信号示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1970-03-08T14:32:13Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2011-08-18T23:12:35Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Here choose style decade occur leader"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Drop"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Truth add because former. Indeed long yeah change near experience."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:OCNG:88914328",  
      "urn:ngsi-ld:Signal:items:QDWA:77960070"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:IKCH:27474652"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          7.167995,  
          -149.393214  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Upon certainly west population. A walk result product major draw "  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Account rich measure every price energy allow. Put customer c"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Prepare family across front. Nothing main religious strategy seven notice where."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Word wai"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Meet know training. Land grow old kid effect. Form director decide join draw."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Several center notice ever deal his. National parent fund focus pull those door."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Activity"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Number",  
    "value": 864  
  },  
  "signalId": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peac"  
  },  
  "signalOrientation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156"  
  },  
  "signalType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalType:CXMW:87784080"  
  },  
  "track": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
  }  
}  
```  
</details>  
#### 信号 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的信号示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 信号 NGSI-LD 归一化示例  
下面是一个以 JSON-LD 格式规范化的信号示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:SUMI:05987689",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2013-12-11T15:53:44Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-09-10T20:37:14Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Owner support present act enter."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Start read half."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Home state area operation respond early. Edge return condition federal."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Total again here high. Team report again ask product these cut."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Republican eight think start. Hot movie want serve father audience management."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:MZLV:03669390",  
      "urn:ngsi-ld:Signal:items:LNRS:49951624"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:JOYH:86575892"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -13.176379,  
        -116.163154  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Coach my discover both usually east page. Rather lead investment child as record resource. In product rise couple v",  
      "addressLocality": "Conference pull tax indeed. Very trou",  
      "addressRegion": "Man issue two memory every. Television traditional draw democratic.",  
      "addressCountry": "Fund threat they increase. Guy series politics bag.",  
      "postalCode": "Production later according down yes. Nothing my forward.",  
      "postOfficeBoxNumber": "Beat maintain people",  
      "streetNr": "East too Republican represent behind leader. Little television few Republican fire behavior good.",  
      "district": "Ever theory social special century spring."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "It she follow board blood. Certainly easy particular she sure by big. Say cold national expect rock. Value ski"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Property",  
    "value": 859  
  },  
  "signalId": {  
    "type": "Property",  
    "value": "Mean PM capital car particular head. Claim ago brother forget. Benefit start body ask yet age believe."  
  },  
  "signalOrientation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalOrientation:XSWZ:79200878"  
  },  
  "signalType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalType:OIXR:27955866"  
  },  
  "track": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:track:SBLI:67422940"  
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

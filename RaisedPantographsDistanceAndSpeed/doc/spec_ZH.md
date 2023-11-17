<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：养成的螳螂距离和速度    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/RaisedPantographsDistanceAndSpeed/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**表示在给定速度下每列列车允许的最大受电弓数量和相邻受电弓弓头中心线到中心线的最小间距（以米为单位）。    
每条轨道可以有多个每列列车允许的凸起式受电弓（结构化）值，每个受电弓都有受电弓数量、受电弓之间的最小间距（以米为单位）和车速（以公里/小时为单位）**。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `raisedPantographsDistance[number]`: 加高的受电弓距离  - `raisedPantographsNumber[number]`: 受电弓数量  - `raisedPantographsSpeed[number]`: 加高的受电弓速度  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 数据类型。它必须是 RaisedPantographsDistanceAndSpeed（RaisedPantographs距离和速度）。  <!-- /30-PropertiesList -->    
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
RaisedPantographsDistanceAndSpeed:      
  description: |-      
    Indication of maximum number of raised pantographs per train allowed and minimum spacing centre line to centre line of adjacent pantograph heads, expressed in metres, at the given speed.      
    Each track can have several raised pantographs per train allowed (structured) values, and each one has values for number of pantographs, minimum distance between pantographs, in metres, and speed considered in km/h.      
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
    raisedPantographsDistance:      
      description: Raised pantographs distance      
      type: number      
      x-ngsi:      
        type: Property      
    raisedPantographsNumber:      
      description: Number of pantographs.      
      type: number      
      x-ngsi:      
        type: Property      
    raisedPantographsSpeed:      
      description: Raised pantographs speed      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be RaisedPantographsDistanceAndSpeed      
      enum:      
        - RaisedPantographsDistanceAndSpeed      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/RaisedPantographsDistanceAndSpeed      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/RaisedPantographsDistanceAndSpeed/LICENSE.md      
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
#### RaisedPantographsDistanceAndSpeed NGSI-v2 关键值 示例    
下面是一个以 JSON-LD 格式作为键值的 RaisedPantographsDistanceAndSpeed 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": "2016-10-01T23:32:51Z",  
  "dateModified": "1994-01-08T16:04:55Z",  
  "source": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment.",  
  "name": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter.",  
  "alternateName": "Describe other scene standard citizen. Exist letter down ready TV phon",  
  "description": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning.",  
  "dataProvider": "Song minute like table knowledge state. Notice line never support stop.",  
  "owner": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      52.853707,  
      -40.868675  
    ]  
  },  
  "address": {  
    "streetAddress": "Special son three figure cost mili",  
    "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
    "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
    "addressCountry": "Consumer include little. Seem ",  
    "postalCode": "Out everything senior. Out staff",  
    "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
    "streetNr": "",  
    "district": "Worker expect realize above. I differenc"  
  },  
  "areaServed": "Table must who. Grow in ",  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": 864,  
  "raisedPantographsNumber": 864,  
  "raisedPantographsSpeed": 864,  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RaisedPantographsDistanceAndSpeed NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的 RaisedPantographsDistanceAndSpeed 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2016-10-01T23:32:51Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1994-01-08T16:04:55Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment."  
  },  
  "name": {  
    "type": "Text",  
    "value": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Describe other scene standard citizen. Exist letter down ready TV phon"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Song minute like table knowledge state. Notice line never support stop."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        52.853707,  
        -40.868675  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Special son three figure cost mili",  
      "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
      "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
      "addressCountry": "Consumer include little. Seem ",  
      "postalCode": "Out everything senior. Out staff",  
      "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
      "streetNr": "",  
      "district": "Worker expect realize above. I differenc"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Table must who. Grow in "  
  },  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": {  
    "type": "Number",  
    "value": 864  
  },  
  "raisedPantographsNumber": {  
    "type": "Number",  
    "value": 864  
  },  
  "raisedPantographsSpeed": {  
    "type": "Number",  
    "value": 864  
  },  
  "context": {  
    "type": "StructuredValue",  
    "value": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
    ]  
  }  
}  
```  
</details>    
#### RaisedPantographsDistanceAndSpeed NGSI-LD 关键值 示例    
下面是一个以 JSON-LD 格式作为键值的 RaisedPantographsDistanceAndSpeed 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": "2016-10-01T23:32:51Z",  
  "dateModified": "1994-01-08T16:04:55Z",  
  "source": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment.",  
  "name": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter.",  
  "alternateName": "Describe other scene standard citizen. Exist letter down ready TV phon",  
  "description": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning.",  
  "dataProvider": "Song minute like table knowledge state. Notice line never support stop.",  
  "owner": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      52.853707,  
      -40.868675  
    ]  
  },  
  "address": {  
    "streetAddress": "Special son three figure cost mili",  
    "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
    "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
    "addressCountry": "Consumer include little. Seem ",  
    "postalCode": "Out everything senior. Out staff",  
    "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
    "streetNr": "",  
    "district": "Worker expect realize above. I differenc"  
  },  
  "areaServed": "Table must who. Grow in ",  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": 864,  
  "raisedPantographsNumber": 864,  
  "raisedPantographsSpeed": 864,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RaisedPantographsDistanceAndSpeed NGSI-LD 归一化示例    
下面是一个以 JSON-LD 格式规范化的 RaisedPantographsDistanceAndSpeed 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:NRAH:81561263",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1971-11-20T03:14:14Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1970-10-03T20:50:52Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "War game help give"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Watch within challenge safe. Raise available seem compare body early. None face safe term before environment drop"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Court I loo"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Them site whole should play generation question. Significant on teach of none."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Bag care religious possible source media team. Skill politics blue yes according."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:DKUU:20419467",  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:BFPP:72232537"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:XVYI:24654995"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        33.252656,  
        109.596554  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Break seem system real part become pay. Sense baby total care investment. Figure break likely behavior talk morning estab",  
      "addressLocality": "Quite himself drive trouble pay they guy. History role mome",  
      "addressRegion": "Cut seem painting race.",  
      "addressCountry": "Room whose forget soldier evidence air. Memory artist real western myse",  
      "postalCode": "Glass artist leg modern. Republican reflect hot skill democratic speak.",  
      "postOfficeBoxNumber": "Serious art magazine morning serious histor",  
      "streetNr": "Small w",  
      "district": "Remain environment performance campaign. Test traditional want call. Building forget argue suggest."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Forward gun require "  
  },  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": {  
    "type": "Property",  
    "value": 131  
  },  
  "raisedPantographsNumber": {  
    "type": "Property",  
    "value": 478  
  },  
  "raisedPantographsSpeed": {  
    "type": "Property",  
    "value": 219  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
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

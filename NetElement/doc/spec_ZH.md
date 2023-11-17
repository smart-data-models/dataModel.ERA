<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体网络元素    
======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/NetElement/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述**用于定义拓扑网络连接图中节点的**基类。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `elementPart[uri]`: 要素部分  - `endIntrinsicCoordinate[number]`: 终点固有坐标  - `hasImplementation[uri]`: 是否已实施  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `startIntrinsicCoordinate[number]`: 起始内在坐标  - `type[string]`: NGSI 数据类型。必须是 NetElement  <!-- /30-PropertiesList -->    
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
NetElement:      
  description: Base class for defining nodes in the connectivity graph representing the topological network.      
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
    elementPart:      
      description: Element part      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    endIntrinsicCoordinate:      
      description: End intrinsic coordinate      
      type: number      
      x-ngsi:      
        type: Property      
    hasImplementation:      
      description: Has implementation      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    startIntrinsicCoordinate:      
      description: Start intrinsic coordinate      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be NetElement      
      enum:      
        - NetElement      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/NetElement      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/NetElement/LICENSE.md      
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
#### NetElement NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 NetElement 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:CDPU:99275524",  
  "dateCreated": "2004-12-12T04:49:10Z",  
  "dateModified": "1992-12-16T09:32:23Z",  
  "source": "Natural film decade",  
  "name": "Price institution dream somebody although song how. Low describe energy significant light road great both. Add explain likely way smile new. Fast must leg public",  
  "alternateName": "Common wind western ball read along. Statement another type seat store. Hot case pressure identify lead.",  
  "description": "Truth expect in recently face. By spend social benefit ask response.",  
  "dataProvider": "Sing whole pres",  
  "owner": [  
    "urn:ngsi-ld:NetElement:items:OKII:37700408",  
    "urn:ngsi-ld:NetElement:items:MRRB:33006272"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetElement:items:NKYQ:56695981"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.6509805,  
      -162.802435  
    ]  
  },  
  "address": {  
    "streetAddress": "Way party system teacher purpose federal. For top far sell.",  
    "addressLocality": "These everyone no measure free finish decision call. Car somebody across glass war ask part. Quality here himself popular service suffer.",  
    "addressRegion": "Article despite environmental service head relate from. L",  
    "addressCountry": "Agreement cover study off. Choose back laugh who management communit",  
    "postalCode": "Radio short thought whole contain. Effect contain character after seem put debate. Decision true mission front maintain re",  
    "postOfficeBoxNumber": "Generatio",  
    "streetNr": "Fi",  
    "district": "Weight over big former dream character. Network anyone easy campaign seek of realize right. Range level level kind cause. Score miss need wear push walk month region."  
  },  
  "areaServed": "She reduce policy necessary campaign your.",  
  "type": "NetElement",  
  "endIntrinsicCoordinate": 172.2,  
  "startIntrinsicCoordinate": 698.8,  
  "elementPart": "urn:ngsi-ld:NetElement:elementPart:MXDV:95711699",  
  "hasImplementation": "urn:ngsi-ld:NetElement:hasImplementation:GOYF:07477051"  
}  
```  
</details>    
#### NetElement NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 NetElement 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:CDPU:99275524",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2004-12-12T04:49:10Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1992-12-16T09:32:23Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Natural film decade"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Price institution dream somebody although song how. Low describe energy significant light road great both. Add explain likely way smile new. Fast must leg public"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Common wind western ball read along. Statement another type seat store. Hot case pressure identify lead."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Truth expect in recently face. By spend social benefit ask response."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Sing whole pres"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:OKII:37700408",  
      "urn:ngsi-ld:NetElement:items:MRRB:33006272"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:NKYQ:56695981"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.6509805,  
        -162.802435  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Way party system teacher purpose federal. For top far sell.",  
      "addressLocality": "These everyone no measure free finish decision call. Car somebody across glass war ask part. Quality here himself popular service suffer.",  
      "addressRegion": "Article despite environmental service head relate from. L",  
      "addressCountry": "Agreement cover study off. Choose back laugh who management communit",  
      "postalCode": "Radio short thought whole contain. Effect contain character after seem put debate. Decision true mission front maintain re",  
      "postOfficeBoxNumber": "Generatio",  
      "streetNr": "Fi",  
      "district": "Weight over big former dream character. Network anyone easy campaign seek of realize right. Range level level kind cause. Score miss need wear push walk month region."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "She reduce policy necessary campaign your."  
  },  
  "type": "NetElement",  
  "endIntrinsicCoordinate": {  
    "type": "Number",  
    "value": 172.2  
  },  
  "startIntrinsicCoordinate": {  
    "type": "Number",  
    "value": 698.8  
  },  
  "elementPart": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetElement:elementPart:MXDV:95711699"  
  },  
  "hasImplementation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetElement:hasImplementation:GOYF:07477051"  
  }  
}  
```  
</details>    
#### NetElement NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 NetElement 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:CDPU:99275524",  
  "dateCreated": "2004-12-12T04:49:10Z",  
  "dateModified": "1992-12-16T09:32:23Z",  
  "source": "Natural film decade",  
  "name": "Price institution dream somebody although song how. Low describe energy significant light road great both. Add explain likely way smile new. Fast must leg public",  
  "alternateName": "Common wind western ball read along. Statement another type seat store. Hot case pressure identify lead.",  
  "description": "Truth expect in recently face. By spend social benefit ask response.",  
  "dataProvider": "Sing whole pres",  
  "owner": [  
    "urn:ngsi-ld:NetElement:items:OKII:37700408",  
    "urn:ngsi-ld:NetElement:items:MRRB:33006272"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetElement:items:NKYQ:56695981"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.6509805,  
      -162.802435  
    ]  
  },  
  "address": {  
    "streetAddress": "Way party system teacher purpose federal. For top far sell.",  
    "addressLocality": "These everyone no measure free finish decision call. Car somebody across glass war ask part. Quality here himself popular service suffer.",  
    "addressRegion": "Article despite environmental service head relate from. L",  
    "addressCountry": "Agreement cover study off. Choose back laugh who management communit",  
    "postalCode": "Radio short thought whole contain. Effect contain character after seem put debate. Decision true mission front maintain re",  
    "postOfficeBoxNumber": "Generatio",  
    "streetNr": "Fi",  
    "district": "Weight over big former dream character. Network anyone easy campaign seek of realize right. Range level level kind cause. Score miss need wear push walk month region."  
  },  
  "areaServed": "She reduce policy necessary campaign your.",  
  "type": "NetElement",  
  "endIntrinsicCoordinate": 172.2,  
  "startIntrinsicCoordinate": 698.8,  
  "elementPart": "urn:ngsi-ld:NetElement:elementPart:MXDV:95711699",  
  "hasImplementation": "urn:ngsi-ld:NetElement:hasImplementation:GOYF:07477051",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### NetElement NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 NetElement 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:NVEI:78144573",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-10-25T09:04:55Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1972-02-02T07:09:51Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Increase administration contain main. Top every your. Approach raise cup kid region under pay."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Indicate group son local suddenly loss."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pul"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Of shoulder push total throw security. Worker body season soon just skin room."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Ok value system send worker. Worry mouth exist economy red. Home voice out offer think make while effort."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:HDKF:77009578",  
      "urn:ngsi-ld:NetElement:items:IZMH:45951686"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:TRQK:78299265"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -82.8184375,  
        29.596471  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Dinner pay business attorney. Bring picture easy knowledge financial.",  
      "addressLocality": "Stock available country onto single have after. Tonight want detail audience best partner better thus.",  
      "addressRegion": "Individual sign most outside position ",  
      "addressCountry": "Treat same head court beyond discuss bad security.",  
      "postalCode": "Western mention large tro",  
      "postOfficeBoxNumber": "Go hold behavior. Police mind sometimes political impact seat. Everyone allow forward weight.",  
      "streetNr": "Step rate start. Term clearly character.",  
      "district": "Over my citizen alone know standard single garden. Daughter sure once whose or."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Wall dream hold team whatever continue field draw. Result poor educati"  
  },  
  "type": "NetElement",  
  "endIntrinsicCoordinate": {  
    "type": "Property",  
    "value": 437.0  
  },  
  "startIntrinsicCoordinate": {  
    "type": "Property",  
    "value": 884.3  
  },  
  "elementPart": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetElement:elementPart:QPYN:94443064"  
  },  
  "hasImplementation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetElement:hasImplementation:LVLV:02180509"  
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

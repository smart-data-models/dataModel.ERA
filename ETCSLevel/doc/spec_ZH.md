<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：ETCSLevel  
============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/ETCSLevel/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**与轨道侧设备相关的 **ERTMS / ETCS 应用级别。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `etcsBaseline[uri]`: ETCS 基线  - `etcsLevelType[uri]`: ETCS 等级类型  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 数据类型。必须是 ETCSLevel  <!-- /30-PropertiesList -->  
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
ETCSLevel:    
  description: ERTMS / ETCS application level related to the track side equipment.    
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
    etcsBaseline:    
      description: ETCS baseline    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    etcsLevelType:    
      description: ETCS level type    
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
    type:    
      description: NGSI data type. It has to be ETCSLevel    
      enum:    
        - ETCSLevel    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/ETCSLevel    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/ETCSLevel/LICENSE.md    
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
#### ETCSLevel NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 ETCSLevel 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ETCSLevel:id:RSJO:91077542",  
  "dateCreated": "1997-11-29T05:48:43Z",  
  "dateModified": "2015-07-18T00:41:49Z",  
  "source": "Pri",  
  "name": "Sure hand project sometimes. Since charge story. Again American value reflect.",  
  "alternateName": "Whom beat begin us m",  
  "description": "Three ok attack attack unit in. Will m",  
  "dataProvider": "Trouble nation score her brother happy. Discuss opportunity cup ball same professor contain. Onto student PM. Siz",  
  "owner": [  
    "urn:ngsi-ld:ETCSLevel:items:MFHE:53716316",  
    "urn:ngsi-ld:ETCSLevel:items:QJNT:88274906"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:ETCSLevel:items:SYYH:37259358"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -79.0649155,  
      11.28973  
    ]  
  },  
  "address": {  
    "streetAddress": "Amount fall concern",  
    "addressLocality": "Agreement it often society several there arrive. Right marriage be where student five",  
    "addressRegion": "Here drop total sort teacher pick knowledge. Yeah time station stop. Scene threat economy bit. Education couple economic Democrat chair.",  
    "addressCountry": "Last hold everybody true air. Anything member book base north. Discover shake he would several series my painting. Whether capital mai",  
    "postalCode": "Drop son guy give. Once southern seek guess wait final.",  
    "postOfficeBoxNumber": "Central away be number Congress choice. Rich money too identify general behavior tough.",  
    "streetNr": "Maintain too loss why those write. Design policy truth. Office trouble never stand.",  
    "district": "Politics scene because choose avoid assume personal teach. Why market interest tough way more none. "  
  },  
  "areaServed": "Necessary garden final arrive. Sport choice ",  
  "type": "ETCSLevel",  
  "etcsBaseline": "urn:ngsi-ld:ETCSLevel:etcsBaseline:HAGI:99857296",  
  "etcsLevelType": "urn:ngsi-ld:ETCSLevel:etcsLevelType:VOLD:97362219",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### ETCSLevel NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 ETCSLevel 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ETCSLevel:id:RSJO:91077542",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1997-11-29T05:48:43Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2015-07-18T00:41:49Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Pri"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Sure hand project sometimes. Since charge story. Again American value reflect."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Whom beat begin us m"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Three ok attack attack unit in. Will m"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Trouble nation score her brother happy. Discuss opportunity cup ball same professor contain. Onto student PM. Siz"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:ETCSLevel:items:MFHE:53716316",  
      "urn:ngsi-ld:ETCSLevel:items:QJNT:88274906"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:ETCSLevel:items:SYYH:37259358"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -79.0649155,  
          11.28973  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Amount fall concern"  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Agreement it often society several there arrive. Right marriage be where student five"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Here drop total sort teacher pick knowledge. Yeah time station stop. Scene threat economy bit. Education couple economic Democrat chair."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Last hold everybody true air. Anything member book base north. Discover shake he would several series my painting. Whether capital mai"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Drop son guy give. Once southern seek guess wait final."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Central away be number Congress choice. Rich money too identify general behavior tough."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Maintain too loss why those write. Design policy truth. Office trouble never stand."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Politics scene because choose avoid assume personal teach. Why market interest tough way more none. "  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Necessary garden final arrive. Sport choice "  
  },  
  "type": "ETCSLevel",  
  "etcsBaseline": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:ETCSLevel:etcsBaseline:HAGI:99857296"  
  },  
  "etcsLevelType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:ETCSLevel:etcsLevelType:VOLD:97362219"  
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
#### ETCSLevel NGSI-LD 键值 示例  
下面是一个以 JSON-LD 格式作为键值的 ETCSLevel 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ETCSLevel:id:RSJO:91077542",  
  "dateCreated": "1997-11-29T05:48:43Z",  
  "dateModified": "2015-07-18T00:41:49Z",  
  "source": "Pri",  
  "name": "Sure hand project sometimes. Since charge story. Again American value reflect.",  
  "alternateName": "Whom beat begin us m",  
  "description": "Three ok attack attack unit in. Will m",  
  "dataProvider": "Trouble nation score her brother happy. Discuss opportunity cup ball same professor contain. Onto student PM. Siz",  
  "owner": [  
    "urn:ngsi-ld:ETCSLevel:items:MFHE:53716316",  
    "urn:ngsi-ld:ETCSLevel:items:QJNT:88274906"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:ETCSLevel:items:SYYH:37259358"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -79.0649155,  
      11.28973  
    ]  
  },  
  "address": {  
    "streetAddress": "Amount fall concern",  
    "addressLocality": "Agreement it often society several there arrive. Right marriage be where student five",  
    "addressRegion": "Here drop total sort teacher pick knowledge. Yeah time station stop. Scene threat economy bit. Education couple economic Democrat chair.",  
    "addressCountry": "Last hold everybody true air. Anything member book base north. Discover shake he would several series my painting. Whether capital mai",  
    "postalCode": "Drop son guy give. Once southern seek guess wait final.",  
    "postOfficeBoxNumber": "Central away be number Congress choice. Rich money too identify general behavior tough.",  
    "streetNr": "Maintain too loss why those write. Design policy truth. Office trouble never stand.",  
    "district": "Politics scene because choose avoid assume personal teach. Why market interest tough way more none. "  
  },  
  "areaServed": "Necessary garden final arrive. Sport choice ",  
  "type": "ETCSLevel",  
  "etcsBaseline": "urn:ngsi-ld:ETCSLevel:etcsBaseline:HAGI:99857296",  
  "etcsLevelType": "urn:ngsi-ld:ETCSLevel:etcsLevelType:VOLD:97362219",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### ETCSLevel NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 ETCSLevel 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ETCSLevel:id:BGAN:05745799",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-02-19T06:53:45Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2006-04-03T21:41:04Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Team writer probably position. Him blue successful media sh"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Unit feel there spring method shoulder general main. Note close and many size price simple."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Position check Ameri"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Idea player within operation area reveal floor energy. Somebody reach technology lay whole trouble."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Amount over our begin image suggest. Machine notice worry treatment deal hotel place mouth. Include party speci"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:ETCSLevel:items:LIXQ:14931750",  
      "urn:ngsi-ld:ETCSLevel:items:RAAU:17602742"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:ETCSLevel:items:DBRI:43078251"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -84.091295,  
        74.323743  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Central water activity su",  
      "addressLocality": "Herself wife wish degree. He chair better tough see sign get think",  
      "addressRegion": "Television staff morning word century quite theory away. Structure conference good account letter star. Mouth course unit difficult response.",  
      "addressCountry": "Its trial provide clear probably. Within resource identify attorney. Perform require area le",  
      "postalCode": "Security country hear character company people. Hear from agency fine case agent religious watch. None cup begin.",  
      "postOfficeBoxNumber": "Big serve only offer. Film red center. Area two wrong.",  
      "streetNr": "Fly improve",  
      "district": "Instead little back should political according. Around pull thing model executive school accept every."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Protect too alone give assume parent character. Attention land political fear good allow. Town part easy various."  
  },  
  "type": "ETCSLevel",  
  "etcsBaseline": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ETCSLevel:etcsBaseline:COZU:74311343"  
  },  
  "etcsLevelType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ETCSLevel:etcsLevelType:DFOI:51546732"  
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

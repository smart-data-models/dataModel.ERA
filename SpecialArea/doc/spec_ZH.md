<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：特殊区域  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/SpecialArea/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**包括所有区域或部分，如安全区、限制区（非停工区或工业风险地点）。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `specialAreaType[uri]`: 特殊区域类型  - `type[string]`: NGSI 数据类型。必须是 SpecialArea  <!-- /30-PropertiesList -->  
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
SpecialArea:    
  description: 'Encompasses all those areas or sections such as safe areas, restricted areas (non-stopping areas or industrial risk locations).'    
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
    specialAreaType:    
      description: Special area type    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI data type. It has to be SpecialArea    
      enum:    
        - SpecialArea    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/SpecialArea    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SpecialArea/LICENSE.md    
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
#### 特殊区域 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 SpecialArea 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:LPYR:16529675",  
  "dateCreated": "1992-05-24T05:59:05Z",  
  "dateModified": "1997-01-09T06:38:30Z",  
  "source": "Federal tough Republican popular any. Society he",  
  "name": "Rule discuss business guess picture. Another stuff new five affect artist instead. Yard test remember smile dem",  
  "alternateName": "Field ball any out authority last set. Charge moment Mrs.",  
  "description": "Piece or sell far time then. Focus deal through her marriage some.",  
  "dataProvider": "National worker admit speak interview day. Person hit behind property.",  
  "owner": [  
    "urn:ngsi-ld:SpecialArea:items:OTDU:99373788",  
    "urn:ngsi-ld:SpecialArea:items:LJSH:77643420"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialArea:items:YBMA:89347369"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      22.340017,  
      19.489173  
    ]  
  },  
  "address": {  
    "streetAddress": "Stay I draw painting sometimes chance. Teacher where quality before commercial property.",  
    "addressLocality": "Exactly question left writer eye. Movie land rich another knowledge mu",  
    "addressRegion": "Good over fish perform. Training lead fund true middle force use. Chair along drop that maintain. ",  
    "addressCountry": "Car easy budget their goal along. Against late alone foot hard differen",  
    "postalCode": "Nor various glass why result spee",  
    "postOfficeBoxNumber": "Half reduce ahead on from quite movement. Movie offer enough type. Name organization apply he hotel.",  
    "streetNr": "No entire boy pick imagine another. Describe purpose president third piece none prepare.",  
    "district": "Traditional development argue hundred. Friend usually after among class put."  
  },  
  "areaServed": "City teacher standard court l",  
  "type": "SpecialArea",  
  "specialAreaType": "urn:ngsi-ld:SpecialArea:specialAreaType:KUMC:59668635"  
}  
```  
</details>  
#### 特殊区域 NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 SpecialArea 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:LPYR:16529675",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1992-05-24T05:59:05Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1997-01-09T06:38:30Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Federal tough Republican popular any. Society he"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Rule discuss business guess picture. Another stuff new five affect artist instead. Yard test remember smile dem"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Field ball any out authority last set. Charge moment Mrs."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Piece or sell far time then. Focus deal through her marriage some."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "National worker admit speak interview day. Person hit behind property."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:OTDU:99373788",  
      "urn:ngsi-ld:SpecialArea:items:LJSH:77643420"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:YBMA:89347369"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          22.340017,  
          19.489173  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Stay I draw painting sometimes chance. Teacher where quality before commercial property."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Exactly question left writer eye. Movie land rich another knowledge mu"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Good over fish perform. Training lead fund true middle force use. Chair along drop that maintain. "  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Car easy budget their goal along. Against late alone foot hard differen"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Nor various glass why result spee"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Half reduce ahead on from quite movement. Movie offer enough type. Name organization apply he hotel."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "No entire boy pick imagine another. Describe purpose president third piece none prepare."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Traditional development argue hundred. Friend usually after among class put."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "City teacher standard court l"  
  },  
  "type": "SpecialArea",  
  "specialAreaType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SpecialArea:specialAreaType:KUMC:59668635"  
  }  
}  
```  
</details>  
#### 特殊区域 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 SpecialArea 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:LPYR:16529675",  
  "dateCreated": "1992-05-24T05:59:05Z",  
  "dateModified": "1997-01-09T06:38:30Z",  
  "source": "Federal tough Republican popular any. Society he",  
  "name": "Rule discuss business guess picture. Another stuff new five affect artist instead. Yard test remember smile dem",  
  "alternateName": "Field ball any out authority last set. Charge moment Mrs.",  
  "description": "Piece or sell far time then. Focus deal through her marriage some.",  
  "dataProvider": "National worker admit speak interview day. Person hit behind property.",  
  "owner": [  
    "urn:ngsi-ld:SpecialArea:items:OTDU:99373788",  
    "urn:ngsi-ld:SpecialArea:items:LJSH:77643420"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialArea:items:YBMA:89347369"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      22.340017,  
      19.489173  
    ]  
  },  
  "address": {  
    "streetAddress": "Stay I draw painting sometimes chance. Teacher where quality before commercial property.",  
    "addressLocality": "Exactly question left writer eye. Movie land rich another knowledge mu",  
    "addressRegion": "Good over fish perform. Training lead fund true middle force use. Chair along drop that maintain. ",  
    "addressCountry": "Car easy budget their goal along. Against late alone foot hard differen",  
    "postalCode": "Nor various glass why result spee",  
    "postOfficeBoxNumber": "Half reduce ahead on from quite movement. Movie offer enough type. Name organization apply he hotel.",  
    "streetNr": "No entire boy pick imagine another. Describe purpose president third piece none prepare.",  
    "district": "Traditional development argue hundred. Friend usually after among class put."  
  },  
  "areaServed": "City teacher standard court l",  
  "type": "SpecialArea",  
  "specialAreaType": "urn:ngsi-ld:SpecialArea:specialAreaType:KUMC:59668635",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### 特殊区域 NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 SpecialArea 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:BXVG:20578065",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-07-13T20:29:53Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1996-03-16T13:18:03Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Work it low government."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Vote upon star show occur. Meeting technology half marriage role number."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Concern threat require Mr suggest benefit. Short run home hard forward."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Environment economy scene se"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Bar teach middle mean born. Skill have person window media man. Run court treatment eat second."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:AFRV:18308441",  
      "urn:ngsi-ld:SpecialArea:items:MUMA:06460118"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:YBKX:99238445"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -44.9842385,  
        -63.929183  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Everything how similar",  
      "addressLocality": "Serious off dog record call somebody. C",  
      "addressRegion": "Resource threat scientist candidate specific realize. Education event population he behavior. Other white member chair image.",  
      "addressCountry": "Professor near behind of will little. Pattern agent nothing arm message say he. Size doctor thing me benefit.",  
      "postalCode": "Standard for same agreement foot wind government. Now project citizen within course trial. Country role report wear indicate customer him simply. Trial smile want marriage m",  
      "postOfficeBoxNumber": "Statement court method chance street develop sound.",  
      "streetNr": "Interest she rather media reality attack. Seat service professor.",  
      "district": "Focus "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Grow same something good. Still go small move fall international mean."  
  },  
  "type": "SpecialArea",  
  "specialAreaType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SpecialArea:specialAreaType:VEIZ:54748811"  
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

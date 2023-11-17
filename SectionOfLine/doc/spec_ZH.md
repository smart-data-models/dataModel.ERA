<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：线段    
=====<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/SectionOfLine/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**线路区段是指相邻运行点之间的线路部分，可能由多条轨道组成。    
在 https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.1 线路区段中**。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `lineNationalId[uri]`: 国家线路识别  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `opEnd[uri]`: 线路末段的运行点  - `opStart[uri]`: 线路起点运行点  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `solNature[uri]`: 线段性质  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `track[uri]`: 轨道  - `type[string]`: NGSI 数据类型。必须是 SectionOfLine  <!-- /30-PropertiesList -->    
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
SectionOfLine:      
  description: |-      
    A section of line means the part of line between adjacent operational points and may consist of several tracks.      
    In https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.1 Line sections.      
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
    lineNationalId:      
      description: National line identification      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    opEnd:      
      description: Operational Point at end of Section of Line      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    opStart:      
      description: Operational Point at start of Section of Line      
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
    solNature:      
      description: Nature of Section of Line      
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
      description: NGSI data type. It has to be SectionOfLine      
      enum:      
        - SectionOfLine      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/SectionOfLine      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SectionOfLine/LICENSE.md      
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
#### SectionOfLine NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 SectionOfLine 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:NVYV:48459502",  
  "dateCreated": "2019-05-29T20:37:27Z",  
  "dateModified": "1990-02-07T09:13:17Z",  
  "source": "Someone perform protect too even. Into",  
  "name": "Should reduce admit door you. Entire tonight hold cultural answer your. That indicate stock r",  
  "alternateName": "Herself teacher rather inside me. A our read. Police phone data ahead.",  
  "description": "Return conference five know",  
  "dataProvider": "Low light peace home. Tend base report admit.",  
  "owner": [  
    "urn:ngsi-ld:SectionOfLine:items:QUNL:25640251",  
    "urn:ngsi-ld:SectionOfLine:items:TUBX:09855374"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SectionOfLine:items:BNLE:70988625"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -49.248493,  
      -99.418946  
    ]  
  },  
  "address": {  
    "streetAddress": "Consider affect seven difference impact or. Carry sport identify magazine listen science ",  
    "addressLocality": "Phone quality top current. Range until big suggest both focus.",  
    "addressRegion": "Light through th",  
    "addressCountry": "Ready pay for presen",  
    "postalCode": "Purpose feel son current mission address. Future although everyone affect.",  
    "postOfficeBoxNumber": "Point road player personal around rich cut. If try raise meet process.",  
    "streetNr": "Somebody lawyer production often nearly news. Material he front.",  
    "district": "Stage especially site list writer. Political pr"  
  },  
  "areaServed": "Finally star wonder ask us. Family focus tell sing goal today them voice. Together story west or official.",  
  "type": "SectionOfLine",  
  "lineNationalId": "urn:ngsi-ld:SectionOfLine:lineNationalId:ISBE:85077227",  
  "opEnd": "urn:ngsi-ld:SectionOfLine:opEnd:MIJK:54736457",  
  "opStart": "urn:ngsi-ld:SectionOfLine:opStart:QOPP:74078654",  
  "solNature": "urn:ngsi-ld:SectionOfLine:solNature:UWFX:27604875",  
  "track": "urn:ngsi-ld:SectionOfLine:track:RKTG:26142248",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SectionOfLine NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的 SectionOfLine 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:NVYV:48459502",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2019-05-29T20:37:27Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1990-02-07T09:13:17Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Someone perform protect too even. Into"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Should reduce admit door you. Entire tonight hold cultural answer your. That indicate stock r"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Herself teacher rather inside me. A our read. Police phone data ahead."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Return conference five know"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Low light peace home. Tend base report admit."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:QUNL:25640251",  
      "urn:ngsi-ld:SectionOfLine:items:TUBX:09855374"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:BNLE:70988625"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -49.248493,  
        -99.418946  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Consider affect seven difference impact or. Carry sport identify magazine listen science ",  
      "addressLocality": "Phone quality top current. Range until big suggest both focus.",  
      "addressRegion": "Light through th",  
      "addressCountry": "Ready pay for presen",  
      "postalCode": "Purpose feel son current mission address. Future although everyone affect.",  
      "postOfficeBoxNumber": "Point road player personal around rich cut. If try raise meet process.",  
      "streetNr": "Somebody lawyer production often nearly news. Material he front.",  
      "district": "Stage especially site list writer. Political pr"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Finally star wonder ask us. Family focus tell sing goal today them voice. Together story west or official."  
  },  
  "type": "SectionOfLine",  
  "lineNationalId": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:lineNationalId:ISBE:85077227"  
  },  
  "opEnd": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:opEnd:MIJK:54736457"  
  },  
  "opStart": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:opStart:QOPP:74078654"  
  },  
  "solNature": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:solNature:UWFX:27604875"  
  },  
  "track": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:track:RKTG:26142248"  
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
#### SectionOfLine NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 SectionOfLine 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:NVYV:48459502",  
  "dateCreated": "2019-05-29T20:37:27Z",  
  "dateModified": "1990-02-07T09:13:17Z",  
  "source": "Someone perform protect too even. Into",  
  "name": "Should reduce admit door you. Entire tonight hold cultural answer your. That indicate stock r",  
  "alternateName": "Herself teacher rather inside me. A our read. Police phone data ahead.",  
  "description": "Return conference five know",  
  "dataProvider": "Low light peace home. Tend base report admit.",  
  "owner": [  
    "urn:ngsi-ld:SectionOfLine:items:QUNL:25640251",  
    "urn:ngsi-ld:SectionOfLine:items:TUBX:09855374"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SectionOfLine:items:BNLE:70988625"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -49.248493,  
      -99.418946  
    ]  
  },  
  "address": {  
    "streetAddress": "Consider affect seven difference impact or. Carry sport identify magazine listen science ",  
    "addressLocality": "Phone quality top current. Range until big suggest both focus.",  
    "addressRegion": "Light through th",  
    "addressCountry": "Ready pay for presen",  
    "postalCode": "Purpose feel son current mission address. Future although everyone affect.",  
    "postOfficeBoxNumber": "Point road player personal around rich cut. If try raise meet process.",  
    "streetNr": "Somebody lawyer production often nearly news. Material he front.",  
    "district": "Stage especially site list writer. Political pr"  
  },  
  "areaServed": "Finally star wonder ask us. Family focus tell sing goal today them voice. Together story west or official.",  
  "type": "SectionOfLine",  
  "lineNationalId": "urn:ngsi-ld:SectionOfLine:lineNationalId:ISBE:85077227",  
  "opEnd": "urn:ngsi-ld:SectionOfLine:opEnd:MIJK:54736457",  
  "opStart": "urn:ngsi-ld:SectionOfLine:opStart:QOPP:74078654",  
  "solNature": "urn:ngsi-ld:SectionOfLine:solNature:UWFX:27604875",  
  "track": "urn:ngsi-ld:SectionOfLine:track:RKTG:26142248",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SectionOfLine NGSI-LD 标准化示例    
下面是一个以 JSON-LD 格式规范化的 SectionOfLine 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:BHSJ:12081625",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2002-06-30T22:12:57Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-07-14T14:37:10Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Travel last avoid across clearly. Listen sign tough police product that."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Painting spend near music activity. That parent item. Despite within instead per cost network. Most argue civil w"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Wait go enough truth player itself. Realize military region fight student hel"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Notice note word ground. Dream conference father co"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Run nor scene growth long."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:PAQY:12003815",  
      "urn:ngsi-ld:SectionOfLine:items:ZNNC:60809737"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:YLLU:61619520"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        87.630235,  
        -145.984526  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Important national determine issue forget. Charge he",  
      "addressLocality": "Part plant learn interview. Always site also within return such. Head food audience cut town office vote across. Mil",  
      "addressRegion": "Know big act. Development series cours",  
      "addressCountry": "Successful Mrs home great issue again education degree. Main myself treatment might. Minute amount central.",  
      "postalCode": "A give claim what throw which. Final front dinner. Rich space fire sister maybe support.",  
      "postOfficeBoxNumber": "Effort prepare seem class collection. Husband task your name some gas control. Own ha",  
      "streetNr": "Eye current positive myself trial change worker. Sure show attorney ",  
      "district": "Expect subject edg"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Apply environmental necessary address trip worry."  
  },  
  "type": "SectionOfLine",  
  "lineNationalId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:lineNationalId:WWXI:47713875"  
  },  
  "opEnd": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:opEnd:ESDA:92317943"  
  },  
  "opStart": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:opStart:EXYH:90955448"  
  },  
  "solNature": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:solNature:UBAH:75574617"  
  },  
  "track": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:track:ZVJB:17662025"  
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

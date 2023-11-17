<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：操作点    
======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/OperationalPoint/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全球描述：**运营点（OP）是指列车服务运营的任何地点，列车服务可在此开始和结束或改变路线，也可在此提供客运或货运服务；运营点还指成员国或基础设施管理者之间边界的任何地点。    
在 https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.2 主要地点（车站、货场、枢纽站、货运站）**。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `borderPointOf[uri]`: 的边界点  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `digitalSchematicOverview[string]`: 数字原理图概览  - `hasSchematicOverviewOPDigitalForm[boolean]`: 具有数字形式的原理图概览  - `id[*]`: 实体的唯一标识符  - `localRulesOrRestrictions[boolean]`: 存在严格的地方性规则和限制。  - `localRulesOrRestrictionsDoc[string]`: IM 提供的有关严格意义上的地方性规则或限制的文件  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `opInfoPerCountry[uri]`: 每个国家的边境点信息  - `opName[string]`: 运行点名称  - `opType[uri]`: 操作点类型  - `opTypeGaugeChangeover[string]`: 轨距转换设施类型  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `schematicOverviewOP[string]`: 操作点示意图  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `siding[uri]`: 护墙板  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `tafTAPCode[string]`: 根据与远程信息处理应用相关的 TSI 制定的用于信息交换的主要位置代码。  - `track[uri]`: 轨道  - `type[string]`: NGSI 数据类型。必须是 OperationalPoint  - `uopid[string]`: 独特的 OP ID  <!-- /30-PropertiesList -->    
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
OperationalPoint:      
  description: |-      
    An operational point (OP) means any location for train service operations, where train services may begin and end or change route, and where passenger or freight services may be provided; operational point also means any location at boundaries between Member States or infrastructure managers.      
    In https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.2 Principal locations (stations, yards, junctions, freight terminals).      
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
    borderPointOf:      
      description: Border point of      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    digitalSchematicOverview:      
      description: Digital schematic overview      
      type: string      
      x-ngsi:      
        type: Property      
    hasSchematicOverviewOPDigitalForm:      
      description: Has schematic overview in digital form      
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
    localRulesOrRestrictions:      
      description: Existence of rules and restrictions of a strictly local nature.      
      type: boolean      
      x-ngsi:      
        type: Property      
    localRulesOrRestrictionsDoc:      
      description: Documents regarding the rules or restrictions of a strictly local nature available by the IM      
      type: string      
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
    opInfoPerCountry:      
      description: Border point information per country      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    opName:      
      description: Name of Operational point      
      type: string      
      x-ngsi:      
        type: Property      
    opType:      
      description: Type of operational point      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    opTypeGaugeChangeover:      
      description: Type of track gauge changeover facility      
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
    schematicOverviewOP:      
      description: Schematic overview of the operational point      
      type: string      
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
    siding:      
      description: Siding      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    tafTAPCode:      
      description: Primary location code developed for information exchange in accordance with the TSIs relating to telematics applications.      
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
      description: NGSI data type. It has to be OperationalPoint      
      enum:      
        - OperationalPoint      
      type: string      
      x-ngsi:      
        type: Property      
    uopid:      
      description: Unique OP ID      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/OperationalPoint      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/OperationalPoint/LICENSE.md      
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
#### OperationalPoint NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 OperationalPoint 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationalPoint:id:IOTD:74551353",  
  "dateCreated": "2005-06-20T07:48:08Z",  
  "dateModified": "1999-04-03T20:20:59Z",  
  "source": "Quite kind treatment situation usually onto. Town everybody sing w",  
  "name": "Foot oil author store ok white. Recent talk much garden eat. Class early so especially open matter first.",  
  "alternateName": "Notice free listen position. Again special understand laugh class. Lot involve worry drug house.",  
  "description": "Lead conference ground civil image not our. Follow heart system why return continue drive.",  
  "dataProvider": "Data rise once authority black training old. North conference off rate. News them te",  
  "owner": [  
    "urn:ngsi-ld:OperationalPoint:items:GHDZ:21768966",  
    "urn:ngsi-ld:OperationalPoint:items:PTHR:22118083"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OperationalPoint:items:ARYU:60588140"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -87.0756655,  
      -98.077607  
    ]  
  },  
  "address": {  
    "streetAddress": "Recently southern war measure. Behind collection relationship something. Join blue expert should happy according deal.",  
    "addressLocality": "Community sit about space need win man. Prevent place we whatever image stock.",  
    "addressRegion": "Into his give degree however.",  
    "addressCountry": "Identify couple five deep bar popular product not. Design sell security trip never adult heart course.",  
    "postalCode": "Product five yourself open. Purpose decade ",  
    "postOfficeBoxNumber": "Involve argue cup subject arm bab",  
    "streetNr": "Fish share ",  
    "district": "Speech customer perhaps ball defense attorney. Pattern indeed bank result hear. Society different open health. Back reduce his know green next produce."  
  },  
  "areaServed": "Character stuff TV.",  
  "type": "OperationalPoint",  
  "digitalSchematicOverview": "Development growth guy contain race practice your. Try where where newspaper.",  
  "hasSchematicOverviewOPDigitalForm": false,  
  "localRulesOrRestrictions": true,  
  "localRulesOrRestrictionsDoc": "Conce",  
  "opName": "Image protect pay until by science he me. Employee scientist couple though center Democrat. Actually pull friend seem.",  
  "opTypeGaugeChangeover": "Arrive box since rise condition quality. Dinner major range certainly. Do rest main or part wife.",  
  "schematicOverviewOP": "Culture still last prove skin. Brother y",  
  "tafTAPCode": "Among sometimes security show environment as. Article save training chance bring performance eight.",  
  "uopid": "Physical practice picture dinner site. While huge miss. Center lawyer ball before loca",  
  "borderPointOf": "urn:ngsi-ld:OperationalPoint:borderPointOf:UIZL:70889589",  
  "opInfoPerCountry": "urn:ngsi-ld:OperationalPoint:opInfoPerCountry:WTMZ:27677089",  
  "opType": "urn:ngsi-ld:OperationalPoint:opType:PHWE:53327313",  
  "siding": "urn:ngsi-ld:OperationalPoint:siding:DTBZ:41746823",  
  "track": "urn:ngsi-ld:OperationalPoint:track:NRVQ:66885969"  
}  
```  
</details>    
#### OperationalPoint NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式 OperationalPoint 的示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationalPoint:id:IOTD:74551353",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2005-06-20T07:48:08Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1999-04-03T20:20:59Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Quite kind treatment situation usually onto. Town everybody sing w"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Foot oil author store ok white. Recent talk much garden eat. Class early so especially open matter first."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Notice free listen position. Again special understand laugh class. Lot involve worry drug house."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Lead conference ground civil image not our. Follow heart system why return continue drive."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Data rise once authority black training old. North conference off rate. News them te"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:OperationalPoint:items:GHDZ:21768966",  
      "urn:ngsi-ld:OperationalPoint:items:PTHR:22118083"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:OperationalPoint:items:ARYU:60588140"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -87.0756655,  
        -98.077607  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Recently southern war measure. Behind collection relationship something. Join blue expert should happy according deal.",  
      "addressLocality": "Community sit about space need win man. Prevent place we whatever image stock.",  
      "addressRegion": "Into his give degree however.",  
      "addressCountry": "Identify couple five deep bar popular product not. Design sell security trip never adult heart course.",  
      "postalCode": "Product five yourself open. Purpose decade ",  
      "postOfficeBoxNumber": "Involve argue cup subject arm bab",  
      "streetNr": "Fish share ",  
      "district": "Speech customer perhaps ball defense attorney. Pattern indeed bank result hear. Society different open health. Back reduce his know green next produce."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Character stuff TV."  
  },  
  "type": "OperationalPoint",  
  "digitalSchematicOverview": {  
    "type": "Text",  
    "value": "Development growth guy contain race practice your. Try where where newspaper."  
  },  
  "hasSchematicOverviewOPDigitalForm": {  
    "type": "Boolean",  
    "value": false  
  },  
  "localRulesOrRestrictions": {  
    "type": "Boolean",  
    "value": true  
  },  
  "localRulesOrRestrictionsDoc": {  
    "type": "Text",  
    "value": "Conce"  
  },  
  "opName": {  
    "type": "Text",  
    "value": "Image protect pay until by science he me. Employee scientist couple though center Democrat. Actually pull friend seem."  
  },  
  "opTypeGaugeChangeover": {  
    "type": "Text",  
    "value": "Arrive box since rise condition quality. Dinner major range certainly. Do rest main or part wife."  
  },  
  "schematicOverviewOP": {  
    "type": "Text",  
    "value": "Culture still last prove skin. Brother y"  
  },  
  "tafTAPCode": {  
    "type": "Text",  
    "value": "Among sometimes security show environment as. Article save training chance bring performance eight."  
  },  
  "uopid": {  
    "type": "Text",  
    "value": "Physical practice picture dinner site. While huge miss. Center lawyer ball before loca"  
  },  
  "borderPointOf": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OperationalPoint:borderPointOf:UIZL:70889589"  
  },  
  "opInfoPerCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OperationalPoint:opInfoPerCountry:WTMZ:27677089"  
  },  
  "opType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OperationalPoint:opType:PHWE:53327313"  
  },  
  "siding": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OperationalPoint:siding:DTBZ:41746823"  
  },  
  "track": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:OperationalPoint:track:NRVQ:66885969"  
  }  
}  
```  
</details>    
#### OperationalPoint NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 OperationalPoint 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationalPoint:id:IOTD:74551353",  
  "dateCreated": "2005-06-20T07:48:08Z",  
  "dateModified": "1999-04-03T20:20:59Z",  
  "source": "Quite kind treatment situation usually onto. Town everybody sing w",  
  "name": "Foot oil author store ok white. Recent talk much garden eat. Class early so especially open matter first.",  
  "alternateName": "Notice free listen position. Again special understand laugh class. Lot involve worry drug house.",  
  "description": "Lead conference ground civil image not our. Follow heart system why return continue drive.",  
  "dataProvider": "Data rise once authority black training old. North conference off rate. News them te",  
  "owner": [  
    "urn:ngsi-ld:OperationalPoint:items:GHDZ:21768966",  
    "urn:ngsi-ld:OperationalPoint:items:PTHR:22118083"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:OperationalPoint:items:ARYU:60588140"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -87.0756655,  
      -98.077607  
    ]  
  },  
  "address": {  
    "streetAddress": "Recently southern war measure. Behind collection relationship something. Join blue expert should happy according deal.",  
    "addressLocality": "Community sit about space need win man. Prevent place we whatever image stock.",  
    "addressRegion": "Into his give degree however.",  
    "addressCountry": "Identify couple five deep bar popular product not. Design sell security trip never adult heart course.",  
    "postalCode": "Product five yourself open. Purpose decade ",  
    "postOfficeBoxNumber": "Involve argue cup subject arm bab",  
    "streetNr": "Fish share ",  
    "district": "Speech customer perhaps ball defense attorney. Pattern indeed bank result hear. Society different open health. Back reduce his know green next produce."  
  },  
  "areaServed": "Character stuff TV.",  
  "type": "OperationalPoint",  
  "digitalSchematicOverview": "Development growth guy contain race practice your. Try where where newspaper.",  
  "hasSchematicOverviewOPDigitalForm": false,  
  "localRulesOrRestrictions": true,  
  "localRulesOrRestrictionsDoc": "Conce",  
  "opName": "Image protect pay until by science he me. Employee scientist couple though center Democrat. Actually pull friend seem.",  
  "opTypeGaugeChangeover": "Arrive box since rise condition quality. Dinner major range certainly. Do rest main or part wife.",  
  "schematicOverviewOP": "Culture still last prove skin. Brother y",  
  "tafTAPCode": "Among sometimes security show environment as. Article save training chance bring performance eight.",  
  "uopid": "Physical practice picture dinner site. While huge miss. Center lawyer ball before loca",  
  "borderPointOf": "urn:ngsi-ld:OperationalPoint:borderPointOf:UIZL:70889589",  
  "opInfoPerCountry": "urn:ngsi-ld:OperationalPoint:opInfoPerCountry:WTMZ:27677089",  
  "opType": "urn:ngsi-ld:OperationalPoint:opType:PHWE:53327313",  
  "siding": "urn:ngsi-ld:OperationalPoint:siding:DTBZ:41746823",  
  "track": "urn:ngsi-ld:OperationalPoint:track:NRVQ:66885969",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 操作点 NGSI-LD 标准化示例    
下面是一个规范化 JSON-LD 格式 OperationalPoint 的示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationalPoint:id:XZFT:49427654",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1970-09-09T19:08:29Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1994-02-06T15:17:27Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Describe help hope I finish ago rate. Impact indicate health resource join maybe career. Tell wish development political lot nearly."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Want know nature store ever shoulder. Husband my cut all. Arm store can when course."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Represent country trouble discuss central large. Onto medical bad fin"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Customer strateg"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Else back sing interest prove girl window cold. Character wide son customer."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OperationalPoint:items:RVZL:45994288",  
      "urn:ngsi-ld:OperationalPoint:items:XLVF:68990583"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:OperationalPoint:items:ICGN:37896114"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        31.5220295,  
        16.017292  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Person simply stage simply power. Price great image affect card certainly. Official body indicate similar look no history bill. Head now yeah son.",  
      "addressLocality": "Learn employee although do mean campaign enjoy. Example only fill. Admit law determine next.",  
      "addressRegion": "Down both or current. Air time grow career ever effect. Too let argue note until money.",  
      "addressCountry": "Fill expert window. Subject entire future. Score war too fire back star still. Clear science good story.",  
      "postalCode": "Market nothing international can to responsibility. Recent attack international year movement democratic provide.",  
      "postOfficeBoxNumber": "Include call assume two see. Ground painting among. Until",  
      "streetNr": "Build factor when type official source western. Pretty child side fly. Compare somebody girl ",  
      "district": "Environmenta"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Development foreign your start try if"  
  },  
  "type": "OperationalPoint",  
  "digitalSchematicOverview": {  
    "type": "Property",  
    "value": "Try somebody term."  
  },  
  "hasSchematicOverviewOPDigitalForm": {  
    "type": "Property",  
    "value": true  
  },  
  "localRulesOrRestrictions": {  
    "type": "Property",  
    "value": true  
  },  
  "localRulesOrRestrictionsDoc": {  
    "type": "Property",  
    "value": "Road others raise first pay. Pra"  
  },  
  "opName": {  
    "type": "Property",  
    "value": "Theory market enough similar push chair become. Opportunity woman "  
  },  
  "opTypeGaugeChangeover": {  
    "type": "Property",  
    "value": "Themselves fact but discuss shake. Physical position recognize onto."  
  },  
  "schematicOverviewOP": {  
    "type": "Property",  
    "value": "Tree final assume trade reach technology. Rock name degree professional stuff. Fly difficult use majo"  
  },  
  "tafTAPCode": {  
    "type": "Property",  
    "value": "Sea read nice start design sense author thank. Able d"  
  },  
  "uopid": {  
    "type": "Property",  
    "value": "Evidence road social politics responsibility. And various space law. Street black decide serious both."  
  },  
  "borderPointOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OperationalPoint:borderPointOf:CNYT:41694123"  
  },  
  "opInfoPerCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OperationalPoint:opInfoPerCountry:GDQX:09330981"  
  },  
  "opType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OperationalPoint:opType:AHNK:46903244"  
  },  
  "siding": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OperationalPoint:siding:JGGJ:46317226"  
  },  
  "track": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:OperationalPoint:track:CMLZ:48730152"  
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

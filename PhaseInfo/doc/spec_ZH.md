<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：阶段信息    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/PhaseInfo/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**说明所需的有关相分离的若干信息。    
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `phaseInfoKm[number]`: 阶段信息 公里  - `phaseInfoLength[number]`: 相位信息长度  - `phaseInfoPantographLowered[boolean]`: 降低相位信息受电弓  - `phaseInfoSwitchOffBreaker[boolean]`: 相位信息 关闭断路器  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `systemSeparationInfoKm[number]`: 系统分隔信息 千米  - `type[string]`: NGSI 数据类型。它必须是 PhaseInfo  <!-- /30-PropertiesList -->    
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
PhaseInfo:      
  description: Indication of required several information on phase separation.      
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
    phaseInfoKm:      
      description: Phase info Km      
      type: number      
      x-ngsi:      
        type: Property      
    phaseInfoLength:      
      description: Phase info length      
      type: number      
      x-ngsi:      
        type: Property      
    phaseInfoPantographLowered:      
      description: Phase info pantograph lowered      
      type: boolean      
      x-ngsi:      
        type: Property      
    phaseInfoSwitchOffBreaker:      
      description: Phase info switch off breaker      
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
    systemSeparationInfoKm:      
      description: System separation info Km      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be PhaseInfo      
      enum:      
        - PhaseInfo      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/PhaseInfo      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/PhaseInfo/LICENSE.md      
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
#### PhaseInfo NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 PhaseInfo 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": "2004-07-16T13:48:20Z",  
  "dateModified": "1991-11-29T03:06:21Z",  
  "source": "Enjoy will style car seem recent. Plan theory u",  
  "name": "Rate office focus whole on produce. Argue Mrs care accept momen",  
  "alternateName": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman.",  
  "description": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense.",  
  "dataProvider": "All owner type finish more race adult.",  
  "owner": [  
    "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
    "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      79.5846865,  
      60.386195  
    ]  
  },  
  "address": {  
    "streetAddress": "Toward idea thought. Among drop position election wear.",  
    "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
    "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
    "addressCountry": "Analysis argue so performance itself really for.",  
    "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
    "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
    "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
    "district": "Return anything ma"  
  },  
  "areaServed": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress.",  
  "type": "PhaseInfo",  
  "phaseInfoKm": 37.5,  
  "phaseInfoLength": 864,  
  "phaseInfoPantographLowered": false,  
  "phaseInfoSwitchOffBreaker": false,  
  "systemSeparationInfoKm": 99.4  
}  
```  
</details>    
#### PhaseInfo NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式的 PhaseInfo 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2004-07-16T13:48:20Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1991-11-29T03:06:21Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Enjoy will style car seem recent. Plan theory u"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Rate office focus whole on produce. Argue Mrs care accept momen"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "All owner type finish more race adult."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
      "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        79.5846865,  
        60.386195  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Toward idea thought. Among drop position election wear.",  
      "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
      "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
      "addressCountry": "Analysis argue so performance itself really for.",  
      "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
      "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
      "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
      "district": "Return anything ma"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress."  
  },  
  "type": "PhaseInfo",  
  "phaseInfoKm": {  
    "type": "Number",  
    "value": 37.5  
  },  
  "phaseInfoLength": {  
    "type": "Number",  
    "value": 864  
  },  
  "phaseInfoPantographLowered": {  
    "type": "Boolean",  
    "value": false  
  },  
  "phaseInfoSwitchOffBreaker": {  
    "type": "Boolean",  
    "value": false  
  },  
  "systemSeparationInfoKm": {  
    "type": "Number",  
    "value": 99.4  
  }  
}  
```  
</details>    
#### PhaseInfo NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 PhaseInfo 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": "2004-07-16T13:48:20Z",  
  "dateModified": "1991-11-29T03:06:21Z",  
  "source": "Enjoy will style car seem recent. Plan theory u",  
  "name": "Rate office focus whole on produce. Argue Mrs care accept momen",  
  "alternateName": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman.",  
  "description": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense.",  
  "dataProvider": "All owner type finish more race adult.",  
  "owner": [  
    "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
    "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      79.5846865,  
      60.386195  
    ]  
  },  
  "address": {  
    "streetAddress": "Toward idea thought. Among drop position election wear.",  
    "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
    "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
    "addressCountry": "Analysis argue so performance itself really for.",  
    "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
    "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
    "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
    "district": "Return anything ma"  
  },  
  "areaServed": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress.",  
  "type": "PhaseInfo",  
  "phaseInfoKm": 37.5,  
  "phaseInfoLength": 864,  
  "phaseInfoPantographLowered": false,  
  "phaseInfoSwitchOffBreaker": false,  
  "systemSeparationInfoKm": 99.4,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### PhaseInfo NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 PhaseInfo 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:MKUJ:15010698",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1980-01-19T22:02:09Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2008-03-14T12:40:50Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Across air language thoug"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Capital wife fast make similar memory first. Face best choose"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Forward arm back. Sell draw treat water mind series. Movement level ago real study."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Book maybe social but reflect traditional standard"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Office late American morning west economic he. Wide wide rule. Arrive four with measure edge policy."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:ZJGM:93382933",  
      "urn:ngsi-ld:PhaseInfo:items:VXVX:69604579"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:MJIU:47652604"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -83.0057365,  
        76.5777  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Own organization seat everyone. Animal offer indeed send environmental outside.",  
      "addressLocality": "Drop hear pull on remember drop top. Experience once heart word nearly. Every a significant size.",  
      "addressRegion": "Watch cold letter student information. Professor knowledge four meeting customer. Stock point on student tend. Born glass effort someone.",  
      "addressCountry": "Congress dog probably buy time. Product style sport amount clearly than.",  
      "postalCode": "Dr",  
      "postOfficeBoxNumber": "Good agency tend happen dark option. Individual different former then ago month environment single.",  
      "streetNr": "Arrive including smile concern head effort economic. Top pick appear treat. Hour th",  
      "district": "Message movie former mean rather. Health serious base boy action picture. Rate high pay get risk security someone image."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Agency great travel kitchen. Travel certain improve official meet answer concern. Remember specific red."  
  },  
  "type": "PhaseInfo",  
  "phaseInfoKm": {  
    "type": "Property",  
    "value": 187.2  
  },  
  "phaseInfoLength": {  
    "type": "Property",  
    "value": 335  
  },  
  "phaseInfoPantographLowered": {  
    "type": "Property",  
    "value": true  
  },  
  "phaseInfoSwitchOffBreaker": {  
    "type": "Property",  
    "value": true  
  },  
  "systemSeparationInfoKm": {  
    "type": "Property",  
    "value": 198.4  
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

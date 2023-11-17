<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 인증서    
========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/Certificate/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `state[uri]`: 상태  - `type[string]`: NGSI 데이터 유형입니다. 인증서여야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
ERA 온톨로지에서 매핑된 데이터 모델 https://data-interop.era.europa.eu/era-vocabulary(유럽 연합 철도청)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Certificate:      
  description: ""      
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
    state:      
      description: State      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    type:      
      description: NGSI data type. It has to be Certificate      
      enum:      
        - Certificate      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/Certificate      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Certificate/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json      
  x-model-tags: 'ERA vocabulary, railway, train'      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### 인증서 NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 인증서 예제입니다. 이것은 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:OEMR:38840161",  
  "dateCreated": "2000-01-17T20:24:29Z",  
  "dateModified": "2014-02-03T22:13:34Z",  
  "source": "Strategy there certainly federal. Risk manager carry shoulder only long.",  
  "name": "Across him eight property help. Beat federal dream conference score special deal accept.",  
  "alternateName": "Heart beat fine nice identify. Wide usually me in painting tough entire.",  
  "description": "Section employee few. Decision prevent easy.",  
  "dataProvider": "Talk necessary run score recent. Expert seem money concern shoulder goal. Recognize camera state want across mind his.",  
  "owner": [  
    "urn:ngsi-ld:Certificate:items:ZTPB:96026524",  
    "urn:ngsi-ld:Certificate:items:MZYH:89260401"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Certificate:items:LMJQ:88266844"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -52.637063,  
      23.558812  
    ]  
  },  
  "address": {  
    "streetAddress": "Modern society station campaign. Important through to discover guess. Someone consider entire li",  
    "addressLocality": "Firm art goal mind as include. Visit memory leg care probably because commercial how.",  
    "addressRegion": "Success right poor each near foot. At without shake main current strategy. Stand along stuff keep coach tow",  
    "addressCountry": "Wrong fall write onto forget. Air hard quality. Rise try blue either s",  
    "postalCode": "Point structure evening policy here. Use talk pressure democratic want.",  
    "postOfficeBoxNumber": "Cell board else course always recent. Property almost serve before.",  
    "streetNr": "Special shake soldier bed include. Thus doctor political blue even girl.",  
    "district": "Accept west participant suggest whatever feel later. Rule deep owner."  
  },  
  "areaServed": "Allow whole live analysis defense million strategy real. Bed chance different attention community protect. Government thus build ",  
  "type": "Certificate",  
  "state": "urn:ngsi-ld:Certificate:state:KHMM:25466110"  
}  
```  
</details>    
#### 인증서 NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 인증서의 예입니다. 이것은 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:OEMR:38840161",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2000-01-17T20:24:29Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2014-02-03T22:13:34Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Strategy there certainly federal. Risk manager carry shoulder only long."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Across him eight property help. Beat federal dream conference score special deal accept."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Heart beat fine nice identify. Wide usually me in painting tough entire."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Section employee few. Decision prevent easy."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Talk necessary run score recent. Expert seem money concern shoulder goal. Recognize camera state want across mind his."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:ZTPB:96026524",  
      "urn:ngsi-ld:Certificate:items:MZYH:89260401"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:LMJQ:88266844"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -52.637063,  
        23.558812  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Modern society station campaign. Important through to discover guess. Someone consider entire li",  
      "addressLocality": "Firm art goal mind as include. Visit memory leg care probably because commercial how.",  
      "addressRegion": "Success right poor each near foot. At without shake main current strategy. Stand along stuff keep coach tow",  
      "addressCountry": "Wrong fall write onto forget. Air hard quality. Rise try blue either s",  
      "postalCode": "Point structure evening policy here. Use talk pressure democratic want.",  
      "postOfficeBoxNumber": "Cell board else course always recent. Property almost serve before.",  
      "streetNr": "Special shake soldier bed include. Thus doctor political blue even girl.",  
      "district": "Accept west participant suggest whatever feel later. Rule deep owner."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Allow whole live analysis defense million strategy real. Bed chance different attention community protect. Government thus build "  
  },  
  "type": "Certificate",  
  "state": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Certificate:state:KHMM:25466110"  
  }  
}  
```  
</details>    
#### 인증서 NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 인증서의 예입니다. 이것은 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:OEMR:38840161",  
  "dateCreated": "2000-01-17T20:24:29Z",  
  "dateModified": "2014-02-03T22:13:34Z",  
  "source": "Strategy there certainly federal. Risk manager carry shoulder only long.",  
  "name": "Across him eight property help. Beat federal dream conference score special deal accept.",  
  "alternateName": "Heart beat fine nice identify. Wide usually me in painting tough entire.",  
  "description": "Section employee few. Decision prevent easy.",  
  "dataProvider": "Talk necessary run score recent. Expert seem money concern shoulder goal. Recognize camera state want across mind his.",  
  "owner": [  
    "urn:ngsi-ld:Certificate:items:ZTPB:96026524",  
    "urn:ngsi-ld:Certificate:items:MZYH:89260401"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Certificate:items:LMJQ:88266844"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -52.637063,  
      23.558812  
    ]  
  },  
  "address": {  
    "streetAddress": "Modern society station campaign. Important through to discover guess. Someone consider entire li",  
    "addressLocality": "Firm art goal mind as include. Visit memory leg care probably because commercial how.",  
    "addressRegion": "Success right poor each near foot. At without shake main current strategy. Stand along stuff keep coach tow",  
    "addressCountry": "Wrong fall write onto forget. Air hard quality. Rise try blue either s",  
    "postalCode": "Point structure evening policy here. Use talk pressure democratic want.",  
    "postOfficeBoxNumber": "Cell board else course always recent. Property almost serve before.",  
    "streetNr": "Special shake soldier bed include. Thus doctor political blue even girl.",  
    "district": "Accept west participant suggest whatever feel later. Rule deep owner."  
  },  
  "areaServed": "Allow whole live analysis defense million strategy real. Bed chance different attention community protect. Government thus build ",  
  "type": "Certificate",  
  "state": "urn:ngsi-ld:Certificate:state:KHMM:25466110",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 인증서 NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 인증서의 예입니다. 이것은 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:FQIG:83987629",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2001-08-13T18:45:46Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1990-10-25T01:23:48Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Teach interview sens"  
  },  
  "name": {  
    "type": "Property",  
    "value": "My away establish push woman none. She once man knowledge question enjoy suddenly. Left lay treatment local agent. Record former deal h"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Treat decide hospital doo"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Site before adult Democrat computer. Mrs at hair small trial arrive picture."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Individual "  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:XJAQ:41164811",  
      "urn:ngsi-ld:Certificate:items:ALDM:78818333"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:TYPY:58686784"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -19.9646155,  
        -63.326103  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Measure defense government. Move",  
      "addressLocality": "Chair fund always official production.",  
      "addressRegion": "Lawyer yeah skill without interview teach address. Quality magazine stand make. Community tough field despite during.",  
      "addressCountry": "Beyond discuss health continue.",  
      "postalCode": "Size song pattern capital plan. Part own break most none.",  
      "postOfficeBoxNumber": "Find degree what fall news. Husband new agreement str",  
      "streetNr": "White share make game perhaps also ago. Teach discussion teach talk.",  
      "district": "Team perform people rise. Attack far add. East card traditional mouth range."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Fill part form so necessary back. Accept color community "  
  },  
  "type": "Certificate",  
  "state": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Certificate:state:HXAA:38754798"  
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
10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

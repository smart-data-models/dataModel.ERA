<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: NetRelation    
================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/NetRelation/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
전역 설명: **토폴로지 네트워크를 나타내는 연결 그래프에서 에지를 정의하기 위한 베이스 클래스**입니다.    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `elementA[uri]`: 요소 A  - `elementB[uri]`: 요소 B  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `navigability[uri]`: 탐색 가능성  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `positionOnA[uri]`: A에 위치  - `positionOnB[uri]`: B에 위치  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 데이터 유형입니다. NetRelation이어야 합니다.  <!-- /30-PropertiesList -->    
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
NetRelation:      
  description: Base class for defining edges in the connectivity graph representing the topological network.      
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
    elementA:      
      description: Element A      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    elementB:      
      description: Element B      
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
    navigability:      
      description: Navigability      
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
    positionOnA:      
      description: Position on A      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    positionOnB:      
      description: Position on B      
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
      description: NGSI data type. It has to be NetRelation      
      enum:      
        - NetRelation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/NetRelation      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/NetRelation/LICENSE.md      
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
#### NetRelation NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 NetRelation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:QVEK:97020978",  
  "dateCreated": "2002-11-19T10:23:16Z",  
  "dateModified": "2003-03-10T03:36:36Z",  
  "source": "Radio occur group guy together. Prepare which behavior maybe watch actually Republican paper.",  
  "name": "Coach economic ",  
  "alternateName": "Friend film shake president politics. Glass but left business question side. Push despite education group house.",  
  "description": "Threat instead a loss add politics.",  
  "dataProvider": "Development reach series assume. Real attention today community.",  
  "owner": [  
    "urn:ngsi-ld:NetRelation:items:MAOY:99573659",  
    "urn:ngsi-ld:NetRelation:items:BYQO:04488951"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetRelation:items:VYGL:22233826"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      89.9053455,  
      -11.456382  
    ]  
  },  
  "address": {  
    "streetAddress": "Clearly chance feel operation able win me. Full firm save.",  
    "addressLocality": "Morning could approa",  
    "addressRegion": "Pressure side account matter so. Ta",  
    "addressCountry": "East back help hundred pay record. Language explain summer min",  
    "postalCode": "Leader view he decision could personal clear. World per",  
    "postOfficeBoxNumber": "White language agency east. Who mother mother same leave them rule.",  
    "streetNr": "Health I particular west. Floor Congress individual someone into ever foot.",  
    "district": "Have when good news trade above. Individual p"  
  },  
  "areaServed": "Spea",  
  "type": "NetRelation",  
  "elementA": "urn:ngsi-ld:NetRelation:elementA:TUIU:78345951",  
  "elementB": "urn:ngsi-ld:NetRelation:elementB:DHHX:71184798",  
  "navigability": "urn:ngsi-ld:NetRelation:navigability:TZOM:33501230",  
  "positionOnA": "urn:ngsi-ld:NetRelation:positionOnA:YSDM:89916223",  
  "positionOnB": "urn:ngsi-ld:NetRelation:positionOnB:IYRF:06079262"  
}  
```  
</details>    
#### NetRelation NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 NetRelation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:QVEK:97020978",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2002-11-19T10:23:16Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2003-03-10T03:36:36Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Radio occur group guy together. Prepare which behavior maybe watch actually Republican paper."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Coach economic "  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Friend film shake president politics. Glass but left business question side. Push despite education group house."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Threat instead a loss add politics."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Development reach series assume. Real attention today community."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:MAOY:99573659",  
      "urn:ngsi-ld:NetRelation:items:BYQO:04488951"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:VYGL:22233826"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        89.9053455,  
        -11.456382  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Clearly chance feel operation able win me. Full firm save.",  
      "addressLocality": "Morning could approa",  
      "addressRegion": "Pressure side account matter so. Ta",  
      "addressCountry": "East back help hundred pay record. Language explain summer min",  
      "postalCode": "Leader view he decision could personal clear. World per",  
      "postOfficeBoxNumber": "White language agency east. Who mother mother same leave them rule.",  
      "streetNr": "Health I particular west. Floor Congress individual someone into ever foot.",  
      "district": "Have when good news trade above. Individual p"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Spea"  
  },  
  "type": "NetRelation",  
  "elementA": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:elementA:TUIU:78345951"  
  },  
  "elementB": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:elementB:DHHX:71184798"  
  },  
  "navigability": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:navigability:TZOM:33501230"  
  },  
  "positionOnA": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:positionOnA:YSDM:89916223"  
  },  
  "positionOnB": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:positionOnB:IYRF:06079262"  
  }  
}  
```  
</details>    
#### NetRelation NGSI-LD 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 NetRelation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:QVEK:97020978",  
  "dateCreated": "2002-11-19T10:23:16Z",  
  "dateModified": "2003-03-10T03:36:36Z",  
  "source": "Radio occur group guy together. Prepare which behavior maybe watch actually Republican paper.",  
  "name": "Coach economic ",  
  "alternateName": "Friend film shake president politics. Glass but left business question side. Push despite education group house.",  
  "description": "Threat instead a loss add politics.",  
  "dataProvider": "Development reach series assume. Real attention today community.",  
  "owner": [  
    "urn:ngsi-ld:NetRelation:items:MAOY:99573659",  
    "urn:ngsi-ld:NetRelation:items:BYQO:04488951"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetRelation:items:VYGL:22233826"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      89.9053455,  
      -11.456382  
    ]  
  },  
  "address": {  
    "streetAddress": "Clearly chance feel operation able win me. Full firm save.",  
    "addressLocality": "Morning could approa",  
    "addressRegion": "Pressure side account matter so. Ta",  
    "addressCountry": "East back help hundred pay record. Language explain summer min",  
    "postalCode": "Leader view he decision could personal clear. World per",  
    "postOfficeBoxNumber": "White language agency east. Who mother mother same leave them rule.",  
    "streetNr": "Health I particular west. Floor Congress individual someone into ever foot.",  
    "district": "Have when good news trade above. Individual p"  
  },  
  "areaServed": "Spea",  
  "type": "NetRelation",  
  "elementA": "urn:ngsi-ld:NetRelation:elementA:TUIU:78345951",  
  "elementB": "urn:ngsi-ld:NetRelation:elementB:DHHX:71184798",  
  "navigability": "urn:ngsi-ld:NetRelation:navigability:TZOM:33501230",  
  "positionOnA": "urn:ngsi-ld:NetRelation:positionOnA:YSDM:89916223",  
  "positionOnB": "urn:ngsi-ld:NetRelation:positionOnB:IYRF:06079262",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### NetRelation NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 NetRelation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:JUHL:24845257",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-03-26T06:21:22Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1991-11-25T01:27:05Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Get able seven not return identify son could. Wish prevent way."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Project nation tea"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Interest since th"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Another whom experience Republican majority maybe. Deal security score accept hour vote. Executive church manage imp"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Heavy under today name available."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:MCOV:78184970",  
      "urn:ngsi-ld:NetRelation:items:WFNU:46021273"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:KMWK:60383200"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        6.426867,  
        -155.118055  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Somebody our issue myself meeting begin knowledge. Best Mr hit sing society economy.",  
      "addressLocality": "Find life economy life sing avoid rock. Similar party tonight natural clear it",  
      "addressRegion": "Pa",  
      "addressCountry": "To push help action score. Brother lose benefit main.",  
      "postalCode": "Base understand particular shake note response trouble spend. Station prevent individual more fl",  
      "postOfficeBoxNumber": "Impact who hand difference even cell never address. Road size back top indeed ",  
      "streetNr": "Race base effect car Mr talk huge blue. Mig",  
      "district": "Describe similar area cu"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Piece idea want likely turn job. Past "  
  },  
  "type": "NetRelation",  
  "elementA": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:elementA:NXWD:06501472"  
  },  
  "elementB": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:elementB:CNDJ:23196407"  
  },  
  "navigability": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:navigability:TDBB:08079538"  
  },  
  "positionOnA": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:positionOnA:WRNS:94567510"  
  },  
  "positionOnB": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:positionOnB:POXU:21033119"  
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

<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 특수 터널 영역    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/SpecialTunnelArea/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **터널 내 통로, 대피 및 구조 지점이 있는 구역 또는 위치**.    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 데이터 유형입니다. 이 데이터 유형은 SpecialTunnelArea  <!-- /30-PropertiesList -->    
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
SpecialTunnelArea:      
  description: 'Area or location within a tunnel where  there is a walkway, evacuation and rescue points.'      
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
    type:      
      description: NGSI data type. It has to be SpecialTunnelArea      
      enum:      
        - SpecialTunnelArea      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/SpecialTunnelArea      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SpecialTunnelArea/LICENSE.md      
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
#### SpecialTunnelArea NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 SpecialTunnelArea의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": "1988-01-11T13:27:45Z",  
  "dateModified": "2010-12-08T20:17:03Z",  
  "source": "Owner kid middle worry po",  
  "name": "Idea able accept. Always four majority education wait. South east t",  
  "alternateName": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two.",  
  "description": "Center these own security subject ability once. Catch animal office poor.",  
  "dataProvider": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve.",  
  "owner": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
    "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.1411545,  
      -167.120745  
    ]  
  },  
  "address": {  
    "streetAddress": "Build next e",  
    "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
    "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
    "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
    "postalCode": "Environmental bag officer do ball. Soc",  
    "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
    "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
    "district": "Pattern over scientist important"  
  },  
  "areaServed": "Current upon put current. His find imagine high course why sea.",  
  "type": "SpecialTunnelArea",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SpecialTunnelArea NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SpecialTunnelArea의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1988-01-11T13:27:45Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2010-12-08T20:17:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Owner kid middle worry po"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Idea able accept. Always four majority education wait. South east t"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Center these own security subject ability once. Catch animal office poor."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
      "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.1411545,  
        -167.120745  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Build next e",  
      "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
      "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
      "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
      "postalCode": "Environmental bag officer do ball. Soc",  
      "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
      "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
      "district": "Pattern over scientist important"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Current upon put current. His find imagine high course why sea."  
  },  
  "type": "SpecialTunnelArea",  
  "context": {  
    "type": "StructuredValue",  
    "value": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
    ]  
  }  
}  
```  
</details>    
#### SpecialTunnelArea NGSI-LD 키-값 예시    
다음은 JSON-LD 형식의 키-값으로 된 SpecialTunnelArea의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": "1988-01-11T13:27:45Z",  
  "dateModified": "2010-12-08T20:17:03Z",  
  "source": "Owner kid middle worry po",  
  "name": "Idea able accept. Always four majority education wait. South east t",  
  "alternateName": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two.",  
  "description": "Center these own security subject ability once. Catch animal office poor.",  
  "dataProvider": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve.",  
  "owner": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
    "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.1411545,  
      -167.120745  
    ]  
  },  
  "address": {  
    "streetAddress": "Build next e",  
    "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
    "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
    "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
    "postalCode": "Environmental bag officer do ball. Soc",  
    "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
    "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
    "district": "Pattern over scientist important"  
  },  
  "areaServed": "Current upon put current. His find imagine high course why sea.",  
  "type": "SpecialTunnelArea",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SpecialTunnelArea NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SpecialTunnelArea의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:INWI:10579735",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1992-01-22T20:24:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1980-02-15T17:27:55Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Three consumer rise certain and. Share operation "  
  },  
  "name": {  
    "type": "Property",  
    "value": "Should program heart effort often not. Black though believe theory choice travel level. Positive big right beat television respond run."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Commercial share budget. Mention industry build."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Friend save analysis event. Summer hospital box site hold matter agency. Measure gun"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Arrive read pattern be despite second matter. Thank teach oil his."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:TUJB:41707682",  
      "urn:ngsi-ld:SpecialTunnelArea:items:UXYT:76593602"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:JGSZ:99017778"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.77738,  
        -119.777978  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "On boy cell night. Sit stage difficult take onto best.",  
      "addressLocality": "East south bill former business federal argue. These machine their war. Vote because born natural",  
      "addressRegion": "Eye occur contain rest. Determine child interest action boy begin more.",  
      "addressCountry": "On home time left. Rather necessary talk same almost. Card computer see security.",  
      "postalCode": "State positive assume themselves media. Tax food while. Write eye st",  
      "postOfficeBoxNumber": "Role call wrong arrive marriage meet authority foreign. Show paper difficult really increase. Difference company free medical rich.",  
      "streetNr": "Use but left assume. Safe be during soldier. Natural success before begin part.",  
      "district": "White hand we return less. Product movie season man."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Those production act story gun necessary such. Almost space without. Herself pressure miss anyone contain car."  
  },  
  "type": "SpecialTunnelArea",  
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
10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

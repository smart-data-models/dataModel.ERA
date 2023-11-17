<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 차량    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/Vehicle/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **철도 노선에서 운행할 수 있는 특정 차량 또는 마차**.    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `compositeBrakeBlockRetrofitted[boolean]`: 복합 브레이크 블록 장착  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `manufacturingCountry[uri]`: 제조 국가  - `name[string]`: 이 항목의 이름  - `operationalRestriction[uri]`: 운영 제한  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `quieterRoutesExemptedCountry[uri]`: 조용한 경로 면제 국가  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 데이터 유형입니다. 차량이어야 합니다.  - `vehicleKeeper[uri]`: 차량 키퍼  - `vehicleNumber[string]`: 차량 번호  - `vehicleSeries[string]`: 차량 시리즈  - `vehicleType[uri]`: 차량 유형  <!-- /30-PropertiesList -->    
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
Vehicle:      
  description: A specific vehicle or wagon able to operate over railway lines.      
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
    compositeBrakeBlockRetrofitted:      
      description: Composite brake block retrofitted      
      type: boolean      
      x-ngsi:      
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
    manufacturingCountry:      
      description: Manufacturing country      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationalRestriction:      
      description: Operational restriction      
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
    quieterRoutesExemptedCountry:      
      description: Quieter route exempted country      
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
      description: NGSI data type. It has to be Vehicle      
      enum:      
        - Vehicle      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleKeeper:      
      description: Vehicle keeper      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    vehicleNumber:      
      description: Vehicle number      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleSeries:      
      description: Vehicle series      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleType:      
      description: Vehicle type      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/Vehicle      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Vehicle/LICENSE.md      
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
#### 차량 NGSI-v2 키값 예시    
다음은 키-값으로 JSON-LD 형식의 차량 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": "1981-05-29T06:37:15Z",  
  "dateModified": "2007-08-18T15:43:14Z",  
  "source": "Visit research power especially ",  
  "name": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door",  
  "alternateName": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research",  
  "description": "Morning continue help p",  
  "dataProvider": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half.",  
  "owner": [  
    "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
    "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      20.376035,  
      172.96204  
    ]  
  },  
  "address": {  
    "streetAddress": "Lay agree media everyone. Ability because cover.",  
    "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
    "addressRegion": "Se",  
    "addressCountry": "Course down what maybe physical. Memory dev",  
    "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
    "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
    "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
    "district": "Order teacher yes head. Report partner without government discuss shoulder."  
  },  
  "areaServed": "Great office person",  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": true,  
  "vehicleNumber": "Of light force police. Indicate best need.",  
  "vehicleSeries": "High article bill ",  
  "manufacturingCountry": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975",  
  "operationalRestriction": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720",  
  "quieterRoutesExemptedCountry": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691",  
  "vehicleKeeper": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099",  
  "vehicleType": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377"  
}  
```  
</details>    
#### 차량 NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 차량 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1981-05-29T06:37:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2007-08-18T15:43:14Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Visit research power especially "  
  },  
  "name": {  
    "type": "Text",  
    "value": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Morning continue help p"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
      "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        20.376035,  
        172.96204  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Lay agree media everyone. Ability because cover.",  
      "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
      "addressRegion": "Se",  
      "addressCountry": "Course down what maybe physical. Memory dev",  
      "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
      "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
      "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
      "district": "Order teacher yes head. Report partner without government discuss shoulder."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Great office person"  
  },  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleNumber": {  
    "type": "Text",  
    "value": "Of light force police. Indicate best need."  
  },  
  "vehicleSeries": {  
    "type": "Text",  
    "value": "High article bill "  
  },  
  "manufacturingCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975"  
  },  
  "operationalRestriction": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720"  
  },  
  "quieterRoutesExemptedCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691"  
  },  
  "vehicleKeeper": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099"  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377"  
  }  
}  
```  
</details>    
#### 차량 NGSI-LD 키 값 예시    
다음은 키-값으로 JSON-LD 형식의 차량 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": "1981-05-29T06:37:15Z",  
  "dateModified": "2007-08-18T15:43:14Z",  
  "source": "Visit research power especially ",  
  "name": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door",  
  "alternateName": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research",  
  "description": "Morning continue help p",  
  "dataProvider": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half.",  
  "owner": [  
    "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
    "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      20.376035,  
      172.96204  
    ]  
  },  
  "address": {  
    "streetAddress": "Lay agree media everyone. Ability because cover.",  
    "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
    "addressRegion": "Se",  
    "addressCountry": "Course down what maybe physical. Memory dev",  
    "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
    "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
    "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
    "district": "Order teacher yes head. Report partner without government discuss shoulder."  
  },  
  "areaServed": "Great office person",  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": true,  
  "vehicleNumber": "Of light force police. Indicate best need.",  
  "vehicleSeries": "High article bill ",  
  "manufacturingCountry": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975",  
  "operationalRestriction": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720",  
  "quieterRoutesExemptedCountry": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691",  
  "vehicleKeeper": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099",  
  "vehicleType": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 차량 NGSI-LD 정규화 예시    
다음은 정규화된 JSON-LD 형식의 차량 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:RFYH:06883935",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-06-19T07:24:12Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1998-03-27T15:27:54Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Project option account government. Ask company grow."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Part matter sh"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nearly alone the when together. Whole sure would require mission."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Church exactly remain situation training effect resource. Movie describe concern single as population moment. Director stage range professional fast. Sell talk onto whom question job decid"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Place teacher support teach practice son pay college. Sit certain near short area by decision. Stand size guy reason rese"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:EBYW:72457592",  
      "urn:ngsi-ld:Vehicle:items:MJUB:28310670"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:WNSX:51918079"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -37.542901,  
        -116.836751  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Rich thousand authority beat best white free. Tend season get prevent wind. Catch door foot wrong citizen miss develop.",  
      "addressLocality": "Test growth another. Be easy painting human. College ",  
      "addressRegion": "Nice pay pattern sense education game. Tonight yourself spring though participant threat majority.",  
      "addressCountry": "Purpose case eight just. Cause discussion technology sing.",  
      "postalCode": "Yeah conference push determine I tough.",  
      "postOfficeBoxNumber": "Sea also cell office force letter week. Total create as onto people. Full wall address early lose everything kid.",  
      "streetNr": "Why rise PM mother bank light. Ha",  
      "district": "Responsibility blue increase. Newspaper remain else"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Make own mother news film PM some. All arrive than put cold five stand."  
  },  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": {  
    "type": "Property",  
    "value": false  
  },  
  "vehicleNumber": {  
    "type": "Property",  
    "value": "Sure stock standard child goal in. Option hand parent piece no."  
  },  
  "vehicleSeries": {  
    "type": "Property",  
    "value": "Public story thus wind whether. Sometimes attorney couple person hand green. Within seek sid"  
  },  
  "manufacturingCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:manufacturingCountry:YUHQ:94193670"  
  },  
  "operationalRestriction": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:operationalRestriction:HSZJ:08079193"  
  },  
  "quieterRoutesExemptedCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:HKQL:88249057"  
  },  
  "vehicleKeeper": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZJDS:72987137"  
  },  
  "vehicleType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:vehicleType:KUTI:03320913"  
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

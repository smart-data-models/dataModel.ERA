<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 사이딩    
========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/Siding/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **사이딩은 운행 중인 열차의 운행이 종료되는 선로 중 열차 운행 경로에 사용되지 않는 모든 선로를 말합니다.**    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `demonstrationINF[string]`: 트랙/사이딩에 대한 EI 데모 선언 [INF]  - `description[string]`: 이 항목에 대한 설명  - `gradient[number]`: 트랙 안정화를 위한 그라데이션  - `hasElectricShoreSupply[boolean]`: 전기 해안 공급의 존재  - `hasExternalCleaning[boolean]`: 외부 청소 시설의 존재 여부  - `hasRefuelling[boolean]`: 급유 존재 여부  - `hasSandRestocking[boolean]`: 모래 재입고 존재 여부  - `hasToiletDischarge[boolean]`: 화장실 분비물 존재 여부  - `hasWaterRestocking[boolean]`: 물 재입고 존재 여부  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maxCurrentStandstillPantograph[number]`: 팬터그래프당 정지 상태에서의 최대 전류  - `minimumHorizontalRadius[number]`: 수평 커브의 최소 반경  - `minimumVerticalRadius[string]`: 수직 커브의 최소 반경  - `minimumVerticalRadiusCrest[number]`: 수직 커브 크레스트의 최소 반경  - `minimumVerticalRadiusHollow[number]`: 수직 커브 중공의 최소 반경  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `sidingId[string]`: 사이딩 식별  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tenClassification[uri]`: TEN 분류(선로, 플랫폼, 사이딩)  - `type[string]`: NGSI 데이터 유형입니다. 사이딩이어야 합니다.  - `verificationINF[string]`: 선로/사이딩에 대한 EC 검증 선언 [INF]  <!-- /30-PropertiesList -->    
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
Siding:      
  description: Sidings are all those tracks where running trains in service movements ends and which are not used for operational routing of a train.      
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
    demonstrationINF:      
      description: 'EI declaration of demonstration for track/siding [INF]'      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    gradient:      
      description: Gradient for stabling tracks      
      type: number      
      x-ngsi:      
        type: Property      
    hasElectricShoreSupply:      
      description: Existence of electric shore supply      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasExternalCleaning:      
      description: Existence of external cleaning facilities      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasRefuelling:      
      description: Existence of refuelling      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasSandRestocking:      
      description: Existence of sand restocking      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasToiletDischarge:      
      description: Existence of toilet discharge      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasWaterRestocking:      
      description: Existence of water restocking      
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
    maxCurrentStandstillPantograph:      
      description: Maximum current at standstill per pantograph      
      type: number      
      x-ngsi:      
        type: Property      
    minimumHorizontalRadius:      
      description: Minimum radius of horizontal curve      
      type: number      
      x-ngsi:      
        type: Property      
    minimumVerticalRadius:      
      description: Minimum radius of vertical curve      
      type: string      
      x-ngsi:      
        type: Property      
    minimumVerticalRadiusCrest:      
      description: Minimum radius of vertical curve crest      
      type: number      
      x-ngsi:      
        type: Property      
    minimumVerticalRadiusHollow:      
      description: Minimum radius of vertical curve hollow      
      type: number      
      x-ngsi:      
        type: Property      
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
    sidingId:      
      description: Identification of siding      
      type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    tenClassification:      
      description: 'TEN classification (of track, of platform, of siding)'      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    type:      
      description: NGSI data type. It has to be Siding      
      enum:      
        - Siding      
      type: string      
      x-ngsi:      
        type: Property      
    verificationINF:      
      description: 'EC declaration of verification for track/siding [INF]'      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/Siding      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Siding/LICENSE.md      
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
#### 사이딩 NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 사이딩의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": "2013-05-04T09:51:15Z",  
  "dateModified": "1974-05-09T12:06:14Z",  
  "source": "Push list then again. State get suddenly nor table.",  
  "name": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s",  
  "alternateName": "Name down over test feeling Congress. Recent his his back partner reduce material your.",  
  "description": "Anything so doctor finally. Despite practice class store.",  
  "dataProvider": "Us which she quickly else party. Way that give main air short near. Real popular whatever s",  
  "owner": [  
    "urn:ngsi-ld:Siding:items:SXEI:27228317",  
    "urn:ngsi-ld:Siding:items:EIZG:41039273"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Siding:items:DOKD:91972812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.875369,  
      98.837859  
    ]  
  },  
  "address": {  
    "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
    "addressLocality": "Since ",  
    "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
    "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
    "postalCode": "Personal build",  
    "postOfficeBoxNumber": "Leader enough weight everything.",  
    "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
    "district": "Area cost hundred same. Sense anyone anyone."  
  },  
  "areaServed": "Moment agent four language. Tend place r",  
  "type": "Siding",  
  "demonstrationINF": "Its federal stand tr",  
  "gradient": 354.9,  
  "hasElectricShoreSupply": true,  
  "hasExternalCleaning": true,  
  "hasRefuelling": true,  
  "hasSandRestocking": false,  
  "hasToiletDischarge": false,  
  "hasWaterRestocking": false,  
  "maxCurrentStandstillPantograph": 81.3,  
  "minimumHorizontalRadius": 864,  
  "minimumVerticalRadius": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "minimumVerticalRadiusCrest": 864,  
  "minimumVerticalRadiusHollow": 864,  
  "sidingId": "American whole magazine",  
  "verificationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "tenClassification": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097"  
}  
```  
</details>    
#### 사이딩 NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 사이딩 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2013-05-04T09:51:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1974-05-09T12:06:14Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Push list then again. State get suddenly nor table."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Name down over test feeling Congress. Recent his his back partner reduce material your."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Anything so doctor finally. Despite practice class store."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Us which she quickly else party. Way that give main air short near. Real popular whatever s"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Siding:items:SXEI:27228317",  
      "urn:ngsi-ld:Siding:items:EIZG:41039273"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Siding:items:DOKD:91972812"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -36.875369,  
        98.837859  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
      "addressLocality": "Since ",  
      "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
      "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
      "postalCode": "Personal build",  
      "postOfficeBoxNumber": "Leader enough weight everything.",  
      "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
      "district": "Area cost hundred same. Sense anyone anyone."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Moment agent four language. Tend place r"  
  },  
  "type": "Siding",  
  "demonstrationINF": {  
    "type": "Text",  
    "value": "Its federal stand tr"  
  },  
  "gradient": {  
    "type": "Number",  
    "value": 354.9  
  },  
  "hasElectricShoreSupply": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasExternalCleaning": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasRefuelling": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasSandRestocking": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasToiletDischarge": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasWaterRestocking": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Number",  
    "value": 81.3  
  },  
  "minimumHorizontalRadius": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumVerticalRadius": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "minimumVerticalRadiusCrest": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumVerticalRadiusHollow": {  
    "type": "Number",  
    "value": 864  
  },  
  "sidingId": {  
    "type": "Text",  
    "value": "American whole magazine"  
  },  
  "verificationINF": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "tenClassification": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097"  
  }  
}  
```  
</details>    
#### 사이딩 NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 사이딩의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": "2013-05-04T09:51:15Z",  
  "dateModified": "1974-05-09T12:06:14Z",  
  "source": "Push list then again. State get suddenly nor table.",  
  "name": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s",  
  "alternateName": "Name down over test feeling Congress. Recent his his back partner reduce material your.",  
  "description": "Anything so doctor finally. Despite practice class store.",  
  "dataProvider": "Us which she quickly else party. Way that give main air short near. Real popular whatever s",  
  "owner": [  
    "urn:ngsi-ld:Siding:items:SXEI:27228317",  
    "urn:ngsi-ld:Siding:items:EIZG:41039273"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Siding:items:DOKD:91972812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.875369,  
      98.837859  
    ]  
  },  
  "address": {  
    "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
    "addressLocality": "Since ",  
    "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
    "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
    "postalCode": "Personal build",  
    "postOfficeBoxNumber": "Leader enough weight everything.",  
    "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
    "district": "Area cost hundred same. Sense anyone anyone."  
  },  
  "areaServed": "Moment agent four language. Tend place r",  
  "type": "Siding",  
  "demonstrationINF": "Its federal stand tr",  
  "gradient": 354.9,  
  "hasElectricShoreSupply": true,  
  "hasExternalCleaning": true,  
  "hasRefuelling": true,  
  "hasSandRestocking": false,  
  "hasToiletDischarge": false,  
  "hasWaterRestocking": false,  
  "maxCurrentStandstillPantograph": 81.3,  
  "minimumHorizontalRadius": 864,  
  "minimumVerticalRadius": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "minimumVerticalRadiusCrest": 864,  
  "minimumVerticalRadiusHollow": 864,  
  "sidingId": "American whole magazine",  
  "verificationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "tenClassification": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 사이딩 NGSI-LD 정규화 예시    
다음은 정규화된 JSON-LD 형식의 사이딩 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:LIKW:54042696",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1996-09-19T23:08:47Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1994-06-22T11:37:34Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Structure decision camera reach purpose role prepare. Fish nor team avoid party memory most unit."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Great discover down event record milita"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Necessary billion gas Congress need explain safe. Law media people a sister consider."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Hotel country risk. Method bit seat organization partner."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Board movement understand. Each I give soon."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Siding:items:RYOP:03718728",  
      "urn:ngsi-ld:Siding:items:OGDX:73134134"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Siding:items:SIJP:84831513"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.4755575,  
        91.269469  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "According laugh government goal teacher social. Only speak effect policy easy learn. Material suddenly appear animal keep.",  
      "addressLocality": "",  
      "addressRegion": "Energy better life herself listen minute attorney. Bank you produce magazine.",  
      "addressCountry": "American sure message",  
      "postalCode": "Everything stand agreement hope forward. End debate deep act.",  
      "postOfficeBoxNumber": "Those public may range public. Hous",  
      "streetNr": "Discussion clear action add key reflect. Skill beautiful leg worker least ",  
      "district": "Discussion early quality that morning eye full. My at"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Report democratic en"  
  },  
  "type": "Siding",  
  "demonstrationINF": {  
    "type": "Property",  
    "value": "Pm can assume agency Mr reach music computer"  
  },  
  "gradient": {  
    "type": "Property",  
    "value": 733.9  
  },  
  "hasElectricShoreSupply": {  
    "type": "Property",  
    "value": true  
  },  
  "hasExternalCleaning": {  
    "type": "Property",  
    "value": true  
  },  
  "hasRefuelling": {  
    "type": "Property",  
    "value": true  
  },  
  "hasSandRestocking": {  
    "type": "Property",  
    "value": true  
  },  
  "hasToiletDischarge": {  
    "type": "Property",  
    "value": false  
  },  
  "hasWaterRestocking": {  
    "type": "Property",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Property",  
    "value": 818.3  
  },  
  "minimumHorizontalRadius": {  
    "type": "Property",  
    "value": 975  
  },  
  "minimumVerticalRadius": {  
    "type": "Property",  
    "value": "Police almost show day. Number only form skin t"  
  },  
  "minimumVerticalRadiusCrest": {  
    "type": "Property",  
    "value": 799  
  },  
  "minimumVerticalRadiusHollow": {  
    "type": "Property",  
    "value": 937  
  },  
  "sidingId": {  
    "type": "Property",  
    "value": "Air owner child site team modern behavior figure. Behavior near pick which civil door."  
  },  
  "verificationINF": {  
    "type": "Property",  
    "value": "Establish wh"  
  },  
  "tenClassification": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Siding:tenClassification:IURD:46677461"  
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

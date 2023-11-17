<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: OperationalPoint    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/OperationalPoint/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **운영 지점(OP)은 열차 서비스가 시작 및 종료되거나 경로를 변경할 수 있고 여객 또는 화물 서비스가 제공될 수 있는 열차 서비스 운영을 위한 모든 위치를 의미하며, 운영 지점은 회원국 또는 인프라 관리자 간의 경계에 있는 모든 위치를 의미하기도 합니다.    
https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.2 주요 위치(역, 야드, 교차로, 화물 터미널)**에서.    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `borderPointOf[uri]`: 의 경계점  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `digitalSchematicOverview[string]`: 디지털 회로도 개요  - `hasSchematicOverviewOPDigitalForm[boolean]`: 디지털 형식의 회로도 개요 제공  - `id[*]`: 엔티티의 고유 식별자  - `localRulesOrRestrictions[boolean]`: 엄격하게 지역적인 성격의 규칙 및 제한이 존재합니다.  - `localRulesOrRestrictionsDoc[string]`: IM에서 제공하는 엄격한 로컬 성격의 규칙 또는 제한에 관한 문서  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `opInfoPerCountry[uri]`: 국가별 국경 지점 정보  - `opName[string]`: 운영 지점 이름  - `opType[uri]`: 운영 포인트 유형  - `opTypeGaugeChangeover[string]`: 선로 게이지 전환 시설의 유형  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `schematicOverviewOP[string]`: 운영 지점에 대한 개략적인 개요  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `siding[uri]`: 사이딩  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tafTAPCode[string]`: 텔레매틱스 애플리케이션과 관련된 TSI에 따라 정보 교환을 위해 개발된 기본 위치 코드입니다.  - `track[uri]`: 트랙  - `type[string]`: NGSI 데이터 유형입니다. OperationalPoint여야 합니다.  - `uopid[string]`: 고유 OP ID  <!-- /30-PropertiesList -->    
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
## 페이로드 예시    
#### OperationalPoint NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 OperationalPoint의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 오퍼레이셔널포인트 NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 OperationalPoint의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### OperationalPoint NGSI-LD 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 OperationalPoint의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 오퍼레이셔널포인트 NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 OperationalPoint의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: VehicleKeeper    
==================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/VehicleKeeper/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **특정 차량을 소유하거나 운영하는 회사 또는 조직**.    
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 데이터 유형입니다. VehicleKeeper여야 합니다.  <!-- /30-PropertiesList -->    
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
VehicleKeeper:      
  description: A company or organization that owns or operates a certain vehicle.      
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
      description: NGSI data type. It has to be VehicleKeeper      
      enum:      
        - VehicleKeeper      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/VehicleKeeper      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/VehicleKeeper/LICENSE.md      
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
#### VehicleKeeper NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 VehicleKeeper의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:XXBI:45242122",  
  "dateCreated": "2021-09-14T02:23:10Z",  
  "dateModified": "1997-03-24T06:16:52Z",  
  "source": "K",  
  "name": "Quite receive message front include indeed with. Sign coach actu",  
  "alternateName": "Measure how American red. Child few inside save. Wonder total moment safe democratic wonder.",  
  "description": "Produce car space whose. Travel candidate compare forget still.",  
  "dataProvider": "Card rise their doctor together enjoy cle",  
  "owner": [  
    "urn:ngsi-ld:VehicleKeeper:items:ETMT:35445191",  
    "urn:ngsi-ld:VehicleKeeper:items:ZVVO:84115238"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:VehicleKeeper:items:HCCU:66226906"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.213131,  
      -151.498321  
    ]  
  },  
  "address": {  
    "streetAddress": "Company recently close affect. Others Congress ",  
    "addressLocality": "Region purpose probably expert road give. Occur and according some. Event outside usually newspaper.",  
    "addressRegion": "Remember discuss Democrat party. Since claim appear stuff pull alo",  
    "addressCountry": "Nature find",  
    "postalCode": "Point begin economy minute. Necessary candidate woman church which beautiful.",  
    "postOfficeBoxNumber": "Affect top receive to security remember area street. Only operation important modern thing join.",  
    "streetNr": "Significant defense agent now ",  
    "district": "Pass heart with several esta"  
  },  
  "areaServed": "So memory ve",  
  "type": "VehicleKeeper"  
}  
```  
</details>    
#### VehicleKeeper NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 VehicleKeeper의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:XXBI:45242122",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2021-09-14T02:23:10Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1997-03-24T06:16:52Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "K"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Quite receive message front include indeed with. Sign coach actu"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Measure how American red. Child few inside save. Wonder total moment safe democratic wonder."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Produce car space whose. Travel candidate compare forget still."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Card rise their doctor together enjoy cle"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:ETMT:35445191",  
      "urn:ngsi-ld:VehicleKeeper:items:ZVVO:84115238"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:HCCU:66226906"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        48.213131,  
        -151.498321  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Company recently close affect. Others Congress ",  
      "addressLocality": "Region purpose probably expert road give. Occur and according some. Event outside usually newspaper.",  
      "addressRegion": "Remember discuss Democrat party. Since claim appear stuff pull alo",  
      "addressCountry": "Nature find",  
      "postalCode": "Point begin economy minute. Necessary candidate woman church which beautiful.",  
      "postOfficeBoxNumber": "Affect top receive to security remember area street. Only operation important modern thing join.",  
      "streetNr": "Significant defense agent now ",  
      "district": "Pass heart with several esta"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "So memory ve"  
  },  
  "type": "VehicleKeeper"  
}  
```  
</details>    
#### VehicleKeeper NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 VehicleKeeper의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:XXBI:45242122",  
  "dateCreated": "2021-09-14T02:23:10Z",  
  "dateModified": "1997-03-24T06:16:52Z",  
  "source": "K",  
  "name": "Quite receive message front include indeed with. Sign coach actu",  
  "alternateName": "Measure how American red. Child few inside save. Wonder total moment safe democratic wonder.",  
  "description": "Produce car space whose. Travel candidate compare forget still.",  
  "dataProvider": "Card rise their doctor together enjoy cle",  
  "owner": [  
    "urn:ngsi-ld:VehicleKeeper:items:ETMT:35445191",  
    "urn:ngsi-ld:VehicleKeeper:items:ZVVO:84115238"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:VehicleKeeper:items:HCCU:66226906"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.213131,  
      -151.498321  
    ]  
  },  
  "address": {  
    "streetAddress": "Company recently close affect. Others Congress ",  
    "addressLocality": "Region purpose probably expert road give. Occur and according some. Event outside usually newspaper.",  
    "addressRegion": "Remember discuss Democrat party. Since claim appear stuff pull alo",  
    "addressCountry": "Nature find",  
    "postalCode": "Point begin economy minute. Necessary candidate woman church which beautiful.",  
    "postOfficeBoxNumber": "Affect top receive to security remember area street. Only operation important modern thing join.",  
    "streetNr": "Significant defense agent now ",  
    "district": "Pass heart with several esta"  
  },  
  "areaServed": "So memory ve",  
  "type": "VehicleKeeper",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### VehicleKeeper NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 VehicleKeeper 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:OQLK:27164371",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-12-25T16:50:11Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1994-07-16T07:43:37Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Shake ago quality hard suddenly. Campaign data itself them industry."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Less walk way success. Kitchen realize edge level action. Reduc"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Wall cold determine who. Water whether under else blue get."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Color opportunity player prevent ago tonight pretty. Themselves nation d"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Space customer statement issue daughter than already."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:VRJH:99019247",  
      "urn:ngsi-ld:VehicleKeeper:items:JMRS:40266513"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:RXUF:20636106"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -68.0082615,  
        43.406974  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Resource scientist company not choice. Move with professor discussion. Stuff less activity either arrive gun American ",  
      "addressLocality": "Inside third practice occur",  
      "addressRegion": "Notice",  
      "addressCountry": "How choice lay. With always game opportunity early. Practice list local particular paper though. Trouble professional Democrat ahead.",  
      "postalCode": "Capital give subject pull. School authority follow set something create.",  
      "postOfficeBoxNumber": "While once summer executive. Wife idea ",  
      "streetNr": "Store hard add. Food down about significa",  
      "district": "Hear real we information."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Air beat year help wrong production and upon. Full long suddenly prevent policy c"  
  },  
  "type": "VehicleKeeper",  
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

<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

엔티티: LineReference    
==================
<!-- /10-Header -->
    
<!-- 15-License -->
    

[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/LineReference/LICENSE.md)    

[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

글로벌 설명: **철도 위치**    

버전: 0.0.1    
<!-- /20-Description -->
    
<!-- 30-PropertiesList -->
    

## 속성 목록    

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  
- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  
- `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  
- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  
- `description[string]`: 이 항목에 대한 설명  
- `id[*]`: 엔티티의 고유 식별자  
- `kilometer[number]`: 킬로미터  
- `lineNationalId[uri]`: 국가 회선 식별  
- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  
- `name[string]`: 이 항목의 이름  
- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  
- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  
- `type[string]`: NGSI 데이터 유형입니다. LineReference여야 합니다.  
<!-- /30-PropertiesList -->
    
<!-- 35-RequiredProperties -->
    

필수 속성    
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
    
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
LineReference:      
  description: Railway location      
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
    kilometer:      
      description: Kilometer      
      type: number      
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
      description: NGSI data type. It has to be LineReference      
      enum:      
        - LineReference      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/LineReference      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/LineReference/LICENSE.md      
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

#### LineReference NGSI-v2 키-값 예시    

다음은 키-값으로 JSON-LD 형식의 LineReference의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:LineReference:id:RHSX:14820983",  
  "dateCreated": "1986-10-27T03:38:58Z",  
  "dateModified": "1977-09-15T07:25:57Z",  
  "source": "New create receive low hotel speech doctor political. Skin new shake view.",  
  "name": "Mind develop police. Change bill thing. Figure nation piece clearly detail others usually. Street writer four establish industr",  
  "alternateName": "Day toward including sometimes. Require ",  
  "description": "Project represent voice project decision yes total. Support idea ",  
  "dataProvider": "Class figure quality she. Continue traditional follow. Civil tough middle act beat.",  
  "owner": [  
    "urn:ngsi-ld:LineReference:items:NUGB:26269993",  
    "urn:ngsi-ld:LineReference:items:GVBX:53792463"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:LineReference:items:FXDW:87126015"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -45.052783,  
      152.191861  
    ]  
  },  
  "address": {  
    "streetAddress": "Western technology water budget everybody. Phone bring kitchen same. Impact policy head serve nothing.",  
    "addressLocality": "Its position them treat few whose compare. Into ok key general next foreign. Among agency kitchen along usually position.",  
    "addressRegion": "Miss important simply economy finish left stuff. Help cover particularly idea. Only chair agree.",  
    "addressCountry": "Town computer thank rather. Break onto money tend.",  
    "postalCode": "Back blue finally suffer notice. Weight fu",  
    "postOfficeBoxNumber": "Any pers",  
    "streetNr": "Mother traditional run campaign.",  
    "district": "Official situation tonight north tough sound. Debate project player car structure vote. Poo"  
  },  
  "areaServed": "Red animal wall front. Left buy see always.",  
  "type": "LineReference",  
  "kilometer": 239.9,  
  "lineNationalId": "urn:ngsi-ld:LineReference:lineNationalId:IIBS:67837023"
}  
```  
</details>    

#### LineReference NGSI-v2 정규화 예제    

다음은 정규화된 JSON-LD 형식의 LineReference의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:LineReference:id:RHSX:14820983",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1986-10-27T03:38:58Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1977-09-15T07:25:57Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "New create receive low hotel speech doctor political. Skin new shake view."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Mind develop police. Change bill thing. Figure nation piece clearly detail others usually. Street writer four establish industr"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Day toward including sometimes. Require "  
  },  
  "description": {  
    "type": "Text",  
    "value": "Project represent voice project decision yes total. Support idea "  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Class figure quality she. Continue traditional follow. Civil tough middle act beat."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:NUGB:26269993",  
      "urn:ngsi-ld:LineReference:items:GVBX:53792463"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:FXDW:87126015"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -45.052783,  
        152.191861  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Western technology water budget everybody. Phone bring kitchen same. Impact policy head serve nothing.",  
      "addressLocality": "Its position them treat few whose compare. Into ok key general next foreign. Among agency kitchen along usually position.",  
      "addressRegion": "Miss important simply economy finish left stuff. Help cover particularly idea. Only chair agree.",  
      "addressCountry": "Town computer thank rather. Break onto money tend.",  
      "postalCode": "Back blue finally suffer notice. Weight fu",  
      "postOfficeBoxNumber": "Any pers",  
      "streetNr": "Mother traditional run campaign.",  
      "district": "Official situation tonight north tough sound. Debate project player car structure vote. Poo"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Red animal wall front. Left buy see always."  
  },  
  "type": "LineReference",  
  "kilometer": {  
    "type": "Number",  
    "value": 239.9  
  },  
  "lineNationalId": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:LineReference:lineNationalId:IIBS:67837023"  
  }  
}  
```  
</details>    

#### LineReference NGSI-LD 키-값 예시    

다음은 키-값으로 JSON-LD 형식의 LineReference의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:LineReference:id:RHSX:14820983",  
  "dateCreated": "1986-10-27T03:38:58Z",  
  "dateModified": "1977-09-15T07:25:57Z",  
  "source": "New create receive low hotel speech doctor political. Skin new shake view.",  
  "name": "Mind develop police. Change bill thing. Figure nation piece clearly detail others usually. Street writer four establish industr",  
  "alternateName": "Day toward including sometimes. Require ",  
  "description": "Project represent voice project decision yes total. Support idea ",  
  "dataProvider": "Class figure quality she. Continue traditional follow. Civil tough middle act beat.",  
  "owner": [  
    "urn:ngsi-ld:LineReference:items:NUGB:26269993",  
    "urn:ngsi-ld:LineReference:items:GVBX:53792463"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:LineReference:items:FXDW:87126015"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -45.052783,  
      152.191861  
    ]  
  },  
  "address": {  
    "streetAddress": "Western technology water budget everybody. Phone bring kitchen same. Impact policy head serve nothing.",  
    "addressLocality": "Its position them treat few whose compare. Into ok key general next foreign. Among agency kitchen along usually position.",  
    "addressRegion": "Miss important simply economy finish left stuff. Help cover particularly idea. Only chair agree.",  
    "addressCountry": "Town computer thank rather. Break onto money tend.",  
    "postalCode": "Back blue finally suffer notice. Weight fu",  
    "postOfficeBoxNumber": "Any pers",  
    "streetNr": "Mother traditional run campaign.",  
    "district": "Official situation tonight north tough sound. Debate project player car structure vote. Poo"  
  },  
  "areaServed": "Red animal wall front. Left buy see always.",  
  "type": "LineReference",  
  "kilometer": 239.9,  
  "lineNationalId": "urn:ngsi-ld:LineReference:lineNationalId:IIBS:67837023",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### LineReference NGSI-LD 정규화 예제    

다음은 정규화된 JSON-LD 형식의 LineReference의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:LineReference:id:UGOL:02314727",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-09-26T20:09:19Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1986-05-17T22:22:32Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Himself peace act."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Among safe number anyone white. Away success listen hot stock road. Early though question economy cause share defense."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Realize huma"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Control get personal raise r"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Drive understand apply town research big. Together hundred event seem back."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:ODGA:61913437",  
      "urn:ngsi-ld:LineReference:items:TQIE:40363820"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:EVEX:08441746"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        46.8926945,  
        -133.98211  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Quite manage event shoulder nation ago. Measure treat nor receive there person. Stay vote",  
      "addressLocality": "Instead air fight minute. Place arm ball end career foreign type size. Morning stuff necessary again.",  
      "addressRegion": "Before account article. Tough pattern himself TV mention strong consumer. Name painting want sing alone.",  
      "addressCountry": "Assume nature organization over. People establish relationship ago. Between seem sport when agent",  
      "postalCode": "Green by seem despite. Yard early tax security five. Traditional red discover interest past if. Happ",  
      "postOfficeBoxNumber": "Check would effect fight best ",  
      "streetNr": "Magazine eat teacher list trial already career his. Yet concern wan",  
      "district": "Adult administration always seat explain."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Security each election well position. Including without official truth past bit. Group or rest whatever he."  
  },  
  "type": "LineReference",  
  "kilometer": {  
    "type": "Property",  
    "value": 890.1  
  },  
  "lineNationalId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:LineReference:lineNationalId:HTQW:41563123"  
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
    

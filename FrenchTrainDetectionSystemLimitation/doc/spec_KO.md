<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: FrenchTrainDetectionSystemLimitation  
============================================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **프랑스 네트워크에서 경로 호환성 확인을 위해 특정됩니다. 다음이 포함된 구간:  
-1 트랙당 순환 톤수가 15000톤/일/트랙보다 낮음  
-2 방향 연동  
-3 방향 연동 시 45초 지연  
-4 트랙 회로 안내와 함께 설치  
-5 비가역 복선 선로의 경우 정상 순환 방향에 분로 보조 페달이 없음  
-6 단선 선로 및 양방향 작업용 선로의 경우 통행 방향에 관계없이 분로 보조 페달 부재  
-7 페달 안내 메커니즘 부재  
-8 특정 안내 방송 리셋 장치의 경우 45초 지연**  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `frenchTrainDetectionSystemLimitationApplicable[boolean]`: 열차 감지 제한이 있는 구간은 프랑스 네트워크에만 적용됩니다.  - `frenchTrainDetectionSystemLimitationNumber[uri]`: 열차 감지 제한 번호가 있는 구간, 프랑스 네트워크 전용  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 데이터 유형입니다. FrenchTrainDetectionSystemLimitation이어야 합니다.  <!-- /30-PropertiesList -->  
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
FrenchTrainDetectionSystemLimitation:    
  description: "Specific for route compatibility check on French network. Sections with: \n-1 Tonnage circulated per track is inferior to 15000 tons/day/track \n-2 Directional Interlocking \n-3 45-second delay for directional interlocking \n-4 Installation with track circuit announcement \n-5 Absence of a shunting assistance pedal in the normal direction of circulation for non-reversible double track lines \n-6 Absence of a shunting assistance pedal regardless of the direction of traffic for single track lines and tracks for two way working \n-7 Absence of a pedal announcement mechanism \n-8 45-second delay for specific announcement reset devices"    
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
    frenchTrainDetectionSystemLimitationApplicable:    
      description: 'Section with train detection limitation is applicable, only for the French network'    
      type: boolean    
      x-ngsi:    
        type: Property    
    frenchTrainDetectionSystemLimitationNumber:    
      description: 'Section with train detection limitation number, only for French  network'    
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
      description: NGSI data type. It has to be FrenchTrainDetectionSystemLimitation    
      enum:    
        - FrenchTrainDetectionSystemLimitation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/FrenchTrainDetectionSystemLimitation    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/LICENSE.md    
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
#### FrenchTrainDetectionSystemLimitation NGSI-v2 키값 예시  
다음은 키 값으로 JSON-LD 형식의 FrenchTrainDetectionSystemLimitation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": "2014-09-23T15:45:27Z",  
  "dateModified": "1995-12-08T08:26:38Z",  
  "source": "Including since ",  
  "name": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure.",  
  "alternateName": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist",  
  "description": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military.",  
  "dataProvider": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science.",  
  "owner": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -21.934426,  
      6.101443  
    ]  
  },  
  "address": {  
    "streetAddress": "Wonder majority ability. Forget throughout discussion cost. Dream store case number.",  
    "addressLocality": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain.",  
    "addressRegion": "Lot watch matter. Item station",  
    "addressCountry": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill.",  
    "postalCode": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker.",  
    "postOfficeBoxNumber": "Near bed always benefit fine popular economic. Ever material save after scientist.",  
    "streetNr": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit",  
    "district": "Open administration space ahead. Soci"  
  },  
  "areaServed": "Including international kind animal customer. Identify large me. Field deal ",  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": false,  
  "frenchTrainDetectionSystemLimitationNumber": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183"  
}  
```  
</details>  
#### FrenchTrainDetectionSystemLimitation NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 FrenchTrainDetectionSystemLimitation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2014-09-23T15:45:27Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1995-12-08T08:26:38Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Including since "  
  },  
  "name": {  
    "type": "Text",  
    "value": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -21.934426,  
          6.101443  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Wonder majority ability. Forget throughout discussion cost. Dream store case number."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Lot watch matter. Item station"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Near bed always benefit fine popular economic. Ever material save after scientist."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Open administration space ahead. Soci"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Including international kind animal customer. Identify large me. Field deal "  
  },  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": {  
    "type": "Boolean",  
    "value": false  
  },  
  "frenchTrainDetectionSystemLimitationNumber": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183"  
  }  
}  
```  
</details>  
#### FrenchTrainDetectionSystemLimitation NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 FrenchTrainDetectionSystemLimitation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": "2014-09-23T15:45:27Z",  
  "dateModified": "1995-12-08T08:26:38Z",  
  "source": "Including since ",  
  "name": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure.",  
  "alternateName": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist",  
  "description": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military.",  
  "dataProvider": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science.",  
  "owner": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -21.934426,  
      6.101443  
    ]  
  },  
  "address": {  
    "streetAddress": "Wonder majority ability. Forget throughout discussion cost. Dream store case number.",  
    "addressLocality": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain.",  
    "addressRegion": "Lot watch matter. Item station",  
    "addressCountry": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill.",  
    "postalCode": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker.",  
    "postOfficeBoxNumber": "Near bed always benefit fine popular economic. Ever material save after scientist.",  
    "streetNr": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit",  
    "district": "Open administration space ahead. Soci"  
  },  
  "areaServed": "Including international kind animal customer. Identify large me. Field deal ",  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": false,  
  "frenchTrainDetectionSystemLimitationNumber": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### FrenchTrainDetectionSystemLimitation NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 FrenchTrainDetectionSystemLimitation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:MUMN:30355615",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-12-11T22:05:23Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-08-04T09:15:57Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Vote middle customer. Know account build. Son garden image support TV"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Kid behavior decision century. Accept father hand hundred order. Space enjoy store radio office enter cover."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pretty four year people. Message mother action recently catch."  
  },  
  "description": {  
    "type": "Property",  
    "value": "National "  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Able involve move contain who director improve speak. Inc"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:OCPM:47545823",  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:YYEI:53415372"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:FKOO:81839190"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -78.20408,  
        125.044799  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Term ",  
      "addressLocality": "Return nature nothing soon democratic in. Time reach name mother pretty. Alone blue treatment together herself sound change painting.",  
      "addressRegion": "Always century cut do accept team despite. Region prevent save over degree. Nice each happen month away card.",  
      "addressCountry": "Land wife history method service they teach. Herself place movement throw discussion father. Nearly talk officer ok.",  
      "postalCode": "Difference less money reason final individual raise. Stay under car interesting check north policy. Purpose face worker apply surface.",  
      "postOfficeBoxNumber": "Baby possible guy set. Road style project hundred of its. Wife film g",  
      "streetNr": "Early star vote stor",  
      "district": "Idea buy concern relate se"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Image agent star total civil. Because a"  
  },  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": {  
    "type": "Property",  
    "value": false  
  },  
  "frenchTrainDetectionSystemLimitationNumber": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:FWCD:62453633"  
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

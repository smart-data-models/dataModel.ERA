<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: MaximumMagneticField  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/MaximumMagneticField/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **정의된 주파수 대역에 대해 액슬 카운터에 허용되는 최대 자기장 제한(dBµA/m)입니다.  
3방향으로 제공되어야 합니다.**  
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
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maximumMagneticFieldDirectionX[number]`: 최대 자기장 방향 X  - `maximumMagneticFieldDirectionY[number]`: 최대 자기장 방향 Y  - `maximumMagneticFieldDirectionZ[number]`: 최대 자기장 방향 Z  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 데이터 유형입니다. MaximumMagneticField여야 합니다.  <!-- /30-PropertiesList -->  
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
MaximumMagneticField:    
  description: |-    
    The maximum magnetic field limits allowed for axle counters (in dBµA/m) for a defined frequency band.    
    It should be provided in 3 directions.    
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
    maximumMagneticFieldDirectionX:    
      description: Maximum magnetic field direction X    
      type: number    
      x-ngsi:    
        type: Property    
    maximumMagneticFieldDirectionY:    
      description: Maximum magnetic field direction Y    
      type: number    
      x-ngsi:    
        type: Property    
    maximumMagneticFieldDirectionZ:    
      description: Maximum magnetic field direction Z    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI data type. It has to be MaximumMagneticField    
      enum:    
        - MaximumMagneticField    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/MaximumMagneticField    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/MaximumMagneticField/LICENSE.md    
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
#### MaximumMagneticField NGSI-v2 키값 예시  
다음은 키 값으로 JSON-LD 형식의 MaximumMagneticField의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": "1992-07-01T01:29:02Z",  
  "dateModified": "2022-07-21T07:13:50Z",  
  "source": "Method modern phone whatever thing. Discussion example your dog fund serv",  
  "name": "Nothing church tonight church do",  
  "alternateName": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve.",  
  "description": "Difficu",  
  "dataProvider": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r",  
  "owner": [  
    "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
    "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      12.1959295,  
      -80.960856  
    ]  
  },  
  "address": {  
    "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
    "addressLocality": "Region may realize sign my. Wester",  
    "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
    "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
    "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
    "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
    "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
    "district": "Allow site finally evidence green."  
  },  
  "areaServed": "Employee they catch fight suggest. Executive positive eight piece.",  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": 864,  
  "maximumMagneticFieldDirectionY": 864,  
  "maximumMagneticFieldDirectionZ": 864,  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MaximumMagneticField NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 MaximumMagneticField의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1992-07-01T01:29:02Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2022-07-21T07:13:50Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Method modern phone whatever thing. Discussion example your dog fund serv"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Nothing church tonight church do"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Difficu"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
      "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          12.1959295,  
          -80.960856  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Number nature rock important pull. Much concern up certainly p"  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Region may realize sign my. Wester"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Project resource recent require bank sell. Similar finish audience end."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Experience institution case officer. Window section area information. College or sport charge remember thing give."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Season check including hard light skill. Firm town nice. Letter"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Series baby such probably cell court. Pretty value still sit chance party. Dra"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Allow site finally evidence green."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Employee they catch fight suggest. Executive positive eight piece."  
  },  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumMagneticFieldDirectionY": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumMagneticFieldDirectionZ": {  
    "type": "Number",  
    "value": 864  
  },  
  "context": {  
    "type": "StructuredValue",  
    "value": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
    ]  
  }  
}  
```  
</details>  
#### MaximumMagneticField NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 MaximumMagneticField의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": "1992-07-01T01:29:02Z",  
  "dateModified": "2022-07-21T07:13:50Z",  
  "source": "Method modern phone whatever thing. Discussion example your dog fund serv",  
  "name": "Nothing church tonight church do",  
  "alternateName": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve.",  
  "description": "Difficu",  
  "dataProvider": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r",  
  "owner": [  
    "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
    "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      12.1959295,  
      -80.960856  
    ]  
  },  
  "address": {  
    "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
    "addressLocality": "Region may realize sign my. Wester",  
    "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
    "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
    "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
    "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
    "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
    "district": "Allow site finally evidence green."  
  },  
  "areaServed": "Employee they catch fight suggest. Executive positive eight piece.",  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": 864,  
  "maximumMagneticFieldDirectionY": 864,  
  "maximumMagneticFieldDirectionZ": 864,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MaximumMagneticField NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 MaximumMagneticField의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:XYSL:59916457",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-01-17T00:20:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1971-04-03T19:24:25Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Seek material four bed eat foot four cut. Industry medical human yet collection."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Everyone safe interesting eat. Again might live manager. Surf"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Here people p"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Activity treat its in. Also step board might truth small interesting."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Article care radio win program responsibility water. South expect yard past most team. Raise population since meet between set."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:QGWL:53478074",  
      "urn:ngsi-ld:MaximumMagneticField:items:IBUO:48085735"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:XXHU:41714471"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.077867,  
        60.671442  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "West trial language field. Stock high senior success go whole.",  
      "addressLocality": "Community catch mission perhaps especially option degree. Create option part not return draw identify art. Success relate series according.",  
      "addressRegion": "List successful a during loss nor. Conference hit well far f",  
      "addressCountry": "Our seem scientist. Hot group true design season crime. Far safe miss doctor.",  
      "postalCode": "Interesting top success try.",  
      "postOfficeBoxNumber": "Huge foot truth ball. ",  
      "streetNr": "Land need cold question.",  
      "district": "Throughout way floor believe movie. Off police in begin. Whatever heart half or already window."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Say already life discuss determine heart. Edge someone parent all her down."  
  },  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": {  
    "type": "Property",  
    "value": 671  
  },  
  "maximumMagneticFieldDirectionY": {  
    "type": "Property",  
    "value": 707  
  },  
  "maximumMagneticFieldDirectionZ": {  
    "type": "Property",  
    "value": 262  
  },  
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

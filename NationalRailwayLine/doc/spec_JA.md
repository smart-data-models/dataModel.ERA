<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ国鉄  
========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ERA/blob/master/NationalRailwayLine/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**加盟国内の鉄道路線。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIデータ型。NationalRailwayLineでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
ERAオントロジー https://data-interop.era.europa.eu/era-vocabulary （欧州鉄道庁）からマッピングされたデータモデル。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
NationalRailwayLine:    
  description: Railway line within a member state.    
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
      description: NGSI data type. It has to be NationalRailwayLine    
      enum:    
        - NationalRailwayLine    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/NationalRailwayLine    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/NationalRailwayLine/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json    
  x-model-tags: 'ERA vocabulary, railway, train'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### NationalRailwayLine NGSI-v2 キー値の例  
以下はNationalRailwayLineをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NationalRailwayLine:id:KZJH:10519466",  
  "dateCreated": "1981-02-03T19:54:38Z",  
  "dateModified": "2001-03-07T16:57:56Z",  
  "source": "Choice west system production forget anyone. Your science middle oil sister plant those.",  
  "name": "Fill pull pick week anyone skill. Project of know.",  
  "alternateName": "Size somebody piece rock real expert effort preve",  
  "description": "Military knowledge name item put tend.",  
  "dataProvider": "Feeling student building national himself month. Become scientist d",  
  "owner": [  
    "urn:ngsi-ld:NationalRailwayLine:items:BIHG:50369174",  
    "urn:ngsi-ld:NationalRailwayLine:items:ABIO:72697824"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NationalRailwayLine:items:PPCV:02276202"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      70.8382295,  
      -178.994614  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "History meet factor country special rise. Like more my.",  
    "addressRegion": "When available trial pick Mr quite mind worry. Each model prepare different yet.",  
    "addressCountry": "Character name key lay society. My understand day interview evidence purpose.",  
    "postalCode": "Produce open safe imagine voice offer pick. Carry consider culture standard nice particularly across miss. Mean why ev",  
    "postOfficeBoxNumber": "Suddenly growth des",  
    "streetNr": "Surface answer oil yourself create. Cup Republican set during standard reveal need measure.",  
    "district": "Sure clearly in city defense send. Medical daughter issue soldier behind production protect. Because score very hold cause law."  
  },  
  "areaServed": "Candidate house speak sort computer move reduce break. Right safe make eve",  
  "type": "NationalRailwayLine",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### NationalRailwayLine NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のNationalRailwayLineの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NationalRailwayLine:id:KZJH:10519466",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1981-02-03T19:54:38Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2001-03-07T16:57:56Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Choice west system production forget anyone. Your science middle oil sister plant those."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Fill pull pick week anyone skill. Project of know."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Size somebody piece rock real expert effort preve"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Military knowledge name item put tend."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Feeling student building national himself month. Become scientist d"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NationalRailwayLine:items:BIHG:50369174",  
      "urn:ngsi-ld:NationalRailwayLine:items:ABIO:72697824"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NationalRailwayLine:items:PPCV:02276202"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          70.8382295,  
          -178.994614  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": ""  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "History meet factor country special rise. Like more my."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "When available trial pick Mr quite mind worry. Each model prepare different yet."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Character name key lay society. My understand day interview evidence purpose."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Produce open safe imagine voice offer pick. Carry consider culture standard nice particularly across miss. Mean why ev"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Suddenly growth des"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Surface answer oil yourself create. Cup Republican set during standard reveal need measure."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Sure clearly in city defense send. Medical daughter issue soldier behind production protect. Because score very hold cause law."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Candidate house speak sort computer move reduce break. Right safe make eve"  
  },  
  "type": "NationalRailwayLine",  
  "context": {  
    "type": "StructuredValue",  
    "value": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
    ]  
  }  
}  
```  
</details>  
#### NationalRailwayLine NGSI-LD キー値の例  
以下はNationalRailwayLineをJSON-LD形式でkey-valuesとした例である。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NationalRailwayLine:id:KZJH:10519466",  
  "dateCreated": "1981-02-03T19:54:38Z",  
  "dateModified": "2001-03-07T16:57:56Z",  
  "source": "Choice west system production forget anyone. Your science middle oil sister plant those.",  
  "name": "Fill pull pick week anyone skill. Project of know.",  
  "alternateName": "Size somebody piece rock real expert effort preve",  
  "description": "Military knowledge name item put tend.",  
  "dataProvider": "Feeling student building national himself month. Become scientist d",  
  "owner": [  
    "urn:ngsi-ld:NationalRailwayLine:items:BIHG:50369174",  
    "urn:ngsi-ld:NationalRailwayLine:items:ABIO:72697824"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NationalRailwayLine:items:PPCV:02276202"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      70.8382295,  
      -178.994614  
    ]  
  },  
  "address": {  
    "streetAddress": "",  
    "addressLocality": "History meet factor country special rise. Like more my.",  
    "addressRegion": "When available trial pick Mr quite mind worry. Each model prepare different yet.",  
    "addressCountry": "Character name key lay society. My understand day interview evidence purpose.",  
    "postalCode": "Produce open safe imagine voice offer pick. Carry consider culture standard nice particularly across miss. Mean why ev",  
    "postOfficeBoxNumber": "Suddenly growth des",  
    "streetNr": "Surface answer oil yourself create. Cup Republican set during standard reveal need measure.",  
    "district": "Sure clearly in city defense send. Medical daughter issue soldier behind production protect. Because score very hold cause law."  
  },  
  "areaServed": "Candidate house speak sort computer move reduce break. Right safe make eve",  
  "type": "NationalRailwayLine",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### NationalRailwayLine NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のNationalRailwayLineの例です。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:NationalRailwayLine:id:CKZB:48186291",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1998-09-11T18:25:59Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1976-08-09T00:01:04Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Exist my economy window together address establish. Instead feeling "  
  },  
  "name": {  
    "type": "Property",  
    "value": "Treatment own thus sometimes. War share whether. Worker fast appear of tree live book."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Figure camera something. Bed minute remain own prepare none evidence. Manage who bed suffer."  
  },  
  "description": {  
    "type": "Property",  
    "value": "So among fill article decision hit. Never maybe reduce individual mission describe."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Into short fire newspaper sign assume collection. Eat data dr"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NationalRailwayLine:items:RKLK:30981211",  
      "urn:ngsi-ld:NationalRailwayLine:items:ESOM:17099202"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NationalRailwayLine:items:RYKV:77061744"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        85.288372,  
        156.213606  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Friend into police civil. Up control soldier program. Space Mr song green yes run.",  
      "addressLocality": "Democratic political player side call. President sense help full. Respond day claim.",  
      "addressRegion": "Majority science than. Your almost bag meeting image signifi",  
      "addressCountry": "Even rock agree. First training student know ability. Worry control determine bad sport bank dark.",  
      "postalCode": "Enter level Democrat. Popular nature six whatever. College affect stand feeling read she forward from.",  
      "postOfficeBoxNumber": "Test change social agent. President card grow ",  
      "streetNr": "Option middle role popular. Record certainly call southern defense simply.",  
      "district": "Rock hot personal ga"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Forget direction bar. Up behavior institution wonder put story PM. Main defense follow continue. Art far hear hersel"  
  },  
  "type": "NationalRailwayLine",  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

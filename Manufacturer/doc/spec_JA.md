<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティメーカー  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ERA/blob/master/Manufacturer/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**自動車を製造する会社または組織。  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIデータ型。これは製造業者でなければならない。  <!-- /30-PropertiesList -->  
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
Manufacturer:    
  description: A company or organization that manufactures vehicles.    
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
      description: NGSI data type. It has to be Manufacturer    
      enum:    
        - Manufacturer    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Manufacturer    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Manufacturer/LICENSE.md    
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
#### メーカー NGSI-v2 キー値 例  
JSON-LD形式のManufacturerのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:VOTT:26597132",  
  "dateCreated": "1999-05-25T21:10:20Z",  
  "dateModified": "1981-08-05T14:31:51Z",  
  "source": "Each low class pretty ball. Heavy Mrs only strategy. Like reduce man security.",  
  "name": "Six store sor",  
  "alternateName": "Expert maintain actually goal. Bank cul",  
  "description": "Wha",  
  "dataProvider": "Market small also far they measure consumer.",  
  "owner": [  
    "urn:ngsi-ld:Manufacturer:items:HBYI:32485482",  
    "urn:ngsi-ld:Manufacturer:items:OBGX:52905874"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Manufacturer:items:UMRJ:07396067"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -7.7970405,  
      -90.393951  
    ]  
  },  
  "address": {  
    "streetAddress": "Goal feel cultural race officer. Future table pay. Grow letter though all type century ",  
    "addressLocality": "Shoulder hold leader hospital since sometimes.",  
    "addressRegion": "Type attorney chance father adult raise. Society author probably.",  
    "addressCountry": "Minute tax really road six.",  
    "postalCode": "Anything wife easy maintain. Hair budget sea significant. Particularly weight anything three feel second.",  
    "postOfficeBoxNumber": "Speech Democrat most life fine my.",  
    "streetNr": "Age court anyone less your. Wear camera responsibility ski",  
    "district": "Involve mention her pr"  
  },  
  "areaServed": "By there since Congress themselves girl everyone. Nature grow important yes.",  
  "type": "Manufacturer"  
}  
```  
</details>  
#### メーカー NGSI-v2 正規化例  
以下は、正規化されたJSON-LDフォーマットのManufacturerの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:VOTT:26597132",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1999-05-25T21:10:20Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1981-08-05T14:31:51Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Each low class pretty ball. Heavy Mrs only strategy. Like reduce man security."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Six store sor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Expert maintain actually goal. Bank cul"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Wha"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Market small also far they measure consumer."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:HBYI:32485482",  
      "urn:ngsi-ld:Manufacturer:items:OBGX:52905874"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:UMRJ:07396067"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -7.7970405,  
          -90.393951  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Goal feel cultural race officer. Future table pay. Grow letter though all type century "  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Shoulder hold leader hospital since sometimes."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Type attorney chance father adult raise. Society author probably."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Minute tax really road six."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Anything wife easy maintain. Hair budget sea significant. Particularly weight anything three feel second."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Speech Democrat most life fine my."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Age court anyone less your. Wear camera responsibility ski"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Involve mention her pr"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "By there since Congress themselves girl everyone. Nature grow important yes."  
  },  
  "type": "Manufacturer"  
}  
```  
</details>  
#### メーカー NGSI-LD キー値 例  
以下は、JSON-LDフォーマットのManufacturerをkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:VOTT:26597132",  
  "dateCreated": "1999-05-25T21:10:20Z",  
  "dateModified": "1981-08-05T14:31:51Z",  
  "source": "Each low class pretty ball. Heavy Mrs only strategy. Like reduce man security.",  
  "name": "Six store sor",  
  "alternateName": "Expert maintain actually goal. Bank cul",  
  "description": "Wha",  
  "dataProvider": "Market small also far they measure consumer.",  
  "owner": [  
    "urn:ngsi-ld:Manufacturer:items:HBYI:32485482",  
    "urn:ngsi-ld:Manufacturer:items:OBGX:52905874"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Manufacturer:items:UMRJ:07396067"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -7.7970405,  
      -90.393951  
    ]  
  },  
  "address": {  
    "streetAddress": "Goal feel cultural race officer. Future table pay. Grow letter though all type century ",  
    "addressLocality": "Shoulder hold leader hospital since sometimes.",  
    "addressRegion": "Type attorney chance father adult raise. Society author probably.",  
    "addressCountry": "Minute tax really road six.",  
    "postalCode": "Anything wife easy maintain. Hair budget sea significant. Particularly weight anything three feel second.",  
    "postOfficeBoxNumber": "Speech Democrat most life fine my.",  
    "streetNr": "Age court anyone less your. Wear camera responsibility ski",  
    "district": "Involve mention her pr"  
  },  
  "areaServed": "By there since Congress themselves girl everyone. Nature grow important yes.",  
  "type": "Manufacturer",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### メーカー NGSI-LD 正規化例  
以下は、正規化されたJSON-LDフォーマットのManufacturerの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:YVMH:41957963",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-03-24T09:32:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1988-09-15T15:09:48Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "With human sound stock. Hundred note morning then compare process music red. Describe as try organization light high."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Newspaper huge dinner later. Wide democratic near product loss. Live own way employee local exactly far. Defense day benefit out."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Goal bl"  
  },  
  "description": {  
    "type": "Property",  
    "value": "History agency occur drop. Consider cold any defense nice cause. Study spring company step."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Prevent knowledge station turn modern energy. Hundred ok morn"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:OYJB:95943841",  
      "urn:ngsi-ld:Manufacturer:items:KFIM:77965610"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:MEPT:90382167"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -29.2915185,  
        -116.219785  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Unit anything much kind attorney. A huge talk receive.",  
      "addressLocality": "Sign operation moment establish laugh. Everybody skill where catch theory. Child later some pretty military.",  
      "addressRegion": "See him total language know. Audience discover responsibility young experience.",  
      "addressCountry": "Through situation laugh others energy particu",  
      "postalCode": "Top firm service. Program system skin should may for police.",  
      "postOfficeBoxNumber": "Well look firm option prepare education. Teacher police turn Democrat.",  
      "streetNr": "Feeling glass century hotel fire which. Old on necessary style article technology know. Air return health method.",  
      "district": "Ability garden behavior keep exactly. Clearly treat type expect bed near."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Real purpose memory rule. Economy responsibility building rather. Project glass throughout final oil specific."  
  },  
  "type": "Manufacturer",  
  "@context": [  
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

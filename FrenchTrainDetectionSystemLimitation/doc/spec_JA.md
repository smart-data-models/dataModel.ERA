<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティフランス列車検知システム制限  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**フランスのネットワークにおけるルートの互換性チェックに特化しています。以下の区間：  
-1 トラックあたりの流通トン数が15000トン／日／トラック未満である。  
-2 方向インターロック  
-3 方向連動に 45 秒の遅延がある。  
-4 軌道回路アナウンスの設置  
-5 非可逆複線路線の場合、通常の循環方向に分流補助ペダルがないこと。  
-6 単線および対面通行の線路では、循環方向に関係なく迂回補助ペダルがない。  
-7 ペダルアナウンス機構がないこと。  
-8 特定アナウンス・リセット装置**の45秒遅れ  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `frenchTrainDetectionSystemLimitationApplicable[boolean]`: 列車検出制限のあるセクションは、フランスのネットワークにのみ適用される。  - `frenchTrainDetectionSystemLimitationNumber[uri]`: 列車検知制限番号のあるセクション（フランスのネットワークのみ  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIデータ型。FrenchTrainDetectionSystemLimitationでなければならない。  <!-- /30-PropertiesList -->  
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
## ペイロードの例  
#### NGSI-v2 キー値の例  
FrenchTrainDetectionSystemLimitationをJSON-LD形式でkey-valuesとした例です。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### FrenchTrainDetectionSystemLimitation NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の FrenchTrainDetectionSystemLimitation の例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### NGSI-LD キー値の例  
FrenchTrainDetectionSystemLimitationをJSON-LD形式でkey-valuesとした例です。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### フランス列車検知システム制限 NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の FrenchTrainDetectionSystemLimitation の例です。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

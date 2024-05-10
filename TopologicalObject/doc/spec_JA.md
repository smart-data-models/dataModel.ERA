<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

エンティティTopologicalObject    
=======================
<!-- /10-Header -->
    
<!-- 15-License -->
    

[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ERA/blob/master/TopologicalObject/LICENSE.md)    

[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

グローバルな記述：**トポロジカルノードエッジモデルとして記述されるトラックネットワークのトップレベルクラス**。    

バージョン: 0.0.1    
<!-- /20-Description -->
    
<!-- 30-PropertiesList -->
    

## プロパティのリスト    

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 公道上の特定の物件を特定する番号      
- `alternateName[string]`: この項目の別名  
- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  
- `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  
- `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  
- `description[string]`: この商品の説明  
- `id[*]`: エンティティの一意識別子  
- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  
- `name[string]`: このアイテムの名前  
- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  
- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  
- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  
- `type[string]`: NGSI データ型。TopologicalObjectでなければならない。  
<!-- /30-PropertiesList -->
    
<!-- 35-RequiredProperties -->
    

必須プロパティ    
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
    
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
TopologicalObject:      
  description: Top level class for the the track network described as a topological node edge model      
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
      description: NGSI data type. It has to be TopologicalObject      
      enum:      
        - TopologicalObject      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/TopologicalObject      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/TopologicalObject/LICENSE.md      
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

#### TopologicalObject NGSI-v2 キー値の例    

JSON-LD形式のTopologicalObjectのkey-valuesの例である。options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:TopologicalObject:id:MDTE:29122911",  
  "dateCreated": "1997-12-28T14:44:16Z",  
  "dateModified": "1986-06-03T02:06:03Z",  
  "source": "Race box market story. Father establish himself everyone",  
  "name": "Least chair pull serve specific expect modern. Debate end difficult wife. Player various popular southern believe amount lot method.",  
  "alternateName": "Address happy television wide bu",  
  "description": "Finish then evidence just. Book hundred kind model opportunity. Always pattern class oil soldier conference involve.",  
  "dataProvider": "Room affect someone need manager. Range represent compare reality beat.",  
  "owner": [  
    "urn:ngsi-ld:TopologicalObject:items:HQJL:52681721",  
    "urn:ngsi-ld:TopologicalObject:items:RKZS:06098455"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TopologicalObject:items:DCVU:82796661"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -6.809152,  
      70.994051  
    ]  
  },  
  "address": {  
    "streetAddress": "Them generation story painting economy hair their. Keep together among she.",  
    "addressLocality": "Charge win great only.",  
    "addressRegion": "Popular thank would represent course. Just image represent decision parent. Degree west lay gar",  
    "addressCountry": "Health history lose defense. About husband market student short cost green. Morning poor example alre",  
    "postalCode": "Ready course edge author. Century once lead approach after.",  
    "postOfficeBoxNumber": "Dream now federal nice. Fish give entire home detail against.",  
    "streetNr": "Turn become hotel game ",  
    "district": "Cover whole pay customer management approach theory."  
  },  
  "areaServed": "Partner a improve about. Because four challenge. Hot north personal benefit.",  
  "type": "TopologicalObject"
}  
```  
</details>    

#### トポロジカルオブジェクト NGSI-v2 正規化例    

以下は、正規化された JSON-LD 形式の TopologicalObject の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:TopologicalObject:id:MDTE:29122911",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1997-12-28T14:44:16Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1986-06-03T02:06:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Race box market story. Father establish himself everyone"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Least chair pull serve specific expect modern. Debate end difficult wife. Player various popular southern believe amount lot method."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Address happy television wide bu"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Finish then evidence just. Book hundred kind model opportunity. Always pattern class oil soldier conference involve."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Room affect someone need manager. Range represent compare reality beat."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:HQJL:52681721",  
      "urn:ngsi-ld:TopologicalObject:items:RKZS:06098455"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:DCVU:82796661"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.809152,  
        70.994051  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Them generation story painting economy hair their. Keep together among she.",  
      "addressLocality": "Charge win great only.",  
      "addressRegion": "Popular thank would represent course. Just image represent decision parent. Degree west lay gar",  
      "addressCountry": "Health history lose defense. About husband market student short cost green. Morning poor example alre",  
      "postalCode": "Ready course edge author. Century once lead approach after.",  
      "postOfficeBoxNumber": "Dream now federal nice. Fish give entire home detail against.",  
      "streetNr": "Turn become hotel game ",  
      "district": "Cover whole pay customer management approach theory."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Partner a improve about. Because four challenge. Hot north personal benefit."  
  },  
  "type": "TopologicalObject"  
}  
```  
</details>    

#### TopologicalObject NGSI-LD キー値の例    

TopologicalObjectをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:TopologicalObject:id:MDTE:29122911",  
  "dateCreated": "1997-12-28T14:44:16Z",  
  "dateModified": "1986-06-03T02:06:03Z",  
  "source": "Race box market story. Father establish himself everyone",  
  "name": "Least chair pull serve specific expect modern. Debate end difficult wife. Player various popular southern believe amount lot method.",  
  "alternateName": "Address happy television wide bu",  
  "description": "Finish then evidence just. Book hundred kind model opportunity. Always pattern class oil soldier conference involve.",  
  "dataProvider": "Room affect someone need manager. Range represent compare reality beat.",  
  "owner": [  
    "urn:ngsi-ld:TopologicalObject:items:HQJL:52681721",  
    "urn:ngsi-ld:TopologicalObject:items:RKZS:06098455"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TopologicalObject:items:DCVU:82796661"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -6.809152,  
      70.994051  
    ]  
  },  
  "address": {  
    "streetAddress": "Them generation story painting economy hair their. Keep together among she.",  
    "addressLocality": "Charge win great only.",  
    "addressRegion": "Popular thank would represent course. Just image represent decision parent. Degree west lay gar",  
    "addressCountry": "Health history lose defense. About husband market student short cost green. Morning poor example alre",  
    "postalCode": "Ready course edge author. Century once lead approach after.",  
    "postOfficeBoxNumber": "Dream now federal nice. Fish give entire home detail against.",  
    "streetNr": "Turn become hotel game ",  
    "district": "Cover whole pay customer management approach theory."  
  },  
  "areaServed": "Partner a improve about. Because four challenge. Hot north personal benefit.",  
  "type": "TopologicalObject",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### トポロジカルオブジェクト NGSI-LD 正規化例    

以下は、正規化された JSON-LD 形式の TopologicalObject の例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:TopologicalObject:id:ANPE:97919193",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-09-17T09:21:53Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1996-07-18T12:43:19Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Yes serve free seat. Room including each yard walk attack."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Actually large man expect eye voic"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Season area fill station news stop. Choice marriage"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Guy remain them seven general. Worker term address. Education detail not share human win item."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Current treatment sing. Hour bed song all tend success fine. Develop guy if them interest high bed. Strong certain say offer i"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:HBZC:96164619",  
      "urn:ngsi-ld:TopologicalObject:items:SZBJ:87847721"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:VWRI:32992685"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        0.125705,  
        0.810063  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Building out then when gas address face. Increase tele",  
      "addressLocality": "Also house growth leave now food information. Management across tree factor Republican.",  
      "addressRegion": "F",  
      "addressCountry": "Score him say majority drug catch figure however. Eat condition subject least. Purpose guess such quickly management wear ",  
      "postalCode": "Southe",  
      "postOfficeBoxNumber": "Fear surface but effect. Sing structure growth with personal western.",  
      "streetNr": "Window down clear window describe hand determine. Talk bill thousand lay recognize. Customer trip place really poor after ene",  
      "district": "Family opportunity leg industry theory smile image. Into "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Hear her year population be."  
  },  
  "type": "TopologicalObject",  
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
    

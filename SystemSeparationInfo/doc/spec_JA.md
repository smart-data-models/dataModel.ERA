<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

エンティティシステム分離情報    
==============
<!-- /10-Header -->
    
<!-- 15-License -->
    

[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ERA/blob/master/SystemSeparationInfo/LICENSE.md)    

[文書が自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

グローバルな記述：**システム分離に必要ないくつかの情報の表示。    

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
- `systemSeparationInfoChangeSupplySystem[string]`: システム分離情報変更供給システム  
- `systemSeparationInfoLength[number]`: システム分離情報の長さ  
- `systemSeparationInfoPantographLowered[boolean]`: システム分離情報 パンタグラフを下げる  
- `systemSeparationInfoSwitchOffBreaker[boolean]`: ブレーカーをオフにするシステム分離情報  
- `type[string]`: NGSI データ型。SystemSeparationInfo でなければならない。  
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
SystemSeparationInfo:      
  description: Indication of required several information on system separation.      
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
    systemSeparationInfoChangeSupplySystem:      
      description: System separation info change supply system      
      type: string      
      x-ngsi:      
        type: Property      
    systemSeparationInfoLength:      
      description: System separation info length      
      type: number      
      x-ngsi:      
        type: Property      
    systemSeparationInfoPantographLowered:      
      description: System separation info  pantograph lowered      
      type: boolean      
      x-ngsi:      
        type: Property      
    systemSeparationInfoSwitchOffBreaker:      
      description: System separation info switch off breaker      
      type: boolean      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be SystemSeparationInfo      
      enum:      
        - SystemSeparationInfo      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/SystemSeparationInfo      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SystemSeparationInfo/LICENSE.md      
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

#### SystemSeparationInfo NGSI-v2 キー値の例    

以下は、SystemSeparationInfoをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": "1971-06-11T11:02:58Z",  
  "dateModified": "1981-04-17T22:16:45Z",  
  "source": "Quickly final probably box society with. View woman main analysis. Think region why best with.",  
  "name": "Treat inside expect figure. Animal ago television visit late.",  
  "alternateName": "Under feel opportunity next win",  
  "description": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro",  
  "dataProvider": "Drive read poor policy. Try quality report safe. Yard reason continue wide.",  
  "owner": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
    "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.1257535,  
      35.88905  
    ]  
  },  
  "address": {  
    "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
    "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
    "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
    "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
    "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
    "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
    "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
    "district": "Forget memory specific own fast p"  
  },  
  "areaServed": "Understand him visit certain task. Bar staff use but.",  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess.",  
  "systemSeparationInfoLength": 864,  
  "systemSeparationInfoPantographLowered": false,  
  "systemSeparationInfoSwitchOffBreaker": false
}  
```  
</details>    

#### SystemSeparationInfo NGSI-v2 正規化例    

以下は、正規化された JSON-LD 形式の SystemSeparationInfo の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1971-06-11T11:02:58Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1981-04-17T22:16:45Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Quickly final probably box society with. View woman main analysis. Think region why best with."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Treat inside expect figure. Animal ago television visit late."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Under feel opportunity next win"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Drive read poor policy. Try quality report safe. Yard reason continue wide."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
      "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        37.1257535,  
        35.88905  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
      "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
      "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
      "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
      "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
      "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
      "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
      "district": "Forget memory specific own fast p"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Understand him visit certain task. Bar staff use but."  
  },  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": {  
    "type": "Text",  
    "value": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess."  
  },  
  "systemSeparationInfoLength": {  
    "type": "Number",  
    "value": 864  
  },  
  "systemSeparationInfoPantographLowered": {  
    "type": "Boolean",  
    "value": false  
  },  
  "systemSeparationInfoSwitchOffBreaker": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>    

#### SystemSeparationInfo NGSI-LD キー値の例    

以下は、SystemSeparationInfoをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": "1971-06-11T11:02:58Z",  
  "dateModified": "1981-04-17T22:16:45Z",  
  "source": "Quickly final probably box society with. View woman main analysis. Think region why best with.",  
  "name": "Treat inside expect figure. Animal ago television visit late.",  
  "alternateName": "Under feel opportunity next win",  
  "description": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro",  
  "dataProvider": "Drive read poor policy. Try quality report safe. Yard reason continue wide.",  
  "owner": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
    "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.1257535,  
      35.88905  
    ]  
  },  
  "address": {  
    "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
    "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
    "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
    "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
    "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
    "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
    "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
    "district": "Forget memory specific own fast p"  
  },  
  "areaServed": "Understand him visit certain task. Bar staff use but.",  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess.",  
  "systemSeparationInfoLength": 864,  
  "systemSeparationInfoPantographLowered": false,  
  "systemSeparationInfoSwitchOffBreaker": false,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### SystemSeparationInfo NGSI-LD 正規化例    

以下は、正規化された JSON-LD 形式の SystemSeparationInfo の例である。これは、オプションを使用しない場合の NGSI-LD と互換性があり、個々のエンティティのコンテキスト・データを返します。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:XYDV:99228074",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1990-08-14T02:23:40Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2005-06-05T23:14:26Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Stuff kind likely de"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Story pay cover hot which. Day difference floor make husband say. Through break ok daughter."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Scientist maintain feel baby inte"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Might new take. Month detail matter moment here current. Rock sign number. "  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Always speak able break billion requ"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:KLAD:01706991",  
      "urn:ngsi-ld:SystemSeparationInfo:items:OUMR:57506132"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:FZOT:63378927"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -75.5485445,  
        77.256275  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Environmental stage comme",  
      "addressLocality": "Go under experience nor. Defense skill make product.",  
      "addressRegion": "Scientist letter artis",  
      "addressCountry": "Close born subject among water. Hear computer quest",  
      "postalCode": "Until along talk long. Keep support prepare direction reveal national. Effect few institution inside avoid. In hundred gun result clearly.",  
      "postOfficeBoxNumber": "Do account nothing executive ground. Brother put all often recognize method. Surface red three front su",  
      "streetNr": "Beautiful hotel necessary college risk baby. Stop wish either everyone. E",  
      "district": "Impact treatment follow leader. "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Push film partner. Soon themselves guy expert however."  
  },  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": {  
    "type": "Property",  
    "value": "Age ten church not. Edge"  
  },  
  "systemSeparationInfoLength": {  
    "type": "Property",  
    "value": 735  
  },  
  "systemSeparationInfoPantographLowered": {  
    "type": "Property",  
    "value": false  
  },  
  "systemSeparationInfoSwitchOffBreaker": {  
    "type": "Property",  
    "value": true  
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
    

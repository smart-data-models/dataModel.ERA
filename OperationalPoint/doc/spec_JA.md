<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティオペレーショナルポイント  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ERA/blob/master/OperationalPoint/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述：**運行地点（OP）とは、列車の運行が開始され、終了され、または経路が変更され、旅客または貨 物のサービスが提供される、列車運行のためのあらゆる場所を意味する。  
https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.2 主要地点（駅、操車場、分岐点、貨物ターミナル）において**。  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `borderPointOf[uri]`: の国境点  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `digitalSchematicOverview[string]`: デジタル回路図の概要  - `hasSchematicOverviewOPDigitalForm[boolean]`: デジタル形式の回路図  - `id[*]`: エンティティの一意識別子  - `localRulesOrRestrictions[boolean]`: 厳密に地域的な性質の規則や制限の存在。  - `localRulesOrRestrictionsDoc[string]`: IMが入手できる、厳密にローカルな性質の規則または制限に関する文書  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `opInfoPerCountry[uri]`: 国ごとの国境ポイント情報  - `opName[string]`: 運用ポイント名  - `opType[uri]`: 運用ポイントの種類  - `opTypeGaugeChangeover[string]`: 軌道軌間切替設備の種類  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `schematicOverviewOP[string]`: 作戦ポイントの概略  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `siding[uri]`: サイディング  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `tafTAPCode[string]`: テレマティクス・アプリケーションに関連する TSI に基づき、情報交換のために開発された一次 位置コード。  - `track[uri]`: トラック  - `type[string]`: NGSI データ型。これはOperationalPointでなければならない。  - `uopid[string]`: ユニークOP ID  <!-- /30-PropertiesList -->  
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
## ペイロードの例  
#### 運用ポイント NGSI-v2 キー値の例  
以下は、JSON-LD形式のOperationalPointのkey-valuesの例である。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### オペレーショナルポイント NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の OperationalPoint の例である。これは、オプションを使用しない場合、NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -87.0756655,  
          -98.077607  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Recently southern war measure. Behind collection relationship something. Join blue expert should happy according deal."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Community sit about space need win man. Prevent place we whatever image stock."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Into his give degree however."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Identify couple five deep bar popular product not. Design sell security trip never adult heart course."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Product five yourself open. Purpose decade "  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Involve argue cup subject arm bab"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Fish share "  
      },  
      "district": {  
        "type": "Text",  
        "value": "Speech customer perhaps ball defense attorney. Pattern indeed bank result hear. Society different open health. Back reduce his know green next produce."  
      }  
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
#### 運用ポイント NGSI-LD キー値の例  
以下は、JSON-LD形式のOperationalPointのkey-valuesの例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### オペレーショナルポイント NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の OperationalPoint の例である。これは、オプションを使用しない場合、NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

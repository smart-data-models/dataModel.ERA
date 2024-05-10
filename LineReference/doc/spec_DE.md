<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

Entität: LineReference    
======================
<!-- /10-Header -->
    
<!-- 15-License -->
    

[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/LineReference/LICENSE.md)    

[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

Globale Beschreibung: **Eisenbahnstandort**    

Version: 0.0.1    
<!-- /20-Description -->
    
<!-- 30-PropertiesList -->
    

## Liste der Eigenschaften    

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße      
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  
- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  
- `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  
- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  
- `description[string]`: Eine Beschreibung dieses Artikels  
- `id[*]`: Eindeutiger Bezeichner der Entität  
- `kilometer[number]`: Kilometer  
- `lineNationalId[uri]`: Nationale Kennzeichnung der Leitung  
- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  
- `name[string]`: Der Name dieses Artikels  
- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  
- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  
- `type[string]`: NGSI-Datentyp. Es muss LineReference sein  
<!-- /30-PropertiesList -->
    
<!-- 35-RequiredProperties -->
    

Erforderliche Eigenschaften    
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
    
<!-- 40-RequiredProperties -->
    

Datenmodell, das von der ERA-Ontologie https://data-interop.era.europa.eu/era-vocabulary (European Union Agency for Railways) übernommen wurde    
<!-- /40-RequiredProperties -->
    
<!-- 50-DataModelHeader -->
    

## Datenmodell Beschreibung der Eigenschaften    

Alphabetisch sortiert (für Details anklicken)    
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
    

## Beispiel-Nutzlasten    

#### LineReference NGSI-v2 key-values Beispiel    

Hier ist ein Beispiel für eine LineReference im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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

#### LineReference NGSI-v2 normalisiert Beispiel    

Hier ist ein Beispiel für eine LineReference im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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

#### LineReference NGSI-LD key-values Beispiel    

Hier ist ein Beispiel für eine LineReference im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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

#### LineReference NGSI-LD normalisiert Beispiel    

Hier ist ein Beispiel für eine LineReference im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
    

Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->
    
<!-- 97-LastFooter -->
    
---    

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
    

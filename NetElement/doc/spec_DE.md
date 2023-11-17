<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: NetElement    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/NetElement/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Basisklasse für die Definition von Knoten im Konnektivitätsgraphen, der das topologische Netz darstellt.**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.      
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße      
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `elementPart[uri]`: Element Teil  - `endIntrinsicCoordinate[number]`: Ende intrinsische Koordinate  - `hasImplementation[uri]`: Hat die Umsetzung  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startIntrinsicCoordinate[number]`: Anfangskoordinate intrinsisch  - `type[string]`: NGSI-Datentyp. Es muss NetElement sein  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
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
NetElement:      
  description: Base class for defining nodes in the connectivity graph representing the topological network.      
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
    elementPart:      
      description: Element part      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    endIntrinsicCoordinate:      
      description: End intrinsic coordinate      
      type: number      
      x-ngsi:      
        type: Property      
    hasImplementation:      
      description: Has implementation      
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
    startIntrinsicCoordinate:      
      description: Start intrinsic coordinate      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be NetElement      
      enum:      
        - NetElement      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/NetElement      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/NetElement/LICENSE.md      
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
#### NetElement NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein NetElement im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:CDPU:99275524",  
  "dateCreated": "2004-12-12T04:49:10Z",  
  "dateModified": "1992-12-16T09:32:23Z",  
  "source": "Natural film decade",  
  "name": "Price institution dream somebody although song how. Low describe energy significant light road great both. Add explain likely way smile new. Fast must leg public",  
  "alternateName": "Common wind western ball read along. Statement another type seat store. Hot case pressure identify lead.",  
  "description": "Truth expect in recently face. By spend social benefit ask response.",  
  "dataProvider": "Sing whole pres",  
  "owner": [  
    "urn:ngsi-ld:NetElement:items:OKII:37700408",  
    "urn:ngsi-ld:NetElement:items:MRRB:33006272"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetElement:items:NKYQ:56695981"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.6509805,  
      -162.802435  
    ]  
  },  
  "address": {  
    "streetAddress": "Way party system teacher purpose federal. For top far sell.",  
    "addressLocality": "These everyone no measure free finish decision call. Car somebody across glass war ask part. Quality here himself popular service suffer.",  
    "addressRegion": "Article despite environmental service head relate from. L",  
    "addressCountry": "Agreement cover study off. Choose back laugh who management communit",  
    "postalCode": "Radio short thought whole contain. Effect contain character after seem put debate. Decision true mission front maintain re",  
    "postOfficeBoxNumber": "Generatio",  
    "streetNr": "Fi",  
    "district": "Weight over big former dream character. Network anyone easy campaign seek of realize right. Range level level kind cause. Score miss need wear push walk month region."  
  },  
  "areaServed": "She reduce policy necessary campaign your.",  
  "type": "NetElement",  
  "endIntrinsicCoordinate": 172.2,  
  "startIntrinsicCoordinate": 698.8,  
  "elementPart": "urn:ngsi-ld:NetElement:elementPart:MXDV:95711699",  
  "hasImplementation": "urn:ngsi-ld:NetElement:hasImplementation:GOYF:07477051"  
}  
```  
</details>    
#### NetElement NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein NetElement im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:CDPU:99275524",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2004-12-12T04:49:10Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1992-12-16T09:32:23Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Natural film decade"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Price institution dream somebody although song how. Low describe energy significant light road great both. Add explain likely way smile new. Fast must leg public"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Common wind western ball read along. Statement another type seat store. Hot case pressure identify lead."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Truth expect in recently face. By spend social benefit ask response."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Sing whole pres"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:OKII:37700408",  
      "urn:ngsi-ld:NetElement:items:MRRB:33006272"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:NKYQ:56695981"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.6509805,  
        -162.802435  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Way party system teacher purpose federal. For top far sell.",  
      "addressLocality": "These everyone no measure free finish decision call. Car somebody across glass war ask part. Quality here himself popular service suffer.",  
      "addressRegion": "Article despite environmental service head relate from. L",  
      "addressCountry": "Agreement cover study off. Choose back laugh who management communit",  
      "postalCode": "Radio short thought whole contain. Effect contain character after seem put debate. Decision true mission front maintain re",  
      "postOfficeBoxNumber": "Generatio",  
      "streetNr": "Fi",  
      "district": "Weight over big former dream character. Network anyone easy campaign seek of realize right. Range level level kind cause. Score miss need wear push walk month region."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "She reduce policy necessary campaign your."  
  },  
  "type": "NetElement",  
  "endIntrinsicCoordinate": {  
    "type": "Number",  
    "value": 172.2  
  },  
  "startIntrinsicCoordinate": {  
    "type": "Number",  
    "value": 698.8  
  },  
  "elementPart": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetElement:elementPart:MXDV:95711699"  
  },  
  "hasImplementation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetElement:hasImplementation:GOYF:07477051"  
  }  
}  
```  
</details>    
#### NetElement NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein NetElement im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:CDPU:99275524",  
  "dateCreated": "2004-12-12T04:49:10Z",  
  "dateModified": "1992-12-16T09:32:23Z",  
  "source": "Natural film decade",  
  "name": "Price institution dream somebody although song how. Low describe energy significant light road great both. Add explain likely way smile new. Fast must leg public",  
  "alternateName": "Common wind western ball read along. Statement another type seat store. Hot case pressure identify lead.",  
  "description": "Truth expect in recently face. By spend social benefit ask response.",  
  "dataProvider": "Sing whole pres",  
  "owner": [  
    "urn:ngsi-ld:NetElement:items:OKII:37700408",  
    "urn:ngsi-ld:NetElement:items:MRRB:33006272"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetElement:items:NKYQ:56695981"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      28.6509805,  
      -162.802435  
    ]  
  },  
  "address": {  
    "streetAddress": "Way party system teacher purpose federal. For top far sell.",  
    "addressLocality": "These everyone no measure free finish decision call. Car somebody across glass war ask part. Quality here himself popular service suffer.",  
    "addressRegion": "Article despite environmental service head relate from. L",  
    "addressCountry": "Agreement cover study off. Choose back laugh who management communit",  
    "postalCode": "Radio short thought whole contain. Effect contain character after seem put debate. Decision true mission front maintain re",  
    "postOfficeBoxNumber": "Generatio",  
    "streetNr": "Fi",  
    "district": "Weight over big former dream character. Network anyone easy campaign seek of realize right. Range level level kind cause. Score miss need wear push walk month region."  
  },  
  "areaServed": "She reduce policy necessary campaign your.",  
  "type": "NetElement",  
  "endIntrinsicCoordinate": 172.2,  
  "startIntrinsicCoordinate": 698.8,  
  "elementPart": "urn:ngsi-ld:NetElement:elementPart:MXDV:95711699",  
  "hasImplementation": "urn:ngsi-ld:NetElement:hasImplementation:GOYF:07477051",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### NetElement NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein NetElement im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetElement:id:NVEI:78144573",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-10-25T09:04:55Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1972-02-02T07:09:51Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Increase administration contain main. Top every your. Approach raise cup kid region under pay."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Indicate group son local suddenly loss."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pul"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Of shoulder push total throw security. Worker body season soon just skin room."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Ok value system send worker. Worry mouth exist economy red. Home voice out offer think make while effort."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:HDKF:77009578",  
      "urn:ngsi-ld:NetElement:items:IZMH:45951686"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetElement:items:TRQK:78299265"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -82.8184375,  
        29.596471  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Dinner pay business attorney. Bring picture easy knowledge financial.",  
      "addressLocality": "Stock available country onto single have after. Tonight want detail audience best partner better thus.",  
      "addressRegion": "Individual sign most outside position ",  
      "addressCountry": "Treat same head court beyond discuss bad security.",  
      "postalCode": "Western mention large tro",  
      "postOfficeBoxNumber": "Go hold behavior. Police mind sometimes political impact seat. Everyone allow forward weight.",  
      "streetNr": "Step rate start. Term clearly character.",  
      "district": "Over my citizen alone know standard single garden. Daughter sure once whose or."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Wall dream hold team whatever continue field draw. Result poor educati"  
  },  
  "type": "NetElement",  
  "endIntrinsicCoordinate": {  
    "type": "Property",  
    "value": 437.0  
  },  
  "startIntrinsicCoordinate": {  
    "type": "Property",  
    "value": 884.3  
  },  
  "elementPart": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetElement:elementPart:QPYN:94443064"  
  },  
  "hasImplementation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetElement:hasImplementation:LVLV:02180509"  
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

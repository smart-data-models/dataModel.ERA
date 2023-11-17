<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: NetRelation    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/NetRelation/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Basisklasse für die Definition von Kanten im Konnektivitätsgraphen, der das topologische Netz darstellt.**    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `elementA[uri]`: Element A  - `elementB[uri]`: Element B  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `navigability[uri]`: Navigierbarkeit  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `positionOnA[uri]`: Standpunkt zu A  - `positionOnB[uri]`: Position auf B  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Datentyp. Es muss NetRelation sein  <!-- /30-PropertiesList -->    
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
NetRelation:      
  description: Base class for defining edges in the connectivity graph representing the topological network.      
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
    elementA:      
      description: Element A      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    elementB:      
      description: Element B      
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
    navigability:      
      description: Navigability      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    positionOnA:      
      description: Position on A      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    positionOnB:      
      description: Position on B      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
      description: NGSI data type. It has to be NetRelation      
      enum:      
        - NetRelation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/NetRelation      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/NetRelation/LICENSE.md      
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
#### NetRelation NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine NetRelation im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:QVEK:97020978",  
  "dateCreated": "2002-11-19T10:23:16Z",  
  "dateModified": "2003-03-10T03:36:36Z",  
  "source": "Radio occur group guy together. Prepare which behavior maybe watch actually Republican paper.",  
  "name": "Coach economic ",  
  "alternateName": "Friend film shake president politics. Glass but left business question side. Push despite education group house.",  
  "description": "Threat instead a loss add politics.",  
  "dataProvider": "Development reach series assume. Real attention today community.",  
  "owner": [  
    "urn:ngsi-ld:NetRelation:items:MAOY:99573659",  
    "urn:ngsi-ld:NetRelation:items:BYQO:04488951"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetRelation:items:VYGL:22233826"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      89.9053455,  
      -11.456382  
    ]  
  },  
  "address": {  
    "streetAddress": "Clearly chance feel operation able win me. Full firm save.",  
    "addressLocality": "Morning could approa",  
    "addressRegion": "Pressure side account matter so. Ta",  
    "addressCountry": "East back help hundred pay record. Language explain summer min",  
    "postalCode": "Leader view he decision could personal clear. World per",  
    "postOfficeBoxNumber": "White language agency east. Who mother mother same leave them rule.",  
    "streetNr": "Health I particular west. Floor Congress individual someone into ever foot.",  
    "district": "Have when good news trade above. Individual p"  
  },  
  "areaServed": "Spea",  
  "type": "NetRelation",  
  "elementA": "urn:ngsi-ld:NetRelation:elementA:TUIU:78345951",  
  "elementB": "urn:ngsi-ld:NetRelation:elementB:DHHX:71184798",  
  "navigability": "urn:ngsi-ld:NetRelation:navigability:TZOM:33501230",  
  "positionOnA": "urn:ngsi-ld:NetRelation:positionOnA:YSDM:89916223",  
  "positionOnB": "urn:ngsi-ld:NetRelation:positionOnB:IYRF:06079262"  
}  
```  
</details>    
#### NetRelation NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für eine NetRelation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:QVEK:97020978",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2002-11-19T10:23:16Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2003-03-10T03:36:36Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Radio occur group guy together. Prepare which behavior maybe watch actually Republican paper."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Coach economic "  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Friend film shake president politics. Glass but left business question side. Push despite education group house."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Threat instead a loss add politics."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Development reach series assume. Real attention today community."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:MAOY:99573659",  
      "urn:ngsi-ld:NetRelation:items:BYQO:04488951"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:VYGL:22233826"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        89.9053455,  
        -11.456382  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Clearly chance feel operation able win me. Full firm save.",  
      "addressLocality": "Morning could approa",  
      "addressRegion": "Pressure side account matter so. Ta",  
      "addressCountry": "East back help hundred pay record. Language explain summer min",  
      "postalCode": "Leader view he decision could personal clear. World per",  
      "postOfficeBoxNumber": "White language agency east. Who mother mother same leave them rule.",  
      "streetNr": "Health I particular west. Floor Congress individual someone into ever foot.",  
      "district": "Have when good news trade above. Individual p"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Spea"  
  },  
  "type": "NetRelation",  
  "elementA": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:elementA:TUIU:78345951"  
  },  
  "elementB": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:elementB:DHHX:71184798"  
  },  
  "navigability": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:navigability:TZOM:33501230"  
  },  
  "positionOnA": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:positionOnA:YSDM:89916223"  
  },  
  "positionOnB": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:NetRelation:positionOnB:IYRF:06079262"  
  }  
}  
```  
</details>    
#### NetRelation NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine NetRelation im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:QVEK:97020978",  
  "dateCreated": "2002-11-19T10:23:16Z",  
  "dateModified": "2003-03-10T03:36:36Z",  
  "source": "Radio occur group guy together. Prepare which behavior maybe watch actually Republican paper.",  
  "name": "Coach economic ",  
  "alternateName": "Friend film shake president politics. Glass but left business question side. Push despite education group house.",  
  "description": "Threat instead a loss add politics.",  
  "dataProvider": "Development reach series assume. Real attention today community.",  
  "owner": [  
    "urn:ngsi-ld:NetRelation:items:MAOY:99573659",  
    "urn:ngsi-ld:NetRelation:items:BYQO:04488951"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:NetRelation:items:VYGL:22233826"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      89.9053455,  
      -11.456382  
    ]  
  },  
  "address": {  
    "streetAddress": "Clearly chance feel operation able win me. Full firm save.",  
    "addressLocality": "Morning could approa",  
    "addressRegion": "Pressure side account matter so. Ta",  
    "addressCountry": "East back help hundred pay record. Language explain summer min",  
    "postalCode": "Leader view he decision could personal clear. World per",  
    "postOfficeBoxNumber": "White language agency east. Who mother mother same leave them rule.",  
    "streetNr": "Health I particular west. Floor Congress individual someone into ever foot.",  
    "district": "Have when good news trade above. Individual p"  
  },  
  "areaServed": "Spea",  
  "type": "NetRelation",  
  "elementA": "urn:ngsi-ld:NetRelation:elementA:TUIU:78345951",  
  "elementB": "urn:ngsi-ld:NetRelation:elementB:DHHX:71184798",  
  "navigability": "urn:ngsi-ld:NetRelation:navigability:TZOM:33501230",  
  "positionOnA": "urn:ngsi-ld:NetRelation:positionOnA:YSDM:89916223",  
  "positionOnB": "urn:ngsi-ld:NetRelation:positionOnB:IYRF:06079262",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### NetRelation NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für eine NetRelation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:NetRelation:id:JUHL:24845257",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-03-26T06:21:22Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1991-11-25T01:27:05Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Get able seven not return identify son could. Wish prevent way."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Project nation tea"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Interest since th"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Another whom experience Republican majority maybe. Deal security score accept hour vote. Executive church manage imp"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Heavy under today name available."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:MCOV:78184970",  
      "urn:ngsi-ld:NetRelation:items:WFNU:46021273"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:NetRelation:items:KMWK:60383200"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        6.426867,  
        -155.118055  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Somebody our issue myself meeting begin knowledge. Best Mr hit sing society economy.",  
      "addressLocality": "Find life economy life sing avoid rock. Similar party tonight natural clear it",  
      "addressRegion": "Pa",  
      "addressCountry": "To push help action score. Brother lose benefit main.",  
      "postalCode": "Base understand particular shake note response trouble spend. Station prevent individual more fl",  
      "postOfficeBoxNumber": "Impact who hand difference even cell never address. Road size back top indeed ",  
      "streetNr": "Race base effect car Mr talk huge blue. Mig",  
      "district": "Describe similar area cu"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Piece idea want likely turn job. Past "  
  },  
  "type": "NetRelation",  
  "elementA": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:elementA:NXWD:06501472"  
  },  
  "elementB": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:elementB:CNDJ:23196407"  
  },  
  "navigability": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:navigability:TDBB:08079538"  
  },  
  "positionOnA": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:positionOnA:WRNS:94567510"  
  },  
  "positionOnB": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:NetRelation:positionOnB:POXU:21033119"  
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

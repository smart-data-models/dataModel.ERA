<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: RaisedPantographsDistanceAndSpeed    
==========================================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/RaisedPantographsDistanceAndSpeed/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Angabe der maximal zulässigen Anzahl von angehobenen Stromabnehmern pro Zug und des Mindestabstands von Mittellinie zu Mittellinie benachbarter Stromabnehmerköpfe, ausgedrückt in Metern, bei der angegebenen Geschwindigkeit.    
Jedes Gleis kann mehrere zulässige (strukturierte) Werte für erhöhte Stromabnehmer pro Zug haben, und jedes Gleis hat Werte für die Anzahl der Stromabnehmer, den Mindestabstand zwischen den Stromabnehmern in Metern und die Geschwindigkeit in km/h.**    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `raisedPantographsDistance[number]`: Erhöhter Abstand der Stromabnehmer  - `raisedPantographsNumber[number]`: Anzahl der Stromabnehmer.  - `raisedPantographsSpeed[number]`: Erhöhte Geschwindigkeit der Stromabnehmer  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Datentyp. Es muss RaisedPantographsDistanceAndSpeed sein  <!-- /30-PropertiesList -->    
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
RaisedPantographsDistanceAndSpeed:      
  description: |-      
    Indication of maximum number of raised pantographs per train allowed and minimum spacing centre line to centre line of adjacent pantograph heads, expressed in metres, at the given speed.      
    Each track can have several raised pantographs per train allowed (structured) values, and each one has values for number of pantographs, minimum distance between pantographs, in metres, and speed considered in km/h.      
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
    raisedPantographsDistance:      
      description: Raised pantographs distance      
      type: number      
      x-ngsi:      
        type: Property      
    raisedPantographsNumber:      
      description: Number of pantographs.      
      type: number      
      x-ngsi:      
        type: Property      
    raisedPantographsSpeed:      
      description: Raised pantographs speed      
      type: number      
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
      description: NGSI data type. It has to be RaisedPantographsDistanceAndSpeed      
      enum:      
        - RaisedPantographsDistanceAndSpeed      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/RaisedPantographsDistanceAndSpeed      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/RaisedPantographsDistanceAndSpeed/LICENSE.md      
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
#### RaisedPantographsDistanceAndSpeed NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine RaisedPantographsDistanceAndSpeed im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": "2016-10-01T23:32:51Z",  
  "dateModified": "1994-01-08T16:04:55Z",  
  "source": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment.",  
  "name": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter.",  
  "alternateName": "Describe other scene standard citizen. Exist letter down ready TV phon",  
  "description": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning.",  
  "dataProvider": "Song minute like table knowledge state. Notice line never support stop.",  
  "owner": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      52.853707,  
      -40.868675  
    ]  
  },  
  "address": {  
    "streetAddress": "Special son three figure cost mili",  
    "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
    "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
    "addressCountry": "Consumer include little. Seem ",  
    "postalCode": "Out everything senior. Out staff",  
    "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
    "streetNr": "",  
    "district": "Worker expect realize above. I differenc"  
  },  
  "areaServed": "Table must who. Grow in ",  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": 864,  
  "raisedPantographsNumber": 864,  
  "raisedPantographsSpeed": 864,  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RaisedPantographsDistanceAndSpeed NGSI-v2 normalized Beispiel    
Hier ist ein Beispiel für eine RaisedPantographsDistanceAndSpeed im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2016-10-01T23:32:51Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1994-01-08T16:04:55Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment."  
  },  
  "name": {  
    "type": "Text",  
    "value": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Describe other scene standard citizen. Exist letter down ready TV phon"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Song minute like table knowledge state. Notice line never support stop."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        52.853707,  
        -40.868675  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Special son three figure cost mili",  
      "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
      "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
      "addressCountry": "Consumer include little. Seem ",  
      "postalCode": "Out everything senior. Out staff",  
      "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
      "streetNr": "",  
      "district": "Worker expect realize above. I differenc"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Table must who. Grow in "  
  },  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": {  
    "type": "Number",  
    "value": 864  
  },  
  "raisedPantographsNumber": {  
    "type": "Number",  
    "value": 864  
  },  
  "raisedPantographsSpeed": {  
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
#### RaisedPantographsDistanceAndSpeed NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine RaisedPantographsDistanceAndSpeed im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": "2016-10-01T23:32:51Z",  
  "dateModified": "1994-01-08T16:04:55Z",  
  "source": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment.",  
  "name": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter.",  
  "alternateName": "Describe other scene standard citizen. Exist letter down ready TV phon",  
  "description": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning.",  
  "dataProvider": "Song minute like table knowledge state. Notice line never support stop.",  
  "owner": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      52.853707,  
      -40.868675  
    ]  
  },  
  "address": {  
    "streetAddress": "Special son three figure cost mili",  
    "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
    "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
    "addressCountry": "Consumer include little. Seem ",  
    "postalCode": "Out everything senior. Out staff",  
    "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
    "streetNr": "",  
    "district": "Worker expect realize above. I differenc"  
  },  
  "areaServed": "Table must who. Grow in ",  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": 864,  
  "raisedPantographsNumber": 864,  
  "raisedPantographsSpeed": 864,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RaisedPantographsDistanceAndSpeed NGSI-LD normalized Beispiel    
Hier ist ein Beispiel für eine RaisedPantographsDistanceAndSpeed im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:NRAH:81561263",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1971-11-20T03:14:14Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1970-10-03T20:50:52Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "War game help give"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Watch within challenge safe. Raise available seem compare body early. None face safe term before environment drop"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Court I loo"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Them site whole should play generation question. Significant on teach of none."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Bag care religious possible source media team. Skill politics blue yes according."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:DKUU:20419467",  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:BFPP:72232537"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:XVYI:24654995"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        33.252656,  
        109.596554  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Break seem system real part become pay. Sense baby total care investment. Figure break likely behavior talk morning estab",  
      "addressLocality": "Quite himself drive trouble pay they guy. History role mome",  
      "addressRegion": "Cut seem painting race.",  
      "addressCountry": "Room whose forget soldier evidence air. Memory artist real western myse",  
      "postalCode": "Glass artist leg modern. Republican reflect hot skill democratic speak.",  
      "postOfficeBoxNumber": "Serious art magazine morning serious histor",  
      "streetNr": "Small w",  
      "district": "Remain environment performance campaign. Test traditional want call. Building forget argue suggest."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Forward gun require "  
  },  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": {  
    "type": "Property",  
    "value": 131  
  },  
  "raisedPantographsNumber": {  
    "type": "Property",  
    "value": 478  
  },  
  "raisedPantographsSpeed": {  
    "type": "Property",  
    "value": 219  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

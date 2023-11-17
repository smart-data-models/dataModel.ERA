<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: LoadCapability    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/LoadCapability/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Klasse ersetzt zusammen mit den Eigenschaften loadCapabilityLineCategory und loadCapabilitySpeed die bisherige SKOS-Eigenschaft loadCapability.**    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `loadCapabilityLineCategory[uri]`: Tragfähigkeitskategorie  - `loadCapabilitySpeed[number]`: Belastbarkeit Geschwindigkeit  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Datentyp. Es muss LoadCapability sein  <!-- /30-PropertiesList -->    
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
LoadCapability:      
  description: This class together with properties loadCapabilityLineCategory and loadCapabilitySpeed replaces the previous loadCapability SKOS property.      
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
    loadCapabilityLineCategory:      
      description: Load capability line category      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    loadCapabilitySpeed:      
      description: Load capability speed      
      type: number      
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
      description: NGSI data type. It has to be LoadCapability      
      enum:      
        - LoadCapability      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/LoadCapability      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/LoadCapability/LICENSE.md      
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
#### LoadCapability NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine LoadCapability im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:LoadCapability:id:MFBV:83261473",  
  "dateCreated": "1974-08-17T19:23:12Z",  
  "dateModified": "2004-07-07T02:44:03Z",  
  "source": "Body group once wind Mrs. Poor action no policy above herself ",  
  "name": "Everything any various including hundred dark. Within beautiful performance campaign. Executive including summer.",  
  "alternateName": "You mach",  
  "description": "Admit million plant when fast lot eat. School exist attack knowledge. Re",  
  "dataProvider": "Bed return effort current keep Mr consider hot.",  
  "owner": [  
    "urn:ngsi-ld:LoadCapability:items:ELMZ:31959345",  
    "urn:ngsi-ld:LoadCapability:items:UJUB:17759651"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:LoadCapability:items:ASHM:52969026"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      67.503895,  
      -57.061105  
    ]  
  },  
  "address": {  
    "streetAddress": "Consider shake vote method animal. Practice state thank spring thank.",  
    "addressLocality": "Speak mention partner be receive. Moment tree crime question hair night any.",  
    "addressRegion": "Special oil rich something become ",  
    "addressCountry": "Term structure specific court. Suggest fire late positive white property beautiful establish. Very certainly could work program alon",  
    "postalCode": "Office money land produce voice single whom. Give three up build list point officer. Peace by apply easy or from lot. Compare water evening",  
    "postOfficeBoxNumber": "The population director although baby. Any college citizen bill official throughout through.",  
    "streetNr": "Week event public activity public single beyond. Skill themselves computer boy already amount.",  
    "district": "Administration from five player both."  
  },  
  "areaServed": "They us song area seat. Cut television audience pattern outside raise. Hit suddenly pay election.",  
  "type": "LoadCapability",  
  "loadCapabilitySpeed": 864,  
  "loadCapabilityLineCategory": "urn:ngsi-ld:LoadCapability:loadCapabilityLineCategory:PLSG:66048764"  
}  
```  
</details>    
#### LoadCapability NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für eine LoadCapability im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:LoadCapability:id:MFBV:83261473",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1974-08-17T19:23:12Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2004-07-07T02:44:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Body group once wind Mrs. Poor action no policy above herself "  
  },  
  "name": {  
    "type": "Text",  
    "value": "Everything any various including hundred dark. Within beautiful performance campaign. Executive including summer."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "You mach"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Admit million plant when fast lot eat. School exist attack knowledge. Re"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Bed return effort current keep Mr consider hot."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:LoadCapability:items:ELMZ:31959345",  
      "urn:ngsi-ld:LoadCapability:items:UJUB:17759651"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:LoadCapability:items:ASHM:52969026"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        67.503895,  
        -57.061105  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Consider shake vote method animal. Practice state thank spring thank.",  
      "addressLocality": "Speak mention partner be receive. Moment tree crime question hair night any.",  
      "addressRegion": "Special oil rich something become ",  
      "addressCountry": "Term structure specific court. Suggest fire late positive white property beautiful establish. Very certainly could work program alon",  
      "postalCode": "Office money land produce voice single whom. Give three up build list point officer. Peace by apply easy or from lot. Compare water evening",  
      "postOfficeBoxNumber": "The population director although baby. Any college citizen bill official throughout through.",  
      "streetNr": "Week event public activity public single beyond. Skill themselves computer boy already amount.",  
      "district": "Administration from five player both."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "They us song area seat. Cut television audience pattern outside raise. Hit suddenly pay election."  
  },  
  "type": "LoadCapability",  
  "loadCapabilitySpeed": {  
    "type": "Number",  
    "value": 864  
  },  
  "loadCapabilityLineCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:LoadCapability:loadCapabilityLineCategory:PLSG:66048764"  
  }  
}  
```  
</details>    
#### LoadCapability NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine LoadCapability im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:LoadCapability:id:MFBV:83261473",  
  "dateCreated": "1974-08-17T19:23:12Z",  
  "dateModified": "2004-07-07T02:44:03Z",  
  "source": "Body group once wind Mrs. Poor action no policy above herself ",  
  "name": "Everything any various including hundred dark. Within beautiful performance campaign. Executive including summer.",  
  "alternateName": "You mach",  
  "description": "Admit million plant when fast lot eat. School exist attack knowledge. Re",  
  "dataProvider": "Bed return effort current keep Mr consider hot.",  
  "owner": [  
    "urn:ngsi-ld:LoadCapability:items:ELMZ:31959345",  
    "urn:ngsi-ld:LoadCapability:items:UJUB:17759651"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:LoadCapability:items:ASHM:52969026"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      67.503895,  
      -57.061105  
    ]  
  },  
  "address": {  
    "streetAddress": "Consider shake vote method animal. Practice state thank spring thank.",  
    "addressLocality": "Speak mention partner be receive. Moment tree crime question hair night any.",  
    "addressRegion": "Special oil rich something become ",  
    "addressCountry": "Term structure specific court. Suggest fire late positive white property beautiful establish. Very certainly could work program alon",  
    "postalCode": "Office money land produce voice single whom. Give three up build list point officer. Peace by apply easy or from lot. Compare water evening",  
    "postOfficeBoxNumber": "The population director although baby. Any college citizen bill official throughout through.",  
    "streetNr": "Week event public activity public single beyond. Skill themselves computer boy already amount.",  
    "district": "Administration from five player both."  
  },  
  "areaServed": "They us song area seat. Cut television audience pattern outside raise. Hit suddenly pay election.",  
  "type": "LoadCapability",  
  "loadCapabilitySpeed": 864,  
  "loadCapabilityLineCategory": "urn:ngsi-ld:LoadCapability:loadCapabilityLineCategory:PLSG:66048764",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### LoadCapability NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für eine LoadCapability im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:LoadCapability:id:UFEX:97758734",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2014-08-02T14:53:09Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2009-07-26T04:55:34Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Few manage cold worker community t"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Attack take position school easy my. Join five president new m"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Very beautiful property least. He so different laugh. "  
  },  
  "description": {  
    "type": "Property",  
    "value": "Gas produce market foot affect force project carry. Another raise read soldier partner best."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Water"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:LoadCapability:items:POZE:75568096",  
      "urn:ngsi-ld:LoadCapability:items:GPCV:40954756"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:LoadCapability:items:VUOM:06241362"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        62.605605,  
        101.293823  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "West ca",  
      "addressLocality": "Add language take thro",  
      "addressRegion": "Ah",  
      "addressCountry": "Beyond fight kind situation drug able itself. Whose serious candidate model never must. Southern would age million nothing.",  
      "postalCode": "Because positive medical miss.",  
      "postOfficeBoxNumber": "American move successful author look. Quality short current site ma",  
      "streetNr": "Staff art around. Foot travel health his world yeah. Line cup road range forward.",  
      "district": "Baby find south message lead federal. Thing thought pattern teacher reflect "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Leg movie push again. Fish prepare music take song fear."  
  },  
  "type": "LoadCapability",  
  "loadCapabilitySpeed": {  
    "type": "Property",  
    "value": 235  
  },  
  "loadCapabilityLineCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:LoadCapability:loadCapabilityLineCategory:SMGO:17205098"  
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

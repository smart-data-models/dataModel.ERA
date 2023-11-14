<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: InfrastructureManager  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/InfrastructureManager/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Der Infrastrukturbetreiber ist Eigentümer und Betreiber des Schienennetzes und der zugehörigen Infrastruktur**.  
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `definesSubset[uri]`: Definiert Teilmenge  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `imCode[string]`: IMs Code  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Datentyp. Es muss InfrastructureManager sein  <!-- /30-PropertiesList -->  
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
InfrastructureManager:    
  description: The infrastructure manager owns and operates the railway network and related infrastructure.    
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
    definesSubset:    
      description: Defines subset    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    imCode:    
      description: IM's code    
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
      description: NGSI data type. It has to be InfrastructureManager    
      enum:    
        - InfrastructureManager    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/InfrastructureManager    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureManager/LICENSE.md    
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
#### InfrastructureManager NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen InfrastructureManager im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:VIMY:89391422",  
  "dateCreated": "2006-09-18T16:56:18Z",  
  "dateModified": "1978-06-20T09:22:50Z",  
  "source": "Sort southern music artist. Fear manage seat population environment.",  
  "name": "Plan challenge vote do again. Enjoy short particularly.",  
  "alternateName": "Rate option level back stuff kind. Teach televi",  
  "description": "In discussion fall economic force shake. This speak fine piece work bil",  
  "dataProvider": "Administration raise door a your. Oil summ",  
  "owner": [  
    "urn:ngsi-ld:InfrastructureManager:items:JMAY:69019141",  
    "urn:ngsi-ld:InfrastructureManager:items:HDMP:30084694"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:InfrastructureManager:items:HEJR:49829825"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.3334725,  
      -142.001584  
    ]  
  },  
  "address": {  
    "streetAddress": "Moment someone learn short affect. Could those herself mention without use.",  
    "addressLocality": "Able born appear fact. Too nature record second letter. Hit pattern because unit easy address befo",  
    "addressRegion": "Physical same read success fight.",  
    "addressCountry": "Girl want over allow ask begin three. Say month call how employee treat environmental energy. Reflect through society experienc",  
    "postalCode": "Here simply my force child kid. Why behavior last here. Back PM carry actually interview rise.",  
    "postOfficeBoxNumber": "Partner magazine cause before. Decide method experience exactly. Operation final feeling staff ten.",  
    "streetNr": "Tell or ok else another allow standard.",  
    "district": "Hot player second fall. Participant state draw agent suggest visit however we. Line we blue. Sit record TV can."  
  },  
  "areaServed": "White task performance blood. Hard eye road probably interview to.",  
  "type": "InfrastructureManager",  
  "imCode": "Responsibility information do paper either",  
  "definesSubset": "urn:ngsi-ld:InfrastructureManager:definesSubset:QKJR:78702924",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### InfrastructureManager NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen InfrastructureManager im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:VIMY:89391422",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2006-09-18T16:56:18Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1978-06-20T09:22:50Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Sort southern music artist. Fear manage seat population environment."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Plan challenge vote do again. Enjoy short particularly."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Rate option level back stuff kind. Teach televi"  
  },  
  "description": {  
    "type": "Text",  
    "value": "In discussion fall economic force shake. This speak fine piece work bil"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Administration raise door a your. Oil summ"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:JMAY:69019141",  
      "urn:ngsi-ld:InfrastructureManager:items:HDMP:30084694"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:HEJR:49829825"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -36.3334725,  
          -142.001584  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Moment someone learn short affect. Could those herself mention without use."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Able born appear fact. Too nature record second letter. Hit pattern because unit easy address befo"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Physical same read success fight."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Girl want over allow ask begin three. Say month call how employee treat environmental energy. Reflect through society experienc"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Here simply my force child kid. Why behavior last here. Back PM carry actually interview rise."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Partner magazine cause before. Decide method experience exactly. Operation final feeling staff ten."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Tell or ok else another allow standard."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Hot player second fall. Participant state draw agent suggest visit however we. Line we blue. Sit record TV can."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "White task performance blood. Hard eye road probably interview to."  
  },  
  "type": "InfrastructureManager",  
  "imCode": {  
    "type": "Text",  
    "value": "Responsibility information do paper either"  
  },  
  "definesSubset": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:InfrastructureManager:definesSubset:QKJR:78702924"  
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
#### InfrastructureManager NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen InfrastructureManager im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Einheit.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:VIMY:89391422",  
  "dateCreated": "2006-09-18T16:56:18Z",  
  "dateModified": "1978-06-20T09:22:50Z",  
  "source": "Sort southern music artist. Fear manage seat population environment.",  
  "name": "Plan challenge vote do again. Enjoy short particularly.",  
  "alternateName": "Rate option level back stuff kind. Teach televi",  
  "description": "In discussion fall economic force shake. This speak fine piece work bil",  
  "dataProvider": "Administration raise door a your. Oil summ",  
  "owner": [  
    "urn:ngsi-ld:InfrastructureManager:items:JMAY:69019141",  
    "urn:ngsi-ld:InfrastructureManager:items:HDMP:30084694"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:InfrastructureManager:items:HEJR:49829825"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.3334725,  
      -142.001584  
    ]  
  },  
  "address": {  
    "streetAddress": "Moment someone learn short affect. Could those herself mention without use.",  
    "addressLocality": "Able born appear fact. Too nature record second letter. Hit pattern because unit easy address befo",  
    "addressRegion": "Physical same read success fight.",  
    "addressCountry": "Girl want over allow ask begin three. Say month call how employee treat environmental energy. Reflect through society experienc",  
    "postalCode": "Here simply my force child kid. Why behavior last here. Back PM carry actually interview rise.",  
    "postOfficeBoxNumber": "Partner magazine cause before. Decide method experience exactly. Operation final feeling staff ten.",  
    "streetNr": "Tell or ok else another allow standard.",  
    "district": "Hot player second fall. Participant state draw agent suggest visit however we. Line we blue. Sit record TV can."  
  },  
  "areaServed": "White task performance blood. Hard eye road probably interview to.",  
  "type": "InfrastructureManager",  
  "imCode": "Responsibility information do paper either",  
  "definesSubset": "urn:ngsi-ld:InfrastructureManager:definesSubset:QKJR:78702924",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### InfrastructureManager NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen InfrastructureManager im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Einheit.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:MXSJ:48211430",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2001-02-17T13:59:21Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1978-12-17T01:37:15Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Drop wear participant probably pull another claim. Soldier among magazine name cause."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Push low morning himself boy. Response push daughter certain blood hour career."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Inter"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Sing condition often fund gun report. Skin yes me"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Shoulder west friend find stage main state. Those way machine consumer current friend within. Artist past participant agree more."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:SHEM:41311877",  
      "urn:ngsi-ld:InfrastructureManager:items:UIQW:30839567"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:PJAF:62503952"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        3.5779895,  
        -137.677126  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Behind play land top reflect material drug. Charge worry newspaper important. Budget position meeting throughout fight daughter.",  
      "addressLocality": "Road husb",  
      "addressRegion": "Official arm decision can often general second. Short establish maintain television pattern.",  
      "addressCountry": "Center system out forward I pressure short. News moment decision spend.",  
      "postalCode": "Serve recent here determine until. Good sure down talk since establish. Challenge describe structure necessary. Rate difference item",  
      "postOfficeBoxNumber": "Camera instead glass stop remember good. War heavy help.",  
      "streetNr": "Total ",  
      "district": "Half consumer condition and night exist human. P"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Attack total help who reduce lay. Daughter step center short property per whether"  
  },  
  "type": "InfrastructureManager",  
  "imCode": {  
    "type": "Property",  
    "value": "Away live too certainly. Ground why include include."  
  },  
  "definesSubset": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:InfrastructureManager:definesSubset:OSEY:46076384"  
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

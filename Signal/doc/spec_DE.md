<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Signal  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/Signal/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Allgemeine Beschreibung: **Ein Eisenbahnsignal ist eine Anlage neben dem Gleis, die dem Triebfahrzeugführer die zulässige Höchstgeschwindigkeit im nächsten Blockabschnitt anzeigt.  
Definition RSM: Gerät, mit dem eine herkömmliche optische oder akustische Anzeige gegeben wird, die im Allgemeinen die Bewegungen von Eisenbahnfahrzeugen betrifft.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Lande liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `relativeDistanceDangerPoint[number]`: Relative Entfernung der Gefahrenstelle  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `signalId[string]`: Name des Signals  - `signalOrientation[uri]`: Signalausrichtung  - `signalType[uri]`: Art des Signals  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `track[uri]`: Spur  - `type[string]`: NGSI-Datentyp. Er muss Signal sein  <!-- /30-PropertiesList -->  
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
Signal:    
  description: |-    
    A railway signal is an installation next to the railway track for signalling the maximum allowed speed in the next block section to the train driver.    
    Definition RSM: Apparatus by means of which a conventional visual or acoustic indication is given, generally concerning the movements of railway vehicles.    
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
    relativeDistanceDangerPoint:    
      description: Relative distance of the danger point    
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
    signalId:    
      description: Name of signal    
      type: string    
      x-ngsi:    
        type: Property    
    signalOrientation:    
      description: Signal orientation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    signalType:    
      description: Type of signal    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
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
      description: NGSI data type. It has to be Signal    
      enum:    
        - Signal    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Signal    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Signal/LICENSE.md    
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
#### Signal NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Signal im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
}  
```  
</details>  
#### Signal NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Signal im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1970-03-08T14:32:13Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2011-08-18T23:12:35Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Here choose style decade occur leader"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Drop"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Truth add because former. Indeed long yeah change near experience."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:OCNG:88914328",  
      "urn:ngsi-ld:Signal:items:QDWA:77960070"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:IKCH:27474652"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          7.167995,  
          -149.393214  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Upon certainly west population. A walk result product major draw "  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Account rich measure every price energy allow. Put customer c"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Prepare family across front. Nothing main religious strategy seven notice where."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Word wai"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Meet know training. Land grow old kid effect. Form director decide join draw."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Several center notice ever deal his. National parent fund focus pull those door."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Activity"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Number",  
    "value": 864  
  },  
  "signalId": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peac"  
  },  
  "signalOrientation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156"  
  },  
  "signalType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalType:CXMW:87784080"  
  },  
  "track": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
  }  
}  
```  
</details>  
#### Signal NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Signal im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Signal NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Signal im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:SUMI:05987689",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2013-12-11T15:53:44Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-09-10T20:37:14Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Owner support present act enter."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Start read half."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Home state area operation respond early. Edge return condition federal."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Total again here high. Team report again ask product these cut."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Republican eight think start. Hot movie want serve father audience management."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:MZLV:03669390",  
      "urn:ngsi-ld:Signal:items:LNRS:49951624"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:JOYH:86575892"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -13.176379,  
        -116.163154  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Coach my discover both usually east page. Rather lead investment child as record resource. In product rise couple v",  
      "addressLocality": "Conference pull tax indeed. Very trou",  
      "addressRegion": "Man issue two memory every. Television traditional draw democratic.",  
      "addressCountry": "Fund threat they increase. Guy series politics bag.",  
      "postalCode": "Production later according down yes. Nothing my forward.",  
      "postOfficeBoxNumber": "Beat maintain people",  
      "streetNr": "East too Republican represent behind leader. Little television few Republican fire behavior good.",  
      "district": "Ever theory social special century spring."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "It she follow board blood. Certainly easy particular she sure by big. Say cold national expect rock. Value ski"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Property",  
    "value": 859  
  },  
  "signalId": {  
    "type": "Property",  
    "value": "Mean PM capital car particular head. Claim ago brother forget. Benefit start body ask yet age believe."  
  },  
  "signalOrientation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalOrientation:XSWZ:79200878"  
  },  
  "signalType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalType:OIXR:27955866"  
  },  
  "track": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:track:SBLI:67422940"  
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

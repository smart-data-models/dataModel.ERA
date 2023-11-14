<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: InfrastructureObject  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/InfrastructureObject/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Klasse umfasst alle Klassen, die Merkmale darstellen, die in der europäischen Eisenbahninfrastruktur implementiert sind. Sie ist eine Unterklasse des ERA-Features, das eine räumliche Darstellung hat. Sie umfasst Gleise, Bahnsteige, Signale, Tunnels, Betriebsstellen und Streckenabschnitte.  
Ein Feature, das zur Infrastruktur gehört, kann als topologisches Objekt abstrahiert werden (hasAbstraction). Über die Eigenschaft infrastructureMgr.** ist es auch mit dem Infrastrukturbetreiber verbunden.  
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `hasAbstraction[uri]`: Hat Abstraktion  - `id[*]`: Eindeutiger Bezeichner der Entität  - `inCountry[uri]`: Auf dem Land  - `infrastructureMgr[uri]`: Leiter der Infrastruktur  - `lineReference[uri]`: Eisenbahnstandort des Einsatzpunktes  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Datentyp. Es muss InfrastructureObject sein  - `validityEndDate[string]`: Datum des Gültigkeitsendes  - `validityStartDate[string]`: Datum des Gültigkeitsbeginns  <!-- /30-PropertiesList -->  
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
InfrastructureObject:    
  description: |-    
    This class encompasses all those classes that represent features that are  implemented in the European railway infrastructure. It is a subclass of the ERA Feature that has a spatial representation. It covers tracks, platforms, signals, tunnels, operational points, and sections of line.    
    A feature that belongs to the infrastructure can be abstracted (hasAbstraction) as a topological object. It also is related to the infrastructure manager through the property infrastructureMgr.    
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
    hasAbstraction:    
      description: Has abstraction    
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
    inCountry:    
      description: In country    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    infrastructureMgr:    
      description: Infrastructure manager    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    lineReference:    
      description: Railway location of Operational point    
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
      description: NGSI data type. It has to be InfrastructureObject    
      enum:    
        - InfrastructureObject    
      type: string    
      x-ngsi:    
        type: Property    
    validityEndDate:    
      description: Validity end date    
      type: string    
      x-ngsi:    
        type: Property    
    validityStartDate:    
      description: Validity start date    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/InfrastructureObject    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureObject/LICENSE.md    
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
#### InfrastructureObject NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein InfrastructureObject im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureObject:id:QRWO:38616864",  
  "dateCreated": "1993-03-01T14:30:32Z",  
  "dateModified": "1992-12-10T19:47:10Z",  
  "source": "Admit close national in. Class all question should. Election machine recently general Mrs.",  
  "name": "Artist follow sit surface military anything. Instead discover hair. Bank table sure south hard.",  
  "alternateName": "Home choose suggest message. Cost perform although I relate.",  
  "description": "Bad contain rate president. Option marriage factor important plan service. Forget manage source throw.",  
  "dataProvider": "Single spring run ",  
  "owner": [  
    "urn:ngsi-ld:InfrastructureObject:items:GAAE:54229861",  
    "urn:ngsi-ld:InfrastructureObject:items:LFCD:71096296"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:InfrastructureObject:items:PGJT:48591099"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      22.2632155,  
      -43.950467  
    ]  
  },  
  "address": {  
    "streetAddress": "Internatio",  
    "addressLocality": "Much east health history people million continue. Either cultural quite its throw day section. Test week start clear into air require",  
    "addressRegion": "Seem mode",  
    "addressCountry": "Small cold lay station new. Every ever star financial. ",  
    "postalCode": "Family goal effort rather. Improve threat five general me general.",  
    "postOfficeBoxNumber": "Since our wife run hour exist letter. Above seek now rest pick then.",  
    "streetNr": "Involve that close few million. Understand wife toward catch off station. Action threat sell mission example.",  
    "district": "Production already capital early. Special stage operation break region. Animal hold key bed value continue west. Mission turn less skin beat seem."  
  },  
  "areaServed": "Class participant race Mr so account.",  
  "type": "InfrastructureObject",  
  "validityEndDate": "Rock officer moment reason. Far deal skin quite. Car inside morning open.",  
  "validityStartDate": "Step matter huge full usually. Who offer ever guess up strong age.",  
  "hasAbstraction": "urn:ngsi-ld:InfrastructureObject:hasAbstraction:OBDC:55634487",  
  "inCountry": "urn:ngsi-ld:InfrastructureObject:inCountry:AVTY:41307833",  
  "infrastructureMgr": "urn:ngsi-ld:InfrastructureObject:infrastructureMgr:BNRH:79617274",  
  "lineReference": "urn:ngsi-ld:InfrastructureObject:lineReference:XOWU:68775152"  
}  
```  
</details>  
#### InfrastructureObject NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein InfrastructureObject im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureObject:id:QRWO:38616864",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1993-03-01T14:30:32Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1992-12-10T19:47:10Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Admit close national in. Class all question should. Election machine recently general Mrs."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Artist follow sit surface military anything. Instead discover hair. Bank table sure south hard."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Home choose suggest message. Cost perform although I relate."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Bad contain rate president. Option marriage factor important plan service. Forget manage source throw."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Single spring run "  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:InfrastructureObject:items:GAAE:54229861",  
      "urn:ngsi-ld:InfrastructureObject:items:LFCD:71096296"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:InfrastructureObject:items:PGJT:48591099"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          22.2632155,  
          -43.950467  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Internatio"  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Much east health history people million continue. Either cultural quite its throw day section. Test week start clear into air require"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Seem mode"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Small cold lay station new. Every ever star financial. "  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Family goal effort rather. Improve threat five general me general."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Since our wife run hour exist letter. Above seek now rest pick then."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Involve that close few million. Understand wife toward catch off station. Action threat sell mission example."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Production already capital early. Special stage operation break region. Animal hold key bed value continue west. Mission turn less skin beat seem."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Class participant race Mr so account."  
  },  
  "type": "InfrastructureObject",  
  "validityEndDate": {  
    "type": "Text",  
    "value": "Rock officer moment reason. Far deal skin quite. Car inside morning open."  
  },  
  "validityStartDate": {  
    "type": "Text",  
    "value": "Step matter huge full usually. Who offer ever guess up strong age."  
  },  
  "hasAbstraction": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:InfrastructureObject:hasAbstraction:OBDC:55634487"  
  },  
  "inCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:InfrastructureObject:inCountry:AVTY:41307833"  
  },  
  "infrastructureMgr": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:InfrastructureObject:infrastructureMgr:BNRH:79617274"  
  },  
  "lineReference": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:InfrastructureObject:lineReference:XOWU:68775152"  
  }  
}  
```  
</details>  
#### InfrastructureObject NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein InfrastructureObject im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Einheit.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureObject:id:QRWO:38616864",  
  "dateCreated": "1993-03-01T14:30:32Z",  
  "dateModified": "1992-12-10T19:47:10Z",  
  "source": "Admit close national in. Class all question should. Election machine recently general Mrs.",  
  "name": "Artist follow sit surface military anything. Instead discover hair. Bank table sure south hard.",  
  "alternateName": "Home choose suggest message. Cost perform although I relate.",  
  "description": "Bad contain rate president. Option marriage factor important plan service. Forget manage source throw.",  
  "dataProvider": "Single spring run ",  
  "owner": [  
    "urn:ngsi-ld:InfrastructureObject:items:GAAE:54229861",  
    "urn:ngsi-ld:InfrastructureObject:items:LFCD:71096296"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:InfrastructureObject:items:PGJT:48591099"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      22.2632155,  
      -43.950467  
    ]  
  },  
  "address": {  
    "streetAddress": "Internatio",  
    "addressLocality": "Much east health history people million continue. Either cultural quite its throw day section. Test week start clear into air require",  
    "addressRegion": "Seem mode",  
    "addressCountry": "Small cold lay station new. Every ever star financial. ",  
    "postalCode": "Family goal effort rather. Improve threat five general me general.",  
    "postOfficeBoxNumber": "Since our wife run hour exist letter. Above seek now rest pick then.",  
    "streetNr": "Involve that close few million. Understand wife toward catch off station. Action threat sell mission example.",  
    "district": "Production already capital early. Special stage operation break region. Animal hold key bed value continue west. Mission turn less skin beat seem."  
  },  
  "areaServed": "Class participant race Mr so account.",  
  "type": "InfrastructureObject",  
  "validityEndDate": "Rock officer moment reason. Far deal skin quite. Car inside morning open.",  
  "validityStartDate": "Step matter huge full usually. Who offer ever guess up strong age.",  
  "hasAbstraction": "urn:ngsi-ld:InfrastructureObject:hasAbstraction:OBDC:55634487",  
  "inCountry": "urn:ngsi-ld:InfrastructureObject:inCountry:AVTY:41307833",  
  "infrastructureMgr": "urn:ngsi-ld:InfrastructureObject:infrastructureMgr:BNRH:79617274",  
  "lineReference": "urn:ngsi-ld:InfrastructureObject:lineReference:XOWU:68775152",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### InfrastructureObject NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein InfrastructureObject im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Einheit.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureObject:id:EFSX:80680454",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2015-09-08T10:05:37Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1976-03-21T09:16:19Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Cup change sell. Speech oil particular whatever. Six free too base answer set seem."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Herself new item involve player PM spring. Letter whose modern."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Loss least hundred growth. Ready operation finish research air blue."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Must floor good general. New coach hour idea."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Wha"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:InfrastructureObject:items:HVVG:89454448",  
      "urn:ngsi-ld:InfrastructureObject:items:UZLG:94631293"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:InfrastructureObject:items:FFFI:41084289"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.6789965,  
        -133.464788  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "East include foot wonder manager wide wide. Here almost together.",  
      "addressLocality": "Same research hand process frie",  
      "addressRegion": "Action analysis data commercial subject. Condition fund differ",  
      "addressCountry": "These school building Congress happy. Industry reflect network shake media difference happy.",  
      "postalCode": "Per letter score several. Rich kind weight young eight s",  
      "postOfficeBoxNumber": "Itself approach line tonight gas we beyond. Personal wish show memory.",  
      "streetNr": "Measure cultural table positive. Green single huge media.",  
      "district": "After at politics can pass detail letter perform. Enjoy audience process newspaper dea"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Test company bill something card when to. Window soldier involve appear as several truth."  
  },  
  "type": "InfrastructureObject",  
  "validityEndDate": {  
    "type": "Property",  
    "value": "Opportunity material huge evidence. Example federal instead reflect."  
  },  
  "validityStartDate": {  
    "type": "Property",  
    "value": "Growth use think rise return certainly number."  
  },  
  "hasAbstraction": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:InfrastructureObject:hasAbstraction:KQPZ:41036335"  
  },  
  "inCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:InfrastructureObject:inCountry:FSPJ:13261002"  
  },  
  "infrastructureMgr": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:InfrastructureObject:infrastructureMgr:DDQW:47212696"  
  },  
  "lineReference": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:InfrastructureObject:lineReference:OOWF:74664692"  
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

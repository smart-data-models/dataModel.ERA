<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: PhaseInfo    
==================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/PhaseInfo/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Angabe mehrerer erforderlicher Informationen zur Phasentrennung**.    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `phaseInfoKm[number]`: Informationen zur Phase Km  - `phaseInfoLength[number]`: Länge der Phaseninformation  - `phaseInfoPantographLowered[boolean]`: Phaseninfo Stromabnehmer abgesenkt  - `phaseInfoSwitchOffBreaker[boolean]`: Phaseninfo Schalter ausschalten  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `systemSeparationInfoKm[number]`: Informationen zur Systemtrennung Km  - `type[string]`: NGSI-Datentyp. Es muss PhaseInfo sein  <!-- /30-PropertiesList -->    
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
PhaseInfo:      
  description: Indication of required several information on phase separation.      
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
    phaseInfoKm:      
      description: Phase info Km      
      type: number      
      x-ngsi:      
        type: Property      
    phaseInfoLength:      
      description: Phase info length      
      type: number      
      x-ngsi:      
        type: Property      
    phaseInfoPantographLowered:      
      description: Phase info pantograph lowered      
      type: boolean      
      x-ngsi:      
        type: Property      
    phaseInfoSwitchOffBreaker:      
      description: Phase info switch off breaker      
      type: boolean      
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
    systemSeparationInfoKm:      
      description: System separation info Km      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be PhaseInfo      
      enum:      
        - PhaseInfo      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/PhaseInfo      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/PhaseInfo/LICENSE.md      
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
#### PhaseInfo NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine PhaseInfo im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": "2004-07-16T13:48:20Z",  
  "dateModified": "1991-11-29T03:06:21Z",  
  "source": "Enjoy will style car seem recent. Plan theory u",  
  "name": "Rate office focus whole on produce. Argue Mrs care accept momen",  
  "alternateName": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman.",  
  "description": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense.",  
  "dataProvider": "All owner type finish more race adult.",  
  "owner": [  
    "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
    "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      79.5846865,  
      60.386195  
    ]  
  },  
  "address": {  
    "streetAddress": "Toward idea thought. Among drop position election wear.",  
    "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
    "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
    "addressCountry": "Analysis argue so performance itself really for.",  
    "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
    "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
    "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
    "district": "Return anything ma"  
  },  
  "areaServed": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress.",  
  "type": "PhaseInfo",  
  "phaseInfoKm": 37.5,  
  "phaseInfoLength": 864,  
  "phaseInfoPantographLowered": false,  
  "phaseInfoSwitchOffBreaker": false,  
  "systemSeparationInfoKm": 99.4  
}  
```  
</details>    
#### PhaseInfo NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für eine PhaseInfo im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2004-07-16T13:48:20Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1991-11-29T03:06:21Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Enjoy will style car seem recent. Plan theory u"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Rate office focus whole on produce. Argue Mrs care accept momen"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "All owner type finish more race adult."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
      "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        79.5846865,  
        60.386195  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Toward idea thought. Among drop position election wear.",  
      "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
      "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
      "addressCountry": "Analysis argue so performance itself really for.",  
      "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
      "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
      "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
      "district": "Return anything ma"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress."  
  },  
  "type": "PhaseInfo",  
  "phaseInfoKm": {  
    "type": "Number",  
    "value": 37.5  
  },  
  "phaseInfoLength": {  
    "type": "Number",  
    "value": 864  
  },  
  "phaseInfoPantographLowered": {  
    "type": "Boolean",  
    "value": false  
  },  
  "phaseInfoSwitchOffBreaker": {  
    "type": "Boolean",  
    "value": false  
  },  
  "systemSeparationInfoKm": {  
    "type": "Number",  
    "value": 99.4  
  }  
}  
```  
</details>    
#### PhaseInfo NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine PhaseInfo im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": "2004-07-16T13:48:20Z",  
  "dateModified": "1991-11-29T03:06:21Z",  
  "source": "Enjoy will style car seem recent. Plan theory u",  
  "name": "Rate office focus whole on produce. Argue Mrs care accept momen",  
  "alternateName": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman.",  
  "description": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense.",  
  "dataProvider": "All owner type finish more race adult.",  
  "owner": [  
    "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
    "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      79.5846865,  
      60.386195  
    ]  
  },  
  "address": {  
    "streetAddress": "Toward idea thought. Among drop position election wear.",  
    "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
    "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
    "addressCountry": "Analysis argue so performance itself really for.",  
    "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
    "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
    "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
    "district": "Return anything ma"  
  },  
  "areaServed": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress.",  
  "type": "PhaseInfo",  
  "phaseInfoKm": 37.5,  
  "phaseInfoLength": 864,  
  "phaseInfoPantographLowered": false,  
  "phaseInfoSwitchOffBreaker": false,  
  "systemSeparationInfoKm": 99.4,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### PhaseInfo NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für eine PhaseInfo im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:MKUJ:15010698",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1980-01-19T22:02:09Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2008-03-14T12:40:50Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Across air language thoug"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Capital wife fast make similar memory first. Face best choose"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Forward arm back. Sell draw treat water mind series. Movement level ago real study."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Book maybe social but reflect traditional standard"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Office late American morning west economic he. Wide wide rule. Arrive four with measure edge policy."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:ZJGM:93382933",  
      "urn:ngsi-ld:PhaseInfo:items:VXVX:69604579"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:MJIU:47652604"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -83.0057365,  
        76.5777  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Own organization seat everyone. Animal offer indeed send environmental outside.",  
      "addressLocality": "Drop hear pull on remember drop top. Experience once heart word nearly. Every a significant size.",  
      "addressRegion": "Watch cold letter student information. Professor knowledge four meeting customer. Stock point on student tend. Born glass effort someone.",  
      "addressCountry": "Congress dog probably buy time. Product style sport amount clearly than.",  
      "postalCode": "Dr",  
      "postOfficeBoxNumber": "Good agency tend happen dark option. Individual different former then ago month environment single.",  
      "streetNr": "Arrive including smile concern head effort economic. Top pick appear treat. Hour th",  
      "district": "Message movie former mean rather. Health serious base boy action picture. Rate high pay get risk security someone image."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Agency great travel kitchen. Travel certain improve official meet answer concern. Remember specific red."  
  },  
  "type": "PhaseInfo",  
  "phaseInfoKm": {  
    "type": "Property",  
    "value": 187.2  
  },  
  "phaseInfoLength": {  
    "type": "Property",  
    "value": 335  
  },  
  "phaseInfoPantographLowered": {  
    "type": "Property",  
    "value": true  
  },  
  "phaseInfoSwitchOffBreaker": {  
    "type": "Property",  
    "value": true  
  },  
  "systemSeparationInfoKm": {  
    "type": "Property",  
    "value": 198.4  
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

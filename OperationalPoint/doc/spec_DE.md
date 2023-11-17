<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: OperationalPoint    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ERA/blob/master/OperationalPoint/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Allgemeine Beschreibung: **Ein Betriebspunkt (OP) ist jeder Ort, an dem Zugverkehrsdienste beginnen und enden oder die Strecke wechseln können und an dem Personen- oder Güterverkehrsdienste erbracht werden können; ein Betriebspunkt ist auch jeder Ort an den Grenzen zwischen Mitgliedstaaten oder Infrastrukturbetreibern.    
In https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.2 Hauptstandorte (Bahnhöfe, Rangierbahnhöfe, Knotenpunkte, Güterterminals).**    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `borderPointOf[uri]`: Grenzpunkt der  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `digitalSchematicOverview[string]`: Übersicht über digitale Schaltpläne  - `hasSchematicOverviewOPDigitalForm[boolean]`: Hat eine schematische Übersicht in digitaler Form  - `id[*]`: Eindeutiger Bezeichner der Entität  - `localRulesOrRestrictions[boolean]`: Vorhandensein von Vorschriften und Beschränkungen rein lokaler Natur.  - `localRulesOrRestrictionsDoc[string]`: Dokumente zu den vom IM zur Verfügung gestellten Vorschriften oder Einschränkungen rein lokaler Natur  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `opInfoPerCountry[uri]`: Informationen zu den Grenzübergängen pro Land  - `opName[string]`: Name der Einsatzstelle  - `opType[uri]`: Art der Einsatzstelle  - `opTypeGaugeChangeover[string]`: Art der Einrichtung zur Spurweitenumstellung  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `schematicOverviewOP[string]`: Schematischer Überblick über die Einsatzstelle  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `siding[uri]`: Abstellgleis  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `tafTAPCode[string]`: Primärer Standortcode, der für den Informationsaustausch gemäß den TSI für Telematikanwendungen entwickelt wurde.  - `track[uri]`: Spur  - `type[string]`: NGSI-Datentyp. Es muss OperationalPoint sein  - `uopid[string]`: Eindeutige OP-ID  <!-- /30-PropertiesList -->    
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
## Beispiel-Nutzlasten    
#### OperationalPoint NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen OperationalPoint im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### OperationalPoint NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für einen OperationalPoint im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
      "coordinates": [  
        -87.0756655,  
        -98.077607  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Recently southern war measure. Behind collection relationship something. Join blue expert should happy according deal.",  
      "addressLocality": "Community sit about space need win man. Prevent place we whatever image stock.",  
      "addressRegion": "Into his give degree however.",  
      "addressCountry": "Identify couple five deep bar popular product not. Design sell security trip never adult heart course.",  
      "postalCode": "Product five yourself open. Purpose decade ",  
      "postOfficeBoxNumber": "Involve argue cup subject arm bab",  
      "streetNr": "Fish share ",  
      "district": "Speech customer perhaps ball defense attorney. Pattern indeed bank result hear. Society different open health. Back reduce his know green next produce."  
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
#### OperationalPoint NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für einen OperationalPoint im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### OperationalPoint NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen OperationalPoint im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Capacità di carico    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/LoadCapability/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Questa classe, insieme alle proprietà loadCapabilityLineCategory e loadCapabilitySpeed, sostituisce la precedente proprietà loadCapability SKOS.    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica      
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `loadCapabilityLineCategory[uri]`: Categoria di linea della capacità di carico  - `loadCapabilitySpeed[number]`: Velocità della capacità di carico  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di dati NGSI. Deve essere LoadCapability  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
modello di dati mappato dall'ontologia ERA https://data-interop.era.europa.eu/era-vocabulary (Agenzia dell'Unione Europea per le Ferrovie)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### LoadCapability Valori chiave NGSI-v2 Esempio    
Ecco un esempio di LoadCapability in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### LoadCapability NGSI-v2 normalizzato Esempio    
Ecco un esempio di LoadCapability in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.    
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
#### LoadCapability Valori chiave NGSI-LD Esempio    
Ecco un esempio di LoadCapability in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### LoadCapability NGSI-LD normalizzato Esempio    
Ecco un esempio di LoadCapability in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

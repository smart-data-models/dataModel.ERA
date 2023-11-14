<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: SpecialTunnelArea  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/SpecialTunnelArea/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Area o luogo all'interno di una galleria in cui sono presenti un passaggio, punti di evacuazione e di soccorso.  
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di dati NGSI. Deve essere SpecialTunnelArea  <!-- /30-PropertiesList -->  
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
SpecialTunnelArea:    
  description: 'Area or location within a tunnel where  there is a walkway, evacuation and rescue points.'    
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
      description: NGSI data type. It has to be SpecialTunnelArea    
      enum:    
        - SpecialTunnelArea    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/SpecialTunnelArea    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SpecialTunnelArea/LICENSE.md    
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
#### SpecialTunnelArea Valori chiave NGSI-v2 Esempio  
Ecco un esempio di SpecialTunnelArea in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": "1988-01-11T13:27:45Z",  
  "dateModified": "2010-12-08T20:17:03Z",  
  "source": "Owner kid middle worry po",  
  "name": "Idea able accept. Always four majority education wait. South east t",  
  "alternateName": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two.",  
  "description": "Center these own security subject ability once. Catch animal office poor.",  
  "dataProvider": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve.",  
  "owner": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
    "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.1411545,  
      -167.120745  
    ]  
  },  
  "address": {  
    "streetAddress": "Build next e",  
    "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
    "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
    "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
    "postalCode": "Environmental bag officer do ball. Soc",  
    "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
    "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
    "district": "Pattern over scientist important"  
  },  
  "areaServed": "Current upon put current. His find imagine high course why sea.",  
  "type": "SpecialTunnelArea",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SpecialTunnelArea NGSI-v2 normalizzato Esempio  
Ecco un esempio di SpecialTunnelArea in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1988-01-11T13:27:45Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2010-12-08T20:17:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Owner kid middle worry po"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Idea able accept. Always four majority education wait. South east t"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Center these own security subject ability once. Catch animal office poor."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
      "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -4.1411545,  
          -167.120745  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Build next e"  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Special campaign he two final actually before treat. Continue miss be young "  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Upon writer local bring last agent seem. Wind participant seem ask try various image."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Trouble phone be. Health last brother attack defense power identify."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Environmental bag officer do ball. Soc"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Arrive question describe throughout official contain which. Wife as te"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Focus still amount him individual number ground. Piece chair opportunity most become."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Pattern over scientist important"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Current upon put current. His find imagine high course why sea."  
  },  
  "type": "SpecialTunnelArea",  
  "context": {  
    "type": "StructuredValue",  
    "value": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
    ]  
  }  
}  
```  
</details>  
#### SpecialTunnelArea Valori chiave NGSI-LD Esempio  
Ecco un esempio di SpecialTunnelArea in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": "1988-01-11T13:27:45Z",  
  "dateModified": "2010-12-08T20:17:03Z",  
  "source": "Owner kid middle worry po",  
  "name": "Idea able accept. Always four majority education wait. South east t",  
  "alternateName": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two.",  
  "description": "Center these own security subject ability once. Catch animal office poor.",  
  "dataProvider": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve.",  
  "owner": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
    "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.1411545,  
      -167.120745  
    ]  
  },  
  "address": {  
    "streetAddress": "Build next e",  
    "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
    "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
    "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
    "postalCode": "Environmental bag officer do ball. Soc",  
    "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
    "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
    "district": "Pattern over scientist important"  
  },  
  "areaServed": "Current upon put current. His find imagine high course why sea.",  
  "type": "SpecialTunnelArea",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SpecialTunnelArea NGSI-LD normalizzato Esempio  
Ecco un esempio di SpecialTunnelArea in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:INWI:10579735",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1992-01-22T20:24:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1980-02-15T17:27:55Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Three consumer rise certain and. Share operation "  
  },  
  "name": {  
    "type": "Property",  
    "value": "Should program heart effort often not. Black though believe theory choice travel level. Positive big right beat television respond run."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Commercial share budget. Mention industry build."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Friend save analysis event. Summer hospital box site hold matter agency. Measure gun"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Arrive read pattern be despite second matter. Thank teach oil his."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:TUJB:41707682",  
      "urn:ngsi-ld:SpecialTunnelArea:items:UXYT:76593602"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:JGSZ:99017778"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.77738,  
        -119.777978  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "On boy cell night. Sit stage difficult take onto best.",  
      "addressLocality": "East south bill former business federal argue. These machine their war. Vote because born natural",  
      "addressRegion": "Eye occur contain rest. Determine child interest action boy begin more.",  
      "addressCountry": "On home time left. Rather necessary talk same almost. Card computer see security.",  
      "postalCode": "State positive assume themselves media. Tax food while. Write eye st",  
      "postOfficeBoxNumber": "Role call wrong arrive marriage meet authority foreign. Show paper difficult really increase. Difference company free medical rich.",  
      "streetNr": "Use but left assume. Safe be during soldier. Natural success before begin part.",  
      "district": "White hand we return less. Product movie season man."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Those production act story gun necessary such. Almost space without. Herself pressure miss anyone contain car."  
  },  
  "type": "SpecialTunnelArea",  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

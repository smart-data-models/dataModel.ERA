<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: MassimoCampoMagnetico    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/MaximumMagneticField/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **I limiti massimi di campo magnetico consentiti per i conta-assi (in dBµA/m) per una banda di frequenza definita.    
Dovrebbe essere fornito in 3 direzioni.**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica      
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maximumMagneticFieldDirectionX[number]`: Direzione massima del campo magnetico X  - `maximumMagneticFieldDirectionY[number]`: Direzione massima del campo magnetico Y  - `maximumMagneticFieldDirectionZ[number]`: Direzione massima del campo magnetico Z  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di dati NGSI. Deve essere MaximumMagneticField (campo magnetico massimo).  <!-- /30-PropertiesList -->    
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
MaximumMagneticField:      
  description: |-      
    The maximum magnetic field limits allowed for axle counters (in dBµA/m) for a defined frequency band.      
    It should be provided in 3 directions.      
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
    maximumMagneticFieldDirectionX:      
      description: Maximum magnetic field direction X      
      type: number      
      x-ngsi:      
        type: Property      
    maximumMagneticFieldDirectionY:      
      description: Maximum magnetic field direction Y      
      type: number      
      x-ngsi:      
        type: Property      
    maximumMagneticFieldDirectionZ:      
      description: Maximum magnetic field direction Z      
      type: number      
      x-ngsi:      
        type: Property      
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
      description: NGSI data type. It has to be MaximumMagneticField      
      enum:      
        - MaximumMagneticField      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/MaximumMagneticField      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/MaximumMagneticField/LICENSE.md      
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
#### MaximumMagneticField Valori chiave NGSI-v2 Esempio    
Ecco un esempio di un campo MaximumMagneticField in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": "1992-07-01T01:29:02Z",  
  "dateModified": "2022-07-21T07:13:50Z",  
  "source": "Method modern phone whatever thing. Discussion example your dog fund serv",  
  "name": "Nothing church tonight church do",  
  "alternateName": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve.",  
  "description": "Difficu",  
  "dataProvider": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r",  
  "owner": [  
    "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
    "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      12.1959295,  
      -80.960856  
    ]  
  },  
  "address": {  
    "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
    "addressLocality": "Region may realize sign my. Wester",  
    "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
    "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
    "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
    "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
    "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
    "district": "Allow site finally evidence green."  
  },  
  "areaServed": "Employee they catch fight suggest. Executive positive eight piece.",  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": 864,  
  "maximumMagneticFieldDirectionY": 864,  
  "maximumMagneticFieldDirectionZ": 864,  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Campo magnetico massimo NGSI-v2 normalizzato Esempio    
Ecco un esempio di campo MaximumMagneticField in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1992-07-01T01:29:02Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2022-07-21T07:13:50Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Method modern phone whatever thing. Discussion example your dog fund serv"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Nothing church tonight church do"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Difficu"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
      "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        12.1959295,  
        -80.960856  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
      "addressLocality": "Region may realize sign my. Wester",  
      "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
      "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
      "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
      "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
      "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
      "district": "Allow site finally evidence green."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Employee they catch fight suggest. Executive positive eight piece."  
  },  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumMagneticFieldDirectionY": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumMagneticFieldDirectionZ": {  
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
#### Campo magnetico massimo Valori chiave NGSI-LD Esempio    
Ecco un esempio di un campo MaximumMagneticField in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": "1992-07-01T01:29:02Z",  
  "dateModified": "2022-07-21T07:13:50Z",  
  "source": "Method modern phone whatever thing. Discussion example your dog fund serv",  
  "name": "Nothing church tonight church do",  
  "alternateName": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve.",  
  "description": "Difficu",  
  "dataProvider": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r",  
  "owner": [  
    "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
    "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      12.1959295,  
      -80.960856  
    ]  
  },  
  "address": {  
    "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
    "addressLocality": "Region may realize sign my. Wester",  
    "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
    "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
    "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
    "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
    "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
    "district": "Allow site finally evidence green."  
  },  
  "areaServed": "Employee they catch fight suggest. Executive positive eight piece.",  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": 864,  
  "maximumMagneticFieldDirectionY": 864,  
  "maximumMagneticFieldDirectionZ": 864,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Campo magnetico massimo NGSI-LD normalizzato Esempio    
Ecco un esempio di campo MaximumMagneticField in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:XYSL:59916457",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-01-17T00:20:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1971-04-03T19:24:25Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Seek material four bed eat foot four cut. Industry medical human yet collection."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Everyone safe interesting eat. Again might live manager. Surf"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Here people p"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Activity treat its in. Also step board might truth small interesting."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Article care radio win program responsibility water. South expect yard past most team. Raise population since meet between set."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:QGWL:53478074",  
      "urn:ngsi-ld:MaximumMagneticField:items:IBUO:48085735"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:XXHU:41714471"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.077867,  
        60.671442  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "West trial language field. Stock high senior success go whole.",  
      "addressLocality": "Community catch mission perhaps especially option degree. Create option part not return draw identify art. Success relate series according.",  
      "addressRegion": "List successful a during loss nor. Conference hit well far f",  
      "addressCountry": "Our seem scientist. Hot group true design season crime. Far safe miss doctor.",  
      "postalCode": "Interesting top success try.",  
      "postOfficeBoxNumber": "Huge foot truth ball. ",  
      "streetNr": "Land need cold question.",  
      "district": "Throughout way floor believe movie. Off police in begin. Whatever heart half or already window."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Say already life discuss determine heart. Edge someone parent all her down."  
  },  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": {  
    "type": "Property",  
    "value": 671  
  },  
  "maximumMagneticFieldDirectionY": {  
    "type": "Property",  
    "value": 707  
  },  
  "maximumMagneticFieldDirectionZ": {  
    "type": "Property",  
    "value": 262  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

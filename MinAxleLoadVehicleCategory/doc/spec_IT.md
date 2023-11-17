<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: MinAxleLoadVehicleCategory    
==================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/MinAxleLoadVehicleCategory/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Deprezzato in base alla modifica del regolamento (UE) 2019/777. Rappresenta un'informazione che indica il carico in tonnellate a seconda della categoria del veicolo. Le sue proprietà sono minAxleLoadVehicleCategory e minAxleLoad.**    
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `minAxleLoad[number]`: Carico minimo consentito per asse  - `minAxleLoadVehicleCategory[uri]`: Carico minimo per asse Categoria di veicoli  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di dati NGSI. Deve essere MinAxleLoadVehicleCategory (categoria di veicolo).  <!-- /30-PropertiesList -->    
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
MinAxleLoadVehicleCategory:      
  description: Deprecated according to the ammendment to the Regulation (EU) 2019/777. Represents information that indicates the load given in tons depending of the category of vehicle. Its properties are minAxleLoadVehicleCategory and minAxleLoad.      
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
    minAxleLoad:      
      description: Minimum permitted axle load      
      type: number      
      x-ngsi:      
        type: Property      
    minAxleLoadVehicleCategory:      
      description: Minimum axle load vehicle category      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
      description: NGSI data type. It has to be MinAxleLoadVehicleCategory      
      enum:      
        - MinAxleLoadVehicleCategory      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/MinAxleLoadVehicleCategory      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/MinAxleLoadVehicleCategory/LICENSE.md      
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
#### Valori chiave NGSI-v2 di MinAxleLoadVehicleCategory Esempio    
Ecco un esempio di una categoria MinAxleLoadVehicleCategory in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:KWOE:64087129",  
  "dateCreated": "2022-03-10T13:47:11Z",  
  "dateModified": "2000-12-08T03:53:13Z",  
  "source": "Address company tonight fight side night apply so. Best fine house past drug evening.",  
  "name": "Read church top never history old. Born edge health strong ",  
  "alternateName": "Lot material matter present from line cost. Season whatever become all wall.",  
  "description": "Not people Congress view window one.",  
  "dataProvider": "Stock minute pretty later. Federal as re",  
  "owner": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:JRVO:17137719",  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:WMGE:53516876"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:TXBP:98820710"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.8985275,  
      -11.102786  
    ]  
  },  
  "address": {  
    "streetAddress": "Accept treat however pretty manage. Term those sit seek ahead through. Camera attorney commercia",  
    "addressLocality": "Manager general nation behind. Prevent comput",  
    "addressRegion": "Song nature part. Degree ev",  
    "addressCountry": "Huge pressure ball music. Role chance govern",  
    "postalCode": "Really ago you director into little manager. Forget national never event important idea attorney. Small think rule individual player.",  
    "postOfficeBoxNumber": "Laugh front history fish four area. Quickly structure glass ne",  
    "streetNr": "Though guy police have chair learn member alone. Camera at if describe Ame",  
    "district": "Fear laugh continue. Read one teacher agency wear nothing customer. Great clear "  
  },  
  "areaServed": "Cultural worry floor professional focus. Need event ma",  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": 953.2,  
  "minAxleLoadVehicleCategory": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UHRQ:86221678"  
}  
```  
</details>    
#### MinAxleLoadVehicleCategory NGSI-v2 normalizzato Esempio    
Ecco un esempio di MinAxleLoadVehicleCategory in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:KWOE:64087129",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2022-03-10T13:47:11Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2000-12-08T03:53:13Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Address company tonight fight side night apply so. Best fine house past drug evening."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Read church top never history old. Born edge health strong "  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Lot material matter present from line cost. Season whatever become all wall."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Not people Congress view window one."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Stock minute pretty later. Federal as re"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:JRVO:17137719",  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:WMGE:53516876"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:TXBP:98820710"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        48.8985275,  
        -11.102786  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Accept treat however pretty manage. Term those sit seek ahead through. Camera attorney commercia",  
      "addressLocality": "Manager general nation behind. Prevent comput",  
      "addressRegion": "Song nature part. Degree ev",  
      "addressCountry": "Huge pressure ball music. Role chance govern",  
      "postalCode": "Really ago you director into little manager. Forget national never event important idea attorney. Small think rule individual player.",  
      "postOfficeBoxNumber": "Laugh front history fish four area. Quickly structure glass ne",  
      "streetNr": "Though guy police have chair learn member alone. Camera at if describe Ame",  
      "district": "Fear laugh continue. Read one teacher agency wear nothing customer. Great clear "  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Cultural worry floor professional focus. Need event ma"  
  },  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": {  
    "type": "Number",  
    "value": 953.2  
  },  
  "minAxleLoadVehicleCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UHRQ:86221678"  
  }  
}  
```  
</details>    
#### Valori chiave NGSI-LD di MinAxleLoadVehicleCategory Esempio    
Ecco un esempio di una categoria MinAxleLoadVehicleCategory in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:KWOE:64087129",  
  "dateCreated": "2022-03-10T13:47:11Z",  
  "dateModified": "2000-12-08T03:53:13Z",  
  "source": "Address company tonight fight side night apply so. Best fine house past drug evening.",  
  "name": "Read church top never history old. Born edge health strong ",  
  "alternateName": "Lot material matter present from line cost. Season whatever become all wall.",  
  "description": "Not people Congress view window one.",  
  "dataProvider": "Stock minute pretty later. Federal as re",  
  "owner": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:JRVO:17137719",  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:WMGE:53516876"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:TXBP:98820710"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.8985275,  
      -11.102786  
    ]  
  },  
  "address": {  
    "streetAddress": "Accept treat however pretty manage. Term those sit seek ahead through. Camera attorney commercia",  
    "addressLocality": "Manager general nation behind. Prevent comput",  
    "addressRegion": "Song nature part. Degree ev",  
    "addressCountry": "Huge pressure ball music. Role chance govern",  
    "postalCode": "Really ago you director into little manager. Forget national never event important idea attorney. Small think rule individual player.",  
    "postOfficeBoxNumber": "Laugh front history fish four area. Quickly structure glass ne",  
    "streetNr": "Though guy police have chair learn member alone. Camera at if describe Ame",  
    "district": "Fear laugh continue. Read one teacher agency wear nothing customer. Great clear "  
  },  
  "areaServed": "Cultural worry floor professional focus. Need event ma",  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": 953.2,  
  "minAxleLoadVehicleCategory": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UHRQ:86221678",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Categoria di carico minimo del veicolo NGSI-LD normalizzato Esempio    
Ecco un esempio di categoria MinAxleLoadVehicleCategory in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:OTDA:84082973",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2015-01-14T11:01:00Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2019-02-23T06:12:58Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Doctor report certainly capital account finally. Science piece Republican identify. Ever recent cost account guess."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Suddenly something particular. Six front desig"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Politics total upon under fear. Know behind after draw billion."  
  },  
  "description": {  
    "type": "Property",  
    "value": "With b"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Glass ago movem"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:UQZZ:42282728",  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:YAYE:91747118"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:FXFD:61807381"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.690969,  
        -150.542766  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Usually attorney ",  
      "addressLocality": "Nothing mind herself table. Again human camera",  
      "addressRegion": "Night party decade meet attack war. Father ready though leader peace development close newspa",  
      "addressCountry": "Mean provide government on. Amount although education start baby third scientist.",  
      "postalCode": "Give project central available class interest good. Author affect next west.",  
      "postOfficeBoxNumber": "Three successful reason happy. Simply movement really make walk nor.",  
      "streetNr": "Activity with positi",  
      "district": "Reason l"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Opportunity easy year night hospital. Image son computer. Company state apply down idea term."  
  },  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": {  
    "type": "Property",  
    "value": 939.1  
  },  
  "minAxleLoadVehicleCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UYDT:81696890"  
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

<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: LineaRiferimento  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/LineReference/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Luogo ferroviario**  
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `kilometer[number]`: Chilometro  - `lineNationalId[uri]`: Identificazione della linea nazionale  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di dati NGSI. Deve essere LineReference  <!-- /30-PropertiesList -->  
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
LineReference:    
  description: Railway location    
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
    kilometer:    
      description: Kilometer    
      type: number    
      x-ngsi:    
        type: Property    
    lineNationalId:    
      description: National line identification    
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
      description: NGSI data type. It has to be LineReference    
      enum:    
        - LineReference    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/LineReference    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/LineReference/LICENSE.md    
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
#### Linea di riferimento Valori chiave NGSI-v2 Esempio  
Ecco un esempio di LineReference in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:LineReference:id:RHSX:14820983",  
  "dateCreated": "1986-10-27T03:38:58Z",  
  "dateModified": "1977-09-15T07:25:57Z",  
  "source": "New create receive low hotel speech doctor political. Skin new shake view.",  
  "name": "Mind develop police. Change bill thing. Figure nation piece clearly detail others usually. Street writer four establish industr",  
  "alternateName": "Day toward including sometimes. Require ",  
  "description": "Project represent voice project decision yes total. Support idea ",  
  "dataProvider": "Class figure quality she. Continue traditional follow. Civil tough middle act beat.",  
  "owner": [  
    "urn:ngsi-ld:LineReference:items:NUGB:26269993",  
    "urn:ngsi-ld:LineReference:items:GVBX:53792463"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:LineReference:items:FXDW:87126015"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -45.052783,  
      152.191861  
    ]  
  },  
  "address": {  
    "streetAddress": "Western technology water budget everybody. Phone bring kitchen same. Impact policy head serve nothing.",  
    "addressLocality": "Its position them treat few whose compare. Into ok key general next foreign. Among agency kitchen along usually position.",  
    "addressRegion": "Miss important simply economy finish left stuff. Help cover particularly idea. Only chair agree.",  
    "addressCountry": "Town computer thank rather. Break onto money tend.",  
    "postalCode": "Back blue finally suffer notice. Weight fu",  
    "postOfficeBoxNumber": "Any pers",  
    "streetNr": "Mother traditional run campaign.",  
    "district": "Official situation tonight north tough sound. Debate project player car structure vote. Poo"  
  },  
  "areaServed": "Red animal wall front. Left buy see always.",  
  "type": "LineReference",  
  "kilometer": 239.9,  
  "lineNationalId": "urn:ngsi-ld:LineReference:lineNationalId:IIBS:67837023",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Riferimento di linea NGSI-v2 normalizzato Esempio  
Ecco un esempio di LineReference in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:LineReference:id:RHSX:14820983",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1986-10-27T03:38:58Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1977-09-15T07:25:57Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "New create receive low hotel speech doctor political. Skin new shake view."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Mind develop police. Change bill thing. Figure nation piece clearly detail others usually. Street writer four establish industr"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Day toward including sometimes. Require "  
  },  
  "description": {  
    "type": "Text",  
    "value": "Project represent voice project decision yes total. Support idea "  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Class figure quality she. Continue traditional follow. Civil tough middle act beat."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:NUGB:26269993",  
      "urn:ngsi-ld:LineReference:items:GVBX:53792463"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:FXDW:87126015"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -45.052783,  
          152.191861  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Western technology water budget everybody. Phone bring kitchen same. Impact policy head serve nothing."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Its position them treat few whose compare. Into ok key general next foreign. Among agency kitchen along usually position."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Miss important simply economy finish left stuff. Help cover particularly idea. Only chair agree."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Town computer thank rather. Break onto money tend."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Back blue finally suffer notice. Weight fu"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Any pers"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Mother traditional run campaign."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Official situation tonight north tough sound. Debate project player car structure vote. Poo"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Red animal wall front. Left buy see always."  
  },  
  "type": "LineReference",  
  "kilometer": {  
    "type": "Number",  
    "value": 239.9  
  },  
  "lineNationalId": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:LineReference:lineNationalId:IIBS:67837023"  
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
#### Linea di riferimento Valori chiave NGSI-LD Esempio  
Ecco un esempio di LineReference in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:LineReference:id:RHSX:14820983",  
  "dateCreated": "1986-10-27T03:38:58Z",  
  "dateModified": "1977-09-15T07:25:57Z",  
  "source": "New create receive low hotel speech doctor political. Skin new shake view.",  
  "name": "Mind develop police. Change bill thing. Figure nation piece clearly detail others usually. Street writer four establish industr",  
  "alternateName": "Day toward including sometimes. Require ",  
  "description": "Project represent voice project decision yes total. Support idea ",  
  "dataProvider": "Class figure quality she. Continue traditional follow. Civil tough middle act beat.",  
  "owner": [  
    "urn:ngsi-ld:LineReference:items:NUGB:26269993",  
    "urn:ngsi-ld:LineReference:items:GVBX:53792463"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:LineReference:items:FXDW:87126015"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -45.052783,  
      152.191861  
    ]  
  },  
  "address": {  
    "streetAddress": "Western technology water budget everybody. Phone bring kitchen same. Impact policy head serve nothing.",  
    "addressLocality": "Its position them treat few whose compare. Into ok key general next foreign. Among agency kitchen along usually position.",  
    "addressRegion": "Miss important simply economy finish left stuff. Help cover particularly idea. Only chair agree.",  
    "addressCountry": "Town computer thank rather. Break onto money tend.",  
    "postalCode": "Back blue finally suffer notice. Weight fu",  
    "postOfficeBoxNumber": "Any pers",  
    "streetNr": "Mother traditional run campaign.",  
    "district": "Official situation tonight north tough sound. Debate project player car structure vote. Poo"  
  },  
  "areaServed": "Red animal wall front. Left buy see always.",  
  "type": "LineReference",  
  "kilometer": 239.9,  
  "lineNationalId": "urn:ngsi-ld:LineReference:lineNationalId:IIBS:67837023",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Riferimento di linea NGSI-LD normalizzato Esempio  
Ecco un esempio di LineReference in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:LineReference:id:UGOL:02314727",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-09-26T20:09:19Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1986-05-17T22:22:32Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Himself peace act."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Among safe number anyone white. Away success listen hot stock road. Early though question economy cause share defense."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Realize huma"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Control get personal raise r"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Drive understand apply town research big. Together hundred event seem back."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:ODGA:61913437",  
      "urn:ngsi-ld:LineReference:items:TQIE:40363820"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:LineReference:items:EVEX:08441746"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        46.8926945,  
        -133.98211  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Quite manage event shoulder nation ago. Measure treat nor receive there person. Stay vote",  
      "addressLocality": "Instead air fight minute. Place arm ball end career foreign type size. Morning stuff necessary again.",  
      "addressRegion": "Before account article. Tough pattern himself TV mention strong consumer. Name painting want sing alone.",  
      "addressCountry": "Assume nature organization over. People establish relationship ago. Between seem sport when agent",  
      "postalCode": "Green by seem despite. Yard early tax security five. Traditional red discover interest past if. Happ",  
      "postOfficeBoxNumber": "Check would effect fight best ",  
      "streetNr": "Magazine eat teacher list trial already career his. Yet concern wan",  
      "district": "Adult administration always seat explain."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Security each election well position. Including without official truth past bit. Group or rest whatever he."  
  },  
  "type": "LineReference",  
  "kilometer": {  
    "type": "Property",  
    "value": 890.1  
  },  
  "lineNationalId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:LineReference:lineNationalId:HTQW:41563123"  
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

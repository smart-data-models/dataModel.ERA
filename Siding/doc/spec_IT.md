<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Rivestimento  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/Siding/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **I binari di raccordo sono tutti quei binari in cui termina la circolazione dei treni in servizio e che non sono utilizzati per l'instradamento operativo di un treno **.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo stradale e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel Paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `demonstrationINF[string]`: Dichiarazione di dimostrazione EI per binari/paratie [INF]  - `description[string]`: Descrizione dell'articolo  - `gradient[number]`: Gradiente per i binari di stazionamento  - `hasElectricShoreSupply[boolean]`: Esistenza di una rete elettrica di terra  - `hasExternalCleaning[boolean]`: Esistenza di strutture di pulizia esterne  - `hasRefuelling[boolean]`: Esistenza di un rifornimento di carburante  - `hasSandRestocking[boolean]`: Esistenza di un ripopolamento di sabbia  - `hasToiletDischarge[boolean]`: Esistenza di scarichi igienici  - `hasWaterRestocking[boolean]`: Esistenza di un rifornimento idrico  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maxCurrentStandstillPantograph[number]`: Corrente massima a riposo per pantografo  - `minimumHorizontalRadius[number]`: Raggio minimo della curva orizzontale  - `minimumVerticalRadius[string]`: Raggio minimo della curva verticale  - `minimumVerticalRadiusCrest[number]`: Raggio minimo della cresta della curva verticale  - `minimumVerticalRadiusHollow[number]`: Raggio minimo della curva verticale cava  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sidingId[string]`: Identificazione del rivestimento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `tenClassification[uri]`: Classificazione TEN (di binario, di piattaforma, di binario di raccordo)  - `type[string]`: Tipo di dati NGSI. Deve essere Siding  - `verificationINF[string]`: Dichiarazione di verifica CE per binari/accompagnamento [INF]  <!-- /30-PropertiesList -->  
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
Siding:    
  description: Sidings are all those tracks where running trains in service movements ends and which are not used for operational routing of a train.    
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
    demonstrationINF:    
      description: 'EI declaration of demonstration for track/siding [INF]'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    gradient:    
      description: Gradient for stabling tracks    
      type: number    
      x-ngsi:    
        type: Property    
    hasElectricShoreSupply:    
      description: Existence of electric shore supply    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasExternalCleaning:    
      description: Existence of external cleaning facilities    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasRefuelling:    
      description: Existence of refuelling    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasSandRestocking:    
      description: Existence of sand restocking    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasToiletDischarge:    
      description: Existence of toilet discharge    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasWaterRestocking:    
      description: Existence of water restocking    
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
    maxCurrentStandstillPantograph:    
      description: Maximum current at standstill per pantograph    
      type: number    
      x-ngsi:    
        type: Property    
    minimumHorizontalRadius:    
      description: Minimum radius of horizontal curve    
      type: number    
      x-ngsi:    
        type: Property    
    minimumVerticalRadius:    
      description: Minimum radius of vertical curve    
      type: string    
      x-ngsi:    
        type: Property    
    minimumVerticalRadiusCrest:    
      description: Minimum radius of vertical curve crest    
      type: number    
      x-ngsi:    
        type: Property    
    minimumVerticalRadiusHollow:    
      description: Minimum radius of vertical curve hollow    
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
    sidingId:    
      description: Identification of siding    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    tenClassification:    
      description: 'TEN classification (of track, of platform, of siding)'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI data type. It has to be Siding    
      enum:    
        - Siding    
      type: string    
      x-ngsi:    
        type: Property    
    verificationINF:    
      description: 'EC declaration of verification for track/siding [INF]'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Siding    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Siding/LICENSE.md    
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
#### Esempio di valori-chiave del rivestimento NGSI-v2  
Ecco un esempio di un binario di raccordo in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": "2013-05-04T09:51:15Z",  
  "dateModified": "1974-05-09T12:06:14Z",  
  "source": "Push list then again. State get suddenly nor table.",  
  "name": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s",  
  "alternateName": "Name down over test feeling Congress. Recent his his back partner reduce material your.",  
  "description": "Anything so doctor finally. Despite practice class store.",  
  "dataProvider": "Us which she quickly else party. Way that give main air short near. Real popular whatever s",  
  "owner": [  
    "urn:ngsi-ld:Siding:items:SXEI:27228317",  
    "urn:ngsi-ld:Siding:items:EIZG:41039273"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Siding:items:DOKD:91972812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.875369,  
      98.837859  
    ]  
  },  
  "address": {  
    "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
    "addressLocality": "Since ",  
    "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
    "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
    "postalCode": "Personal build",  
    "postOfficeBoxNumber": "Leader enough weight everything.",  
    "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
    "district": "Area cost hundred same. Sense anyone anyone."  
  },  
  "areaServed": "Moment agent four language. Tend place r",  
  "type": "Siding",  
  "demonstrationINF": "Its federal stand tr",  
  "gradient": 354.9,  
  "hasElectricShoreSupply": true,  
  "hasExternalCleaning": true,  
  "hasRefuelling": true,  
  "hasSandRestocking": false,  
  "hasToiletDischarge": false,  
  "hasWaterRestocking": false,  
  "maxCurrentStandstillPantograph": 81.3,  
  "minimumHorizontalRadius": 864,  
  "minimumVerticalRadius": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "minimumVerticalRadiusCrest": 864,  
  "minimumVerticalRadiusHollow": 864,  
  "sidingId": "American whole magazine",  
  "verificationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "tenClassification": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097"  
}  
```  
</details>  
#### Rivestimento NGSI-v2 normalizzato Esempio  
Ecco un esempio di un binario di raccordo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2013-05-04T09:51:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1974-05-09T12:06:14Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Push list then again. State get suddenly nor table."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Name down over test feeling Congress. Recent his his back partner reduce material your."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Anything so doctor finally. Despite practice class store."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Us which she quickly else party. Way that give main air short near. Real popular whatever s"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Siding:items:SXEI:27228317",  
      "urn:ngsi-ld:Siding:items:EIZG:41039273"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Siding:items:DOKD:91972812"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -36.875369,  
          98.837859  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Since "  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Radio across best yard. Central until beyond knowledge care matter. Without air d"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Argue data get fire. Water opportunity citizen. Score interview letter evidence."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Personal build"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Leader enough weight everything."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Area cost hundred same. Sense anyone anyone."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Moment agent four language. Tend place r"  
  },  
  "type": "Siding",  
  "demonstrationINF": {  
    "type": "Text",  
    "value": "Its federal stand tr"  
  },  
  "gradient": {  
    "type": "Number",  
    "value": 354.9  
  },  
  "hasElectricShoreSupply": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasExternalCleaning": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasRefuelling": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasSandRestocking": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasToiletDischarge": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasWaterRestocking": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Number",  
    "value": 81.3  
  },  
  "minimumHorizontalRadius": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumVerticalRadius": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "minimumVerticalRadiusCrest": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumVerticalRadiusHollow": {  
    "type": "Number",  
    "value": 864  
  },  
  "sidingId": {  
    "type": "Text",  
    "value": "American whole magazine"  
  },  
  "verificationINF": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "tenClassification": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097"  
  }  
}  
```  
</details>  
#### Esempio di valori chiave NGSI-LD per il rivestimento Esempio  
Ecco un esempio di un binario di raccordo in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": "2013-05-04T09:51:15Z",  
  "dateModified": "1974-05-09T12:06:14Z",  
  "source": "Push list then again. State get suddenly nor table.",  
  "name": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s",  
  "alternateName": "Name down over test feeling Congress. Recent his his back partner reduce material your.",  
  "description": "Anything so doctor finally. Despite practice class store.",  
  "dataProvider": "Us which she quickly else party. Way that give main air short near. Real popular whatever s",  
  "owner": [  
    "urn:ngsi-ld:Siding:items:SXEI:27228317",  
    "urn:ngsi-ld:Siding:items:EIZG:41039273"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Siding:items:DOKD:91972812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.875369,  
      98.837859  
    ]  
  },  
  "address": {  
    "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
    "addressLocality": "Since ",  
    "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
    "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
    "postalCode": "Personal build",  
    "postOfficeBoxNumber": "Leader enough weight everything.",  
    "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
    "district": "Area cost hundred same. Sense anyone anyone."  
  },  
  "areaServed": "Moment agent four language. Tend place r",  
  "type": "Siding",  
  "demonstrationINF": "Its federal stand tr",  
  "gradient": 354.9,  
  "hasElectricShoreSupply": true,  
  "hasExternalCleaning": true,  
  "hasRefuelling": true,  
  "hasSandRestocking": false,  
  "hasToiletDischarge": false,  
  "hasWaterRestocking": false,  
  "maxCurrentStandstillPantograph": 81.3,  
  "minimumHorizontalRadius": 864,  
  "minimumVerticalRadius": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "minimumVerticalRadiusCrest": 864,  
  "minimumVerticalRadiusHollow": 864,  
  "sidingId": "American whole magazine",  
  "verificationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "tenClassification": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Rivestimento NGSI-LD normalizzato Esempio  
Ecco un esempio di un binario di raccordo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:LIKW:54042696",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1996-09-19T23:08:47Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1994-06-22T11:37:34Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Structure decision camera reach purpose role prepare. Fish nor team avoid party memory most unit."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Great discover down event record milita"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Necessary billion gas Congress need explain safe. Law media people a sister consider."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Hotel country risk. Method bit seat organization partner."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Board movement understand. Each I give soon."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Siding:items:RYOP:03718728",  
      "urn:ngsi-ld:Siding:items:OGDX:73134134"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Siding:items:SIJP:84831513"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.4755575,  
        91.269469  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "According laugh government goal teacher social. Only speak effect policy easy learn. Material suddenly appear animal keep.",  
      "addressLocality": "",  
      "addressRegion": "Energy better life herself listen minute attorney. Bank you produce magazine.",  
      "addressCountry": "American sure message",  
      "postalCode": "Everything stand agreement hope forward. End debate deep act.",  
      "postOfficeBoxNumber": "Those public may range public. Hous",  
      "streetNr": "Discussion clear action add key reflect. Skill beautiful leg worker least ",  
      "district": "Discussion early quality that morning eye full. My at"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Report democratic en"  
  },  
  "type": "Siding",  
  "demonstrationINF": {  
    "type": "Property",  
    "value": "Pm can assume agency Mr reach music computer"  
  },  
  "gradient": {  
    "type": "Property",  
    "value": 733.9  
  },  
  "hasElectricShoreSupply": {  
    "type": "Property",  
    "value": true  
  },  
  "hasExternalCleaning": {  
    "type": "Property",  
    "value": true  
  },  
  "hasRefuelling": {  
    "type": "Property",  
    "value": true  
  },  
  "hasSandRestocking": {  
    "type": "Property",  
    "value": true  
  },  
  "hasToiletDischarge": {  
    "type": "Property",  
    "value": false  
  },  
  "hasWaterRestocking": {  
    "type": "Property",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Property",  
    "value": 818.3  
  },  
  "minimumHorizontalRadius": {  
    "type": "Property",  
    "value": 975  
  },  
  "minimumVerticalRadius": {  
    "type": "Property",  
    "value": "Police almost show day. Number only form skin t"  
  },  
  "minimumVerticalRadiusCrest": {  
    "type": "Property",  
    "value": 799  
  },  
  "minimumVerticalRadiusHollow": {  
    "type": "Property",  
    "value": 937  
  },  
  "sidingId": {  
    "type": "Property",  
    "value": "Air owner child site team modern behavior figure. Behavior near pick which civil door."  
  },  
  "verificationINF": {  
    "type": "Property",  
    "value": "Establish wh"  
  },  
  "tenClassification": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Siding:tenClassification:IURD:46677461"  
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

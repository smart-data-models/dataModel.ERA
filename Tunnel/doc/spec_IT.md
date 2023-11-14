<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Tunnel  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/Tunnel/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Una galleria ferroviaria è uno scavo o una costruzione intorno al binario per consentire alla ferrovia di passare, ad esempio, su un terreno più alto, su edifici o sull'acqua.  
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `complianceInfTsi[boolean]`: Conformità della galleria alla STI INF  - `crossSectionArea[number]`: Area della sezione trasversale  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `demonstrationSRT[string]`: Dichiarazione EI di dimostrazione per il tunnel (SRT)  - `description[string]`: Descrizione dell'articolo  - `dieselThermalAllowed[boolean]`: Ammessa la trazione diesel o altra trazione termica  - `endLocation[['geosparql#Geometry', 'wgs84_pos#Point']]`: Fine del tunnel  - `hasEmergencyPlan[boolean]`: Esistenza di un piano di emergenza  - `hasEvacuationAndRescuePoints[boolean]`: Esistenza di punti di evacuazione e soccorso  - `hasWalkway[boolean]`: Esistenza di passaggi pedonali  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `nationalRollingStockFireCategory[string]`: Categoria antincendio nazionale del materiale rotabile richiesto  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `rollingStockFireCategory[uri]`: Categoria di fuoco del materiale rotabile richiesto  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `specialTunnelArea[uri]`: Area speciale del tunnel  - `startLocation[['geosparql#Geometry', 'wgs84_pos#Point']]`: Inizio del tunnel  - `tunnelDocRef[string]`: Riferimento a un documento disponibile presso il GI con una descrizione precisa della galleria.  - `tunnelIdentification[string]`: Identificazione del tunnel  - `tunnelKilometerEnd[number]`: Fine del chilometro della galleria  - `tunnelKilometerStart[number]`: Inizio del chilometro in galleria  - `type[string]`: Tipo di dati NGSI. Deve essere Tunnel  - `verificationSRT[string]`: Dichiarazione di verifica CE per il tunnel (SRT)  <!-- /30-PropertiesList -->  
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
Tunnel:    
  description: 'A railway tunnel is an excavation or a construction around the track provided to allow the railway to pass for example higher land, buildings or water.'    
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
    complianceInfTsi:    
      description: Compliance of the tunnel with INF TSI    
      type: boolean    
      x-ngsi:    
        type: Property    
    crossSectionArea:    
      description: Cross section area    
      type: number    
      x-ngsi:    
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
    demonstrationSRT:    
      description: EI declaration of demonstration for tunnel (SRT)    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dieselThermalAllowed:    
      description: Diesel or other thermal traction allowed    
      type: boolean    
      x-ngsi:    
        type: Property    
    endLocation:    
      description: End of tunnel    
      type:    
        - "geosparql#Geometry"    
        - "wgs84_pos#Point"    
      x-ngsi:    
        type: Relationship    
    hasEmergencyPlan:    
      description: Existence of emergency plan    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasEvacuationAndRescuePoints:    
      description: Existence of evacuation and rescue points    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasWalkway:    
      description: Existence of walkways    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nationalRollingStockFireCategory:    
      description: National fire category of rolling stock required    
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
    rollingStockFireCategory:    
      description: Fire category of rolling stock required    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    specialTunnelArea:    
      description: Special tunnel area    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    startLocation:    
      description: Start of tunnel    
      type:    
        - "geosparql#Geometry"    
        - "wgs84_pos#Point"    
      x-ngsi:    
        type: Relationship    
    tunnelDocRef:    
      description: Reference to a document available from the IM with precise description of the tunnel    
      type: string    
      x-ngsi:    
        type: Property    
    tunnelIdentification:    
      description: Tunnel identification    
      type: string    
      x-ngsi:    
        type: Property    
    tunnelKilometerEnd:    
      description: Tunnel kilometer end    
      type: number    
      x-ngsi:    
        type: Property    
    tunnelKilometerStart:    
      description: Tunnel kilometer start    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI data type. It has to be Tunnel    
      enum:    
        - Tunnel    
      type: string    
      x-ngsi:    
        type: Property    
    verificationSRT:    
      description: EC declaration of verification for tunnel (SRT)    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Tunnel    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Tunnel/LICENSE.md    
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
#### Tunnel NGSI-v2 valori chiave Esempio  
Ecco un esempio di Tunnel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Tunnel:id:LHUX:38737711",  
  "dateCreated": "1993-07-30T17:21:52Z",  
  "dateModified": "1993-08-21T03:30:26Z",  
  "source": "Arrive goal matter bank next.",  
  "name": "Open happen water without bring type.",  
  "alternateName": "Not strategy respond sign hospital pull under budget. Type Democrat product. Guess some campaign people according.",  
  "description": "Vote site huge everybody save stuff fall. Stock natural probably true project else mouth skill. Reveal buil",  
  "dataProvider": "Moment where many forward wrong western season. Blood clearly daughter computer prove military.",  
  "owner": [  
    "urn:ngsi-ld:Tunnel:items:FLGJ:73287977",  
    "urn:ngsi-ld:Tunnel:items:KDIS:91192246"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Tunnel:items:VMTM:63360939"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      31.3980825,  
      74.021124  
    ]  
  },  
  "address": {  
    "streetAddress": "Foot stock case full according. Interesting record boy yeah.",  
    "addressLocality": "Then itself if owner across stage. Star hard blood fish thing rad",  
    "addressRegion": "Green customer when such heart make year cell. Toward military fight task. Without true drive still recently culture culture.",  
    "addressCountry": "Wait family smile remain. Report home media kind item assume.",  
    "postalCode": "Nature news stop total. Student measure hair century.",  
    "postOfficeBoxNumber": "Door message care security sound artist leave. Successful kid believe yoursel",  
    "streetNr": "According wor",  
    "district": "Eye reality attorney surface argue though ever. Herself usually in police according order degree. Production write back wear green forward."  
  },  
  "areaServed": "Range these design. Tv take understand first campaign natural century.",  
  "type": "Tunnel",  
  "complianceInfTsi": false,  
  "crossSectionArea": 864,  
  "demonstrationSRT": "American whole magazine truth ",  
  "dieselThermalAllowed": true,  
  "hasEmergencyPlan": true,  
  "hasEvacuationAndRescuePoints": false,  
  "hasWalkway": false,  
  "nationalRollingStockFireCategory": "Government first policy daughter. Local tend employee source nature add rest. Report size personal partner stock four.",  
  "tunnelDocRef": "Course nothing draw whose. Language ball f",  
  "tunnelIdentification": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type successful together. Raise study modern mi",  
  "tunnelKilometerEnd": 954.8,  
  "tunnelKilometerStart": 16.2,  
  "verificationSRT": "Change remain fly reach detail rule church.",  
  "endLocation": "urn:ngsi-ld:Tunnel:endLocation:ZSDZ:47247488",  
  "rollingStockFireCategory": "urn:ngsi-ld:Tunnel:rollingStockFireCategory:HWDR:37365505",  
  "specialTunnelArea": "urn:ngsi-ld:Tunnel:specialTunnelArea:MEMD:08918829",  
  "startLocation": "urn:ngsi-ld:Tunnel:startLocation:ZKRP:09411129",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Tunnel NGSI-v2 normalizzato Esempio  
Ecco un esempio di Tunnel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Tunnel:id:LHUX:38737711",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1993-07-30T17:21:52Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1993-08-21T03:30:26Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Arrive goal matter bank next."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Open happen water without bring type."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Not strategy respond sign hospital pull under budget. Type Democrat product. Guess some campaign people according."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Vote site huge everybody save stuff fall. Stock natural probably true project else mouth skill. Reveal buil"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Moment where many forward wrong western season. Blood clearly daughter computer prove military."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Tunnel:items:FLGJ:73287977",  
      "urn:ngsi-ld:Tunnel:items:KDIS:91192246"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Tunnel:items:VMTM:63360939"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          31.3980825,  
          74.021124  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Foot stock case full according. Interesting record boy yeah."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Then itself if owner across stage. Star hard blood fish thing rad"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Green customer when such heart make year cell. Toward military fight task. Without true drive still recently culture culture."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Wait family smile remain. Report home media kind item assume."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Nature news stop total. Student measure hair century."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Door message care security sound artist leave. Successful kid believe yoursel"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "According wor"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Eye reality attorney surface argue though ever. Herself usually in police according order degree. Production write back wear green forward."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Range these design. Tv take understand first campaign natural century."  
  },  
  "type": "Tunnel",  
  "complianceInfTsi": {  
    "type": "Boolean",  
    "value": false  
  },  
  "crossSectionArea": {  
    "type": "Number",  
    "value": 864  
  },  
  "demonstrationSRT": {  
    "type": "Text",  
    "value": "American whole magazine truth "  
  },  
  "dieselThermalAllowed": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasEmergencyPlan": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasEvacuationAndRescuePoints": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasWalkway": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nationalRollingStockFireCategory": {  
    "type": "Text",  
    "value": "Government first policy daughter. Local tend employee source nature add rest. Report size personal partner stock four."  
  },  
  "tunnelDocRef": {  
    "type": "Text",  
    "value": "Course nothing draw whose. Language ball f"  
  },  
  "tunnelIdentification": {  
    "type": "Text",  
    "value": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type successful together. Raise study modern mi"  
  },  
  "tunnelKilometerEnd": {  
    "type": "Number",  
    "value": 954.8  
  },  
  "tunnelKilometerStart": {  
    "type": "Number",  
    "value": 16.2  
  },  
  "verificationSRT": {  
    "type": "Text",  
    "value": "Change remain fly reach detail rule church."  
  },  
  "endLocation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Tunnel:endLocation:ZSDZ:47247488"  
  },  
  "rollingStockFireCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Tunnel:rollingStockFireCategory:HWDR:37365505"  
  },  
  "specialTunnelArea": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Tunnel:specialTunnelArea:MEMD:08918829"  
  },  
  "startLocation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Tunnel:startLocation:ZKRP:09411129"  
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
#### Tunnel NGSI-LD valori chiave Esempio  
Ecco un esempio di Tunnel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Tunnel:id:LHUX:38737711",  
  "dateCreated": "1993-07-30T17:21:52Z",  
  "dateModified": "1993-08-21T03:30:26Z",  
  "source": "Arrive goal matter bank next.",  
  "name": "Open happen water without bring type.",  
  "alternateName": "Not strategy respond sign hospital pull under budget. Type Democrat product. Guess some campaign people according.",  
  "description": "Vote site huge everybody save stuff fall. Stock natural probably true project else mouth skill. Reveal buil",  
  "dataProvider": "Moment where many forward wrong western season. Blood clearly daughter computer prove military.",  
  "owner": [  
    "urn:ngsi-ld:Tunnel:items:FLGJ:73287977",  
    "urn:ngsi-ld:Tunnel:items:KDIS:91192246"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Tunnel:items:VMTM:63360939"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      31.3980825,  
      74.021124  
    ]  
  },  
  "address": {  
    "streetAddress": "Foot stock case full according. Interesting record boy yeah.",  
    "addressLocality": "Then itself if owner across stage. Star hard blood fish thing rad",  
    "addressRegion": "Green customer when such heart make year cell. Toward military fight task. Without true drive still recently culture culture.",  
    "addressCountry": "Wait family smile remain. Report home media kind item assume.",  
    "postalCode": "Nature news stop total. Student measure hair century.",  
    "postOfficeBoxNumber": "Door message care security sound artist leave. Successful kid believe yoursel",  
    "streetNr": "According wor",  
    "district": "Eye reality attorney surface argue though ever. Herself usually in police according order degree. Production write back wear green forward."  
  },  
  "areaServed": "Range these design. Tv take understand first campaign natural century.",  
  "type": "Tunnel",  
  "complianceInfTsi": false,  
  "crossSectionArea": 864,  
  "demonstrationSRT": "American whole magazine truth ",  
  "dieselThermalAllowed": true,  
  "hasEmergencyPlan": true,  
  "hasEvacuationAndRescuePoints": false,  
  "hasWalkway": false,  
  "nationalRollingStockFireCategory": "Government first policy daughter. Local tend employee source nature add rest. Report size personal partner stock four.",  
  "tunnelDocRef": "Course nothing draw whose. Language ball f",  
  "tunnelIdentification": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type successful together. Raise study modern mi",  
  "tunnelKilometerEnd": 954.8,  
  "tunnelKilometerStart": 16.2,  
  "verificationSRT": "Change remain fly reach detail rule church.",  
  "endLocation": "urn:ngsi-ld:Tunnel:endLocation:ZSDZ:47247488",  
  "rollingStockFireCategory": "urn:ngsi-ld:Tunnel:rollingStockFireCategory:HWDR:37365505",  
  "specialTunnelArea": "urn:ngsi-ld:Tunnel:specialTunnelArea:MEMD:08918829",  
  "startLocation": "urn:ngsi-ld:Tunnel:startLocation:ZKRP:09411129",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Tunnel NGSI-LD normalizzato Esempio  
Ecco un esempio di Tunnel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Tunnel:id:YMRP:29425393",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1970-10-12T15:22:01Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2000-08-21T06:04:12Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Prevent before forget ask successful. Identify strategy character answer."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Modern us visit money. Experience yourself life home section may bar discover. How without suggest"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Outside gas admit age. War remember effort lose throughout single possible. Image perhaps floor style me."  
  },  
  "description": {  
    "type": "Property",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Across employee usually avoid police my. Third today run discuss night major now itself. American bring here sea money s"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Tunnel:items:EHZA:05225209",  
      "urn:ngsi-ld:Tunnel:items:CCXR:67610141"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Tunnel:items:ICRE:18932978"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -46.185967,  
        147.441006  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Six throw concern day order knowledge. And director then begin federal old above.",  
      "addressLocality": "Once human computer same leader. Federal prepare adult partner light amount. Direction my bag",  
      "addressRegion": "Prevent author allow candidate. Run beautiful rise suddenly current resource. Talk decade her both professor manage interview.",  
      "addressCountry": "Executive seek source southern item. Easy cause together foreign.",  
      "postalCode": "Energy notice hundred then. Certain human parent none suggest like which.",  
      "postOfficeBoxNumber": "Outside miss region. Letter standard coach call leave dark leg. Official fire generation table everyone.",  
      "streetNr": "Nature tough walk number. Fund address name.",  
      "district": "Production life me position type. While miss check purpose major oil including."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Mission news student your. Late enjoy figure physical."  
  },  
  "type": "Tunnel",  
  "complianceInfTsi": {  
    "type": "Property",  
    "value": true  
  },  
  "crossSectionArea": {  
    "type": "Property",  
    "value": 753  
  },  
  "demonstrationSRT": {  
    "type": "Property",  
    "value": "Computer fire say hotel though ef"  
  },  
  "dieselThermalAllowed": {  
    "type": "Property",  
    "value": true  
  },  
  "hasEmergencyPlan": {  
    "type": "Property",  
    "value": true  
  },  
  "hasEvacuationAndRescuePoints": {  
    "type": "Property",  
    "value": true  
  },  
  "hasWalkway": {  
    "type": "Property",  
    "value": true  
  },  
  "nationalRollingStockFireCategory": {  
    "type": "Property",  
    "value": "Safe cost just force business career save. Will act raise according method customer share."  
  },  
  "tunnelDocRef": {  
    "type": "Property",  
    "value": "Floor campaign later bar performance. Pay scientist senior girl. T"  
  },  
  "tunnelIdentification": {  
    "type": "Property",  
    "value": "Kid who detail look bad. Certainly environmental politics. Local serious take along occur."  
  },  
  "tunnelKilometerEnd": {  
    "type": "Property",  
    "value": 986.2  
  },  
  "tunnelKilometerStart": {  
    "type": "Property",  
    "value": 714.8  
  },  
  "verificationSRT": {  
    "type": "Property",  
    "value": "Final light treat against enter especially. Energy compare week performance table. Conference front team late once wind."  
  },  
  "endLocation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Tunnel:endLocation:WRDQ:94614100"  
  },  
  "rollingStockFireCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Tunnel:rollingStockFireCategory:IAAZ:08611397"  
  },  
  "specialTunnelArea": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Tunnel:specialTunnelArea:VINZ:05152325"  
  },  
  "startLocation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Tunnel:startLocation:UCYY:96379223"  
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

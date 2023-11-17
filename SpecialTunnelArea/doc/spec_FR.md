<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : SpecialTunnelArea    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/SpecialTunnelArea/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Aire ou emplacement à l'intérieur d'un tunnel où il y a une passerelle, des points d'évacuation et de sauvetage**.    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique      
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de SpecialTunnelArea  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
modèle de données mappé à partir de l'ontologie de l'ERA https://data-interop.era.europa.eu/era-vocabulary (Agence de l'Union européenne pour les chemins de fer)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
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
## Exemples de charges utiles    
#### SpecialTunnelArea Valeurs clés NGSI-v2 Exemple    
Voici un exemple de SpecialTunnelArea au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### SpecialTunnelArea NGSI-v2 normalisé Exemple    
Voici un exemple de SpecialTunnelArea au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
      "coordinates": [  
        -4.1411545,  
        -167.120745  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Build next e",  
      "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
      "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
      "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
      "postalCode": "Environmental bag officer do ball. Soc",  
      "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
      "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
      "district": "Pattern over scientist important"  
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
#### SpecialTunnelArea Valeurs clés NGSI-LD Exemple    
Voici un exemple de SpecialTunnelArea au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### SpecialTunnelArea NGSI-LD normalisé Exemple    
Voici un exemple de SpecialTunnelArea au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

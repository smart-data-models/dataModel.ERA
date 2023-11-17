<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Distance et vitesse des pantographes élevés    
====================================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/RaisedPantographsDistanceAndSpeed/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Indication du nombre maximal de pantographes surélevés par train autorisé et de l'espacement minimal d'axe en axe des têtes de pantographes adjacentes, exprimés en mètres, à la vitesse donnée.    
Chaque voie peut avoir plusieurs valeurs (structurées) de pantographes surélevés par train autorisé, et chacune a des valeurs pour le nombre de pantographes, la distance minimale entre les pantographes, en mètres, et la vitesse considérée en km/h**.    
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `raisedPantographsDistance[number]`: Distance des pantographes surélevés  - `raisedPantographsNumber[number]`: Nombre de pantographes.  - `raisedPantographsSpeed[number]`: Vitesse des pantographes surélevés  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de RaisedPantographsDistanceAndSpeed (distance et vitesse des pantographes).  <!-- /30-PropertiesList -->    
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
RaisedPantographsDistanceAndSpeed:      
  description: |-      
    Indication of maximum number of raised pantographs per train allowed and minimum spacing centre line to centre line of adjacent pantograph heads, expressed in metres, at the given speed.      
    Each track can have several raised pantographs per train allowed (structured) values, and each one has values for number of pantographs, minimum distance between pantographs, in metres, and speed considered in km/h.      
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
    raisedPantographsDistance:      
      description: Raised pantographs distance      
      type: number      
      x-ngsi:      
        type: Property      
    raisedPantographsNumber:      
      description: Number of pantographs.      
      type: number      
      x-ngsi:      
        type: Property      
    raisedPantographsSpeed:      
      description: Raised pantographs speed      
      type: number      
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
      description: NGSI data type. It has to be RaisedPantographsDistanceAndSpeed      
      enum:      
        - RaisedPantographsDistanceAndSpeed      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/RaisedPantographsDistanceAndSpeed      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/RaisedPantographsDistanceAndSpeed/LICENSE.md      
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
#### RaisedPantographsDistanceAndSpeed Valeurs-clés de l'INSIG-v2 Exemple    
Voici un exemple de RaisedPantographsDistanceAndSpeed au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": "2016-10-01T23:32:51Z",  
  "dateModified": "1994-01-08T16:04:55Z",  
  "source": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment.",  
  "name": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter.",  
  "alternateName": "Describe other scene standard citizen. Exist letter down ready TV phon",  
  "description": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning.",  
  "dataProvider": "Song minute like table knowledge state. Notice line never support stop.",  
  "owner": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      52.853707,  
      -40.868675  
    ]  
  },  
  "address": {  
    "streetAddress": "Special son three figure cost mili",  
    "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
    "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
    "addressCountry": "Consumer include little. Seem ",  
    "postalCode": "Out everything senior. Out staff",  
    "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
    "streetNr": "",  
    "district": "Worker expect realize above. I differenc"  
  },  
  "areaServed": "Table must who. Grow in ",  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": 864,  
  "raisedPantographsNumber": 864,  
  "raisedPantographsSpeed": 864,  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RaisedPantographsDistanceAndSpeed NGSI-v2 normalisé Exemple    
Voici un exemple de RaisedPantographsDistanceAndSpeed au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2016-10-01T23:32:51Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1994-01-08T16:04:55Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment."  
  },  
  "name": {  
    "type": "Text",  
    "value": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Describe other scene standard citizen. Exist letter down ready TV phon"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Song minute like table knowledge state. Notice line never support stop."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        52.853707,  
        -40.868675  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Special son three figure cost mili",  
      "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
      "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
      "addressCountry": "Consumer include little. Seem ",  
      "postalCode": "Out everything senior. Out staff",  
      "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
      "streetNr": "",  
      "district": "Worker expect realize above. I differenc"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Table must who. Grow in "  
  },  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": {  
    "type": "Number",  
    "value": 864  
  },  
  "raisedPantographsNumber": {  
    "type": "Number",  
    "value": 864  
  },  
  "raisedPantographsSpeed": {  
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
#### RaisedPantographsDistanceAndSpeed Valeurs-clés de l'INS-LD Exemple    
Voici un exemple de RaisedPantographsDistanceAndSpeed au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:XXHA:11264005",  
  "dateCreated": "2016-10-01T23:32:51Z",  
  "dateModified": "1994-01-08T16:04:55Z",  
  "source": "Design summer official cost wait travel white. Thus down magazine. Risk enjoy open view indicate daughter environment.",  
  "name": "His husband act type factor. Later pattern suggest leave. Safe rate result make still include moment. Economy like style Congress enter.",  
  "alternateName": "Describe other scene standard citizen. Exist letter down ready TV phon",  
  "description": "Meet none consider however west line read pretty. Something tell however imagine the discuss. Such whose fund morning.",  
  "dataProvider": "Song minute like table knowledge state. Notice line never support stop.",  
  "owner": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CPQC:54321719",  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:CNAZ:75020813"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:SWTZ:53232778"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      52.853707,  
      -40.868675  
    ]  
  },  
  "address": {  
    "streetAddress": "Special son three figure cost mili",  
    "addressLocality": "Myself character lot apply. Course remember market moment face boy purpose. ",  
    "addressRegion": "Air bar step cover at front. Interest result reality Mrs foot have mouth. Open thousand wo",  
    "addressCountry": "Consumer include little. Seem ",  
    "postalCode": "Out everything senior. Out staff",  
    "postOfficeBoxNumber": "Official foreign month shake bring service see. One everything military store instead assume memory. Build entire one man ground.",  
    "streetNr": "",  
    "district": "Worker expect realize above. I differenc"  
  },  
  "areaServed": "Table must who. Grow in ",  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": 864,  
  "raisedPantographsNumber": 864,  
  "raisedPantographsSpeed": 864,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RaisedPantographsDistanceAndSpeed NGSI-LD normalisé Exemple    
Voici un exemple de RaisedPantographsDistanceAndSpeed au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:id:NRAH:81561263",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1971-11-20T03:14:14Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1970-10-03T20:50:52Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "War game help give"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Watch within challenge safe. Raise available seem compare body early. None face safe term before environment drop"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Court I loo"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Them site whole should play generation question. Significant on teach of none."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Bag care religious possible source media team. Skill politics blue yes according."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:DKUU:20419467",  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:BFPP:72232537"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RaisedPantographsDistanceAndSpeed:items:XVYI:24654995"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        33.252656,  
        109.596554  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Break seem system real part become pay. Sense baby total care investment. Figure break likely behavior talk morning estab",  
      "addressLocality": "Quite himself drive trouble pay they guy. History role mome",  
      "addressRegion": "Cut seem painting race.",  
      "addressCountry": "Room whose forget soldier evidence air. Memory artist real western myse",  
      "postalCode": "Glass artist leg modern. Republican reflect hot skill democratic speak.",  
      "postOfficeBoxNumber": "Serious art magazine morning serious histor",  
      "streetNr": "Small w",  
      "district": "Remain environment performance campaign. Test traditional want call. Building forget argue suggest."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Forward gun require "  
  },  
  "type": "RaisedPantographsDistanceAndSpeed",  
  "raisedPantographsDistance": {  
    "type": "Property",  
    "value": 131  
  },  
  "raisedPantographsNumber": {  
    "type": "Property",  
    "value": 478  
  },  
  "raisedPantographsSpeed": {  
    "type": "Property",  
    "value": 219  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

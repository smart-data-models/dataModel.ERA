<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

Entité : SystemSeparationInfo    
=============================
<!-- /10-Header -->
    
<!-- 15-License -->
    

[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/SystemSeparationInfo/LICENSE.md)    

[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

Description globale : **Indication de plusieurs informations requises sur la séparation du système**.    

version : 0.0.1    
<!-- /20-Description -->
    
<!-- 30-PropertiesList -->
    

## Liste des propriétés    

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique      
- `alternateName[string]`: Un nom alternatif pour ce poste  
- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  
- `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  
- `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  
- `description[string]`: Une description de l'article  
- `id[*]`: Identifiant unique de l'entité  
- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  
- `name[string]`: Le nom de cet élément  
- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  
- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  
- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  
- `systemSeparationInfoChangeSupplySystem[string]`: Séparation des systèmes info changement de système d'approvisionnement  
- `systemSeparationInfoLength[number]`: Longueur de l'information sur la séparation du système  
- `systemSeparationInfoPantographLowered[boolean]`: Séparation du système info pantographe abaissé  
- `systemSeparationInfoSwitchOffBreaker[boolean]`: Séparation du système info coupure du disjoncteur  
- `type[string]`: Type de données NGSI. Il doit s'agir de SystemSeparationInfo  
<!-- /30-PropertiesList -->
    
<!-- 35-RequiredProperties -->
    

Propriétés requises    
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
    
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
SystemSeparationInfo:      
  description: Indication of required several information on system separation.      
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
    systemSeparationInfoChangeSupplySystem:      
      description: System separation info change supply system      
      type: string      
      x-ngsi:      
        type: Property      
    systemSeparationInfoLength:      
      description: System separation info length      
      type: number      
      x-ngsi:      
        type: Property      
    systemSeparationInfoPantographLowered:      
      description: System separation info  pantograph lowered      
      type: boolean      
      x-ngsi:      
        type: Property      
    systemSeparationInfoSwitchOffBreaker:      
      description: System separation info switch off breaker      
      type: boolean      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be SystemSeparationInfo      
      enum:      
        - SystemSeparationInfo      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/SystemSeparationInfo      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SystemSeparationInfo/LICENSE.md      
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

#### SystemSeparationInfo Valeurs clés de l'INSG-v2 Exemple    

Voici un exemple de SystemSeparationInfo au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": "1971-06-11T11:02:58Z",  
  "dateModified": "1981-04-17T22:16:45Z",  
  "source": "Quickly final probably box society with. View woman main analysis. Think region why best with.",  
  "name": "Treat inside expect figure. Animal ago television visit late.",  
  "alternateName": "Under feel opportunity next win",  
  "description": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro",  
  "dataProvider": "Drive read poor policy. Try quality report safe. Yard reason continue wide.",  
  "owner": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
    "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.1257535,  
      35.88905  
    ]  
  },  
  "address": {  
    "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
    "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
    "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
    "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
    "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
    "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
    "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
    "district": "Forget memory specific own fast p"  
  },  
  "areaServed": "Understand him visit certain task. Bar staff use but.",  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess.",  
  "systemSeparationInfoLength": 864,  
  "systemSeparationInfoPantographLowered": false,  
  "systemSeparationInfoSwitchOffBreaker": false
}  
```  
</details>    

#### SystemSeparationInfo NGSI-v2 normalisé Exemple    

Voici un exemple de SystemSeparationInfo au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1971-06-11T11:02:58Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1981-04-17T22:16:45Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Quickly final probably box society with. View woman main analysis. Think region why best with."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Treat inside expect figure. Animal ago television visit late."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Under feel opportunity next win"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Drive read poor policy. Try quality report safe. Yard reason continue wide."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
      "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        37.1257535,  
        35.88905  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
      "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
      "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
      "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
      "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
      "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
      "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
      "district": "Forget memory specific own fast p"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Understand him visit certain task. Bar staff use but."  
  },  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": {  
    "type": "Text",  
    "value": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess."  
  },  
  "systemSeparationInfoLength": {  
    "type": "Number",  
    "value": 864  
  },  
  "systemSeparationInfoPantographLowered": {  
    "type": "Boolean",  
    "value": false  
  },  
  "systemSeparationInfoSwitchOffBreaker": {  
    "type": "Boolean",  
    "value": false  
  }  
}  
```  
</details>    

#### SystemSeparationInfo Valeurs clés NGSI-LD Exemple    

Voici un exemple de SystemSeparationInfo au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": "1971-06-11T11:02:58Z",  
  "dateModified": "1981-04-17T22:16:45Z",  
  "source": "Quickly final probably box society with. View woman main analysis. Think region why best with.",  
  "name": "Treat inside expect figure. Animal ago television visit late.",  
  "alternateName": "Under feel opportunity next win",  
  "description": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro",  
  "dataProvider": "Drive read poor policy. Try quality report safe. Yard reason continue wide.",  
  "owner": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
    "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.1257535,  
      35.88905  
    ]  
  },  
  "address": {  
    "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
    "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
    "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
    "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
    "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
    "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
    "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
    "district": "Forget memory specific own fast p"  
  },  
  "areaServed": "Understand him visit certain task. Bar staff use but.",  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess.",  
  "systemSeparationInfoLength": 864,  
  "systemSeparationInfoPantographLowered": false,  
  "systemSeparationInfoSwitchOffBreaker": false,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### SystemSeparationInfo NGSI-LD normalisé Exemple    

Voici un exemple de SystemSeparationInfo au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:XYDV:99228074",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1990-08-14T02:23:40Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2005-06-05T23:14:26Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Stuff kind likely de"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Story pay cover hot which. Day difference floor make husband say. Through break ok daughter."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Scientist maintain feel baby inte"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Might new take. Month detail matter moment here current. Rock sign number. "  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Always speak able break billion requ"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:KLAD:01706991",  
      "urn:ngsi-ld:SystemSeparationInfo:items:OUMR:57506132"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:FZOT:63378927"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -75.5485445,  
        77.256275  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Environmental stage comme",  
      "addressLocality": "Go under experience nor. Defense skill make product.",  
      "addressRegion": "Scientist letter artis",  
      "addressCountry": "Close born subject among water. Hear computer quest",  
      "postalCode": "Until along talk long. Keep support prepare direction reveal national. Effect few institution inside avoid. In hundred gun result clearly.",  
      "postOfficeBoxNumber": "Do account nothing executive ground. Brother put all often recognize method. Surface red three front su",  
      "streetNr": "Beautiful hotel necessary college risk baby. Stop wish either everyone. E",  
      "district": "Impact treatment follow leader. "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Push film partner. Soon themselves guy expert however."  
  },  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": {  
    "type": "Property",  
    "value": "Age ten church not. Edge"  
  },  
  "systemSeparationInfoLength": {  
    "type": "Property",  
    "value": 735  
  },  
  "systemSeparationInfoPantographLowered": {  
    "type": "Property",  
    "value": false  
  },  
  "systemSeparationInfoSwitchOffBreaker": {  
    "type": "Property",  
    "value": true  
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
    

Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->
    
<!-- 97-LastFooter -->
    
---    

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
    

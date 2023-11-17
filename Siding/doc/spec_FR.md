<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Revêtement    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/Siding/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Les voies de garage sont toutes les voies où la circulation des trains en service se termine et qui ne sont pas utilisées pour l'acheminement opérationnel d'un train**.    
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `demonstrationINF[string]`: Déclaration de démonstration de l'IE pour les voies et les bardages [INF].  - `description[string]`: Une description de l'article  - `gradient[number]`: Pente des pistes de stabulation  - `hasElectricShoreSupply[boolean]`: Existence d'une alimentation électrique à quai  - `hasExternalCleaning[boolean]`: Existence d'installations de nettoyage externes  - `hasRefuelling[boolean]`: Existence d'un ravitaillement en carburant  - `hasSandRestocking[boolean]`: Existence d'un repeuplement en sable  - `hasToiletDischarge[boolean]`: Existence d'un écoulement des toilettes  - `hasWaterRestocking[boolean]`: Existence d'une réserve d'eau  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `maxCurrentStandstillPantograph[number]`: Courant maximal à l'arrêt par pantographe  - `minimumHorizontalRadius[number]`: Rayon minimal de la courbe horizontale  - `minimumVerticalRadius[string]`: Rayon minimal de la courbe verticale  - `minimumVerticalRadiusCrest[number]`: Rayon minimal de la crête de la courbe verticale  - `minimumVerticalRadiusHollow[number]`: Rayon minimal de la courbe verticale creuse  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `sidingId[string]`: Identification du revêtement  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `tenClassification[uri]`: Classification TEN (de la voie, du quai, de la voie d'évitement)  - `type[string]`: Type de données NGSI. Il doit s'agir de Siding  - `verificationINF[string]`: Déclaration de vérification de la CE pour la voie et la glissière [INF].  <!-- /30-PropertiesList -->    
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
## Exemples de charges utiles    
#### Bardage NGSI-v2 valeurs clés Exemple    
Voici un exemple de Siding au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### Bardage NGSI-v2 normalisé Exemple    
Voici un exemple d'une voie d'évitement au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
      "coordinates": [  
        -36.875369,  
        98.837859  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
      "addressLocality": "Since ",  
      "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
      "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
      "postalCode": "Personal build",  
      "postOfficeBoxNumber": "Leader enough weight everything.",  
      "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
      "district": "Area cost hundred same. Sense anyone anyone."  
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
#### Bardage Valeurs clés NGSI-LD Exemple    
Voici un exemple de Siding au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### Bardage NGSI-LD normalisé Exemple    
Voici un exemple d'une voie d'évitement au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

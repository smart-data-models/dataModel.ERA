<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Objet topologique    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/TopologicalObject/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Classe de haut niveau pour le réseau de voies décrit comme un modèle topologique de nœuds et d'arêtes**    
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de TopologicalObject  <!-- /30-PropertiesList -->    
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
TopologicalObject:      
  description: Top level class for the the track network described as a topological node edge model      
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
      description: NGSI data type. It has to be TopologicalObject      
      enum:      
        - TopologicalObject      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/TopologicalObject      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/TopologicalObject/LICENSE.md      
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
#### TopologicalObject Valeurs-clés de l'INSIG-v2 Exemple    
Voici un exemple d'un TopologicalObject au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TopologicalObject:id:MDTE:29122911",  
  "dateCreated": "1997-12-28T14:44:16Z",  
  "dateModified": "1986-06-03T02:06:03Z",  
  "source": "Race box market story. Father establish himself everyone",  
  "name": "Least chair pull serve specific expect modern. Debate end difficult wife. Player various popular southern believe amount lot method.",  
  "alternateName": "Address happy television wide bu",  
  "description": "Finish then evidence just. Book hundred kind model opportunity. Always pattern class oil soldier conference involve.",  
  "dataProvider": "Room affect someone need manager. Range represent compare reality beat.",  
  "owner": [  
    "urn:ngsi-ld:TopologicalObject:items:HQJL:52681721",  
    "urn:ngsi-ld:TopologicalObject:items:RKZS:06098455"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TopologicalObject:items:DCVU:82796661"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -6.809152,  
      70.994051  
    ]  
  },  
  "address": {  
    "streetAddress": "Them generation story painting economy hair their. Keep together among she.",  
    "addressLocality": "Charge win great only.",  
    "addressRegion": "Popular thank would represent course. Just image represent decision parent. Degree west lay gar",  
    "addressCountry": "Health history lose defense. About husband market student short cost green. Morning poor example alre",  
    "postalCode": "Ready course edge author. Century once lead approach after.",  
    "postOfficeBoxNumber": "Dream now federal nice. Fish give entire home detail against.",  
    "streetNr": "Turn become hotel game ",  
    "district": "Cover whole pay customer management approach theory."  
  },  
  "areaServed": "Partner a improve about. Because four challenge. Hot north personal benefit.",  
  "type": "TopologicalObject",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### TopologicalObject NGSI-v2 normalisé Exemple    
Voici un exemple d'un TopologicalObject au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TopologicalObject:id:MDTE:29122911",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1997-12-28T14:44:16Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1986-06-03T02:06:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Race box market story. Father establish himself everyone"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Least chair pull serve specific expect modern. Debate end difficult wife. Player various popular southern believe amount lot method."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Address happy television wide bu"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Finish then evidence just. Book hundred kind model opportunity. Always pattern class oil soldier conference involve."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Room affect someone need manager. Range represent compare reality beat."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:HQJL:52681721",  
      "urn:ngsi-ld:TopologicalObject:items:RKZS:06098455"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:DCVU:82796661"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.809152,  
        70.994051  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Them generation story painting economy hair their. Keep together among she.",  
      "addressLocality": "Charge win great only.",  
      "addressRegion": "Popular thank would represent course. Just image represent decision parent. Degree west lay gar",  
      "addressCountry": "Health history lose defense. About husband market student short cost green. Morning poor example alre",  
      "postalCode": "Ready course edge author. Century once lead approach after.",  
      "postOfficeBoxNumber": "Dream now federal nice. Fish give entire home detail against.",  
      "streetNr": "Turn become hotel game ",  
      "district": "Cover whole pay customer management approach theory."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Partner a improve about. Because four challenge. Hot north personal benefit."  
  },  
  "type": "TopologicalObject",  
  "context": {  
    "type": "StructuredValue",  
    "value": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
    ]  
  }  
}  
```  
</details>    
#### TopologicalObject Valeurs clés NGSI-LD Exemple    
Voici un exemple d'objet topologique au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TopologicalObject:id:MDTE:29122911",  
  "dateCreated": "1997-12-28T14:44:16Z",  
  "dateModified": "1986-06-03T02:06:03Z",  
  "source": "Race box market story. Father establish himself everyone",  
  "name": "Least chair pull serve specific expect modern. Debate end difficult wife. Player various popular southern believe amount lot method.",  
  "alternateName": "Address happy television wide bu",  
  "description": "Finish then evidence just. Book hundred kind model opportunity. Always pattern class oil soldier conference involve.",  
  "dataProvider": "Room affect someone need manager. Range represent compare reality beat.",  
  "owner": [  
    "urn:ngsi-ld:TopologicalObject:items:HQJL:52681721",  
    "urn:ngsi-ld:TopologicalObject:items:RKZS:06098455"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TopologicalObject:items:DCVU:82796661"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -6.809152,  
      70.994051  
    ]  
  },  
  "address": {  
    "streetAddress": "Them generation story painting economy hair their. Keep together among she.",  
    "addressLocality": "Charge win great only.",  
    "addressRegion": "Popular thank would represent course. Just image represent decision parent. Degree west lay gar",  
    "addressCountry": "Health history lose defense. About husband market student short cost green. Morning poor example alre",  
    "postalCode": "Ready course edge author. Century once lead approach after.",  
    "postOfficeBoxNumber": "Dream now federal nice. Fish give entire home detail against.",  
    "streetNr": "Turn become hotel game ",  
    "district": "Cover whole pay customer management approach theory."  
  },  
  "areaServed": "Partner a improve about. Because four challenge. Hot north personal benefit.",  
  "type": "TopologicalObject",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### TopologicalObject NGSI-LD normalisé Exemple    
Voici un exemple d'un TopologicalObject au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TopologicalObject:id:ANPE:97919193",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-09-17T09:21:53Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1996-07-18T12:43:19Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Yes serve free seat. Room including each yard walk attack."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Actually large man expect eye voic"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Season area fill station news stop. Choice marriage"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Guy remain them seven general. Worker term address. Education detail not share human win item."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Current treatment sing. Hour bed song all tend success fine. Develop guy if them interest high bed. Strong certain say offer i"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:HBZC:96164619",  
      "urn:ngsi-ld:TopologicalObject:items:SZBJ:87847721"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:TopologicalObject:items:VWRI:32992685"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        0.125705,  
        0.810063  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Building out then when gas address face. Increase tele",  
      "addressLocality": "Also house growth leave now food information. Management across tree factor Republican.",  
      "addressRegion": "F",  
      "addressCountry": "Score him say majority drug catch figure however. Eat condition subject least. Purpose guess such quickly management wear ",  
      "postalCode": "Southe",  
      "postOfficeBoxNumber": "Fear surface but effect. Sing structure growth with personal western.",  
      "streetNr": "Window down clear window describe hand determine. Talk bill thousand lay recognize. Customer trip place really poor after ene",  
      "district": "Family opportunity leg industry theory smile image. Into "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Hear her year population be."  
  },  
  "type": "TopologicalObject",  
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

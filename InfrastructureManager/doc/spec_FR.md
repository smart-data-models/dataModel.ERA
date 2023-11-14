<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Gestionnaire d'infrastructure  
======================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/InfrastructureManager/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Le gestionnaire d'infrastructure possède et exploite le réseau ferroviaire et les infrastructures connexes**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `definesSubset[uri]`: Définit le sous-ensemble  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `imCode[string]`: Code de l'IM  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de InfrastructureManager  <!-- /30-PropertiesList -->  
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
InfrastructureManager:    
  description: The infrastructure manager owns and operates the railway network and related infrastructure.    
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
    definesSubset:    
      description: Defines subset    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    imCode:    
      description: IM's code    
      type: string    
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
      description: NGSI data type. It has to be InfrastructureManager    
      enum:    
        - InfrastructureManager    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/InfrastructureManager    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/InfrastructureManager/LICENSE.md    
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
#### InfrastructureManager NGSI-v2 key-values Exemple  
Voici un exemple d'InfrastructureManager au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:VIMY:89391422",  
  "dateCreated": "2006-09-18T16:56:18Z",  
  "dateModified": "1978-06-20T09:22:50Z",  
  "source": "Sort southern music artist. Fear manage seat population environment.",  
  "name": "Plan challenge vote do again. Enjoy short particularly.",  
  "alternateName": "Rate option level back stuff kind. Teach televi",  
  "description": "In discussion fall economic force shake. This speak fine piece work bil",  
  "dataProvider": "Administration raise door a your. Oil summ",  
  "owner": [  
    "urn:ngsi-ld:InfrastructureManager:items:JMAY:69019141",  
    "urn:ngsi-ld:InfrastructureManager:items:HDMP:30084694"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:InfrastructureManager:items:HEJR:49829825"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.3334725,  
      -142.001584  
    ]  
  },  
  "address": {  
    "streetAddress": "Moment someone learn short affect. Could those herself mention without use.",  
    "addressLocality": "Able born appear fact. Too nature record second letter. Hit pattern because unit easy address befo",  
    "addressRegion": "Physical same read success fight.",  
    "addressCountry": "Girl want over allow ask begin three. Say month call how employee treat environmental energy. Reflect through society experienc",  
    "postalCode": "Here simply my force child kid. Why behavior last here. Back PM carry actually interview rise.",  
    "postOfficeBoxNumber": "Partner magazine cause before. Decide method experience exactly. Operation final feeling staff ten.",  
    "streetNr": "Tell or ok else another allow standard.",  
    "district": "Hot player second fall. Participant state draw agent suggest visit however we. Line we blue. Sit record TV can."  
  },  
  "areaServed": "White task performance blood. Hard eye road probably interview to.",  
  "type": "InfrastructureManager",  
  "imCode": "Responsibility information do paper either",  
  "definesSubset": "urn:ngsi-ld:InfrastructureManager:definesSubset:QKJR:78702924",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### InfrastructureManager NGSI-v2 normalisé Exemple  
Voici un exemple de gestionnaire d'infrastructure au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:VIMY:89391422",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2006-09-18T16:56:18Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1978-06-20T09:22:50Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Sort southern music artist. Fear manage seat population environment."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Plan challenge vote do again. Enjoy short particularly."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Rate option level back stuff kind. Teach televi"  
  },  
  "description": {  
    "type": "Text",  
    "value": "In discussion fall economic force shake. This speak fine piece work bil"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Administration raise door a your. Oil summ"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:JMAY:69019141",  
      "urn:ngsi-ld:InfrastructureManager:items:HDMP:30084694"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:HEJR:49829825"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -36.3334725,  
          -142.001584  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Moment someone learn short affect. Could those herself mention without use."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Able born appear fact. Too nature record second letter. Hit pattern because unit easy address befo"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Physical same read success fight."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Girl want over allow ask begin three. Say month call how employee treat environmental energy. Reflect through society experienc"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Here simply my force child kid. Why behavior last here. Back PM carry actually interview rise."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Partner magazine cause before. Decide method experience exactly. Operation final feeling staff ten."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Tell or ok else another allow standard."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Hot player second fall. Participant state draw agent suggest visit however we. Line we blue. Sit record TV can."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "White task performance blood. Hard eye road probably interview to."  
  },  
  "type": "InfrastructureManager",  
  "imCode": {  
    "type": "Text",  
    "value": "Responsibility information do paper either"  
  },  
  "definesSubset": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:InfrastructureManager:definesSubset:QKJR:78702924"  
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
#### InfrastructureManager Valeurs clés NGSI-LD Exemple  
Voici un exemple d'InfrastructureManager au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:VIMY:89391422",  
  "dateCreated": "2006-09-18T16:56:18Z",  
  "dateModified": "1978-06-20T09:22:50Z",  
  "source": "Sort southern music artist. Fear manage seat population environment.",  
  "name": "Plan challenge vote do again. Enjoy short particularly.",  
  "alternateName": "Rate option level back stuff kind. Teach televi",  
  "description": "In discussion fall economic force shake. This speak fine piece work bil",  
  "dataProvider": "Administration raise door a your. Oil summ",  
  "owner": [  
    "urn:ngsi-ld:InfrastructureManager:items:JMAY:69019141",  
    "urn:ngsi-ld:InfrastructureManager:items:HDMP:30084694"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:InfrastructureManager:items:HEJR:49829825"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.3334725,  
      -142.001584  
    ]  
  },  
  "address": {  
    "streetAddress": "Moment someone learn short affect. Could those herself mention without use.",  
    "addressLocality": "Able born appear fact. Too nature record second letter. Hit pattern because unit easy address befo",  
    "addressRegion": "Physical same read success fight.",  
    "addressCountry": "Girl want over allow ask begin three. Say month call how employee treat environmental energy. Reflect through society experienc",  
    "postalCode": "Here simply my force child kid. Why behavior last here. Back PM carry actually interview rise.",  
    "postOfficeBoxNumber": "Partner magazine cause before. Decide method experience exactly. Operation final feeling staff ten.",  
    "streetNr": "Tell or ok else another allow standard.",  
    "district": "Hot player second fall. Participant state draw agent suggest visit however we. Line we blue. Sit record TV can."  
  },  
  "areaServed": "White task performance blood. Hard eye road probably interview to.",  
  "type": "InfrastructureManager",  
  "imCode": "Responsibility information do paper either",  
  "definesSubset": "urn:ngsi-ld:InfrastructureManager:definesSubset:QKJR:78702924",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### InfrastructureManager NGSI-LD normalisé Exemple  
Voici un exemple de gestionnaire d'infrastructure au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InfrastructureManager:id:MXSJ:48211430",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2001-02-17T13:59:21Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1978-12-17T01:37:15Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Drop wear participant probably pull another claim. Soldier among magazine name cause."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Push low morning himself boy. Response push daughter certain blood hour career."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Inter"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Sing condition often fund gun report. Skin yes me"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Shoulder west friend find stage main state. Those way machine consumer current friend within. Artist past participant agree more."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:SHEM:41311877",  
      "urn:ngsi-ld:InfrastructureManager:items:UIQW:30839567"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:InfrastructureManager:items:PJAF:62503952"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        3.5779895,  
        -137.677126  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Behind play land top reflect material drug. Charge worry newspaper important. Budget position meeting throughout fight daughter.",  
      "addressLocality": "Road husb",  
      "addressRegion": "Official arm decision can often general second. Short establish maintain television pattern.",  
      "addressCountry": "Center system out forward I pressure short. News moment decision spend.",  
      "postalCode": "Serve recent here determine until. Good sure down talk since establish. Challenge describe structure necessary. Rate difference item",  
      "postOfficeBoxNumber": "Camera instead glass stop remember good. War heavy help.",  
      "streetNr": "Total ",  
      "district": "Half consumer condition and night exist human. P"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Attack total help who reduce lay. Daughter step center short property per whether"  
  },  
  "type": "InfrastructureManager",  
  "imCode": {  
    "type": "Property",  
    "value": "Away live too certainly. Ground why include include."  
  },  
  "definesSubset": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:InfrastructureManager:definesSubset:OSEY:46076384"  
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

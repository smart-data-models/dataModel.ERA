<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Vitesse maximale et insuffisance de capacité  
=====================================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/MaximumSpeedAndCantDeficiency/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Combinaison de la vitesse maximale et de l'insuffisance de dévers maximale pour laquelle le véhicule a été évalué**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de MaximumSpeedAndCantDeficiency (vitesse maximale et insuffisance).  - `vehicleTypeMaximumCantDeficiency[number]`: Type de véhicule Défaut de dévers maximal  - `vehicleTypeMaximumSpeed[number]`: Type de véhicule vitesse maximale  <!-- /30-PropertiesList -->  
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
MaximumSpeedAndCantDeficiency:    
  description: Combination of maximum speed and maximum cant deficiency for which the vehicle was assessed.    
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
      description: NGSI data type. It has to be MaximumSpeedAndCantDeficiency    
      enum:    
        - MaximumSpeedAndCantDeficiency    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleTypeMaximumCantDeficiency:    
      description: Vehicle type maximum cant deficiency    
      type: number    
      x-ngsi:    
        type: Property    
    vehicleTypeMaximumSpeed:    
      description: Vehicle type maximum speed    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/MaximumSpeedAndCantDeficiency    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/MaximumSpeedAndCantDeficiency/LICENSE.md    
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
#### MaximumSpeedAndCantDeficiency Valeurs clés de l'INSIG-v2 Exemple  
Voici un exemple de MaximumSpeedAndCantDeficiency au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:EYEV:77635914",  
  "dateCreated": "1978-04-01T14:31:45Z",  
  "dateModified": "1994-03-24T04:16:42Z",  
  "source": "Exist camera tend minute beyond.",  
  "name": "Mission provide place alone move they represent. This theory space sound face personal color. Thing skill kitchen behavior p",  
  "alternateName": "Read look newspaper",  
  "description": "Thing water act tend probably already. Defense future feeling.",  
  "dataProvider": "Evening source mean. Very word edge appe",  
  "owner": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:EKQU:29912232",  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:JOHF:20639722"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:WZSM:91628276"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      82.6869565,  
      24.725948  
    ]  
  },  
  "address": {  
    "streetAddress": "Happy actually court. Cut seek serious anything.",  
    "addressLocality": "Or worry third know leader. Son design detail in matter fine raise. Majority measure other size.",  
    "addressRegion": "Foreign tell several support enter police team respond. History senior position day four month painting. Central nice arm main more phone.",  
    "addressCountry": "Value discussio",  
    "postalCode": "Blue final campaign teacher coach guess. Serve billion development sp",  
    "postOfficeBoxNumber": "Stay never foot thought thing music scientist make.",  
    "streetNr": "Poor party produce sing thought those nature. Same how care either reduce those executive. People bed training continue my.",  
    "district": "Mother tonight this. Pull how blue public support s"  
  },  
  "areaServed": "Character ",  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": 864,  
  "vehicleTypeMaximumSpeed": 864  
}  
```  
</details>  
#### MaximumSpeedAndCantDeficiency NGSI-v2 normalisé Exemple  
Voici un exemple de MaximumSpeedAndCantDeficiency au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:EYEV:77635914",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1978-04-01T14:31:45Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1994-03-24T04:16:42Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Exist camera tend minute beyond."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Mission provide place alone move they represent. This theory space sound face personal color. Thing skill kitchen behavior p"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Read look newspaper"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Thing water act tend probably already. Defense future feeling."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Evening source mean. Very word edge appe"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:EKQU:29912232",  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:JOHF:20639722"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:WZSM:91628276"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          82.6869565,  
          24.725948  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Happy actually court. Cut seek serious anything."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Or worry third know leader. Son design detail in matter fine raise. Majority measure other size."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Foreign tell several support enter police team respond. History senior position day four month painting. Central nice arm main more phone."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Value discussio"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Blue final campaign teacher coach guess. Serve billion development sp"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Stay never foot thought thing music scientist make."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Poor party produce sing thought those nature. Same how care either reduce those executive. People bed training continue my."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Mother tonight this. Pull how blue public support s"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Character "  
  },  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": {  
    "type": "Number",  
    "value": 864  
  },  
  "vehicleTypeMaximumSpeed": {  
    "type": "Number",  
    "value": 864  
  }  
}  
```  
</details>  
#### MaximumSpeedAndCantDeficiency Valeurs clés de la NGSI-LD Exemple  
Voici un exemple de MaximumSpeedAndCantDeficiency au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:EYEV:77635914",  
  "dateCreated": "1978-04-01T14:31:45Z",  
  "dateModified": "1994-03-24T04:16:42Z",  
  "source": "Exist camera tend minute beyond.",  
  "name": "Mission provide place alone move they represent. This theory space sound face personal color. Thing skill kitchen behavior p",  
  "alternateName": "Read look newspaper",  
  "description": "Thing water act tend probably already. Defense future feeling.",  
  "dataProvider": "Evening source mean. Very word edge appe",  
  "owner": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:EKQU:29912232",  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:JOHF:20639722"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:WZSM:91628276"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      82.6869565,  
      24.725948  
    ]  
  },  
  "address": {  
    "streetAddress": "Happy actually court. Cut seek serious anything.",  
    "addressLocality": "Or worry third know leader. Son design detail in matter fine raise. Majority measure other size.",  
    "addressRegion": "Foreign tell several support enter police team respond. History senior position day four month painting. Central nice arm main more phone.",  
    "addressCountry": "Value discussio",  
    "postalCode": "Blue final campaign teacher coach guess. Serve billion development sp",  
    "postOfficeBoxNumber": "Stay never foot thought thing music scientist make.",  
    "streetNr": "Poor party produce sing thought those nature. Same how care either reduce those executive. People bed training continue my.",  
    "district": "Mother tonight this. Pull how blue public support s"  
  },  
  "areaServed": "Character ",  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": 864,  
  "vehicleTypeMaximumSpeed": 864,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### MaximumSpeedAndCantDeficiency NGSI-LD normalisé Exemple  
Voici un exemple de MaximumSpeedAndCantDeficiency au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:BFGJ:99213827",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1976-12-27T03:20:14Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1978-08-12T05:10:54Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "She response spring everyone western."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Base eat lose toward alone sure arrive. Writer "  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Something process c"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Natural window weight police easy second leader. Benefit I let inside."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Since possible deep care actually see side. Budget mean everybody ago hot."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:LZWP:28604460",  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:TIOK:10942469"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:GDOF:24605591"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -65.854435,  
        85.690336  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "College thing born our. Military join language old throw lot responsibility suddenly.",  
      "addressLocality": "Inside born clear run budget about green. Certainly baby under budget wonder.",  
      "addressRegion": "Purpose take tonight themselves foot maybe foreign. Administration enjoy tonight research five. City defense recently responsibility.",  
      "addressCountry": "Hope item civil. Population total carry today purpose significant rock. Pretty truth simply huge.",  
      "postalCode": "Cold that again including create. Upon recent pattern choose require message when reduce. Factor of",  
      "postOfficeBoxNumber": "Charge agree message edge main ",  
      "streetNr": "Everything same unit rule imagine option responsibility. Around out future almost some throw. Central president close work a",  
      "district": "Society white card region much specific. Without pretty my various price resource program quite."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Build positive decide listen behind city. Employee exactly nothing material. Ball window mention phone state concern."  
  },  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": {  
    "type": "Property",  
    "value": 615  
  },  
  "vehicleTypeMaximumSpeed": {  
    "type": "Property",  
    "value": 988  
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

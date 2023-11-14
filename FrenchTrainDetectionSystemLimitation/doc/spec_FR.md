<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Limitation du système de détection des trains français  
===============================================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Spécifique à la vérification de la compatibilité des itinéraires sur le réseau français. Sections avec :  
-1 Le tonnage circulé par voie est inférieur à 15000 tonnes/jour/voie.  
-2 Verrouillage directionnel  
-3 Délai de 45 secondes pour l'enclenchement directionnel  
-4 Installation avec annonce de circuit de voie  
-5 Absence d'une pédale d'assistance au triage dans le sens normal de circulation pour les lignes à double voie non réversibles  
-6 Absence de pédale d'aide aux manœuvres quel que soit le sens de circulation pour les lignes à voie unique et les voies à double sens de circulation  
-7 Absence de mécanisme d'annonce de la pédale  
-8 Délai de 45 secondes pour les dispositifs spécifiques de réinitialisation de l'annonce**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `frenchTrainDetectionSystemLimitationApplicable[boolean]`: La section avec limitation de la détection des trains est applicable, uniquement pour le réseau français  - `frenchTrainDetectionSystemLimitationNumber[uri]`: Section avec numéro de limitation de la détection des trains, uniquement pour le réseau français  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de FrenchTrainDetectionSystemLimitation  <!-- /30-PropertiesList -->  
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
FrenchTrainDetectionSystemLimitation:    
  description: "Specific for route compatibility check on French network. Sections with: \n-1 Tonnage circulated per track is inferior to 15000 tons/day/track \n-2 Directional Interlocking \n-3 45-second delay for directional interlocking \n-4 Installation with track circuit announcement \n-5 Absence of a shunting assistance pedal in the normal direction of circulation for non-reversible double track lines \n-6 Absence of a shunting assistance pedal regardless of the direction of traffic for single track lines and tracks for two way working \n-7 Absence of a pedal announcement mechanism \n-8 45-second delay for specific announcement reset devices"    
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
    frenchTrainDetectionSystemLimitationApplicable:    
      description: 'Section with train detection limitation is applicable, only for the French network'    
      type: boolean    
      x-ngsi:    
        type: Property    
    frenchTrainDetectionSystemLimitationNumber:    
      description: 'Section with train detection limitation number, only for French  network'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
      description: NGSI data type. It has to be FrenchTrainDetectionSystemLimitation    
      enum:    
        - FrenchTrainDetectionSystemLimitation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/FrenchTrainDetectionSystemLimitation    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/LICENSE.md    
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
#### FrenchTrainDetectionSystemLimitation Valeurs clés de l'INSIG-v2 Exemple  
Voici un exemple de FrenchTrainDetectionSystemLimitation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": "2014-09-23T15:45:27Z",  
  "dateModified": "1995-12-08T08:26:38Z",  
  "source": "Including since ",  
  "name": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure.",  
  "alternateName": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist",  
  "description": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military.",  
  "dataProvider": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science.",  
  "owner": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -21.934426,  
      6.101443  
    ]  
  },  
  "address": {  
    "streetAddress": "Wonder majority ability. Forget throughout discussion cost. Dream store case number.",  
    "addressLocality": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain.",  
    "addressRegion": "Lot watch matter. Item station",  
    "addressCountry": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill.",  
    "postalCode": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker.",  
    "postOfficeBoxNumber": "Near bed always benefit fine popular economic. Ever material save after scientist.",  
    "streetNr": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit",  
    "district": "Open administration space ahead. Soci"  
  },  
  "areaServed": "Including international kind animal customer. Identify large me. Field deal ",  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": false,  
  "frenchTrainDetectionSystemLimitationNumber": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183"  
}  
```  
</details>  
#### FrenchTrainDetectionSystemLimitation NGSI-v2 normalisé Exemple  
Voici un exemple de FrenchTrainDetectionSystemLimitation au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2014-09-23T15:45:27Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1995-12-08T08:26:38Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Including since "  
  },  
  "name": {  
    "type": "Text",  
    "value": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -21.934426,  
          6.101443  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Wonder majority ability. Forget throughout discussion cost. Dream store case number."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Lot watch matter. Item station"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Near bed always benefit fine popular economic. Ever material save after scientist."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Open administration space ahead. Soci"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Including international kind animal customer. Identify large me. Field deal "  
  },  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": {  
    "type": "Boolean",  
    "value": false  
  },  
  "frenchTrainDetectionSystemLimitationNumber": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183"  
  }  
}  
```  
</details>  
#### FrenchTrainDetectionSystemLimitation Valeurs clés de la NGSI-LD Exemple  
Voici un exemple de FrenchTrainDetectionSystemLimitation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": "2014-09-23T15:45:27Z",  
  "dateModified": "1995-12-08T08:26:38Z",  
  "source": "Including since ",  
  "name": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure.",  
  "alternateName": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist",  
  "description": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military.",  
  "dataProvider": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science.",  
  "owner": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -21.934426,  
      6.101443  
    ]  
  },  
  "address": {  
    "streetAddress": "Wonder majority ability. Forget throughout discussion cost. Dream store case number.",  
    "addressLocality": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain.",  
    "addressRegion": "Lot watch matter. Item station",  
    "addressCountry": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill.",  
    "postalCode": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker.",  
    "postOfficeBoxNumber": "Near bed always benefit fine popular economic. Ever material save after scientist.",  
    "streetNr": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit",  
    "district": "Open administration space ahead. Soci"  
  },  
  "areaServed": "Including international kind animal customer. Identify large me. Field deal ",  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": false,  
  "frenchTrainDetectionSystemLimitationNumber": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### FrenchTrainDetectionSystemLimitation NGSI-LD normalisé Exemple  
Voici un exemple de FrenchTrainDetectionSystemLimitation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:MUMN:30355615",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-12-11T22:05:23Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-08-04T09:15:57Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Vote middle customer. Know account build. Son garden image support TV"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Kid behavior decision century. Accept father hand hundred order. Space enjoy store radio office enter cover."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pretty four year people. Message mother action recently catch."  
  },  
  "description": {  
    "type": "Property",  
    "value": "National "  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Able involve move contain who director improve speak. Inc"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:OCPM:47545823",  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:YYEI:53415372"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:FKOO:81839190"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -78.20408,  
        125.044799  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Term ",  
      "addressLocality": "Return nature nothing soon democratic in. Time reach name mother pretty. Alone blue treatment together herself sound change painting.",  
      "addressRegion": "Always century cut do accept team despite. Region prevent save over degree. Nice each happen month away card.",  
      "addressCountry": "Land wife history method service they teach. Herself place movement throw discussion father. Nearly talk officer ok.",  
      "postalCode": "Difference less money reason final individual raise. Stay under car interesting check north policy. Purpose face worker apply surface.",  
      "postOfficeBoxNumber": "Baby possible guy set. Road style project hundred of its. Wife film g",  
      "streetNr": "Early star vote stor",  
      "district": "Idea buy concern relate se"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Image agent star total civil. Because a"  
  },  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": {  
    "type": "Property",  
    "value": false  
  },  
  "frenchTrainDetectionSystemLimitationNumber": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:FWCD:62453633"  
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

<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Signal  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/Signal/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un signal ferroviaire est une installation située à proximité de la voie ferrée et destinée à indiquer au conducteur du train la vitesse maximale autorisée dans la section de canton suivante.  
Définition RSM : Appareil permettant de donner une indication visuelle ou sonore conventionnelle, généralement concernant les mouvements des véhicules ferroviaires**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `relativeDistanceDangerPoint[number]`: Distance relative du point dangereux  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `signalId[string]`: Nom du signal  - `signalOrientation[uri]`: Orientation du signal  - `signalType[uri]`: Type de signal  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `track[uri]`: Poursuivre  - `type[string]`: Type de données NGSI. Il doit s'agir de Signal  <!-- /30-PropertiesList -->  
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
Signal:    
  description: |-    
    A railway signal is an installation next to the railway track for signalling the maximum allowed speed in the next block section to the train driver.    
    Definition RSM: Apparatus by means of which a conventional visual or acoustic indication is given, generally concerning the movements of railway vehicles.    
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
    relativeDistanceDangerPoint:    
      description: Relative distance of the danger point    
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
    signalId:    
      description: Name of signal    
      type: string    
      x-ngsi:    
        type: Property    
    signalOrientation:    
      description: Signal orientation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    signalType:    
      description: Type of signal    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    track:    
      description: Track    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI data type. It has to be Signal    
      enum:    
        - Signal    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Signal    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Signal/LICENSE.md    
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
#### Signal Valeurs clés de l'INSIG-v2 Exemple  
Voici un exemple de signal au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
}  
```  
</details>  
#### Signal NGSI-v2 normalisé Exemple  
Voici un exemple de signal au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1970-03-08T14:32:13Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2011-08-18T23:12:35Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Here choose style decade occur leader"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Drop"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Truth add because former. Indeed long yeah change near experience."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:OCNG:88914328",  
      "urn:ngsi-ld:Signal:items:QDWA:77960070"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:IKCH:27474652"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          7.167995,  
          -149.393214  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Upon certainly west population. A walk result product major draw "  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Account rich measure every price energy allow. Put customer c"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Prepare family across front. Nothing main religious strategy seven notice where."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Word wai"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Meet know training. Land grow old kid effect. Form director decide join draw."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Several center notice ever deal his. National parent fund focus pull those door."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Activity"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Number",  
    "value": 864  
  },  
  "signalId": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peac"  
  },  
  "signalOrientation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156"  
  },  
  "signalType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalType:CXMW:87784080"  
  },  
  "track": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
  }  
}  
```  
</details>  
#### Signal Valeurs clés NGSI-LD Exemple  
Voici un exemple de signal au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Signal NGSI-LD normalisé Exemple  
Voici un exemple de signal au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:SUMI:05987689",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2013-12-11T15:53:44Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-09-10T20:37:14Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Owner support present act enter."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Start read half."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Home state area operation respond early. Edge return condition federal."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Total again here high. Team report again ask product these cut."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Republican eight think start. Hot movie want serve father audience management."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:MZLV:03669390",  
      "urn:ngsi-ld:Signal:items:LNRS:49951624"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:JOYH:86575892"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -13.176379,  
        -116.163154  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Coach my discover both usually east page. Rather lead investment child as record resource. In product rise couple v",  
      "addressLocality": "Conference pull tax indeed. Very trou",  
      "addressRegion": "Man issue two memory every. Television traditional draw democratic.",  
      "addressCountry": "Fund threat they increase. Guy series politics bag.",  
      "postalCode": "Production later according down yes. Nothing my forward.",  
      "postOfficeBoxNumber": "Beat maintain people",  
      "streetNr": "East too Republican represent behind leader. Little television few Republican fire behavior good.",  
      "district": "Ever theory social special century spring."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "It she follow board blood. Certainly easy particular she sure by big. Say cold national expect rock. Value ski"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Property",  
    "value": 859  
  },  
  "signalId": {  
    "type": "Property",  
    "value": "Mean PM capital car particular head. Claim ago brother forget. Benefit start body ask yet age believe."  
  },  
  "signalOrientation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalOrientation:XSWZ:79200878"  
  },  
  "signalType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalType:OIXR:27955866"  
  },  
  "track": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:track:SBLI:67422940"  
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

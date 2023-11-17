<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Catégorie de véhicule à charge minimale d'essieu    
=========================================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/MinAxleLoadVehicleCategory/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Dépassé conformément à la modification du règlement (UE) 2019/777. Représente l'information qui indique la charge donnée en tonnes en fonction de la catégorie du véhicule. Ses propriétés sont minAxleLoadVehicleCategory et minAxleLoad.    
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `minAxleLoad[number]`: Charge minimale autorisée par essieu  - `minAxleLoadVehicleCategory[uri]`: Charge minimale par essieu Catégorie de véhicule  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de MinAxleLoadVehicleCategory.  <!-- /30-PropertiesList -->    
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
MinAxleLoadVehicleCategory:      
  description: Deprecated according to the ammendment to the Regulation (EU) 2019/777. Represents information that indicates the load given in tons depending of the category of vehicle. Its properties are minAxleLoadVehicleCategory and minAxleLoad.      
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
    minAxleLoad:      
      description: Minimum permitted axle load      
      type: number      
      x-ngsi:      
        type: Property      
    minAxleLoadVehicleCategory:      
      description: Minimum axle load vehicle category      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
      description: NGSI data type. It has to be MinAxleLoadVehicleCategory      
      enum:      
        - MinAxleLoadVehicleCategory      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/MinAxleLoadVehicleCategory      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/MinAxleLoadVehicleCategory/LICENSE.md      
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
#### MinAxleLoadVehicleCategory Valeurs clés de l'INS-V2 Exemple    
Voici un exemple de catégorie de véhicule MinAxleLoadVehicleCategory au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:KWOE:64087129",  
  "dateCreated": "2022-03-10T13:47:11Z",  
  "dateModified": "2000-12-08T03:53:13Z",  
  "source": "Address company tonight fight side night apply so. Best fine house past drug evening.",  
  "name": "Read church top never history old. Born edge health strong ",  
  "alternateName": "Lot material matter present from line cost. Season whatever become all wall.",  
  "description": "Not people Congress view window one.",  
  "dataProvider": "Stock minute pretty later. Federal as re",  
  "owner": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:JRVO:17137719",  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:WMGE:53516876"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:TXBP:98820710"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.8985275,  
      -11.102786  
    ]  
  },  
  "address": {  
    "streetAddress": "Accept treat however pretty manage. Term those sit seek ahead through. Camera attorney commercia",  
    "addressLocality": "Manager general nation behind. Prevent comput",  
    "addressRegion": "Song nature part. Degree ev",  
    "addressCountry": "Huge pressure ball music. Role chance govern",  
    "postalCode": "Really ago you director into little manager. Forget national never event important idea attorney. Small think rule individual player.",  
    "postOfficeBoxNumber": "Laugh front history fish four area. Quickly structure glass ne",  
    "streetNr": "Though guy police have chair learn member alone. Camera at if describe Ame",  
    "district": "Fear laugh continue. Read one teacher agency wear nothing customer. Great clear "  
  },  
  "areaServed": "Cultural worry floor professional focus. Need event ma",  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": 953.2,  
  "minAxleLoadVehicleCategory": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UHRQ:86221678"  
}  
```  
</details>    
#### MinAxleLoadVehicleCategory NGSI-v2 normalisé Exemple    
Voici un exemple de MinAxleLoadVehicleCategory au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:KWOE:64087129",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2022-03-10T13:47:11Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2000-12-08T03:53:13Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Address company tonight fight side night apply so. Best fine house past drug evening."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Read church top never history old. Born edge health strong "  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Lot material matter present from line cost. Season whatever become all wall."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Not people Congress view window one."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Stock minute pretty later. Federal as re"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:JRVO:17137719",  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:WMGE:53516876"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:TXBP:98820710"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        48.8985275,  
        -11.102786  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Accept treat however pretty manage. Term those sit seek ahead through. Camera attorney commercia",  
      "addressLocality": "Manager general nation behind. Prevent comput",  
      "addressRegion": "Song nature part. Degree ev",  
      "addressCountry": "Huge pressure ball music. Role chance govern",  
      "postalCode": "Really ago you director into little manager. Forget national never event important idea attorney. Small think rule individual player.",  
      "postOfficeBoxNumber": "Laugh front history fish four area. Quickly structure glass ne",  
      "streetNr": "Though guy police have chair learn member alone. Camera at if describe Ame",  
      "district": "Fear laugh continue. Read one teacher agency wear nothing customer. Great clear "  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Cultural worry floor professional focus. Need event ma"  
  },  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": {  
    "type": "Number",  
    "value": 953.2  
  },  
  "minAxleLoadVehicleCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UHRQ:86221678"  
  }  
}  
```  
</details>    
#### MinAxleLoadVehicleCategory Valeurs clés NGSI-LD Exemple    
Voici un exemple de catégorie de véhicule MinAxleLoadVehicleCategory au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:KWOE:64087129",  
  "dateCreated": "2022-03-10T13:47:11Z",  
  "dateModified": "2000-12-08T03:53:13Z",  
  "source": "Address company tonight fight side night apply so. Best fine house past drug evening.",  
  "name": "Read church top never history old. Born edge health strong ",  
  "alternateName": "Lot material matter present from line cost. Season whatever become all wall.",  
  "description": "Not people Congress view window one.",  
  "dataProvider": "Stock minute pretty later. Federal as re",  
  "owner": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:JRVO:17137719",  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:WMGE:53516876"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:TXBP:98820710"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.8985275,  
      -11.102786  
    ]  
  },  
  "address": {  
    "streetAddress": "Accept treat however pretty manage. Term those sit seek ahead through. Camera attorney commercia",  
    "addressLocality": "Manager general nation behind. Prevent comput",  
    "addressRegion": "Song nature part. Degree ev",  
    "addressCountry": "Huge pressure ball music. Role chance govern",  
    "postalCode": "Really ago you director into little manager. Forget national never event important idea attorney. Small think rule individual player.",  
    "postOfficeBoxNumber": "Laugh front history fish four area. Quickly structure glass ne",  
    "streetNr": "Though guy police have chair learn member alone. Camera at if describe Ame",  
    "district": "Fear laugh continue. Read one teacher agency wear nothing customer. Great clear "  
  },  
  "areaServed": "Cultural worry floor professional focus. Need event ma",  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": 953.2,  
  "minAxleLoadVehicleCategory": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UHRQ:86221678",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### MinAxleLoadVehicleCategory NGSI-LD normalisé Exemple    
Voici un exemple de MinAxleLoadVehicleCategory au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MinAxleLoadVehicleCategory:id:OTDA:84082973",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2015-01-14T11:01:00Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2019-02-23T06:12:58Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Doctor report certainly capital account finally. Science piece Republican identify. Ever recent cost account guess."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Suddenly something particular. Six front desig"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Politics total upon under fear. Know behind after draw billion."  
  },  
  "description": {  
    "type": "Property",  
    "value": "With b"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Glass ago movem"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:UQZZ:42282728",  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:YAYE:91747118"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MinAxleLoadVehicleCategory:items:FXFD:61807381"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.690969,  
        -150.542766  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Usually attorney ",  
      "addressLocality": "Nothing mind herself table. Again human camera",  
      "addressRegion": "Night party decade meet attack war. Father ready though leader peace development close newspa",  
      "addressCountry": "Mean provide government on. Amount although education start baby third scientist.",  
      "postalCode": "Give project central available class interest good. Author affect next west.",  
      "postOfficeBoxNumber": "Three successful reason happy. Simply movement really make walk nor.",  
      "streetNr": "Activity with positi",  
      "district": "Reason l"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Opportunity easy year night hospital. Image son computer. Company state apply down idea term."  
  },  
  "type": "MinAxleLoadVehicleCategory",  
  "minAxleLoad": {  
    "type": "Property",  
    "value": 939.1  
  },  
  "minAxleLoadVehicleCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:MinAxleLoadVehicleCategory:minAxleLoadVehicleCategory:UYDT:81696890"  
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

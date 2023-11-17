<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Véhicule    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/Vehicle/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Véhicule ou wagon spécifique capable de circuler sur les voies ferrées**.    
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `compositeBrakeBlockRetrofitted[boolean]`: Bloc de freinage en composite monté ultérieurement  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `manufacturingCountry[uri]`: Pays de production  - `name[string]`: Le nom de cet élément  - `operationalRestriction[uri]`: Restriction opérationnelle  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `quieterRoutesExemptedCountry[uri]`: Route moins bruyante pays exempté  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de Vehicle  - `vehicleKeeper[uri]`: Détenteur du véhicule  - `vehicleNumber[string]`: Numéro du véhicule  - `vehicleSeries[string]`: Série de véhicules  - `vehicleType[uri]`: Type de véhicule  <!-- /30-PropertiesList -->    
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
Vehicle:      
  description: A specific vehicle or wagon able to operate over railway lines.      
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
    compositeBrakeBlockRetrofitted:      
      description: Composite brake block retrofitted      
      type: boolean      
      x-ngsi:      
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
    manufacturingCountry:      
      description: Manufacturing country      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationalRestriction:      
      description: Operational restriction      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    quieterRoutesExemptedCountry:      
      description: Quieter route exempted country      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
      description: NGSI data type. It has to be Vehicle      
      enum:      
        - Vehicle      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleKeeper:      
      description: Vehicle keeper      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    vehicleNumber:      
      description: Vehicle number      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleSeries:      
      description: Vehicle series      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleType:      
      description: Vehicle type      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/Vehicle      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Vehicle/LICENSE.md      
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
#### Véhicule Valeurs clés de l'INSG-v2 Exemple    
Voici un exemple de véhicule au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": "1981-05-29T06:37:15Z",  
  "dateModified": "2007-08-18T15:43:14Z",  
  "source": "Visit research power especially ",  
  "name": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door",  
  "alternateName": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research",  
  "description": "Morning continue help p",  
  "dataProvider": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half.",  
  "owner": [  
    "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
    "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      20.376035,  
      172.96204  
    ]  
  },  
  "address": {  
    "streetAddress": "Lay agree media everyone. Ability because cover.",  
    "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
    "addressRegion": "Se",  
    "addressCountry": "Course down what maybe physical. Memory dev",  
    "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
    "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
    "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
    "district": "Order teacher yes head. Report partner without government discuss shoulder."  
  },  
  "areaServed": "Great office person",  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": true,  
  "vehicleNumber": "Of light force police. Indicate best need.",  
  "vehicleSeries": "High article bill ",  
  "manufacturingCountry": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975",  
  "operationalRestriction": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720",  
  "quieterRoutesExemptedCountry": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691",  
  "vehicleKeeper": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099",  
  "vehicleType": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377"  
}  
```  
</details>    
#### Véhicule NGSI-v2 normalisé Exemple    
Voici un exemple de véhicule au format JSON-LD normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1981-05-29T06:37:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2007-08-18T15:43:14Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Visit research power especially "  
  },  
  "name": {  
    "type": "Text",  
    "value": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Morning continue help p"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
      "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        20.376035,  
        172.96204  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Lay agree media everyone. Ability because cover.",  
      "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
      "addressRegion": "Se",  
      "addressCountry": "Course down what maybe physical. Memory dev",  
      "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
      "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
      "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
      "district": "Order teacher yes head. Report partner without government discuss shoulder."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Great office person"  
  },  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleNumber": {  
    "type": "Text",  
    "value": "Of light force police. Indicate best need."  
  },  
  "vehicleSeries": {  
    "type": "Text",  
    "value": "High article bill "  
  },  
  "manufacturingCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975"  
  },  
  "operationalRestriction": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720"  
  },  
  "quieterRoutesExemptedCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691"  
  },  
  "vehicleKeeper": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099"  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377"  
  }  
}  
```  
</details>    
#### Valeurs clés de l'INS-LD pour les véhicules Exemple    
Voici un exemple de véhicule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:TDKA:86614872",  
  "dateCreated": "1981-05-29T06:37:15Z",  
  "dateModified": "2007-08-18T15:43:14Z",  
  "source": "Visit research power especially ",  
  "name": "Feeling total key pass. Arm since speak television into. Score region specific base knowledge member door",  
  "alternateName": "Various management institution. Moment more ahead chance happy table herself. There pattern feel out. Show success research",  
  "description": "Morning continue help p",  
  "dataProvider": "Or only go together theory. Effort identify role work Congress forward citizen. Than fear turn success raise price half.",  
  "owner": [  
    "urn:ngsi-ld:Vehicle:items:TWCU:98173996",  
    "urn:ngsi-ld:Vehicle:items:YYBK:47777639"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Vehicle:items:EUJW:18707883"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      20.376035,  
      172.96204  
    ]  
  },  
  "address": {  
    "streetAddress": "Lay agree media everyone. Ability because cover.",  
    "addressLocality": "Watch right student high TV. Moment well seek natural write choose be real. Recognize note themselves foot fast eat visit her. Simple chair green generation large.",  
    "addressRegion": "Se",  
    "addressCountry": "Course down what maybe physical. Memory dev",  
    "postalCode": "White quite go which. Lay wall carry election adult across. Growth morning daughter by both animal choose agree.",  
    "postOfficeBoxNumber": "To bit provide individual. Drug let bed v",  
    "streetNr": "Of price ever raise their heart. Dinner song industry and family. Debate hold first say hotel fly federal.",  
    "district": "Order teacher yes head. Report partner without government discuss shoulder."  
  },  
  "areaServed": "Great office person",  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": true,  
  "vehicleNumber": "Of light force police. Indicate best need.",  
  "vehicleSeries": "High article bill ",  
  "manufacturingCountry": "urn:ngsi-ld:Vehicle:manufacturingCountry:TILS:75334975",  
  "operationalRestriction": "urn:ngsi-ld:Vehicle:operationalRestriction:HMKL:62237720",  
  "quieterRoutesExemptedCountry": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:XMUI:51546691",  
  "vehicleKeeper": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZIEP:97566099",  
  "vehicleType": "urn:ngsi-ld:Vehicle:vehicleType:CAMN:07078377",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Véhicule NGSI-LD normalisé Exemple    
Voici un exemple de véhicule au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Vehicle:id:RFYH:06883935",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-06-19T07:24:12Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1998-03-27T15:27:54Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Project option account government. Ask company grow."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Part matter sh"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nearly alone the when together. Whole sure would require mission."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Church exactly remain situation training effect resource. Movie describe concern single as population moment. Director stage range professional fast. Sell talk onto whom question job decid"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Place teacher support teach practice son pay college. Sit certain near short area by decision. Stand size guy reason rese"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:EBYW:72457592",  
      "urn:ngsi-ld:Vehicle:items:MJUB:28310670"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Vehicle:items:WNSX:51918079"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -37.542901,  
        -116.836751  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Rich thousand authority beat best white free. Tend season get prevent wind. Catch door foot wrong citizen miss develop.",  
      "addressLocality": "Test growth another. Be easy painting human. College ",  
      "addressRegion": "Nice pay pattern sense education game. Tonight yourself spring though participant threat majority.",  
      "addressCountry": "Purpose case eight just. Cause discussion technology sing.",  
      "postalCode": "Yeah conference push determine I tough.",  
      "postOfficeBoxNumber": "Sea also cell office force letter week. Total create as onto people. Full wall address early lose everything kid.",  
      "streetNr": "Why rise PM mother bank light. Ha",  
      "district": "Responsibility blue increase. Newspaper remain else"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Make own mother news film PM some. All arrive than put cold five stand."  
  },  
  "type": "Vehicle",  
  "compositeBrakeBlockRetrofitted": {  
    "type": "Property",  
    "value": false  
  },  
  "vehicleNumber": {  
    "type": "Property",  
    "value": "Sure stock standard child goal in. Option hand parent piece no."  
  },  
  "vehicleSeries": {  
    "type": "Property",  
    "value": "Public story thus wind whether. Sometimes attorney couple person hand green. Within seek sid"  
  },  
  "manufacturingCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:manufacturingCountry:YUHQ:94193670"  
  },  
  "operationalRestriction": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:operationalRestriction:HSZJ:08079193"  
  },  
  "quieterRoutesExemptedCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:quieterRoutesExemptedCountry:HKQL:88249057"  
  },  
  "vehicleKeeper": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:vehicleKeeper:ZJDS:72987137"  
  },  
  "vehicleType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:vehicleType:KUTI:03320913"  
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

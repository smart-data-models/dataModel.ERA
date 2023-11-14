<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : ContactLineSystem  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/ContactLineSystem/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Système utilisé pour transmettre l'énergie électrique aux véhicules routiers ou ferroviaires**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `conditionalRegenerativeBrake[boolean]`: Autorisation de freinage par récupération  - `conditionsAppliedRegenerativeBraking[string]`: Conditions applicables au freinage par récupération  - `conditionsChargingElectricEnergyStorage[string]`: Conditions autorisées pour la charge des accumulateurs d'énergie électrique à des fins de traction à l'arrêt  - `contactLineSystemType[uri]`: Type de système de ligne de contact  - `currentLimitationRequired[boolean]`: Limitation du courant ou de la puissance sur la carte requise  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `energySupplySystem[uri]`: Système d'approvisionnement en énergie  - `energySupplySystemTSICompliant[boolean]`: Système d'approvisionnement en énergie conforme aux STI  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `maxCurrentStandstillPantograph[number]`: Courant maximal à l'arrêt par pantographe  - `maxTrainCurrent[number]`: Courant maximal du train  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `permissionChargingElectricEnergyTractionStandstill[boolean]`: Autorisation de charger le stockage d'énergie électrique à des fins de traction à l'arrêt  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type de données NGSI. Il doit s'agir de ContactLineSystem  - `umax2[number]`: Umax2 pour les lignes visées aux sections 7.4.2.2.1 et 7.4.2.11.1 du règlement (UE)1301/2014.  <!-- /30-PropertiesList -->  
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
ContactLineSystem:    
  description: System that is used to transmit electrical energy to road or rail vehicles.    
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
    conditionalRegenerativeBrake:    
      description: Permission for regenerative braking    
      type: boolean    
      x-ngsi:    
        type: Property    
    conditionsAppliedRegenerativeBraking:    
      description: Conditions applying in regards to regenerative braking    
      type: string    
      x-ngsi:    
        type: Property    
    conditionsChargingElectricEnergyStorage:    
      description: Permitted conditions for charging electric energy storage for traction purposes at standstill    
      type: string    
      x-ngsi:    
        type: Property    
    contactLineSystemType:    
      description: Type of contact line system    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    currentLimitationRequired:    
      description: Current or power limitation on board required    
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
    energySupplySystem:    
      description: Energy supply system    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    energySupplySystemTSICompliant:    
      description: Energy supply system TSI compliant    
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
    maxTrainCurrent:    
      description: Maximum train current    
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
    permissionChargingElectricEnergyTractionStandstill:    
      description: Permission for charging electric energy storage for traction purposes at standstill    
      type: boolean    
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
      description: NGSI data type. It has to be ContactLineSystem    
      enum:    
        - ContactLineSystem    
      type: string    
      x-ngsi:    
        type: Property    
    umax2:    
      description: Umax2 for lines referred to in sections 7.4.2.2.1 and 7.4.2.11.1 of Regulation (EU)1301/2014.    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/ContactLineSystem    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/ContactLineSystem/LICENSE.md    
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
#### ContactLineSystem Valeurs clés NGSI-v2 Exemple  
Voici un exemple de ContactLineSystem au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:ORAF:23996206",  
  "dateCreated": "2018-03-08T03:23:31Z",  
  "dateModified": "2021-08-20T12:07:54Z",  
  "source": "Eat election thought team pressure. Tend page true affect politics shoulder provide. Life message important cost night itself event.",  
  "name": "Southern no country without man white when. Let",  
  "alternateName": "Arm detail soon day wait our open number. Society argue a learn identify.",  
  "description": "Girl main model democratic.",  
  "dataProvider": "Sort watch here letter choice down nature. ",  
  "owner": [  
    "urn:ngsi-ld:ContactLineSystem:items:OPHQ:68569337",  
    "urn:ngsi-ld:ContactLineSystem:items:AWZO:22775427"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:ContactLineSystem:items:CXFY:92898664"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      16.1310075,  
      131.493498  
    ]  
  },  
  "address": {  
    "streetAddress": "Nor when wall inside. Discussion experience include rest rather form large.",  
    "addressLocality": "Wife significant think simply author thus town. Sort purpose style discover study. Again themse",  
    "addressRegion": "Political star worker bar. Land if war nothing year with easy. Section other national new eye tree. Thus fine skin address hour imagine.",  
    "addressCountry": "Hour relationship apply practice this development hotel. Any economy score none join including others.",  
    "postalCode": "Present why Mrs former almost black. Officer concern natural federal ",  
    "postOfficeBoxNumber": "Subject yourself remain seek ability energy",  
    "streetNr": "Their staff check TV break. Cup person all air. Show explain maintain ",  
    "district": "Enjoy record as yeah discuss. Even own itself."  
  },  
  "areaServed": "Throughout month dark figure add ago small. Point and financial mu",  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": true,  
  "conditionsAppliedRegenerativeBraking": "Never understand could change arrive. Senior change can surface language.",  
  "conditionsChargingElectricEnergyStorage": "Vo",  
  "currentLimitationRequired": false,  
  "energySupplySystemTSICompliant": false,  
  "maxCurrentStandstillPantograph": 615.8,  
  "maxTrainCurrent": 864,  
  "permissionChargingElectricEnergyTractionStandstill": false,  
  "umax2": 864,  
  "contactLineSystemType": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:PLSG:66048764",  
  "energySupplySystem": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:WZTE:82421948"  
}  
```  
</details>  
#### ContactLineSystem NGSI-v2 normalisé Exemple  
Voici un exemple de ContactLineSystem au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:ORAF:23996206",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2018-03-08T03:23:31Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-08-20T12:07:54Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Eat election thought team pressure. Tend page true affect politics shoulder provide. Life message important cost night itself event."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Southern no country without man white when. Let"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Arm detail soon day wait our open number. Society argue a learn identify."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Girl main model democratic."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Sort watch here letter choice down nature. "  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:OPHQ:68569337",  
      "urn:ngsi-ld:ContactLineSystem:items:AWZO:22775427"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:CXFY:92898664"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          16.1310075,  
          131.493498  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Nor when wall inside. Discussion experience include rest rather form large."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Wife significant think simply author thus town. Sort purpose style discover study. Again themse"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Political star worker bar. Land if war nothing year with easy. Section other national new eye tree. Thus fine skin address hour imagine."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Hour relationship apply practice this development hotel. Any economy score none join including others."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Present why Mrs former almost black. Officer concern natural federal "  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Subject yourself remain seek ability energy"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Their staff check TV break. Cup person all air. Show explain maintain "  
      },  
      "district": {  
        "type": "Text",  
        "value": "Enjoy record as yeah discuss. Even own itself."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Throughout month dark figure add ago small. Point and financial mu"  
  },  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": {  
    "type": "Boolean",  
    "value": true  
  },  
  "conditionsAppliedRegenerativeBraking": {  
    "type": "Text",  
    "value": "Never understand could change arrive. Senior change can surface language."  
  },  
  "conditionsChargingElectricEnergyStorage": {  
    "type": "Text",  
    "value": "Vo"  
  },  
  "currentLimitationRequired": {  
    "type": "Boolean",  
    "value": false  
  },  
  "energySupplySystemTSICompliant": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Number",  
    "value": 615.8  
  },  
  "maxTrainCurrent": {  
    "type": "Number",  
    "value": 864  
  },  
  "permissionChargingElectricEnergyTractionStandstill": {  
    "type": "Boolean",  
    "value": false  
  },  
  "umax2": {  
    "type": "Number",  
    "value": 864  
  },  
  "contactLineSystemType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:PLSG:66048764"  
  },  
  "energySupplySystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:WZTE:82421948"  
  }  
}  
```  
</details>  
#### ContactLineSystem Valeurs clés NGSI-LD Exemple  
Voici un exemple de ContactLineSystem au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:ORAF:23996206",  
  "dateCreated": "2018-03-08T03:23:31Z",  
  "dateModified": "2021-08-20T12:07:54Z",  
  "source": "Eat election thought team pressure. Tend page true affect politics shoulder provide. Life message important cost night itself event.",  
  "name": "Southern no country without man white when. Let",  
  "alternateName": "Arm detail soon day wait our open number. Society argue a learn identify.",  
  "description": "Girl main model democratic.",  
  "dataProvider": "Sort watch here letter choice down nature. ",  
  "owner": [  
    "urn:ngsi-ld:ContactLineSystem:items:OPHQ:68569337",  
    "urn:ngsi-ld:ContactLineSystem:items:AWZO:22775427"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:ContactLineSystem:items:CXFY:92898664"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      16.1310075,  
      131.493498  
    ]  
  },  
  "address": {  
    "streetAddress": "Nor when wall inside. Discussion experience include rest rather form large.",  
    "addressLocality": "Wife significant think simply author thus town. Sort purpose style discover study. Again themse",  
    "addressRegion": "Political star worker bar. Land if war nothing year with easy. Section other national new eye tree. Thus fine skin address hour imagine.",  
    "addressCountry": "Hour relationship apply practice this development hotel. Any economy score none join including others.",  
    "postalCode": "Present why Mrs former almost black. Officer concern natural federal ",  
    "postOfficeBoxNumber": "Subject yourself remain seek ability energy",  
    "streetNr": "Their staff check TV break. Cup person all air. Show explain maintain ",  
    "district": "Enjoy record as yeah discuss. Even own itself."  
  },  
  "areaServed": "Throughout month dark figure add ago small. Point and financial mu",  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": true,  
  "conditionsAppliedRegenerativeBraking": "Never understand could change arrive. Senior change can surface language.",  
  "conditionsChargingElectricEnergyStorage": "Vo",  
  "currentLimitationRequired": false,  
  "energySupplySystemTSICompliant": false,  
  "maxCurrentStandstillPantograph": 615.8,  
  "maxTrainCurrent": 864,  
  "permissionChargingElectricEnergyTractionStandstill": false,  
  "umax2": 864,  
  "contactLineSystemType": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:PLSG:66048764",  
  "energySupplySystem": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:WZTE:82421948",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### ContactLineSystem NGSI-LD normalisé Exemple  
Voici un exemple de ContactLineSystem au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ContactLineSystem:id:YUFG:14034194",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1989-01-20T05:58:09Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1972-01-07T08:46:29Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Pick red ability information. Positive development policy financial learn career. Nothing firm at memory."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Face response pass cut perform easy. Discuss couple think no difference singl"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Trade international loss friend every sing available because. Per agent stock call manage share."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Worry certain if our thought it resource. Everyone blood commercial respond face take probably. Culture their concern trade crime."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Including future politics return table mention section. Together year agency know. Manager image positive suffer perform enough."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:GYWA:00643390",  
      "urn:ngsi-ld:ContactLineSystem:items:WEEM:69764788"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:ContactLineSystem:items:WMLL:21052726"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        88.082114,  
        -116.450812  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Role even option. Push play firm may. City grow director audience body reduce.",  
      "addressLocality": "Report yet sit hundred use political his. Build special recently make.",  
      "addressRegion": "Floor someone tend. News fight against fall television. Writer full bed official concern small.",  
      "addressCountry": "Lead consider hundred offer look hit future. Fly appear remain pattern wall goal.",  
      "postalCode": "Suddenly our visit that field. Trip fi",  
      "postOfficeBoxNumber": "Current wha",  
      "streetNr": "Page effort station.",  
      "district": "Next respond oil important guy leave capital. Provide street good create range growth war. Visit across media consumer land spring total well."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "White laugh space discussion. Throw international continue while senior gas pro"  
  },  
  "type": "ContactLineSystem",  
  "conditionalRegenerativeBrake": {  
    "type": "Property",  
    "value": false  
  },  
  "conditionsAppliedRegenerativeBraking": {  
    "type": "Property",  
    "value": "Design hard short dream cost entire year. Better consumer recently. Population rich recent tough environmental rock image speech."  
  },  
  "conditionsChargingElectricEnergyStorage": {  
    "type": "Property",  
    "value": "Force inside tell. Daughter miss true member voice thus. Dream many which church strong "  
  },  
  "currentLimitationRequired": {  
    "type": "Property",  
    "value": true  
  },  
  "energySupplySystemTSICompliant": {  
    "type": "Property",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Property",  
    "value": 773.8  
  },  
  "maxTrainCurrent": {  
    "type": "Property",  
    "value": 68  
  },  
  "permissionChargingElectricEnergyTractionStandstill": {  
    "type": "Property",  
    "value": false  
  },  
  "umax2": {  
    "type": "Property",  
    "value": 756  
  },  
  "contactLineSystemType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ContactLineSystem:contactLineSystemType:JNYV:94337272"  
  },  
  "energySupplySystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ContactLineSystem:energySupplySystem:BFQY:01787468"  
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

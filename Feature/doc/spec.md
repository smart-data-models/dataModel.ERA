<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Feature  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/Feature/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Class that encompasses the features that are part of the physical infrastructure (class InfrastructureObject) and the topological objects (class TopologicalObject). It is a subclass of the geographical Feature class that has a spatial representation.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `currentlyValid[boolean]`: Currently valid  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `length[number]`: Length  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI data type. It has to be Feature  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
data model mapped from ERA ontology https://data-interop.era.europa.eu/era-vocabulary (European Union Agency for Railways)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Feature:    
  description: Class that encompasses the features that are part of the physical infrastructure (class InfrastructureObject) and the topological objects (class TopologicalObject). It is a subclass of the geographical Feature class that has a spatial representation.    
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
    currentlyValid:    
      description: Currently valid    
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
    length:    
      description: Length    
      type: number    
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
      description: NGSI data type. It has to be Feature    
      enum:    
        - Feature    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Feature    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Feature/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json    
  x-model-tags: 'ERA vocabulary, railway, train'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### Feature NGSI-v2 key-values Example    
Here is an example of a Feature in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:SWJZ:26079559",  
  "dateCreated": "2000-11-09T19:30:45Z",  
  "dateModified": "1982-01-16T22:00:49Z",  
  "source": "Table live too always movie.",  
  "name": "Somebody his past show. Provide goal who",  
  "alternateName": "Any rise challenge type.",  
  "description": "Responsibility our class apply",  
  "dataProvider": "Rich clear century others contain help. Not about certainly box. Wi",  
  "owner": [  
    "urn:ngsi-ld:Feature:items:WDIR:57277343",  
    "urn:ngsi-ld:Feature:items:YUTH:26427588"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Feature:items:EGCJ:82697620"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      71.6338955,  
      -141.895474  
    ]  
  },  
  "address": {  
    "streetAddress": "Return end child.",  
    "addressLocality": "Trip professional staff answer. Kitchen yard ten worry suggest whose.",  
    "addressRegion": "Art music already home low. Human despite easy back wind people.",  
    "addressCountry": "Great main confere",  
    "postalCode": "Door weight control head southern pass. Practice art anything even.",  
    "postOfficeBoxNumber": "Clear health there former approach. Now money among budget. Current kind page rather.",  
    "streetNr": "Eight quality not include six. Line response ahead girl we. Answer finally daughter everybody fast.",  
    "district": "Camera worker machine away have loss practice since. Along indeed debate Mrs cut. Lot game charge indeed."  
  },  
  "areaServed": "Real throw sell. Two remembe",  
  "type": "Feature",  
  "currentlyValid": true,  
  "length": 845.9  
}  
```  
</details>  
#### Feature NGSI-v2 normalized Example    
Here is an example of a Feature in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:SWJZ:26079559",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2000-11-09T19:30:45Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1982-01-16T22:00:49Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Table live too always movie."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Somebody his past show. Provide goal who"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Any rise challenge type."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Responsibility our class apply"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Rich clear century others contain help. Not about certainly box. Wi"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Feature:items:WDIR:57277343",  
      "urn:ngsi-ld:Feature:items:YUTH:26427588"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Feature:items:EGCJ:82697620"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          71.6338955,  
          -141.895474  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Return end child."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Trip professional staff answer. Kitchen yard ten worry suggest whose."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Art music already home low. Human despite easy back wind people."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Great main confere"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Door weight control head southern pass. Practice art anything even."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Clear health there former approach. Now money among budget. Current kind page rather."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Eight quality not include six. Line response ahead girl we. Answer finally daughter everybody fast."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Camera worker machine away have loss practice since. Along indeed debate Mrs cut. Lot game charge indeed."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Real throw sell. Two remembe"  
  },  
  "type": "Feature",  
  "currentlyValid": {  
    "type": "Boolean",  
    "value": true  
  },  
  "length": {  
    "type": "Number",  
    "value": 845.9  
  }  
}  
```  
</details>  
#### Feature NGSI-LD key-values Example    
Here is an example of a Feature in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:SWJZ:26079559",  
  "dateCreated": "2000-11-09T19:30:45Z",  
  "dateModified": "1982-01-16T22:00:49Z",  
  "source": "Table live too always movie.",  
  "name": "Somebody his past show. Provide goal who",  
  "alternateName": "Any rise challenge type.",  
  "description": "Responsibility our class apply",  
  "dataProvider": "Rich clear century others contain help. Not about certainly box. Wi",  
  "owner": [  
    "urn:ngsi-ld:Feature:items:WDIR:57277343",  
    "urn:ngsi-ld:Feature:items:YUTH:26427588"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Feature:items:EGCJ:82697620"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      71.6338955,  
      -141.895474  
    ]  
  },  
  "address": {  
    "streetAddress": "Return end child.",  
    "addressLocality": "Trip professional staff answer. Kitchen yard ten worry suggest whose.",  
    "addressRegion": "Art music already home low. Human despite easy back wind people.",  
    "addressCountry": "Great main confere",  
    "postalCode": "Door weight control head southern pass. Practice art anything even.",  
    "postOfficeBoxNumber": "Clear health there former approach. Now money among budget. Current kind page rather.",  
    "streetNr": "Eight quality not include six. Line response ahead girl we. Answer finally daughter everybody fast.",  
    "district": "Camera worker machine away have loss practice since. Along indeed debate Mrs cut. Lot game charge indeed."  
  },  
  "areaServed": "Real throw sell. Two remembe",  
  "type": "Feature",  
  "currentlyValid": true,  
  "length": 845.9,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Feature NGSI-LD normalized Example    
Here is an example of a Feature in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:NAYS:82910625",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2015-12-02T02:59:26Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-04-07T17:47:44Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Station pick serious other seat. Power way score institution. Bill TV some h"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Production factor successful white she live size. Fire social air enter. Skill son sell painting do garden true."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Such culture so million. His break business remembe"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Lose edge want describe nice. Else course war direction international near ask second."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Cell force pull majo"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Feature:items:NLJN:58101473",  
      "urn:ngsi-ld:Feature:items:NCUV:87294142"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Feature:items:TOZC:68395253"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -21.7138025,  
        -147.023625  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Film tend professional them against between.",  
      "addressLocality": "Country wall dream shoulder treatm",  
      "addressRegion": "Nothing seek address military edge analysis. Well difference series adult method rather",  
      "addressCountry": "Rate purpose see clearly new serious effort. Law travel draw i",  
      "postalCode": "Owner because learn medical. Education adult",  
      "postOfficeBoxNumber": "As true environmental give. Wait how machine century task.",  
      "streetNr": "Anything president her culture each. Several hold couple hair rule manage early most.",  
      "district": "Beyond state c"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Market yeah different one range lay blood. Operation into near drug something. Beautiful effort"  
  },  
  "type": "Feature",  
  "currentlyValid": {  
    "type": "Property",  
    "value": true  
  },  
  "length": {  
    "type": "Property",  
    "value": 955.0  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

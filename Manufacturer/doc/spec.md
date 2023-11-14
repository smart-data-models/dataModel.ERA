<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Manufacturer  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/Manufacturer/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **A company or organization that manufactures vehicles.**  
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI data type. It has to be Manufacturer  <!-- /30-PropertiesList -->  
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
Manufacturer:    
  description: A company or organization that manufactures vehicles.    
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
      description: NGSI data type. It has to be Manufacturer    
      enum:    
        - Manufacturer    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Manufacturer    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Manufacturer/LICENSE.md    
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
#### Manufacturer NGSI-v2 key-values Example    
Here is an example of a Manufacturer in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:VOTT:26597132",  
  "dateCreated": "1999-05-25T21:10:20Z",  
  "dateModified": "1981-08-05T14:31:51Z",  
  "source": "Each low class pretty ball. Heavy Mrs only strategy. Like reduce man security.",  
  "name": "Six store sor",  
  "alternateName": "Expert maintain actually goal. Bank cul",  
  "description": "Wha",  
  "dataProvider": "Market small also far they measure consumer.",  
  "owner": [  
    "urn:ngsi-ld:Manufacturer:items:HBYI:32485482",  
    "urn:ngsi-ld:Manufacturer:items:OBGX:52905874"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Manufacturer:items:UMRJ:07396067"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -7.7970405,  
      -90.393951  
    ]  
  },  
  "address": {  
    "streetAddress": "Goal feel cultural race officer. Future table pay. Grow letter though all type century ",  
    "addressLocality": "Shoulder hold leader hospital since sometimes.",  
    "addressRegion": "Type attorney chance father adult raise. Society author probably.",  
    "addressCountry": "Minute tax really road six.",  
    "postalCode": "Anything wife easy maintain. Hair budget sea significant. Particularly weight anything three feel second.",  
    "postOfficeBoxNumber": "Speech Democrat most life fine my.",  
    "streetNr": "Age court anyone less your. Wear camera responsibility ski",  
    "district": "Involve mention her pr"  
  },  
  "areaServed": "By there since Congress themselves girl everyone. Nature grow important yes.",  
  "type": "Manufacturer"  
}  
```  
</details>  
#### Manufacturer NGSI-v2 normalized Example    
Here is an example of a Manufacturer in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:VOTT:26597132",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1999-05-25T21:10:20Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1981-08-05T14:31:51Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Each low class pretty ball. Heavy Mrs only strategy. Like reduce man security."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Six store sor"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Expert maintain actually goal. Bank cul"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Wha"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Market small also far they measure consumer."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:HBYI:32485482",  
      "urn:ngsi-ld:Manufacturer:items:OBGX:52905874"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:UMRJ:07396067"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -7.7970405,  
          -90.393951  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Goal feel cultural race officer. Future table pay. Grow letter though all type century "  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Shoulder hold leader hospital since sometimes."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Type attorney chance father adult raise. Society author probably."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Minute tax really road six."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Anything wife easy maintain. Hair budget sea significant. Particularly weight anything three feel second."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Speech Democrat most life fine my."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Age court anyone less your. Wear camera responsibility ski"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Involve mention her pr"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "By there since Congress themselves girl everyone. Nature grow important yes."  
  },  
  "type": "Manufacturer"  
}  
```  
</details>  
#### Manufacturer NGSI-LD key-values Example    
Here is an example of a Manufacturer in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:VOTT:26597132",  
  "dateCreated": "1999-05-25T21:10:20Z",  
  "dateModified": "1981-08-05T14:31:51Z",  
  "source": "Each low class pretty ball. Heavy Mrs only strategy. Like reduce man security.",  
  "name": "Six store sor",  
  "alternateName": "Expert maintain actually goal. Bank cul",  
  "description": "Wha",  
  "dataProvider": "Market small also far they measure consumer.",  
  "owner": [  
    "urn:ngsi-ld:Manufacturer:items:HBYI:32485482",  
    "urn:ngsi-ld:Manufacturer:items:OBGX:52905874"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Manufacturer:items:UMRJ:07396067"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -7.7970405,  
      -90.393951  
    ]  
  },  
  "address": {  
    "streetAddress": "Goal feel cultural race officer. Future table pay. Grow letter though all type century ",  
    "addressLocality": "Shoulder hold leader hospital since sometimes.",  
    "addressRegion": "Type attorney chance father adult raise. Society author probably.",  
    "addressCountry": "Minute tax really road six.",  
    "postalCode": "Anything wife easy maintain. Hair budget sea significant. Particularly weight anything three feel second.",  
    "postOfficeBoxNumber": "Speech Democrat most life fine my.",  
    "streetNr": "Age court anyone less your. Wear camera responsibility ski",  
    "district": "Involve mention her pr"  
  },  
  "areaServed": "By there since Congress themselves girl everyone. Nature grow important yes.",  
  "type": "Manufacturer",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Manufacturer NGSI-LD normalized Example    
Here is an example of a Manufacturer in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Manufacturer:id:YVMH:41957963",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-03-24T09:32:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1988-09-15T15:09:48Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "With human sound stock. Hundred note morning then compare process music red. Describe as try organization light high."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Newspaper huge dinner later. Wide democratic near product loss. Live own way employee local exactly far. Defense day benefit out."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Goal bl"  
  },  
  "description": {  
    "type": "Property",  
    "value": "History agency occur drop. Consider cold any defense nice cause. Study spring company step."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Prevent knowledge station turn modern energy. Hundred ok morn"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:OYJB:95943841",  
      "urn:ngsi-ld:Manufacturer:items:KFIM:77965610"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Manufacturer:items:MEPT:90382167"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -29.2915185,  
        -116.219785  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Unit anything much kind attorney. A huge talk receive.",  
      "addressLocality": "Sign operation moment establish laugh. Everybody skill where catch theory. Child later some pretty military.",  
      "addressRegion": "See him total language know. Audience discover responsibility young experience.",  
      "addressCountry": "Through situation laugh others energy particu",  
      "postalCode": "Top firm service. Program system skin should may for police.",  
      "postOfficeBoxNumber": "Well look firm option prepare education. Teacher police turn Democrat.",  
      "streetNr": "Feeling glass century hotel fire which. Old on necessary style article technology know. Air return health method.",  
      "district": "Ability garden behavior keep exactly. Clearly treat type expect bed near."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Real purpose memory rule. Economy responsibility building rather. Project glass throughout final oil specific."  
  },  
  "type": "Manufacturer",  
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

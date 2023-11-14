<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Siding  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/Siding/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Sidings are all those tracks where running trains in service movements ends and which are not used for operational routing of a train.**  
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `demonstrationINF[string]`: EI declaration of demonstration for track/siding [INF]  - `description[string]`: A description of this item  - `gradient[number]`: Gradient for stabling tracks  - `hasElectricShoreSupply[boolean]`: Existence of electric shore supply  - `hasExternalCleaning[boolean]`: Existence of external cleaning facilities  - `hasRefuelling[boolean]`: Existence of refuelling  - `hasSandRestocking[boolean]`: Existence of sand restocking  - `hasToiletDischarge[boolean]`: Existence of toilet discharge  - `hasWaterRestocking[boolean]`: Existence of water restocking  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxCurrentStandstillPantograph[number]`: Maximum current at standstill per pantograph  - `minimumHorizontalRadius[number]`: Minimum radius of horizontal curve  - `minimumVerticalRadius[string]`: Minimum radius of vertical curve  - `minimumVerticalRadiusCrest[number]`: Minimum radius of vertical curve crest  - `minimumVerticalRadiusHollow[number]`: Minimum radius of vertical curve hollow  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `sidingId[string]`: Identification of siding  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `tenClassification[uri]`: TEN classification (of track, of platform, of siding)  - `type[string]`: NGSI data type. It has to be Siding  - `verificationINF[string]`: EC declaration of verification for track/siding [INF]  <!-- /30-PropertiesList -->  
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
Siding:    
  description: Sidings are all those tracks where running trains in service movements ends and which are not used for operational routing of a train.    
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
    demonstrationINF:    
      description: 'EI declaration of demonstration for track/siding [INF]'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    gradient:    
      description: Gradient for stabling tracks    
      type: number    
      x-ngsi:    
        type: Property    
    hasElectricShoreSupply:    
      description: Existence of electric shore supply    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasExternalCleaning:    
      description: Existence of external cleaning facilities    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasRefuelling:    
      description: Existence of refuelling    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasSandRestocking:    
      description: Existence of sand restocking    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasToiletDischarge:    
      description: Existence of toilet discharge    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasWaterRestocking:    
      description: Existence of water restocking    
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
    minimumHorizontalRadius:    
      description: Minimum radius of horizontal curve    
      type: number    
      x-ngsi:    
        type: Property    
    minimumVerticalRadius:    
      description: Minimum radius of vertical curve    
      type: string    
      x-ngsi:    
        type: Property    
    minimumVerticalRadiusCrest:    
      description: Minimum radius of vertical curve crest    
      type: number    
      x-ngsi:    
        type: Property    
    minimumVerticalRadiusHollow:    
      description: Minimum radius of vertical curve hollow    
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
    sidingId:    
      description: Identification of siding    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    tenClassification:    
      description: 'TEN classification (of track, of platform, of siding)'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI data type. It has to be Siding    
      enum:    
        - Siding    
      type: string    
      x-ngsi:    
        type: Property    
    verificationINF:    
      description: 'EC declaration of verification for track/siding [INF]'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Siding    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Siding/LICENSE.md    
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
#### Siding NGSI-v2 key-values Example    
Here is an example of a Siding in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": "2013-05-04T09:51:15Z",  
  "dateModified": "1974-05-09T12:06:14Z",  
  "source": "Push list then again. State get suddenly nor table.",  
  "name": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s",  
  "alternateName": "Name down over test feeling Congress. Recent his his back partner reduce material your.",  
  "description": "Anything so doctor finally. Despite practice class store.",  
  "dataProvider": "Us which she quickly else party. Way that give main air short near. Real popular whatever s",  
  "owner": [  
    "urn:ngsi-ld:Siding:items:SXEI:27228317",  
    "urn:ngsi-ld:Siding:items:EIZG:41039273"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Siding:items:DOKD:91972812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.875369,  
      98.837859  
    ]  
  },  
  "address": {  
    "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
    "addressLocality": "Since ",  
    "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
    "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
    "postalCode": "Personal build",  
    "postOfficeBoxNumber": "Leader enough weight everything.",  
    "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
    "district": "Area cost hundred same. Sense anyone anyone."  
  },  
  "areaServed": "Moment agent four language. Tend place r",  
  "type": "Siding",  
  "demonstrationINF": "Its federal stand tr",  
  "gradient": 354.9,  
  "hasElectricShoreSupply": true,  
  "hasExternalCleaning": true,  
  "hasRefuelling": true,  
  "hasSandRestocking": false,  
  "hasToiletDischarge": false,  
  "hasWaterRestocking": false,  
  "maxCurrentStandstillPantograph": 81.3,  
  "minimumHorizontalRadius": 864,  
  "minimumVerticalRadius": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "minimumVerticalRadiusCrest": 864,  
  "minimumVerticalRadiusHollow": 864,  
  "sidingId": "American whole magazine",  
  "verificationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "tenClassification": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097"  
}  
```  
</details>  
#### Siding NGSI-v2 normalized Example    
Here is an example of a Siding in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2013-05-04T09:51:15Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1974-05-09T12:06:14Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Push list then again. State get suddenly nor table."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Name down over test feeling Congress. Recent his his back partner reduce material your."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Anything so doctor finally. Despite practice class store."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Us which she quickly else party. Way that give main air short near. Real popular whatever s"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Siding:items:SXEI:27228317",  
      "urn:ngsi-ld:Siding:items:EIZG:41039273"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Siding:items:DOKD:91972812"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -36.875369,  
          98.837859  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Since "  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Radio across best yard. Central until beyond knowledge care matter. Without air d"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Argue data get fire. Water opportunity citizen. Score interview letter evidence."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Personal build"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Leader enough weight everything."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Area cost hundred same. Sense anyone anyone."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Moment agent four language. Tend place r"  
  },  
  "type": "Siding",  
  "demonstrationINF": {  
    "type": "Text",  
    "value": "Its federal stand tr"  
  },  
  "gradient": {  
    "type": "Number",  
    "value": 354.9  
  },  
  "hasElectricShoreSupply": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasExternalCleaning": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasRefuelling": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasSandRestocking": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasToiletDischarge": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasWaterRestocking": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Number",  
    "value": 81.3  
  },  
  "minimumHorizontalRadius": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumVerticalRadius": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "minimumVerticalRadiusCrest": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumVerticalRadiusHollow": {  
    "type": "Number",  
    "value": 864  
  },  
  "sidingId": {  
    "type": "Text",  
    "value": "American whole magazine"  
  },  
  "verificationINF": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "tenClassification": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097"  
  }  
}  
```  
</details>  
#### Siding NGSI-LD key-values Example    
Here is an example of a Siding in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:GKYX:31219414",  
  "dateCreated": "2013-05-04T09:51:15Z",  
  "dateModified": "1974-05-09T12:06:14Z",  
  "source": "Push list then again. State get suddenly nor table.",  
  "name": "Federal policy check them. Senior of management simply lose program voice guy. Information direction big expert street big s",  
  "alternateName": "Name down over test feeling Congress. Recent his his back partner reduce material your.",  
  "description": "Anything so doctor finally. Despite practice class store.",  
  "dataProvider": "Us which she quickly else party. Way that give main air short near. Real popular whatever s",  
  "owner": [  
    "urn:ngsi-ld:Siding:items:SXEI:27228317",  
    "urn:ngsi-ld:Siding:items:EIZG:41039273"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Siding:items:DOKD:91972812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -36.875369,  
      98.837859  
    ]  
  },  
  "address": {  
    "streetAddress": "Consumer employee major free billion instead. Treatment yet keep action work close. Nearly check drive I range magazine appear. Quickly respond property.",  
    "addressLocality": "Since ",  
    "addressRegion": "Radio across best yard. Central until beyond knowledge care matter. Without air d",  
    "addressCountry": "Argue data get fire. Water opportunity citizen. Score interview letter evidence.",  
    "postalCode": "Personal build",  
    "postOfficeBoxNumber": "Leader enough weight everything.",  
    "streetNr": "Drug debate effect sure manage point. Economic but single commercial standard. Indicate environment guess long da",  
    "district": "Area cost hundred same. Sense anyone anyone."  
  },  
  "areaServed": "Moment agent four language. Tend place r",  
  "type": "Siding",  
  "demonstrationINF": "Its federal stand tr",  
  "gradient": 354.9,  
  "hasElectricShoreSupply": true,  
  "hasExternalCleaning": true,  
  "hasRefuelling": true,  
  "hasSandRestocking": false,  
  "hasToiletDischarge": false,  
  "hasWaterRestocking": false,  
  "maxCurrentStandstillPantograph": 81.3,  
  "minimumHorizontalRadius": 864,  
  "minimumVerticalRadius": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "minimumVerticalRadiusCrest": 864,  
  "minimumVerticalRadiusHollow": 864,  
  "sidingId": "American whole magazine",  
  "verificationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "tenClassification": "urn:ngsi-ld:Siding:tenClassification:KHXK:08016097",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Siding NGSI-LD normalized Example    
Here is an example of a Siding in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Siding:id:LIKW:54042696",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1996-09-19T23:08:47Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1994-06-22T11:37:34Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Structure decision camera reach purpose role prepare. Fish nor team avoid party memory most unit."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Great discover down event record milita"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Necessary billion gas Congress need explain safe. Law media people a sister consider."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Hotel country risk. Method bit seat organization partner."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Board movement understand. Each I give soon."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Siding:items:RYOP:03718728",  
      "urn:ngsi-ld:Siding:items:OGDX:73134134"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Siding:items:SIJP:84831513"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        28.4755575,  
        91.269469  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "According laugh government goal teacher social. Only speak effect policy easy learn. Material suddenly appear animal keep.",  
      "addressLocality": "",  
      "addressRegion": "Energy better life herself listen minute attorney. Bank you produce magazine.",  
      "addressCountry": "American sure message",  
      "postalCode": "Everything stand agreement hope forward. End debate deep act.",  
      "postOfficeBoxNumber": "Those public may range public. Hous",  
      "streetNr": "Discussion clear action add key reflect. Skill beautiful leg worker least ",  
      "district": "Discussion early quality that morning eye full. My at"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Report democratic en"  
  },  
  "type": "Siding",  
  "demonstrationINF": {  
    "type": "Property",  
    "value": "Pm can assume agency Mr reach music computer"  
  },  
  "gradient": {  
    "type": "Property",  
    "value": 733.9  
  },  
  "hasElectricShoreSupply": {  
    "type": "Property",  
    "value": true  
  },  
  "hasExternalCleaning": {  
    "type": "Property",  
    "value": true  
  },  
  "hasRefuelling": {  
    "type": "Property",  
    "value": true  
  },  
  "hasSandRestocking": {  
    "type": "Property",  
    "value": true  
  },  
  "hasToiletDischarge": {  
    "type": "Property",  
    "value": false  
  },  
  "hasWaterRestocking": {  
    "type": "Property",  
    "value": false  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Property",  
    "value": 818.3  
  },  
  "minimumHorizontalRadius": {  
    "type": "Property",  
    "value": 975  
  },  
  "minimumVerticalRadius": {  
    "type": "Property",  
    "value": "Police almost show day. Number only form skin t"  
  },  
  "minimumVerticalRadiusCrest": {  
    "type": "Property",  
    "value": 799  
  },  
  "minimumVerticalRadiusHollow": {  
    "type": "Property",  
    "value": 937  
  },  
  "sidingId": {  
    "type": "Property",  
    "value": "Air owner child site team modern behavior figure. Behavior near pick which civil door."  
  },  
  "verificationINF": {  
    "type": "Property",  
    "value": "Establish wh"  
  },  
  "tenClassification": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Siding:tenClassification:IURD:46677461"  
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

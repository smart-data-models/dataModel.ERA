<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: MinAxleLoadVehicleCategory    
==================================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/MinAxleLoadVehicleCategory/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Deprecated according to the ammendment to the Regulation (EU) 2019/777. Represents information that indicates the load given in tons depending of the category of vehicle. Its properties are minAxleLoadVehicleCategory and minAxleLoad.**    
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `minAxleLoad[number]`: Minimum permitted axle load  - `minAxleLoadVehicleCategory[uri]`: Minimum axle load vehicle category  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI data type. It has to be MinAxleLoadVehicleCategory  <!-- /30-PropertiesList -->    
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
## Example payloads      
#### MinAxleLoadVehicleCategory NGSI-v2 key-values Example      
Here is an example of a MinAxleLoadVehicleCategory in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
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
#### MinAxleLoadVehicleCategory NGSI-v2 normalized Example      
Here is an example of a MinAxleLoadVehicleCategory in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
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
#### MinAxleLoadVehicleCategory NGSI-LD key-values Example      
Here is an example of a MinAxleLoadVehicleCategory in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
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
#### MinAxleLoadVehicleCategory NGSI-LD normalized Example      
Here is an example of a MinAxleLoadVehicleCategory in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

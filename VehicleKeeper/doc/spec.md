<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: VehicleKeeper    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/VehicleKeeper/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **A company or organization that owns or operates a certain vehicle.**    
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI data type. It has to be VehicleKeeper  <!-- /30-PropertiesList -->    
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
VehicleKeeper:      
  description: A company or organization that owns or operates a certain vehicle.      
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
      description: NGSI data type. It has to be VehicleKeeper      
      enum:      
        - VehicleKeeper      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/VehicleKeeper      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/VehicleKeeper/LICENSE.md      
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
#### VehicleKeeper NGSI-v2 key-values Example      
Here is an example of a VehicleKeeper in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:XXBI:45242122",  
  "dateCreated": "2021-09-14T02:23:10Z",  
  "dateModified": "1997-03-24T06:16:52Z",  
  "source": "K",  
  "name": "Quite receive message front include indeed with. Sign coach actu",  
  "alternateName": "Measure how American red. Child few inside save. Wonder total moment safe democratic wonder.",  
  "description": "Produce car space whose. Travel candidate compare forget still.",  
  "dataProvider": "Card rise their doctor together enjoy cle",  
  "owner": [  
    "urn:ngsi-ld:VehicleKeeper:items:ETMT:35445191",  
    "urn:ngsi-ld:VehicleKeeper:items:ZVVO:84115238"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:VehicleKeeper:items:HCCU:66226906"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.213131,  
      -151.498321  
    ]  
  },  
  "address": {  
    "streetAddress": "Company recently close affect. Others Congress ",  
    "addressLocality": "Region purpose probably expert road give. Occur and according some. Event outside usually newspaper.",  
    "addressRegion": "Remember discuss Democrat party. Since claim appear stuff pull alo",  
    "addressCountry": "Nature find",  
    "postalCode": "Point begin economy minute. Necessary candidate woman church which beautiful.",  
    "postOfficeBoxNumber": "Affect top receive to security remember area street. Only operation important modern thing join.",  
    "streetNr": "Significant defense agent now ",  
    "district": "Pass heart with several esta"  
  },  
  "areaServed": "So memory ve",  
  "type": "VehicleKeeper"  
}  
```  
</details>    
#### VehicleKeeper NGSI-v2 normalized Example      
Here is an example of a VehicleKeeper in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:XXBI:45242122",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2021-09-14T02:23:10Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1997-03-24T06:16:52Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "K"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Quite receive message front include indeed with. Sign coach actu"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Measure how American red. Child few inside save. Wonder total moment safe democratic wonder."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Produce car space whose. Travel candidate compare forget still."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Card rise their doctor together enjoy cle"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:ETMT:35445191",  
      "urn:ngsi-ld:VehicleKeeper:items:ZVVO:84115238"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:HCCU:66226906"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        48.213131,  
        -151.498321  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Company recently close affect. Others Congress ",  
      "addressLocality": "Region purpose probably expert road give. Occur and according some. Event outside usually newspaper.",  
      "addressRegion": "Remember discuss Democrat party. Since claim appear stuff pull alo",  
      "addressCountry": "Nature find",  
      "postalCode": "Point begin economy minute. Necessary candidate woman church which beautiful.",  
      "postOfficeBoxNumber": "Affect top receive to security remember area street. Only operation important modern thing join.",  
      "streetNr": "Significant defense agent now ",  
      "district": "Pass heart with several esta"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "So memory ve"  
  },  
  "type": "VehicleKeeper"  
}  
```  
</details>    
#### VehicleKeeper NGSI-LD key-values Example      
Here is an example of a VehicleKeeper in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:XXBI:45242122",  
  "dateCreated": "2021-09-14T02:23:10Z",  
  "dateModified": "1997-03-24T06:16:52Z",  
  "source": "K",  
  "name": "Quite receive message front include indeed with. Sign coach actu",  
  "alternateName": "Measure how American red. Child few inside save. Wonder total moment safe democratic wonder.",  
  "description": "Produce car space whose. Travel candidate compare forget still.",  
  "dataProvider": "Card rise their doctor together enjoy cle",  
  "owner": [  
    "urn:ngsi-ld:VehicleKeeper:items:ETMT:35445191",  
    "urn:ngsi-ld:VehicleKeeper:items:ZVVO:84115238"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:VehicleKeeper:items:HCCU:66226906"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      48.213131,  
      -151.498321  
    ]  
  },  
  "address": {  
    "streetAddress": "Company recently close affect. Others Congress ",  
    "addressLocality": "Region purpose probably expert road give. Occur and according some. Event outside usually newspaper.",  
    "addressRegion": "Remember discuss Democrat party. Since claim appear stuff pull alo",  
    "addressCountry": "Nature find",  
    "postalCode": "Point begin economy minute. Necessary candidate woman church which beautiful.",  
    "postOfficeBoxNumber": "Affect top receive to security remember area street. Only operation important modern thing join.",  
    "streetNr": "Significant defense agent now ",  
    "district": "Pass heart with several esta"  
  },  
  "areaServed": "So memory ve",  
  "type": "VehicleKeeper",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### VehicleKeeper NGSI-LD normalized Example      
Here is an example of a VehicleKeeper in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:VehicleKeeper:id:OQLK:27164371",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-12-25T16:50:11Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1994-07-16T07:43:37Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Shake ago quality hard suddenly. Campaign data itself them industry."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Less walk way success. Kitchen realize edge level action. Reduc"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Wall cold determine who. Water whether under else blue get."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Color opportunity player prevent ago tonight pretty. Themselves nation d"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Space customer statement issue daughter than already."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:VRJH:99019247",  
      "urn:ngsi-ld:VehicleKeeper:items:JMRS:40266513"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:VehicleKeeper:items:RXUF:20636106"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -68.0082615,  
        43.406974  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Resource scientist company not choice. Move with professor discussion. Stuff less activity either arrive gun American ",  
      "addressLocality": "Inside third practice occur",  
      "addressRegion": "Notice",  
      "addressCountry": "How choice lay. With always game opportunity early. Practice list local particular paper though. Trouble professional Democrat ahead.",  
      "postalCode": "Capital give subject pull. School authority follow set something create.",  
      "postOfficeBoxNumber": "While once summer executive. Wife idea ",  
      "streetNr": "Store hard add. Food down about significa",  
      "district": "Hear real we information."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Air beat year help wrong production and upon. Full long suddenly prevent policy c"  
  },  
  "type": "VehicleKeeper",  
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

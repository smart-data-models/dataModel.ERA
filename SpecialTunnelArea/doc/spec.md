<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

Entity: SpecialTunnelArea    
=========================
<!-- /10-Header -->
    
<!-- 15-License -->
    

[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/SpecialTunnelArea/LICENSE.md)    

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

Global description: **Area or location within a tunnel where  there is a walkway, evacuation and rescue points.**    

version: 0.0.1    
<!-- /20-Description -->
    
<!-- 30-PropertiesList -->
    

## List of properties    

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Number identifying a specific property on a public street      
- `alternateName[string]`: An alternative name for this item  
- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  
- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  
- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  
- `description[string]`: A description of this item  
- `id[*]`: Unique identifier of the entity  
- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name[string]`: The name of this item  
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso[*]`: list of uri pointing to additional resources about the item  
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  
- `type[string]`: NGSI data type. It has to be SpecialTunnelArea  
<!-- /30-PropertiesList -->
    
<!-- 35-RequiredProperties -->
    

Required properties    
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
    
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
SpecialTunnelArea:      
  description: 'Area or location within a tunnel where  there is a walkway, evacuation and rescue points.'      
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
      description: NGSI data type. It has to be SpecialTunnelArea      
      enum:      
        - SpecialTunnelArea      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/SpecialTunnelArea      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SpecialTunnelArea/LICENSE.md      
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

#### SpecialTunnelArea NGSI-v2 key-values Example      

Here is an example of a SpecialTunnelArea in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": "1988-01-11T13:27:45Z",  
  "dateModified": "2010-12-08T20:17:03Z",  
  "source": "Owner kid middle worry po",  
  "name": "Idea able accept. Always four majority education wait. South east t",  
  "alternateName": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two.",  
  "description": "Center these own security subject ability once. Catch animal office poor.",  
  "dataProvider": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve.",  
  "owner": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
    "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.1411545,  
      -167.120745  
    ]  
  },  
  "address": {  
    "streetAddress": "Build next e",  
    "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
    "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
    "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
    "postalCode": "Environmental bag officer do ball. Soc",  
    "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
    "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
    "district": "Pattern over scientist important"  
  },  
  "areaServed": "Current upon put current. His find imagine high course why sea.",  
  "type": "SpecialTunnelArea"
}  
```  
</details>    

#### SpecialTunnelArea NGSI-v2 normalized Example      

Here is an example of a SpecialTunnelArea in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1988-01-11T13:27:45Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2010-12-08T20:17:03Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Owner kid middle worry po"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Idea able accept. Always four majority education wait. South east t"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Center these own security subject ability once. Catch animal office poor."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
      "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.1411545,  
        -167.120745  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Build next e",  
      "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
      "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
      "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
      "postalCode": "Environmental bag officer do ball. Soc",  
      "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
      "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
      "district": "Pattern over scientist important"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Current upon put current. His find imagine high course why sea."  
  },  
  "type": "SpecialTunnelArea"  
}  
```  
</details>    

#### SpecialTunnelArea NGSI-LD key-values Example      

Here is an example of a SpecialTunnelArea in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:LFLJ:85738742",  
  "dateCreated": "1988-01-11T13:27:45Z",  
  "dateModified": "2010-12-08T20:17:03Z",  
  "source": "Owner kid middle worry po",  
  "name": "Idea able accept. Always four majority education wait. South east t",  
  "alternateName": "Program teacher speech police mission word. System according within wall use side performance off. Travel oil organization traditional two.",  
  "description": "Center these own security subject ability once. Catch animal office poor.",  
  "dataProvider": "Middle to quickly industry cell. Skin many research system service. View population inside help wall list serve.",  
  "owner": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:WFVO:31498652",  
    "urn:ngsi-ld:SpecialTunnelArea:items:ZFBW:53633422"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialTunnelArea:items:GMKJ:39779882"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.1411545,  
      -167.120745  
    ]  
  },  
  "address": {  
    "streetAddress": "Build next e",  
    "addressLocality": "Special campaign he two final actually before treat. Continue miss be young ",  
    "addressRegion": "Upon writer local bring last agent seem. Wind participant seem ask try various image.",  
    "addressCountry": "Trouble phone be. Health last brother attack defense power identify.",  
    "postalCode": "Environmental bag officer do ball. Soc",  
    "postOfficeBoxNumber": "Arrive question describe throughout official contain which. Wife as te",  
    "streetNr": "Focus still amount him individual number ground. Piece chair opportunity most become.",  
    "district": "Pattern over scientist important"  
  },  
  "areaServed": "Current upon put current. His find imagine high course why sea.",  
  "type": "SpecialTunnelArea",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### SpecialTunnelArea NGSI-LD normalized Example      

Here is an example of a SpecialTunnelArea in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:SpecialTunnelArea:id:INWI:10579735",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1992-01-22T20:24:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1980-02-15T17:27:55Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Three consumer rise certain and. Share operation "  
  },  
  "name": {  
    "type": "Property",  
    "value": "Should program heart effort often not. Black though believe theory choice travel level. Positive big right beat television respond run."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Commercial share budget. Mention industry build."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Friend save analysis event. Summer hospital box site hold matter agency. Measure gun"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Arrive read pattern be despite second matter. Thank teach oil his."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:TUJB:41707682",  
      "urn:ngsi-ld:SpecialTunnelArea:items:UXYT:76593602"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialTunnelArea:items:JGSZ:99017778"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        57.77738,  
        -119.777978  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "On boy cell night. Sit stage difficult take onto best.",  
      "addressLocality": "East south bill former business federal argue. These machine their war. Vote because born natural",  
      "addressRegion": "Eye occur contain rest. Determine child interest action boy begin more.",  
      "addressCountry": "On home time left. Rather necessary talk same almost. Card computer see security.",  
      "postalCode": "State positive assume themselves media. Tax food while. Write eye st",  
      "postOfficeBoxNumber": "Role call wrong arrive marriage meet authority foreign. Show paper difficult really increase. Difference company free medical rich.",  
      "streetNr": "Use but left assume. Safe be during soldier. Natural success before begin part.",  
      "district": "White hand we return less. Product movie season man."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Those production act story gun necessary such. Almost space without. Herself pressure miss anyone contain car."  
  },  
  "type": "SpecialTunnelArea",  
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
    

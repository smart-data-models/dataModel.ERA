<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: MaximumMagneticField    
============================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/MaximumMagneticField/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **The maximum magnetic field limits allowed for axle counters (in dBµA/m) for a defined frequency band.    
It should be provided in 3 directions.**    
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maximumMagneticFieldDirectionX[number]`: Maximum magnetic field direction X  - `maximumMagneticFieldDirectionY[number]`: Maximum magnetic field direction Y  - `maximumMagneticFieldDirectionZ[number]`: Maximum magnetic field direction Z  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI data type. It has to be MaximumMagneticField  <!-- /30-PropertiesList -->    
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
MaximumMagneticField:      
  description: |-      
    The maximum magnetic field limits allowed for axle counters (in dBµA/m) for a defined frequency band.      
    It should be provided in 3 directions.      
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
    maximumMagneticFieldDirectionX:      
      description: Maximum magnetic field direction X      
      type: number      
      x-ngsi:      
        type: Property      
    maximumMagneticFieldDirectionY:      
      description: Maximum magnetic field direction Y      
      type: number      
      x-ngsi:      
        type: Property      
    maximumMagneticFieldDirectionZ:      
      description: Maximum magnetic field direction Z      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be MaximumMagneticField      
      enum:      
        - MaximumMagneticField      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/MaximumMagneticField      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/MaximumMagneticField/LICENSE.md      
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
#### MaximumMagneticField NGSI-v2 key-values Example      
Here is an example of a MaximumMagneticField in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": "1992-07-01T01:29:02Z",  
  "dateModified": "2022-07-21T07:13:50Z",  
  "source": "Method modern phone whatever thing. Discussion example your dog fund serv",  
  "name": "Nothing church tonight church do",  
  "alternateName": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve.",  
  "description": "Difficu",  
  "dataProvider": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r",  
  "owner": [  
    "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
    "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      12.1959295,  
      -80.960856  
    ]  
  },  
  "address": {  
    "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
    "addressLocality": "Region may realize sign my. Wester",  
    "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
    "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
    "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
    "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
    "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
    "district": "Allow site finally evidence green."  
  },  
  "areaServed": "Employee they catch fight suggest. Executive positive eight piece.",  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": 864,  
  "maximumMagneticFieldDirectionY": 864,  
  "maximumMagneticFieldDirectionZ": 864,  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### MaximumMagneticField NGSI-v2 normalized Example      
Here is an example of a MaximumMagneticField in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1992-07-01T01:29:02Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2022-07-21T07:13:50Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Method modern phone whatever thing. Discussion example your dog fund serv"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Nothing church tonight church do"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Difficu"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
      "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        12.1959295,  
        -80.960856  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
      "addressLocality": "Region may realize sign my. Wester",  
      "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
      "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
      "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
      "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
      "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
      "district": "Allow site finally evidence green."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Employee they catch fight suggest. Executive positive eight piece."  
  },  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumMagneticFieldDirectionY": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumMagneticFieldDirectionZ": {  
    "type": "Number",  
    "value": 864  
  },  
  "context": {  
    "type": "StructuredValue",  
    "value": [  
      "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
    ]  
  }  
}  
```  
</details>    
#### MaximumMagneticField NGSI-LD key-values Example      
Here is an example of a MaximumMagneticField in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:RBVW:96380852",  
  "dateCreated": "1992-07-01T01:29:02Z",  
  "dateModified": "2022-07-21T07:13:50Z",  
  "source": "Method modern phone whatever thing. Discussion example your dog fund serv",  
  "name": "Nothing church tonight church do",  
  "alternateName": "Near second chance respond energy. Within try notice oil. Almost either worker school game list improve.",  
  "description": "Difficu",  
  "dataProvider": "Protect relationship almost movie hand when. End foot woman military appear manage meet long. Threat r",  
  "owner": [  
    "urn:ngsi-ld:MaximumMagneticField:items:VXOI:93063711",  
    "urn:ngsi-ld:MaximumMagneticField:items:YGLS:61846331"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumMagneticField:items:LSEW:60720157"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      12.1959295,  
      -80.960856  
    ]  
  },  
  "address": {  
    "streetAddress": "Number nature rock important pull. Much concern up certainly p",  
    "addressLocality": "Region may realize sign my. Wester",  
    "addressRegion": "Project resource recent require bank sell. Similar finish audience end.",  
    "addressCountry": "Experience institution case officer. Window section area information. College or sport charge remember thing give.",  
    "postalCode": "Season check including hard light skill. Firm town nice. Letter",  
    "postOfficeBoxNumber": "Fire gun push somebody concern pretty away what. Bit hotel say discuss. Small similar common whether painting stock.",  
    "streetNr": "Series baby such probably cell court. Pretty value still sit chance party. Dra",  
    "district": "Allow site finally evidence green."  
  },  
  "areaServed": "Employee they catch fight suggest. Executive positive eight piece.",  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": 864,  
  "maximumMagneticFieldDirectionY": 864,  
  "maximumMagneticFieldDirectionZ": 864,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### MaximumMagneticField NGSI-LD normalized Example      
Here is an example of a MaximumMagneticField in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MaximumMagneticField:id:XYSL:59916457",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2011-01-17T00:20:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1971-04-03T19:24:25Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Seek material four bed eat foot four cut. Industry medical human yet collection."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Everyone safe interesting eat. Again might live manager. Surf"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Here people p"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Activity treat its in. Also step board might truth small interesting."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Article care radio win program responsibility water. South expect yard past most team. Raise population since meet between set."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:QGWL:53478074",  
      "urn:ngsi-ld:MaximumMagneticField:items:IBUO:48085735"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumMagneticField:items:XXHU:41714471"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.077867,  
        60.671442  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "West trial language field. Stock high senior success go whole.",  
      "addressLocality": "Community catch mission perhaps especially option degree. Create option part not return draw identify art. Success relate series according.",  
      "addressRegion": "List successful a during loss nor. Conference hit well far f",  
      "addressCountry": "Our seem scientist. Hot group true design season crime. Far safe miss doctor.",  
      "postalCode": "Interesting top success try.",  
      "postOfficeBoxNumber": "Huge foot truth ball. ",  
      "streetNr": "Land need cold question.",  
      "district": "Throughout way floor believe movie. Off police in begin. Whatever heart half or already window."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Say already life discuss determine heart. Edge someone parent all her down."  
  },  
  "type": "MaximumMagneticField",  
  "maximumMagneticFieldDirectionX": {  
    "type": "Property",  
    "value": 671  
  },  
  "maximumMagneticFieldDirectionY": {  
    "type": "Property",  
    "value": 707  
  },  
  "maximumMagneticFieldDirectionZ": {  
    "type": "Property",  
    "value": 262  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
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

<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Certificate  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/Certificate/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `state[uri]`: State  - `type[string]`: NGSI data type. It has to be Certificate  <!-- /30-PropertiesList -->  
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
Certificate:    
  description: ""    
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
    state:    
      description: State    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI data type. It has to be Certificate    
      enum:    
        - Certificate    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Certificate    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Certificate/LICENSE.md    
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
#### Certificate NGSI-v2 key-values Example    
Here is an example of a Certificate in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:OEMR:38840161",  
  "dateCreated": "2000-01-17T20:24:29Z",  
  "dateModified": "2014-02-03T22:13:34Z",  
  "source": "Strategy there certainly federal. Risk manager carry shoulder only long.",  
  "name": "Across him eight property help. Beat federal dream conference score special deal accept.",  
  "alternateName": "Heart beat fine nice identify. Wide usually me in painting tough entire.",  
  "description": "Section employee few. Decision prevent easy.",  
  "dataProvider": "Talk necessary run score recent. Expert seem money concern shoulder goal. Recognize camera state want across mind his.",  
  "owner": [  
    "urn:ngsi-ld:Certificate:items:ZTPB:96026524",  
    "urn:ngsi-ld:Certificate:items:MZYH:89260401"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Certificate:items:LMJQ:88266844"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -52.637063,  
      23.558812  
    ]  
  },  
  "address": {  
    "streetAddress": "Modern society station campaign. Important through to discover guess. Someone consider entire li",  
    "addressLocality": "Firm art goal mind as include. Visit memory leg care probably because commercial how.",  
    "addressRegion": "Success right poor each near foot. At without shake main current strategy. Stand along stuff keep coach tow",  
    "addressCountry": "Wrong fall write onto forget. Air hard quality. Rise try blue either s",  
    "postalCode": "Point structure evening policy here. Use talk pressure democratic want.",  
    "postOfficeBoxNumber": "Cell board else course always recent. Property almost serve before.",  
    "streetNr": "Special shake soldier bed include. Thus doctor political blue even girl.",  
    "district": "Accept west participant suggest whatever feel later. Rule deep owner."  
  },  
  "areaServed": "Allow whole live analysis defense million strategy real. Bed chance different attention community protect. Government thus build ",  
  "type": "Certificate",  
  "state": "urn:ngsi-ld:Certificate:state:KHMM:25466110"  
}  
```  
</details>  
#### Certificate NGSI-v2 normalized Example    
Here is an example of a Certificate in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:OEMR:38840161",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2000-01-17T20:24:29Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2014-02-03T22:13:34Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Strategy there certainly federal. Risk manager carry shoulder only long."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Across him eight property help. Beat federal dream conference score special deal accept."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Heart beat fine nice identify. Wide usually me in painting tough entire."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Section employee few. Decision prevent easy."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Talk necessary run score recent. Expert seem money concern shoulder goal. Recognize camera state want across mind his."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:ZTPB:96026524",  
      "urn:ngsi-ld:Certificate:items:MZYH:89260401"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:LMJQ:88266844"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -52.637063,  
          23.558812  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Modern society station campaign. Important through to discover guess. Someone consider entire li"  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Firm art goal mind as include. Visit memory leg care probably because commercial how."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Success right poor each near foot. At without shake main current strategy. Stand along stuff keep coach tow"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Wrong fall write onto forget. Air hard quality. Rise try blue either s"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Point structure evening policy here. Use talk pressure democratic want."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Cell board else course always recent. Property almost serve before."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Special shake soldier bed include. Thus doctor political blue even girl."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Accept west participant suggest whatever feel later. Rule deep owner."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Allow whole live analysis defense million strategy real. Bed chance different attention community protect. Government thus build "  
  },  
  "type": "Certificate",  
  "state": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Certificate:state:KHMM:25466110"  
  }  
}  
```  
</details>  
#### Certificate NGSI-LD key-values Example    
Here is an example of a Certificate in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:OEMR:38840161",  
  "dateCreated": "2000-01-17T20:24:29Z",  
  "dateModified": "2014-02-03T22:13:34Z",  
  "source": "Strategy there certainly federal. Risk manager carry shoulder only long.",  
  "name": "Across him eight property help. Beat federal dream conference score special deal accept.",  
  "alternateName": "Heart beat fine nice identify. Wide usually me in painting tough entire.",  
  "description": "Section employee few. Decision prevent easy.",  
  "dataProvider": "Talk necessary run score recent. Expert seem money concern shoulder goal. Recognize camera state want across mind his.",  
  "owner": [  
    "urn:ngsi-ld:Certificate:items:ZTPB:96026524",  
    "urn:ngsi-ld:Certificate:items:MZYH:89260401"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Certificate:items:LMJQ:88266844"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -52.637063,  
      23.558812  
    ]  
  },  
  "address": {  
    "streetAddress": "Modern society station campaign. Important through to discover guess. Someone consider entire li",  
    "addressLocality": "Firm art goal mind as include. Visit memory leg care probably because commercial how.",  
    "addressRegion": "Success right poor each near foot. At without shake main current strategy. Stand along stuff keep coach tow",  
    "addressCountry": "Wrong fall write onto forget. Air hard quality. Rise try blue either s",  
    "postalCode": "Point structure evening policy here. Use talk pressure democratic want.",  
    "postOfficeBoxNumber": "Cell board else course always recent. Property almost serve before.",  
    "streetNr": "Special shake soldier bed include. Thus doctor political blue even girl.",  
    "district": "Accept west participant suggest whatever feel later. Rule deep owner."  
  },  
  "areaServed": "Allow whole live analysis defense million strategy real. Bed chance different attention community protect. Government thus build ",  
  "type": "Certificate",  
  "state": "urn:ngsi-ld:Certificate:state:KHMM:25466110",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### Certificate NGSI-LD normalized Example    
Here is an example of a Certificate in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Certificate:id:FQIG:83987629",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2001-08-13T18:45:46Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1990-10-25T01:23:48Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Teach interview sens"  
  },  
  "name": {  
    "type": "Property",  
    "value": "My away establish push woman none. She once man knowledge question enjoy suddenly. Left lay treatment local agent. Record former deal h"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Treat decide hospital doo"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Site before adult Democrat computer. Mrs at hair small trial arrive picture."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Individual "  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:XJAQ:41164811",  
      "urn:ngsi-ld:Certificate:items:ALDM:78818333"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Certificate:items:TYPY:58686784"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -19.9646155,  
        -63.326103  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Measure defense government. Move",  
      "addressLocality": "Chair fund always official production.",  
      "addressRegion": "Lawyer yeah skill without interview teach address. Quality magazine stand make. Community tough field despite during.",  
      "addressCountry": "Beyond discuss health continue.",  
      "postalCode": "Size song pattern capital plan. Part own break most none.",  
      "postOfficeBoxNumber": "Find degree what fall news. Husband new agreement str",  
      "streetNr": "White share make game perhaps also ago. Teach discussion teach talk.",  
      "district": "Team perform people rise. Attack far add. East card traditional mouth range."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Fill part form so necessary back. Accept color community "  
  },  
  "type": "Certificate",  
  "state": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Certificate:state:HXAA:38754798"  
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

<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: PhaseInfo    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/PhaseInfo/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Indication of required several information on phase separation.**    
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `phaseInfoKm[number]`: Phase info Km  - `phaseInfoLength[number]`: Phase info length  - `phaseInfoPantographLowered[boolean]`: Phase info pantograph lowered  - `phaseInfoSwitchOffBreaker[boolean]`: Phase info switch off breaker  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `systemSeparationInfoKm[number]`: System separation info Km  - `type[string]`: NGSI data type. It has to be PhaseInfo  <!-- /30-PropertiesList -->    
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
PhaseInfo:      
  description: Indication of required several information on phase separation.      
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
    phaseInfoKm:      
      description: Phase info Km      
      type: number      
      x-ngsi:      
        type: Property      
    phaseInfoLength:      
      description: Phase info length      
      type: number      
      x-ngsi:      
        type: Property      
    phaseInfoPantographLowered:      
      description: Phase info pantograph lowered      
      type: boolean      
      x-ngsi:      
        type: Property      
    phaseInfoSwitchOffBreaker:      
      description: Phase info switch off breaker      
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
    systemSeparationInfoKm:      
      description: System separation info Km      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be PhaseInfo      
      enum:      
        - PhaseInfo      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/PhaseInfo      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/PhaseInfo/LICENSE.md      
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
#### PhaseInfo NGSI-v2 key-values Example      
Here is an example of a PhaseInfo in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": "2004-07-16T13:48:20Z",  
  "dateModified": "1991-11-29T03:06:21Z",  
  "source": "Enjoy will style car seem recent. Plan theory u",  
  "name": "Rate office focus whole on produce. Argue Mrs care accept momen",  
  "alternateName": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman.",  
  "description": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense.",  
  "dataProvider": "All owner type finish more race adult.",  
  "owner": [  
    "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
    "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      79.5846865,  
      60.386195  
    ]  
  },  
  "address": {  
    "streetAddress": "Toward idea thought. Among drop position election wear.",  
    "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
    "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
    "addressCountry": "Analysis argue so performance itself really for.",  
    "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
    "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
    "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
    "district": "Return anything ma"  
  },  
  "areaServed": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress.",  
  "type": "PhaseInfo",  
  "phaseInfoKm": 37.5,  
  "phaseInfoLength": 864,  
  "phaseInfoPantographLowered": false,  
  "phaseInfoSwitchOffBreaker": false,  
  "systemSeparationInfoKm": 99.4  
}  
```  
</details>    
#### PhaseInfo NGSI-v2 normalized Example      
Here is an example of a PhaseInfo in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2004-07-16T13:48:20Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1991-11-29T03:06:21Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Enjoy will style car seem recent. Plan theory u"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Rate office focus whole on produce. Argue Mrs care accept momen"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "All owner type finish more race adult."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
      "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        79.5846865,  
        60.386195  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Toward idea thought. Among drop position election wear.",  
      "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
      "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
      "addressCountry": "Analysis argue so performance itself really for.",  
      "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
      "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
      "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
      "district": "Return anything ma"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress."  
  },  
  "type": "PhaseInfo",  
  "phaseInfoKm": {  
    "type": "Number",  
    "value": 37.5  
  },  
  "phaseInfoLength": {  
    "type": "Number",  
    "value": 864  
  },  
  "phaseInfoPantographLowered": {  
    "type": "Boolean",  
    "value": false  
  },  
  "phaseInfoSwitchOffBreaker": {  
    "type": "Boolean",  
    "value": false  
  },  
  "systemSeparationInfoKm": {  
    "type": "Number",  
    "value": 99.4  
  }  
}  
```  
</details>    
#### PhaseInfo NGSI-LD key-values Example      
Here is an example of a PhaseInfo in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:XMGY:78379942",  
  "dateCreated": "2004-07-16T13:48:20Z",  
  "dateModified": "1991-11-29T03:06:21Z",  
  "source": "Enjoy will style car seem recent. Plan theory u",  
  "name": "Rate office focus whole on produce. Argue Mrs care accept momen",  
  "alternateName": "Cost picture despite man natural. Value animal ahead picture prevent time product. Into real pull woman.",  
  "description": "Face same answer media. Phone trouble push ready. Pressure sister might let military. May way describe sense.",  
  "dataProvider": "All owner type finish more race adult.",  
  "owner": [  
    "urn:ngsi-ld:PhaseInfo:items:SBSW:39844667",  
    "urn:ngsi-ld:PhaseInfo:items:HYML:41787352"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:PhaseInfo:items:VWBK:17967020"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      79.5846865,  
      60.386195  
    ]  
  },  
  "address": {  
    "streetAddress": "Toward idea thought. Among drop position election wear.",  
    "addressLocality": "Thousand lay myself necessary good them movement. More hour type view. Various still c",  
    "addressRegion": "Year must writer thousand stuff language. Bill plant r",  
    "addressCountry": "Analysis argue so performance itself really for.",  
    "postalCode": "Around executive beyond myself school same turn. Against ten usually that activity claim take operation.",  
    "postOfficeBoxNumber": "Bill they yet month wind benefit. Training itself property college large hundred night.",  
    "streetNr": "Black discover economic dark simply. They their rich trip citizen.",  
    "district": "Return anything ma"  
  },  
  "areaServed": "Well both election camera. Word maintain character it most society situation. Heavy remember some let every. Big prepare commercial Congress.",  
  "type": "PhaseInfo",  
  "phaseInfoKm": 37.5,  
  "phaseInfoLength": 864,  
  "phaseInfoPantographLowered": false,  
  "phaseInfoSwitchOffBreaker": false,  
  "systemSeparationInfoKm": 99.4,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### PhaseInfo NGSI-LD normalized Example      
Here is an example of a PhaseInfo in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PhaseInfo:id:MKUJ:15010698",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1980-01-19T22:02:09Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2008-03-14T12:40:50Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Across air language thoug"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Capital wife fast make similar memory first. Face best choose"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Forward arm back. Sell draw treat water mind series. Movement level ago real study."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Book maybe social but reflect traditional standard"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Office late American morning west economic he. Wide wide rule. Arrive four with measure edge policy."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:ZJGM:93382933",  
      "urn:ngsi-ld:PhaseInfo:items:VXVX:69604579"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:PhaseInfo:items:MJIU:47652604"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -83.0057365,  
        76.5777  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Own organization seat everyone. Animal offer indeed send environmental outside.",  
      "addressLocality": "Drop hear pull on remember drop top. Experience once heart word nearly. Every a significant size.",  
      "addressRegion": "Watch cold letter student information. Professor knowledge four meeting customer. Stock point on student tend. Born glass effort someone.",  
      "addressCountry": "Congress dog probably buy time. Product style sport amount clearly than.",  
      "postalCode": "Dr",  
      "postOfficeBoxNumber": "Good agency tend happen dark option. Individual different former then ago month environment single.",  
      "streetNr": "Arrive including smile concern head effort economic. Top pick appear treat. Hour th",  
      "district": "Message movie former mean rather. Health serious base boy action picture. Rate high pay get risk security someone image."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Agency great travel kitchen. Travel certain improve official meet answer concern. Remember specific red."  
  },  
  "type": "PhaseInfo",  
  "phaseInfoKm": {  
    "type": "Property",  
    "value": 187.2  
  },  
  "phaseInfoLength": {  
    "type": "Property",  
    "value": 335  
  },  
  "phaseInfoPantographLowered": {  
    "type": "Property",  
    "value": true  
  },  
  "phaseInfoSwitchOffBreaker": {  
    "type": "Property",  
    "value": true  
  },  
  "systemSeparationInfoKm": {  
    "type": "Property",  
    "value": 198.4  
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

<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: Signal    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.ERA/blob/master/Signal/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **A railway signal is an installation next to the railway track for signalling the maximum allowed speed in the next block section to the train driver.    
Definition RSM: Apparatus by means of which a conventional visual or acoustic indication is given, generally concerning the movements of railway vehicles.**    
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `relativeDistanceDangerPoint[number]`: Relative distance of the danger point  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `signalId[string]`: Name of signal  - `signalOrientation[uri]`: Signal orientation  - `signalType[uri]`: Type of signal  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `track[uri]`: Track  - `type[string]`: NGSI data type. It has to be Signal  <!-- /30-PropertiesList -->    
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
Signal:      
  description: |-      
    A railway signal is an installation next to the railway track for signalling the maximum allowed speed in the next block section to the train driver.      
    Definition RSM: Apparatus by means of which a conventional visual or acoustic indication is given, generally concerning the movements of railway vehicles.      
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
    relativeDistanceDangerPoint:      
      description: Relative distance of the danger point      
      type: number      
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
    signalId:      
      description: Name of signal      
      type: string      
      x-ngsi:      
        type: Property      
    signalOrientation:      
      description: Signal orientation      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    signalType:      
      description: Type of signal      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    track:      
      description: Track      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    type:      
      description: NGSI data type. It has to be Signal      
      enum:      
        - Signal      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/Signal      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Signal/LICENSE.md      
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
#### Signal NGSI-v2 key-values Example      
Here is an example of a Signal in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
}  
```  
</details>    
#### Signal NGSI-v2 normalized Example      
Here is an example of a Signal in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1970-03-08T14:32:13Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2011-08-18T23:12:35Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Here choose style decade occur leader"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Drop"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Truth add because former. Indeed long yeah change near experience."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:OCNG:88914328",  
      "urn:ngsi-ld:Signal:items:QDWA:77960070"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Signal:items:IKCH:27474652"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.167995,  
        -149.393214  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Upon certainly west population. A walk result product major draw ",  
      "addressLocality": "Account rich measure every price energy allow. Put customer c",  
      "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
      "addressCountry": "Word wai",  
      "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
      "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
      "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
      "district": "Activity"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Number",  
    "value": 864  
  },  
  "signalId": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peac"  
  },  
  "signalOrientation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156"  
  },  
  "signalType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:signalType:CXMW:87784080"  
  },  
  "track": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Signal:track:SHHZ:09753513"  
  }  
}  
```  
</details>    
#### Signal NGSI-LD key-values Example      
Here is an example of a Signal in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:NVJX:48788523",  
  "dateCreated": "1970-03-08T14:32:13Z",  
  "dateModified": "2011-08-18T23:12:35Z",  
  "source": "Here choose style decade occur leader",  
  "name": "Drop",  
  "alternateName": "Truth add because former. Indeed long yeah change near experience.",  
  "description": "Reveal school simply perhaps study owner. Instead card positive between guess other. Will beyond out easy serve.",  
  "dataProvider": "Market represent thing security. Stock whole section will wonder final right minute. Together bill tho",  
  "owner": [  
    "urn:ngsi-ld:Signal:items:OCNG:88914328",  
    "urn:ngsi-ld:Signal:items:QDWA:77960070"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Signal:items:IKCH:27474652"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.167995,  
      -149.393214  
    ]  
  },  
  "address": {  
    "streetAddress": "Upon certainly west population. A walk result product major draw ",  
    "addressLocality": "Account rich measure every price energy allow. Put customer c",  
    "addressRegion": "Prepare family across front. Nothing main religious strategy seven notice where.",  
    "addressCountry": "Word wai",  
    "postalCode": "Meet know training. Land grow old kid effect. Form director decide join draw.",  
    "postOfficeBoxNumber": "Several center notice ever deal his. National parent fund focus pull those door.",  
    "streetNr": "Place course bad watch environment while third. There half join Republican and control perhaps network. Him remain structure.",  
    "district": "Activity"  
  },  
  "areaServed": "Charge suddenly fall resource stock admit leave. Hair such budget many different in cup. Lawyer nati",  
  "type": "Signal",  
  "relativeDistanceDangerPoint": 864,  
  "signalId": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "signalOrientation": "urn:ngsi-ld:Signal:signalOrientation:KTUG:11578156",  
  "signalType": "urn:ngsi-ld:Signal:signalType:CXMW:87784080",  
  "track": "urn:ngsi-ld:Signal:track:SHHZ:09753513",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Signal NGSI-LD normalized Example      
Here is an example of a Signal in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Signal:id:SUMI:05987689",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2013-12-11T15:53:44Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-09-10T20:37:14Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Owner support present act enter."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Start read half."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Home state area operation respond early. Edge return condition federal."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Total again here high. Team report again ask product these cut."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Republican eight think start. Hot movie want serve father audience management."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:MZLV:03669390",  
      "urn:ngsi-ld:Signal:items:LNRS:49951624"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Signal:items:JOYH:86575892"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -13.176379,  
        -116.163154  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Coach my discover both usually east page. Rather lead investment child as record resource. In product rise couple v",  
      "addressLocality": "Conference pull tax indeed. Very trou",  
      "addressRegion": "Man issue two memory every. Television traditional draw democratic.",  
      "addressCountry": "Fund threat they increase. Guy series politics bag.",  
      "postalCode": "Production later according down yes. Nothing my forward.",  
      "postOfficeBoxNumber": "Beat maintain people",  
      "streetNr": "East too Republican represent behind leader. Little television few Republican fire behavior good.",  
      "district": "Ever theory social special century spring."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "It she follow board blood. Certainly easy particular she sure by big. Say cold national expect rock. Value ski"  
  },  
  "type": "Signal",  
  "relativeDistanceDangerPoint": {  
    "type": "Property",  
    "value": 859  
  },  
  "signalId": {  
    "type": "Property",  
    "value": "Mean PM capital car particular head. Claim ago brother forget. Benefit start body ask yet age believe."  
  },  
  "signalOrientation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalOrientation:XSWZ:79200878"  
  },  
  "signalType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:signalType:OIXR:27955866"  
  },  
  "track": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Signal:track:SBLI:67422940"  
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

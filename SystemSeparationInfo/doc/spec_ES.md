<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: SystemSeparationInfo    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ERA/blob/master/SystemSeparationInfo/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Indicación de varias informaciones necesarias sobre la separación del sistema.**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública      
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `systemSeparationInfoChangeSupplySystem[string]`: Información sobre la separación del sistema Cambiar el sistema de suministro  - `systemSeparationInfoLength[number]`: Longitud de la información de separación del sistema  - `systemSeparationInfoPantographLowered[boolean]`: Sistema de separación info pantógrafo bajado  - `systemSeparationInfoSwitchOffBreaker[boolean]`: Información sobre la separación del sistema Desconectar el disyuntor  - `type[string]`: Tipo de datos NGSI. Tiene que ser SystemSeparationInfo  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
modelo de datos extraído de la ontología ERA https://data-interop.era.europa.eu/era-vocabulary (Agencia Ferroviaria de la Unión Europea)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SystemSeparationInfo:      
  description: Indication of required several information on system separation.      
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
    systemSeparationInfoChangeSupplySystem:      
      description: System separation info change supply system      
      type: string      
      x-ngsi:      
        type: Property      
    systemSeparationInfoLength:      
      description: System separation info length      
      type: number      
      x-ngsi:      
        type: Property      
    systemSeparationInfoPantographLowered:      
      description: System separation info  pantograph lowered      
      type: boolean      
      x-ngsi:      
        type: Property      
    systemSeparationInfoSwitchOffBreaker:      
      description: System separation info switch off breaker      
      type: boolean      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be SystemSeparationInfo      
      enum:      
        - SystemSeparationInfo      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/SystemSeparationInfo      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SystemSeparationInfo/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json      
  x-model-tags: 'ERA vocabulary, railway, train'      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### SystemSeparationInfo NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un SystemSeparationInfo en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": "1971-06-11T11:02:58Z",  
  "dateModified": "1981-04-17T22:16:45Z",  
  "source": "Quickly final probably box society with. View woman main analysis. Think region why best with.",  
  "name": "Treat inside expect figure. Animal ago television visit late.",  
  "alternateName": "Under feel opportunity next win",  
  "description": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro",  
  "dataProvider": "Drive read poor policy. Try quality report safe. Yard reason continue wide.",  
  "owner": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
    "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.1257535,  
      35.88905  
    ]  
  },  
  "address": {  
    "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
    "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
    "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
    "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
    "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
    "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
    "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
    "district": "Forget memory specific own fast p"  
  },  
  "areaServed": "Understand him visit certain task. Bar staff use but.",  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess.",  
  "systemSeparationInfoLength": 864,  
  "systemSeparationInfoPantographLowered": false,  
  "systemSeparationInfoSwitchOffBreaker": false,  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SystemSeparationInfo NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un SystemSeparationInfo en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1971-06-11T11:02:58Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1981-04-17T22:16:45Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Quickly final probably box society with. View woman main analysis. Think region why best with."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Treat inside expect figure. Animal ago television visit late."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Under feel opportunity next win"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Drive read poor policy. Try quality report safe. Yard reason continue wide."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
      "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        37.1257535,  
        35.88905  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
      "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
      "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
      "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
      "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
      "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
      "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
      "district": "Forget memory specific own fast p"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Understand him visit certain task. Bar staff use but."  
  },  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": {  
    "type": "Text",  
    "value": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess."  
  },  
  "systemSeparationInfoLength": {  
    "type": "Number",  
    "value": 864  
  },  
  "systemSeparationInfoPantographLowered": {  
    "type": "Boolean",  
    "value": false  
  },  
  "systemSeparationInfoSwitchOffBreaker": {  
    "type": "Boolean",  
    "value": false  
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
#### SystemSeparationInfo NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un SystemSeparationInfo en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:OEYU:04558809",  
  "dateCreated": "1971-06-11T11:02:58Z",  
  "dateModified": "1981-04-17T22:16:45Z",  
  "source": "Quickly final probably box society with. View woman main analysis. Think region why best with.",  
  "name": "Treat inside expect figure. Animal ago television visit late.",  
  "alternateName": "Under feel opportunity next win",  
  "description": "Notice customer speak employee spend lose. Role middle teach important order section task outside. Center resource contro",  
  "dataProvider": "Drive read poor policy. Try quality report safe. Yard reason continue wide.",  
  "owner": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:ADKU:62722895",  
    "urn:ngsi-ld:SystemSeparationInfo:items:TSIM:96224949"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SystemSeparationInfo:items:GQMR:39834804"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      37.1257535,  
      35.88905  
    ]  
  },  
  "address": {  
    "streetAddress": "Rate matter lawyer kitchen late since opportunity sou",  
    "addressLocality": "Two tell buy opportunity particular pass. Military food together peace successfu",  
    "addressRegion": "Always mission where respond campaign military. Key town democratic trade control. Reach myself staff week",  
    "addressCountry": "Prove quite trouble call throughout specific force. Cut gas short explain hospital note.",  
    "postalCode": "Yet position eye manager might chair. Window rich blue media stop expect view care. Floor although light its.",  
    "postOfficeBoxNumber": "Miss word baby put think what. Political everybody than put world discu",  
    "streetNr": "Town main career staff why ahead process. Woman seat PM never good. Cut at w",  
    "district": "Forget memory specific own fast p"  
  },  
  "areaServed": "Understand him visit certain task. Bar staff use but.",  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": "Bed class laugh idea improve garden goal. Skin possible perhaps board. Letter short agent class. Trial role guess.",  
  "systemSeparationInfoLength": 864,  
  "systemSeparationInfoPantographLowered": false,  
  "systemSeparationInfoSwitchOffBreaker": false,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SystemSeparationInfo NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un SystemSeparationInfo en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SystemSeparationInfo:id:XYDV:99228074",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1990-08-14T02:23:40Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2005-06-05T23:14:26Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Stuff kind likely de"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Story pay cover hot which. Day difference floor make husband say. Through break ok daughter."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Scientist maintain feel baby inte"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Might new take. Month detail matter moment here current. Rock sign number. "  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Always speak able break billion requ"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:KLAD:01706991",  
      "urn:ngsi-ld:SystemSeparationInfo:items:OUMR:57506132"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SystemSeparationInfo:items:FZOT:63378927"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -75.5485445,  
        77.256275  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Environmental stage comme",  
      "addressLocality": "Go under experience nor. Defense skill make product.",  
      "addressRegion": "Scientist letter artis",  
      "addressCountry": "Close born subject among water. Hear computer quest",  
      "postalCode": "Until along talk long. Keep support prepare direction reveal national. Effect few institution inside avoid. In hundred gun result clearly.",  
      "postOfficeBoxNumber": "Do account nothing executive ground. Brother put all often recognize method. Surface red three front su",  
      "streetNr": "Beautiful hotel necessary college risk baby. Stop wish either everyone. E",  
      "district": "Impact treatment follow leader. "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Push film partner. Soon themselves guy expert however."  
  },  
  "type": "SystemSeparationInfo",  
  "systemSeparationInfoChangeSupplySystem": {  
    "type": "Property",  
    "value": "Age ten church not. Edge"  
  },  
  "systemSeparationInfoLength": {  
    "type": "Property",  
    "value": 735  
  },  
  "systemSeparationInfoPantographLowered": {  
    "type": "Property",  
    "value": false  
  },  
  "systemSeparationInfoSwitchOffBreaker": {  
    "type": "Property",  
    "value": true  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

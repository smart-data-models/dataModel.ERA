<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Artículo    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ERA/blob/master/Feature/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Clase que engloba las características que forman parte de la infraestructura física (clase InfrastructureObject) y los objetos topológicos (clase TopologicalObject). Es una subclase de la clase Feature geográfica que tiene una representación espacial.**.    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `currentlyValid[boolean]`: Actualmente en vigor  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `length[number]`: Longitud  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de datos NGSI. Tiene que ser Característica  <!-- /30-PropertiesList -->    
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
Feature:      
  description: Class that encompasses the features that are part of the physical infrastructure (class InfrastructureObject) and the topological objects (class TopologicalObject). It is a subclass of the geographical Feature class that has a spatial representation.      
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
    currentlyValid:      
      description: Currently valid      
      type: boolean      
      x-ngsi:      
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
    length:      
      description: Length      
      type: number      
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
      description: NGSI data type. It has to be Feature      
      enum:      
        - Feature      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/Feature      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Feature/LICENSE.md      
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
#### Feature NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de una Característica en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:SWJZ:26079559",  
  "dateCreated": "2000-11-09T19:30:45Z",  
  "dateModified": "1982-01-16T22:00:49Z",  
  "source": "Table live too always movie.",  
  "name": "Somebody his past show. Provide goal who",  
  "alternateName": "Any rise challenge type.",  
  "description": "Responsibility our class apply",  
  "dataProvider": "Rich clear century others contain help. Not about certainly box. Wi",  
  "owner": [  
    "urn:ngsi-ld:Feature:items:WDIR:57277343",  
    "urn:ngsi-ld:Feature:items:YUTH:26427588"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Feature:items:EGCJ:82697620"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      71.6338955,  
      -141.895474  
    ]  
  },  
  "address": {  
    "streetAddress": "Return end child.",  
    "addressLocality": "Trip professional staff answer. Kitchen yard ten worry suggest whose.",  
    "addressRegion": "Art music already home low. Human despite easy back wind people.",  
    "addressCountry": "Great main confere",  
    "postalCode": "Door weight control head southern pass. Practice art anything even.",  
    "postOfficeBoxNumber": "Clear health there former approach. Now money among budget. Current kind page rather.",  
    "streetNr": "Eight quality not include six. Line response ahead girl we. Answer finally daughter everybody fast.",  
    "district": "Camera worker machine away have loss practice since. Along indeed debate Mrs cut. Lot game charge indeed."  
  },  
  "areaServed": "Real throw sell. Two remembe",  
  "type": "Feature",  
  "currentlyValid": true,  
  "length": 845.9  
}  
```  
</details>    
#### Característica NGSI-v2 normalizada Ejemplo    
He aquí un ejemplo de una característica en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:SWJZ:26079559",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2000-11-09T19:30:45Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1982-01-16T22:00:49Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Table live too always movie."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Somebody his past show. Provide goal who"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Any rise challenge type."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Responsibility our class apply"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Rich clear century others contain help. Not about certainly box. Wi"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Feature:items:WDIR:57277343",  
      "urn:ngsi-ld:Feature:items:YUTH:26427588"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Feature:items:EGCJ:82697620"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        71.6338955,  
        -141.895474  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Return end child.",  
      "addressLocality": "Trip professional staff answer. Kitchen yard ten worry suggest whose.",  
      "addressRegion": "Art music already home low. Human despite easy back wind people.",  
      "addressCountry": "Great main confere",  
      "postalCode": "Door weight control head southern pass. Practice art anything even.",  
      "postOfficeBoxNumber": "Clear health there former approach. Now money among budget. Current kind page rather.",  
      "streetNr": "Eight quality not include six. Line response ahead girl we. Answer finally daughter everybody fast.",  
      "district": "Camera worker machine away have loss practice since. Along indeed debate Mrs cut. Lot game charge indeed."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Real throw sell. Two remembe"  
  },  
  "type": "Feature",  
  "currentlyValid": {  
    "type": "Boolean",  
    "value": true  
  },  
  "length": {  
    "type": "Number",  
    "value": 845.9  
  }  
}  
```  
</details>    
#### Feature NGSI-LD key-values Ejemplo    
He aquí un ejemplo de una Característica en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:SWJZ:26079559",  
  "dateCreated": "2000-11-09T19:30:45Z",  
  "dateModified": "1982-01-16T22:00:49Z",  
  "source": "Table live too always movie.",  
  "name": "Somebody his past show. Provide goal who",  
  "alternateName": "Any rise challenge type.",  
  "description": "Responsibility our class apply",  
  "dataProvider": "Rich clear century others contain help. Not about certainly box. Wi",  
  "owner": [  
    "urn:ngsi-ld:Feature:items:WDIR:57277343",  
    "urn:ngsi-ld:Feature:items:YUTH:26427588"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Feature:items:EGCJ:82697620"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      71.6338955,  
      -141.895474  
    ]  
  },  
  "address": {  
    "streetAddress": "Return end child.",  
    "addressLocality": "Trip professional staff answer. Kitchen yard ten worry suggest whose.",  
    "addressRegion": "Art music already home low. Human despite easy back wind people.",  
    "addressCountry": "Great main confere",  
    "postalCode": "Door weight control head southern pass. Practice art anything even.",  
    "postOfficeBoxNumber": "Clear health there former approach. Now money among budget. Current kind page rather.",  
    "streetNr": "Eight quality not include six. Line response ahead girl we. Answer finally daughter everybody fast.",  
    "district": "Camera worker machine away have loss practice since. Along indeed debate Mrs cut. Lot game charge indeed."  
  },  
  "areaServed": "Real throw sell. Two remembe",  
  "type": "Feature",  
  "currentlyValid": true,  
  "length": 845.9,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Característica NGSI-LD normalizada Ejemplo    
He aquí un ejemplo de una característica en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Feature:id:NAYS:82910625",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2015-12-02T02:59:26Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-04-07T17:47:44Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Station pick serious other seat. Power way score institution. Bill TV some h"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Production factor successful white she live size. Fire social air enter. Skill son sell painting do garden true."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Such culture so million. His break business remembe"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Lose edge want describe nice. Else course war direction international near ask second."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Cell force pull majo"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Feature:items:NLJN:58101473",  
      "urn:ngsi-ld:Feature:items:NCUV:87294142"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Feature:items:TOZC:68395253"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -21.7138025,  
        -147.023625  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Film tend professional them against between.",  
      "addressLocality": "Country wall dream shoulder treatm",  
      "addressRegion": "Nothing seek address military edge analysis. Well difference series adult method rather",  
      "addressCountry": "Rate purpose see clearly new serious effort. Law travel draw i",  
      "postalCode": "Owner because learn medical. Education adult",  
      "postOfficeBoxNumber": "As true environmental give. Wait how machine century task.",  
      "streetNr": "Anything president her culture each. Several hold couple hair rule manage early most.",  
      "district": "Beyond state c"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Market yeah different one range lay blood. Operation into near drug something. Beautiful effort"  
  },  
  "type": "Feature",  
  "currentlyValid": {  
    "type": "Property",  
    "value": true  
  },  
  "length": {  
    "type": "Property",  
    "value": 955.0  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

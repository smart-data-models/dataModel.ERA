<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Plataforma    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ERA/blob/master/Platform/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **A efectos del RINF, por andén se entiende un borde de andén. Un andén se refiere únicamente a la parte de la estructura vecina a la vía (interconectada con los trenes)**.    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaBoardingAid[number]`: Información del nivel de acceso al tren para el que puede utilizarse la ayuda de embarque.  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `assistanceStartingTrain[boolean]`: Existencia de asistencia en el andén para arrancar el tren  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `hasPlatformCurvature[boolean]`: Existencia de curvatura de la plataforma  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `platformHeight[uri]`: Altura de la plataforma  - `platformId[string]`: Id de plataforma  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `tenClassification[uri]`: Clasificación RTE (de vía, de andén, de apartadero)  - `type[string]`: Tipo de datos NGSI. Tiene que ser Plataforma  <!-- /30-PropertiesList -->    
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
Platform:      
  description: Platform for the purpose of RINF is understood as a platform edge. A platform concerns only the part of the structure neighbouring to the track (interfaced with trains).      
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
    areaBoardingAid:      
      description: Information of the train access level for which the boarding aid can be used.      
      type: number      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    assistanceStartingTrain:      
      description: Existence of platform assistance for starting train      
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
    hasPlatformCurvature:      
      description: Existence of  platform curvature      
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
    platformHeight:      
      description: Height of platform      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    platformId:      
      description: Platform id      
      type: string      
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
    tenClassification:      
      description: 'TEN classification (of track, of platform, of siding)'      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    type:      
      description: NGSI data type. It has to be Platform      
      enum:      
        - Platform      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/Platform      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Platform/LICENSE.md      
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
#### Platform NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de Plataforma en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Platform:id:REDQ:77428165",  
  "dateCreated": "2014-05-22T17:31:26Z",  
  "dateModified": "2015-07-10T11:53:40Z",  
  "source": "Expert add young argue expect fast cover. Last choose environment among authority. Though these set phone movie.",  
  "name": "Ahead wish nation. Suddenly item price thank ",  
  "alternateName": "Thing always des",  
  "description": "Brother teacher eight. Seven dark discuss cut industry. Woman morning new something reach state summer also.",  
  "dataProvider": "Box party next industry growth. Ask whether smile. Ready performance hit physical.",  
  "owner": [  
    "urn:ngsi-ld:Platform:items:EWLF:88873659",  
    "urn:ngsi-ld:Platform:items:RDZQ:94648337"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Platform:items:KUEW:50743453"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      0.7759285,  
      6.065558  
    ]  
  },  
  "address": {  
    "streetAddress": "Beat change nor western floor. Quickly continue let often.",  
    "addressLocality": "Certainly from interesting race standard natura",  
    "addressRegion": "Sense road week mention or. Worker still partner position wall fly training. By field husband professional.",  
    "addressCountry": "Tend thank artist prepare. Pretty choice",  
    "postalCode": "Measure dark able win usually respond whom. Cult",  
    "postOfficeBoxNumber": "Possible consumer war call at certain. Wrong stuff program color professional. Tax fish medical end performance as Mrs run.",  
    "streetNr": "Both in human kid trouble else. Cause wi",  
    "district": "Box vote much somebody. Story center listen push. Manager last address degree exactly."  
  },  
  "areaServed": "Election young each situation water. Discover situation change prove entire middle.",  
  "type": "Platform",  
  "areaBoardingAid": 864,  
  "assistanceStartingTrain": false,  
  "hasPlatformCurvature": false,  
  "platformId": "Whole magazine truth st",  
  "platformHeight": "urn:ngsi-ld:Platform:platformHeight:TZIR:59382421",  
  "tenClassification": "urn:ngsi-ld:Platform:tenClassification:DLNK:92411578",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Plataforma NGSI-v2 normalizada Ejemplo    
He aquí un ejemplo de Plataforma en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Platform:id:REDQ:77428165",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2014-05-22T17:31:26Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2015-07-10T11:53:40Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Expert add young argue expect fast cover. Last choose environment among authority. Though these set phone movie."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Ahead wish nation. Suddenly item price thank "  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Thing always des"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Brother teacher eight. Seven dark discuss cut industry. Woman morning new something reach state summer also."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Box party next industry growth. Ask whether smile. Ready performance hit physical."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Platform:items:EWLF:88873659",  
      "urn:ngsi-ld:Platform:items:RDZQ:94648337"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Platform:items:KUEW:50743453"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        0.7759285,  
        6.065558  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Beat change nor western floor. Quickly continue let often.",  
      "addressLocality": "Certainly from interesting race standard natura",  
      "addressRegion": "Sense road week mention or. Worker still partner position wall fly training. By field husband professional.",  
      "addressCountry": "Tend thank artist prepare. Pretty choice",  
      "postalCode": "Measure dark able win usually respond whom. Cult",  
      "postOfficeBoxNumber": "Possible consumer war call at certain. Wrong stuff program color professional. Tax fish medical end performance as Mrs run.",  
      "streetNr": "Both in human kid trouble else. Cause wi",  
      "district": "Box vote much somebody. Story center listen push. Manager last address degree exactly."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Election young each situation water. Discover situation change prove entire middle."  
  },  
  "type": "Platform",  
  "areaBoardingAid": {  
    "type": "Number",  
    "value": 864  
  },  
  "assistanceStartingTrain": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasPlatformCurvature": {  
    "type": "Boolean",  
    "value": false  
  },  
  "platformId": {  
    "type": "Text",  
    "value": "Whole magazine truth st"  
  },  
  "platformHeight": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Platform:platformHeight:TZIR:59382421"  
  },  
  "tenClassification": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Platform:tenClassification:DLNK:92411578"  
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
#### Plataforma NGSI-LD de valores clave Ejemplo    
He aquí un ejemplo de Plataforma en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Platform:id:REDQ:77428165",  
  "dateCreated": "2014-05-22T17:31:26Z",  
  "dateModified": "2015-07-10T11:53:40Z",  
  "source": "Expert add young argue expect fast cover. Last choose environment among authority. Though these set phone movie.",  
  "name": "Ahead wish nation. Suddenly item price thank ",  
  "alternateName": "Thing always des",  
  "description": "Brother teacher eight. Seven dark discuss cut industry. Woman morning new something reach state summer also.",  
  "dataProvider": "Box party next industry growth. Ask whether smile. Ready performance hit physical.",  
  "owner": [  
    "urn:ngsi-ld:Platform:items:EWLF:88873659",  
    "urn:ngsi-ld:Platform:items:RDZQ:94648337"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Platform:items:KUEW:50743453"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      0.7759285,  
      6.065558  
    ]  
  },  
  "address": {  
    "streetAddress": "Beat change nor western floor. Quickly continue let often.",  
    "addressLocality": "Certainly from interesting race standard natura",  
    "addressRegion": "Sense road week mention or. Worker still partner position wall fly training. By field husband professional.",  
    "addressCountry": "Tend thank artist prepare. Pretty choice",  
    "postalCode": "Measure dark able win usually respond whom. Cult",  
    "postOfficeBoxNumber": "Possible consumer war call at certain. Wrong stuff program color professional. Tax fish medical end performance as Mrs run.",  
    "streetNr": "Both in human kid trouble else. Cause wi",  
    "district": "Box vote much somebody. Story center listen push. Manager last address degree exactly."  
  },  
  "areaServed": "Election young each situation water. Discover situation change prove entire middle.",  
  "type": "Platform",  
  "areaBoardingAid": 864,  
  "assistanceStartingTrain": false,  
  "hasPlatformCurvature": false,  
  "platformId": "Whole magazine truth st",  
  "platformHeight": "urn:ngsi-ld:Platform:platformHeight:TZIR:59382421",  
  "tenClassification": "urn:ngsi-ld:Platform:tenClassification:DLNK:92411578",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Plataforma NGSI-LD normalizada Ejemplo    
He aquí un ejemplo de Plataforma en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Platform:id:IGEE:91325946",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2004-01-10T21:28:28Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-02-19T11:00:31Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Professional mean like fine box. Most statement military this there after also consumer."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Organization human on apply history enter. Response guy today fact field stand. Should statement strategy tru"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Huge address same song act power. Property man sit direction wonder. Year general doctor production black after hold."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Break official black hold. Them next create between half."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Partner base paper. Positive form"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Platform:items:DWXZ:32083986",  
      "urn:ngsi-ld:Platform:items:DFRT:50172537"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Platform:items:JJZM:20586004"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        83.360268,  
        -144.578543  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Teach analysis agent poor chair local American. These number wrong nation.",  
      "addressLocality": "Will floor nearly baby. Writer admit race training one several quality.",  
      "addressRegion": "Probably know top realize various whole. Perhaps success a",  
      "addressCountry": "Open economy town early change family future. Remember democratic meet boy total method. Av",  
      "postalCode": "Future business hear hold especially like perform require. Direction establish hospital. Ball Democrat sound executive run though.",  
      "postOfficeBoxNumber": "Edge particularly improve g",  
      "streetNr": "Likely grow million large responsibility. Film watch m",  
      "district": "Sure certain give hospital thought buy. Room really specific seem president. Should condition level especi"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Rise fear color answer federal smile. Phone believe although relationship"  
  },  
  "type": "Platform",  
  "areaBoardingAid": {  
    "type": "Property",  
    "value": 908  
  },  
  "assistanceStartingTrain": {  
    "type": "Property",  
    "value": true  
  },  
  "hasPlatformCurvature": {  
    "type": "Property",  
    "value": false  
  },  
  "platformId": {  
    "type": "Property",  
    "value": "Final politics cultural from travel respond."  
  },  
  "platformHeight": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Platform:platformHeight:AJIG:62479263"  
  },  
  "tenClassification": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Platform:tenClassification:VRUU:42134110"  
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

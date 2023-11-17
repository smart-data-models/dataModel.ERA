<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: FrenchTrainDetectionSystemLimitation    
=============================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Específico para la comprobación de compatibilidad de rutas en la red francesa. Secciones con:    
-1 El tonelaje circulado por vía es inferior a 15000 toneladas/día/pista    
-2 Enclavamiento direccional    
-3 Retardo de 45 segundos para el enclavamiento direccional    
-4 Instalación con anuncio de circuito de vía    
-5 Ausencia de pedal de ayuda a la maniobra en el sentido normal de circulación para líneas de doble vía no reversibles    
-6 Ausencia de pedal de ayuda a la maniobra independientemente del sentido de circulación para las líneas de vía única y las vías para doble sentido de circulación    
-7 Ausencia de pedal anunciador    
-8 Retardo de 45 segundos para los dispositivos específicos de rearme del anuncio**    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `frenchTrainDetectionSystemLimitationApplicable[boolean]`: Se aplica la sección con limitación de detección de trenes, sólo para la red francesa  - `frenchTrainDetectionSystemLimitationNumber[uri]`: Sección con número de limitación de detección de trenes, sólo para la red francesa  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de datos NGSI. Tiene que ser FrenchTrainDetectionSystemLimitation  <!-- /30-PropertiesList -->    
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
FrenchTrainDetectionSystemLimitation:      
  description: "Specific for route compatibility check on French network. Sections with: \n-1 Tonnage circulated per track is inferior to 15000 tons/day/track \n-2 Directional Interlocking \n-3 45-second delay for directional interlocking \n-4 Installation with track circuit announcement \n-5 Absence of a shunting assistance pedal in the normal direction of circulation for non-reversible double track lines \n-6 Absence of a shunting assistance pedal regardless of the direction of traffic for single track lines and tracks for two way working \n-7 Absence of a pedal announcement mechanism \n-8 45-second delay for specific announcement reset devices"      
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
    frenchTrainDetectionSystemLimitationApplicable:      
      description: 'Section with train detection limitation is applicable, only for the French network'      
      type: boolean      
      x-ngsi:      
        type: Property      
    frenchTrainDetectionSystemLimitationNumber:      
      description: 'Section with train detection limitation number, only for French  network'      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
      description: NGSI data type. It has to be FrenchTrainDetectionSystemLimitation      
      enum:      
        - FrenchTrainDetectionSystemLimitation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/FrenchTrainDetectionSystemLimitation      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/FrenchTrainDetectionSystemLimitation/LICENSE.md      
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
#### FrenchTrainDetectionSystemLimitation NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de FrenchTrainDetectionSystemLimitation en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": "2014-09-23T15:45:27Z",  
  "dateModified": "1995-12-08T08:26:38Z",  
  "source": "Including since ",  
  "name": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure.",  
  "alternateName": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist",  
  "description": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military.",  
  "dataProvider": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science.",  
  "owner": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -21.934426,  
      6.101443  
    ]  
  },  
  "address": {  
    "streetAddress": "Wonder majority ability. Forget throughout discussion cost. Dream store case number.",  
    "addressLocality": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain.",  
    "addressRegion": "Lot watch matter. Item station",  
    "addressCountry": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill.",  
    "postalCode": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker.",  
    "postOfficeBoxNumber": "Near bed always benefit fine popular economic. Ever material save after scientist.",  
    "streetNr": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit",  
    "district": "Open administration space ahead. Soci"  
  },  
  "areaServed": "Including international kind animal customer. Identify large me. Field deal ",  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": false,  
  "frenchTrainDetectionSystemLimitationNumber": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183"  
}  
```  
</details>    
#### FrenchTrainDetectionSystemLimitation NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de FrenchTrainDetectionSystemLimitation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2014-09-23T15:45:27Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1995-12-08T08:26:38Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Including since "  
  },  
  "name": {  
    "type": "Text",  
    "value": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -21.934426,  
        6.101443  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Wonder majority ability. Forget throughout discussion cost. Dream store case number.",  
      "addressLocality": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain.",  
      "addressRegion": "Lot watch matter. Item station",  
      "addressCountry": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill.",  
      "postalCode": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker.",  
      "postOfficeBoxNumber": "Near bed always benefit fine popular economic. Ever material save after scientist.",  
      "streetNr": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit",  
      "district": "Open administration space ahead. Soci"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Including international kind animal customer. Identify large me. Field deal "  
  },  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": {  
    "type": "Boolean",  
    "value": false  
  },  
  "frenchTrainDetectionSystemLimitationNumber": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183"  
  }  
}  
```  
</details>    
#### FrenchTrainDetectionSystemLimitation NGSI-LD key-values Ejemplo    
He aquí un ejemplo de FrenchTrainDetectionSystemLimitation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:PSSH:36864867",  
  "dateCreated": "2014-09-23T15:45:27Z",  
  "dateModified": "1995-12-08T08:26:38Z",  
  "source": "Including since ",  
  "name": "Happy partner share space rock know wait. Easy something result inside strategy approach. Hold book dream agreement loss site sure.",  
  "alternateName": "Effort actually scientist window act green modern. Picture read theory deep set minute even. Beautiful machine reduce truth television design time scientist",  
  "description": "Person opportunity very kitchen phone similar. Service service find strategy. Wall to ready institution support meeting military.",  
  "dataProvider": "Computer hotel federal kid it perhaps. Source within international senior stop final around. Evidence music science.",  
  "owner": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:ZDER:64486064",  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:EWOX:19497229"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:BOEA:61450089"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -21.934426,  
      6.101443  
    ]  
  },  
  "address": {  
    "streetAddress": "Wonder majority ability. Forget throughout discussion cost. Dream store case number.",  
    "addressLocality": "Turn which sometimes. Environmental middle popular series. Stock cold hundred street read she maintain.",  
    "addressRegion": "Lot watch matter. Item station",  
    "addressCountry": "Religious none pretty defense. End out without then party. Stock million difficult resource million bring name bill.",  
    "postalCode": "Enjoy fear task company run. Left play marriage type someone ok. Away require city worker.",  
    "postOfficeBoxNumber": "Near bed always benefit fine popular economic. Ever material save after scientist.",  
    "streetNr": "Read much station loss door room cold entire. Various agree whether above ago where. Knowledge risk article degree spend drive. Science most question meet visit",  
    "district": "Open administration space ahead. Soci"  
  },  
  "areaServed": "Including international kind animal customer. Identify large me. Field deal ",  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": false,  
  "frenchTrainDetectionSystemLimitationNumber": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:PVYQ:85174183",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### FrenchTrainDetectionSystemLimitation NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de FrenchTrainDetectionSystemLimitation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:id:MUMN:30355615",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-12-11T22:05:23Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1974-08-04T09:15:57Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Vote middle customer. Know account build. Son garden image support TV"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Kid behavior decision century. Accept father hand hundred order. Space enjoy store radio office enter cover."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Pretty four year people. Message mother action recently catch."  
  },  
  "description": {  
    "type": "Property",  
    "value": "National "  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Able involve move contain who director improve speak. Inc"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:OCPM:47545823",  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:YYEI:53415372"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:items:FKOO:81839190"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -78.20408,  
        125.044799  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Term ",  
      "addressLocality": "Return nature nothing soon democratic in. Time reach name mother pretty. Alone blue treatment together herself sound change painting.",  
      "addressRegion": "Always century cut do accept team despite. Region prevent save over degree. Nice each happen month away card.",  
      "addressCountry": "Land wife history method service they teach. Herself place movement throw discussion father. Nearly talk officer ok.",  
      "postalCode": "Difference less money reason final individual raise. Stay under car interesting check north policy. Purpose face worker apply surface.",  
      "postOfficeBoxNumber": "Baby possible guy set. Road style project hundred of its. Wife film g",  
      "streetNr": "Early star vote stor",  
      "district": "Idea buy concern relate se"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Image agent star total civil. Because a"  
  },  
  "type": "FrenchTrainDetectionSystemLimitation",  
  "frenchTrainDetectionSystemLimitationApplicable": {  
    "type": "Property",  
    "value": false  
  },  
  "frenchTrainDetectionSystemLimitationNumber": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FrenchTrainDetectionSystemLimitation:frenchTrainDetectionSystemLimitationNumber:FWCD:62453633"  
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

<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Zona especial    
======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ERA/blob/master/SpecialArea/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Abarca todas aquellas zonas o secciones como zonas seguras, zonas restringidas (zonas sin paradas o lugares de riesgo industrial)**.    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `specialAreaType[uri]`: Tipo de zona especial  - `type[string]`: Tipo de datos NGSI. Tiene que ser SpecialArea  <!-- /30-PropertiesList -->    
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
SpecialArea:      
  description: 'Encompasses all those areas or sections such as safe areas, restricted areas (non-stopping areas or industrial risk locations).'      
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
    specialAreaType:      
      description: Special area type      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    type:      
      description: NGSI data type. It has to be SpecialArea      
      enum:      
        - SpecialArea      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/SpecialArea      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SpecialArea/LICENSE.md      
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
#### SpecialArea NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de un SpecialArea en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:LPYR:16529675",  
  "dateCreated": "1992-05-24T05:59:05Z",  
  "dateModified": "1997-01-09T06:38:30Z",  
  "source": "Federal tough Republican popular any. Society he",  
  "name": "Rule discuss business guess picture. Another stuff new five affect artist instead. Yard test remember smile dem",  
  "alternateName": "Field ball any out authority last set. Charge moment Mrs.",  
  "description": "Piece or sell far time then. Focus deal through her marriage some.",  
  "dataProvider": "National worker admit speak interview day. Person hit behind property.",  
  "owner": [  
    "urn:ngsi-ld:SpecialArea:items:OTDU:99373788",  
    "urn:ngsi-ld:SpecialArea:items:LJSH:77643420"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialArea:items:YBMA:89347369"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      22.340017,  
      19.489173  
    ]  
  },  
  "address": {  
    "streetAddress": "Stay I draw painting sometimes chance. Teacher where quality before commercial property.",  
    "addressLocality": "Exactly question left writer eye. Movie land rich another knowledge mu",  
    "addressRegion": "Good over fish perform. Training lead fund true middle force use. Chair along drop that maintain. ",  
    "addressCountry": "Car easy budget their goal along. Against late alone foot hard differen",  
    "postalCode": "Nor various glass why result spee",  
    "postOfficeBoxNumber": "Half reduce ahead on from quite movement. Movie offer enough type. Name organization apply he hotel.",  
    "streetNr": "No entire boy pick imagine another. Describe purpose president third piece none prepare.",  
    "district": "Traditional development argue hundred. Friend usually after among class put."  
  },  
  "areaServed": "City teacher standard court l",  
  "type": "SpecialArea",  
  "specialAreaType": "urn:ngsi-ld:SpecialArea:specialAreaType:KUMC:59668635"  
}  
```  
</details>    
#### SpecialArea NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un SpecialArea en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:LPYR:16529675",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1992-05-24T05:59:05Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1997-01-09T06:38:30Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Federal tough Republican popular any. Society he"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Rule discuss business guess picture. Another stuff new five affect artist instead. Yard test remember smile dem"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Field ball any out authority last set. Charge moment Mrs."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Piece or sell far time then. Focus deal through her marriage some."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "National worker admit speak interview day. Person hit behind property."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:OTDU:99373788",  
      "urn:ngsi-ld:SpecialArea:items:LJSH:77643420"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:YBMA:89347369"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        22.340017,  
        19.489173  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Stay I draw painting sometimes chance. Teacher where quality before commercial property.",  
      "addressLocality": "Exactly question left writer eye. Movie land rich another knowledge mu",  
      "addressRegion": "Good over fish perform. Training lead fund true middle force use. Chair along drop that maintain. ",  
      "addressCountry": "Car easy budget their goal along. Against late alone foot hard differen",  
      "postalCode": "Nor various glass why result spee",  
      "postOfficeBoxNumber": "Half reduce ahead on from quite movement. Movie offer enough type. Name organization apply he hotel.",  
      "streetNr": "No entire boy pick imagine another. Describe purpose president third piece none prepare.",  
      "district": "Traditional development argue hundred. Friend usually after among class put."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "City teacher standard court l"  
  },  
  "type": "SpecialArea",  
  "specialAreaType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SpecialArea:specialAreaType:KUMC:59668635"  
  }  
}  
```  
</details>    
#### SpecialArea NGSI-LD key-values Ejemplo    
He aquí un ejemplo de un SpecialArea en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:LPYR:16529675",  
  "dateCreated": "1992-05-24T05:59:05Z",  
  "dateModified": "1997-01-09T06:38:30Z",  
  "source": "Federal tough Republican popular any. Society he",  
  "name": "Rule discuss business guess picture. Another stuff new five affect artist instead. Yard test remember smile dem",  
  "alternateName": "Field ball any out authority last set. Charge moment Mrs.",  
  "description": "Piece or sell far time then. Focus deal through her marriage some.",  
  "dataProvider": "National worker admit speak interview day. Person hit behind property.",  
  "owner": [  
    "urn:ngsi-ld:SpecialArea:items:OTDU:99373788",  
    "urn:ngsi-ld:SpecialArea:items:LJSH:77643420"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SpecialArea:items:YBMA:89347369"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      22.340017,  
      19.489173  
    ]  
  },  
  "address": {  
    "streetAddress": "Stay I draw painting sometimes chance. Teacher where quality before commercial property.",  
    "addressLocality": "Exactly question left writer eye. Movie land rich another knowledge mu",  
    "addressRegion": "Good over fish perform. Training lead fund true middle force use. Chair along drop that maintain. ",  
    "addressCountry": "Car easy budget their goal along. Against late alone foot hard differen",  
    "postalCode": "Nor various glass why result spee",  
    "postOfficeBoxNumber": "Half reduce ahead on from quite movement. Movie offer enough type. Name organization apply he hotel.",  
    "streetNr": "No entire boy pick imagine another. Describe purpose president third piece none prepare.",  
    "district": "Traditional development argue hundred. Friend usually after among class put."  
  },  
  "areaServed": "City teacher standard court l",  
  "type": "SpecialArea",  
  "specialAreaType": "urn:ngsi-ld:SpecialArea:specialAreaType:KUMC:59668635",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SpecialArea NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un SpecialArea en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SpecialArea:id:BXVG:20578065",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-07-13T20:29:53Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1996-03-16T13:18:03Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Work it low government."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Vote upon star show occur. Meeting technology half marriage role number."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Concern threat require Mr suggest benefit. Short run home hard forward."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Environment economy scene se"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Bar teach middle mean born. Skill have person window media man. Run court treatment eat second."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:AFRV:18308441",  
      "urn:ngsi-ld:SpecialArea:items:MUMA:06460118"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SpecialArea:items:YBKX:99238445"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -44.9842385,  
        -63.929183  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Everything how similar",  
      "addressLocality": "Serious off dog record call somebody. C",  
      "addressRegion": "Resource threat scientist candidate specific realize. Education event population he behavior. Other white member chair image.",  
      "addressCountry": "Professor near behind of will little. Pattern agent nothing arm message say he. Size doctor thing me benefit.",  
      "postalCode": "Standard for same agreement foot wind government. Now project citizen within course trial. Country role report wear indicate customer him simply. Trial smile want marriage m",  
      "postOfficeBoxNumber": "Statement court method chance street develop sound.",  
      "streetNr": "Interest she rather media reality attack. Seat service professor.",  
      "district": "Focus "  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Grow same something good. Still go small move fall international mean."  
  },  
  "type": "SpecialArea",  
  "specialAreaType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SpecialArea:specialAreaType:VEIZ:54748811"  
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

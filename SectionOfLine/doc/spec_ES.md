<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: SectionOfLine  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.ERA/blob/master/SectionOfLine/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Se entiende por tramo de línea la parte de línea comprendida entre puntos operativos adyacentes y puede constar de varias vías.  
En https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.1 Secciones de línea.**  
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `lineNationalId[uri]`: Identificación de la línea nacional  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `opEnd[uri]`: Punto operativo al final del tramo de línea  - `opStart[uri]`: Punto operativo al inicio del tramo de línea  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `solNature[uri]`: Naturaleza de la sección de la línea  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `track[uri]`: Pista  - `type[string]`: Tipo de datos NGSI. Tiene que ser SectionOfLine  <!-- /30-PropertiesList -->  
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
SectionOfLine:    
  description: |-    
    A section of line means the part of line between adjacent operational points and may consist of several tracks.    
    In https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.1 Line sections.    
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
    lineNationalId:    
      description: National line identification    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    opEnd:    
      description: Operational Point at end of Section of Line    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    opStart:    
      description: Operational Point at start of Section of Line    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    solNature:    
      description: Nature of Section of Line    
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
      description: NGSI data type. It has to be SectionOfLine    
      enum:    
        - SectionOfLine    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/SectionOfLine    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SectionOfLine/LICENSE.md    
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
#### SectionOfLine NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de una SectionOfLine en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:NVYV:48459502",  
  "dateCreated": "2019-05-29T20:37:27Z",  
  "dateModified": "1990-02-07T09:13:17Z",  
  "source": "Someone perform protect too even. Into",  
  "name": "Should reduce admit door you. Entire tonight hold cultural answer your. That indicate stock r",  
  "alternateName": "Herself teacher rather inside me. A our read. Police phone data ahead.",  
  "description": "Return conference five know",  
  "dataProvider": "Low light peace home. Tend base report admit.",  
  "owner": [  
    "urn:ngsi-ld:SectionOfLine:items:QUNL:25640251",  
    "urn:ngsi-ld:SectionOfLine:items:TUBX:09855374"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SectionOfLine:items:BNLE:70988625"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -49.248493,  
      -99.418946  
    ]  
  },  
  "address": {  
    "streetAddress": "Consider affect seven difference impact or. Carry sport identify magazine listen science ",  
    "addressLocality": "Phone quality top current. Range until big suggest both focus.",  
    "addressRegion": "Light through th",  
    "addressCountry": "Ready pay for presen",  
    "postalCode": "Purpose feel son current mission address. Future although everyone affect.",  
    "postOfficeBoxNumber": "Point road player personal around rich cut. If try raise meet process.",  
    "streetNr": "Somebody lawyer production often nearly news. Material he front.",  
    "district": "Stage especially site list writer. Political pr"  
  },  
  "areaServed": "Finally star wonder ask us. Family focus tell sing goal today them voice. Together story west or official.",  
  "type": "SectionOfLine",  
  "lineNationalId": "urn:ngsi-ld:SectionOfLine:lineNationalId:ISBE:85077227",  
  "opEnd": "urn:ngsi-ld:SectionOfLine:opEnd:MIJK:54736457",  
  "opStart": "urn:ngsi-ld:SectionOfLine:opStart:QOPP:74078654",  
  "solNature": "urn:ngsi-ld:SectionOfLine:solNature:UWFX:27604875",  
  "track": "urn:ngsi-ld:SectionOfLine:track:RKTG:26142248",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SectionOfLine NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de SectionOfLine en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:NVYV:48459502",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2019-05-29T20:37:27Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1990-02-07T09:13:17Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Someone perform protect too even. Into"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Should reduce admit door you. Entire tonight hold cultural answer your. That indicate stock r"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Herself teacher rather inside me. A our read. Police phone data ahead."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Return conference five know"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Low light peace home. Tend base report admit."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:QUNL:25640251",  
      "urn:ngsi-ld:SectionOfLine:items:TUBX:09855374"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:BNLE:70988625"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -49.248493,  
          -99.418946  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Consider affect seven difference impact or. Carry sport identify magazine listen science "  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Phone quality top current. Range until big suggest both focus."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Light through th"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Ready pay for presen"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Purpose feel son current mission address. Future although everyone affect."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Point road player personal around rich cut. If try raise meet process."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Somebody lawyer production often nearly news. Material he front."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Stage especially site list writer. Political pr"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Finally star wonder ask us. Family focus tell sing goal today them voice. Together story west or official."  
  },  
  "type": "SectionOfLine",  
  "lineNationalId": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:lineNationalId:ISBE:85077227"  
  },  
  "opEnd": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:opEnd:MIJK:54736457"  
  },  
  "opStart": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:opStart:QOPP:74078654"  
  },  
  "solNature": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:solNature:UWFX:27604875"  
  },  
  "track": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SectionOfLine:track:RKTG:26142248"  
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
#### SectionOfLine NGSI-LD key-values Ejemplo  
He aquí un ejemplo de una SectionOfLine en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:NVYV:48459502",  
  "dateCreated": "2019-05-29T20:37:27Z",  
  "dateModified": "1990-02-07T09:13:17Z",  
  "source": "Someone perform protect too even. Into",  
  "name": "Should reduce admit door you. Entire tonight hold cultural answer your. That indicate stock r",  
  "alternateName": "Herself teacher rather inside me. A our read. Police phone data ahead.",  
  "description": "Return conference five know",  
  "dataProvider": "Low light peace home. Tend base report admit.",  
  "owner": [  
    "urn:ngsi-ld:SectionOfLine:items:QUNL:25640251",  
    "urn:ngsi-ld:SectionOfLine:items:TUBX:09855374"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SectionOfLine:items:BNLE:70988625"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -49.248493,  
      -99.418946  
    ]  
  },  
  "address": {  
    "streetAddress": "Consider affect seven difference impact or. Carry sport identify magazine listen science ",  
    "addressLocality": "Phone quality top current. Range until big suggest both focus.",  
    "addressRegion": "Light through th",  
    "addressCountry": "Ready pay for presen",  
    "postalCode": "Purpose feel son current mission address. Future although everyone affect.",  
    "postOfficeBoxNumber": "Point road player personal around rich cut. If try raise meet process.",  
    "streetNr": "Somebody lawyer production often nearly news. Material he front.",  
    "district": "Stage especially site list writer. Political pr"  
  },  
  "areaServed": "Finally star wonder ask us. Family focus tell sing goal today them voice. Together story west or official.",  
  "type": "SectionOfLine",  
  "lineNationalId": "urn:ngsi-ld:SectionOfLine:lineNationalId:ISBE:85077227",  
  "opEnd": "urn:ngsi-ld:SectionOfLine:opEnd:MIJK:54736457",  
  "opStart": "urn:ngsi-ld:SectionOfLine:opStart:QOPP:74078654",  
  "solNature": "urn:ngsi-ld:SectionOfLine:solNature:UWFX:27604875",  
  "track": "urn:ngsi-ld:SectionOfLine:track:RKTG:26142248",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SectionOfLine NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de SectionOfLine en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SectionOfLine:id:BHSJ:12081625",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2002-06-30T22:12:57Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-07-14T14:37:10Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Travel last avoid across clearly. Listen sign tough police product that."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Painting spend near music activity. That parent item. Despite within instead per cost network. Most argue civil w"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Wait go enough truth player itself. Realize military region fight student hel"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Notice note word ground. Dream conference father co"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Run nor scene growth long."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:PAQY:12003815",  
      "urn:ngsi-ld:SectionOfLine:items:ZNNC:60809737"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SectionOfLine:items:YLLU:61619520"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        87.630235,  
        -145.984526  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Important national determine issue forget. Charge he",  
      "addressLocality": "Part plant learn interview. Always site also within return such. Head food audience cut town office vote across. Mil",  
      "addressRegion": "Know big act. Development series cours",  
      "addressCountry": "Successful Mrs home great issue again education degree. Main myself treatment might. Minute amount central.",  
      "postalCode": "A give claim what throw which. Final front dinner. Rich space fire sister maybe support.",  
      "postOfficeBoxNumber": "Effort prepare seem class collection. Husband task your name some gas control. Own ha",  
      "streetNr": "Eye current positive myself trial change worker. Sure show attorney ",  
      "district": "Expect subject edg"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Apply environmental necessary address trip worry."  
  },  
  "type": "SectionOfLine",  
  "lineNationalId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:lineNationalId:WWXI:47713875"  
  },  
  "opEnd": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:opEnd:ESDA:92317943"  
  },  
  "opStart": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:opStart:EXYH:90955448"  
  },  
  "solNature": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:solNature:UBAH:75574617"  
  },  
  "track": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SectionOfLine:track:ZVJB:17662025"  
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

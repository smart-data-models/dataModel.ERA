<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : SectionOfLine    
======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/SectionOfLine/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Un tronçon de ligne désigne la partie de la ligne située entre des points opérationnels adjacents et peut être constitué de plusieurs voies.    
Dans https://eur-lex.europa.eu/eli/reg_impl/2019/773/oj 2.1.1 Sections de ligne.**    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique      
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `lineNationalId[uri]`: Identification de la ligne nationale  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `opEnd[uri]`: Point opérationnel à l'extrémité de la section de la ligne  - `opStart[uri]`: Point opérationnel au début de la section de la ligne  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `solNature[uri]`: Nature de la section de la ligne  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `track[uri]`: Poursuivre  - `type[string]`: Type de données NGSI. Il doit s'agir de SectionOfLine  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
modèle de données mappé à partir de l'ontologie de l'ERA https://data-interop.era.europa.eu/era-vocabulary (Agence de l'Union européenne pour les chemins de fer)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
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
## Exemples de charges utiles    
#### SectionOfLine Valeurs-clés de l'INSIG-v2 Exemple    
Voici un exemple de SectionOfLine au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### SectionOfLine NGSI-v2 normalisée Exemple    
Voici un exemple de SectionOfLine au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
      "coordinates": [  
        -49.248493,  
        -99.418946  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Consider affect seven difference impact or. Carry sport identify magazine listen science ",  
      "addressLocality": "Phone quality top current. Range until big suggest both focus.",  
      "addressRegion": "Light through th",  
      "addressCountry": "Ready pay for presen",  
      "postalCode": "Purpose feel son current mission address. Future although everyone affect.",  
      "postOfficeBoxNumber": "Point road player personal around rich cut. If try raise meet process.",  
      "streetNr": "Somebody lawyer production often nearly news. Material he front.",  
      "district": "Stage especially site list writer. Political pr"  
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
#### SectionOfLine Valeurs clés de la NGSI-LD Exemple    
Voici un exemple de SectionOfLine au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### SectionOfLine NGSI-LD normalisée Exemple    
Voici un exemple de SectionOfLine au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

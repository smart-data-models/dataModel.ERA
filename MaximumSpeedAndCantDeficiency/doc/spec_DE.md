<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

======================================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

MaximumSpeedAndCantDeficiency:    
  description: Combination of maximum speed and maximum cant deficiency for which the vehicle was assessed.    
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
    type:    
      description: NGSI data type. It has to be MaximumSpeedAndCantDeficiency    
      enum:    
        - MaximumSpeedAndCantDeficiency    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleTypeMaximumCantDeficiency:    
      description: Vehicle type maximum cant deficiency    
      type: number    
      x-ngsi:    
        type: Property    
    vehicleTypeMaximumSpeed:    
      description: Vehicle type maximum speed    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/MaximumSpeedAndCantDeficiency    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/MaximumSpeedAndCantDeficiency/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json    
  x-model-tags: 'ERA vocabulary, railway, train'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:EYEV:77635914",  
  "dateCreated": "1978-04-01T14:31:45Z",  
  "dateModified": "1994-03-24T04:16:42Z",  
  "source": "Exist camera tend minute beyond.",  
  "name": "Mission provide place alone move they represent. This theory space sound face personal color. Thing skill kitchen behavior p",  
  "alternateName": "Read look newspaper",  
  "description": "Thing water act tend probably already. Defense future feeling.",  
  "dataProvider": "Evening source mean. Very word edge appe",  
  "owner": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:EKQU:29912232",  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:JOHF:20639722"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:WZSM:91628276"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      82.6869565,  
      24.725948  
    ]  
  },  
  "address": {  
    "streetAddress": "Happy actually court. Cut seek serious anything.",  
    "addressLocality": "Or worry third know leader. Son design detail in matter fine raise. Majority measure other size.",  
    "addressRegion": "Foreign tell several support enter police team respond. History senior position day four month painting. Central nice arm main more phone.",  
    "addressCountry": "Value discussio",  
    "postalCode": "Blue final campaign teacher coach guess. Serve billion development sp",  
    "postOfficeBoxNumber": "Stay never foot thought thing music scientist make.",  
    "streetNr": "Poor party produce sing thought those nature. Same how care either reduce those executive. People bed training continue my.",  
    "district": "Mother tonight this. Pull how blue public support s"  
  },  
  "areaServed": "Character ",  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": 864,  
  "vehicleTypeMaximumSpeed": 864  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:EYEV:77635914",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1978-04-01T14:31:45Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "1994-03-24T04:16:42Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Exist camera tend minute beyond."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Mission provide place alone move they represent. This theory space sound face personal color. Thing skill kitchen behavior p"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Read look newspaper"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Thing water act tend probably already. Defense future feeling."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Evening source mean. Very word edge appe"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:EKQU:29912232",  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:JOHF:20639722"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:WZSM:91628276"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          82.6869565,  
          24.725948  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Happy actually court. Cut seek serious anything."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Or worry third know leader. Son design detail in matter fine raise. Majority measure other size."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Foreign tell several support enter police team respond. History senior position day four month painting. Central nice arm main more phone."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Value discussio"  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Blue final campaign teacher coach guess. Serve billion development sp"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Stay never foot thought thing music scientist make."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Poor party produce sing thought those nature. Same how care either reduce those executive. People bed training continue my."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Mother tonight this. Pull how blue public support s"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Character "  
  },  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": {  
    "type": "Number",  
    "value": 864  
  },  
  "vehicleTypeMaximumSpeed": {  
    "type": "Number",  
    "value": 864  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:EYEV:77635914",  
  "dateCreated": "1978-04-01T14:31:45Z",  
  "dateModified": "1994-03-24T04:16:42Z",  
  "source": "Exist camera tend minute beyond.",  
  "name": "Mission provide place alone move they represent. This theory space sound face personal color. Thing skill kitchen behavior p",  
  "alternateName": "Read look newspaper",  
  "description": "Thing water act tend probably already. Defense future feeling.",  
  "dataProvider": "Evening source mean. Very word edge appe",  
  "owner": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:EKQU:29912232",  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:JOHF:20639722"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:WZSM:91628276"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      82.6869565,  
      24.725948  
    ]  
  },  
  "address": {  
    "streetAddress": "Happy actually court. Cut seek serious anything.",  
    "addressLocality": "Or worry third know leader. Son design detail in matter fine raise. Majority measure other size.",  
    "addressRegion": "Foreign tell several support enter police team respond. History senior position day four month painting. Central nice arm main more phone.",  
    "addressCountry": "Value discussio",  
    "postalCode": "Blue final campaign teacher coach guess. Serve billion development sp",  
    "postOfficeBoxNumber": "Stay never foot thought thing music scientist make.",  
    "streetNr": "Poor party produce sing thought those nature. Same how care either reduce those executive. People bed training continue my.",  
    "district": "Mother tonight this. Pull how blue public support s"  
  },  
  "areaServed": "Character ",  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": 864,  
  "vehicleTypeMaximumSpeed": 864,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:id:BFGJ:99213827",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1976-12-27T03:20:14Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1978-08-12T05:10:54Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "She response spring everyone western."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Base eat lose toward alone sure arrive. Writer "  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Something process c"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Natural window weight police easy second leader. Benefit I let inside."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Since possible deep care actually see side. Budget mean everybody ago hot."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:LZWP:28604460",  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:TIOK:10942469"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:MaximumSpeedAndCantDeficiency:items:GDOF:24605591"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -65.854435,  
        85.690336  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "College thing born our. Military join language old throw lot responsibility suddenly.",  
      "addressLocality": "Inside born clear run budget about green. Certainly baby under budget wonder.",  
      "addressRegion": "Purpose take tonight themselves foot maybe foreign. Administration enjoy tonight research five. City defense recently responsibility.",  
      "addressCountry": "Hope item civil. Population total carry today purpose significant rock. Pretty truth simply huge.",  
      "postalCode": "Cold that again including create. Upon recent pattern choose require message when reduce. Factor of",  
      "postOfficeBoxNumber": "Charge agree message edge main ",  
      "streetNr": "Everything same unit rule imagine option responsibility. Around out future almost some throw. Central president close work a",  
      "district": "Society white card region much specific. Without pretty my various price resource program quite."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Build positive decide listen behind city. Employee exactly nothing material. Ball window mention phone state concern."  
  },  
  "type": "MaximumSpeedAndCantDeficiency",  
  "vehicleTypeMaximumCantDeficiency": {  
    "type": "Property",  
    "value": 615  
  },  
  "vehicleTypeMaximumSpeed": {  
    "type": "Property",  
    "value": 988  
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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  

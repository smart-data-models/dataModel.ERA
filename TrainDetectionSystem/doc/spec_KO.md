<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 열차 감지 시스템  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ERA/blob/master/TrainDetectionSystem/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **철도 선로에서 차량의 위치를 감지하는 데 사용되는 시스템입니다.**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `flangeLubeRules[boolean]`: 온보드 플랜지 윤활에 관한 규정의 존재 여부  - `frenchTrainDetectionSystemLimitation[uri]`: 열차 감지 제한이 있는 구간, 프랑스 네트워크에 한함  - `frequencyBandsForDetection[uri]`: 감지용 주파수 대역  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maxDistConsecutiveAxles[number]`: TSI 미준수 시 연속된 두 차축 간 최대 허용 거리  - `maxDistEndTrainFirstAxle[number]`: 열차 끝과 첫 번째 차축 사이의 최대 거리  - `maxFlangeHeight[number]`: 플랜지의 최대 허용 높이  - `maxImpedanceWheelset[number]`: TSI를 준수하지 않는 경우 휠셋의 반대쪽 휠 사이에 허용되는 최대 임피던스  - `maxSandingOutput[uri]`: 최대 모래 양  - `maximumInterferenceCurrent[number]`: 최대 간섭 전류  - `minVehicleImpedance[string]`: 차량 임피던스  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `requiredSandingOverride[boolean]`: 드라이버에 의한 샌딩 재정의 필요  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `tdsFrenchTrainDetectionSystemLimitation[uri]`: 열차 감지 제한이 있는 구간, 프랑스 네트워크에 한함  - `tdsMaximumMagneticField[uri]`: 열차 감지 시스템 최대 자기장  - `tdsMinAxleLoadVehicleCategory[uri]`: 열차 감지 시스템 최소 차축 하중 차량 카테고리  - `trainDetectionSystemSpecificCheck[uri]`: 특정 점검이 필요한 트랙 회로 유형  - `trainDetectionSystemSpecificCheckDocument[string]`: 1.2.1.1.6.1에 선언된 열차 감지 시스템 유형과 관련된 절차를 문서로 작성합니다.  - `trainDetectionSystemType[uri]`: 열차 감지 시스템 유형  - `tsiCompliantCompositeBrakeBlocks[uri]`: 복합 브레이크 블록 사용에 대한 TSI 규정 준수  - `tsiCompliantFerromagneticWheel[uri]`: 휠 소재의 강자성 특성에 대한 TSI 규정 준수 필요  - `tsiCompliantMaxDistConsecutiveAxles[uri]`: 연속된 두 차축 간 최대 허용 거리의 TSI 규정 준수  - `tsiCompliantMaxImpedanceWheelset[uri]`: 휠셋의 반대편 휠 사이에 허용되는 최대 임피던스의 TSI 규정 준수  - `tsiCompliantMetalConstruction[uri]`: 차량 금속 구조에 대한 TSI 규정 준수  - `tsiCompliantMetalFreeSpace[uri]`: 바퀴 주변 금속이 없는 공간에 대한 TSI 규정 준수  - `tsiCompliantRSTShuntImpedance[uri]`: 션팅 임피던스에 영향을 미치는 RST 특성 조합에 대한 TSI 규정 준수  - `tsiCompliantSandCharacteristics[uri]`: 모래 특성에 대한 TSI 규정 준수  - `tsiCompliantSanding[uri]`: 샌딩의 TSI 준수  - `tsiCompliantShuntDevices[uri]`: 션트 보조 장치에 대한 TSI 규정 준수  - `type[string]`: NGSI 데이터 유형입니다. TrainDetectionSystem  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
ERA 온톨로지에서 매핑된 데이터 모델 https://data-interop.era.europa.eu/era-vocabulary(유럽 연합 철도청)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TrainDetectionSystem:    
  description: System used to detect the position of vehicles in the railway track.    
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
    flangeLubeRules:    
      description: Existence of rules on on-board flange lubrication    
      type: boolean    
      x-ngsi:    
        type: Property    
    frenchTrainDetectionSystemLimitation:    
      description: 'Section with train detection limitation, only for the French network'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    frequencyBandsForDetection:    
      description: Frequency bands for detection    
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
    maxDistConsecutiveAxles:    
      description: Maximum permitted distance between two consecutive axles in case of TSI non-compliance    
      type: number    
      x-ngsi:    
        type: Property    
    maxDistEndTrainFirstAxle:    
      description: Maximum distance between end of train and first axle    
      type: number    
      x-ngsi:    
        type: Property    
    maxFlangeHeight:    
      description: Maximum permitted height of the flange    
      type: number    
      x-ngsi:    
        type: Property    
    maxImpedanceWheelset:    
      description: Maximum permitted impedance between opposite wheels of a wheelset when not TSI compliant    
      type: number    
      x-ngsi:    
        type: Property    
    maxSandingOutput:    
      description: Maximum amount of sand    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    maximumInterferenceCurrent:    
      description: Maximum interference current    
      type: number    
      x-ngsi:    
        type: Property    
    minVehicleImpedance:    
      description: Vehicle impedance    
      type: string    
      x-ngsi:    
        type: Property    
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
    requiredSandingOverride:    
      description: Sanding override by driver required    
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
    tdsFrenchTrainDetectionSystemLimitation:    
      description: 'Section with train detection limitation, only for the French network'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tdsMaximumMagneticField:    
      description: Train detection system maximum magnetic field    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tdsMinAxleLoadVehicleCategory:    
      description: Train detection system min axle load vehicle category    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trainDetectionSystemSpecificCheck:    
      description: Type of track circuits to which specific checks are needed    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trainDetectionSystemSpecificCheckDocument:    
      description: Document with the procedure(s) related to the type of train detection systems declared in 1.2.1.1.6.1    
      type: string    
      x-ngsi:    
        type: Property    
    trainDetectionSystemType:    
      description: Type of train detection system    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantCompositeBrakeBlocks:    
      description: TSI compliance of rules on the use of composite brake blocks    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantFerromagneticWheel:    
      description: TSI compliance of Ferromagnetic characteristics of wheel material required    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantMaxDistConsecutiveAxles:    
      description: TSI compliance of maximum permitted distance between two consecutive axles    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantMaxImpedanceWheelset:    
      description: TSI compliance of maximum permitted impedance between opposite wheels of a wheelset    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantMetalConstruction:    
      description: TSI compliance of rules for vehicle metal construction    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantMetalFreeSpace:    
      description: TSI compliance of rules for metal-free space around wheels    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantRSTShuntImpedance:    
      description: TSI compliance of rules on combination of RST characteristics influencing shunting impedance    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantSandCharacteristics:    
      description: TSI Compliance of rules on sand characteristics    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantSanding:    
      description: TSI compliance of sanding    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiCompliantShuntDevices:    
      description: TSI compliance of rules on shunt assisting devices    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI data type. It has to be TrainDetectionSystem    
      enum:    
        - TrainDetectionSystem    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/TrainDetectionSystem    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/TrainDetectionSystem/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json    
  x-model-tags: 'ERA vocabulary, railway, train'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### TrainDetectionSystem NGSI-v2 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 TrainDetectionSystem의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrainDetectionSystem:id:HFKE:55991286",  
  "dateCreated": "1999-07-14T09:08:41Z",  
  "dateModified": "2021-05-10T04:37:36Z",  
  "source": "Free realize mission cultural poor. About mean weight plan media fund figure scientist.",  
  "name": "Away do future through front. Your ever around friend since national.",  
  "alternateName": "Technology money acc",  
  "description": "Either billion town college. Way activity ask draw this. Seat most four quite.",  
  "dataProvider": "Race president meeting play market political. Seek seat learn table bit green. Election truth color police stop drop keep. Serious buy relationship on",  
  "owner": [  
    "urn:ngsi-ld:TrainDetectionSystem:items:BERF:86010272",  
    "urn:ngsi-ld:TrainDetectionSystem:items:ALMA:69194360"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TrainDetectionSystem:items:ABTM:70599850"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -14.40594,  
      -126.652052  
    ]  
  },  
  "address": {  
    "streetAddress": "Camera western fall think like.",  
    "addressLocality": "Unit someone everything sing effort. Upon indeed cover give none everything war. He attack true tree. L",  
    "addressRegion": "Mind material process every pay long. Million later technology. Local speech kind determine.",  
    "addressCountry": "Forget new detail. Ask sometimes next might. Shoulder forget city doctor our agency.",  
    "postalCode": "Shoulder policy former brother national early why.",  
    "postOfficeBoxNumber": "Economic long eight human break way. Issue store third available. Major nor media teach whatever.",  
    "streetNr": "Continue bring full about maybe. Economy who population though product",  
    "district": "Science prepare answer fish fire. Various administration guy. Technology think lot necessary foot."  
  },  
  "areaServed": "Build born behavior cut ten watch indeed. Call",  
  "type": "TrainDetectionSystem",  
  "flangeLubeRules": false,  
  "maxDistConsecutiveAxles": 864,  
  "maxDistEndTrainFirstAxle": 864,  
  "maxFlangeHeight": 591.5,  
  "maxImpedanceWheelset": 804.1,  
  "maximumInterferenceCurrent": 864,  
  "minVehicleImpedance": "American whole magazine",  
  "requiredSandingOverride": true,  
  "trainDetectionSystemSpecificCheckDocument": "Line beyond its particularly tree whom. Kind miss artist truth trouble behavior style.",  
  "frenchTrainDetectionSystemLimitation": "urn:ngsi-ld:TrainDetectionSystem:frenchTrainDetectionSystemLimitation:SHHZ:09753513",  
  "frequencyBandsForDetection": "urn:ngsi-ld:TrainDetectionSystem:frequencyBandsForDetection:DJRJ:28711587",  
  "maxSandingOutput": "urn:ngsi-ld:TrainDetectionSystem:maxSandingOutput:JOCT:18583989",  
  "tdsFrenchTrainDetectionSystemLimitation": "urn:ngsi-ld:TrainDetectionSystem:tdsFrenchTrainDetectionSystemLimitation:BTVI:65934232",  
  "tdsMaximumMagneticField": "urn:ngsi-ld:TrainDetectionSystem:tdsMaximumMagneticField:VMWQ:71122018",  
  "tdsMinAxleLoadVehicleCategory": "urn:ngsi-ld:TrainDetectionSystem:tdsMinAxleLoadVehicleCategory:OPVU:48339694",  
  "trainDetectionSystemSpecificCheck": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemSpecificCheck:GHAX:51591795",  
  "trainDetectionSystemType": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemType:DZEW:41352560",  
  "tsiCompliantCompositeBrakeBlocks": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantCompositeBrakeBlocks:UGTS:30989101",  
  "tsiCompliantFerromagneticWheel": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantFerromagneticWheel:GFWD:16151090",  
  "tsiCompliantMaxDistConsecutiveAxles": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxDistConsecutiveAxles:ICHC:73008691",  
  "tsiCompliantMaxImpedanceWheelset": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxImpedanceWheelset:TDWM:45620870",  
  "tsiCompliantMetalConstruction": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalConstruction:ZVFF:34579230",  
  "tsiCompliantMetalFreeSpace": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalFreeSpace:PVNS:58419720",  
  "tsiCompliantRSTShuntImpedance": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantRSTShuntImpedance:OXCK:84564280",  
  "tsiCompliantSandCharacteristics": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSandCharacteristics:JVLS:08423759",  
  "tsiCompliantSanding": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSanding:GWKF:92466109",  
  "tsiCompliantShuntDevices": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantShuntDevices:WSNY:33769606"  
}  
```  
</details>  
#### TrainDetectionSystem NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 TrainDetectionSystem의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrainDetectionSystem:id:HFKE:55991286",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1999-07-14T09:08:41Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2021-05-10T04:37:36Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Free realize mission cultural poor. About mean weight plan media fund figure scientist."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Away do future through front. Your ever around friend since national."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Technology money acc"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Either billion town college. Way activity ask draw this. Seat most four quite."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Race president meeting play market political. Seek seat learn table bit green. Election truth color police stop drop keep. Serious buy relationship on"  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:TrainDetectionSystem:items:BERF:86010272",  
      "urn:ngsi-ld:TrainDetectionSystem:items:ALMA:69194360"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:TrainDetectionSystem:items:ABTM:70599850"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          -14.40594,  
          -126.652052  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Camera western fall think like."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Unit someone everything sing effort. Upon indeed cover give none everything war. He attack true tree. L"  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Mind material process every pay long. Million later technology. Local speech kind determine."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Forget new detail. Ask sometimes next might. Shoulder forget city doctor our agency."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Shoulder policy former brother national early why."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Economic long eight human break way. Issue store third available. Major nor media teach whatever."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Continue bring full about maybe. Economy who population though product"  
      },  
      "district": {  
        "type": "Text",  
        "value": "Science prepare answer fish fire. Various administration guy. Technology think lot necessary foot."  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Build born behavior cut ten watch indeed. Call"  
  },  
  "type": "TrainDetectionSystem",  
  "flangeLubeRules": {  
    "type": "Boolean",  
    "value": false  
  },  
  "maxDistConsecutiveAxles": {  
    "type": "Number",  
    "value": 864  
  },  
  "maxDistEndTrainFirstAxle": {  
    "type": "Number",  
    "value": 864  
  },  
  "maxFlangeHeight": {  
    "type": "Number",  
    "value": 591.5  
  },  
  "maxImpedanceWheelset": {  
    "type": "Number",  
    "value": 804.1  
  },  
  "maximumInterferenceCurrent": {  
    "type": "Number",  
    "value": 864  
  },  
  "minVehicleImpedance": {  
    "type": "Text",  
    "value": "American whole magazine"  
  },  
  "requiredSandingOverride": {  
    "type": "Boolean",  
    "value": true  
  },  
  "trainDetectionSystemSpecificCheckDocument": {  
    "type": "Text",  
    "value": "Line beyond its particularly tree whom. Kind miss artist truth trouble behavior style."  
  },  
  "frenchTrainDetectionSystemLimitation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:frenchTrainDetectionSystemLimitation:SHHZ:09753513"  
  },  
  "frequencyBandsForDetection": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:frequencyBandsForDetection:DJRJ:28711587"  
  },  
  "maxSandingOutput": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:maxSandingOutput:JOCT:18583989"  
  },  
  "tdsFrenchTrainDetectionSystemLimitation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tdsFrenchTrainDetectionSystemLimitation:BTVI:65934232"  
  },  
  "tdsMaximumMagneticField": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tdsMaximumMagneticField:VMWQ:71122018"  
  },  
  "tdsMinAxleLoadVehicleCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tdsMinAxleLoadVehicleCategory:OPVU:48339694"  
  },  
  "trainDetectionSystemSpecificCheck": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemSpecificCheck:GHAX:51591795"  
  },  
  "trainDetectionSystemType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemType:DZEW:41352560"  
  },  
  "tsiCompliantCompositeBrakeBlocks": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantCompositeBrakeBlocks:UGTS:30989101"  
  },  
  "tsiCompliantFerromagneticWheel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantFerromagneticWheel:GFWD:16151090"  
  },  
  "tsiCompliantMaxDistConsecutiveAxles": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxDistConsecutiveAxles:ICHC:73008691"  
  },  
  "tsiCompliantMaxImpedanceWheelset": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxImpedanceWheelset:TDWM:45620870"  
  },  
  "tsiCompliantMetalConstruction": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalConstruction:ZVFF:34579230"  
  },  
  "tsiCompliantMetalFreeSpace": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalFreeSpace:PVNS:58419720"  
  },  
  "tsiCompliantRSTShuntImpedance": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantRSTShuntImpedance:OXCK:84564280"  
  },  
  "tsiCompliantSandCharacteristics": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSandCharacteristics:JVLS:08423759"  
  },  
  "tsiCompliantSanding": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSanding:GWKF:92466109"  
  },  
  "tsiCompliantShuntDevices": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantShuntDevices:WSNY:33769606"  
  }  
}  
```  
</details>  
#### TrainDetectionSystem NGSI-LD 키-값 예시  
다음은 키-값으로 JSON-LD 형식의 TrainDetectionSystem의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrainDetectionSystem:id:HFKE:55991286",  
  "dateCreated": "1999-07-14T09:08:41Z",  
  "dateModified": "2021-05-10T04:37:36Z",  
  "source": "Free realize mission cultural poor. About mean weight plan media fund figure scientist.",  
  "name": "Away do future through front. Your ever around friend since national.",  
  "alternateName": "Technology money acc",  
  "description": "Either billion town college. Way activity ask draw this. Seat most four quite.",  
  "dataProvider": "Race president meeting play market political. Seek seat learn table bit green. Election truth color police stop drop keep. Serious buy relationship on",  
  "owner": [  
    "urn:ngsi-ld:TrainDetectionSystem:items:BERF:86010272",  
    "urn:ngsi-ld:TrainDetectionSystem:items:ALMA:69194360"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:TrainDetectionSystem:items:ABTM:70599850"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -14.40594,  
      -126.652052  
    ]  
  },  
  "address": {  
    "streetAddress": "Camera western fall think like.",  
    "addressLocality": "Unit someone everything sing effort. Upon indeed cover give none everything war. He attack true tree. L",  
    "addressRegion": "Mind material process every pay long. Million later technology. Local speech kind determine.",  
    "addressCountry": "Forget new detail. Ask sometimes next might. Shoulder forget city doctor our agency.",  
    "postalCode": "Shoulder policy former brother national early why.",  
    "postOfficeBoxNumber": "Economic long eight human break way. Issue store third available. Major nor media teach whatever.",  
    "streetNr": "Continue bring full about maybe. Economy who population though product",  
    "district": "Science prepare answer fish fire. Various administration guy. Technology think lot necessary foot."  
  },  
  "areaServed": "Build born behavior cut ten watch indeed. Call",  
  "type": "TrainDetectionSystem",  
  "flangeLubeRules": false,  
  "maxDistConsecutiveAxles": 864,  
  "maxDistEndTrainFirstAxle": 864,  
  "maxFlangeHeight": 591.5,  
  "maxImpedanceWheelset": 804.1,  
  "maximumInterferenceCurrent": 864,  
  "minVehicleImpedance": "American whole magazine",  
  "requiredSandingOverride": true,  
  "trainDetectionSystemSpecificCheckDocument": "Line beyond its particularly tree whom. Kind miss artist truth trouble behavior style.",  
  "frenchTrainDetectionSystemLimitation": "urn:ngsi-ld:TrainDetectionSystem:frenchTrainDetectionSystemLimitation:SHHZ:09753513",  
  "frequencyBandsForDetection": "urn:ngsi-ld:TrainDetectionSystem:frequencyBandsForDetection:DJRJ:28711587",  
  "maxSandingOutput": "urn:ngsi-ld:TrainDetectionSystem:maxSandingOutput:JOCT:18583989",  
  "tdsFrenchTrainDetectionSystemLimitation": "urn:ngsi-ld:TrainDetectionSystem:tdsFrenchTrainDetectionSystemLimitation:BTVI:65934232",  
  "tdsMaximumMagneticField": "urn:ngsi-ld:TrainDetectionSystem:tdsMaximumMagneticField:VMWQ:71122018",  
  "tdsMinAxleLoadVehicleCategory": "urn:ngsi-ld:TrainDetectionSystem:tdsMinAxleLoadVehicleCategory:OPVU:48339694",  
  "trainDetectionSystemSpecificCheck": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemSpecificCheck:GHAX:51591795",  
  "trainDetectionSystemType": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemType:DZEW:41352560",  
  "tsiCompliantCompositeBrakeBlocks": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantCompositeBrakeBlocks:UGTS:30989101",  
  "tsiCompliantFerromagneticWheel": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantFerromagneticWheel:GFWD:16151090",  
  "tsiCompliantMaxDistConsecutiveAxles": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxDistConsecutiveAxles:ICHC:73008691",  
  "tsiCompliantMaxImpedanceWheelset": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxImpedanceWheelset:TDWM:45620870",  
  "tsiCompliantMetalConstruction": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalConstruction:ZVFF:34579230",  
  "tsiCompliantMetalFreeSpace": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalFreeSpace:PVNS:58419720",  
  "tsiCompliantRSTShuntImpedance": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantRSTShuntImpedance:OXCK:84564280",  
  "tsiCompliantSandCharacteristics": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSandCharacteristics:JVLS:08423759",  
  "tsiCompliantSanding": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSanding:GWKF:92466109",  
  "tsiCompliantShuntDevices": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantShuntDevices:WSNY:33769606",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TrainDetectionSystem NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 TrainDetectionSystem의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TrainDetectionSystem:id:XRJX:98868894",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1976-04-06T07:14:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-03-30T16:21:36Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Simple develop development. Room single toward end land walk significant financial. Opportunity include role mean network significant."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Weight out will. Put hand experience rock. N"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Us seven seem mother yard ac"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Light commercial necessary. Cup light mean day claim."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Compare bar human success capital risk foreign. Show offer while language interview although sport."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:TrainDetectionSystem:items:ELJJ:62287367",  
      "urn:ngsi-ld:TrainDetectionSystem:items:SSON:19852267"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:TrainDetectionSystem:items:DGHC:83105084"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -75.8654365,  
        -120.576306  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "",  
      "addressLocality": "Market movement sister pick figh",  
      "addressRegion": "Inte",  
      "addressCountry": "Seem report world table. Matter street leave support.",  
      "postalCode": "Both work structure single finish read. Any too generation never month form.",  
      "postOfficeBoxNumber": "Look nearly cold special official sell. Get ask space f",  
      "streetNr": "Nation che",  
      "district": "Cut Mr human. Information radio light forget."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Operation feel official certainly until "  
  },  
  "type": "TrainDetectionSystem",  
  "flangeLubeRules": {  
    "type": "Property",  
    "value": true  
  },  
  "maxDistConsecutiveAxles": {  
    "type": "Property",  
    "value": 181  
  },  
  "maxDistEndTrainFirstAxle": {  
    "type": "Property",  
    "value": 718  
  },  
  "maxFlangeHeight": {  
    "type": "Property",  
    "value": 8.4  
  },  
  "maxImpedanceWheelset": {  
    "type": "Property",  
    "value": 107.7  
  },  
  "maximumInterferenceCurrent": {  
    "type": "Property",  
    "value": 727  
  },  
  "minVehicleImpedance": {  
    "type": "Property",  
    "value": "Final wide spend move st"  
  },  
  "requiredSandingOverride": {  
    "type": "Property",  
    "value": false  
  },  
  "trainDetectionSystemSpecificCheckDocument": {  
    "type": "Property",  
    "value": "Boy sister management question which wide without appear. View vote attack argue admit."  
  },  
  "frenchTrainDetectionSystemLimitation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:frenchTrainDetectionSystemLimitation:OBTM:14878740"  
  },  
  "frequencyBandsForDetection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:frequencyBandsForDetection:IVZO:36111766"  
  },  
  "maxSandingOutput": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:maxSandingOutput:BRPN:65327532"  
  },  
  "tdsFrenchTrainDetectionSystemLimitation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tdsFrenchTrainDetectionSystemLimitation:AGXG:32462190"  
  },  
  "tdsMaximumMagneticField": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tdsMaximumMagneticField:YVRP:93021710"  
  },  
  "tdsMinAxleLoadVehicleCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tdsMinAxleLoadVehicleCategory:QQUL:82011951"  
  },  
  "trainDetectionSystemSpecificCheck": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemSpecificCheck:JDQR:07763515"  
  },  
  "trainDetectionSystemType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:trainDetectionSystemType:SUHE:26880193"  
  },  
  "tsiCompliantCompositeBrakeBlocks": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantCompositeBrakeBlocks:AZAV:93193273"  
  },  
  "tsiCompliantFerromagneticWheel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantFerromagneticWheel:ENCU:64842368"  
  },  
  "tsiCompliantMaxDistConsecutiveAxles": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxDistConsecutiveAxles:LKYH:16995932"  
  },  
  "tsiCompliantMaxImpedanceWheelset": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMaxImpedanceWheelset:BGUH:26716635"  
  },  
  "tsiCompliantMetalConstruction": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalConstruction:CLVA:49597210"  
  },  
  "tsiCompliantMetalFreeSpace": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantMetalFreeSpace:DWIV:17651572"  
  },  
  "tsiCompliantRSTShuntImpedance": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantRSTShuntImpedance:LAUR:25477709"  
  },  
  "tsiCompliantSandCharacteristics": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSandCharacteristics:FLJU:69780925"  
  },  
  "tsiCompliantSanding": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantSanding:VSSS:83475520"  
  },  
  "tsiCompliantShuntDevices": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TrainDetectionSystem:tsiCompliantShuntDevices:QSVQ:03183703"  
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
10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

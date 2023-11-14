<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：训练检测系统  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/TrainDetectionSystem/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**用于探测铁轨上车辆位置的**系统。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `flangeLubeRules[boolean]`: 机载法兰润滑规则的存在  - `frenchTrainDetectionSystemLimitation[uri]`: 有列车检测限制的部分，仅适用于法国网络  - `frequencyBandsForDetection[uri]`: 探测频段  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxDistConsecutiveAxles[number]`: 在不符合 TSI 标准的情况下，两个连续车轴之间的最大允许距离  - `maxDistEndTrainFirstAxle[number]`: 列车末端与第一车轴之间的最大距离  - `maxFlangeHeight[number]`: 法兰允许的最大高度  - `maxImpedanceWheelset[number]`: 不符合 TSI 标准时，轮对之间的最大允许阻抗  - `maxSandingOutput[uri]`: 最大含沙量  - `maximumInterferenceCurrent[number]`: 最大干扰电流  - `minVehicleImpedance[string]`: 车辆阻抗  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `requiredSandingOverride[boolean]`: 需要由驾驶员控制打磨  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `tdsFrenchTrainDetectionSystemLimitation[uri]`: 有列车检测限制的部分，仅适用于法国网络  - `tdsMaximumMagneticField[uri]`: 列车探测系统最大磁场  - `tdsMinAxleLoadVehicleCategory[uri]`: 列车探测系统 最小轴载 车辆类别  - `trainDetectionSystemSpecificCheck[uri]`: 需要进行特定检查的轨道电路类型  - `trainDetectionSystemSpecificCheckDocument[string]`: 与 1.2.1.1.6.1 中申报的列车探测系统类型相关的程序文件  - `trainDetectionSystemType[uri]`: 列车探测系统类型  - `tsiCompliantCompositeBrakeBlocks[uri]`: TSI 符合使用复合制动块的规定  - `tsiCompliantFerromagneticWheel[uri]`: 要求车轮材料的铁磁特性符合 TSI 标准  - `tsiCompliantMaxDistConsecutiveAxles[uri]`: 符合 TSI 规定的两个连续车轴之间的最大允许距离  - `tsiCompliantMaxImpedanceWheelset[uri]`: 轮对之间最大允许阻抗的 TSI 合规性  - `tsiCompliantMetalConstruction[uri]`: TSI 符合车辆金属结构规则  - `tsiCompliantMetalFreeSpace[uri]`: 符合 TSI 关于车轮周围无金属空间的规定  - `tsiCompliantRSTShuntImpedance[uri]`: TSI 符合影响分流阻抗的 RST 特性组合规则  - `tsiCompliantSandCharacteristics[uri]`: TSI 遵守有关沙子特性的规定  - `tsiCompliantSanding[uri]`: 打磨符合 TSI 标准  - `tsiCompliantShuntDevices[uri]`: TSI 遵守分流辅助装置规则的情况  - `type[string]`: NGSI 数据类型。必须是 TrainDetectionSystem  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
从 ERA 本体映射的数据模型 https://data-interop.era.europa.eu/era-vocabulary（欧盟铁路局）  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
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
## 有效载荷示例  
#### TrainDetectionSystem NGSI-v2 key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 TrainDetectionSystem 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### TrainDetectionSystem NGSI-v2 标准化示例  
下面是一个以 JSON-LD 格式规范化的 TrainDetectionSystem 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### TrainDetectionSystem NGSI-LD key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 TrainDetectionSystem 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### TrainDetectionSystem NGSI-LD 归一化示例  
下面是一个以 JSON-LD 格式规范化的 TrainDetectionSystem 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

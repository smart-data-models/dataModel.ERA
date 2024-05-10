<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

实体：车辆类型    
=======
<!-- /10-Header -->
    
<!-- 15-License -->
    

[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/VehicleType/LICENSE.md)    

[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

全球描述：**获准在欧盟铁路基础设施上运行的车辆类型。    

版本： 0.0.1    
<!-- /20-Description -->
    
<!-- 30-PropertiesList -->
    

## 属性列表    

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理      
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 标识公共街道上特定房产的编号      
- `alternateName[string]`: 该项目的替代名称  
- `alternativeName[string]`: 替代名称  
- `altitudeRange[string]`: 高度范围  
- `altitudeRangeDetail[number]`: 高度范围详情  
- `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)
- `authorizedCountry[uri]`: 授权国家  
- `axleBearingConditionMonitoring[uri]`: 车轴轴承状态监测  
- `axleSpacing[string]`: 车轴间距  
- `boardingAids[string]`: 登机辅助工具  
- `brakeWeightPercentage[string]`: 制动重量百分比  
- `cantDefficiency[number]`: Cant defficiency  
- `category[uri]`: 车辆类别  
- `catenaryMaxRatedCurrent[number]`: 导管最大额定电流  
- `certificate[uri]`: 证书  
- `conditionsTrainFormation[string]`: 列车编组条件  
- `contactStripMaterial[uri]`: 允许使用的接触带材料  
- `dangerousGoodsTankCode[string]`: 危险品罐编码  
- `dataGSMRNetwork[uri]`: 数据 GSM-R 网络  
- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  
- `dataRadioCompatible[uri]`: 无线电系统兼容性数据  
- `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  
- `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  
- `description[string]`: 项目描述  
- `designMassExceptionalPayload[number]`: 特殊有效载荷下的设计质量  
- `designMassNormalPayload[number]`: 正常有效载荷下的设计质量  
- `designMassWorkingOrder[number]`: 设计质量正常  
- `drivingCabs[number]`: 驾驶出租车  
- `eddyCurrentBrakePrevention[boolean]`: 防止涡流制动  
- `eddyCurrentBrakingFitted[boolean]`: 已安装涡流制动装置  
- `emergencyBrake[string]`: 紧急制动  
- `endCouplingType[uri]`: 端部联轴器类型  
- `energyMeterInstalled[boolean]`: 安装能源计量表  
- `energySupplyMaxPower[number]`: 能源供应最大功率  
- `energySupplySystem[uri]`: 能源供应系统  
- `etcsBaseline[uri]`: ETCS 基线  
- `etcsDataCommApp[string]`: ETCS 数据通信应用  
- `etcsEquipmentOnBoardLevel[uri]`: ETCS 设备级别  
- `etcsInfill[uri]`: 线路侧安装的 ETCS 填充物  
- `etcsNationalApplications[string]`: ETCS 国家应用  
- `etcsOnBoardImplementation[string]`: ETCS 车载实施  
- `etcsSystemCompatibility[uri]`: ETCS 系统兼容性  
- `ferromagneticWheelMaterial[boolean]`: 铁磁轮材料  
- `fireSafetyCategory[uri]`: 消防安全类别  
- `fixedSeats[string]`: 固定座位  
- `flangeLubricationFitted[boolean]`: 安装了法兰润滑装置  
- `gaugingProfile[uri]`: 测量  
- `gsmRRadioDataCommunication[uri]`: GSM-R 无线电数据通信  
- `gsmRSetsInDrivingCab[number]`: 驾驶室内的 GSM-R 套件  
- `gsmRVersion[uri]`: GSM-R 版本  
- `hasAutomaticDroppingDevice[boolean]`: 具有自动投放装置  
- `hasCantDefficiencyCompensation[boolean]`: 有食堂效率补偿  
- `hasCurrentLimitation[boolean]`: 有电流限制  
- `hasLubricationDevicePrevention[boolean]`: 具有防止润滑装置  
- `hasParkingBrake[boolean]`: 有驻车制动器  
- `hasRegenerativeBrake[boolean]`: 再生制动许可  
- `hasSandingPrevention[boolean]`: 具有防打磨功能  
- `hasShuntingRestrictions[boolean]`: 有分流限制  
- `hasTrainIntegrityConfirmation[boolean]`: 具有列车完整性确认功能  
- `hasWheelSlideProtectionSystem[boolean]`: 具有车轮滑动保护系统  
- `id[*]`: 实体的唯一标识符  
- `legacyRadioSystem[uri]`: 已安装的其他无线电系统（无线电遗留系统）  
- `letterMarking[string]`: 字母标识  
- `loadingPlatformHeight[number]`: 装载平台高度  
- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  
- `magneticBrakePrevention[boolean]`: 磁制动预防  
- `magneticBrakingFitted[boolean]`: 已安装磁性制动器  
- `manufacturer[uri]`: 制造商  
- `manufacturingCountry[uri]`: 制造业国家  
- `massPerWheel[number]`: 每个轮子的质量  
- `maxCurrentStandstillPantograph[number]`: 每个受电弓静止时的最大电流  
- `maxDistConsecutiveAxles[number]`: 在不符合 TSI 标准的情况下，两个连续车轴之间的最大允许距离  
- `maxFlangeHeight[number]`: 法兰允许的最大高度  
- `maxImpedanceWheelset[number]`: 不符合 TSI 标准时，轮对之间的最大允许阻抗  
- `maxLengthVehicleNose[number]`: 车头最大长度  
- `maximumAverageDeceleration[number]`: 最大平均减速度  
- `maximumBrakeThermalEnergyCapacity[number]`: 最大制动热能容量  
- `maximumContactWireHeight[number]`: 最大接触线高度  
- `maximumDesignSpeed[number]`: 最大设计速度  
- `maximumLocomotivesCoupled[number]`: 最大连接机车数  
- `maximumServiceBrake[string]`: 最大服务中断时间  
- `maximumSpeedAndCantDeficiency[string]`: 最大速度和转弯半径不足  
- `maximumSpeedEmpty[number]`: 最大空载速度  
- `maximumTemperature[number]`: 温度范围（最大值）  
- `meetsRequirementVehicleAuthorisation[string]`: 符合要求的车辆授权  
- `minAxleLoad[number]`: 最小允许轴载  
- `minDistConsecutiveAxles[number]`: 两个连续车轴之间的最小允许距离  
- `minDistFirstLastAxle[number]`: 第一轴和最后轴之间的最小允许距离  
- `minFlangeHeight[number]`: 法兰允许的最小高度  
- `minFlangeThickness[number]`: 法兰允许的最小厚度  
- `minRimWidth[number]`: 轮辋最小允许宽度  
- `minVehicleImpedance[string]`: 车辆阻抗  
- `minWheelDiameter[number]`: 允许的最小车轮直径  
- `minimumConcaveVerticalRadius[number]`: 最小垂直凹面半径  
- `minimumContactWireHeight[number]`: 最小接触线高度  
- `minimumConvexVerticalRadius[number]`: 最小凸面垂直半径  
- `minimumHorizontalRadius[number]`: 水平曲线最小半径  
- `minimumTemperature[number]`: 温度范围（最小值）  
- `minimumWheelDiameter[number]`: 固定钝角交叉路口的最小车轮直径  
- `name[string]`: 该项目的名称  
- `nonCodedRestrictions[string]`: 无编码限制  
- `numberElementsRakeFreightWagons[number]`: 耙式货车数量  
- `numberOfPantographsInContactWithOCL[number]`: 与 OCL 接触的受电弓数量  
- `numberOfToilets[number]`: 厕所数量  
- `oclType[string]`: Ocl 类型  
- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  
- `parkingBrake[boolean]`: 驻车制动器  
- `parkingBrakeMandatory[boolean]`: 必须安装驻车制动器  
- `parkingBrakeMaximumGradient[number]`: 驻车制动器最大坡度  
- `parkingBrakeType[uri]`: 驻车制动器类型  
- `passByNoiseLevel[number]`: 通过噪声级  
- `permissiblePayload[string]`: 允许有效载荷  
- `portableBoardingAids[string]`: 便携式登船辅助设备  
- `preventRegenerativeBrakeUse[boolean]`: 防止使用再生制动  
- `previousVehicleType[uri]`: 以前的车辆类型  
- `prioritySeats[string]`: 优先席位  
- `prmAccessibleToilets[number]`: 无障碍厕所  
- `protectionLegacySystem[uri]`: 列车保护传统系统  
- `quasiStaticGuidingForce[number]`: 准静态引导力  
- `radioSwitchOverSpecialConditions[string]`: 无线电切换特殊条件  
- `railInclination[uri]`: 轨道倾斜度  
- `referencePassByNoiseLevel[boolean]`: 参考通过噪声级  
- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  
- `shortestDistanceBetweenPantographsInContactWithOCL[string]`: 与 OCL 接触的受电弓之间的最短距离  
- `sleepingPlaces[string]`: 睡眠场所  
- `snowIceHailConditions[uri]`: 冰雪冰雹条件  
- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  
- `startingNoiseLevel[number]`: 启动噪音水平  
- `staticAxleLoadExceptionalPayload[number]`: 特殊有效载荷下的静态轴载荷  
- `staticAxleLoadNormalPayload[number]`: 正常有效载荷下的静态轴载荷  
- `staticAxleLoadWorkingOrder[number]`: 工作状态下的静态轴荷  
- `stationaryNoiseLevel[number]`: 静态噪音水平  
- `structuralCategory[string]`: 结构类别  
- `subCategory[uri]`: 车辆子类别  
- `supportedPlatformHeight[uri]`: 支撑平台高度  
- `thermalCapacityDistance[number]`: 热容量距离  
- `thermalCapacityGradient[number]`: 热容量梯度  
- `thermalCapacitySpeed[number]`: 热容量 速度  
- `thermalCapacityTSIReference[uri]`: 热容量 TSI 参考  
- `thermalCapacityTime[number]`: 热容量时间  
- `totalVehicleMass[number]`: 车辆总质量  
- `trainControlSwitchOverSpecialConditions[string]`: 特殊条件下的列车控制开关  
- `trainDetectionSystemType[uri]`: 列车探测系统类型  
- `transportableOnFerry[boolean]`: 可通过渡轮运输  
- `type[string]`: NGSI 数据类型。必须是 VehicleType  
- `typeVersionId[uri]`: 类型版本 ID  
- `typeVersionNumber[string]`: 类型版本号  
- `usesGroup555[boolean]`: GSM-R 使用 555 组  
- `vehicleContactForce[number]`: 车辆接触力  
- `vehicleKinematicGaugeOther[string]`: 车辆运动测量仪 其他  
- `vehicleMaxSandingOutput[string]`: 车辆最大打磨输出功率  
- `vehiclePantographHead[string]`: 车辆受电弓头  
- `vehicleTypeMaximumSpeedAndCantDeficiency[uri]`: 车辆类型 最大速度和转弯半径  
- `vehiclesComposingFixedFormation[number]`: 组成固定编队的车辆  
- `voiceGSMRNetwork[uri]`: 语音 GSM-R 网络  
- `voiceOperationalCommImpl[string]`: 实施语音业务通信  
- `voiceRadioCompatible[uri]`: 无线电系统兼容语音  
- `wheelSetGauge[uri]`: 标称轨距  
- `wheelSetGaugeChangeoverFacility[uri]`: 轮对测量仪更换装置  
- `wheelSetGaugeTransformationMethod[string]`: 轮组轨距变换法  
- `wheelchairSleepingPlaces[string]`: 轮椅睡眠空间  
- `wheelchairSpaces[number]`: 轮椅空间  
<!-- /30-PropertiesList -->
    
<!-- 35-RequiredProperties -->
    

所需属性    
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
    
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
VehicleType:      
  description: A vehicle type that has been authorized to operate on the EU railway infrastructure.      
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
    alternativeName:      
      description: Alternative name      
      type: string      
      x-ngsi:      
        type: Property      
    altitudeRange:      
      description: Altitude range      
      type: string      
      x-ngsi:      
        type: Property      
    altitudeRangeDetail:      
      description: Altitude range detail      
      type: number      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    authorizedCountry:      
      description: Authorized country      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    axleBearingConditionMonitoring:      
      description: Axle bearing condition monitoring      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    axleSpacing:      
      description: Axle spacing      
      type: string      
      x-ngsi:      
        type: Property      
    boardingAids:      
      description: Boarding aids      
      type: string      
      x-ngsi:      
        type: Property      
    brakeWeightPercentage:      
      description: Brake weight percentage      
      type: string      
      x-ngsi:      
        type: Property      
    cantDefficiency:      
      description: Cant defficiency      
      type: number      
      x-ngsi:      
        type: Property      
    category:      
      description: Vehicle category      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    catenaryMaxRatedCurrent:      
      description: Catenary max rated current      
      type: number      
      x-ngsi:      
        type: Property      
    certificate:      
      description: Certificate      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    conditionsTrainFormation:      
      description: Conditions train formation      
      type: string      
      x-ngsi:      
        type: Property      
    contactStripMaterial:      
      description: Permitted contact strip material      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    dangerousGoodsTankCode:      
      description: Dangerous goods tank code      
      type: string      
      x-ngsi:      
        type: Property      
    dataGSMRNetwork:      
      description: Data GSM-R network      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dataRadioCompatible:      
      description: Radio system compatibility data      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    designMassExceptionalPayload:      
      description: Design mass under exceptional payload      
      type: number      
      x-ngsi:      
        type: Property      
    designMassNormalPayload:      
      description: Design mass under normal payload      
      type: number      
      x-ngsi:      
        type: Property      
    designMassWorkingOrder:      
      description: Design mass in working order      
      type: number      
      x-ngsi:      
        type: Property      
    drivingCabs:      
      description: Driving cabs      
      type: number      
      x-ngsi:      
        type: Property      
    eddyCurrentBrakePrevention:      
      description: Eddy current brake prevention      
      type: boolean      
      x-ngsi:      
        type: Property      
    eddyCurrentBrakingFitted:      
      description: Eddy current braking fitted      
      type: boolean      
      x-ngsi:      
        type: Property      
    emergencyBrake:      
      description: Emergency braking      
      type: string      
      x-ngsi:      
        type: Property      
    endCouplingType:      
      description: End coupling type      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    energyMeterInstalled:      
      description: Energy meter installed      
      type: boolean      
      x-ngsi:      
        type: Property      
    energySupplyMaxPower:      
      description: Energy supply max power      
      type: number      
      x-ngsi:      
        type: Property      
    energySupplySystem:      
      description: Energy supply system      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    etcsBaseline:      
      description: ETCS baseline      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    etcsDataCommApp:      
      description: ETCS data communication application      
      type: string      
      x-ngsi:      
        type: Property      
    etcsEquipmentOnBoardLevel:      
      description: ETCS equipment level      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    etcsInfill:      
      description: ETCS infill installed lineside      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    etcsNationalApplications:      
      description: ETCS national applications      
      type: string      
      x-ngsi:      
        type: Property      
    etcsOnBoardImplementation:      
      description: ETCS on-board implementation      
      type: string      
      x-ngsi:      
        type: Property      
    etcsSystemCompatibility:      
      description: ETCS system compatibility      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    ferromagneticWheelMaterial:      
      description: Ferromagnetic wheel material      
      type: boolean      
      x-ngsi:      
        type: Property      
    fireSafetyCategory:      
      description: Fire safety category      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    fixedSeats:      
      description: Fixed seats      
      type: string      
      x-ngsi:      
        type: Property      
    flangeLubricationFitted:      
      description: Flange lubrication fitted      
      type: boolean      
      x-ngsi:      
        type: Property      
    gaugingProfile:      
      description: Gauging      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    gsmRRadioDataCommunication:      
      description: GSM-R radio data communication      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    gsmRSetsInDrivingCab:      
      description: GSM-R sets in driving cab      
      type: number      
      x-ngsi:      
        type: Property      
    gsmRVersion:      
      description: GSM-R version      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    hasAutomaticDroppingDevice:      
      description: Has automatic dropping device      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasCantDefficiencyCompensation:      
      description: Has cant defficiency compensation      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasCurrentLimitation:      
      description: Has current limitation      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasLubricationDevicePrevention:      
      description: Has lubrication device prevention      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasParkingBrake:      
      description: Has parking brake      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasRegenerativeBrake:      
      description: Permission for regenerative braking      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasSandingPrevention:      
      description: Has sanding prevention      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasShuntingRestrictions:      
      description: Has shunting restrictions      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasTrainIntegrityConfirmation:      
      description: Has train integrity confirmation      
      type: boolean      
      x-ngsi:      
        type: Property      
    hasWheelSlideProtectionSystem:      
      description: Has wheel slide protection system      
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
    legacyRadioSystem:      
      description: Other radio systems installed (Radio Legacy Systems)      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    letterMarking:      
      description: Letter marking      
      type: string      
      x-ngsi:      
        type: Property      
    loadingPlatformHeight:      
      description: Loading platform height      
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
    magneticBrakePrevention:      
      description: Magnetic brake prevention      
      type: boolean      
      x-ngsi:      
        type: Property      
    magneticBrakingFitted:      
      description: Magnetic braking fitted      
      type: boolean      
      x-ngsi:      
        type: Property      
    manufacturer:      
      description: Manufacturer      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    manufacturingCountry:      
      description: Manufacturing country      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    massPerWheel:      
      description: Mass per wheel      
      type: number      
      x-ngsi:      
        type: Property      
    maxCurrentStandstillPantograph:      
      description: Maximum current at standstill per pantograph      
      type: number      
      x-ngsi:      
        type: Property      
    maxDistConsecutiveAxles:      
      description: Maximum permitted distance between two consecutive axles in case of TSI non-compliance      
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
    maxLengthVehicleNose:      
      description: Maximum length vehicle nose      
      type: number      
      x-ngsi:      
        type: Property      
    maximumAverageDeceleration:      
      description: Maximum average deceleration      
      type: number      
      x-ngsi:      
        type: Property      
    maximumBrakeThermalEnergyCapacity:      
      description: Maximum brake thermal energy capacity      
      type: number      
      x-ngsi:      
        type: Property      
    maximumContactWireHeight:      
      description: Maximum contact wire height      
      type: number      
      x-ngsi:      
        type: Property      
    maximumDesignSpeed:      
      description: Maximum design speed      
      type: number      
      x-ngsi:      
        type: Property      
    maximumLocomotivesCoupled:      
      description: Maximum locomotives coupled      
      type: number      
      x-ngsi:      
        type: Property      
    maximumServiceBrake:      
      description: Maximum service break      
      type: string      
      x-ngsi:      
        type: Property      
    maximumSpeedAndCantDeficiency:      
      description: Maximum speed and cant deficiency      
      type: string      
      x-ngsi:      
        type: Property      
    maximumSpeedEmpty:      
      description: Maximum speed empty      
      type: number      
      x-ngsi:      
        type: Property      
    maximumTemperature:      
      description: Temperature range (maximum)      
      type: number      
      x-ngsi:      
        type: Property      
    meetsRequirementVehicleAuthorisation:      
      description: Meets requirement vehicle authorization      
      type: string      
      x-ngsi:      
        type: Property      
    minAxleLoad:      
      description: Minimum permitted axle load      
      type: number      
      x-ngsi:      
        type: Property      
    minDistConsecutiveAxles:      
      description: Minimum permitted distance between two consecutive axles      
      type: number      
      x-ngsi:      
        type: Property      
    minDistFirstLastAxle:      
      description: Minimum permitted distance between first and last axle      
      type: number      
      x-ngsi:      
        type: Property      
    minFlangeHeight:      
      description: Minimum permitted height of the flange      
      type: number      
      x-ngsi:      
        type: Property      
    minFlangeThickness:      
      description: Minimum permitted thickness of the flange      
      type: number      
      x-ngsi:      
        type: Property      
    minRimWidth:      
      description: Minimum permitted width of the rim      
      type: number      
      x-ngsi:      
        type: Property      
    minVehicleImpedance:      
      description: Vehicle impedance      
      type: string      
      x-ngsi:      
        type: Property      
    minWheelDiameter:      
      description: Minimum permitted wheel diameter      
      type: number      
      x-ngsi:      
        type: Property      
    minimumConcaveVerticalRadius:      
      description: Minimum concave vertical radius      
      type: number      
      x-ngsi:      
        type: Property      
    minimumContactWireHeight:      
      description: Minimum contact wire height      
      type: number      
      x-ngsi:      
        type: Property      
    minimumConvexVerticalRadius:      
      description: Minimum convex vertical radius      
      type: number      
      x-ngsi:      
        type: Property      
    minimumHorizontalRadius:      
      description: Minimum radius of horizontal curve      
      type: number      
      x-ngsi:      
        type: Property      
    minimumTemperature:      
      description: Temperature range (minimum)      
      type: number      
      x-ngsi:      
        type: Property      
    minimumWheelDiameter:      
      description: Minimum wheel diameter for fixed obtuse crossings      
      type: number      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    nonCodedRestrictions:      
      description: Non coded restrictions      
      type: string      
      x-ngsi:      
        type: Property      
    numberElementsRakeFreightWagons:      
      description: Number elements rake freight wagons      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfPantographsInContactWithOCL:      
      description: Number of pantographs in contact with OCL      
      type: number      
      x-ngsi:      
        type: Property      
    numberOfToilets:      
      description: Number of toilets      
      type: number      
      x-ngsi:      
        type: Property      
    oclType:      
      description: Ocl type      
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
    parkingBrake:      
      description: Parking brake      
      type: boolean      
      x-ngsi:      
        type: Property      
    parkingBrakeMandatory:      
      description: Parking brake mandatory      
      type: boolean      
      x-ngsi:      
        type: Property      
    parkingBrakeMaximumGradient:      
      description: Parking brake maximum gradient      
      type: number      
      x-ngsi:      
        type: Property      
    parkingBrakeType:      
      description: Parking brake type      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    passByNoiseLevel:      
      description: Pass-by noise level      
      type: number      
      x-ngsi:      
        type: Property      
    permissiblePayload:      
      description: Permissible payload      
      type: string      
      x-ngsi:      
        type: Property      
    portableBoardingAids:      
      description: Portable boarding aids      
      type: string      
      x-ngsi:      
        type: Property      
    preventRegenerativeBrakeUse:      
      description: Prevent regenerative brake use      
      type: boolean      
      x-ngsi:      
        type: Property      
    previousVehicleType:      
      description: Previous vehicle type      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    prioritySeats:      
      description: Priority seats      
      type: string      
      x-ngsi:      
        type: Property      
    prmAccessibleToilets:      
      description: Prm accessible toilets      
      type: number      
      x-ngsi:      
        type: Property      
    protectionLegacySystem:      
      description: Train protection legacy system      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    quasiStaticGuidingForce:      
      description: Quasi static guiding force      
      type: number      
      x-ngsi:      
        type: Property      
    radioSwitchOverSpecialConditions:      
      description: Radio switch over special conditions      
      type: string      
      x-ngsi:      
        type: Property      
    railInclination:      
      description: Rail inclination      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    referencePassByNoiseLevel:      
      description: Reference pass-by noise level      
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
    shortestDistanceBetweenPantographsInContactWithOCL:      
      description: Shortest distance between pantographs in contact with OCL      
      type: string      
      x-ngsi:      
        type: Property      
    sleepingPlaces:      
      description: Sleeping places      
      type: string      
      x-ngsi:      
        type: Property      
    snowIceHailConditions:      
      description: Snow ice hail conditions      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startingNoiseLevel:      
      description: Starting noise level      
      type: number      
      x-ngsi:      
        type: Property      
    staticAxleLoadExceptionalPayload:      
      description: Static axle load under exceptional payload      
      type: number      
      x-ngsi:      
        type: Property      
    staticAxleLoadNormalPayload:      
      description: Static axle load under normal payload      
      type: number      
      x-ngsi:      
        type: Property      
    staticAxleLoadWorkingOrder:      
      description: Static axle load in working order      
      type: number      
      x-ngsi:      
        type: Property      
    stationaryNoiseLevel:      
      description: Stationary noise level      
      type: number      
      x-ngsi:      
        type: Property      
    structuralCategory:      
      description: Structural category      
      type: string      
      x-ngsi:      
        type: Property      
    subCategory:      
      description: Vehicle subcategory      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    supportedPlatformHeight:      
      description: Supported platform height      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    thermalCapacityDistance:      
      description: Thermal capacity distance      
      type: number      
      x-ngsi:      
        type: Property      
    thermalCapacityGradient:      
      description: Thermal capacity gradient      
      type: number      
      x-ngsi:      
        type: Property      
    thermalCapacitySpeed:      
      description: Thermal capacity speed      
      type: number      
      x-ngsi:      
        type: Property      
    thermalCapacityTSIReference:      
      description: Thermal capacity TSI reference      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    thermalCapacityTime:      
      description: Thermal capacity time      
      type: number      
      x-ngsi:      
        type: Property      
    totalVehicleMass:      
      description: Total vehicle mass      
      type: number      
      x-ngsi:      
        type: Property      
    trainControlSwitchOverSpecialConditions:      
      description: Train control switch over special conditions      
      type: string      
      x-ngsi:      
        type: Property      
    trainDetectionSystemType:      
      description: Type of train detection system      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    transportableOnFerry:      
      description: Transportable on ferry      
      type: boolean      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI data type. It has to be VehicleType      
      enum:      
        - VehicleType      
      type: string      
      x-ngsi:      
        type: Property      
    typeVersionId:      
      description: Type version id      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    typeVersionNumber:      
      description: Type version number      
      type: string      
      x-ngsi:      
        type: Property      
    usesGroup555:      
      description: GSM-R use of group 555      
      type: boolean      
      x-ngsi:      
        type: Property      
    vehicleContactForce:      
      description: Vehicle contact force      
      type: number      
      x-ngsi:      
        type: Property      
    vehicleKinematicGaugeOther:      
      description: Vehicle kinematic gauge other      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleMaxSandingOutput:      
      description: Vehicle max sanding output      
      type: string      
      x-ngsi:      
        type: Property      
    vehiclePantographHead:      
      description: Vehicle pantograph head      
      type: string      
      x-ngsi:      
        type: Property      
    vehicleTypeMaximumSpeedAndCantDeficiency:      
      description: Vehicle type maximum speed and cant deficiency      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    vehiclesComposingFixedFormation:      
      description: Vehicles composing fixed formation      
      type: number      
      x-ngsi:      
        type: Property      
    voiceGSMRNetwork:      
      description: Voice GSM-R network      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    voiceOperationalCommImpl:      
      description: Voice operational communication implementation      
      type: string      
      x-ngsi:      
        type: Property      
    voiceRadioCompatible:      
      description: Radio system compatibility voice      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    wheelSetGauge:      
      description: Nominal track gauge      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    wheelSetGaugeChangeoverFacility:      
      description: Wheelset gauge changeover facility      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    wheelSetGaugeTransformationMethod:      
      description: Wheel set gauge transformation method      
      type: string      
      x-ngsi:      
        type: Property      
    wheelchairSleepingPlaces:      
      description: Wheelchair sleeping spaces      
      type: string      
      x-ngsi:      
        type: Property      
    wheelchairSpaces:      
      description: Wheelchair spaces      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: http://data.europa.eu/949/VehicleType      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/VehicleType/LICENSE.md      
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

#### VehicleType NGSI-v2 关键值 示例    

下面是一个以 JSON-LD 格式作为键值的 VehicleType 示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:VehicleType:id:DXAW:12886056",  
  "dateCreated": "1980-12-10T17:21:19Z",  
  "dateModified": "2012-03-07T09:15:20Z",  
  "source": "Mission bag remember actually possible. Stay red have pai",  
  "name": "Trip skin thank. Grow six second age building represent.",  
  "alternateName": "Number statement water man friend others past. Dream newspaper former mind nothing even. Onto write control increase worry.",  
  "description": "Capital magazine importan",  
  "dataProvider": "Seek generation late nothing. Suddenly develop traditional decision decade mean understand.",  
  "owner": [  
    "urn:ngsi-ld:VehicleType:items:CUKT:91140271",  
    "urn:ngsi-ld:VehicleType:items:FLEJ:52177408"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:VehicleType:items:CIUV:68035929"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -74.8296485,  
      108.332861  
    ]  
  },  
  "address": {  
    "streetAddress": "Community single me pass anything during. My form world image partner over.",  
    "addressLocality": "Put little like analysis phone traditional morning.",  
    "addressRegion": "Center agent do.",  
    "addressCountry": "Perhaps reason least blood group. Station purpose clearly decision lay per assume. ",  
    "postalCode": "Sport meeting answer arm. Be lawyer front painting go particular much. Clearly",  
    "postOfficeBoxNumber": "Hard together trouble guess without herself six. Night",  
    "streetNr": "Myself network just business bill too chance. Body small accept radio similar. By nice understand upon",  
    "district": "Feel peace dinner catch. Ten federal make home where already line. Whose turn player."  
  },  
  "areaServed": "Happen quite safe or every opportunity. Difference as ball something red particularly conference however. Major building doctor here standard",  
  "type": "VehicleType",  
  "alternativeName": "Series only stage to. Determin",  
  "altitudeRange": "Doctor carry through song body something against. Out and hotel college fact your community early.",  
  "altitudeRangeDetail": 864,  
  "axleSpacing": "American whole magazine",  
  "boardingAids": "Together range lin",  
  "brakeWeightPercentage": "Troubl",  
  "cantDefficiency": 864,  
  "catenaryMaxRatedCurrent": 537.5,  
  "conditionsTrainFormation": "Bank mind language simply education. Walk task move fall ever director.",  
  "dangerousGoodsTankCode": "Time shoulder so letter campaign take across. Rise scene executive certain they house. Eat show continue their it go.",  
  "designMassExceptionalPayload": 864,  
  "designMassNormalPayload": 864,  
  "designMassWorkingOrder": 864,  
  "drivingCabs": 864,  
  "eddyCurrentBrakePrevention": false,  
  "eddyCurrentBrakingFitted": false,  
  "emergencyBrake": "Whole magazine truth stop whose.",  
  "energyMeterInstalled": false,  
  "energySupplyMaxPower": 688.1,  
  "etcsDataCommApp": "Throw somebody actually whatever mean. Never itself bill work degree challenge. Pattern my respond week suddenly visit describe actually.",  
  "etcsNationalApplications": "Age ground small which rest. Foreign serve physical human indicate suddenly easy. Total tonight little trip.",  
  "etcsOnBoardImplementation": "Mrs I bad around article. Safe him key left per instead other.",  
  "ferromagneticWheelMaterial": false,  
  "fixedSeats": "North",  
  "flangeLubricationFitted": false,  
  "gsmRSetsInDrivingCab": 864,  
  "hasAutomaticDroppingDevice": false,  
  "hasCantDefficiencyCompensation": false,  
  "hasCurrentLimitation": true,  
  "hasLubricationDevicePrevention": false,  
  "hasParkingBrake": false,  
  "hasRegenerativeBrake": false,  
  "hasSandingPrevention": false,  
  "hasShuntingRestrictions": false,  
  "hasTrainIntegrityConfirmation": false,  
  "hasWheelSlideProtectionSystem": true,  
  "letterMarking": "Example se",  
  "loadingPlatformHeight": 864,  
  "magneticBrakePrevention": false,  
  "magneticBrakingFitted": false,  
  "massPerWheel": 864,  
  "maxCurrentStandstillPantograph": 81.7,  
  "maxDistConsecutiveAxles": 864,  
  "maxFlangeHeight": 117.3,  
  "maxImpedanceWheelset": 538.0,  
  "maxLengthVehicleNose": 864,  
  "maximumAverageDeceleration": 16.4,  
  "maximumBrakeThermalEnergyCapacity": 864,  
  "maximumContactWireHeight": 842.8,  
  "maximumDesignSpeed": 864,  
  "maximumLocomotivesCoupled": 864,  
  "maximumServiceBrake": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "maximumSpeedAndCantDeficiency": "Together range line beyond. First policy daughter need kind miss.",  
  "maximumSpeedEmpty": 864,  
  "maximumTemperature": 864,  
  "meetsRequirementVehicleAuthorisation": "American whole magazine truth stop whose. On traditional measure example s",  
  "minAxleLoad": 997.0,  
  "minDistConsecutiveAxles": 864,  
  "minDistFirstLastAxle": 864,  
  "minFlangeHeight": 817.2,  
  "minFlangeThickness": 837.0,  
  "minRimWidth": 392.0,  
  "minVehicleImpedance": "Whom who down claim. Themselves machine husband long certainly.",  
  "minWheelDiameter": 864,  
  "minimumConcaveVerticalRadius": 864,  
  "minimumContactWireHeight": 402.1,  
  "minimumConvexVerticalRadius": 864,  
  "minimumHorizontalRadius": 864,  
  "minimumTemperature": 864,  
  "minimumWheelDiameter": 864,  
  "nonCodedRestrictions": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "numberElementsRakeFreightWagons": 864,  
  "numberOfPantographsInContactWithOCL": 864,  
  "numberOfToilets": 864,  
  "oclType": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "parkingBrake": true,  
  "parkingBrakeMandatory": true,  
  "parkingBrakeMaximumGradient": 440.5,  
  "passByNoiseLevel": 259.7,  
  "permissiblePayload": "Response nation store you performance. Same protect hope special tough.",  
  "portableBoardingAids": "Five everybody student some woman. Author school me officer fall city more.",  
  "preventRegenerativeBrakeUse": false,  
  "prioritySeats": "Owner each effort movie cell goal live. Character family kid vote school that economic.",  
  "prmAccessibleToilets": 864,  
  "quasiStaticGuidingForce": 885.3,  
  "radioSwitchOverSpecialConditions": "Sing last already yet account direction near. Unit well performance three safe. Design long like black ",  
  "referencePassByNoiseLevel": false,  
  "shortestDistanceBetweenPantographsInContactWithOCL": "Difference million they late. Person product glass experience tax pull.",  
  "sleepingPlaces": "Society stay edge nor example leave within always. Very respond truth actually scientist some. ",  
  "startingNoiseLevel": 495.6,  
  "staticAxleLoadExceptionalPayload": 579.6,  
  "staticAxleLoadNormalPayload": 779.8,  
  "staticAxleLoadWorkingOrder": 684.9,  
  "stationaryNoiseLevel": 0.3,  
  "structuralCategory": "Laugh us design carry guess. Because recognize let.",  
  "thermalCapacityDistance": 528.5,  
  "thermalCapacityGradient": 299.1,  
  "thermalCapacitySpeed": 709.3,  
  "thermalCapacityTime": 864,  
  "totalVehicleMass": 864,  
  "trainControlSwitchOverSpecialConditions": "American whole magazine truth stop whose. On traditional measure example sense peace. Would ",  
  "transportableOnFerry": true,  
  "typeVersionNumber": "Line beyond its particularly tree whom. Kind miss artist truth trouble behavior style.",  
  "usesGroup555": true,  
  "vehicleContactForce": 864,  
  "vehicleKinematicGaugeOther": "American whole magazine truth stop whose. On traditional m",  
  "vehicleMaxSandingOutput": "Together range line bey",  
  "vehiclePantographHead": "Trouble behavior style report size personal partner. During foot that course nothin",  
  "vehiclesComposingFixedFormation": 864,  
  "voiceOperationalCommImpl": "American whole magazine truth stop whose. On tradition",  
  "wheelSetGaugeTransformationMethod": "Together range line beyond. First policy daughter need kind miss.",  
  "wheelchairSleepingPlaces": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "wheelchairSpaces": 864,  
  "authorizedCountry": "urn:ngsi-ld:VehicleType:authorizedCountry:PLSG:66048764",  
  "axleBearingConditionMonitoring": "urn:ngsi-ld:VehicleType:axleBearingConditionMonitoring:WZTE:82421948",  
  "category": "urn:ngsi-ld:VehicleType:category:NKTU:41157815",  
  "certificate": "urn:ngsi-ld:VehicleType:certificate:ACXM:38778408",  
  "contactStripMaterial": "urn:ngsi-ld:VehicleType:contactStripMaterial:SHHZ:09753513",  
  "dataGSMRNetwork": "urn:ngsi-ld:VehicleType:dataGSMRNetwork:DJRJ:28711587",  
  "dataRadioCompatible": "urn:ngsi-ld:VehicleType:dataRadioCompatible:JOCT:18583989",  
  "endCouplingType": "urn:ngsi-ld:VehicleType:endCouplingType:BTVI:65934232",  
  "energySupplySystem": "urn:ngsi-ld:VehicleType:energySupplySystem:VMWQ:71122018",  
  "etcsBaseline": "urn:ngsi-ld:VehicleType:etcsBaseline:OPVU:48339694",  
  "etcsEquipmentOnBoardLevel": "urn:ngsi-ld:VehicleType:etcsEquipmentOnBoardLevel:GHAX:51591795",  
  "etcsInfill": "urn:ngsi-ld:VehicleType:etcsInfill:DZEW:41352560",  
  "etcsSystemCompatibility": "urn:ngsi-ld:VehicleType:etcsSystemCompatibility:UGTS:30989101",  
  "fireSafetyCategory": "urn:ngsi-ld:VehicleType:fireSafetyCategory:GFWD:16151090",  
  "gaugingProfile": "urn:ngsi-ld:VehicleType:gaugingProfile:ICHC:73008691",  
  "gsmRRadioDataCommunication": "urn:ngsi-ld:VehicleType:gsmRRadioDataCommunication:TDWM:45620870",  
  "gsmRVersion": "urn:ngsi-ld:VehicleType:gsmRVersion:ZVFF:34579230",  
  "legacyRadioSystem": "urn:ngsi-ld:VehicleType:legacyRadioSystem:PVNS:58419720",  
  "manufacturer": "urn:ngsi-ld:VehicleType:manufacturer:OXCK:84564280",  
  "manufacturingCountry": "urn:ngsi-ld:VehicleType:manufacturingCountry:JVLS:08423759",  
  "parkingBrakeType": "urn:ngsi-ld:VehicleType:parkingBrakeType:GWKF:92466109",  
  "previousVehicleType": "urn:ngsi-ld:VehicleType:previousVehicleType:WSNY:33769606",  
  "protectionLegacySystem": "urn:ngsi-ld:VehicleType:protectionLegacySystem:PRTY:02714278",  
  "railInclination": "urn:ngsi-ld:VehicleType:railInclination:GRUC:00754706",  
  "snowIceHailConditions": "urn:ngsi-ld:VehicleType:snowIceHailConditions:WYAV:20665030",  
  "subCategory": "urn:ngsi-ld:VehicleType:subCategory:IWFD:89131934",  
  "supportedPlatformHeight": "urn:ngsi-ld:VehicleType:supportedPlatformHeight:EUQU:76104714",  
  "thermalCapacityTSIReference": "urn:ngsi-ld:VehicleType:thermalCapacityTSIReference:VIRK:51240003",  
  "trainDetectionSystemType": "urn:ngsi-ld:VehicleType:trainDetectionSystemType:RFGM:59097765",  
  "typeVersionId": "urn:ngsi-ld:VehicleType:typeVersionId:ZLWC:94022455",  
  "vehicleTypeMaximumSpeedAndCantDeficiency": "urn:ngsi-ld:VehicleType:vehicleTypeMaximumSpeedAndCantDeficiency:JLMR:59004229",  
  "voiceGSMRNetwork": "urn:ngsi-ld:VehicleType:voiceGSMRNetwork:QXCJ:24173042",  
  "voiceRadioCompatible": "urn:ngsi-ld:VehicleType:voiceRadioCompatible:PKZZ:65461187",  
  "wheelSetGauge": "urn:ngsi-ld:VehicleType:wheelSetGauge:KXVE:51717604",  
  "wheelSetGaugeChangeoverFacility": "urn:ngsi-ld:VehicleType:wheelSetGaugeChangeoverFacility:BMAD:29611133"
}  
```  
</details>    

#### VehicleType NGSI-v2 标准化示例    

下面是一个规范化 JSON-LD 格式的 VehicleType 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:VehicleType:id:DXAW:12886056",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1980-12-10T17:21:19Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2012-03-07T09:15:20Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Mission bag remember actually possible. Stay red have pai"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Trip skin thank. Grow six second age building represent."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Number statement water man friend others past. Dream newspaper former mind nothing even. Onto write control increase worry."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Capital magazine importan"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Seek generation late nothing. Suddenly develop traditional decision decade mean understand."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:VehicleType:items:CUKT:91140271",  
      "urn:ngsi-ld:VehicleType:items:FLEJ:52177408"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:VehicleType:items:CIUV:68035929"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -74.8296485,  
        108.332861  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Community single me pass anything during. My form world image partner over.",  
      "addressLocality": "Put little like analysis phone traditional morning.",  
      "addressRegion": "Center agent do.",  
      "addressCountry": "Perhaps reason least blood group. Station purpose clearly decision lay per assume. ",  
      "postalCode": "Sport meeting answer arm. Be lawyer front painting go particular much. Clearly",  
      "postOfficeBoxNumber": "Hard together trouble guess without herself six. Night",  
      "streetNr": "Myself network just business bill too chance. Body small accept radio similar. By nice understand upon",  
      "district": "Feel peace dinner catch. Ten federal make home where already line. Whose turn player."  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Happen quite safe or every opportunity. Difference as ball something red particularly conference however. Major building doctor here standard"  
  },  
  "type": "VehicleType",  
  "alternativeName": {  
    "type": "Text",  
    "value": "Series only stage to. Determin"  
  },  
  "altitudeRange": {  
    "type": "Text",  
    "value": "Doctor carry through song body something against. Out and hotel college fact your community early."  
  },  
  "altitudeRangeDetail": {  
    "type": "Number",  
    "value": 864  
  },  
  "axleSpacing": {  
    "type": "Text",  
    "value": "American whole magazine"  
  },  
  "boardingAids": {  
    "type": "Text",  
    "value": "Together range lin"  
  },  
  "brakeWeightPercentage": {  
    "type": "Text",  
    "value": "Troubl"  
  },  
  "cantDefficiency": {  
    "type": "Number",  
    "value": 864  
  },  
  "catenaryMaxRatedCurrent": {  
    "type": "Number",  
    "value": 537.5  
  },  
  "conditionsTrainFormation": {  
    "type": "Text",  
    "value": "Bank mind language simply education. Walk task move fall ever director."  
  },  
  "dangerousGoodsTankCode": {  
    "type": "Text",  
    "value": "Time shoulder so letter campaign take across. Rise scene executive certain they house. Eat show continue their it go."  
  },  
  "designMassExceptionalPayload": {  
    "type": "Number",  
    "value": 864  
  },  
  "designMassNormalPayload": {  
    "type": "Number",  
    "value": 864  
  },  
  "designMassWorkingOrder": {  
    "type": "Number",  
    "value": 864  
  },  
  "drivingCabs": {  
    "type": "Number",  
    "value": 864  
  },  
  "eddyCurrentBrakePrevention": {  
    "type": "Boolean",  
    "value": false  
  },  
  "eddyCurrentBrakingFitted": {  
    "type": "Boolean",  
    "value": false  
  },  
  "emergencyBrake": {  
    "type": "Text",  
    "value": "Whole magazine truth stop whose."  
  },  
  "energyMeterInstalled": {  
    "type": "Boolean",  
    "value": false  
  },  
  "energySupplyMaxPower": {  
    "type": "Number",  
    "value": 688.1  
  },  
  "etcsDataCommApp": {  
    "type": "Text",  
    "value": "Throw somebody actually whatever mean. Never itself bill work degree challenge. Pattern my respond week suddenly visit describe actually."  
  },  
  "etcsNationalApplications": {  
    "type": "Text",  
    "value": "Age ground small which rest. Foreign serve physical human indicate suddenly easy. Total tonight little trip."  
  },  
  "etcsOnBoardImplementation": {  
    "type": "Text",  
    "value": "Mrs I bad around article. Safe him key left per instead other."  
  },  
  "ferromagneticWheelMaterial": {  
    "type": "Boolean",  
    "value": false  
  },  
  "fixedSeats": {  
    "type": "Text",  
    "value": "North"  
  },  
  "flangeLubricationFitted": {  
    "type": "Boolean",  
    "value": false  
  },  
  "gsmRSetsInDrivingCab": {  
    "type": "Number",  
    "value": 864  
  },  
  "hasAutomaticDroppingDevice": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasCantDefficiencyCompensation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasCurrentLimitation": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasLubricationDevicePrevention": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasParkingBrake": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasRegenerativeBrake": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasSandingPrevention": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasShuntingRestrictions": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasTrainIntegrityConfirmation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasWheelSlideProtectionSystem": {  
    "type": "Boolean",  
    "value": true  
  },  
  "letterMarking": {  
    "type": "Text",  
    "value": "Example se"  
  },  
  "loadingPlatformHeight": {  
    "type": "Number",  
    "value": 864  
  },  
  "magneticBrakePrevention": {  
    "type": "Boolean",  
    "value": false  
  },  
  "magneticBrakingFitted": {  
    "type": "Boolean",  
    "value": false  
  },  
  "massPerWheel": {  
    "type": "Number",  
    "value": 864  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Number",  
    "value": 81.7  
  },  
  "maxDistConsecutiveAxles": {  
    "type": "Number",  
    "value": 864  
  },  
  "maxFlangeHeight": {  
    "type": "Number",  
    "value": 117.3  
  },  
  "maxImpedanceWheelset": {  
    "type": "Number",  
    "value": 538.0  
  },  
  "maxLengthVehicleNose": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumAverageDeceleration": {  
    "type": "Number",  
    "value": 16.4  
  },  
  "maximumBrakeThermalEnergyCapacity": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumContactWireHeight": {  
    "type": "Number",  
    "value": 842.8  
  },  
  "maximumDesignSpeed": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumLocomotivesCoupled": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumServiceBrake": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "maximumSpeedAndCantDeficiency": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "maximumSpeedEmpty": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumTemperature": {  
    "type": "Number",  
    "value": 864  
  },  
  "meetsRequirementVehicleAuthorisation": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example s"  
  },  
  "minAxleLoad": {  
    "type": "Number",  
    "value": 997.0  
  },  
  "minDistConsecutiveAxles": {  
    "type": "Number",  
    "value": 864  
  },  
  "minDistFirstLastAxle": {  
    "type": "Number",  
    "value": 864  
  },  
  "minFlangeHeight": {  
    "type": "Number",  
    "value": 817.2  
  },  
  "minFlangeThickness": {  
    "type": "Number",  
    "value": 837.0  
  },  
  "minRimWidth": {  
    "type": "Number",  
    "value": 392.0  
  },  
  "minVehicleImpedance": {  
    "type": "Text",  
    "value": "Whom who down claim. Themselves machine husband long certainly."  
  },  
  "minWheelDiameter": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumConcaveVerticalRadius": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumContactWireHeight": {  
    "type": "Number",  
    "value": 402.1  
  },  
  "minimumConvexVerticalRadius": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumHorizontalRadius": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumTemperature": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumWheelDiameter": {  
    "type": "Number",  
    "value": 864  
  },  
  "nonCodedRestrictions": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peac"  
  },  
  "numberElementsRakeFreightWagons": {  
    "type": "Number",  
    "value": 864  
  },  
  "numberOfPantographsInContactWithOCL": {  
    "type": "Number",  
    "value": 864  
  },  
  "numberOfToilets": {  
    "type": "Number",  
    "value": 864  
  },  
  "oclType": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "parkingBrake": {  
    "type": "Boolean",  
    "value": true  
  },  
  "parkingBrakeMandatory": {  
    "type": "Boolean",  
    "value": true  
  },  
  "parkingBrakeMaximumGradient": {  
    "type": "Number",  
    "value": 440.5  
  },  
  "passByNoiseLevel": {  
    "type": "Number",  
    "value": 259.7  
  },  
  "permissiblePayload": {  
    "type": "Text",  
    "value": "Response nation store you performance. Same protect hope special tough."  
  },  
  "portableBoardingAids": {  
    "type": "Text",  
    "value": "Five everybody student some woman. Author school me officer fall city more."  
  },  
  "preventRegenerativeBrakeUse": {  
    "type": "Boolean",  
    "value": false  
  },  
  "prioritySeats": {  
    "type": "Text",  
    "value": "Owner each effort movie cell goal live. Character family kid vote school that economic."  
  },  
  "prmAccessibleToilets": {  
    "type": "Number",  
    "value": 864  
  },  
  "quasiStaticGuidingForce": {  
    "type": "Number",  
    "value": 885.3  
  },  
  "radioSwitchOverSpecialConditions": {  
    "type": "Text",  
    "value": "Sing last already yet account direction near. Unit well performance three safe. Design long like black "  
  },  
  "referencePassByNoiseLevel": {  
    "type": "Boolean",  
    "value": false  
  },  
  "shortestDistanceBetweenPantographsInContactWithOCL": {  
    "type": "Text",  
    "value": "Difference million they late. Person product glass experience tax pull."  
  },  
  "sleepingPlaces": {  
    "type": "Text",  
    "value": "Society stay edge nor example leave within always. Very respond truth actually scientist some. "  
  },  
  "startingNoiseLevel": {  
    "type": "Number",  
    "value": 495.6  
  },  
  "staticAxleLoadExceptionalPayload": {  
    "type": "Number",  
    "value": 579.6  
  },  
  "staticAxleLoadNormalPayload": {  
    "type": "Number",  
    "value": 779.8  
  },  
  "staticAxleLoadWorkingOrder": {  
    "type": "Number",  
    "value": 684.9  
  },  
  "stationaryNoiseLevel": {  
    "type": "Number",  
    "value": 0.3  
  },  
  "structuralCategory": {  
    "type": "Text",  
    "value": "Laugh us design carry guess. Because recognize let."  
  },  
  "thermalCapacityDistance": {  
    "type": "Number",  
    "value": 528.5  
  },  
  "thermalCapacityGradient": {  
    "type": "Number",  
    "value": 299.1  
  },  
  "thermalCapacitySpeed": {  
    "type": "Number",  
    "value": 709.3  
  },  
  "thermalCapacityTime": {  
    "type": "Number",  
    "value": 864  
  },  
  "totalVehicleMass": {  
    "type": "Number",  
    "value": 864  
  },  
  "trainControlSwitchOverSpecialConditions": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would "  
  },  
  "transportableOnFerry": {  
    "type": "Boolean",  
    "value": true  
  },  
  "typeVersionNumber": {  
    "type": "Text",  
    "value": "Line beyond its particularly tree whom. Kind miss artist truth trouble behavior style."  
  },  
  "usesGroup555": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleContactForce": {  
    "type": "Number",  
    "value": 864  
  },  
  "vehicleKinematicGaugeOther": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional m"  
  },  
  "vehicleMaxSandingOutput": {  
    "type": "Text",  
    "value": "Together range line bey"  
  },  
  "vehiclePantographHead": {  
    "type": "Text",  
    "value": "Trouble behavior style report size personal partner. During foot that course nothin"  
  },  
  "vehiclesComposingFixedFormation": {  
    "type": "Number",  
    "value": 864  
  },  
  "voiceOperationalCommImpl": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On tradition"  
  },  
  "wheelSetGaugeTransformationMethod": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "wheelchairSleepingPlaces": {  
    "type": "Text",  
    "value": "Trouble behavior style report size personal partner. During foot that course nothing draw."  
  },  
  "wheelchairSpaces": {  
    "type": "Number",  
    "value": 864  
  },  
  "authorizedCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:authorizedCountry:PLSG:66048764"  
  },  
  "axleBearingConditionMonitoring": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:axleBearingConditionMonitoring:WZTE:82421948"  
  },  
  "category": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:category:NKTU:41157815"  
  },  
  "certificate": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:certificate:ACXM:38778408"  
  },  
  "contactStripMaterial": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:contactStripMaterial:SHHZ:09753513"  
  },  
  "dataGSMRNetwork": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:dataGSMRNetwork:DJRJ:28711587"  
  },  
  "dataRadioCompatible": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:dataRadioCompatible:JOCT:18583989"  
  },  
  "endCouplingType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:endCouplingType:BTVI:65934232"  
  },  
  "energySupplySystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:energySupplySystem:VMWQ:71122018"  
  },  
  "etcsBaseline": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:etcsBaseline:OPVU:48339694"  
  },  
  "etcsEquipmentOnBoardLevel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:etcsEquipmentOnBoardLevel:GHAX:51591795"  
  },  
  "etcsInfill": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:etcsInfill:DZEW:41352560"  
  },  
  "etcsSystemCompatibility": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:etcsSystemCompatibility:UGTS:30989101"  
  },  
  "fireSafetyCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:fireSafetyCategory:GFWD:16151090"  
  },  
  "gaugingProfile": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:gaugingProfile:ICHC:73008691"  
  },  
  "gsmRRadioDataCommunication": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:gsmRRadioDataCommunication:TDWM:45620870"  
  },  
  "gsmRVersion": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:gsmRVersion:ZVFF:34579230"  
  },  
  "legacyRadioSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:legacyRadioSystem:PVNS:58419720"  
  },  
  "manufacturer": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:manufacturer:OXCK:84564280"  
  },  
  "manufacturingCountry": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:manufacturingCountry:JVLS:08423759"  
  },  
  "parkingBrakeType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:parkingBrakeType:GWKF:92466109"  
  },  
  "previousVehicleType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:previousVehicleType:WSNY:33769606"  
  },  
  "protectionLegacySystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:protectionLegacySystem:PRTY:02714278"  
  },  
  "railInclination": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:railInclination:GRUC:00754706"  
  },  
  "snowIceHailConditions": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:snowIceHailConditions:WYAV:20665030"  
  },  
  "subCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:subCategory:IWFD:89131934"  
  },  
  "supportedPlatformHeight": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:supportedPlatformHeight:EUQU:76104714"  
  },  
  "thermalCapacityTSIReference": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:thermalCapacityTSIReference:VIRK:51240003"  
  },  
  "trainDetectionSystemType": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:trainDetectionSystemType:RFGM:59097765"  
  },  
  "typeVersionId": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:typeVersionId:ZLWC:94022455"  
  },  
  "vehicleTypeMaximumSpeedAndCantDeficiency": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:vehicleTypeMaximumSpeedAndCantDeficiency:JLMR:59004229"  
  },  
  "voiceGSMRNetwork": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:voiceGSMRNetwork:QXCJ:24173042"  
  },  
  "voiceRadioCompatible": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:voiceRadioCompatible:PKZZ:65461187"  
  },  
  "wheelSetGauge": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:wheelSetGauge:KXVE:51717604"  
  },  
  "wheelSetGaugeChangeoverFacility": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:VehicleType:wheelSetGaugeChangeoverFacility:BMAD:29611133"  
  }  
}  
```  
</details>    

#### VehicleType NGSI-LD 关键值 示例    

下面是一个以 JSON-LD 格式作为键值的 VehicleType 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:VehicleType:id:DXAW:12886056",  
  "dateCreated": "1980-12-10T17:21:19Z",  
  "dateModified": "2012-03-07T09:15:20Z",  
  "source": "Mission bag remember actually possible. Stay red have pai",  
  "name": "Trip skin thank. Grow six second age building represent.",  
  "alternateName": "Number statement water man friend others past. Dream newspaper former mind nothing even. Onto write control increase worry.",  
  "description": "Capital magazine importan",  
  "dataProvider": "Seek generation late nothing. Suddenly develop traditional decision decade mean understand.",  
  "owner": [  
    "urn:ngsi-ld:VehicleType:items:CUKT:91140271",  
    "urn:ngsi-ld:VehicleType:items:FLEJ:52177408"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:VehicleType:items:CIUV:68035929"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -74.8296485,  
      108.332861  
    ]  
  },  
  "address": {  
    "streetAddress": "Community single me pass anything during. My form world image partner over.",  
    "addressLocality": "Put little like analysis phone traditional morning.",  
    "addressRegion": "Center agent do.",  
    "addressCountry": "Perhaps reason least blood group. Station purpose clearly decision lay per assume. ",  
    "postalCode": "Sport meeting answer arm. Be lawyer front painting go particular much. Clearly",  
    "postOfficeBoxNumber": "Hard together trouble guess without herself six. Night",  
    "streetNr": "Myself network just business bill too chance. Body small accept radio similar. By nice understand upon",  
    "district": "Feel peace dinner catch. Ten federal make home where already line. Whose turn player."  
  },  
  "areaServed": "Happen quite safe or every opportunity. Difference as ball something red particularly conference however. Major building doctor here standard",  
  "type": "VehicleType",  
  "alternativeName": "Series only stage to. Determin",  
  "altitudeRange": "Doctor carry through song body something against. Out and hotel college fact your community early.",  
  "altitudeRangeDetail": 864,  
  "axleSpacing": "American whole magazine",  
  "boardingAids": "Together range lin",  
  "brakeWeightPercentage": "Troubl",  
  "cantDefficiency": 864,  
  "catenaryMaxRatedCurrent": 537.5,  
  "conditionsTrainFormation": "Bank mind language simply education. Walk task move fall ever director.",  
  "dangerousGoodsTankCode": "Time shoulder so letter campaign take across. Rise scene executive certain they house. Eat show continue their it go.",  
  "designMassExceptionalPayload": 864,  
  "designMassNormalPayload": 864,  
  "designMassWorkingOrder": 864,  
  "drivingCabs": 864,  
  "eddyCurrentBrakePrevention": false,  
  "eddyCurrentBrakingFitted": false,  
  "emergencyBrake": "Whole magazine truth stop whose.",  
  "energyMeterInstalled": false,  
  "energySupplyMaxPower": 688.1,  
  "etcsDataCommApp": "Throw somebody actually whatever mean. Never itself bill work degree challenge. Pattern my respond week suddenly visit describe actually.",  
  "etcsNationalApplications": "Age ground small which rest. Foreign serve physical human indicate suddenly easy. Total tonight little trip.",  
  "etcsOnBoardImplementation": "Mrs I bad around article. Safe him key left per instead other.",  
  "ferromagneticWheelMaterial": false,  
  "fixedSeats": "North",  
  "flangeLubricationFitted": false,  
  "gsmRSetsInDrivingCab": 864,  
  "hasAutomaticDroppingDevice": false,  
  "hasCantDefficiencyCompensation": false,  
  "hasCurrentLimitation": true,  
  "hasLubricationDevicePrevention": false,  
  "hasParkingBrake": false,  
  "hasRegenerativeBrake": false,  
  "hasSandingPrevention": false,  
  "hasShuntingRestrictions": false,  
  "hasTrainIntegrityConfirmation": false,  
  "hasWheelSlideProtectionSystem": true,  
  "letterMarking": "Example se",  
  "loadingPlatformHeight": 864,  
  "magneticBrakePrevention": false,  
  "magneticBrakingFitted": false,  
  "massPerWheel": 864,  
  "maxCurrentStandstillPantograph": 81.7,  
  "maxDistConsecutiveAxles": 864,  
  "maxFlangeHeight": 117.3,  
  "maxImpedanceWheelset": 538.0,  
  "maxLengthVehicleNose": 864,  
  "maximumAverageDeceleration": 16.4,  
  "maximumBrakeThermalEnergyCapacity": 864,  
  "maximumContactWireHeight": 842.8,  
  "maximumDesignSpeed": 864,  
  "maximumLocomotivesCoupled": 864,  
  "maximumServiceBrake": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "maximumSpeedAndCantDeficiency": "Together range line beyond. First policy daughter need kind miss.",  
  "maximumSpeedEmpty": 864,  
  "maximumTemperature": 864,  
  "meetsRequirementVehicleAuthorisation": "American whole magazine truth stop whose. On traditional measure example s",  
  "minAxleLoad": 997.0,  
  "minDistConsecutiveAxles": 864,  
  "minDistFirstLastAxle": 864,  
  "minFlangeHeight": 817.2,  
  "minFlangeThickness": 837.0,  
  "minRimWidth": 392.0,  
  "minVehicleImpedance": "Whom who down claim. Themselves machine husband long certainly.",  
  "minWheelDiameter": 864,  
  "minimumConcaveVerticalRadius": 864,  
  "minimumContactWireHeight": 402.1,  
  "minimumConvexVerticalRadius": 864,  
  "minimumHorizontalRadius": 864,  
  "minimumTemperature": 864,  
  "minimumWheelDiameter": 864,  
  "nonCodedRestrictions": "American whole magazine truth stop whose. On traditional measure example sense peac",  
  "numberElementsRakeFreightWagons": 864,  
  "numberOfPantographsInContactWithOCL": 864,  
  "numberOfToilets": 864,  
  "oclType": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "parkingBrake": true,  
  "parkingBrakeMandatory": true,  
  "parkingBrakeMaximumGradient": 440.5,  
  "passByNoiseLevel": 259.7,  
  "permissiblePayload": "Response nation store you performance. Same protect hope special tough.",  
  "portableBoardingAids": "Five everybody student some woman. Author school me officer fall city more.",  
  "preventRegenerativeBrakeUse": false,  
  "prioritySeats": "Owner each effort movie cell goal live. Character family kid vote school that economic.",  
  "prmAccessibleToilets": 864,  
  "quasiStaticGuidingForce": 885.3,  
  "radioSwitchOverSpecialConditions": "Sing last already yet account direction near. Unit well performance three safe. Design long like black ",  
  "referencePassByNoiseLevel": false,  
  "shortestDistanceBetweenPantographsInContactWithOCL": "Difference million they late. Person product glass experience tax pull.",  
  "sleepingPlaces": "Society stay edge nor example leave within always. Very respond truth actually scientist some. ",  
  "startingNoiseLevel": 495.6,  
  "staticAxleLoadExceptionalPayload": 579.6,  
  "staticAxleLoadNormalPayload": 779.8,  
  "staticAxleLoadWorkingOrder": 684.9,  
  "stationaryNoiseLevel": 0.3,  
  "structuralCategory": "Laugh us design carry guess. Because recognize let.",  
  "thermalCapacityDistance": 528.5,  
  "thermalCapacityGradient": 299.1,  
  "thermalCapacitySpeed": 709.3,  
  "thermalCapacityTime": 864,  
  "totalVehicleMass": 864,  
  "trainControlSwitchOverSpecialConditions": "American whole magazine truth stop whose. On traditional measure example sense peace. Would ",  
  "transportableOnFerry": true,  
  "typeVersionNumber": "Line beyond its particularly tree whom. Kind miss artist truth trouble behavior style.",  
  "usesGroup555": true,  
  "vehicleContactForce": 864,  
  "vehicleKinematicGaugeOther": "American whole magazine truth stop whose. On traditional m",  
  "vehicleMaxSandingOutput": "Together range line bey",  
  "vehiclePantographHead": "Trouble behavior style report size personal partner. During foot that course nothin",  
  "vehiclesComposingFixedFormation": 864,  
  "voiceOperationalCommImpl": "American whole magazine truth stop whose. On tradition",  
  "wheelSetGaugeTransformationMethod": "Together range line beyond. First policy daughter need kind miss.",  
  "wheelchairSleepingPlaces": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "wheelchairSpaces": 864,  
  "authorizedCountry": "urn:ngsi-ld:VehicleType:authorizedCountry:PLSG:66048764",  
  "axleBearingConditionMonitoring": "urn:ngsi-ld:VehicleType:axleBearingConditionMonitoring:WZTE:82421948",  
  "category": "urn:ngsi-ld:VehicleType:category:NKTU:41157815",  
  "certificate": "urn:ngsi-ld:VehicleType:certificate:ACXM:38778408",  
  "contactStripMaterial": "urn:ngsi-ld:VehicleType:contactStripMaterial:SHHZ:09753513",  
  "dataGSMRNetwork": "urn:ngsi-ld:VehicleType:dataGSMRNetwork:DJRJ:28711587",  
  "dataRadioCompatible": "urn:ngsi-ld:VehicleType:dataRadioCompatible:JOCT:18583989",  
  "endCouplingType": "urn:ngsi-ld:VehicleType:endCouplingType:BTVI:65934232",  
  "energySupplySystem": "urn:ngsi-ld:VehicleType:energySupplySystem:VMWQ:71122018",  
  "etcsBaseline": "urn:ngsi-ld:VehicleType:etcsBaseline:OPVU:48339694",  
  "etcsEquipmentOnBoardLevel": "urn:ngsi-ld:VehicleType:etcsEquipmentOnBoardLevel:GHAX:51591795",  
  "etcsInfill": "urn:ngsi-ld:VehicleType:etcsInfill:DZEW:41352560",  
  "etcsSystemCompatibility": "urn:ngsi-ld:VehicleType:etcsSystemCompatibility:UGTS:30989101",  
  "fireSafetyCategory": "urn:ngsi-ld:VehicleType:fireSafetyCategory:GFWD:16151090",  
  "gaugingProfile": "urn:ngsi-ld:VehicleType:gaugingProfile:ICHC:73008691",  
  "gsmRRadioDataCommunication": "urn:ngsi-ld:VehicleType:gsmRRadioDataCommunication:TDWM:45620870",  
  "gsmRVersion": "urn:ngsi-ld:VehicleType:gsmRVersion:ZVFF:34579230",  
  "legacyRadioSystem": "urn:ngsi-ld:VehicleType:legacyRadioSystem:PVNS:58419720",  
  "manufacturer": "urn:ngsi-ld:VehicleType:manufacturer:OXCK:84564280",  
  "manufacturingCountry": "urn:ngsi-ld:VehicleType:manufacturingCountry:JVLS:08423759",  
  "parkingBrakeType": "urn:ngsi-ld:VehicleType:parkingBrakeType:GWKF:92466109",  
  "previousVehicleType": "urn:ngsi-ld:VehicleType:previousVehicleType:WSNY:33769606",  
  "protectionLegacySystem": "urn:ngsi-ld:VehicleType:protectionLegacySystem:PRTY:02714278",  
  "railInclination": "urn:ngsi-ld:VehicleType:railInclination:GRUC:00754706",  
  "snowIceHailConditions": "urn:ngsi-ld:VehicleType:snowIceHailConditions:WYAV:20665030",  
  "subCategory": "urn:ngsi-ld:VehicleType:subCategory:IWFD:89131934",  
  "supportedPlatformHeight": "urn:ngsi-ld:VehicleType:supportedPlatformHeight:EUQU:76104714",  
  "thermalCapacityTSIReference": "urn:ngsi-ld:VehicleType:thermalCapacityTSIReference:VIRK:51240003",  
  "trainDetectionSystemType": "urn:ngsi-ld:VehicleType:trainDetectionSystemType:RFGM:59097765",  
  "typeVersionId": "urn:ngsi-ld:VehicleType:typeVersionId:ZLWC:94022455",  
  "vehicleTypeMaximumSpeedAndCantDeficiency": "urn:ngsi-ld:VehicleType:vehicleTypeMaximumSpeedAndCantDeficiency:JLMR:59004229",  
  "voiceGSMRNetwork": "urn:ngsi-ld:VehicleType:voiceGSMRNetwork:QXCJ:24173042",  
  "voiceRadioCompatible": "urn:ngsi-ld:VehicleType:voiceRadioCompatible:PKZZ:65461187",  
  "wheelSetGauge": "urn:ngsi-ld:VehicleType:wheelSetGauge:KXVE:51717604",  
  "wheelSetGaugeChangeoverFacility": "urn:ngsi-ld:VehicleType:wheelSetGaugeChangeoverFacility:BMAD:29611133",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### 车辆类型 NGSI-LD 标准化示例    

下面是一个规范化 JSON-LD 格式的 VehicleType 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      

```json  

{  
  "id": "urn:ngsi-ld:VehicleType:id:RTWI:29731639",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1989-06-15T16:47:58Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1973-10-10T18:23:00Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "What language agree piece meet summer see certainly. Who ag"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Claim successful radio management family. Improve score long dur"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Room laugh agreement significant techn"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Someone remain admit include question. Where debate art attention. Mention detail late act television collection bring."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Will spend newspaper remain. Catch building will image require chance ani"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:VehicleType:items:BSOU:89857339",  
      "urn:ngsi-ld:VehicleType:items:BBCR:76018674"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:VehicleType:items:OXVY:50210180"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -5.404456,  
        -71.456341  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Speak memory there way loss. Wonder up buy power old catch. Recent them person thousand protect number.",  
      "addressLocality": "Inside prove oil should short seek decide. At happy old actually fund receive service. Teach commercial mean.",  
      "addressRegion": "Fast south describe else. My born too foot smile least. Choice list anyone be catch bank program.",  
      "addressCountry": "North poor also little political growth establish themselves. Answer parent office them job cultural water.",  
      "postalCode": "Point feeling foot ball compare. Service process serious present. Brother interview right line begin.",  
      "postOfficeBoxNumber": "Guy whom avoid attack glass. Really nation he head when. Tree very prove reduce security project experience.",  
      "streetNr": "Interest gun stop according",  
      "district": "Open side participant want. Enter difficult coach prevent third cup perhaps. Tonight none style executive."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Note prove law plan prove artist. According population job through especially factor head."  
  },  
  "type": "VehicleType",  
  "alternativeName": {  
    "type": "Property",  
    "value": "Beat arrive cell. Glass style industry professor arrive such. Almost cup tha"  
  },  
  "altitudeRange": {  
    "type": "Property",  
    "value": "Less case relate necessary certainly. Group pull station severa"  
  },  
  "altitudeRangeDetail": {  
    "type": "Property",  
    "value": 361  
  },  
  "axleSpacing": {  
    "type": "Property",  
    "value": "Mother through might manage soon. Power house stuff together source yard Democrat. Develop rock than."  
  },  
  "boardingAids": {  
    "type": "Property",  
    "value": "Enough country expect environmental but. Foreign western remember."  
  },  
  "brakeWeightPercentage": {  
    "type": "Property",  
    "value": "Foot her enough PM. Skill them message staff important owner. Who challenge forget room environment throughout."  
  },  
  "cantDefficiency": {  
    "type": "Property",  
    "value": 468  
  },  
  "catenaryMaxRatedCurrent": {  
    "type": "Property",  
    "value": 367.5  
  },  
  "conditionsTrainFormation": {  
    "type": "Property",  
    "value": "Do join care rock. Organization policy professor why treatment just accept. Mor"  
  },  
  "dangerousGoodsTankCode": {  
    "type": "Property",  
    "value": "When teach model generation. Final if stay design."  
  },  
  "designMassExceptionalPayload": {  
    "type": "Property",  
    "value": 171  
  },  
  "designMassNormalPayload": {  
    "type": "Property",  
    "value": 914  
  },  
  "designMassWorkingOrder": {  
    "type": "Property",  
    "value": 139  
  },  
  "drivingCabs": {  
    "type": "Property",  
    "value": 496  
  },  
  "eddyCurrentBrakePrevention": {  
    "type": "Property",  
    "value": false  
  },  
  "eddyCurrentBrakingFitted": {  
    "type": "Property",  
    "value": true  
  },  
  "emergencyBrake": {  
    "type": "Property",  
    "value": "Good remain heart career. Despite situation enter animal outs"  
  },  
  "energyMeterInstalled": {  
    "type": "Property",  
    "value": true  
  },  
  "energySupplyMaxPower": {  
    "type": "Property",  
    "value": 709.8  
  },  
  "etcsDataCommApp": {  
    "type": "Property",  
    "value": "Yard democratic itself forget investment day."  
  },  
  "etcsNationalApplications": {  
    "type": "Property",  
    "value": "Far ability beautiful human. Tv rise pretty against market hit. Offer among from I anoth"  
  },  
  "etcsOnBoardImplementation": {  
    "type": "Property",  
    "value": "Traditional player others design lay local suffer language. Gas perhaps force which glass continue describe. Control bac"  
  },  
  "ferromagneticWheelMaterial": {  
    "type": "Property",  
    "value": false  
  },  
  "fixedSeats": {  
    "type": "Property",  
    "value": "Impact media near push let. Personal board citizen cost either inside. Of hand local increase."  
  },  
  "flangeLubricationFitted": {  
    "type": "Property",  
    "value": false  
  },  
  "gsmRSetsInDrivingCab": {  
    "type": "Property",  
    "value": 290  
  },  
  "hasAutomaticDroppingDevice": {  
    "type": "Property",  
    "value": false  
  },  
  "hasCantDefficiencyCompensation": {  
    "type": "Property",  
    "value": true  
  },  
  "hasCurrentLimitation": {  
    "type": "Property",  
    "value": true  
  },  
  "hasLubricationDevicePrevention": {  
    "type": "Property",  
    "value": true  
  },  
  "hasParkingBrake": {  
    "type": "Property",  
    "value": false  
  },  
  "hasRegenerativeBrake": {  
    "type": "Property",  
    "value": false  
  },  
  "hasSandingPrevention": {  
    "type": "Property",  
    "value": true  
  },  
  "hasShuntingRestrictions": {  
    "type": "Property",  
    "value": false  
  },  
  "hasTrainIntegrityConfirmation": {  
    "type": "Property",  
    "value": false  
  },  
  "hasWheelSlideProtectionSystem": {  
    "type": "Property",  
    "value": true  
  },  
  "letterMarking": {  
    "type": "Property",  
    "value": "White raise process challenge anyone. Picture lit"  
  },  
  "loadingPlatformHeight": {  
    "type": "Property",  
    "value": 632  
  },  
  "magneticBrakePrevention": {  
    "type": "Property",  
    "value": true  
  },  
  "magneticBrakingFitted": {  
    "type": "Property",  
    "value": false  
  },  
  "massPerWheel": {  
    "type": "Property",  
    "value": 195  
  },  
  "maxCurrentStandstillPantograph": {  
    "type": "Property",  
    "value": 5.0  
  },  
  "maxDistConsecutiveAxles": {  
    "type": "Property",  
    "value": 382  
  },  
  "maxFlangeHeight": {  
    "type": "Property",  
    "value": 899.7  
  },  
  "maxImpedanceWheelset": {  
    "type": "Property",  
    "value": 434.9  
  },  
  "maxLengthVehicleNose": {  
    "type": "Property",  
    "value": 813  
  },  
  "maximumAverageDeceleration": {  
    "type": "Property",  
    "value": 925.6  
  },  
  "maximumBrakeThermalEnergyCapacity": {  
    "type": "Property",  
    "value": 577  
  },  
  "maximumContactWireHeight": {  
    "type": "Property",  
    "value": 847.5  
  },  
  "maximumDesignSpeed": {  
    "type": "Property",  
    "value": 901  
  },  
  "maximumLocomotivesCoupled": {  
    "type": "Property",  
    "value": 234  
  },  
  "maximumServiceBrake": {  
    "type": "Property",  
    "value": "Major fine else soon myself degree. Single food increase rate ask than. Similar front standard"  
  },  
  "maximumSpeedAndCantDeficiency": {  
    "type": "Property",  
    "value": "Poor child might Democrat price personal pull question. Leader bad focus name its."  
  },  
  "maximumSpeedEmpty": {  
    "type": "Property",  
    "value": 797  
  },  
  "maximumTemperature": {  
    "type": "Property",  
    "value": 539  
  },  
  "meetsRequirementVehicleAuthorisation": {  
    "type": "Property",  
    "value": "Modern public me movement simple pretty either. Wonder respon"  
  },  
  "minAxleLoad": {  
    "type": "Property",  
    "value": 548.5  
  },  
  "minDistConsecutiveAxles": {  
    "type": "Property",  
    "value": 805  
  },  
  "minDistFirstLastAxle": {  
    "type": "Property",  
    "value": 348  
  },  
  "minFlangeHeight": {  
    "type": "Property",  
    "value": 478.5  
  },  
  "minFlangeThickness": {  
    "type": "Property",  
    "value": 952.4  
  },  
  "minRimWidth": {  
    "type": "Property",  
    "value": 409.8  
  },  
  "minVehicleImpedance": {  
    "type": "Property",  
    "value": "Natural past offer break. Box everyone challenge figure daughter politics. Left last project answer hour mention."  
  },  
  "minWheelDiameter": {  
    "type": "Property",  
    "value": 758  
  },  
  "minimumConcaveVerticalRadius": {  
    "type": "Property",  
    "value": 550  
  },  
  "minimumContactWireHeight": {  
    "type": "Property",  
    "value": 129.1  
  },  
  "minimumConvexVerticalRadius": {  
    "type": "Property",  
    "value": 56  
  },  
  "minimumHorizontalRadius": {  
    "type": "Property",  
    "value": 889  
  },  
  "minimumTemperature": {  
    "type": "Property",  
    "value": 529  
  },  
  "minimumWheelDiameter": {  
    "type": "Property",  
    "value": 325  
  },  
  "nonCodedRestrictions": {  
    "type": "Property",  
    "value": "Ten if should fire stuff level. Three perhaps few risk model determine collection."  
  },  
  "numberElementsRakeFreightWagons": {  
    "type": "Property",  
    "value": 69  
  },  
  "numberOfPantographsInContactWithOCL": {  
    "type": "Property",  
    "value": 263  
  },  
  "numberOfToilets": {  
    "type": "Property",  
    "value": 775  
  },  
  "oclType": {  
    "type": "Property",  
    "value": "Fire us man nature. Continue dark both city wish maintain the door."  
  },  
  "parkingBrake": {  
    "type": "Property",  
    "value": true  
  },  
  "parkingBrakeMandatory": {  
    "type": "Property",  
    "value": false  
  },  
  "parkingBrakeMaximumGradient": {  
    "type": "Property",  
    "value": 585.7  
  },  
  "passByNoiseLevel": {  
    "type": "Property",  
    "value": 331.7  
  },  
  "permissiblePayload": {  
    "type": "Property",  
    "value": "Successful third western gun. Little study how politics which foreign visit. At management structure new"  
  },  
  "portableBoardingAids": {  
    "type": "Property",  
    "value": "Evidence security organization generation third agree. Explain south phone agree why thus reveal of"  
  },  
  "preventRegenerativeBrakeUse": {  
    "type": "Property",  
    "value": false  
  },  
  "prioritySeats": {  
    "type": "Property",  
    "value": "Apply help ten share huge so"  
  },  
  "prmAccessibleToilets": {  
    "type": "Property",  
    "value": 315  
  },  
  "quasiStaticGuidingForce": {  
    "type": "Property",  
    "value": 35.0  
  },  
  "radioSwitchOverSpecialConditions": {  
    "type": "Property",  
    "value": "Represent single thing often focus on. Water attorney buy recent piece impact region what. Push executive continue still trip around onto."  
  },  
  "referencePassByNoiseLevel": {  
    "type": "Property",  
    "value": false  
  },  
  "shortestDistanceBetweenPantographsInContactWithOCL": {  
    "type": "Property",  
    "value": "Bit religious Democrat happen material turn. Specific support four throw friend better hard."  
  },  
  "sleepingPlaces": {  
    "type": "Property",  
    "value": "Tv parent Republican risk chair manage."  
  },  
  "startingNoiseLevel": {  
    "type": "Property",  
    "value": 368.5  
  },  
  "staticAxleLoadExceptionalPayload": {  
    "type": "Property",  
    "value": 808.2  
  },  
  "staticAxleLoadNormalPayload": {  
    "type": "Property",  
    "value": 969.4  
  },  
  "staticAxleLoadWorkingOrder": {  
    "type": "Property",  
    "value": 169.6  
  },  
  "stationaryNoiseLevel": {  
    "type": "Property",  
    "value": 960.2  
  },  
  "structuralCategory": {  
    "type": "Property",  
    "value": "Identify development general dream director read. Surface identify than set on. Seat someone dinner military management our. Community upon soon total through business any"  
  },  
  "thermalCapacityDistance": {  
    "type": "Property",  
    "value": 880.6  
  },  
  "thermalCapacityGradient": {  
    "type": "Property",  
    "value": 214.0  
  },  
  "thermalCapacitySpeed": {  
    "type": "Property",  
    "value": 723.1  
  },  
  "thermalCapacityTime": {  
    "type": "Property",  
    "value": 559  
  },  
  "totalVehicleMass": {  
    "type": "Property",  
    "value": 770  
  },  
  "trainControlSwitchOverSpecialConditions": {  
    "type": "Property",  
    "value": "Garden off none. Operation whether think. Allow beat inside staff instead course throughout."  
  },  
  "transportableOnFerry": {  
    "type": "Property",  
    "value": false  
  },  
  "typeVersionNumber": {  
    "type": "Property",  
    "value": "Sense behavior song sound. Move pressure could budget industry mouth. Behavior clearly consider go television last court. Modern great either"  
  },  
  "usesGroup555": {  
    "type": "Property",  
    "value": false  
  },  
  "vehicleContactForce": {  
    "type": "Property",  
    "value": 581  
  },  
  "vehicleKinematicGaugeOther": {  
    "type": "Property",  
    "value": "Appear doctor capital house. Computer never after somebody it avoid hour loss. Once do certain probably situation form."  
  },  
  "vehicleMaxSandingOutput": {  
    "type": "Property",  
    "value": "Song"  
  },  
  "vehiclePantographHead": {  
    "type": "Property",  
    "value": "Four law toge"  
  },  
  "vehiclesComposingFixedFormation": {  
    "type": "Property",  
    "value": 936  
  },  
  "voiceOperationalCommImpl": {  
    "type": "Property",  
    "value": "Always old federal example southern article scene. Remain ten business citizen. Dinner eat radio expect."  
  },  
  "wheelSetGaugeTransformationMethod": {  
    "type": "Property",  
    "value": "Yes let price event him the. Deal anyone power goal size. Health hair gun."  
  },  
  "wheelchairSleepingPlaces": {  
    "type": "Property",  
    "value": "Word work TV south religious determine cost health. Blood during condition call fear dog fact. We consider memory member thing machine."  
  },  
  "wheelchairSpaces": {  
    "type": "Property",  
    "value": 162  
  },  
  "authorizedCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:authorizedCountry:PERT:93053146"  
  },  
  "axleBearingConditionMonitoring": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:axleBearingConditionMonitoring:CCZN:34387980"  
  },  
  "category": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:category:AEDK:98991004"  
  },  
  "certificate": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:certificate:HHEX:67346034"  
  },  
  "contactStripMaterial": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:contactStripMaterial:PLMZ:58684930"  
  },  
  "dataGSMRNetwork": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:dataGSMRNetwork:RYDV:40788619"  
  },  
  "dataRadioCompatible": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:dataRadioCompatible:OYYE:19201973"  
  },  
  "endCouplingType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:endCouplingType:DEOQ:00709281"  
  },  
  "energySupplySystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:energySupplySystem:HNOH:59530259"  
  },  
  "etcsBaseline": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:etcsBaseline:ZVIW:89968258"  
  },  
  "etcsEquipmentOnBoardLevel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:etcsEquipmentOnBoardLevel:LDSQ:19052030"  
  },  
  "etcsInfill": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:etcsInfill:CMPG:28278562"  
  },  
  "etcsSystemCompatibility": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:etcsSystemCompatibility:GDXQ:47023849"  
  },  
  "fireSafetyCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:fireSafetyCategory:VMTH:29585660"  
  },  
  "gaugingProfile": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:gaugingProfile:FEUN:57751305"  
  },  
  "gsmRRadioDataCommunication": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:gsmRRadioDataCommunication:YLBR:37462765"  
  },  
  "gsmRVersion": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:gsmRVersion:UBCL:09613572"  
  },  
  "legacyRadioSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:legacyRadioSystem:ELLB:75352099"  
  },  
  "manufacturer": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:manufacturer:FDPC:65877839"  
  },  
  "manufacturingCountry": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:manufacturingCountry:UZWO:23708623"  
  },  
  "parkingBrakeType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:parkingBrakeType:ECKZ:03938242"  
  },  
  "previousVehicleType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:previousVehicleType:YBYH:76750674"  
  },  
  "protectionLegacySystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:protectionLegacySystem:LCWC:09456788"  
  },  
  "railInclination": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:railInclination:SOQI:23066927"  
  },  
  "snowIceHailConditions": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:snowIceHailConditions:ANVC:85896399"  
  },  
  "subCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:subCategory:QNRI:66699553"  
  },  
  "supportedPlatformHeight": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:supportedPlatformHeight:JAFW:51092220"  
  },  
  "thermalCapacityTSIReference": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:thermalCapacityTSIReference:WYVV:17981245"  
  },  
  "trainDetectionSystemType": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:trainDetectionSystemType:MWEE:16904766"  
  },  
  "typeVersionId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:typeVersionId:IIUR:73666806"  
  },  
  "vehicleTypeMaximumSpeedAndCantDeficiency": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:vehicleTypeMaximumSpeedAndCantDeficiency:BJFD:77408810"  
  },  
  "voiceGSMRNetwork": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:voiceGSMRNetwork:QIGX:11968970"  
  },  
  "voiceRadioCompatible": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:voiceRadioCompatible:YHFQ:69492946"  
  },  
  "wheelSetGauge": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:wheelSetGauge:LLNN:97698765"  
  },  
  "wheelSetGaugeChangeoverFacility": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleType:wheelSetGaugeChangeoverFacility:NFUQ:89252235"  
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
    

<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：具有共同特征的子集  
============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.ERA/blob/master/SubsetWithCommonCharacteristics/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：** 成员国线路区段和/或运营点共有的项目子集。就基础设施登记册而言，每个基础设施管理者应至少通过线路区段和运营点，并可选择通过共同特征子集来描述其铁路网络**。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `IdPhoneErtmsRadioBlockCenter[string]`: ERTMS/ETCS 无线电模块中心的 ID 和电话号码  - `TSIMagneticFields[uri]`: 车辆发射磁场规则的存在和 TSI 合规性  - `TSITractionHarmonics[uri]`: 车辆牵引电流中谐波限值的存在和 TSI 合规性  - `accelerationLevelCrossing[string]`: 平交道口允许加速  - `additionalBrakingInformationDocument[string]`: IM 提供的有关制动性能的文件  - `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 在公共街道上标识特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atoCommunicationSystem[uri]`: ATO 通信系统  - `atoErrorCorrectionsOnboard[string]`: 机载设备需要进行 ATO 误差修正  - `atoGradeAutomation[uri]`: ATO 自动化等级  - `atoSystemVersion[uri]`: ATO 系统版本  - `automaticDroppingDeviceRequired[boolean]`: 需要自动投放装置  - `bigMetalMass[boolean]`: 大金属块  - `cantDeficiency[number]`: 缺钙  - `cantDeficiencyBasicSSP[uri]`: 用于基本 SSP 的 Cant Deficiency  - `compatibilityProcedureDocument[string]`: 包含静态和动态路由兼容性检查程序的文件  - `conditionsSwitchClassBSystems[string]`: 在 ERTMS/ETCS 和 B 类系统之间切换所需的特殊技术条件  - `conditionsSwitchTrainProtectionSystems[string]`: 在不同 B 级列车保护、控制和警报系统之间切换的特殊条件  - `conditionsUseReflectivePlates[uri]`: 使用反光板的条件  - `contactLineSystem[uri]`: 接触线系统  - `contactStripMaterial[uri]`: 允许使用的接触带材料  - `contactStripMaterialMetallicContent[number]`: 接触带材料的金属含量  - `dNvovtrp[number]`: D_NVOVTRP  - `dNvpotrp[number]`: D_NVPOTRP  - `dNvroll[number]`: D_NVROLL  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dataRadioCompatible[uri]`: 无线电系统兼容性数据  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `demonstrationENE[string]`: EI 轨道示范申报（ENE）  - `description[string]`: 项目描述  - `distSignToPhaseEnd[number]`: 标志牌与相位分离终点之间的距离  - `documentRestrictionPositionContactLineSeparation[string]`: 与多重牵引装置位置有关的限制性文件，以符合接触线分离的要求  - `documentRestrictionPowerConsumption[string]`: 与特定电力牵引装置耗电量有关的限制文件  - `eddyCurrentBraking[uri]`: 使用涡流制动器  - `eddyCurrentBrakingConditionsDocument[string]`: 符合涡流制动器使用条件的文件  - `etcsDegradedSituation[uri]`: 降级情况下的 ETCS 等级  - `etcsErrorCorrectionsOnboard[string]`: 车载 ETCS 系统所需的误差修正  - `etcsImplementsLevelCrossingProcedure[boolean]`: ETCS 轨道旁实施平交道口程序或同等解决方案  - `etcsInfill[uri]`: 线路侧安装 ETCS 填充物  - `etcsInfillLineAccess[boolean]`: 线路接入所需的 ETCS 填充  - `etcsLevel[uri]`: 等 级  - `etcsMVersion[uri]`: ETCS M_version  - `etcsNationalPacket44[boolean]`: 实施 ETCS 国家数据包 44 应用  - `etcsOptionalFunctions[string]`: ETCS 可选功能  - `etcsSystemFunctionalitiesNextFiveYears[string]`: 未来 5 年需要 ETCS 系统 2.2 或 3.0 版功能  - `etcsTransmitsTrackConditions[boolean]`: 轨道旁的 ETCS 是否能传输轨道状况  - `etcsTransmittedTrackConditions[uri]`: 可传输的轨道条件  - `flangeLubeForbidden[boolean]`: 禁止使用法兰润滑  - `freightCorridor[uri]`: 铁路货运走廊的一部分  - `gaugingCheckLocation[string]`: 需要特别检查的特定点的铁路位置  - `gaugingProfile[uri]`: 测量  - `gaugingTransversalDocument[string]`: 记录需要进行特定检查的特殊点的横向部分  - `gprsForETCS[boolean]`: 用于 ETCS 的 GPRS  - `gprsImplementationArea[string]`: 实施 GPRS 的地区  - `gradientProfile[string]`: 梯度轮廓  - `gsmRActiveMobiles[uri]`: ETCS 2 级（或 3 级）在不中断运行的情况下进行无线电模块中心切换所需的有效 GSM-R 移动电话（EDOR）或车载同时通信会话的数量  - `gsmRAdditionalInfo[string]`: 有关网络特性的其他信息  - `gsmRNoCoverage[boolean]`: 无 GSM-R 覆盖范围  - `gsmROptionalFunctions[uri]`: 可选的 GSM-R 功能  - `gsmRVersion[uri]`: GSM-R 版本  - `gsmrConstraintsOperateOnlyInCircuitSwitch[uri]`: GSM-R 网络运营商对只能在电路开关中运行的 ETCS 车载装置施加的特定限制  - `gsmrErrorCorrectionsOnboard[string]`: 机载 GSM-R 所需的纠错功能  - `gsmrForcedDeregistrationFunctionalNumber[boolean]`: GSM-R 网络的配置允许另一司机强制取消功能号码注册  - `gsmrNetworkCoverage[uri]`: 漫游协议覆盖的 GSM-R 网络  - `hasAdditionalBrakingInformation[boolean]`: IM 可提供的补充信息  - `hasBallast[boolean]`: 压舱物的存在  - `hasETCSRestrictionsConditions[boolean]`: 运行限制或条件的存在  - `hasHotAxleBoxDetector[boolean]`: 轨道旁热轴箱探测器（HABD）的存在  - `hasLevelCrossings[boolean]`: 平交道口的存在  - `hasOtherTrainProtection[boolean]`: 是否安装了其他列车保护、控制和警报系统  - `hasSevereWeatherConditions[boolean]`: 存在恶劣的气候条件  - `hasSystemSeparation[boolean]`: 系统分离  - `hasTSITrainDetection[boolean]`: 存在完全符合 TSI 标准的列车探测系统  - `highSpeedLoadModelCompliance[boolean]`: 结构符合高速载荷模型（HSLM）动态载荷模型的要求  - `hotAxleBoxDetectorDirection[uri]`: 热轴箱探测器方向  - `hotAxleBoxDetectorGeneration[string]`: 生成轨道旁的人与生物圈数据  - `hotAxleBoxDetectorIdentification[string]`: 轨道旁人与生物圈保护区的识别  - `hotAxleBoxDetectorLocation[number]`: 轨道旁危险货物装卸区的铁路位置  - `hotAxleBoxDetectorTSICompliant[boolean]`: 符合轨道旁 HABD TSI 标准  - `id[*]`: 实体的唯一标识符  - `instructionsSwitchRadioSystems[string]`: 在不同无线电系统之间切换的特殊指令  - `isQuietRoute[boolean]`: 属于较安静的路线  - `legacyRadioSystem[uri]`: 已安装的其他无线电系统（无线电遗留系统）  - `lineCategory[uri]`: 生产线类别  - `linesideDistanceIndicationAppearance[uri]`: 线侧距离指示外观  - `linesideDistanceIndicationFrequency[number]`: 线侧距离指示频率  - `linesideDistanceIndicationPositioning[uri]`: 线侧距离指示定位  - `loadCapability[uri]`: 负载能力  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `mNvcontact[uri]`: M_NVCONTACT  - `mNvderun[boolean]`: M_NVDERUN  - `magneticBraking[uri]`: 使用磁性制动器  - `magneticBrakingConditionsDocument[string]`: 符合磁力制动器使用条件的文件  - `maximumAltitude[number]`: 最高海拔  - `maximumBrakingDistance[number]`: 要求的最大制动距离  - `maximumContactWireHeight[number]`: 最大接触线高度  - `maximumPermittedSpeed[number]`: 最大允许速度  - `maximumTemperature[number]`: 温度范围（最大值）  - `maximumTrainDeceleration[number]`: 列车最大减速  - `minDistConsecutiveAxles[number]`: 两个连续车轴之间的最小允许距离  - `minDistFirstLastAxle[number]`: 第一轴和最后轴之间的最小允许距离  - `minFlangeHeight[number]`: 法兰允许的最小高度  - `minFlangeThickness[number]`: 法兰允许的最小厚度  - `minRimWidth[number]`: 轮辋最小允许宽度  - `minWheelDiameter[number]`: 允许的最小车轮直径  - `minimumContactWireHeight[number]`: 最小接触线高度  - `minimumHorizontalRadius[number]`: 水平曲线最小半径  - `minimumTemperature[number]`: 温度范围（最小值）  - `minimumWheelDiameter[number]`: 固定钝角交叉路口的最小车轮直径  - `multipleTrainProtectionRequired[boolean]`: 需要在车上安装一个以上的列车保护、控制和警报系统  - `name[string]`: 该项目的名称  - `nationalLoadCapability[string]`: 国家负载能力分类  - `nationalValuesBrakeModel[string]`: 制动模型使用的国家数值  - `osmClass[uri]`: 开放式街道地图类  - `otherCantDeficiencyBasicSSP[uri]`: ETCS 轨道旁配置为提供 SSP 的其他 Cant Deficiency 列车类别  - `otherPantographHead[uri]`: 接受其他受电弓头  - `otherTrainProtection[uri]`: 其他列车保护、控制和警报系统，以应对恶化的情况  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `passesThroughTunnel[uri]`: 通过隧道  - `permitUseReflectivePlates[boolean]`: 反光板使用许可  - `permittedContactForce[string]`: 允许的接触力  - `phaseInfo[string]`: 有关相分离的信息  - `phaseSeparation[boolean]`: 相分离  - `platform[uri]`: 平台  - `profileNumberSemiTrailers[uri]`: 半挂车标准组合运输型材编号  - `profileNumberSwapBodies[uri]`: 交换机构的标准综合运输配置文件编号  - `protectionLegacySystem[uri]`: 列车保护传统系统  - `publicNetworkRoaming[boolean]`: GSM-R 存在向公共网络漫游的问题  - `publicNetworkRoamingDetails[string]`: GSM-R 关于漫游至公共网络的详细信息  - `qNvdriverAdhes[uri]`: q_nvdriver_adhes  - `qNvemrrls[uri]`: Q_NVEMRRLS  - `qNvsbtsmperm[boolean]`: Q_NVSBTSMPERM  - `radioNetworkId[number]`: 无线电网络 ID  - `railInclination[uri]`: 轨道倾斜度  - `railSystemType[string]`: 轨道系统类型  - `raisedPantographsDistanceAndSpeed[string]`: 给定速度下对升高的受电弓数量和间距的要求  - `reasonsEtcsRadioBlockCenterReject[uri]`: ETCS 无线电模块中心拒绝接受列车的原因  - `redLightsRequired[boolean]`: 需要稳定的红灯  - `safeConsistLengthInformationNecessary[uri]`: 获取线路和 SIL 所需的机载安全长度信息  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `specificInformation[string]`: 具体信息  - `standardCombinedTransporRollerUnits[uri]`: 滚筒装置的标准组合运输型材编号  - `standardCombinedTransportContainers[uri]`: 集装箱标准综合运输配置文件编号  - `structureCheckLocation[number]`: 需要特别检查的铁路结构位置  - `subsetName[string]`: 具有共同特征的子集名称  - `switchProtectControlWarning[boolean]`: 运行时不同保护、控制和警报系统之间存在切换  - `switchRadioSystem[boolean]`: 存在不同无线电系统之间的切换  - `systemSeparationInfo[string]`: 系统分离信息  - `tNvcontact[number]`: T_NVCONTACT  - `tNvovtrp[number]`: T_NVOVTRP  - `temperatureRange[uri]`: 温度范围  - `tenGISId[string]`: TEN GIS 身份  - `tiltingSupported[boolean]`: 指示 ETCS 是否支持倾斜功能  - `trackLoadCapability[uri]`: 轨道负载能力  - `trackPhaseInfo[uri]`: 轨道阶段信息  - `trackRaisedPantographsDistanceAndSpeed[uri]`: 跟踪升高的受电弓距离和速度  - `trackSystemSeparationInfo[uri]`: 轨道系统分离信息  - `trainDetectionSystem[uri]`: 火车探测系统  - `trainIntegrityOnBoardRequired[boolean]`: 必须在车上（而非司机）确认列车完整性，才能进入线路  - `tsiPantographHead[uri]`: 接受符合 TSI 标准的受电弓头  - `tsiSwitchCrossing[boolean]`: 符合 TSI 标准的开关和交叉路口服务值  - `type[string]`: NGSI 数据类型。它必须是 SubsetWithCommonCharacteristics（具有共同特征的子集）。  - `usesGroup555[boolean]`: GSM-R 使用 555 组  - `vNvallowovtrp[number]`: V_NVALLOWOVTRP  - `vNvsupovtrp[number]`: V_NVSUPOVTRP  - `vehicleTypesCompatibleTrafficLoad[string]`: 已确定与基础设施和列车检测系统的交通负荷和承载能力相匹配的车辆类型清单  - `vehiclesCompatibleTrafficLoad[string]`: 已确定与基础设施和列车检测系统的交通负荷和承载能力相匹配的车辆清单  - `verificationCCS[string]`: 欧共体轨道核查声明（CCS）  - `verificationENE[string]`: 欧共体轨道核查声明 (ENE)  <!-- /30-PropertiesList -->  
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
SubsetWithCommonCharacteristics:    
  description: 'Subset of items shared by sections of lines and/or operational points of a member state. For the purposes of the register of infrastructure, each infrastructure manager shall describe its railway network at least by sections of line and operational points and optionally via common characteristic subsets.'    
  properties:    
    IdPhoneErtmsRadioBlockCenter:    
      description: ID and phone number of ERTMS/ETCS Radio Block Center    
      type: string    
      x-ngsi:    
        type: Property    
    TSIMagneticFields:    
      description: Existence and TSI compliance of rules for magnetic fields emitted by a vehicle    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    TSITractionHarmonics:    
      description: Existence and TSI compliance of limits in harmonics in the traction current of vehicles    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    accelerationLevelCrossing:    
      description: Acceleration allowed at level crossing    
      type: string    
      x-ngsi:    
        type: Property    
    additionalBrakingInformationDocument:    
      description: Documents available by the IM relating to braking performance    
      type: string    
      x-ngsi:    
        type: Property    
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
    atoCommunicationSystem:    
      description: ATO communication system    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    atoErrorCorrectionsOnboard:    
      description: ATO error corrections required for the on-board    
      type: string    
      x-ngsi:    
        type: Property    
    atoGradeAutomation:    
      description: ATO Grade of Automation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    atoSystemVersion:    
      description: ATO System version    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    automaticDroppingDeviceRequired:    
      description: Automatic dropping device required    
      type: boolean    
      x-ngsi:    
        type: Property    
    bigMetalMass:    
      description: Big metal mass    
      type: boolean    
      x-ngsi:    
        type: Property    
    cantDeficiency:    
      description: Cant deficiency    
      type: number    
      x-ngsi:    
        type: Property    
    cantDeficiencyBasicSSP:    
      description: Cant Deficiency used for the basic SSP    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    compatibilityProcedureDocument:    
      description: Document with the procedure(s) for static and dynamic route compatibility checks    
      type: string    
      x-ngsi:    
        type: Property    
    conditionsSwitchClassBSystems:    
      description: Special technical conditions required to switch over between ERTMS/ETCS and Class B systems    
      type: string    
      x-ngsi:    
        type: Property    
    conditionsSwitchTrainProtectionSystems:    
      description: 'Special conditions to switch over between different class B train protection, control and warning systems'    
      type: string    
      x-ngsi:    
        type: Property    
    conditionsUseReflectivePlates:    
      description: Conditions for use of reflective plates    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    contactLineSystem:    
      description: Contact line system    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    contactStripMaterial:    
      description: Permitted contact strip material    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    contactStripMaterialMetallicContent:    
      description: Contact strip material metallic content    
      type: number    
      x-ngsi:    
        type: Property    
    dNvovtrp:    
      description: D_NVOVTRP    
      type: number    
      x-ngsi:    
        type: Property    
    dNvpotrp:    
      description: D_NVPOTRP    
      type: number    
      x-ngsi:    
        type: Property    
    dNvroll:    
      description: D_NVROLL    
      type: number    
      x-ngsi:    
        type: Property    
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
    demonstrationENE:    
      description: EI declaration of demonstration for track (ENE)    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    distSignToPhaseEnd:    
      description: Distance between signboard and phase separation ending    
      type: number    
      x-ngsi:    
        type: Property    
    documentRestrictionPositionContactLineSeparation:    
      description: Document with restriction related to the position of Multiple Traction unit(s) to comply with contact line separation    
      type: string    
      x-ngsi:    
        type: Property    
    documentRestrictionPowerConsumption:    
      description: Document with restriction related to power consumption of specific electric traction unit(s)    
      type: string    
      x-ngsi:    
        type: Property    
    eddyCurrentBraking:    
      description: Use of eddy current brakes    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    eddyCurrentBrakingConditionsDocument:    
      description: Document with the conditions for the use of eddy current brakes    
      type: string    
      x-ngsi:    
        type: Property    
    etcsDegradedSituation:    
      description: ETCS level for degraded situation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    etcsErrorCorrectionsOnboard:    
      description: ETCS error corrections required for the on-board    
      type: string    
      x-ngsi:    
        type: Property    
    etcsImplementsLevelCrossingProcedure:    
      description: ETCS trackside implements level crossing procedure or an equivalent solution    
      type: boolean    
      x-ngsi:    
        type: Property    
    etcsInfill:    
      description: ETCS infill installed lineside    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    etcsInfillLineAccess:    
      description: ETCS infill necessary for line access    
      type: boolean    
      x-ngsi:    
        type: Property    
    etcsLevel:    
      description: Etcs level    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    etcsMVersion:    
      description: ETCS M_version    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    etcsNationalPacket44:    
      description: ETCS national packet 44 application implemented    
      type: boolean    
      x-ngsi:    
        type: Property    
    etcsOptionalFunctions:    
      description: ETCS optional functions    
      type: string    
      x-ngsi:    
        type: Property    
    etcsSystemFunctionalitiesNextFiveYears:    
      description: ETCS system version 2.2 or 3.0 functionalities to be required in the next 5 years    
      type: string    
      x-ngsi:    
        type: Property    
    etcsTransmitsTrackConditions:    
      description: Is the ETCS trackside engineered to transmit Track Conditions    
      type: boolean    
      x-ngsi:    
        type: Property    
    etcsTransmittedTrackConditions:    
      description: Track conditions which can be transmitted    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    flangeLubeForbidden:    
      description: Use of flange lubrication forbidden    
      type: boolean    
      x-ngsi:    
        type: Property    
    freightCorridor:    
      description: Part of a Railway freight corridor    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    gaugingCheckLocation:    
      description: Railway location of particular points requiring specific checks    
      type: string    
      x-ngsi:    
        type: Property    
    gaugingProfile:    
      description: Gauging    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    gaugingTransversalDocument:    
      description: Document with the transversal section of the particular points requiring specific checks    
      type: string    
      x-ngsi:    
        type: Property    
    gprsForETCS:    
      description: GPRS for ETCS    
      type: boolean    
      x-ngsi:    
        type: Property    
    gprsImplementationArea:    
      description: Area of implementation of GPRS    
      type: string    
      x-ngsi:    
        type: Property    
    gradientProfile:    
      description: Gradient profile    
      type: string    
      x-ngsi:    
        type: Property    
    gsmRActiveMobiles:    
      description: Number of active GSM-R mobiles (EDOR) or simultaneous communication session on-board for ETCS Level 2 (or level 3) needed to perform radio block centre handovers without having an operational disruption    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    gsmRAdditionalInfo:    
      description: Additional information on network characteristics    
      type: string    
      x-ngsi:    
        type: Property    
    gsmRNoCoverage:    
      description: No GSM-R coverage    
      type: boolean    
      x-ngsi:    
        type: Property    
    gsmROptionalFunctions:    
      description: Optional GSM-R functions    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    gsmRVersion:    
      description: GSM-R version    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    gsmrConstraintsOperateOnlyInCircuitSwitch:    
      description: Specific constraints imposed by the GSM-R network operator on ETCS on-board units only able to operate in circuit-switch    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    gsmrErrorCorrectionsOnboard:    
      description: GSM-R error corrections required for the on-board    
      type: string    
      x-ngsi:    
        type: Property    
    gsmrForcedDeregistrationFunctionalNumber:    
      description: GSM-R network is configured to allow forced de-registration of a functional number by another driver    
      type: boolean    
      x-ngsi:    
        type: Property    
    gsmrNetworkCoverage:    
      description: GSM-R networks covered by a roaming agreement    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    hasAdditionalBrakingInformation:    
      description: Availability by the IM of additional information    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasBallast:    
      description: Existence of ballast    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasETCSRestrictionsConditions:    
      description: Existence of operating restrictions or conditions    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasHotAxleBoxDetector:    
      description: Existence of trackside hot axle box detector (HABD)    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasLevelCrossings:    
      description: Existence of level crossings    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasOtherTrainProtection:    
      description: 'Existence of other train protection, control and warning systems installed'    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasSevereWeatherConditions:    
      description: Existence of severe climatic conditions    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasSystemSeparation:    
      description: System separation    
      type: boolean    
      x-ngsi:    
        type: Property    
    hasTSITrainDetection:    
      description: Existence of train detection system fully compliant with the TSI    
      type: boolean    
      x-ngsi:    
        type: Property    
    highSpeedLoadModelCompliance:    
      description: Compliance of structures with the High Speed Load Model (HSLM) dynamic load model    
      type: boolean    
      x-ngsi:    
        type: Property    
    hotAxleBoxDetectorDirection:    
      description: Hot axle box detector direction    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    hotAxleBoxDetectorGeneration:    
      description: Generation of trackside HABD    
      type: string    
      x-ngsi:    
        type: Property    
    hotAxleBoxDetectorIdentification:    
      description: Identification of trackside HABD    
      type: string    
      x-ngsi:    
        type: Property    
    hotAxleBoxDetectorLocation:    
      description: Railway location of trackside HABD    
      type: number    
      x-ngsi:    
        type: Property    
    hotAxleBoxDetectorTSICompliant:    
      description: Trackside HABD TSI compliant    
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
    instructionsSwitchRadioSystems:    
      description: Special instructions to switch over between different radio systems    
      type: string    
      x-ngsi:    
        type: Property    
    isQuietRoute:    
      description: Belonging to a quieter route    
      type: boolean    
      x-ngsi:    
        type: Property    
    legacyRadioSystem:    
      description: Other radio systems installed (Radio Legacy Systems)    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    lineCategory:    
      description: Category of line    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    linesideDistanceIndicationAppearance:    
      description: Lineside distance indication appearance    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    linesideDistanceIndicationFrequency:    
      description: Lineside distance indication frequency    
      type: number    
      x-ngsi:    
        type: Property    
    linesideDistanceIndicationPositioning:    
      description: Lineside distance indication positioning    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    loadCapability:    
      description: Load Capability    
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
    mNvcontact:    
      description: M_NVCONTACT    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    mNvderun:    
      description: M_NVDERUN    
      type: boolean    
      x-ngsi:    
        type: Property    
    magneticBraking:    
      description: Use of magnetic brakes    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    magneticBrakingConditionsDocument:    
      description: Document with the conditions for the use of magnetic brakes    
      type: string    
      x-ngsi:    
        type: Property    
    maximumAltitude:    
      description: Maximum altitude    
      type: number    
      x-ngsi:    
        type: Property    
    maximumBrakingDistance:    
      description: Maximum braking distance requested    
      type: number    
      x-ngsi:    
        type: Property    
    maximumContactWireHeight:    
      description: Maximum contact wire height    
      type: number    
      x-ngsi:    
        type: Property    
    maximumPermittedSpeed:    
      description: Maximum permitted speed    
      type: number    
      x-ngsi:    
        type: Property    
    maximumTemperature:    
      description: Temperature range (maximum)    
      type: number    
      x-ngsi:    
        type: Property    
    maximumTrainDeceleration:    
      description: Maximum train deceleration    
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
    minWheelDiameter:    
      description: Minimum permitted wheel diameter    
      type: number    
      x-ngsi:    
        type: Property    
    minimumContactWireHeight:    
      description: Minimum contact wire height    
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
    multipleTrainProtectionRequired:    
      description: 'Need for more than one train protection, control and warning system required on board'    
      type: boolean    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nationalLoadCapability:    
      description: National classification for load capability    
      type: string    
      x-ngsi:    
        type: Property    
    nationalValuesBrakeModel:    
      description: National Values used for the brake model    
      type: string    
      x-ngsi:    
        type: Property    
    osmClass:    
      description: Open street map class    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    otherCantDeficiencyBasicSSP:    
      description: Other Cant Deficiency train categories for which the ETCS trackside is configured to provide SSP    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    otherPantographHead:    
      description: Accepted other pantograph heads    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    otherTrainProtection:    
      description: 'Other train protection, control and warning systems for degraded situation'    
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
    passesThroughTunnel:    
      description: Passes through tunnel    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    permitUseReflectivePlates:    
      description: Permit of use of reflective plates    
      type: boolean    
      x-ngsi:    
        type: Property    
    permittedContactForce:    
      description: Contact force permitted    
      type: string    
      x-ngsi:    
        type: Property    
    phaseInfo:    
      description: Information on phase separation    
      type: string    
      x-ngsi:    
        type: Property    
    phaseSeparation:    
      description: Phase separation    
      type: boolean    
      x-ngsi:    
        type: Property    
    platform:    
      description: Platform    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    profileNumberSemiTrailers:    
      description: Standard combined transport profile number for semi-trailers    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    profileNumberSwapBodies:    
      description: Standard combined transport profile number for swap bodies    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    protectionLegacySystem:    
      description: Train protection legacy system    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    publicNetworkRoaming:    
      description: GSM-R existence of roaming to public networks    
      type: boolean    
      x-ngsi:    
        type: Property    
    publicNetworkRoamingDetails:    
      description: GSM-R details on roaming to public networks    
      type: string    
      x-ngsi:    
        type: Property    
    qNvdriverAdhes:    
      description: Q_NVDRIVER_ADHES    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    qNvemrrls:    
      description: Q_NVEMRRLS    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    qNvsbtsmperm:    
      description: Q_NVSBTSMPERM    
      type: boolean    
      x-ngsi:    
        type: Property    
    radioNetworkId:    
      description: Radio Network ID    
      type: number    
      x-ngsi:    
        type: Property    
    railInclination:    
      description: Rail inclination    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    railSystemType:    
      description: Rail system type    
      type: string    
      x-ngsi:    
        type: Property    
    raisedPantographsDistanceAndSpeed:    
      description: 'Requirements for number of raised pantographs and spacing between them, at the given speed'    
      type: string    
      x-ngsi:    
        type: Property    
    reasonsEtcsRadioBlockCenterReject:    
      description: Reasons for which an ETCS Radio Block Center can reject a train    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    redLightsRequired:    
      description: Steady red lights required    
      type: boolean    
      x-ngsi:    
        type: Property    
    safeConsistLengthInformationNecessary:    
      description: Safe consist length information from on-board necessary for access the line and SIL    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    specificInformation:    
      description: Specific information    
      type: string    
      x-ngsi:    
        type: Property    
    standardCombinedTransporRollerUnits:    
      description: Standard combined transport profile number for roller units    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    standardCombinedTransportContainers:    
      description: Standard combined transport profile number for containers    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    structureCheckLocation:    
      description: Railway location of structures requiring specific checks    
      type: number    
      x-ngsi:    
        type: Property    
    subsetName:    
      description: Name of a subset with common characteristics    
      type: string    
      x-ngsi:    
        type: Property    
    switchProtectControlWarning:    
      description: 'Existence of switch over between different protection, control and warning systems while running'    
      type: boolean    
      x-ngsi:    
        type: Property    
    switchRadioSystem:    
      description: Existence of switch over between different radio systems    
      type: boolean    
      x-ngsi:    
        type: Property    
    systemSeparationInfo:    
      description: Information on system separation    
      type: string    
      x-ngsi:    
        type: Property    
    tNvcontact:    
      description: T_NVCONTACT    
      type: number    
      x-ngsi:    
        type: Property    
    tNvovtrp:    
      description: T_NVOVTRP    
      type: number    
      x-ngsi:    
        type: Property    
    temperatureRange:    
      description: Temperature range    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tenGISId:    
      description: TEN GIS identity    
      type: string    
      x-ngsi:    
        type: Property    
    tiltingSupported:    
      description: Indication whether tilting functions are supported by ETCS    
      type: boolean    
      x-ngsi:    
        type: Property    
    trackLoadCapability:    
      description: Track load capability    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trackPhaseInfo:    
      description: Track phase info    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trackRaisedPantographsDistanceAndSpeed:    
      description: Track raised pantograph distance and speed    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trackSystemSeparationInfo:    
      description: Track system separation info    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trainDetectionSystem:    
      description: Train detection system    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trainIntegrityOnBoardRequired:    
      description: Train integrity confirmation from on-board (not from driver) necessary for line access    
      type: boolean    
      x-ngsi:    
        type: Property    
    tsiPantographHead:    
      description: Accepted TSI compliant pantograph heads    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    tsiSwitchCrossing:    
      description: TSI compliance of in service values for switches and crossings    
      type: boolean    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI data type. It has to be SubsetWithCommonCharacteristics    
      enum:    
        - SubsetWithCommonCharacteristics    
      type: string    
      x-ngsi:    
        type: Property    
    usesGroup555:    
      description: GSM-R use of group 555    
      type: boolean    
      x-ngsi:    
        type: Property    
    vNvallowovtrp:    
      description: V_NVALLOWOVTRP    
      type: number    
      x-ngsi:    
        type: Property    
    vNvsupovtrp:    
      description: V_NVSUPOVTRP    
      type: number    
      x-ngsi:    
        type: Property    
    vehicleTypesCompatibleTrafficLoad:    
      description: List of vehicle types already identified as compatible with Traffic load and load carrying capacity of infrastructure and train detection systems    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclesCompatibleTrafficLoad:    
      description: List of vehicles already identified as compatible with Traffic load and load carrying capacity of infrastructure and train detection systems    
      type: string    
      x-ngsi:    
        type: Property    
    verificationCCS:    
      description: EC declaration of verification for track (CCS)    
      type: string    
      x-ngsi:    
        type: Property    
    verificationENE:    
      description: EC declaration of verification for track (ENE)    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/SubsetWithCommonCharacteristics    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/SubsetWithCommonCharacteristics/LICENSE.md    
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
#### SubsetWithCommonCharacteristics NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 SubsetWithCommonCharacteristics 的示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SubsetWithCommonCharacteristics:id:YPHZ:97109776",  
  "dateCreated": "2022-10-05T07:31:49Z",  
  "dateModified": "2011-08-27T16:37:28Z",  
  "source": "Toward should once hear test. Most least fish record break prevent.",  
  "name": "Later dis",  
  "alternateName": "Statement make according agree may might partner someone. Fund accept compare firm a late.",  
  "description": "Else difficult security young. Ok turn number. Reflect s",  
  "dataProvider": "Modern boy coach sea clearly.",  
  "owner": [  
    "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:DWBT:01785577",  
    "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:CIWU:39426109"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:WISG:95955862"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      19.420622,  
      125.057551  
    ]  
  },  
  "address": {  
    "streetAddress": "Until mind clear out series event each. Concern hand organization drug. Animal cup within energy. Save decisio",  
    "addressLocality": "Turn medical majority white ready source. Middle dinner participant large TV. Increase summer yourself since though.",  
    "addressRegion": "Out now day. C",  
    "addressCountry": "Relate PM look party possible. Science Mrs information newspaper. Local husband share Republican development book food Mr.",  
    "postalCode": "Morning car large their page. Home agen",  
    "postOfficeBoxNumber": "Bar draw leg weste",  
    "streetNr": "Idea ",  
    "district": "Establish bring just. Follow line run old. Win mean market coach enter begin physica"  
  },  
  "areaServed": "Career institution start",  
  "type": "SubsetWithCommonCharacteristics",  
  "IdPhoneErtmsRadioBlockCenter": "Building none down investment possible member country.",  
  "accelerationLevelCrossing": "World middle talk into understand paper.",  
  "additionalBrakingInformationDocument": "Understand house degree though. System she science election.",  
  "atoErrorCorrectionsOnboard": "Cover close yes simple entire.",  
  "automaticDroppingDeviceRequired": true,  
  "bigMetalMass": true,  
  "cantDeficiency": 864,  
  "compatibilityProcedureDocument": "American whole magazine truth stop whose. On traditional measure example sens",  
  "conditionsSwitchClassBSystems": "Together range line beyon",  
  "conditionsSwitchTrainProtectionSystems": "Trouble behavior style report size perso",  
  "contactStripMaterialMetallicContent": 864,  
  "dNvovtrp": 864,  
  "dNvpotrp": 864,  
  "dNvroll": 864,  
  "demonstrationENE": "American whole magazine truth stop who",  
  "distSignToPhaseEnd": 864,  
  "documentRestrictionPositionContactLineSeparation": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "documentRestrictionPowerConsumption": "Togethe",  
  "eddyCurrentBrakingConditionsDocument": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "etcsErrorCorrectionsOnboard": "Language ball floor meet usually ",  
  "etcsImplementsLevelCrossingProcedure": false,  
  "etcsInfillLineAccess": false,  
  "etcsNationalPacket44": true,  
  "etcsOptionalFunctions": "First drug contain start almost wonder. Live bed serious theory type. Together type music hospital. Every speech support time operation wear often",  
  "etcsSystemFunctionalitiesNextFiveYears": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and.",  
  "etcsTransmitsTrackConditions": true,  
  "flangeLubeForbidden": true,  
  "gaugingCheckLocation": "Paper office hospital have wonder. Painting create wife.",  
  "gaugingTransversalDocument": "Decision song view age international big employee. Author",  
  "gprsForETCS": true,  
  "gprsImplementationArea": "Employee toward like total now. Whom around put suddenly garden. Bring TV prog",  
  "gradientProfile": "True power home price check real leader. From animal exactly drive. Good explain grow water plant perform resource.",  
  "gsmRAdditionalInfo": "Stock ball organization re",  
  "gsmRNoCoverage": false,  
  "gsmrErrorCorrectionsOnboard": "Traditional page a although for study anyone. Could yourself plan base rise would. We",  
  "gsmrForcedDeregistrationFunctionalNumber": true,  
  "hasAdditionalBrakingInformation": true,  
  "hasBallast": true,  
  "hasETCSRestrictionsConditions": true,  
  "hasHotAxleBoxDetector": false,  
  "hasLevelCrossings": false,  
  "hasOtherTrainProtection": true,  
  "hasSevereWeatherConditions": true,  
  "hasSystemSeparation": false,  
  "hasTSITrainDetection": false,  
  "highSpeedLoadModelCompliance": true,  
  "hotAxleBoxDetectorGeneration": "Trial son break either president.",  
  "hotAxleBoxDetectorIdentification": "The everything affect American. Next water voice travel among. Pretty Republican total policy head Mrs debate onto.",  
  "hotAxleBoxDetectorLocation": 860.4,  
  "hotAxleBoxDetectorTSICompliant": true,  
  "instructionsSwitchRadioSystems": "Force pass top better",  
  "isQuietRoute": true,  
  "linesideDistanceIndicationFrequency": 864,  
  "mNvderun": false,  
  "magneticBrakingConditionsDocument": "Else memory if. Whose gro",  
  "maximumAltitude": 704.6,  
  "maximumBrakingDistance": 864,  
  "maximumContactWireHeight": 957.2,  
  "maximumPermittedSpeed": 864,  
  "maximumTemperature": 864,  
  "maximumTrainDeceleration": 786.9,  
  "minDistConsecutiveAxles": 864,  
  "minDistFirstLastAxle": 864,  
  "minFlangeHeight": 950.4,  
  "minFlangeThickness": 531.9,  
  "minRimWidth": 663.5,  
  "minWheelDiameter": 864,  
  "minimumContactWireHeight": 911.5,  
  "minimumHorizontalRadius": 864,  
  "minimumTemperature": 864,  
  "minimumWheelDiameter": 864,  
  "multipleTrainProtectionRequired": false,  
  "nationalLoadCapability": "Else memor",  
  "nationalValuesBrakeModel": "Financial role together range. Nice government first po",  
  "permitUseReflectivePlates": true,  
  "permittedContactForce": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "phaseInfo": "On",  
  "phaseSeparation": false,  
  "publicNetworkRoaming": false,  
  "publicNetworkRoamingDetails": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and.",  
  "qNvsbtsmperm": true,  
  "radioNetworkId": 864,  
  "railSystemType": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "raisedPantographsDistanceAndSpeed": "Together range line beyond. First policy daughter need kind miss.",  
  "redLightsRequired": true,  
  "specificInformation": "Behavior style report. Ability management test during foot that co",  
  "structureCheckLocation": 935.8,  
  "subsetName": "Central our people stage. Money create avoid sea. Pa",  
  "switchProtectControlWarning": true,  
  "switchRadioSystem": true,  
  "systemSeparationInfo": "Only really for space ",  
  "tNvcontact": 864,  
  "tNvovtrp": 864,  
  "tenGISId": "American whole magazine truth stop ",  
  "tiltingSupported": true,  
  "trainIntegrityOnBoardRequired": true,  
  "tsiSwitchCrossing": false,  
  "usesGroup555": false,  
  "vNvallowovtrp": 864,  
  "vNvsupovtrp": 864,  
  "vehicleTypesCompatibleTrafficLoad": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "vehiclesCompatibleTrafficLoad": "Together range line beyond. First policy daughter need kind miss.",  
  "verificationCCS": "Trouble behavior style report s",  
  "verificationENE": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "TSIMagneticFields": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSIMagneticFields:KSHJ:98947196",  
  "TSITractionHarmonics": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSITractionHarmonics:CVYE:23209471",  
  "atoCommunicationSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoCommunicationSystem:ZHGV:20186848",  
  "atoGradeAutomation": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoGradeAutomation:KTDP:96947751",  
  "atoSystemVersion": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoSystemVersion:LZFK:95330413",  
  "cantDeficiencyBasicSSP": "urn:ngsi-ld:SubsetWithCommonCharacteristics:cantDeficiencyBasicSSP:TVCA:60123098",  
  "conditionsUseReflectivePlates": "urn:ngsi-ld:SubsetWithCommonCharacteristics:conditionsUseReflectivePlates:DBTA:13991615",  
  "contactLineSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactLineSystem:NTDI:32173008",  
  "contactStripMaterial": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactStripMaterial:QOBT:13145620",  
  "dataRadioCompatible": "urn:ngsi-ld:SubsetWithCommonCharacteristics:dataRadioCompatible:WVGY:16345792",  
  "eddyCurrentBraking": "urn:ngsi-ld:SubsetWithCommonCharacteristics:eddyCurrentBraking:OVFA:02258419",  
  "etcsDegradedSituation": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsDegradedSituation:ERWA:76984564",  
  "etcsInfill": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsInfill:YPLT:71508423",  
  "etcsLevel": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsLevel:UCAT:45992466",  
  "etcsMVersion": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsMVersion:NBMW:35233769",  
  "etcsTransmittedTrackConditions": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsTransmittedTrackConditions:OQPR:96027142",  
  "freightCorridor": "urn:ngsi-ld:SubsetWithCommonCharacteristics:freightCorridor:ZZNG:90075470",  
  "gaugingProfile": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gaugingProfile:GAWY:81206650",  
  "gsmRActiveMobiles": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRActiveMobiles:JIWF:08913193",  
  "gsmROptionalFunctions": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmROptionalFunctions:IEUQ:17610471",  
  "gsmRVersion": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRVersion:VIRK:51240003",  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrConstraintsOperateOnlyInCircuitSwitch:RFGM:59097765",  
  "gsmrNetworkCoverage": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrNetworkCoverage:ZLWC:94022455",  
  "hotAxleBoxDetectorDirection": "urn:ngsi-ld:SubsetWithCommonCharacteristics:hotAxleBoxDetectorDirection:JLMR:59004229",  
  "legacyRadioSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:legacyRadioSystem:QXCJ:24173042",  
  "lineCategory": "urn:ngsi-ld:SubsetWithCommonCharacteristics:lineCategory:PKZZ:65461187",  
  "linesideDistanceIndicationAppearance": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationAppearance:KXVE:51717604",  
  "linesideDistanceIndicationPositioning": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationPositioning:BMAD:29611133",  
  "loadCapability": "urn:ngsi-ld:SubsetWithCommonCharacteristics:loadCapability:NCLH:68847793",  
  "mNvcontact": "urn:ngsi-ld:SubsetWithCommonCharacteristics:mNvcontact:WAQO:49263511",  
  "magneticBraking": "urn:ngsi-ld:SubsetWithCommonCharacteristics:magneticBraking:TEDG:31764303",  
  "osmClass": "urn:ngsi-ld:SubsetWithCommonCharacteristics:osmClass:ESMU:76582197",  
  "otherCantDeficiencyBasicSSP": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherCantDeficiencyBasicSSP:THAK:68757738",  
  "otherPantographHead": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherPantographHead:MSJW:55082492",  
  "otherTrainProtection": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherTrainProtection:BJAY:71180132",  
  "passesThroughTunnel": "urn:ngsi-ld:SubsetWithCommonCharacteristics:passesThroughTunnel:QQBS:75227586",  
  "platform": "urn:ngsi-ld:SubsetWithCommonCharacteristics:platform:TNPZ:18916348",  
  "profileNumberSemiTrailers": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSemiTrailers:QSIK:69930024",  
  "profileNumberSwapBodies": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSwapBodies:FUEH:17446660",  
  "protectionLegacySystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:protectionLegacySystem:TWCV:45007627",  
  "qNvdriverAdhes": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvdriverAdhes:BDPY:25609767",  
  "qNvemrrls": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvemrrls:WRUL:20099251",  
  "railInclination": "urn:ngsi-ld:SubsetWithCommonCharacteristics:railInclination:UKUD:36710979",  
  "reasonsEtcsRadioBlockCenterReject": "urn:ngsi-ld:SubsetWithCommonCharacteristics:reasonsEtcsRadioBlockCenterReject:BZMO:94264183",  
  "safeConsistLengthInformationNecessary": "urn:ngsi-ld:SubsetWithCommonCharacteristics:safeConsistLengthInformationNecessary:IAQV:53751007",  
  "standardCombinedTransporRollerUnits": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransporRollerUnits:QJDE:99331886",  
  "standardCombinedTransportContainers": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransportContainers:NYEX:69611611",  
  "temperatureRange": "urn:ngsi-ld:SubsetWithCommonCharacteristics:temperatureRange:CLCD:07660754",  
  "trackLoadCapability": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackLoadCapability:CTEG:50552035",  
  "trackPhaseInfo": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackPhaseInfo:HEFO:03104509",  
  "trackRaisedPantographsDistanceAndSpeed": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackRaisedPantographsDistanceAndSpeed:KPJJ:17542035",  
  "trackSystemSeparationInfo": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackSystemSeparationInfo:JFME:85291189",  
  "trainDetectionSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trainDetectionSystem:LNVB:23583324",  
  "tsiPantographHead": "urn:ngsi-ld:SubsetWithCommonCharacteristics:tsiPantographHead:JRNX:29061126"  
}  
```  
</details>  
#### SubsetWithCommonCharacteristics NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 SubsetWithCommonCharacteristics 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SubsetWithCommonCharacteristics:id:YPHZ:97109776",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2022-10-05T07:31:49Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2011-08-27T16:37:28Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Toward should once hear test. Most least fish record break prevent."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Later dis"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Statement make according agree may might partner someone. Fund accept compare firm a late."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Else difficult security young. Ok turn number. Reflect s"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Modern boy coach sea clearly."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:DWBT:01785577",  
      "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:CIWU:39426109"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:WISG:95955862"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          19.420622,  
          125.057551  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Until mind clear out series event each. Concern hand organization drug. Animal cup within energy. Save decisio"  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Turn medical majority white ready source. Middle dinner participant large TV. Increase summer yourself since though."  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Out now day. C"  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Relate PM look party possible. Science Mrs information newspaper. Local husband share Republican development book food Mr."  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Morning car large their page. Home agen"  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Bar draw leg weste"  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Idea "  
      },  
      "district": {  
        "type": "Text",  
        "value": "Establish bring just. Follow line run old. Win mean market coach enter begin physica"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Career institution start"  
  },  
  "type": "SubsetWithCommonCharacteristics",  
  "IdPhoneErtmsRadioBlockCenter": {  
    "type": "Text",  
    "value": "Building none down investment possible member country."  
  },  
  "accelerationLevelCrossing": {  
    "type": "Text",  
    "value": "World middle talk into understand paper."  
  },  
  "additionalBrakingInformationDocument": {  
    "type": "Text",  
    "value": "Understand house degree though. System she science election."  
  },  
  "atoErrorCorrectionsOnboard": {  
    "type": "Text",  
    "value": "Cover close yes simple entire."  
  },  
  "automaticDroppingDeviceRequired": {  
    "type": "Boolean",  
    "value": true  
  },  
  "bigMetalMass": {  
    "type": "Boolean",  
    "value": true  
  },  
  "cantDeficiency": {  
    "type": "Number",  
    "value": 864  
  },  
  "compatibilityProcedureDocument": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sens"  
  },  
  "conditionsSwitchClassBSystems": {  
    "type": "Text",  
    "value": "Together range line beyon"  
  },  
  "conditionsSwitchTrainProtectionSystems": {  
    "type": "Text",  
    "value": "Trouble behavior style report size perso"  
  },  
  "contactStripMaterialMetallicContent": {  
    "type": "Number",  
    "value": 864  
  },  
  "dNvovtrp": {  
    "type": "Number",  
    "value": 864  
  },  
  "dNvpotrp": {  
    "type": "Number",  
    "value": 864  
  },  
  "dNvroll": {  
    "type": "Number",  
    "value": 864  
  },  
  "demonstrationENE": {  
    "type": "Text",  
    "value": "American whole magazine truth stop who"  
  },  
  "distSignToPhaseEnd": {  
    "type": "Number",  
    "value": 864  
  },  
  "documentRestrictionPositionContactLineSeparation": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "documentRestrictionPowerConsumption": {  
    "type": "Text",  
    "value": "Togethe"  
  },  
  "eddyCurrentBrakingConditionsDocument": {  
    "type": "Text",  
    "value": "Trouble behavior style report size personal partner. During foot that course nothing draw."  
  },  
  "etcsErrorCorrectionsOnboard": {  
    "type": "Text",  
    "value": "Language ball floor meet usually "  
  },  
  "etcsImplementsLevelCrossingProcedure": {  
    "type": "Boolean",  
    "value": false  
  },  
  "etcsInfillLineAccess": {  
    "type": "Boolean",  
    "value": false  
  },  
  "etcsNationalPacket44": {  
    "type": "Boolean",  
    "value": true  
  },  
  "etcsOptionalFunctions": {  
    "type": "Text",  
    "value": "First drug contain start almost wonder. Live bed serious theory type. Together type music hospital. Every speech support time operation wear often"  
  },  
  "etcsSystemFunctionalitiesNextFiveYears": {  
    "type": "Text",  
    "value": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and."  
  },  
  "etcsTransmitsTrackConditions": {  
    "type": "Boolean",  
    "value": true  
  },  
  "flangeLubeForbidden": {  
    "type": "Boolean",  
    "value": true  
  },  
  "gaugingCheckLocation": {  
    "type": "Text",  
    "value": "Paper office hospital have wonder. Painting create wife."  
  },  
  "gaugingTransversalDocument": {  
    "type": "Text",  
    "value": "Decision song view age international big employee. Author"  
  },  
  "gprsForETCS": {  
    "type": "Boolean",  
    "value": true  
  },  
  "gprsImplementationArea": {  
    "type": "Text",  
    "value": "Employee toward like total now. Whom around put suddenly garden. Bring TV prog"  
  },  
  "gradientProfile": {  
    "type": "Text",  
    "value": "True power home price check real leader. From animal exactly drive. Good explain grow water plant perform resource."  
  },  
  "gsmRAdditionalInfo": {  
    "type": "Text",  
    "value": "Stock ball organization re"  
  },  
  "gsmRNoCoverage": {  
    "type": "Boolean",  
    "value": false  
  },  
  "gsmrErrorCorrectionsOnboard": {  
    "type": "Text",  
    "value": "Traditional page a although for study anyone. Could yourself plan base rise would. We"  
  },  
  "gsmrForcedDeregistrationFunctionalNumber": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasAdditionalBrakingInformation": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasBallast": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasETCSRestrictionsConditions": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasHotAxleBoxDetector": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasLevelCrossings": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasOtherTrainProtection": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasSevereWeatherConditions": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hasSystemSeparation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "hasTSITrainDetection": {  
    "type": "Boolean",  
    "value": false  
  },  
  "highSpeedLoadModelCompliance": {  
    "type": "Boolean",  
    "value": true  
  },  
  "hotAxleBoxDetectorGeneration": {  
    "type": "Text",  
    "value": "Trial son break either president."  
  },  
  "hotAxleBoxDetectorIdentification": {  
    "type": "Text",  
    "value": "The everything affect American. Next water voice travel among. Pretty Republican total policy head Mrs debate onto."  
  },  
  "hotAxleBoxDetectorLocation": {  
    "type": "Number",  
    "value": 860.4  
  },  
  "hotAxleBoxDetectorTSICompliant": {  
    "type": "Boolean",  
    "value": true  
  },  
  "instructionsSwitchRadioSystems": {  
    "type": "Text",  
    "value": "Force pass top better"  
  },  
  "isQuietRoute": {  
    "type": "Boolean",  
    "value": true  
  },  
  "linesideDistanceIndicationFrequency": {  
    "type": "Number",  
    "value": 864  
  },  
  "mNvderun": {  
    "type": "Boolean",  
    "value": false  
  },  
  "magneticBrakingConditionsDocument": {  
    "type": "Text",  
    "value": "Else memory if. Whose gro"  
  },  
  "maximumAltitude": {  
    "type": "Number",  
    "value": 704.6  
  },  
  "maximumBrakingDistance": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumContactWireHeight": {  
    "type": "Number",  
    "value": 957.2  
  },  
  "maximumPermittedSpeed": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumTemperature": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumTrainDeceleration": {  
    "type": "Number",  
    "value": 786.9  
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
    "value": 950.4  
  },  
  "minFlangeThickness": {  
    "type": "Number",  
    "value": 531.9  
  },  
  "minRimWidth": {  
    "type": "Number",  
    "value": 663.5  
  },  
  "minWheelDiameter": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumContactWireHeight": {  
    "type": "Number",  
    "value": 911.5  
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
  "multipleTrainProtectionRequired": {  
    "type": "Boolean",  
    "value": false  
  },  
  "nationalLoadCapability": {  
    "type": "Text",  
    "value": "Else memor"  
  },  
  "nationalValuesBrakeModel": {  
    "type": "Text",  
    "value": "Financial role together range. Nice government first po"  
  },  
  "permitUseReflectivePlates": {  
    "type": "Boolean",  
    "value": true  
  },  
  "permittedContactForce": {  
    "type": "Text",  
    "value": "Language ball floor meet usually board necessary. Natural sport music white."  
  },  
  "phaseInfo": {  
    "type": "Text",  
    "value": "On"  
  },  
  "phaseSeparation": {  
    "type": "Boolean",  
    "value": false  
  },  
  "publicNetworkRoaming": {  
    "type": "Boolean",  
    "value": false  
  },  
  "publicNetworkRoamingDetails": {  
    "type": "Text",  
    "value": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and."  
  },  
  "qNvsbtsmperm": {  
    "type": "Boolean",  
    "value": true  
  },  
  "radioNetworkId": {  
    "type": "Number",  
    "value": 864  
  },  
  "railSystemType": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "raisedPantographsDistanceAndSpeed": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "redLightsRequired": {  
    "type": "Boolean",  
    "value": true  
  },  
  "specificInformation": {  
    "type": "Text",  
    "value": "Behavior style report. Ability management test during foot that co"  
  },  
  "structureCheckLocation": {  
    "type": "Number",  
    "value": 935.8  
  },  
  "subsetName": {  
    "type": "Text",  
    "value": "Central our people stage. Money create avoid sea. Pa"  
  },  
  "switchProtectControlWarning": {  
    "type": "Boolean",  
    "value": true  
  },  
  "switchRadioSystem": {  
    "type": "Boolean",  
    "value": true  
  },  
  "systemSeparationInfo": {  
    "type": "Text",  
    "value": "Only really for space "  
  },  
  "tNvcontact": {  
    "type": "Number",  
    "value": 864  
  },  
  "tNvovtrp": {  
    "type": "Number",  
    "value": 864  
  },  
  "tenGISId": {  
    "type": "Text",  
    "value": "American whole magazine truth stop "  
  },  
  "tiltingSupported": {  
    "type": "Boolean",  
    "value": true  
  },  
  "trainIntegrityOnBoardRequired": {  
    "type": "Boolean",  
    "value": true  
  },  
  "tsiSwitchCrossing": {  
    "type": "Boolean",  
    "value": false  
  },  
  "usesGroup555": {  
    "type": "Boolean",  
    "value": false  
  },  
  "vNvallowovtrp": {  
    "type": "Number",  
    "value": 864  
  },  
  "vNvsupovtrp": {  
    "type": "Number",  
    "value": 864  
  },  
  "vehicleTypesCompatibleTrafficLoad": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "vehiclesCompatibleTrafficLoad": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "verificationCCS": {  
    "type": "Text",  
    "value": "Trouble behavior style report s"  
  },  
  "verificationENE": {  
    "type": "Text",  
    "value": "Language ball floor meet usually board necessary. Natural sport music white."  
  },  
  "TSIMagneticFields": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSIMagneticFields:KSHJ:98947196"  
  },  
  "TSITractionHarmonics": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSITractionHarmonics:CVYE:23209471"  
  },  
  "atoCommunicationSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoCommunicationSystem:ZHGV:20186848"  
  },  
  "atoGradeAutomation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoGradeAutomation:KTDP:96947751"  
  },  
  "atoSystemVersion": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoSystemVersion:LZFK:95330413"  
  },  
  "cantDeficiencyBasicSSP": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:cantDeficiencyBasicSSP:TVCA:60123098"  
  },  
  "conditionsUseReflectivePlates": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:conditionsUseReflectivePlates:DBTA:13991615"  
  },  
  "contactLineSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactLineSystem:NTDI:32173008"  
  },  
  "contactStripMaterial": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactStripMaterial:QOBT:13145620"  
  },  
  "dataRadioCompatible": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:dataRadioCompatible:WVGY:16345792"  
  },  
  "eddyCurrentBraking": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:eddyCurrentBraking:OVFA:02258419"  
  },  
  "etcsDegradedSituation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsDegradedSituation:ERWA:76984564"  
  },  
  "etcsInfill": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsInfill:YPLT:71508423"  
  },  
  "etcsLevel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsLevel:UCAT:45992466"  
  },  
  "etcsMVersion": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsMVersion:NBMW:35233769"  
  },  
  "etcsTransmittedTrackConditions": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsTransmittedTrackConditions:OQPR:96027142"  
  },  
  "freightCorridor": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:freightCorridor:ZZNG:90075470"  
  },  
  "gaugingProfile": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gaugingProfile:GAWY:81206650"  
  },  
  "gsmRActiveMobiles": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRActiveMobiles:JIWF:08913193"  
  },  
  "gsmROptionalFunctions": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmROptionalFunctions:IEUQ:17610471"  
  },  
  "gsmRVersion": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRVersion:VIRK:51240003"  
  },  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrConstraintsOperateOnlyInCircuitSwitch:RFGM:59097765"  
  },  
  "gsmrNetworkCoverage": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrNetworkCoverage:ZLWC:94022455"  
  },  
  "hotAxleBoxDetectorDirection": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:hotAxleBoxDetectorDirection:JLMR:59004229"  
  },  
  "legacyRadioSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:legacyRadioSystem:QXCJ:24173042"  
  },  
  "lineCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:lineCategory:PKZZ:65461187"  
  },  
  "linesideDistanceIndicationAppearance": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationAppearance:KXVE:51717604"  
  },  
  "linesideDistanceIndicationPositioning": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationPositioning:BMAD:29611133"  
  },  
  "loadCapability": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:loadCapability:NCLH:68847793"  
  },  
  "mNvcontact": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:mNvcontact:WAQO:49263511"  
  },  
  "magneticBraking": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:magneticBraking:TEDG:31764303"  
  },  
  "osmClass": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:osmClass:ESMU:76582197"  
  },  
  "otherCantDeficiencyBasicSSP": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherCantDeficiencyBasicSSP:THAK:68757738"  
  },  
  "otherPantographHead": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherPantographHead:MSJW:55082492"  
  },  
  "otherTrainProtection": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherTrainProtection:BJAY:71180132"  
  },  
  "passesThroughTunnel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:passesThroughTunnel:QQBS:75227586"  
  },  
  "platform": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:platform:TNPZ:18916348"  
  },  
  "profileNumberSemiTrailers": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSemiTrailers:QSIK:69930024"  
  },  
  "profileNumberSwapBodies": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSwapBodies:FUEH:17446660"  
  },  
  "protectionLegacySystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:protectionLegacySystem:TWCV:45007627"  
  },  
  "qNvdriverAdhes": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvdriverAdhes:BDPY:25609767"  
  },  
  "qNvemrrls": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvemrrls:WRUL:20099251"  
  },  
  "railInclination": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:railInclination:UKUD:36710979"  
  },  
  "reasonsEtcsRadioBlockCenterReject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:reasonsEtcsRadioBlockCenterReject:BZMO:94264183"  
  },  
  "safeConsistLengthInformationNecessary": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:safeConsistLengthInformationNecessary:IAQV:53751007"  
  },  
  "standardCombinedTransporRollerUnits": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransporRollerUnits:QJDE:99331886"  
  },  
  "standardCombinedTransportContainers": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransportContainers:NYEX:69611611"  
  },  
  "temperatureRange": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:temperatureRange:CLCD:07660754"  
  },  
  "trackLoadCapability": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackLoadCapability:CTEG:50552035"  
  },  
  "trackPhaseInfo": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackPhaseInfo:HEFO:03104509"  
  },  
  "trackRaisedPantographsDistanceAndSpeed": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackRaisedPantographsDistanceAndSpeed:KPJJ:17542035"  
  },  
  "trackSystemSeparationInfo": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackSystemSeparationInfo:JFME:85291189"  
  },  
  "trainDetectionSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trainDetectionSystem:LNVB:23583324"  
  },  
  "tsiPantographHead": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubsetWithCommonCharacteristics:tsiPantographHead:JRNX:29061126"  
  }  
}  
```  
</details>  
#### SubsetWithCommonCharacteristics NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 SubsetWithCommonCharacteristics 的示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SubsetWithCommonCharacteristics:id:YPHZ:97109776",  
  "dateCreated": "2022-10-05T07:31:49Z",  
  "dateModified": "2011-08-27T16:37:28Z",  
  "source": "Toward should once hear test. Most least fish record break prevent.",  
  "name": "Later dis",  
  "alternateName": "Statement make according agree may might partner someone. Fund accept compare firm a late.",  
  "description": "Else difficult security young. Ok turn number. Reflect s",  
  "dataProvider": "Modern boy coach sea clearly.",  
  "owner": [  
    "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:DWBT:01785577",  
    "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:CIWU:39426109"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:WISG:95955862"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      19.420622,  
      125.057551  
    ]  
  },  
  "address": {  
    "streetAddress": "Until mind clear out series event each. Concern hand organization drug. Animal cup within energy. Save decisio",  
    "addressLocality": "Turn medical majority white ready source. Middle dinner participant large TV. Increase summer yourself since though.",  
    "addressRegion": "Out now day. C",  
    "addressCountry": "Relate PM look party possible. Science Mrs information newspaper. Local husband share Republican development book food Mr.",  
    "postalCode": "Morning car large their page. Home agen",  
    "postOfficeBoxNumber": "Bar draw leg weste",  
    "streetNr": "Idea ",  
    "district": "Establish bring just. Follow line run old. Win mean market coach enter begin physica"  
  },  
  "areaServed": "Career institution start",  
  "type": "SubsetWithCommonCharacteristics",  
  "IdPhoneErtmsRadioBlockCenter": "Building none down investment possible member country.",  
  "accelerationLevelCrossing": "World middle talk into understand paper.",  
  "additionalBrakingInformationDocument": "Understand house degree though. System she science election.",  
  "atoErrorCorrectionsOnboard": "Cover close yes simple entire.",  
  "automaticDroppingDeviceRequired": true,  
  "bigMetalMass": true,  
  "cantDeficiency": 864,  
  "compatibilityProcedureDocument": "American whole magazine truth stop whose. On traditional measure example sens",  
  "conditionsSwitchClassBSystems": "Together range line beyon",  
  "conditionsSwitchTrainProtectionSystems": "Trouble behavior style report size perso",  
  "contactStripMaterialMetallicContent": 864,  
  "dNvovtrp": 864,  
  "dNvpotrp": 864,  
  "dNvroll": 864,  
  "demonstrationENE": "American whole magazine truth stop who",  
  "distSignToPhaseEnd": 864,  
  "documentRestrictionPositionContactLineSeparation": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "documentRestrictionPowerConsumption": "Togethe",  
  "eddyCurrentBrakingConditionsDocument": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "etcsErrorCorrectionsOnboard": "Language ball floor meet usually ",  
  "etcsImplementsLevelCrossingProcedure": false,  
  "etcsInfillLineAccess": false,  
  "etcsNationalPacket44": true,  
  "etcsOptionalFunctions": "First drug contain start almost wonder. Live bed serious theory type. Together type music hospital. Every speech support time operation wear often",  
  "etcsSystemFunctionalitiesNextFiveYears": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and.",  
  "etcsTransmitsTrackConditions": true,  
  "flangeLubeForbidden": true,  
  "gaugingCheckLocation": "Paper office hospital have wonder. Painting create wife.",  
  "gaugingTransversalDocument": "Decision song view age international big employee. Author",  
  "gprsForETCS": true,  
  "gprsImplementationArea": "Employee toward like total now. Whom around put suddenly garden. Bring TV prog",  
  "gradientProfile": "True power home price check real leader. From animal exactly drive. Good explain grow water plant perform resource.",  
  "gsmRAdditionalInfo": "Stock ball organization re",  
  "gsmRNoCoverage": false,  
  "gsmrErrorCorrectionsOnboard": "Traditional page a although for study anyone. Could yourself plan base rise would. We",  
  "gsmrForcedDeregistrationFunctionalNumber": true,  
  "hasAdditionalBrakingInformation": true,  
  "hasBallast": true,  
  "hasETCSRestrictionsConditions": true,  
  "hasHotAxleBoxDetector": false,  
  "hasLevelCrossings": false,  
  "hasOtherTrainProtection": true,  
  "hasSevereWeatherConditions": true,  
  "hasSystemSeparation": false,  
  "hasTSITrainDetection": false,  
  "highSpeedLoadModelCompliance": true,  
  "hotAxleBoxDetectorGeneration": "Trial son break either president.",  
  "hotAxleBoxDetectorIdentification": "The everything affect American. Next water voice travel among. Pretty Republican total policy head Mrs debate onto.",  
  "hotAxleBoxDetectorLocation": 860.4,  
  "hotAxleBoxDetectorTSICompliant": true,  
  "instructionsSwitchRadioSystems": "Force pass top better",  
  "isQuietRoute": true,  
  "linesideDistanceIndicationFrequency": 864,  
  "mNvderun": false,  
  "magneticBrakingConditionsDocument": "Else memory if. Whose gro",  
  "maximumAltitude": 704.6,  
  "maximumBrakingDistance": 864,  
  "maximumContactWireHeight": 957.2,  
  "maximumPermittedSpeed": 864,  
  "maximumTemperature": 864,  
  "maximumTrainDeceleration": 786.9,  
  "minDistConsecutiveAxles": 864,  
  "minDistFirstLastAxle": 864,  
  "minFlangeHeight": 950.4,  
  "minFlangeThickness": 531.9,  
  "minRimWidth": 663.5,  
  "minWheelDiameter": 864,  
  "minimumContactWireHeight": 911.5,  
  "minimumHorizontalRadius": 864,  
  "minimumTemperature": 864,  
  "minimumWheelDiameter": 864,  
  "multipleTrainProtectionRequired": false,  
  "nationalLoadCapability": "Else memor",  
  "nationalValuesBrakeModel": "Financial role together range. Nice government first po",  
  "permitUseReflectivePlates": true,  
  "permittedContactForce": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "phaseInfo": "On",  
  "phaseSeparation": false,  
  "publicNetworkRoaming": false,  
  "publicNetworkRoamingDetails": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and.",  
  "qNvsbtsmperm": true,  
  "radioNetworkId": 864,  
  "railSystemType": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "raisedPantographsDistanceAndSpeed": "Together range line beyond. First policy daughter need kind miss.",  
  "redLightsRequired": true,  
  "specificInformation": "Behavior style report. Ability management test during foot that co",  
  "structureCheckLocation": 935.8,  
  "subsetName": "Central our people stage. Money create avoid sea. Pa",  
  "switchProtectControlWarning": true,  
  "switchRadioSystem": true,  
  "systemSeparationInfo": "Only really for space ",  
  "tNvcontact": 864,  
  "tNvovtrp": 864,  
  "tenGISId": "American whole magazine truth stop ",  
  "tiltingSupported": true,  
  "trainIntegrityOnBoardRequired": true,  
  "tsiSwitchCrossing": false,  
  "usesGroup555": false,  
  "vNvallowovtrp": 864,  
  "vNvsupovtrp": 864,  
  "vehicleTypesCompatibleTrafficLoad": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "vehiclesCompatibleTrafficLoad": "Together range line beyond. First policy daughter need kind miss.",  
  "verificationCCS": "Trouble behavior style report s",  
  "verificationENE": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "TSIMagneticFields": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSIMagneticFields:KSHJ:98947196",  
  "TSITractionHarmonics": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSITractionHarmonics:CVYE:23209471",  
  "atoCommunicationSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoCommunicationSystem:ZHGV:20186848",  
  "atoGradeAutomation": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoGradeAutomation:KTDP:96947751",  
  "atoSystemVersion": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoSystemVersion:LZFK:95330413",  
  "cantDeficiencyBasicSSP": "urn:ngsi-ld:SubsetWithCommonCharacteristics:cantDeficiencyBasicSSP:TVCA:60123098",  
  "conditionsUseReflectivePlates": "urn:ngsi-ld:SubsetWithCommonCharacteristics:conditionsUseReflectivePlates:DBTA:13991615",  
  "contactLineSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactLineSystem:NTDI:32173008",  
  "contactStripMaterial": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactStripMaterial:QOBT:13145620",  
  "dataRadioCompatible": "urn:ngsi-ld:SubsetWithCommonCharacteristics:dataRadioCompatible:WVGY:16345792",  
  "eddyCurrentBraking": "urn:ngsi-ld:SubsetWithCommonCharacteristics:eddyCurrentBraking:OVFA:02258419",  
  "etcsDegradedSituation": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsDegradedSituation:ERWA:76984564",  
  "etcsInfill": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsInfill:YPLT:71508423",  
  "etcsLevel": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsLevel:UCAT:45992466",  
  "etcsMVersion": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsMVersion:NBMW:35233769",  
  "etcsTransmittedTrackConditions": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsTransmittedTrackConditions:OQPR:96027142",  
  "freightCorridor": "urn:ngsi-ld:SubsetWithCommonCharacteristics:freightCorridor:ZZNG:90075470",  
  "gaugingProfile": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gaugingProfile:GAWY:81206650",  
  "gsmRActiveMobiles": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRActiveMobiles:JIWF:08913193",  
  "gsmROptionalFunctions": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmROptionalFunctions:IEUQ:17610471",  
  "gsmRVersion": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRVersion:VIRK:51240003",  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrConstraintsOperateOnlyInCircuitSwitch:RFGM:59097765",  
  "gsmrNetworkCoverage": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrNetworkCoverage:ZLWC:94022455",  
  "hotAxleBoxDetectorDirection": "urn:ngsi-ld:SubsetWithCommonCharacteristics:hotAxleBoxDetectorDirection:JLMR:59004229",  
  "legacyRadioSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:legacyRadioSystem:QXCJ:24173042",  
  "lineCategory": "urn:ngsi-ld:SubsetWithCommonCharacteristics:lineCategory:PKZZ:65461187",  
  "linesideDistanceIndicationAppearance": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationAppearance:KXVE:51717604",  
  "linesideDistanceIndicationPositioning": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationPositioning:BMAD:29611133",  
  "loadCapability": "urn:ngsi-ld:SubsetWithCommonCharacteristics:loadCapability:NCLH:68847793",  
  "mNvcontact": "urn:ngsi-ld:SubsetWithCommonCharacteristics:mNvcontact:WAQO:49263511",  
  "magneticBraking": "urn:ngsi-ld:SubsetWithCommonCharacteristics:magneticBraking:TEDG:31764303",  
  "osmClass": "urn:ngsi-ld:SubsetWithCommonCharacteristics:osmClass:ESMU:76582197",  
  "otherCantDeficiencyBasicSSP": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherCantDeficiencyBasicSSP:THAK:68757738",  
  "otherPantographHead": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherPantographHead:MSJW:55082492",  
  "otherTrainProtection": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherTrainProtection:BJAY:71180132",  
  "passesThroughTunnel": "urn:ngsi-ld:SubsetWithCommonCharacteristics:passesThroughTunnel:QQBS:75227586",  
  "platform": "urn:ngsi-ld:SubsetWithCommonCharacteristics:platform:TNPZ:18916348",  
  "profileNumberSemiTrailers": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSemiTrailers:QSIK:69930024",  
  "profileNumberSwapBodies": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSwapBodies:FUEH:17446660",  
  "protectionLegacySystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:protectionLegacySystem:TWCV:45007627",  
  "qNvdriverAdhes": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvdriverAdhes:BDPY:25609767",  
  "qNvemrrls": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvemrrls:WRUL:20099251",  
  "railInclination": "urn:ngsi-ld:SubsetWithCommonCharacteristics:railInclination:UKUD:36710979",  
  "reasonsEtcsRadioBlockCenterReject": "urn:ngsi-ld:SubsetWithCommonCharacteristics:reasonsEtcsRadioBlockCenterReject:BZMO:94264183",  
  "safeConsistLengthInformationNecessary": "urn:ngsi-ld:SubsetWithCommonCharacteristics:safeConsistLengthInformationNecessary:IAQV:53751007",  
  "standardCombinedTransporRollerUnits": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransporRollerUnits:QJDE:99331886",  
  "standardCombinedTransportContainers": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransportContainers:NYEX:69611611",  
  "temperatureRange": "urn:ngsi-ld:SubsetWithCommonCharacteristics:temperatureRange:CLCD:07660754",  
  "trackLoadCapability": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackLoadCapability:CTEG:50552035",  
  "trackPhaseInfo": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackPhaseInfo:HEFO:03104509",  
  "trackRaisedPantographsDistanceAndSpeed": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackRaisedPantographsDistanceAndSpeed:KPJJ:17542035",  
  "trackSystemSeparationInfo": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackSystemSeparationInfo:JFME:85291189",  
  "trainDetectionSystem": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trainDetectionSystem:LNVB:23583324",  
  "tsiPantographHead": "urn:ngsi-ld:SubsetWithCommonCharacteristics:tsiPantographHead:JRNX:29061126",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SubsetWithCommonCharacteristics NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 SubsetWithCommonCharacteristics 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SubsetWithCommonCharacteristics:id:EEHL:48448508",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1997-12-18T11:08:38Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2013-09-08T14:45:24Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "They stage must recent already. Personal where wait yard nature position."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Everything address truth nation community miss li"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Fear institution hit paper only. We evening boy measure score choose often inside."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Station site already mention sign low. According station strategy skill news."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Because do arrive partner soon century prepare. Light likely music back discover."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:JMDD:03595678",  
      "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:UUSE:49704479"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SubsetWithCommonCharacteristics:items:KDTR:83494975"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -45.727198,  
        65.334527  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Receive country stage key more s",  
      "addressLocality": "Sort best treat including gas. Clear term many training present profe",  
      "addressRegion": "Game leave good strong my or. Simple return two daughter. C",  
      "addressCountry": "Eye north hundred guess trip posit",  
      "postalCode": "Her public ok effect as simply training figure. Live safe group goal name kid. Discussion recently so Democrat field successful hundred beyond.",  
      "postOfficeBoxNumber": "Section on full option. Story attention attack factor necessary cut available. Write town candidate end nearly garden.",  
      "streetNr": "Care surface chance simply hair senior. Within like hundred.",  
      "district": "Where go take create enter trip. In data she attention defense."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "He well management onto executive. Note student medical mother building total."  
  },  
  "type": "SubsetWithCommonCharacteristics",  
  "IdPhoneErtmsRadioBlockCenter": {  
    "type": "Property",  
    "value": "Seem discussion realize almost detail cul"  
  },  
  "accelerationLevelCrossing": {  
    "type": "Property",  
    "value": "Site gun if side population guess. Recent event green letter only learn safe. New ahead ask speak rule. Box this by catch leg hers"  
  },  
  "additionalBrakingInformationDocument": {  
    "type": "Property",  
    "value": "Certain certainly treat population rich. Which those term"  
  },  
  "atoErrorCorrectionsOnboard": {  
    "type": "Property",  
    "value": "Write language operation hundred show message specific "  
  },  
  "automaticDroppingDeviceRequired": {  
    "type": "Property",  
    "value": true  
  },  
  "bigMetalMass": {  
    "type": "Property",  
    "value": true  
  },  
  "cantDeficiency": {  
    "type": "Property",  
    "value": 415  
  },  
  "compatibilityProcedureDocument": {  
    "type": "Property",  
    "value": "Doctor my save design tell special. Final many author possible."  
  },  
  "conditionsSwitchClassBSystems": {  
    "type": "Property",  
    "value": "Suffer eye water movie. End green student fine."  
  },  
  "conditionsSwitchTrainProtectionSystems": {  
    "type": "Property",  
    "value": "Establish gre"  
  },  
  "contactStripMaterialMetallicContent": {  
    "type": "Property",  
    "value": 701  
  },  
  "dNvovtrp": {  
    "type": "Property",  
    "value": 369  
  },  
  "dNvpotrp": {  
    "type": "Property",  
    "value": 32  
  },  
  "dNvroll": {  
    "type": "Property",  
    "value": 642  
  },  
  "demonstrationENE": {  
    "type": "Property",  
    "value": "Catch my apply stay some."  
  },  
  "distSignToPhaseEnd": {  
    "type": "Property",  
    "value": 726  
  },  
  "documentRestrictionPositionContactLineSeparation": {  
    "type": "Property",  
    "value": "Candidate window fly decide from real meet. Heavy particular rock north foreign. Perhaps bad interview either."  
  },  
  "documentRestrictionPowerConsumption": {  
    "type": "Property",  
    "value": "Still special staff rule. Soon want look else finish network."  
  },  
  "eddyCurrentBrakingConditionsDocument": {  
    "type": "Property",  
    "value": "A bed father three spring trade listen. Kind matter think up glass."  
  },  
  "etcsErrorCorrectionsOnboard": {  
    "type": "Property",  
    "value": "Nice view field prove."  
  },  
  "etcsImplementsLevelCrossingProcedure": {  
    "type": "Property",  
    "value": false  
  },  
  "etcsInfillLineAccess": {  
    "type": "Property",  
    "value": false  
  },  
  "etcsNationalPacket44": {  
    "type": "Property",  
    "value": false  
  },  
  "etcsOptionalFunctions": {  
    "type": "Property",  
    "value": "Better process improve best. Amount behind withi"  
  },  
  "etcsSystemFunctionalitiesNextFiveYears": {  
    "type": "Property",  
    "value": "Maintain position him ground provide m"  
  },  
  "etcsTransmitsTrackConditions": {  
    "type": "Property",  
    "value": true  
  },  
  "flangeLubeForbidden": {  
    "type": "Property",  
    "value": false  
  },  
  "gaugingCheckLocation": {  
    "type": "Property",  
    "value": "Build woman manager. Information time late deep quality single while book."  
  },  
  "gaugingTransversalDocument": {  
    "type": "Property",  
    "value": "Year whether high community. Bed go top near."  
  },  
  "gprsForETCS": {  
    "type": "Property",  
    "value": true  
  },  
  "gprsImplementationArea": {  
    "type": "Property",  
    "value": "Also most the too age. Language ever others cell."  
  },  
  "gradientProfile": {  
    "type": "Property",  
    "value": "Third none also establish west material assume. Fund would item rock easy notice. Civil particular determine benefi"  
  },  
  "gsmRAdditionalInfo": {  
    "type": "Property",  
    "value": "Page serious top read strong. First very view realize marriage kitchen."  
  },  
  "gsmRNoCoverage": {  
    "type": "Property",  
    "value": false  
  },  
  "gsmrErrorCorrectionsOnboard": {  
    "type": "Property",  
    "value": "Very write site question. Left before wait voice road while tell magazine."  
  },  
  "gsmrForcedDeregistrationFunctionalNumber": {  
    "type": "Property",  
    "value": false  
  },  
  "hasAdditionalBrakingInformation": {  
    "type": "Property",  
    "value": true  
  },  
  "hasBallast": {  
    "type": "Property",  
    "value": true  
  },  
  "hasETCSRestrictionsConditions": {  
    "type": "Property",  
    "value": true  
  },  
  "hasHotAxleBoxDetector": {  
    "type": "Property",  
    "value": true  
  },  
  "hasLevelCrossings": {  
    "type": "Property",  
    "value": false  
  },  
  "hasOtherTrainProtection": {  
    "type": "Property",  
    "value": false  
  },  
  "hasSevereWeatherConditions": {  
    "type": "Property",  
    "value": false  
  },  
  "hasSystemSeparation": {  
    "type": "Property",  
    "value": false  
  },  
  "hasTSITrainDetection": {  
    "type": "Property",  
    "value": true  
  },  
  "highSpeedLoadModelCompliance": {  
    "type": "Property",  
    "value": false  
  },  
  "hotAxleBoxDetectorGeneration": {  
    "type": "Property",  
    "value": "Travel movie expect individual. Smile we remember own."  
  },  
  "hotAxleBoxDetectorIdentification": {  
    "type": "Property",  
    "value": "Catch method beat. Fly race about himself. Appear gu"  
  },  
  "hotAxleBoxDetectorLocation": {  
    "type": "Property",  
    "value": 535.0  
  },  
  "hotAxleBoxDetectorTSICompliant": {  
    "type": "Property",  
    "value": true  
  },  
  "instructionsSwitchRadioSystems": {  
    "type": "Property",  
    "value": "Scientist field final good. Blood this party career interesting suggest. View baby book husband painting."  
  },  
  "isQuietRoute": {  
    "type": "Property",  
    "value": true  
  },  
  "linesideDistanceIndicationFrequency": {  
    "type": "Property",  
    "value": 61  
  },  
  "mNvderun": {  
    "type": "Property",  
    "value": true  
  },  
  "magneticBrakingConditionsDocument": {  
    "type": "Property",  
    "value": "Will fear very like painting debate. Material us quite avoid."  
  },  
  "maximumAltitude": {  
    "type": "Property",  
    "value": 608.0  
  },  
  "maximumBrakingDistance": {  
    "type": "Property",  
    "value": 986  
  },  
  "maximumContactWireHeight": {  
    "type": "Property",  
    "value": 92.8  
  },  
  "maximumPermittedSpeed": {  
    "type": "Property",  
    "value": 834  
  },  
  "maximumTemperature": {  
    "type": "Property",  
    "value": 553  
  },  
  "maximumTrainDeceleration": {  
    "type": "Property",  
    "value": 631.8  
  },  
  "minDistConsecutiveAxles": {  
    "type": "Property",  
    "value": 141  
  },  
  "minDistFirstLastAxle": {  
    "type": "Property",  
    "value": 327  
  },  
  "minFlangeHeight": {  
    "type": "Property",  
    "value": 690.3  
  },  
  "minFlangeThickness": {  
    "type": "Property",  
    "value": 256.1  
  },  
  "minRimWidth": {  
    "type": "Property",  
    "value": 904.5  
  },  
  "minWheelDiameter": {  
    "type": "Property",  
    "value": 686  
  },  
  "minimumContactWireHeight": {  
    "type": "Property",  
    "value": 244.0  
  },  
  "minimumHorizontalRadius": {  
    "type": "Property",  
    "value": 847  
  },  
  "minimumTemperature": {  
    "type": "Property",  
    "value": 361  
  },  
  "minimumWheelDiameter": {  
    "type": "Property",  
    "value": 69  
  },  
  "multipleTrainProtectionRequired": {  
    "type": "Property",  
    "value": false  
  },  
  "nationalLoadCapability": {  
    "type": "Property",  
    "value": "Growth series ever leader clearly. Service fund body their charge."  
  },  
  "nationalValuesBrakeModel": {  
    "type": "Property",  
    "value": "Day wife go. Too north team among."  
  },  
  "permitUseReflectivePlates": {  
    "type": "Property",  
    "value": true  
  },  
  "permittedContactForce": {  
    "type": "Property",  
    "value": "Tonight service coach bag but our score. Reveal right become shoulder meet family wind edge."  
  },  
  "phaseInfo": {  
    "type": "Property",  
    "value": "Indicate cell Mrs democratic. Suggest training hair prepare."  
  },  
  "phaseSeparation": {  
    "type": "Property",  
    "value": false  
  },  
  "publicNetworkRoaming": {  
    "type": "Property",  
    "value": false  
  },  
  "publicNetworkRoamingDetails": {  
    "type": "Property",  
    "value": "Without day itself him edge. Yard will back investment however memory. Area reality image people lose life government."  
  },  
  "qNvsbtsmperm": {  
    "type": "Property",  
    "value": false  
  },  
  "radioNetworkId": {  
    "type": "Property",  
    "value": 608  
  },  
  "railSystemType": {  
    "type": "Property",  
    "value": "Top particularly industry around performance. Know compare live past produce."  
  },  
  "raisedPantographsDistanceAndSpeed": {  
    "type": "Property",  
    "value": "Performance modern according staff everything. Mrs dark sometimes turn thousand then ever. Every defense arm plant."  
  },  
  "redLightsRequired": {  
    "type": "Property",  
    "value": false  
  },  
  "specificInformation": {  
    "type": "Property",  
    "value": "Lose friend enter fear prevent. Rule oil drop d"  
  },  
  "structureCheckLocation": {  
    "type": "Property",  
    "value": 735.1  
  },  
  "subsetName": {  
    "type": "Property",  
    "value": "Almost"  
  },  
  "switchProtectControlWarning": {  
    "type": "Property",  
    "value": true  
  },  
  "switchRadioSystem": {  
    "type": "Property",  
    "value": true  
  },  
  "systemSeparationInfo": {  
    "type": "Property",  
    "value": "Financial require seat image large prepare. Manage forget turn business."  
  },  
  "tNvcontact": {  
    "type": "Property",  
    "value": 80  
  },  
  "tNvovtrp": {  
    "type": "Property",  
    "value": 521  
  },  
  "tenGISId": {  
    "type": "Property",  
    "value": "Consumer father fill air. Real"  
  },  
  "tiltingSupported": {  
    "type": "Property",  
    "value": false  
  },  
  "trainIntegrityOnBoardRequired": {  
    "type": "Property",  
    "value": false  
  },  
  "tsiSwitchCrossing": {  
    "type": "Property",  
    "value": false  
  },  
  "usesGroup555": {  
    "type": "Property",  
    "value": true  
  },  
  "vNvallowovtrp": {  
    "type": "Property",  
    "value": 152  
  },  
  "vNvsupovtrp": {  
    "type": "Property",  
    "value": 745  
  },  
  "vehicleTypesCompatibleTrafficLoad": {  
    "type": "Property",  
    "value": "Investment magazine these Republican life agency box bill. Service born hope west h"  
  },  
  "vehiclesCompatibleTrafficLoad": {  
    "type": "Property",  
    "value": "Soldier so card. Current discussion majority grow capital. Dream player push list else five or."  
  },  
  "verificationCCS": {  
    "type": "Property",  
    "value": "Understand image child total hot. Enter stage still happen politics theory "  
  },  
  "verificationENE": {  
    "type": "Property",  
    "value": "Sell wall glass imagine president piece. Bed above sign owner own require a"  
  },  
  "TSIMagneticFields": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSIMagneticFields:YETD:71552341"  
  },  
  "TSITractionHarmonics": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:TSITractionHarmonics:XJRB:92668078"  
  },  
  "atoCommunicationSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoCommunicationSystem:YJHK:25146078"  
  },  
  "atoGradeAutomation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoGradeAutomation:NGXM:88258398"  
  },  
  "atoSystemVersion": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:atoSystemVersion:HGKL:66451400"  
  },  
  "cantDeficiencyBasicSSP": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:cantDeficiencyBasicSSP:MXZF:17947559"  
  },  
  "conditionsUseReflectivePlates": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:conditionsUseReflectivePlates:RUMA:61322622"  
  },  
  "contactLineSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactLineSystem:ELBB:74359791"  
  },  
  "contactStripMaterial": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:contactStripMaterial:DFSL:17845103"  
  },  
  "dataRadioCompatible": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:dataRadioCompatible:PIFT:62735259"  
  },  
  "eddyCurrentBraking": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:eddyCurrentBraking:PQLI:07763157"  
  },  
  "etcsDegradedSituation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsDegradedSituation:XOKG:98634550"  
  },  
  "etcsInfill": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsInfill:NETA:33742148"  
  },  
  "etcsLevel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsLevel:ZBNX:62993357"  
  },  
  "etcsMVersion": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsMVersion:MUUO:53142156"  
  },  
  "etcsTransmittedTrackConditions": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:etcsTransmittedTrackConditions:SPXX:96763419"  
  },  
  "freightCorridor": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:freightCorridor:CEIX:72574968"  
  },  
  "gaugingProfile": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gaugingProfile:KVHC:21558525"  
  },  
  "gsmRActiveMobiles": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRActiveMobiles:CYIY:43705461"  
  },  
  "gsmROptionalFunctions": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmROptionalFunctions:EEKJ:86360026"  
  },  
  "gsmRVersion": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmRVersion:HLYF:21513072"  
  },  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrConstraintsOperateOnlyInCircuitSwitch:GCYG:90039353"  
  },  
  "gsmrNetworkCoverage": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:gsmrNetworkCoverage:YJUN:26445648"  
  },  
  "hotAxleBoxDetectorDirection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:hotAxleBoxDetectorDirection:QPFQ:28273281"  
  },  
  "legacyRadioSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:legacyRadioSystem:FUSZ:34428582"  
  },  
  "lineCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:lineCategory:RGCO:85229035"  
  },  
  "linesideDistanceIndicationAppearance": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationAppearance:LLGD:29505059"  
  },  
  "linesideDistanceIndicationPositioning": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:linesideDistanceIndicationPositioning:TSCK:55243683"  
  },  
  "loadCapability": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:loadCapability:HRFK:52472482"  
  },  
  "mNvcontact": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:mNvcontact:ENBE:86876189"  
  },  
  "magneticBraking": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:magneticBraking:CQQU:03536027"  
  },  
  "osmClass": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:osmClass:BIXX:14601767"  
  },  
  "otherCantDeficiencyBasicSSP": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherCantDeficiencyBasicSSP:FLBU:13071514"  
  },  
  "otherPantographHead": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherPantographHead:RQHY:17784567"  
  },  
  "otherTrainProtection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:otherTrainProtection:QEUL:24767807"  
  },  
  "passesThroughTunnel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:passesThroughTunnel:RVPL:47739741"  
  },  
  "platform": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:platform:LBTD:46534566"  
  },  
  "profileNumberSemiTrailers": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSemiTrailers:VSLI:98951041"  
  },  
  "profileNumberSwapBodies": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:profileNumberSwapBodies:PKGU:10889914"  
  },  
  "protectionLegacySystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:protectionLegacySystem:VDVG:36463208"  
  },  
  "qNvdriverAdhes": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvdriverAdhes:HZYL:22374007"  
  },  
  "qNvemrrls": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:qNvemrrls:QMHE:10697778"  
  },  
  "railInclination": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:railInclination:YGLS:70579726"  
  },  
  "reasonsEtcsRadioBlockCenterReject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:reasonsEtcsRadioBlockCenterReject:AGKX:72529171"  
  },  
  "safeConsistLengthInformationNecessary": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:safeConsistLengthInformationNecessary:DTEV:72904047"  
  },  
  "standardCombinedTransporRollerUnits": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransporRollerUnits:DMLM:74143959"  
  },  
  "standardCombinedTransportContainers": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:standardCombinedTransportContainers:BMYF:71612243"  
  },  
  "temperatureRange": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:temperatureRange:MKMW:85982547"  
  },  
  "trackLoadCapability": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackLoadCapability:BQAC:30254673"  
  },  
  "trackPhaseInfo": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackPhaseInfo:TMME:74285663"  
  },  
  "trackRaisedPantographsDistanceAndSpeed": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackRaisedPantographsDistanceAndSpeed:LWCZ:50651782"  
  },  
  "trackSystemSeparationInfo": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trackSystemSeparationInfo:OOCP:57288872"  
  },  
  "trainDetectionSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:trainDetectionSystem:CGRT:45814692"  
  },  
  "tsiPantographHead": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SubsetWithCommonCharacteristics:tsiPantographHead:GJFU:60443579"  
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

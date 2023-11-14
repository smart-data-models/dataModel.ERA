<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティトラック  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ERA/blob/master/Track/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明：**列車の運行に使用される線路。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `IdPhoneErtmsRadioBlockCenter[string]`: ERTMS/ETCS無線ブロックセンターのIDと電話番号  - `TSIMagneticFields[uri]`: 自動車から放出される磁場に関する規則の存在とTSIへの適合性  - `TSITractionHarmonics[uri]`: 自動車のトラクション電流における高調波規制の存在とTSIへの適合性  - `accelerationLevelCrossing[string]`: 踏切での加速  - `additionalBrakingInformationDocument[string]`: ブレーキ性能に関するIMが入手可能な文書  - `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `atoCommunicationSystem[uri]`: ATO通信システム  - `atoErrorCorrectionsOnboard[string]`: オンボードに必要なATOエラー修正  - `atoGradeAutomation[uri]`: ATOグレード・オブ・オートメーション  - `atoSystemVersion[uri]`: ATOシステムバージョン  - `automaticDroppingDeviceRequired[boolean]`: 自動落下装置が必要  - `bigMetalMass[boolean]`: 大きな金属の塊  - `bridge[boolean]`: ブリッジ  - `cantDeficiency[number]`: カント不足  - `cantDeficiencyBasicSSP[uri]`: 基本的なSSPに使用されるカント欠乏症  - `compatibilityProcedureDocument[string]`: スタティックルートとダイナミックルートの互換性チェックの手順を記載した文書  - `conditionsSwitchClassBSystems[string]`: ERTMS/ETCSとクラスBシステム間の切り替えに必要な特別な技術的条件  - `conditionsSwitchTrainProtectionSystems[string]`: 異なるクラスBの列車保護、制御、警報システムを切り替えるための特別な条件  - `conditionsUseReflectivePlates[uri]`: 反射板の使用条件  - `contactLineSystem[uri]`: コンタクトライン方式  - `contactStripMaterial[uri]`: 許可されたコンタクトストリップ材料  - `contactStripMaterialMetallicContent[number]`: コンタクトストリップ材 金属含有量  - `dNvovtrp[number]`: D_NVOVTRP  - `dNvpotrp[number]`: D_NVPOTRP  - `dNvroll[number]`: D_NVROLL  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dataRadioCompatible[uri]`: 無線システム互換性データ  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `demonstrationENE[string]`: EIトラック実証宣言（ENE）  - `demonstrationINF[string]`: EIトラック／サイディング実証宣言 [INF］  - `description[string]`: この商品の説明  - `distSignToPhaseEnd[number]`: 看板と相分離終点までの距離  - `documentRestrictionPositionContactLineSeparation[string]`: 接触線分離を遵守するために、マルチプル・トラクション・ユニットの位置に関する制限を文書化する。  - `documentRestrictionPowerConsumption[string]`: 特定の電気牽引装置の消費電力に関する制限を記載した文書  - `eddyCurrentBraking[uri]`: 渦電流ブレーキの使用  - `eddyCurrentBrakingConditionsDocument[string]`: 渦電流ブレーキの使用条件を記載した文書  - `etcsDegradedSituation[uri]`: デグレード時のETCSレベル  - `etcsErrorCorrectionsOnboard[string]`: 車載に必要なETCSエラー修正  - `etcsImplementsLevelCrossingProcedure[boolean]`: ETCSトラックサイドが踏切手順または同等のソリューションを実施する。  - `etcsInfill[uri]`: ラインサイドに設置されたETCSインフィル  - `etcsInfillLineAccess[boolean]`: ラインアクセスに必要なETCSインフィル  - `etcsLevel[uri]`: その他レベル  - `etcsMVersion[uri]`: ETCS M_バージョン  - `etcsNationalPacket44[boolean]`: ETCS全国パケット44アプリケーションの実装  - `etcsOptionalFunctions[string]`: ETCSオプション機能  - `etcsSystemCompatibility[uri]`: ETCSシステムの互換性  - `etcsSystemFunctionalitiesNextFiveYears[string]`: 今後5年間に必要とされるETCSシステムのバージョン2.2または3.0の機能  - `etcsTransmitsTrackConditions[boolean]`: ETCSはトラックサイドでトラックコンディションを送信するように設計されているか？  - `etcsTransmittedTrackConditions[uri]`: 送信可能なトラック状況  - `flangeLubeForbidden[boolean]`: フランジ潤滑の使用禁止  - `freightCorridor[uri]`: 鉄道貨物コリドーの一部  - `gaugingCheckLocation[string]`: 特定のチェックが必要な鉄道地点  - `gaugingProfile[uri]`: ゲージング  - `gaugingTransversalDocument[string]`: 特定のチェックが必要な箇所の横断面を文書化する。  - `gprsForETCS[boolean]`: ETCS用GPRS  - `gprsImplementationArea[string]`: GPRSの導入地域  - `gradientProfile[string]`: 勾配プロファイル  - `gsmRActiveMobiles[uri]`: ETCSレベル2（またはレベル3）において、運用を中断することなく無線ブロックセンターのハンドオーバーを行うために必要な、アクティブなGSM-R移動機（EDOR）の数、または同時通信セッションの数。  - `gsmRAdditionalInfo[string]`: ネットワーク特性に関する追加情報  - `gsmRNoCoverage[boolean]`: GSM-Rカバレッジなし  - `gsmROptionalFunctions[uri]`: オプションのGSM-R機能  - `gsmRVersion[uri]`: GSM-Rバージョン  - `gsmrConstraintsOperateOnlyInCircuitSwitch[uri]`: GSM-Rネットワーク事業者がETCS車載器に課した、回線交換でのみ動作可能な特定の制約  - `gsmrErrorCorrectionsOnboard[string]`: オンボードに必要なGSM-Rエラー訂正  - `gsmrForcedDeregistrationFunctionalNumber[boolean]`: GSM-Rネットワークは、他のドライバによる機能番号の強制登録解除を許可するように構成されている。  - `gsmrNetworkCoverage[uri]`: ローミング契約の対象となるGSM-Rネットワーク  - `hasAdditionalBrakingInformation[boolean]`: IMによる追加情報の提供  - `hasBallast[boolean]`: バラストの存在  - `hasETCSRestrictionsConditions[boolean]`: 営業上の制限または条件の存在  - `hasHotAxleBoxDetector[boolean]`: トラックサイドのホットアクスルボックス検出器（HABD）の存在  - `hasLevelCrossings[boolean]`: 踏切の存在  - `hasOtherTrainProtection[boolean]`: その他の列車保護、制御、警報システムの設置の有無  - `hasSevereWeatherConditions[boolean]`: 厳しい気候条件の存在  - `hasSystemSeparation[boolean]`: システム分離  - `hasTSITrainDetection[boolean]`: TSIに完全に準拠した列車検知システムの存在  - `highSpeedLoadModelCompliance[boolean]`: 高速荷重モデル（HSLM）動的荷重モデルに対する構造物の適合性  - `hotAxleBoxDetectorDirection[uri]`: ホットアクスルボックスの検知方向  - `hotAxleBoxDetectorGeneration[string]`: トラックサイドHABDの生成  - `hotAxleBoxDetectorIdentification[string]`: トラックサイドHABDの特定  - `hotAxleBoxDetectorLocation[number]`: 沿線HABDの鉄道位置  - `hotAxleBoxDetectorTSICompliant[boolean]`: トラックサイドHABD TSI準拠  - `id[*]`: エンティティの一意識別子  - `instructionsSwitchRadioSystems[string]`: 異なる無線システムを切り替えるための特別な指示  - `isQuietRoute[boolean]`: より静かな路線に所属  - `legacyRadioSystem[uri]`: その他の無線システムの設置（無線レガシーシステム）  - `lineCategory[uri]`: ラインのカテゴリー  - `linesideDistanceIndicationAppearance[uri]`: ラインサイド距離表示外観  - `linesideDistanceIndicationFrequency[number]`: ラインサイド距離表示周波数  - `linesideDistanceIndicationPositioning[uri]`: ラインサイド距離表示位置決め  - `loadCapability[uri]`: 負荷能力  - `localRulesOrRestrictions[boolean]`: 厳密に地域的な性質の規則や制限の存在。  - `localRulesOrRestrictionsDoc[string]`: IMが入手できる、厳密にローカルな性質の規則または制限に関する文書  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `mNvcontact[uri]`: M_NVCONTACT  - `mNvderun[boolean]`: M_NVDERUN  - `magneticBraking[uri]`: 磁気ブレーキの使用  - `magneticBrakingConditionsDocument[string]`: 磁気ブレーキの使用条件を記載した文書  - `maximumAltitude[number]`: 最高高度  - `maximumBrakingDistance[number]`: 最大制動距離  - `maximumContactWireHeight[number]`: コンタクトワイヤーの最大高さ  - `maximumPermittedSpeed[number]`: 最大許容速度  - `maximumTemperature[number]`: 温度範囲（最大）  - `maximumTrainDeceleration[number]`: 列車の最大減速  - `minDistConsecutiveAxles[number]`: 連続する2つの車軸間の最小許容距離  - `minDistFirstLastAxle[number]`: 最初の車軸と最後の車軸の間の最小許容距離  - `minFlangeHeight[number]`: フランジの最低許容高さ  - `minFlangeThickness[number]`: フランジの最小許容厚さ  - `minRimWidth[number]`: リムの最小許容幅  - `minWheelDiameter[number]`: 許容最小ホイール径  - `minimumContactWireHeight[number]`: コンタクトワイヤーの最小高さ  - `minimumHorizontalRadius[number]`: 水平カーブの最小半径  - `minimumTemperature[number]`: 温度範囲（最小）  - `minimumWheelDiameter[number]`: 固定鈍角交差の最小車輪直径  - `multipleTrainProtectionRequired[boolean]`: 車内に複数の列車保護、制御、警告システムが必要  - `name[string]`: このアイテムの名前  - `nationalLoadCapability[string]`: 負荷能力に関する国家分類  - `nationalValuesBrakeModel[string]`: ブレーキモデルに使用される国の値  - `osmClass[uri]`: オープンストリートマップクラス  - `otherCantDeficiencyBasicSSP[uri]`: ETCSがSSPを提供するようトラックサイドに設定されているその他のCant Deficiency列車カテゴリー  - `otherPantographHead[uri]`: その他のパンタグラフ・ヘッドを受け入れる  - `otherTrainProtection[uri]`: その他の列車保護、制御、劣化状況警告システム  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `passesThroughTunnel[uri]`: トンネルを通過  - `permitUseReflectivePlates[boolean]`: 反射板の使用許可  - `permittedContactForce[string]`: 許容接触力  - `phaseInfo[string]`: 相分離に関する情報  - `phaseSeparation[boolean]`: 相分離  - `platform[uri]`: プラットフォーム  - `profileNumberSemiTrailers[uri]`: セミトレーラ用標準複合輸送プロファイル番号  - `profileNumberSwapBodies[uri]`: スワップボディ用標準複合輸送プロファイル番号  - `protectionLegacySystem[uri]`: 列車保護レガシーシステム  - `publicNetworkRoaming[boolean]`: GSM-R 公共ネットワークへのローミングの存在  - `publicNetworkRoamingDetails[string]`: 公共ネットワークへのローミングに関するGSM-Rの詳細  - `qNvdriverAdhes[uri]`: q_nvdriver_adhes  - `qNvemrrls[uri]`: Q_NVEMRRLS  - `qNvsbtsmperm[boolean]`: Q_NVSBTSMPERM  - `radioNetworkId[number]`: 無線ネットワークID  - `railInclination[uri]`: レール傾斜  - `raisedPantographsDistanceAndSpeed[string]`: 所定速度でのパンタグラフの上昇数と間隔に関する要件  - `reasonsEtcsRadioBlockCenterReject[uri]`: ETCS無線ブロックセンターが列車を拒否できる理由  - `redLightsRequired[boolean]`: 赤色定常点灯が必要  - `safeConsistLengthInformationNecessary[uri]`: ラインとSILにアクセスするために必要な船上からの安全な構成長情報  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `specificInformation[string]`: 具体的な情報  - `standardCombinedTransporRollerUnits[uri]`: ローラーユニットの標準複合輸送プロファイル番号  - `standardCombinedTransportContainers[uri]`: コンテナの標準複合輸送プロファイル番号  - `structureCheckLocation[number]`: 特定のチェックが必要な構造物の鉄道での位置  - `switchProtectControlWarning[boolean]`: 走行中の異なる保護、制御、警告システム間の切り替えの存在  - `switchRadioSystem[boolean]`: 異なる無線システム間のスイッチ・オーバーの存在  - `systemSeparationInfo[string]`: システム分離に関する情報  - `tNvcontact[number]`: T_NVCONTACT  - `tNvovtrp[number]`: T_NVOVTRP  - `temperatureRange[uri]`: 温度範囲  - `tenClassification[uri]`: TEN分類（線路、ホーム、サイディング）  - `tenGISId[string]`: TEN GISアイデンティティ  - `tiltingSupported[boolean]`: ETCSでチルト機能がサポートされているかどうかの表示  - `trackDirection[uri]`: 通常の走行方向  - `trackId[string]`: トラックの識別  - `trackLoadCapability[uri]`: トラック積載能力  - `trackPhaseInfo[uri]`: トラック位相情報  - `trackRaisedPantographsDistanceAndSpeed[uri]`: 上昇したパンタグラフの距離と速度を追跡  - `trackSystemSeparationInfo[uri]`: トラックシステム分離情報  - `trainDetectionSystem[uri]`: 列車検知システム  - `trainIntegrityOnBoardRequired[boolean]`: 線路へのアクセスに必要な（運転手ではなく）車内からの列車完全性の確認  - `tsiPantographHead[uri]`: TSI準拠のパンタグラフ・ヘッドに対応  - `tsiSwitchCrossing[boolean]`: スイッチおよびクロッシングのインサービス値のTSI適合性  - `type[string]`: NGSIデータ型。トラック  - `usesGroup555[boolean]`: GSM-Rによるグループ555の使用  - `vNvallowovtrp[number]`: V_NVALLOWTRP  - `vNvsupovtrp[number]`: V_NVSUPOVTRP  - `vehicleTypesCompatibleTrafficLoad[string]`: インフラおよび列車検知システムの交通負荷および耐荷重に適合することが確認されている車種のリスト。  - `vehiclesCompatibleTrafficLoad[string]`: インフラおよび列車検知システムの交通負荷および耐荷重に適合することが確認されている車両のリスト。  - `verificationCCS[string]`: ECトラック検証宣言（CCS）  - `verificationENE[string]`: ECトラック検証宣言（ENE）  - `verificationINF[string]`: トラック／サイディングのEC検証宣言 [INF］  - `voiceRadioCompatible[uri]`: 無線システム互換ボイス  - `wheelSetGauge[uri]`: 公称軌道軌間  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
ERAオントロジー https://data-interop.era.europa.eu/era-vocabulary （欧州鉄道庁）からマッピングされたデータモデル。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Track:    
  description: A running track that is used for train service movements.    
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
    bridge:    
      description: Is bridge    
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
    demonstrationINF:    
      description: 'EI declaration of demonstration for track/siding [INF]'    
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
    etcsSystemCompatibility:    
      description: ETCS system compatibility    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    localRulesOrRestrictions:    
      description: Existence of rules and restrictions of a strictly local nature.    
      type: boolean    
      x-ngsi:    
        type: Property    
    localRulesOrRestrictionsDoc:    
      description: Documents regarding the rules or restrictions of a strictly local nature available by the IM    
      type: string    
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
    tenClassification:    
      description: 'TEN classification (of track, of platform, of siding)'    
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
    trackDirection:    
      description: Normal running direction    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    trackId:    
      description: Identification of track    
      type: string    
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
      description: NGSI data type. It has to be Track    
      enum:    
        - Track    
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
    verificationINF:    
      description: 'EC declaration of verification for track/siding [INF]'    
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
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: http://data.europa.eu/949/Track    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ERA/blob/master/Track/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ERA/Certificate/schema.json    
  x-model-tags: 'ERA vocabulary, railway, train'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### NGSI-v2 キー値の追跡 例  
以下は、JSON-LD形式のTrackをkey-valuesとして返す例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Track:id:OOXM:87352290",  
  "dateCreated": "1999-12-30T09:02:54Z",  
  "dateModified": "2011-07-03T23:49:28Z",  
  "source": "Particularly hit determine. Three north girl table save adult use.",  
  "name": "Risk fall allow table mother soon parent. Cost sure difficult. Executive traditional response wish identify onto.",  
  "alternateName": "Message to pick partner nothing. Five short better assume. Air she help land.",  
  "description": "Loss so own entire teach. Mrs anyone true small century nor reveal.",  
  "dataProvider": "Natural cultural toward office. Hour where job pretty her.",  
  "owner": [  
    "urn:ngsi-ld:Track:items:IPKE:18505641",  
    "urn:ngsi-ld:Track:items:LAWY:56608364"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Track:items:BKZL:67048585"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      61.970078,  
      -74.303326  
    ]  
  },  
  "address": {  
    "streetAddress": "Interview today ago. Eight together class financial former forward under. Hope no window fall discuss we foreign glass.",  
    "addressLocality": "Resource respond arrive remain use most. Process ",  
    "addressRegion": "Job start fish church. Or however baby possible front positive what. Writer last hospital item describe special. Lot experience rule.",  
    "addressCountry": "Section ",  
    "postalCode": "Size though picture school artist. Include might result value especially five. Wife article tend production.",  
    "postOfficeBoxNumber": "Buy how fine note actually democratic. Such family type give send. Start cause build cut suggest.",  
    "streetNr": "Resource give top movement. Southern their than last.",  
    "district": "Center ready threat chance wide. Because than shoulder near. Head wind fall pl"  
  },  
  "areaServed": "Management really",  
  "type": "Track",  
  "IdPhoneErtmsRadioBlockCenter": "Become name off project born far significant. Teacher water become big.",  
  "accelerationLevelCrossing": "Today wait agree car build phone local.",  
  "additionalBrakingInformationDocument": "Shake himself their lot. Home show two guess society find assume. Sign hand price apply likely art arrive.",  
  "atoErrorCorrectionsOnboard": "Green writer religious even. Million up tax city everyone why strong comp",  
  "automaticDroppingDeviceRequired": false,  
  "bigMetalMass": false,  
  "bridge": false,  
  "cantDeficiency": 864,  
  "compatibilityProcedureDocument": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "conditionsSwitchClassBSystems": "Together range line beyond. First policy daughter need kind miss.",  
  "conditionsSwitchTrainProtectionSystems": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "contactStripMaterialMetallicContent": 864,  
  "dNvovtrp": 864,  
  "dNvpotrp": 864,  
  "dNvroll": 864,  
  "demonstrationENE": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth ",  
  "demonstrationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "distSignToPhaseEnd": 864,  
  "documentRestrictionPositionContactLineSeparation": "A",  
  "documentRestrictionPowerConsumption": "Together ra",  
  "eddyCurrentBrakingConditionsDocument": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "etcsErrorCorrectionsOnboard": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "etcsImplementsLevelCrossingProcedure": false,  
  "etcsInfillLineAccess": false,  
  "etcsNationalPacket44": true,  
  "etcsOptionalFunctions": "First drug contain start almost wonder. Live bed serious theory type. Together t",  
  "etcsSystemFunctionalitiesNextFiveYears": "Produce you true soldier bank party main. Friend couple administration even relate",  
  "etcsTransmitsTrackConditions": true,  
  "flangeLubeForbidden": true,  
  "gaugingCheckLocation": "Paper of",  
  "gaugingTransversalDocument": "Decision song view age international big employee. Author feeling job article level.",  
  "gprsForETCS": true,  
  "gprsImplementationArea": "Employee toward like total now. Whom around put suddenly garden. Bring TV program actually race.",  
  "gradientProfile": "True power home price check real leader. From animal exactly drive. Good explain grow water plant perf",  
  "gsmRAdditionalInfo": "Stock ball organization recognize civil",  
  "gsmRNoCoverage": false,  
  "gsmrErrorCorrectionsOnboard": "Traditional pag",  
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
  "hotAxleBoxDetectorIdentification": "The everything affect American. Next water voice travel amo",  
  "hotAxleBoxDetectorLocation": 855.9,  
  "hotAxleBoxDetectorTSICompliant": false,  
  "instructionsSwitchRadioSystems": "Modern power political",  
  "isQuietRoute": false,  
  "linesideDistanceIndicationFrequency": 864,  
  "localRulesOrRestrictions": false,  
  "localRulesOrRestrictionsDoc": "Else memory if. Whose group through ",  
  "mNvderun": true,  
  "magneticBrakingConditionsDocument": "Role together range line. Government first policy daughter.",  
  "maximumAltitude": 468.7,  
  "maximumBrakingDistance": 864,  
  "maximumContactWireHeight": 249.2,  
  "maximumPermittedSpeed": 864,  
  "maximumTemperature": 864,  
  "maximumTrainDeceleration": 150.8,  
  "minDistConsecutiveAxles": 864,  
  "minDistFirstLastAxle": 864,  
  "minFlangeHeight": 636.8,  
  "minFlangeThickness": 42.8,  
  "minRimWidth": 903.6,  
  "minWheelDiameter": 864,  
  "minimumContactWireHeight": 950.2,  
  "minimumHorizontalRadius": 864,  
  "minimumTemperature": 864,  
  "minimumWheelDiameter": 864,  
  "multipleTrainProtectionRequired": false,  
  "nationalLoadCapability": "Else memory if. Whose group through despite cause. Sense peace economy trave",  
  "nationalValuesBrakeModel": "Financial role together range. Nice government first policy daughter need kind. Employee source nature add rest human statio",  
  "permitUseReflectivePlates": true,  
  "permittedContactForce": "Language ball floor meet usually board necessary. Natural",  
  "phaseInfo": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type successful together. Raise study modern miss dog Democrat quickly.",  
  "phaseSeparation": false,  
  "publicNetworkRoaming": false,  
  "publicNetworkRoamingDetails": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and.",  
  "qNvsbtsmperm": true,  
  "radioNetworkId": 864,  
  "raisedPantographsDistanceAndSpeed": "American whole magazine truth stop whose. On traditional measure example sense peace. W",  
  "redLightsRequired": true,  
  "specificInformation": "Line beyon",  
  "structureCheckLocation": 636.5,  
  "switchProtectControlWarning": true,  
  "switchRadioSystem": true,  
  "systemSeparationInfo": "Sure allow together find pass under. Language Republican strategy really office program us. Shoulder weight fly participant from campaign avoid.",  
  "tNvcontact": 864,  
  "tNvovtrp": 864,  
  "tenGISId": "American whole magazine truth stop whose. On traditional measure example sense",  
  "tiltingSupported": true,  
  "trackId": "Line beyond its particularly",  
  "trainIntegrityOnBoardRequired": true,  
  "tsiSwitchCrossing": false,  
  "usesGroup555": false,  
  "vNvallowovtrp": 864,  
  "vNvsupovtrp": 864,  
  "vehicleTypesCompatibleTrafficLoad": "American whole magazine truth stop whose. On traditional measure example sense peace. Would",  
  "vehiclesCompatibleTrafficLoad": "Together range line beyond. First policy daughter need kind miss.",  
  "verificationCCS": "Trouble behavior style report size pe",  
  "verificationENE": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "verificationINF": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type succes",  
  "TSIMagneticFields": "urn:ngsi-ld:Track:TSIMagneticFields:TDPS:69477515",  
  "TSITractionHarmonics": "urn:ngsi-ld:Track:TSITractionHarmonics:ZFKN:53304135",  
  "atoCommunicationSystem": "urn:ngsi-ld:Track:atoCommunicationSystem:VCAD:01230989",  
  "atoGradeAutomation": "urn:ngsi-ld:Track:atoGradeAutomation:BTAG:39916151",  
  "atoSystemVersion": "urn:ngsi-ld:Track:atoSystemVersion:TDIC:21730086",  
  "cantDeficiencyBasicSSP": "urn:ngsi-ld:Track:cantDeficiencyBasicSSP:OBTD:31456208",  
  "conditionsUseReflectivePlates": "urn:ngsi-ld:Track:conditionsUseReflectivePlates:YBZV:63457923",  
  "contactLineSystem": "urn:ngsi-ld:Track:contactLineSystem:VFAP:22584197",  
  "contactStripMaterial": "urn:ngsi-ld:Track:contactStripMaterial:RWAO:69845642",  
  "dataRadioCompatible": "urn:ngsi-ld:Track:dataRadioCompatible:LTJV:15084237",  
  "eddyCurrentBraking": "urn:ngsi-ld:Track:eddyCurrentBraking:ATGW:59924661",  
  "etcsDegradedSituation": "urn:ngsi-ld:Track:etcsDegradedSituation:BMWS:52337696",  
  "etcsInfill": "urn:ngsi-ld:Track:etcsInfill:QPRT:60271427",  
  "etcsLevel": "urn:ngsi-ld:Track:etcsLevel:GRUC:00754706",  
  "etcsMVersion": "urn:ngsi-ld:Track:etcsMVersion:WYAV:20665030",  
  "etcsSystemCompatibility": "urn:ngsi-ld:Track:etcsSystemCompatibility:IWFD:89131934",  
  "etcsTransmittedTrackConditions": "urn:ngsi-ld:Track:etcsTransmittedTrackConditions:EUQU:76104714",  
  "freightCorridor": "urn:ngsi-ld:Track:freightCorridor:VIRK:51240003",  
  "gaugingProfile": "urn:ngsi-ld:Track:gaugingProfile:RFGM:59097765",  
  "gsmRActiveMobiles": "urn:ngsi-ld:Track:gsmRActiveMobiles:ZLWC:94022455",  
  "gsmROptionalFunctions": "urn:ngsi-ld:Track:gsmROptionalFunctions:JLMR:59004229",  
  "gsmRVersion": "urn:ngsi-ld:Track:gsmRVersion:QXCJ:24173042",  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": "urn:ngsi-ld:Track:gsmrConstraintsOperateOnlyInCircuitSwitch:PKZZ:65461187",  
  "gsmrNetworkCoverage": "urn:ngsi-ld:Track:gsmrNetworkCoverage:KXVE:51717604",  
  "hotAxleBoxDetectorDirection": "urn:ngsi-ld:Track:hotAxleBoxDetectorDirection:BMAD:29611133",  
  "legacyRadioSystem": "urn:ngsi-ld:Track:legacyRadioSystem:NCLH:68847793",  
  "lineCategory": "urn:ngsi-ld:Track:lineCategory:WAQO:49263511",  
  "linesideDistanceIndicationAppearance": "urn:ngsi-ld:Track:linesideDistanceIndicationAppearance:TEDG:31764303",  
  "linesideDistanceIndicationPositioning": "urn:ngsi-ld:Track:linesideDistanceIndicationPositioning:ESMU:76582197",  
  "loadCapability": "urn:ngsi-ld:Track:loadCapability:THAK:68757738",  
  "mNvcontact": "urn:ngsi-ld:Track:mNvcontact:MSJW:55082492",  
  "magneticBraking": "urn:ngsi-ld:Track:magneticBraking:BJAY:71180132",  
  "osmClass": "urn:ngsi-ld:Track:osmClass:QQBS:75227586",  
  "otherCantDeficiencyBasicSSP": "urn:ngsi-ld:Track:otherCantDeficiencyBasicSSP:TNPZ:18916348",  
  "otherPantographHead": "urn:ngsi-ld:Track:otherPantographHead:QSIK:69930024",  
  "otherTrainProtection": "urn:ngsi-ld:Track:otherTrainProtection:FUEH:17446660",  
  "passesThroughTunnel": "urn:ngsi-ld:Track:passesThroughTunnel:TWCV:45007627",  
  "platform": "urn:ngsi-ld:Track:platform:BDPY:25609767",  
  "profileNumberSemiTrailers": "urn:ngsi-ld:Track:profileNumberSemiTrailers:WRUL:20099251",  
  "profileNumberSwapBodies": "urn:ngsi-ld:Track:profileNumberSwapBodies:UKUD:36710979",  
  "protectionLegacySystem": "urn:ngsi-ld:Track:protectionLegacySystem:BZMO:94264183",  
  "qNvdriverAdhes": "urn:ngsi-ld:Track:qNvdriverAdhes:IAQV:53751007",  
  "qNvemrrls": "urn:ngsi-ld:Track:qNvemrrls:QJDE:99331886",  
  "railInclination": "urn:ngsi-ld:Track:railInclination:NYEX:69611611",  
  "reasonsEtcsRadioBlockCenterReject": "urn:ngsi-ld:Track:reasonsEtcsRadioBlockCenterReject:CLCD:07660754",  
  "safeConsistLengthInformationNecessary": "urn:ngsi-ld:Track:safeConsistLengthInformationNecessary:CTEG:50552035",  
  "standardCombinedTransporRollerUnits": "urn:ngsi-ld:Track:standardCombinedTransporRollerUnits:HEFO:03104509",  
  "standardCombinedTransportContainers": "urn:ngsi-ld:Track:standardCombinedTransportContainers:KPJJ:17542035",  
  "temperatureRange": "urn:ngsi-ld:Track:temperatureRange:JFME:85291189",  
  "tenClassification": "urn:ngsi-ld:Track:tenClassification:LNVB:23583324",  
  "trackDirection": "urn:ngsi-ld:Track:trackDirection:JRNX:29061126",  
  "trackLoadCapability": "urn:ngsi-ld:Track:trackLoadCapability:ULUQ:29645137",  
  "trackPhaseInfo": "urn:ngsi-ld:Track:trackPhaseInfo:LJPC:06606573",  
  "trackRaisedPantographsDistanceAndSpeed": "urn:ngsi-ld:Track:trackRaisedPantographsDistanceAndSpeed:MFYN:21418927",  
  "trackSystemSeparationInfo": "urn:ngsi-ld:Track:trackSystemSeparationInfo:OUUC:62375825",  
  "trainDetectionSystem": "urn:ngsi-ld:Track:trainDetectionSystem:GJDY:73407970",  
  "tsiPantographHead": "urn:ngsi-ld:Track:tsiPantographHead:YHRY:48926717",  
  "voiceRadioCompatible": "urn:ngsi-ld:Track:voiceRadioCompatible:MQSW:64014004",  
  "wheelSetGauge": "urn:ngsi-ld:Track:wheelSetGauge:CBCZ:67145439",  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### トラック NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のTrackの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Track:id:OOXM:87352290",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1999-12-30T09:02:54Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2011-07-03T23:49:28Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": "Particularly hit determine. Three north girl table save adult use."  
  },  
  "name": {  
    "type": "Text",  
    "value": "Risk fall allow table mother soon parent. Cost sure difficult. Executive traditional response wish identify onto."  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Message to pick partner nothing. Five short better assume. Air she help land."  
  },  
  "description": {  
    "type": "Text",  
    "value": "Loss so own entire teach. Mrs anyone true small century nor reveal."  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Natural cultural toward office. Hour where job pretty her."  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Track:items:IPKE:18505641",  
      "urn:ngsi-ld:Track:items:LAWY:56608364"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Track:items:BKZL:67048585"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": {  
        "type": "StructuredValue",  
        "value": [  
          61.970078,  
          -74.303326  
        ]  
      }  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": {  
        "type": "Text",  
        "value": "Interview today ago. Eight together class financial former forward under. Hope no window fall discuss we foreign glass."  
      },  
      "addressLocality": {  
        "type": "Text",  
        "value": "Resource respond arrive remain use most. Process "  
      },  
      "addressRegion": {  
        "type": "Text",  
        "value": "Job start fish church. Or however baby possible front positive what. Writer last hospital item describe special. Lot experience rule."  
      },  
      "addressCountry": {  
        "type": "Text",  
        "value": "Section "  
      },  
      "postalCode": {  
        "type": "Text",  
        "value": "Size though picture school artist. Include might result value especially five. Wife article tend production."  
      },  
      "postOfficeBoxNumber": {  
        "type": "Text",  
        "value": "Buy how fine note actually democratic. Such family type give send. Start cause build cut suggest."  
      },  
      "streetNr": {  
        "type": "Text",  
        "value": "Resource give top movement. Southern their than last."  
      },  
      "district": {  
        "type": "Text",  
        "value": "Center ready threat chance wide. Because than shoulder near. Head wind fall pl"  
      }  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Management really"  
  },  
  "type": "Track",  
  "IdPhoneErtmsRadioBlockCenter": {  
    "type": "Text",  
    "value": "Become name off project born far significant. Teacher water become big."  
  },  
  "accelerationLevelCrossing": {  
    "type": "Text",  
    "value": "Today wait agree car build phone local."  
  },  
  "additionalBrakingInformationDocument": {  
    "type": "Text",  
    "value": "Shake himself their lot. Home show two guess society find assume. Sign hand price apply likely art arrive."  
  },  
  "atoErrorCorrectionsOnboard": {  
    "type": "Text",  
    "value": "Green writer religious even. Million up tax city everyone why strong comp"  
  },  
  "automaticDroppingDeviceRequired": {  
    "type": "Boolean",  
    "value": false  
  },  
  "bigMetalMass": {  
    "type": "Boolean",  
    "value": false  
  },  
  "bridge": {  
    "type": "Boolean",  
    "value": false  
  },  
  "cantDeficiency": {  
    "type": "Number",  
    "value": 864  
  },  
  "compatibilityProcedureDocument": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair."  
  },  
  "conditionsSwitchClassBSystems": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "conditionsSwitchTrainProtectionSystems": {  
    "type": "Text",  
    "value": "Trouble behavior style report size personal partner. During foot that course nothing draw."  
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
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth "  
  },  
  "demonstrationINF": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "distSignToPhaseEnd": {  
    "type": "Number",  
    "value": 864  
  },  
  "documentRestrictionPositionContactLineSeparation": {  
    "type": "Text",  
    "value": "A"  
  },  
  "documentRestrictionPowerConsumption": {  
    "type": "Text",  
    "value": "Together ra"  
  },  
  "eddyCurrentBrakingConditionsDocument": {  
    "type": "Text",  
    "value": "Trouble behavior style report size personal partner. During foot that course nothing draw."  
  },  
  "etcsErrorCorrectionsOnboard": {  
    "type": "Text",  
    "value": "Language ball floor meet usually board necessary. Natural sport music white."  
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
    "value": "First drug contain start almost wonder. Live bed serious theory type. Together t"  
  },  
  "etcsSystemFunctionalitiesNextFiveYears": {  
    "type": "Text",  
    "value": "Produce you true soldier bank party main. Friend couple administration even relate"  
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
    "value": "Paper of"  
  },  
  "gaugingTransversalDocument": {  
    "type": "Text",  
    "value": "Decision song view age international big employee. Author feeling job article level."  
  },  
  "gprsForETCS": {  
    "type": "Boolean",  
    "value": true  
  },  
  "gprsImplementationArea": {  
    "type": "Text",  
    "value": "Employee toward like total now. Whom around put suddenly garden. Bring TV program actually race."  
  },  
  "gradientProfile": {  
    "type": "Text",  
    "value": "True power home price check real leader. From animal exactly drive. Good explain grow water plant perf"  
  },  
  "gsmRAdditionalInfo": {  
    "type": "Text",  
    "value": "Stock ball organization recognize civil"  
  },  
  "gsmRNoCoverage": {  
    "type": "Boolean",  
    "value": false  
  },  
  "gsmrErrorCorrectionsOnboard": {  
    "type": "Text",  
    "value": "Traditional pag"  
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
    "value": "The everything affect American. Next water voice travel amo"  
  },  
  "hotAxleBoxDetectorLocation": {  
    "type": "Number",  
    "value": 855.9  
  },  
  "hotAxleBoxDetectorTSICompliant": {  
    "type": "Boolean",  
    "value": false  
  },  
  "instructionsSwitchRadioSystems": {  
    "type": "Text",  
    "value": "Modern power political"  
  },  
  "isQuietRoute": {  
    "type": "Boolean",  
    "value": false  
  },  
  "linesideDistanceIndicationFrequency": {  
    "type": "Number",  
    "value": 864  
  },  
  "localRulesOrRestrictions": {  
    "type": "Boolean",  
    "value": false  
  },  
  "localRulesOrRestrictionsDoc": {  
    "type": "Text",  
    "value": "Else memory if. Whose group through "  
  },  
  "mNvderun": {  
    "type": "Boolean",  
    "value": true  
  },  
  "magneticBrakingConditionsDocument": {  
    "type": "Text",  
    "value": "Role together range line. Government first policy daughter."  
  },  
  "maximumAltitude": {  
    "type": "Number",  
    "value": 468.7  
  },  
  "maximumBrakingDistance": {  
    "type": "Number",  
    "value": 864  
  },  
  "maximumContactWireHeight": {  
    "type": "Number",  
    "value": 249.2  
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
    "value": 150.8  
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
    "value": 636.8  
  },  
  "minFlangeThickness": {  
    "type": "Number",  
    "value": 42.8  
  },  
  "minRimWidth": {  
    "type": "Number",  
    "value": 903.6  
  },  
  "minWheelDiameter": {  
    "type": "Number",  
    "value": 864  
  },  
  "minimumContactWireHeight": {  
    "type": "Number",  
    "value": 950.2  
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
    "value": "Else memory if. Whose group through despite cause. Sense peace economy trave"  
  },  
  "nationalValuesBrakeModel": {  
    "type": "Text",  
    "value": "Financial role together range. Nice government first policy daughter need kind. Employee source nature add rest human statio"  
  },  
  "permitUseReflectivePlates": {  
    "type": "Boolean",  
    "value": true  
  },  
  "permittedContactForce": {  
    "type": "Text",  
    "value": "Language ball floor meet usually board necessary. Natural"  
  },  
  "phaseInfo": {  
    "type": "Text",  
    "value": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type successful together. Raise study modern miss dog Democrat quickly."  
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
  "raisedPantographsDistanceAndSpeed": {  
    "type": "Text",  
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. W"  
  },  
  "redLightsRequired": {  
    "type": "Boolean",  
    "value": true  
  },  
  "specificInformation": {  
    "type": "Text",  
    "value": "Line beyon"  
  },  
  "structureCheckLocation": {  
    "type": "Number",  
    "value": 636.5  
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
    "value": "Sure allow together find pass under. Language Republican strategy really office program us. Shoulder weight fly participant from campaign avoid."  
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
    "value": "American whole magazine truth stop whose. On traditional measure example sense"  
  },  
  "tiltingSupported": {  
    "type": "Boolean",  
    "value": true  
  },  
  "trackId": {  
    "type": "Text",  
    "value": "Line beyond its particularly"  
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
    "value": "American whole magazine truth stop whose. On traditional measure example sense peace. Would"  
  },  
  "vehiclesCompatibleTrafficLoad": {  
    "type": "Text",  
    "value": "Together range line beyond. First policy daughter need kind miss."  
  },  
  "verificationCCS": {  
    "type": "Text",  
    "value": "Trouble behavior style report size pe"  
  },  
  "verificationENE": {  
    "type": "Text",  
    "value": "Language ball floor meet usually board necessary. Natural sport music white."  
  },  
  "verificationINF": {  
    "type": "Text",  
    "value": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type succes"  
  },  
  "TSIMagneticFields": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:TSIMagneticFields:TDPS:69477515"  
  },  
  "TSITractionHarmonics": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:TSITractionHarmonics:ZFKN:53304135"  
  },  
  "atoCommunicationSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:atoCommunicationSystem:VCAD:01230989"  
  },  
  "atoGradeAutomation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:atoGradeAutomation:BTAG:39916151"  
  },  
  "atoSystemVersion": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:atoSystemVersion:TDIC:21730086"  
  },  
  "cantDeficiencyBasicSSP": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:cantDeficiencyBasicSSP:OBTD:31456208"  
  },  
  "conditionsUseReflectivePlates": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:conditionsUseReflectivePlates:YBZV:63457923"  
  },  
  "contactLineSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:contactLineSystem:VFAP:22584197"  
  },  
  "contactStripMaterial": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:contactStripMaterial:RWAO:69845642"  
  },  
  "dataRadioCompatible": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:dataRadioCompatible:LTJV:15084237"  
  },  
  "eddyCurrentBraking": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:eddyCurrentBraking:ATGW:59924661"  
  },  
  "etcsDegradedSituation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:etcsDegradedSituation:BMWS:52337696"  
  },  
  "etcsInfill": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:etcsInfill:QPRT:60271427"  
  },  
  "etcsLevel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:etcsLevel:GRUC:00754706"  
  },  
  "etcsMVersion": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:etcsMVersion:WYAV:20665030"  
  },  
  "etcsSystemCompatibility": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:etcsSystemCompatibility:IWFD:89131934"  
  },  
  "etcsTransmittedTrackConditions": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:etcsTransmittedTrackConditions:EUQU:76104714"  
  },  
  "freightCorridor": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:freightCorridor:VIRK:51240003"  
  },  
  "gaugingProfile": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:gaugingProfile:RFGM:59097765"  
  },  
  "gsmRActiveMobiles": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:gsmRActiveMobiles:ZLWC:94022455"  
  },  
  "gsmROptionalFunctions": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:gsmROptionalFunctions:JLMR:59004229"  
  },  
  "gsmRVersion": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:gsmRVersion:QXCJ:24173042"  
  },  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:gsmrConstraintsOperateOnlyInCircuitSwitch:PKZZ:65461187"  
  },  
  "gsmrNetworkCoverage": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:gsmrNetworkCoverage:KXVE:51717604"  
  },  
  "hotAxleBoxDetectorDirection": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:hotAxleBoxDetectorDirection:BMAD:29611133"  
  },  
  "legacyRadioSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:legacyRadioSystem:NCLH:68847793"  
  },  
  "lineCategory": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:lineCategory:WAQO:49263511"  
  },  
  "linesideDistanceIndicationAppearance": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:linesideDistanceIndicationAppearance:TEDG:31764303"  
  },  
  "linesideDistanceIndicationPositioning": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:linesideDistanceIndicationPositioning:ESMU:76582197"  
  },  
  "loadCapability": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:loadCapability:THAK:68757738"  
  },  
  "mNvcontact": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:mNvcontact:MSJW:55082492"  
  },  
  "magneticBraking": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:magneticBraking:BJAY:71180132"  
  },  
  "osmClass": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:osmClass:QQBS:75227586"  
  },  
  "otherCantDeficiencyBasicSSP": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:otherCantDeficiencyBasicSSP:TNPZ:18916348"  
  },  
  "otherPantographHead": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:otherPantographHead:QSIK:69930024"  
  },  
  "otherTrainProtection": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:otherTrainProtection:FUEH:17446660"  
  },  
  "passesThroughTunnel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:passesThroughTunnel:TWCV:45007627"  
  },  
  "platform": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:platform:BDPY:25609767"  
  },  
  "profileNumberSemiTrailers": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:profileNumberSemiTrailers:WRUL:20099251"  
  },  
  "profileNumberSwapBodies": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:profileNumberSwapBodies:UKUD:36710979"  
  },  
  "protectionLegacySystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:protectionLegacySystem:BZMO:94264183"  
  },  
  "qNvdriverAdhes": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:qNvdriverAdhes:IAQV:53751007"  
  },  
  "qNvemrrls": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:qNvemrrls:QJDE:99331886"  
  },  
  "railInclination": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:railInclination:NYEX:69611611"  
  },  
  "reasonsEtcsRadioBlockCenterReject": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:reasonsEtcsRadioBlockCenterReject:CLCD:07660754"  
  },  
  "safeConsistLengthInformationNecessary": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:safeConsistLengthInformationNecessary:CTEG:50552035"  
  },  
  "standardCombinedTransporRollerUnits": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:standardCombinedTransporRollerUnits:HEFO:03104509"  
  },  
  "standardCombinedTransportContainers": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:standardCombinedTransportContainers:KPJJ:17542035"  
  },  
  "temperatureRange": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:temperatureRange:JFME:85291189"  
  },  
  "tenClassification": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:tenClassification:LNVB:23583324"  
  },  
  "trackDirection": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:trackDirection:JRNX:29061126"  
  },  
  "trackLoadCapability": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:trackLoadCapability:ULUQ:29645137"  
  },  
  "trackPhaseInfo": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:trackPhaseInfo:LJPC:06606573"  
  },  
  "trackRaisedPantographsDistanceAndSpeed": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:trackRaisedPantographsDistanceAndSpeed:MFYN:21418927"  
  },  
  "trackSystemSeparationInfo": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:trackSystemSeparationInfo:OUUC:62375825"  
  },  
  "trainDetectionSystem": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:trainDetectionSystem:GJDY:73407970"  
  },  
  "tsiPantographHead": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:tsiPantographHead:YHRY:48926717"  
  },  
  "voiceRadioCompatible": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:voiceRadioCompatible:MQSW:64014004"  
  },  
  "wheelSetGauge": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Track:wheelSetGauge:CBCZ:67145439"  
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
#### NGSI-LD キー値の追跡 例  
以下はJSON-LD形式のTrackをkey-valuesとして返す例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Track:id:OOXM:87352290",  
  "dateCreated": "1999-12-30T09:02:54Z",  
  "dateModified": "2011-07-03T23:49:28Z",  
  "source": "Particularly hit determine. Three north girl table save adult use.",  
  "name": "Risk fall allow table mother soon parent. Cost sure difficult. Executive traditional response wish identify onto.",  
  "alternateName": "Message to pick partner nothing. Five short better assume. Air she help land.",  
  "description": "Loss so own entire teach. Mrs anyone true small century nor reveal.",  
  "dataProvider": "Natural cultural toward office. Hour where job pretty her.",  
  "owner": [  
    "urn:ngsi-ld:Track:items:IPKE:18505641",  
    "urn:ngsi-ld:Track:items:LAWY:56608364"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:Track:items:BKZL:67048585"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      61.970078,  
      -74.303326  
    ]  
  },  
  "address": {  
    "streetAddress": "Interview today ago. Eight together class financial former forward under. Hope no window fall discuss we foreign glass.",  
    "addressLocality": "Resource respond arrive remain use most. Process ",  
    "addressRegion": "Job start fish church. Or however baby possible front positive what. Writer last hospital item describe special. Lot experience rule.",  
    "addressCountry": "Section ",  
    "postalCode": "Size though picture school artist. Include might result value especially five. Wife article tend production.",  
    "postOfficeBoxNumber": "Buy how fine note actually democratic. Such family type give send. Start cause build cut suggest.",  
    "streetNr": "Resource give top movement. Southern their than last.",  
    "district": "Center ready threat chance wide. Because than shoulder near. Head wind fall pl"  
  },  
  "areaServed": "Management really",  
  "type": "Track",  
  "IdPhoneErtmsRadioBlockCenter": "Become name off project born far significant. Teacher water become big.",  
  "accelerationLevelCrossing": "Today wait agree car build phone local.",  
  "additionalBrakingInformationDocument": "Shake himself their lot. Home show two guess society find assume. Sign hand price apply likely art arrive.",  
  "atoErrorCorrectionsOnboard": "Green writer religious even. Million up tax city everyone why strong comp",  
  "automaticDroppingDeviceRequired": false,  
  "bigMetalMass": false,  
  "bridge": false,  
  "cantDeficiency": 864,  
  "compatibilityProcedureDocument": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth relate own chair.",  
  "conditionsSwitchClassBSystems": "Together range line beyond. First policy daughter need kind miss.",  
  "conditionsSwitchTrainProtectionSystems": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "contactStripMaterialMetallicContent": 864,  
  "dNvovtrp": 864,  
  "dNvpotrp": 864,  
  "dNvroll": 864,  
  "demonstrationENE": "American whole magazine truth stop whose. On traditional measure example sense peace. Would mouth ",  
  "demonstrationINF": "Together range line beyond. First policy daughter need kind miss.",  
  "distSignToPhaseEnd": 864,  
  "documentRestrictionPositionContactLineSeparation": "A",  
  "documentRestrictionPowerConsumption": "Together ra",  
  "eddyCurrentBrakingConditionsDocument": "Trouble behavior style report size personal partner. During foot that course nothing draw.",  
  "etcsErrorCorrectionsOnboard": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "etcsImplementsLevelCrossingProcedure": false,  
  "etcsInfillLineAccess": false,  
  "etcsNationalPacket44": true,  
  "etcsOptionalFunctions": "First drug contain start almost wonder. Live bed serious theory type. Together t",  
  "etcsSystemFunctionalitiesNextFiveYears": "Produce you true soldier bank party main. Friend couple administration even relate",  
  "etcsTransmitsTrackConditions": true,  
  "flangeLubeForbidden": true,  
  "gaugingCheckLocation": "Paper of",  
  "gaugingTransversalDocument": "Decision song view age international big employee. Author feeling job article level.",  
  "gprsForETCS": true,  
  "gprsImplementationArea": "Employee toward like total now. Whom around put suddenly garden. Bring TV program actually race.",  
  "gradientProfile": "True power home price check real leader. From animal exactly drive. Good explain grow water plant perf",  
  "gsmRAdditionalInfo": "Stock ball organization recognize civil",  
  "gsmRNoCoverage": false,  
  "gsmrErrorCorrectionsOnboard": "Traditional pag",  
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
  "hotAxleBoxDetectorIdentification": "The everything affect American. Next water voice travel amo",  
  "hotAxleBoxDetectorLocation": 855.9,  
  "hotAxleBoxDetectorTSICompliant": false,  
  "instructionsSwitchRadioSystems": "Modern power political",  
  "isQuietRoute": false,  
  "linesideDistanceIndicationFrequency": 864,  
  "localRulesOrRestrictions": false,  
  "localRulesOrRestrictionsDoc": "Else memory if. Whose group through ",  
  "mNvderun": true,  
  "magneticBrakingConditionsDocument": "Role together range line. Government first policy daughter.",  
  "maximumAltitude": 468.7,  
  "maximumBrakingDistance": 864,  
  "maximumContactWireHeight": 249.2,  
  "maximumPermittedSpeed": 864,  
  "maximumTemperature": 864,  
  "maximumTrainDeceleration": 150.8,  
  "minDistConsecutiveAxles": 864,  
  "minDistFirstLastAxle": 864,  
  "minFlangeHeight": 636.8,  
  "minFlangeThickness": 42.8,  
  "minRimWidth": 903.6,  
  "minWheelDiameter": 864,  
  "minimumContactWireHeight": 950.2,  
  "minimumHorizontalRadius": 864,  
  "minimumTemperature": 864,  
  "minimumWheelDiameter": 864,  
  "multipleTrainProtectionRequired": false,  
  "nationalLoadCapability": "Else memory if. Whose group through despite cause. Sense peace economy trave",  
  "nationalValuesBrakeModel": "Financial role together range. Nice government first policy daughter need kind. Employee source nature add rest human statio",  
  "permitUseReflectivePlates": true,  
  "permittedContactForce": "Language ball floor meet usually board necessary. Natural",  
  "phaseInfo": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type successful together. Raise study modern miss dog Democrat quickly.",  
  "phaseSeparation": false,  
  "publicNetworkRoaming": false,  
  "publicNetworkRoamingDetails": "Produce you true soldier bank party main. Friend couple administration even relate head color international. Beyond chair recently and.",  
  "qNvsbtsmperm": true,  
  "radioNetworkId": 864,  
  "raisedPantographsDistanceAndSpeed": "American whole magazine truth stop whose. On traditional measure example sense peace. W",  
  "redLightsRequired": true,  
  "specificInformation": "Line beyon",  
  "structureCheckLocation": 636.5,  
  "switchProtectControlWarning": true,  
  "switchRadioSystem": true,  
  "systemSeparationInfo": "Sure allow together find pass under. Language Republican strategy really office program us. Shoulder weight fly participant from campaign avoid.",  
  "tNvcontact": 864,  
  "tNvovtrp": 864,  
  "tenGISId": "American whole magazine truth stop whose. On traditional measure example sense",  
  "tiltingSupported": true,  
  "trackId": "Line beyond its particularly",  
  "trainIntegrityOnBoardRequired": true,  
  "tsiSwitchCrossing": false,  
  "usesGroup555": false,  
  "vNvallowovtrp": 864,  
  "vNvsupovtrp": 864,  
  "vehicleTypesCompatibleTrafficLoad": "American whole magazine truth stop whose. On traditional measure example sense peace. Would",  
  "vehiclesCompatibleTrafficLoad": "Together range line beyond. First policy daughter need kind miss.",  
  "verificationCCS": "Trouble behavior style report size pe",  
  "verificationENE": "Language ball floor meet usually board necessary. Natural sport music white.",  
  "verificationINF": "Onto knowledge other his offer face country. Almost wonder employee attorney. Theory type succes",  
  "TSIMagneticFields": "urn:ngsi-ld:Track:TSIMagneticFields:TDPS:69477515",  
  "TSITractionHarmonics": "urn:ngsi-ld:Track:TSITractionHarmonics:ZFKN:53304135",  
  "atoCommunicationSystem": "urn:ngsi-ld:Track:atoCommunicationSystem:VCAD:01230989",  
  "atoGradeAutomation": "urn:ngsi-ld:Track:atoGradeAutomation:BTAG:39916151",  
  "atoSystemVersion": "urn:ngsi-ld:Track:atoSystemVersion:TDIC:21730086",  
  "cantDeficiencyBasicSSP": "urn:ngsi-ld:Track:cantDeficiencyBasicSSP:OBTD:31456208",  
  "conditionsUseReflectivePlates": "urn:ngsi-ld:Track:conditionsUseReflectivePlates:YBZV:63457923",  
  "contactLineSystem": "urn:ngsi-ld:Track:contactLineSystem:VFAP:22584197",  
  "contactStripMaterial": "urn:ngsi-ld:Track:contactStripMaterial:RWAO:69845642",  
  "dataRadioCompatible": "urn:ngsi-ld:Track:dataRadioCompatible:LTJV:15084237",  
  "eddyCurrentBraking": "urn:ngsi-ld:Track:eddyCurrentBraking:ATGW:59924661",  
  "etcsDegradedSituation": "urn:ngsi-ld:Track:etcsDegradedSituation:BMWS:52337696",  
  "etcsInfill": "urn:ngsi-ld:Track:etcsInfill:QPRT:60271427",  
  "etcsLevel": "urn:ngsi-ld:Track:etcsLevel:GRUC:00754706",  
  "etcsMVersion": "urn:ngsi-ld:Track:etcsMVersion:WYAV:20665030",  
  "etcsSystemCompatibility": "urn:ngsi-ld:Track:etcsSystemCompatibility:IWFD:89131934",  
  "etcsTransmittedTrackConditions": "urn:ngsi-ld:Track:etcsTransmittedTrackConditions:EUQU:76104714",  
  "freightCorridor": "urn:ngsi-ld:Track:freightCorridor:VIRK:51240003",  
  "gaugingProfile": "urn:ngsi-ld:Track:gaugingProfile:RFGM:59097765",  
  "gsmRActiveMobiles": "urn:ngsi-ld:Track:gsmRActiveMobiles:ZLWC:94022455",  
  "gsmROptionalFunctions": "urn:ngsi-ld:Track:gsmROptionalFunctions:JLMR:59004229",  
  "gsmRVersion": "urn:ngsi-ld:Track:gsmRVersion:QXCJ:24173042",  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": "urn:ngsi-ld:Track:gsmrConstraintsOperateOnlyInCircuitSwitch:PKZZ:65461187",  
  "gsmrNetworkCoverage": "urn:ngsi-ld:Track:gsmrNetworkCoverage:KXVE:51717604",  
  "hotAxleBoxDetectorDirection": "urn:ngsi-ld:Track:hotAxleBoxDetectorDirection:BMAD:29611133",  
  "legacyRadioSystem": "urn:ngsi-ld:Track:legacyRadioSystem:NCLH:68847793",  
  "lineCategory": "urn:ngsi-ld:Track:lineCategory:WAQO:49263511",  
  "linesideDistanceIndicationAppearance": "urn:ngsi-ld:Track:linesideDistanceIndicationAppearance:TEDG:31764303",  
  "linesideDistanceIndicationPositioning": "urn:ngsi-ld:Track:linesideDistanceIndicationPositioning:ESMU:76582197",  
  "loadCapability": "urn:ngsi-ld:Track:loadCapability:THAK:68757738",  
  "mNvcontact": "urn:ngsi-ld:Track:mNvcontact:MSJW:55082492",  
  "magneticBraking": "urn:ngsi-ld:Track:magneticBraking:BJAY:71180132",  
  "osmClass": "urn:ngsi-ld:Track:osmClass:QQBS:75227586",  
  "otherCantDeficiencyBasicSSP": "urn:ngsi-ld:Track:otherCantDeficiencyBasicSSP:TNPZ:18916348",  
  "otherPantographHead": "urn:ngsi-ld:Track:otherPantographHead:QSIK:69930024",  
  "otherTrainProtection": "urn:ngsi-ld:Track:otherTrainProtection:FUEH:17446660",  
  "passesThroughTunnel": "urn:ngsi-ld:Track:passesThroughTunnel:TWCV:45007627",  
  "platform": "urn:ngsi-ld:Track:platform:BDPY:25609767",  
  "profileNumberSemiTrailers": "urn:ngsi-ld:Track:profileNumberSemiTrailers:WRUL:20099251",  
  "profileNumberSwapBodies": "urn:ngsi-ld:Track:profileNumberSwapBodies:UKUD:36710979",  
  "protectionLegacySystem": "urn:ngsi-ld:Track:protectionLegacySystem:BZMO:94264183",  
  "qNvdriverAdhes": "urn:ngsi-ld:Track:qNvdriverAdhes:IAQV:53751007",  
  "qNvemrrls": "urn:ngsi-ld:Track:qNvemrrls:QJDE:99331886",  
  "railInclination": "urn:ngsi-ld:Track:railInclination:NYEX:69611611",  
  "reasonsEtcsRadioBlockCenterReject": "urn:ngsi-ld:Track:reasonsEtcsRadioBlockCenterReject:CLCD:07660754",  
  "safeConsistLengthInformationNecessary": "urn:ngsi-ld:Track:safeConsistLengthInformationNecessary:CTEG:50552035",  
  "standardCombinedTransporRollerUnits": "urn:ngsi-ld:Track:standardCombinedTransporRollerUnits:HEFO:03104509",  
  "standardCombinedTransportContainers": "urn:ngsi-ld:Track:standardCombinedTransportContainers:KPJJ:17542035",  
  "temperatureRange": "urn:ngsi-ld:Track:temperatureRange:JFME:85291189",  
  "tenClassification": "urn:ngsi-ld:Track:tenClassification:LNVB:23583324",  
  "trackDirection": "urn:ngsi-ld:Track:trackDirection:JRNX:29061126",  
  "trackLoadCapability": "urn:ngsi-ld:Track:trackLoadCapability:ULUQ:29645137",  
  "trackPhaseInfo": "urn:ngsi-ld:Track:trackPhaseInfo:LJPC:06606573",  
  "trackRaisedPantographsDistanceAndSpeed": "urn:ngsi-ld:Track:trackRaisedPantographsDistanceAndSpeed:MFYN:21418927",  
  "trackSystemSeparationInfo": "urn:ngsi-ld:Track:trackSystemSeparationInfo:OUUC:62375825",  
  "trainDetectionSystem": "urn:ngsi-ld:Track:trainDetectionSystem:GJDY:73407970",  
  "tsiPantographHead": "urn:ngsi-ld:Track:tsiPantographHead:YHRY:48926717",  
  "voiceRadioCompatible": "urn:ngsi-ld:Track:voiceRadioCompatible:MQSW:64014004",  
  "wheelSetGauge": "urn:ngsi-ld:Track:wheelSetGauge:CBCZ:67145439",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### トラック NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のTrackの例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Track:id:YMIK:19710861",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1983-10-08T09:10:35Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2007-09-24T21:04:11Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "Indeed task discover hand. Responsibility first husband still. Turn chance deep wait contain."  
  },  
  "name": {  
    "type": "Property",  
    "value": "Maybe much relationshi"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Agree rock network artist card house. Main four stay relationship rise produce. Present foot paper."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Evening fine fill always teach card once. Put need door operation identify."  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Always maybe language begin camera bad. Product information each happy someone environment. Key star woman rock foreign fire."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Track:items:NRYA:75191355",  
      "urn:ngsi-ld:Track:items:LEIP:84892904"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:Track:items:MGJZ:05541161"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -57.44138,  
        125.273819  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Guy conference civil economy yes. Program this huge must. Time party firm argue design specific similar.",  
      "addressLocality": "Better future write. Someone measure general explain parent field.",  
      "addressRegion": "Congress those of all shoulder name. Perhaps entire pric",  
      "addressCountry": "",  
      "postalCode": "Pattern imagine reality management t",  
      "postOfficeBoxNumber": "Firm around citizen. Situation enjoy end size study computer enjoy. Site into store.",  
      "streetNr": "Against serve store. If affect think improve surface exist. Down blood former hand.",  
      "district": "Run lay poor next budget day. Suggest offer easy community hour high. Project seem m"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Certain forward fly billion between service identify. Mr relate arrive"  
  },  
  "type": "Track",  
  "IdPhoneErtmsRadioBlockCenter": {  
    "type": "Property",  
    "value": "Town myself religious would lose. Statement first ball experience threat. Oil position rule."  
  },  
  "accelerationLevelCrossing": {  
    "type": "Property",  
    "value": "Us day century either. Job just either group message left born. Idea wear produce two."  
  },  
  "additionalBrakingInformationDocument": {  
    "type": "Property",  
    "value": "Even product let cell last rule. Cultural require specific hold see police. Smile st"  
  },  
  "atoErrorCorrectionsOnboard": {  
    "type": "Property",  
    "value": "Brother style drug place company PM. New past Democrat common piece reveal. Loss bed collection theory week netw"  
  },  
  "automaticDroppingDeviceRequired": {  
    "type": "Property",  
    "value": false  
  },  
  "bigMetalMass": {  
    "type": "Property",  
    "value": true  
  },  
  "bridge": {  
    "type": "Property",  
    "value": false  
  },  
  "cantDeficiency": {  
    "type": "Property",  
    "value": 556  
  },  
  "compatibilityProcedureDocument": {  
    "type": "Property",  
    "value": "Kind give able story way. Arm under step board student opportunity. Say morning position see not appear measure. Onto never guy."  
  },  
  "conditionsSwitchClassBSystems": {  
    "type": "Property",  
    "value": "Join deep surface street you sing field. Nice behavior onto."  
  },  
  "conditionsSwitchTrainProtectionSystems": {  
    "type": "Property",  
    "value": "Deal per change central expert. Develop blood minute report only personal."  
  },  
  "contactStripMaterialMetallicContent": {  
    "type": "Property",  
    "value": 660  
  },  
  "dNvovtrp": {  
    "type": "Property",  
    "value": 591  
  },  
  "dNvpotrp": {  
    "type": "Property",  
    "value": 620  
  },  
  "dNvroll": {  
    "type": "Property",  
    "value": 753  
  },  
  "demonstrationENE": {  
    "type": "Property",  
    "value": "Fast fear risk fear wife run. Information"  
  },  
  "demonstrationINF": {  
    "type": "Property",  
    "value": "Face tough job plant window. Activity amount world wind today read cell. Meeting its cause respond."  
  },  
  "distSignToPhaseEnd": {  
    "type": "Property",  
    "value": 544  
  },  
  "documentRestrictionPositionContactLineSeparation": {  
    "type": "Property",  
    "value": "I fish message note world. Actually space chair common simple."  
  },  
  "documentRestrictionPowerConsumption": {  
    "type": "Property",  
    "value": "As bag despite seem almost someone play."  
  },  
  "eddyCurrentBrakingConditionsDocument": {  
    "type": "Property",  
    "value": "Fight continue effort. Hold note find project great low."  
  },  
  "etcsErrorCorrectionsOnboard": {  
    "type": "Property",  
    "value": "Understand story will glass among owner. Military scene age senior film specific rema"  
  },  
  "etcsImplementsLevelCrossingProcedure": {  
    "type": "Property",  
    "value": true  
  },  
  "etcsInfillLineAccess": {  
    "type": "Property",  
    "value": true  
  },  
  "etcsNationalPacket44": {  
    "type": "Property",  
    "value": true  
  },  
  "etcsOptionalFunctions": {  
    "type": "Property",  
    "value": "It glass room street value. Expert next age language lead fund moment. It continue reach. Represent maj"  
  },  
  "etcsSystemFunctionalitiesNextFiveYears": {  
    "type": "Property",  
    "value": "Smile this phone walk off often try. Act everybody owner opportunity until television."  
  },  
  "etcsTransmitsTrackConditions": {  
    "type": "Property",  
    "value": false  
  },  
  "flangeLubeForbidden": {  
    "type": "Property",  
    "value": true  
  },  
  "gaugingCheckLocation": {  
    "type": "Property",  
    "value": "Network trial sound painting culture better. Many do air d"  
  },  
  "gaugingTransversalDocument": {  
    "type": "Property",  
    "value": "Myself black bill professional population debate tough. "  
  },  
  "gprsForETCS": {  
    "type": "Property",  
    "value": true  
  },  
  "gprsImplementationArea": {  
    "type": "Property",  
    "value": "Instead week mind. Clear recent series second."  
  },  
  "gradientProfile": {  
    "type": "Property",  
    "value": "Ball assume especially attack save always news. Participant everybody upon hope management son. Miss according anything performance"  
  },  
  "gsmRAdditionalInfo": {  
    "type": "Property",  
    "value": "Clearly southern meeting. Laugh home meeting gas heavy really."  
  },  
  "gsmRNoCoverage": {  
    "type": "Property",  
    "value": true  
  },  
  "gsmrErrorCorrectionsOnboard": {  
    "type": "Property",  
    "value": "Local position order defense project. Group tell box standard it."  
  },  
  "gsmrForcedDeregistrationFunctionalNumber": {  
    "type": "Property",  
    "value": true  
  },  
  "hasAdditionalBrakingInformation": {  
    "type": "Property",  
    "value": false  
  },  
  "hasBallast": {  
    "type": "Property",  
    "value": true  
  },  
  "hasETCSRestrictionsConditions": {  
    "type": "Property",  
    "value": false  
  },  
  "hasHotAxleBoxDetector": {  
    "type": "Property",  
    "value": true  
  },  
  "hasLevelCrossings": {  
    "type": "Property",  
    "value": true  
  },  
  "hasOtherTrainProtection": {  
    "type": "Property",  
    "value": true  
  },  
  "hasSevereWeatherConditions": {  
    "type": "Property",  
    "value": true  
  },  
  "hasSystemSeparation": {  
    "type": "Property",  
    "value": true  
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
    "value": "Woman interest off low. Budget officer situation notice throw culture score."  
  },  
  "hotAxleBoxDetectorIdentification": {  
    "type": "Property",  
    "value": "Bring police system approach center too. News amount w"  
  },  
  "hotAxleBoxDetectorLocation": {  
    "type": "Property",  
    "value": 968.7  
  },  
  "hotAxleBoxDetectorTSICompliant": {  
    "type": "Property",  
    "value": false  
  },  
  "instructionsSwitchRadioSystems": {  
    "type": "Property",  
    "value": "Drive hundred result take itself we time. Very whom fund course."  
  },  
  "isQuietRoute": {  
    "type": "Property",  
    "value": true  
  },  
  "linesideDistanceIndicationFrequency": {  
    "type": "Property",  
    "value": 230  
  },  
  "localRulesOrRestrictions": {  
    "type": "Property",  
    "value": false  
  },  
  "localRulesOrRestrictionsDoc": {  
    "type": "Property",  
    "value": "Similar past into. Agreement budget gr"  
  },  
  "mNvderun": {  
    "type": "Property",  
    "value": false  
  },  
  "magneticBrakingConditionsDocument": {  
    "type": "Property",  
    "value": "Themselves because they contain yet house. Wall to former"  
  },  
  "maximumAltitude": {  
    "type": "Property",  
    "value": 424.1  
  },  
  "maximumBrakingDistance": {  
    "type": "Property",  
    "value": 391  
  },  
  "maximumContactWireHeight": {  
    "type": "Property",  
    "value": 131.9  
  },  
  "maximumPermittedSpeed": {  
    "type": "Property",  
    "value": 54  
  },  
  "maximumTemperature": {  
    "type": "Property",  
    "value": 638  
  },  
  "maximumTrainDeceleration": {  
    "type": "Property",  
    "value": 65.0  
  },  
  "minDistConsecutiveAxles": {  
    "type": "Property",  
    "value": 899  
  },  
  "minDistFirstLastAxle": {  
    "type": "Property",  
    "value": 452  
  },  
  "minFlangeHeight": {  
    "type": "Property",  
    "value": 779.3  
  },  
  "minFlangeThickness": {  
    "type": "Property",  
    "value": 390.2  
  },  
  "minRimWidth": {  
    "type": "Property",  
    "value": 431.1  
  },  
  "minWheelDiameter": {  
    "type": "Property",  
    "value": 687  
  },  
  "minimumContactWireHeight": {  
    "type": "Property",  
    "value": 705.9  
  },  
  "minimumHorizontalRadius": {  
    "type": "Property",  
    "value": 666  
  },  
  "minimumTemperature": {  
    "type": "Property",  
    "value": 879  
  },  
  "minimumWheelDiameter": {  
    "type": "Property",  
    "value": 567  
  },  
  "multipleTrainProtectionRequired": {  
    "type": "Property",  
    "value": true  
  },  
  "nationalLoadCapability": {  
    "type": "Property",  
    "value": "Election everyone field have half speech recent. Gas task heavy night detail. Politics know almost home left fear."  
  },  
  "nationalValuesBrakeModel": {  
    "type": "Property",  
    "value": "Tv majorit"  
  },  
  "permitUseReflectivePlates": {  
    "type": "Property",  
    "value": false  
  },  
  "permittedContactForce": {  
    "type": "Property",  
    "value": "Popular prove consumer dream market guy performance. Give hot media wish activity treat girl. Yourself TV address ago vote sing"  
  },  
  "phaseInfo": {  
    "type": "Property",  
    "value": "Part whom teach picture give home. Either happy know answer wonder view. There learn oil ahead practice."  
  },  
  "phaseSeparation": {  
    "type": "Property",  
    "value": true  
  },  
  "publicNetworkRoaming": {  
    "type": "Property",  
    "value": false  
  },  
  "publicNetworkRoamingDetails": {  
    "type": "Property",  
    "value": "Fly street break PM. So national"  
  },  
  "qNvsbtsmperm": {  
    "type": "Property",  
    "value": false  
  },  
  "radioNetworkId": {  
    "type": "Property",  
    "value": 851  
  },  
  "raisedPantographsDistanceAndSpeed": {  
    "type": "Property",  
    "value": "But several suggest cause much bag shoulder. Meet couple lead important you. Future clear trade attention probably."  
  },  
  "redLightsRequired": {  
    "type": "Property",  
    "value": true  
  },  
  "specificInformation": {  
    "type": "Property",  
    "value": "Information risk me others ok sea. Recent travel raise medical staff evidence baby. Plant old government itself. Why any medical college whose."  
  },  
  "structureCheckLocation": {  
    "type": "Property",  
    "value": 429.9  
  },  
  "switchProtectControlWarning": {  
    "type": "Property",  
    "value": true  
  },  
  "switchRadioSystem": {  
    "type": "Property",  
    "value": false  
  },  
  "systemSeparationInfo": {  
    "type": "Property",  
    "value": "Someone public bring. Everything include us nation. Will national true color yes t"  
  },  
  "tNvcontact": {  
    "type": "Property",  
    "value": 830  
  },  
  "tNvovtrp": {  
    "type": "Property",  
    "value": 85  
  },  
  "tenGISId": {  
    "type": "Property",  
    "value": "Paper agency spring. Few back sit information exist draw identify."  
  },  
  "tiltingSupported": {  
    "type": "Property",  
    "value": true  
  },  
  "trackId": {  
    "type": "Property",  
    "value": "Tree stock shake human professional first outside. Look carry important past movie necessary figure everything. You rather doctor possible sister. Seem simple task pressure"  
  },  
  "trainIntegrityOnBoardRequired": {  
    "type": "Property",  
    "value": true  
  },  
  "tsiSwitchCrossing": {  
    "type": "Property",  
    "value": true  
  },  
  "usesGroup555": {  
    "type": "Property",  
    "value": true  
  },  
  "vNvallowovtrp": {  
    "type": "Property",  
    "value": 657  
  },  
  "vNvsupovtrp": {  
    "type": "Property",  
    "value": 936  
  },  
  "vehicleTypesCompatibleTrafficLoad": {  
    "type": "Property",  
    "value": "Live fly north pretty sea certainly training. Trouble hundred wait live open."  
  },  
  "vehiclesCompatibleTrafficLoad": {  
    "type": "Property",  
    "value": "At head help fight response rich husband body. Draw about social type. Surfac"  
  },  
  "verificationCCS": {  
    "type": "Property",  
    "value": "Me western very well. Edge discussion car body task sound. Travel seem decide contain inside down relationship professor."  
  },  
  "verificationENE": {  
    "type": "Property",  
    "value": "Enjoy take after glass. Between rea"  
  },  
  "verificationINF": {  
    "type": "Property",  
    "value": "Ability hair town effort. Develop outside agent again seek catch argue."  
  },  
  "TSIMagneticFields": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:TSIMagneticFields:OOYK:91421135"  
  },  
  "TSITractionHarmonics": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:TSITractionHarmonics:LTWL:00520154"  
  },  
  "atoCommunicationSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:atoCommunicationSystem:SJYB:48735869"  
  },  
  "atoGradeAutomation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:atoGradeAutomation:SLRC:85544407"  
  },  
  "atoSystemVersion": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:atoSystemVersion:CYRS:55134775"  
  },  
  "cantDeficiencyBasicSSP": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:cantDeficiencyBasicSSP:EHVL:93679918"  
  },  
  "conditionsUseReflectivePlates": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:conditionsUseReflectivePlates:FHYL:27007228"  
  },  
  "contactLineSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:contactLineSystem:MARF:88307190"  
  },  
  "contactStripMaterial": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:contactStripMaterial:AIHT:63698483"  
  },  
  "dataRadioCompatible": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:dataRadioCompatible:QIUU:65751465"  
  },  
  "eddyCurrentBraking": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:eddyCurrentBraking:VRSD:98231067"  
  },  
  "etcsDegradedSituation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:etcsDegradedSituation:YSMP:90403683"  
  },  
  "etcsInfill": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:etcsInfill:ERMC:18844372"  
  },  
  "etcsLevel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:etcsLevel:FHFK:37841904"  
  },  
  "etcsMVersion": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:etcsMVersion:YIZO:03842167"  
  },  
  "etcsSystemCompatibility": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:etcsSystemCompatibility:CSSH:13556650"  
  },  
  "etcsTransmittedTrackConditions": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:etcsTransmittedTrackConditions:UDJR:99717898"  
  },  
  "freightCorridor": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:freightCorridor:TGKO:22567327"  
  },  
  "gaugingProfile": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:gaugingProfile:USBY:90624372"  
  },  
  "gsmRActiveMobiles": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:gsmRActiveMobiles:UVXI:37755506"  
  },  
  "gsmROptionalFunctions": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:gsmROptionalFunctions:HUDH:30501659"  
  },  
  "gsmRVersion": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:gsmRVersion:OYAB:89561253"  
  },  
  "gsmrConstraintsOperateOnlyInCircuitSwitch": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:gsmrConstraintsOperateOnlyInCircuitSwitch:XXHU:62821232"  
  },  
  "gsmrNetworkCoverage": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:gsmrNetworkCoverage:BDOZ:37189007"  
  },  
  "hotAxleBoxDetectorDirection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:hotAxleBoxDetectorDirection:EXYN:59773905"  
  },  
  "legacyRadioSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:legacyRadioSystem:YDOJ:63240175"  
  },  
  "lineCategory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:lineCategory:HFDH:09460960"  
  },  
  "linesideDistanceIndicationAppearance": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:linesideDistanceIndicationAppearance:LAWH:90479517"  
  },  
  "linesideDistanceIndicationPositioning": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:linesideDistanceIndicationPositioning:DVZL:67395551"  
  },  
  "loadCapability": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:loadCapability:WWFO:32627285"  
  },  
  "mNvcontact": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:mNvcontact:JALR:56122084"  
  },  
  "magneticBraking": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:magneticBraking:QPFX:89274330"  
  },  
  "osmClass": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:osmClass:EVYL:67103052"  
  },  
  "otherCantDeficiencyBasicSSP": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:otherCantDeficiencyBasicSSP:XUWE:77419425"  
  },  
  "otherPantographHead": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:otherPantographHead:BCWZ:38394845"  
  },  
  "otherTrainProtection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:otherTrainProtection:KCQT:40278265"  
  },  
  "passesThroughTunnel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:passesThroughTunnel:RYPG:38053723"  
  },  
  "platform": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:platform:FHAV:37709561"  
  },  
  "profileNumberSemiTrailers": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:profileNumberSemiTrailers:KMZM:36574592"  
  },  
  "profileNumberSwapBodies": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:profileNumberSwapBodies:UUVE:36082316"  
  },  
  "protectionLegacySystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:protectionLegacySystem:WVYY:37500833"  
  },  
  "qNvdriverAdhes": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:qNvdriverAdhes:IFAT:71819772"  
  },  
  "qNvemrrls": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:qNvemrrls:BYXQ:08045038"  
  },  
  "railInclination": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:railInclination:ADZF:92982559"  
  },  
  "reasonsEtcsRadioBlockCenterReject": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:reasonsEtcsRadioBlockCenterReject:GUNC:87503017"  
  },  
  "safeConsistLengthInformationNecessary": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:safeConsistLengthInformationNecessary:USNW:64305786"  
  },  
  "standardCombinedTransporRollerUnits": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:standardCombinedTransporRollerUnits:CYJJ:16508631"  
  },  
  "standardCombinedTransportContainers": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:standardCombinedTransportContainers:PKMY:93489985"  
  },  
  "temperatureRange": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:temperatureRange:XFWH:83012413"  
  },  
  "tenClassification": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:tenClassification:CZXH:84258804"  
  },  
  "trackDirection": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:trackDirection:RJPW:74017654"  
  },  
  "trackLoadCapability": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:trackLoadCapability:BRRC:75525461"  
  },  
  "trackPhaseInfo": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:trackPhaseInfo:LSSZ:55099385"  
  },  
  "trackRaisedPantographsDistanceAndSpeed": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:trackRaisedPantographsDistanceAndSpeed:CMSB:95766165"  
  },  
  "trackSystemSeparationInfo": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:trackSystemSeparationInfo:NVPV:50578868"  
  },  
  "trainDetectionSystem": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:trainDetectionSystem:GUAJ:85296846"  
  },  
  "tsiPantographHead": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:tsiPantographHead:LFLG:38361605"  
  },  
  "voiceRadioCompatible": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:voiceRadioCompatible:QXQK:41864045"  
  },  
  "wheelSetGauge": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Track:wheelSetGauge:PWVQ:21449032"  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  

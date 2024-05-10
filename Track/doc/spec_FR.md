<!-- 10-Header -->
    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    

Entité : Voie    
=============
<!-- /10-Header -->
    
<!-- 15-License -->
    

[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/Track/LICENSE.md)    

[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->
    
<!-- 20-Description -->
    

Description globale : **Une voie de roulement utilisée pour la circulation des trains**.    

version : 0.0.1    
<!-- /20-Description -->
    
<!-- 30-PropertiesList -->
    

## Liste des propriétés    

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `IdPhoneErtmsRadioBlockCenter[string]`: ID et numéro de téléphone du centre de bloc radio ERTMS/ETCS  
- `TSIMagneticFields[uri]`: Existence et conformité aux STI des règles relatives aux champs magnétiques émis par un véhicule  
- `TSITractionHarmonics[uri]`: Existence et conformité aux STI des limites des harmoniques dans le courant de traction des véhicules  
- `accelerationLevelCrossing[string]`: Accélération autorisée au passage à niveau  
- `additionalBrakingInformationDocument[string]`: Documents disponibles auprès de l'IM concernant les performances de freinage  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique      
- `alternateName[string]`: Un nom alternatif pour ce poste  
- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)
- `atoCommunicationSystem[uri]`: Système de communication ATO  
- `atoErrorCorrectionsOnboard[string]`: Corrections d'erreurs ATO requises pour le système de bord  
- `atoGradeAutomation[uri]`: ATO Grade d'automatisation  
- `atoSystemVersion[uri]`: Version du système ATO  
- `automaticDroppingDeviceRequired[boolean]`: Dispositif de chute automatique requis  
- `bigMetalMass[boolean]`: Grande masse métallique  
- `bridge[boolean]`: Est un pont  
- `cantDeficiency[number]`: Défaut de cant  
- `cantDeficiencyBasicSSP[uri]`: Défaut de cantonnement utilisé pour le PAS de base  
- `compatibilityProcedureDocument[string]`: Document contenant la ou les procédures de vérification de la compatibilité des routes statiques et dynamiques  
- `conditionsSwitchClassBSystems[string]`: Conditions techniques particulières requises pour passer d'un système ERTMS/ETCS à un système de classe B  
- `conditionsSwitchTrainProtectionSystems[string]`: Conditions particulières pour passer d'un système de protection, de contrôle et d'avertissement des trains de classe B à un autre  
- `conditionsUseReflectivePlates[uri]`: Conditions d'utilisation des plaques réfléchissantes  
- `contactLineSystem[uri]`: Système de ligne de contact  
- `contactStripMaterial[uri]`: Matériau autorisé pour les bandes de contact  
- `contactStripMaterialMetallicContent[number]`: Matériau de la bande de contact Contenu métallique  
- `dNvovtrp[number]`: D_NVOVTRP  
- `dNvpotrp[number]`: D_NVPOTRP  
- `dNvroll[number]`: D_NVROLL  
- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  
- `dataRadioCompatible[uri]`: Données sur la compatibilité des systèmes radio  
- `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  
- `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  
- `demonstrationENE[string]`: Déclaration de démonstration de l'IE pour la voie ferrée (ENE)  
- `demonstrationINF[string]`: Déclaration de démonstration de l'IE pour les voies et les bardages [INF].  
- `description[string]`: Une description de l'article  
- `distSignToPhaseEnd[number]`: Distance entre le panneau de signalisation et la fin de la séparation de phase  
- `documentRestrictionPositionContactLineSeparation[string]`: Document avec restriction relative à la position de l'unité (des unités) de traction multiple(s) pour respecter la séparation des lignes de contact  
- `documentRestrictionPowerConsumption[string]`: Document avec restriction relative à la consommation d'énergie d'un ou de plusieurs engins de traction électrique spécifiques  
- `eddyCurrentBraking[uri]`: Utilisation de freins à courants de Foucault  
- `eddyCurrentBrakingConditionsDocument[string]`: Document sur les conditions d'utilisation des freins à courants de Foucault  
- `etcsDegradedSituation[uri]`: Niveau ETCS pour une situation dégradée  
- `etcsErrorCorrectionsOnboard[string]`: Corrections d'erreurs ETCS requises pour le système de bord  
- `etcsImplementsLevelCrossingProcedure[boolean]`: ETCS trackside met en œuvre la procédure de passage à niveau ou une solution équivalente  
- `etcsInfill[uri]`: Remplissage ETCS installé côté ligne  
- `etcsInfillLineAccess[boolean]`: Remplissage ETCS nécessaire pour l'accès à la ligne  
- `etcsLevel[uri]`: Niveau Etcs  
- `etcsMVersion[uri]`: ETCS M_version  
- `etcsOptionalFunctions[string]`: Fonctions optionnelles de l'ETCS  
- `etcsSystemCompatibility[uri]`: Compatibilité du système ETCS  
- `etcsSystemFunctionalitiesNextFiveYears[string]`: Fonctionnalités du système ETCS version 2.2 ou 3.0 requises dans les 5 prochaines années  
- `etcsTransmitsTrackConditions[boolean]`: Le système ETCS est-il conçu pour transmettre l'état de la voie ?  
- `etcsTransmittedTrackConditions[uri]`: Conditions de suivi pouvant être transmises  
- `flangeLubeForbidden[boolean]`: Utilisation de la lubrification de la bride interdite  
- `freightCorridor[uri]`: Partie d'un corridor de fret ferroviaire  
- `gaugingCheckLocation[string]`: Localisation ferroviaire de points particuliers nécessitant des vérifications spécifiques  
- `gaugingProfile[uri]`: Jaugeage  
- `gaugingTransversalDocument[string]`: Document avec la section transversale des points particuliers nécessitant des contrôles spécifiques  
- `gprsForETCS[boolean]`: GPRS pour ETCS  
- `gradientProfile[string]`: Profil de gradient  
- `gsmRActiveMobiles[uri]`: Nombre de mobiles GSM-R actifs (EDOR) ou de sessions de communication simultanées à bord pour le niveau 2 (ou 3) de l'ETCS, nécessaires pour effectuer des transferts de centre de bloc radio sans interruption de l'exploitation.  
- `gsmRAdditionalInfo[string]`: Informations complémentaires sur les caractéristiques du réseau  
- `gsmRNoCoverage[boolean]`: Pas de couverture GSM-R  
- `gsmROptionalFunctions[uri]`: Fonctions GSM-R en option  
- `gsmRVersion[uri]`: Version GSM-R  
- `gsmrConstraintsOperateOnlyInCircuitSwitch[uri]`: Contraintes spécifiques imposées par l'opérateur du réseau GSM-R aux unités embarquées de l'ETCS ne pouvant fonctionner qu'en commutation de circuits  
- `gsmrErrorCorrectionsOnboard[string]`: Corrections d'erreurs GSM-R requises pour le système embarqué  
- `gsmrForcedDeregistrationFunctionalNumber[boolean]`: Le réseau GSM-R est configuré pour permettre le désenregistrement forcé d'un numéro fonctionnel par un autre conducteur.  
- `gsmrNetworkCoverage[uri]`: Réseaux GSM-R couverts par un accord d'itinérance  
- `hasAdditionalBrakingInformation[boolean]`: Disponibilité d'informations supplémentaires par l'IM  
- `hasBallast[boolean]`: Existence d'un lest  
- `hasETCSRestrictionsConditions[boolean]`: Existence de restrictions ou de conditions d'exploitation  
- `hasHotAxleBoxDetector[boolean]`: Existence d'un détecteur de boîtes d'essieu chaudes en bordure de voie (HABD)  
- `hasLevelCrossings[boolean]`: Existence de passages à niveau  
- `hasOtherTrainProtection[boolean]`: Existence d'autres systèmes de protection, de contrôle et d'avertissement des trains installés  
- `hasSevereWeatherConditions[boolean]`: Existence de conditions climatiques sévères  
- `hasSystemSeparation[boolean]`: Séparation des systèmes  
- `hasTSITrainDetection[boolean]`: Existence d'un système de détection des trains entièrement conforme à la STI  
- `highSpeedLoadModelCompliance[boolean]`: Conformité des structures au modèle de charge dynamique High Speed Load Model (HSLM)  
- `hotAxleBoxDetectorDirection[uri]`: Direction du détecteur de boîtes d'essieu chaudes  
- `hotAxleBoxDetectorGeneration[string]`: Génération de DBC en bord de voie  
- `hotAxleBoxDetectorIdentification[string]`: Identification des DBC en bord de voie  
- `hotAxleBoxDetectorLocation[number]`: Emplacement des DBC en bord de voie  
- `hotAxleBoxDetectorTSICompliant[boolean]`: Conformité de la STI HABD du côté de la voie ferrée  
- `id[*]`: Identifiant unique de l'entité  
- `instructionsSwitchRadioSystems[string]`: Instructions spéciales pour passer d'un système radio à l'autre  
- `isQuietRoute[boolean]`: Appartenir à un itinéraire plus calme  
- `legacyRadioSystem[uri]`: Autres systèmes radio installés (systèmes radio hérités)  
- `lineCategory[uri]`: Catégorie de ligne  
- `linesideDistanceIndicationAppearance[uri]`: Apparition de l'indication de la distance sur le côté de la ligne  
- `linesideDistanceIndicationFrequency[number]`: Fréquence d'indication de la distance en bord de ligne  
- `linesideDistanceIndicationPositioning[uri]`: Positionnement de l'indication de la distance en bord de ligne  
- `loadCapability[uri]`: Capacité de charge  
- `localRulesOrRestrictions[boolean]`: Existence de règles et de restrictions de nature strictement locale.  
- `localRulesOrRestrictionsDoc[string]`: Documents relatifs aux règles ou restrictions de nature strictement locale disponibles auprès de l'IM  
- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  
- `mNvcontact[uri]`: M_NVCONTACT  
- `mNvderun[boolean]`: M_NVDERUN  
- `magneticBraking[uri]`: Utilisation de freins magnétiques  
- `magneticBrakingConditionsDocument[string]`: Document relatif aux conditions d'utilisation des freins magnétiques  
- `maximumAltitude[number]`: Altitude maximale  
- `maximumBrakingDistance[number]`: Distance de freinage maximale demandée  
- `maximumContactWireHeight[number]`: Hauteur maximale du fil de contact  
- `maximumPermittedSpeed[number]`: Vitesse maximale autorisée  
- `maximumTemperature[number]`: Plage de température (maximale)  
- `maximumTrainDeceleration[number]`: Décélération maximale du train  
- `minDistConsecutiveAxles[number]`: Distance minimale autorisée entre deux essieux consécutifs  
- `minDistFirstLastAxle[number]`: Distance minimale autorisée entre le premier et le dernier essieu  
- `minFlangeHeight[number]`: Hauteur minimale autorisée de la bride  
- `minFlangeThickness[number]`: Épaisseur minimale autorisée de la bride  
- `minRimWidth[number]`: Largeur minimale autorisée de la jante  
- `minWheelDiameter[number]`: Diamètre minimal autorisé des roues  
- `minimumContactWireHeight[number]`: Hauteur minimale du fil de contact  
- `minimumHorizontalRadius[number]`: Rayon minimal de la courbe horizontale  
- `minimumTemperature[number]`: Plage de température (minimum)  
- `minimumWheelDiameter[number]`: Diamètre minimal des roues pour les croisements obtus fixes  
- `multipleTrainProtectionRequired[boolean]`: Nécessité de disposer de plusieurs systèmes de protection, de contrôle et d'alerte à bord des trains  
- `name[string]`: Le nom de cet élément  
- `nationalLoadCapability[string]`: Classification nationale pour la capacité de charge  
- `nationalValuesBrakeModel[string]`: Valeurs nationales utilisées pour le modèle de freinage  
- `osmClass[uri]`: Classe de cartes de rues ouvertes  
- `otherCantDeficiencyBasicSSP[uri]`: Autres catégories de trains déficients pour lesquelles l'ETCS est configuré pour fournir un SSP  
- `otherPantographHead[uri]`: Autres têtes de pantographe acceptées  
- `otherTrainProtection[uri]`: Autres systèmes de protection, de contrôle et d'avertissement des trains en cas de situation dégradée  
- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  
- `passesThroughTunnel[uri]`: Traverse le tunnel  
- `permitUseReflectivePlates[boolean]`: Autorisation d'utiliser des plaques réfléchissantes  
- `permittedContactForce[string]`: Force de contact autorisée  
- `phaseInfo[string]`: Informations sur la séparation des phases  
- `phaseSeparation[boolean]`: Séparation de phases  
- `platform[uri]`: Plate-forme  
- `profileNumberSemiTrailers[uri]`: Numéro de profil de transport combiné standard pour les semi-remorques  
- `profileNumberSwapBodies[uri]`: Numéro de profil de transport combiné standard pour les caisses mobiles  
- `protectionLegacySystem[uri]`: Système de protection des trains  
- `publicNetworkRoaming[boolean]`: GSM-R existence de l'itinérance vers les réseaux publics  
- `publicNetworkRoamingDetails[string]`: Détails du GSM-R sur l'itinérance vers les réseaux publics  
- `qNvdriverAdhes[uri]`: Q_NVDRIVER_ADHES  
- `qNvemrrls[uri]`: Q_NVEMRRLS  
- `qNvsbtsmperm[boolean]`: Q_NVSBTSMPERM  
- `radioNetworkId[number]`: ID du réseau radio  
- `railInclination[uri]`: Inclinaison du rail  
- `raisedPantographsDistanceAndSpeed[string]`: Exigences relatives au nombre de pantographes relevés et à l'espacement entre eux, à la vitesse donnée  
- `reasonsEtcsRadioBlockCenterReject[uri]`: Raisons pour lesquelles un centre de bloc radio ETCS peut refuser un train  
- `redLightsRequired[boolean]`: Feux rouges fixes requis  
- `safeConsistLengthInformationNecessary[uri]`: Informations sur la longueur de la bande de sécurité à bord nécessaires pour l'accès à la ligne et au SIL  
- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  
- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  
- `specificInformation[string]`: Informations spécifiques  
- `standardCombinedTransporRollerUnits[uri]`: Numéro du profil de transport combiné standard pour les unités à rouleaux  
- `standardCombinedTransportContainers[uri]`: Numéro de profil de transport combiné standard pour les conteneurs  
- `structureCheckLocation[number]`: Localisation ferroviaire des structures nécessitant des contrôles spécifiques  
- `switchProtectControlWarning[boolean]`: Existence d'une commutation entre les différents systèmes de protection, de contrôle et d'alerte en cours de fonctionnement  
- `switchRadioSystem[boolean]`: Existence d'une commutation entre différents systèmes radio  
- `systemSeparationInfo[string]`: Informations sur la séparation des systèmes  
- `tNvcontact[number]`: T_NVCONTACT  
- `tNvovtrp[number]`: T_NVOVTRP  
- `temperatureRange[uri]`: Plage de température  
- `tenClassification[uri]`: Classification TEN (de la voie, du quai, de la voie d'évitement)  
- `tenGISId[string]`: Identité du SIG TEN  
- `tiltingSupported[boolean]`: Indication si les fonctions de basculement sont prises en charge par l'ETCS  
- `trackDirection[uri]`: Sens de marche normal  
- `trackId[string]`: Identification de la voie  
- `trackLoadCapability[uri]`: Capacité de charge des chenilles  
- `trackPhaseInfo[uri]`: Informations sur les phases de la voie  
- `trackRaisedPantographsDistanceAndSpeed[uri]`: Poursuivre la distance et la vitesse du pantographe relevé  
- `trackSystemSeparationInfo[uri]`: Informations sur la séparation des voies  
- `trainDetectionSystem[uri]`: Système de détection des trains  
- `trainIntegrityOnBoardRequired[boolean]`: Confirmation de l'intégrité du train à bord (et non par le conducteur) nécessaire pour l'accès à la ligne  
- `tsiPantographHead[uri]`: Têtes de pantographe acceptées et conformes à la STI  
- `tsiSwitchCrossing[boolean]`: Conformité aux STI des valeurs en service pour les appareils de voie  
- `type[string]`: Type de données NGSI. Il doit s'agir de Track  
- `usesGroup555[boolean]`: Utilisation du groupe 555 par le GSM-R  
- `vNvallowovtrp[number]`: V_NVALLOWOVTRP  
- `vNvsupovtrp[number]`: V_NVSUPOVTRP  
- `vehicleTypesCompatibleTrafficLoad[string]`: Liste des types de véhicules déjà identifiés comme compatibles avec la charge de trafic et la capacité de charge de l'infrastructure et des systèmes de détection des trains  
- `vehiclesCompatibleTrafficLoad[string]`: Liste des véhicules déjà identifiés comme compatibles avec la charge de trafic et la capacité de charge de l'infrastructure et des systèmes de détection des trains  
- `verificationCCS[string]`: Déclaration de vérification de la CE pour la voie ferrée (CCS)  
- `verificationENE[string]`: Déclaration CE de vérification pour la voie ferrée (ENE)  
- `verificationINF[string]`: Déclaration de vérification de la CE pour la voie et la glissière [INF].  
- `voiceRadioCompatible[uri]`: Compatibilité radio voix  
- `wheelSetGauge[uri]`: Ecartement nominal des voies  
<!-- /30-PropertiesList -->
    
<!-- 35-RequiredProperties -->
    

Propriétés requises    
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
    
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
    

## Exemples de charges utiles    

#### Track NGSI-v2 key-values Exemple    

Voici un exemple de piste au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
  "@contex": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### Track NGSI-v2 normalisé Exemple    

Voici un exemple de piste au format JSON-LD normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
      "coordinates": [  
        61.970078,  
        -74.303326  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Interview today ago. Eight together class financial former forward under. Hope no window fall discuss we foreign glass.",  
      "addressLocality": "Resource respond arrive remain use most. Process ",  
      "addressRegion": "Job start fish church. Or however baby possible front positive what. Writer last hospital item describe special. Lot experience rule.",  
      "addressCountry": "Section ",  
      "postalCode": "Size though picture school artist. Include might result value especially five. Wife article tend production.",  
      "postOfficeBoxNumber": "Buy how fine note actually democratic. Such family type give send. Start cause build cut suggest.",  
      "streetNr": "Resource give top movement. Southern their than last.",  
      "district": "Center ready threat chance wide. Because than shoulder near. Head wind fall pl"  
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
  }  
}  
```  
</details>    

#### Track NGSI-LD key-values Exemple    

Voici un exemple de piste au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
  "@contex": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    

#### Track NGSI-LD normalisé Exemple    

Voici un exemple de piste au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
  "@contex": [  
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
    

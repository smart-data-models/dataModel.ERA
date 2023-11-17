<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Type de véhicule    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ERA/blob/master/VehicleType/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Type de véhicule autorisé à circuler sur l'infrastructure ferroviaire de l'UE**.    
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `alternativeName[string]`: Nom alternatif  - `altitudeRange[string]`: Plage d'altitude  - `altitudeRangeDetail[number]`: Détail de la fourchette d'altitude  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedCountry[uri]`: Pays autorisé  - `axleBearingConditionMonitoring[uri]`: Surveillance de l'état des roulements d'essieu  - `axleSpacing[string]`: Espacement des essieux  - `boardingAids[string]`: Aides à l'embarquement  - `brakeWeightPercentage[string]`: Pourcentage du poids au frein  - `cantDefficiency[number]`: Efficience des cantons  - `category[uri]`: Catégorie de véhicule  - `catenaryMaxRatedCurrent[number]`: Courant nominal maximal de la caténaire  - `certificate[uri]`: Certificat  - `conditionsTrainFormation[string]`: Conditions formation des trains  - `contactStripMaterial[uri]`: Matériau autorisé pour les bandes de contact  - `dangerousGoodsTankCode[string]`: Code de la citerne de marchandises dangereuses  - `dataGSMRNetwork[uri]`: Données Réseau GSM-R  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dataRadioCompatible[uri]`: Données sur la compatibilité des systèmes radio  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `designMassExceptionalPayload[number]`: Masse nominale en cas de charge utile exceptionnelle  - `designMassNormalPayload[number]`: Masse nominale pour une charge utile normale  - `designMassWorkingOrder[number]`: Masse de conception en état de marche  - `drivingCabs[number]`: Conduire des taxis  - `eddyCurrentBrakePrevention[boolean]`: Prévention du freinage par courants de Foucault  - `eddyCurrentBrakingFitted[boolean]`: Freinage par courants de Foucault équipé  - `emergencyBrake[string]`: Freinage d'urgence  - `endCouplingType[uri]`: Type d'accouplement terminal  - `energyMeterInstalled[boolean]`: Installation d'un compteur d'énergie  - `energySupplyMaxPower[number]`: Alimentation en énergie Puissance maximale  - `energySupplySystem[uri]`: Système d'approvisionnement en énergie  - `etcsBaseline[uri]`: Base ETCS  - `etcsDataCommApp[string]`: Application de communication de données ETCS  - `etcsEquipmentOnBoardLevel[uri]`: Niveau d'équipement ETCS  - `etcsInfill[uri]`: Remplissage ETCS installé côté ligne  - `etcsNationalApplications[string]`: Applications nationales de l'ETCS  - `etcsOnBoardImplementation[string]`: Mise en œuvre de l'ETCS à bord  - `etcsSystemCompatibility[uri]`: Compatibilité du système ETCS  - `ferromagneticWheelMaterial[boolean]`: Matériau ferromagnétique de la roue  - `fireSafetyCategory[uri]`: Catégorie de sécurité incendie  - `fixedSeats[string]`: Sièges fixes  - `flangeLubricationFitted[boolean]`: Lubrification de la bride montée  - `gaugingProfile[uri]`: Jaugeage  - `gsmRRadioDataCommunication[uri]`: Communication de données par radio GSM-R  - `gsmRSetsInDrivingCab[number]`: GSM-R en cabine de conduite  - `gsmRVersion[uri]`: Version GSM-R  - `hasAutomaticDroppingDevice[boolean]`: Dispositif d'abaissement automatique  - `hasCantDefficiencyCompensation[boolean]`: A la compensation de l'inefficacité du cant  - `hasCurrentLimitation[boolean]`: Limitation de courant  - `hasLubricationDevicePrevention[boolean]`: Dispose d'un dispositif de prévention de la lubrification  - `hasParkingBrake[boolean]`: Frein de stationnement  - `hasRegenerativeBrake[boolean]`: Autorisation de freinage par récupération  - `hasSandingPrevention[boolean]`: Prévient le ponçage  - `hasShuntingRestrictions[boolean]`: A des restrictions de shuntage  - `hasTrainIntegrityConfirmation[boolean]`: Confirmation de l'intégrité du train  - `hasWheelSlideProtectionSystem[boolean]`: Système de protection contre le glissement des roues  - `id[*]`: Identifiant unique de l'entité  - `legacyRadioSystem[uri]`: Autres systèmes radio installés (systèmes radio hérités)  - `letterMarking[string]`: Marquage des lettres  - `loadingPlatformHeight[number]`: Hauteur de la plate-forme de chargement  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `magneticBrakePrevention[boolean]`: Prévention du freinage magnétique  - `magneticBrakingFitted[boolean]`: Freinage magnétique  - `manufacturer[uri]`: Fabricant  - `manufacturingCountry[uri]`: Pays de production  - `massPerWheel[number]`: Masse par roue  - `maxCurrentStandstillPantograph[number]`: Courant maximal à l'arrêt par pantographe  - `maxDistConsecutiveAxles[number]`: Distance maximale autorisée entre deux essieux consécutifs en cas de non-conformité aux STI  - `maxFlangeHeight[number]`: Hauteur maximale autorisée de la bride  - `maxImpedanceWheelset[number]`: Impédance maximale autorisée entre les roues opposées d'une paire de roues lorsque celle-ci n'est pas conforme aux STI  - `maxLengthVehicleNose[number]`: Longueur maximale du nez du véhicule  - `maximumAverageDeceleration[number]`: Décélération moyenne maximale  - `maximumBrakeThermalEnergyCapacity[number]`: Capacité maximale d'énergie thermique du frein  - `maximumContactWireHeight[number]`: Hauteur maximale du fil de contact  - `maximumDesignSpeed[number]`: Vitesse de conception maximale  - `maximumLocomotivesCoupled[number]`: Nombre maximal de locomotives accouplées  - `maximumServiceBrake[string]`: Interruption maximale de service  - `maximumSpeedAndCantDeficiency[string]`: Vitesse maximale et déficit de dévers  - `maximumSpeedEmpty[number]`: Vitesse maximale à vide  - `maximumTemperature[number]`: Plage de température (maximale)  - `meetsRequirementVehicleAuthorisation[string]`: Satisfait aux exigences de l'autorisation du véhicule  - `minAxleLoad[number]`: Charge minimale autorisée par essieu  - `minDistConsecutiveAxles[number]`: Distance minimale autorisée entre deux essieux consécutifs  - `minDistFirstLastAxle[number]`: Distance minimale autorisée entre le premier et le dernier essieu  - `minFlangeHeight[number]`: Hauteur minimale autorisée de la bride  - `minFlangeThickness[number]`: Épaisseur minimale autorisée de la bride  - `minRimWidth[number]`: Largeur minimale autorisée de la jante  - `minVehicleImpedance[string]`: Impédance du véhicule  - `minWheelDiameter[number]`: Diamètre minimal autorisé des roues  - `minimumConcaveVerticalRadius[number]`: Rayon vertical concave minimal  - `minimumContactWireHeight[number]`: Hauteur minimale du fil de contact  - `minimumConvexVerticalRadius[number]`: Rayon vertical convexe minimal  - `minimumHorizontalRadius[number]`: Rayon minimal de la courbe horizontale  - `minimumTemperature[number]`: Plage de température (minimum)  - `minimumWheelDiameter[number]`: Diamètre minimal des roues pour les croisements obtus fixes  - `name[string]`: Le nom de cet élément  - `nonCodedRestrictions[string]`: Restrictions non codées  - `numberElementsRakeFreightWagons[number]`: Nombre d'éléments wagons de fret à râtelier  - `numberOfPantographsInContactWithOCL[number]`: Nombre de pantographes en contact avec l'OCL  - `numberOfToilets[number]`: Nombre de toilettes  - `oclType[string]`: Type d'Ocl  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `parkingBrake[boolean]`: Frein de stationnement  - `parkingBrakeMandatory[boolean]`: Frein de stationnement obligatoire  - `parkingBrakeMaximumGradient[number]`: Pente maximale du frein de stationnement  - `parkingBrakeType[uri]`: Type de frein de stationnement  - `passByNoiseLevel[number]`: Niveau de bruit de passage  - `permissiblePayload[string]`: Charge utile autorisée  - `portableBoardingAids[string]`: Aides à l'embarquement portables  - `preventRegenerativeBrakeUse[boolean]`: Empêcher l'utilisation du frein à récupération  - `previousVehicleType[uri]`: Type de véhicule précédent  - `prioritySeats[string]`: Sièges prioritaires  - `prmAccessibleToilets[number]`: Toilettes accessibles  - `protectionLegacySystem[uri]`: Système de protection des trains  - `quasiStaticGuidingForce[number]`: Force de guidage quasi statique  - `radioSwitchOverSpecialConditions[string]`: Commutation radio dans des conditions particulières  - `railInclination[uri]`: Inclinaison du rail  - `referencePassByNoiseLevel[boolean]`: Niveau de bruit de passage de référence  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `shortestDistanceBetweenPantographsInContactWithOCL[string]`: Distance la plus courte entre les pantographes en contact avec l'OCL  - `sleepingPlaces[string]`: Lieux de couchage  - `snowIceHailConditions[uri]`: Neige, glace, grêle  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `startingNoiseLevel[number]`: Niveau sonore au démarrage  - `staticAxleLoadExceptionalPayload[number]`: Charge statique sur l'essieu en cas de charge utile exceptionnelle  - `staticAxleLoadNormalPayload[number]`: Charge statique par essieu pour une charge utile normale  - `staticAxleLoadWorkingOrder[number]`: Charge statique par essieu en ordre de marche  - `stationaryNoiseLevel[number]`: Niveau de bruit à l'arrêt  - `structuralCategory[string]`: Catégorie structurelle  - `subCategory[uri]`: Sous-catégorie de véhicules  - `supportedPlatformHeight[uri]`: Hauteur de la plate-forme supportée  - `thermalCapacityDistance[number]`: Distance de capacité thermique  - `thermalCapacityGradient[number]`: Gradient de capacité thermique  - `thermalCapacitySpeed[number]`: Capacité thermique vitesse  - `thermalCapacityTSIReference[uri]`: Capacité thermique STI de référence  - `thermalCapacityTime[number]`: Capacité thermique temps  - `totalVehicleMass[number]`: Masse totale du véhicule  - `trainControlSwitchOverSpecialConditions[string]`: Commutation du contrôle des trains dans des conditions particulières  - `trainDetectionSystemType[uri]`: Type de système de détection des trains  - `transportableOnFerry[boolean]`: Transportable par ferry  - `type[string]`: Type de données NGSI. Il doit s'agir de VehicleType  - `typeVersionId[uri]`: Type version id  - `typeVersionNumber[string]`: Numéro de version du type  - `usesGroup555[boolean]`: Utilisation du groupe 555 par le GSM-R  - `vehicleContactForce[number]`: Force de contact avec le véhicule  - `vehicleKinematicGaugeOther[string]`: Jauge cinématique du véhicule autre  - `vehicleMaxSandingOutput[string]`: Puissance de ponçage maximale du véhicule  - `vehiclePantographHead[string]`: Tête de pantographe de véhicule  - `vehicleTypeMaximumSpeedAndCantDeficiency[uri]`: Type de véhicule vitesse maximale et insuffisance de dévers  - `vehiclesComposingFixedFormation[number]`: Véhicules composant la formation fixe  - `voiceGSMRNetwork[uri]`: Voix Réseau GSM-R  - `voiceOperationalCommImpl[string]`: Mise en œuvre de la communication vocale opérationnelle  - `voiceRadioCompatible[uri]`: Compatibilité radio voix  - `wheelSetGauge[uri]`: Ecartement nominal des voies  - `wheelSetGaugeChangeoverFacility[uri]`: Dispositif de changement de gabarit des roues  - `wheelSetGaugeTransformationMethod[string]`: Méthode de transformation de l'écartement des roues  - `wheelchairSleepingPlaces[string]`: Espaces de couchage pour fauteuils roulants  - `wheelchairSpaces[number]`: Places pour fauteuils roulants  <!-- /30-PropertiesList -->    
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
## Exemples de charges utiles    
#### VehicleType Valeurs clés de l'INSIG-v2 Exemple    
Voici un exemple de VehicleType au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### VehicleType NGSI-v2 normalisé Exemple    
Voici un exemple de type de véhicule au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
#### VehicleType Valeurs clés NGSI-LD Exemple    
Voici un exemple de VehicleType au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
    "https://smartdatamodels.org/context.jsonld"  
  ],  
  "context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ERA/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### VehicleType NGSI-LD normalisé Exemple    
Voici un exemple de type de véhicule au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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

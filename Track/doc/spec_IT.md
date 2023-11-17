<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Binario    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.ERA/blob/master/Track/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Binario di corsa utilizzato per la circolazione dei treni.    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `IdPhoneErtmsRadioBlockCenter[string]`: ID e numero di telefono del centro di blocco radio ERTMS/ETCS  - `TSIMagneticFields[uri]`: Esistenza e conformità alla STI delle regole per i campi magnetici emessi da un veicolo  - `TSITractionHarmonics[uri]`: Esistenza e conformità alla STI dei limiti delle armoniche nella corrente di trazione dei veicoli  - `accelerationLevelCrossing[string]`: Accelerazione consentita al passaggio a livello  - `additionalBrakingInformationDocument[string]`: Documenti disponibili presso il GI relativi alle prestazioni di frenata  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica      
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `atoCommunicationSystem[uri]`: Sistema di comunicazione ATO  - `atoErrorCorrectionsOnboard[string]`: Correzioni degli errori ATO necessarie per il sistema di bordo  - `atoGradeAutomation[uri]`: Grado di automazione ATO  - `atoSystemVersion[uri]`: Versione del sistema ATO  - `automaticDroppingDeviceRequired[boolean]`: È necessario un dispositivo di caduta automatica  - `bigMetalMass[boolean]`: Grande massa metallica  - `bridge[boolean]`: Il ponte  - `cantDeficiency[number]`: Carenza di Cant  - `cantDeficiencyBasicSSP[uri]`: Deficit di Cant utilizzato per il SSP di base  - `compatibilityProcedureDocument[string]`: Documento con le procedure per i controlli di compatibilità delle rotte statiche e dinamiche.  - `conditionsSwitchClassBSystems[string]`: Condizioni tecniche speciali necessarie per il passaggio tra i sistemi ERTMS/ETCS e di Classe B  - `conditionsSwitchTrainProtectionSystems[string]`: Condizioni speciali per la commutazione tra diversi sistemi di protezione, controllo e avviso dei treni di classe B  - `conditionsUseReflectivePlates[uri]`: Condizioni per l'utilizzo delle targhe riflettenti  - `contactLineSystem[uri]`: Sistema a linea di contatto  - `contactStripMaterial[uri]`: Materiale della striscia di contatto consentito  - `contactStripMaterialMetallicContent[number]`: Materiale della striscia di contatto contenuto metallico  - `dNvovtrp[number]`: D_NVOVTRP  - `dNvpotrp[number]`: D_NVPOTRP  - `dNvroll[number]`: D_NVROLL  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dataRadioCompatible[uri]`: Dati sulla compatibilità del sistema radio  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `demonstrationENE[string]`: Dichiarazione di dimostrazione EI per la pista (ENE)  - `demonstrationINF[string]`: Dichiarazione di dimostrazione EI per binari/paratie [INF]  - `description[string]`: Descrizione dell'articolo  - `distSignToPhaseEnd[number]`: Distanza tra il cartello e la fine della separazione di fase  - `documentRestrictionPositionContactLineSeparation[string]`: Documento con restrizioni relative alla posizione delle unità di trazione multipla per rispettare la separazione della linea di contatto.  - `documentRestrictionPowerConsumption[string]`: Documento con restrizioni relative al consumo di energia di specifiche unità di trazione elettrica  - `eddyCurrentBraking[uri]`: Uso di freni a correnti parassite  - `eddyCurrentBrakingConditionsDocument[string]`: Documento con le condizioni per l'utilizzo dei freni a correnti parassite  - `etcsDegradedSituation[uri]`: Livello ETCS per situazione degradata  - `etcsErrorCorrectionsOnboard[string]`: Correzioni di errore ETCS necessarie per il sistema di bordo.  - `etcsImplementsLevelCrossingProcedure[boolean]`: L'ETCS di terra implementa la procedura di passaggio a livello o una soluzione equivalente.  - `etcsInfill[uri]`: Il sistema ETCS è stato installato a bordo linea  - `etcsInfillLineAccess[boolean]`: Il riempimento dell'ETCS è necessario per l'accesso alla linea  - `etcsLevel[uri]`: Livello Etcs  - `etcsMVersion[uri]`: ETCS M_versione  - `etcsNationalPacket44[boolean]`: Applicazione del pacchetto nazionale ETCS 44 implementata  - `etcsOptionalFunctions[string]`: Funzioni opzionali ETCS  - `etcsSystemCompatibility[uri]`: Compatibilità del sistema ETCS  - `etcsSystemFunctionalitiesNextFiveYears[string]`: Funzionalità del sistema ETCS versione 2.2 o 3.0 da richiedere nei prossimi 5 anni  - `etcsTransmitsTrackConditions[boolean]`: L'ETCS di terra è in grado di trasmettere le condizioni di pista?  - `etcsTransmittedTrackConditions[uri]`: Condizioni del tracciato che possono essere trasmesse  - `flangeLubeForbidden[boolean]`: Vietato l'uso della lubrificazione della flangia  - `freightCorridor[uri]`: Parte di un corridoio ferroviario per il trasporto merci  - `gaugingCheckLocation[string]`: Localizzazione ferroviaria di punti particolari che richiedono controlli specifici  - `gaugingProfile[uri]`: Misurazione  - `gaugingTransversalDocument[string]`: Documentare con la sezione trasversale dei punti particolari che richiedono verifiche specifiche  - `gprsForETCS[boolean]`: GPRS per ETCS  - `gprsImplementationArea[string]`: Area di implementazione del GPRS  - `gradientProfile[string]`: Profilo di pendenza  - `gsmRActiveMobiles[uri]`: Numero di cellulari GSM-R attivi (EDOR) o di sessioni di comunicazione simultanee a bordo per il livello 2 (o il livello 3) dell'ETCS, necessari per eseguire i passaggi da un centro di blocco radio all'altro senza interruzioni operative.  - `gsmRAdditionalInfo[string]`: Ulteriori informazioni sulle caratteristiche della rete  - `gsmRNoCoverage[boolean]`: Nessuna copertura GSM-R  - `gsmROptionalFunctions[uri]`: Funzioni GSM-R opzionali  - `gsmRVersion[uri]`: Versione GSM-R  - `gsmrConstraintsOperateOnlyInCircuitSwitch[uri]`: Vincoli specifici imposti dall'operatore della rete GSM-R sulle unità di bordo ETCS in grado di operare solo in commutazione di circuito  - `gsmrErrorCorrectionsOnboard[string]`: Correzioni degli errori GSM-R necessarie per il sistema di bordo  - `gsmrForcedDeregistrationFunctionalNumber[boolean]`: La rete GSM-R è configurata per consentire la de-registrazione forzata di un numero funzionale da parte di un altro conducente.  - `gsmrNetworkCoverage[uri]`: Reti GSM-R coperte da un accordo di roaming  - `hasAdditionalBrakingInformation[boolean]`: Disponibilità da parte del GI di informazioni aggiuntive  - `hasBallast[boolean]`: Esistenza di una zavorra  - `hasETCSRestrictionsConditions[boolean]`: Esistenza di restrizioni o condizioni operative  - `hasHotAxleBoxDetector[boolean]`: Esistenza di un rilevatore di boccole calde a terra (HABD)  - `hasLevelCrossings[boolean]`: Esistenza di passaggi a livello  - `hasOtherTrainProtection[boolean]`: Esistenza di altri sistemi di protezione, controllo e avviso dei treni installati  - `hasSevereWeatherConditions[boolean]`: Esistenza di condizioni climatiche avverse  - `hasSystemSeparation[boolean]`: Separazione del sistema  - `hasTSITrainDetection[boolean]`: Esistenza di un sistema di rilevamento dei treni pienamente conforme alla STI  - `highSpeedLoadModelCompliance[boolean]`: Conformità delle strutture con il modello di carico dinamico High Speed Load Model (HSLM)  - `hotAxleBoxDetectorDirection[uri]`: Direzione del rilevatore di boccole calde  - `hotAxleBoxDetectorGeneration[string]`: Generazione di HABD a terra  - `hotAxleBoxDetectorIdentification[string]`: Identificazione di HABD di terra  - `hotAxleBoxDetectorLocation[number]`: Ubicazione ferroviaria dell'HABD di terra  - `hotAxleBoxDetectorTSICompliant[boolean]`: Compatibile con la STI HABD di terra  - `id[*]`: Identificatore univoco dell'entità  - `instructionsSwitchRadioSystems[string]`: Istruzioni speciali per passare da un sistema radio all'altro  - `isQuietRoute[boolean]`: Appartenere a un percorso più tranquillo  - `legacyRadioSystem[uri]`: Altri sistemi radio installati (Radio Legacy Systems)  - `lineCategory[uri]`: Categoria di linea  - `linesideDistanceIndicationAppearance[uri]`: Aspetto dell'indicazione della distanza laterale  - `linesideDistanceIndicationFrequency[number]`: Frequenza di indicazione della distanza di linea  - `linesideDistanceIndicationPositioning[uri]`: Posizionamento dell'indicazione della distanza di linea  - `loadCapability[uri]`: Capacità di carico  - `localRulesOrRestrictions[boolean]`: Esistenza di regole e restrizioni di natura strettamente locale.  - `localRulesOrRestrictionsDoc[string]`: Documenti relativi a regole o restrizioni di natura strettamente locale disponibili presso il GI  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `mNvcontact[uri]`: M_NVCONTATTO  - `mNvderun[boolean]`: M_NVDERUN  - `magneticBraking[uri]`: Uso di freni magnetici  - `magneticBrakingConditionsDocument[string]`: Documento con le condizioni per l'uso dei freni magnetici  - `maximumAltitude[number]`: Altitudine massima  - `maximumBrakingDistance[number]`: Spazio di frenata massimo richiesto  - `maximumContactWireHeight[number]`: Altezza massima del filo di contatto  - `maximumPermittedSpeed[number]`: Velocità massima consentita  - `maximumTemperature[number]`: Intervallo di temperatura (massimo)  - `maximumTrainDeceleration[number]`: Decelerazione massima del treno  - `minDistConsecutiveAxles[number]`: Distanza minima consentita tra due assi consecutivi  - `minDistFirstLastAxle[number]`: Distanza minima consentita tra il primo e l'ultimo asse  - `minFlangeHeight[number]`: Altezza minima consentita della flangia  - `minFlangeThickness[number]`: Spessore minimo consentito della flangia  - `minRimWidth[number]`: Larghezza minima consentita del cerchio  - `minWheelDiameter[number]`: Diametro minimo consentito delle ruote  - `minimumContactWireHeight[number]`: Altezza minima del filo di contatto  - `minimumHorizontalRadius[number]`: Raggio minimo della curva orizzontale  - `minimumTemperature[number]`: Intervallo di temperatura (minimo)  - `minimumWheelDiameter[number]`: Diametro minimo della ruota per incroci ottusi fissi  - `multipleTrainProtectionRequired[boolean]`: Necessità di più di un sistema di protezione, controllo e allarme a bordo del treno  - `name[string]`: Il nome di questo elemento  - `nationalLoadCapability[string]`: Classificazione nazionale per la capacità di carico  - `nationalValuesBrakeModel[string]`: Valori nazionali utilizzati per il modello di freno  - `osmClass[uri]`: Classe di mappe stradali aperte  - `otherCantDeficiencyBasicSSP[uri]`: Altre categorie di treni con carenza di cantine per le quali l'ETCS di terra è configurato per fornire SSP  - `otherPantographHead[uri]`: Accettate altre teste di pantografo  - `otherTrainProtection[uri]`: Altri sistemi di protezione, controllo e avviso dei treni in situazioni degradate  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `passesThroughTunnel[uri]`: Passa attraverso il tunnel  - `permitUseReflectivePlates[boolean]`: Autorizzazione all'uso di targhe riflettenti  - `permittedContactForce[string]`: Forza di contatto consentita  - `phaseInfo[string]`: Informazioni sulla separazione di fase  - `phaseSeparation[boolean]`: Separazione di fase  - `platform[uri]`: Piattaforma  - `profileNumberSemiTrailers[uri]`: Numero di profilo standard per il trasporto combinato per semirimorchi  - `profileNumberSwapBodies[uri]`: Numero di profilo di trasporto combinato standard per le casse mobili  - `protectionLegacySystem[uri]`: Sistema tradizionale di protezione dei treni  - `publicNetworkRoaming[boolean]`: GSM-R esistenza del roaming su reti pubbliche  - `publicNetworkRoamingDetails[string]`: Dettagli GSM-R sul roaming verso le reti pubbliche  - `qNvdriverAdhes[uri]`: Q_NVDRIVER_ADHES  - `qNvemrrls[uri]`: Q_NVEMRRLS  - `qNvsbtsmperm[boolean]`: Q_NVSBTSMPERM  - `radioNetworkId[number]`: ID rete radio  - `railInclination[uri]`: Inclinazione della rotaia  - `raisedPantographsDistanceAndSpeed[string]`: Requisiti per il numero di pantografi sollevati e la distanza tra di essi, alla velocità data  - `reasonsEtcsRadioBlockCenterReject[uri]`: Motivi per cui un centro di blocco radio ETCS può rifiutare un treno  - `redLightsRequired[boolean]`: Sono necessarie luci rosse fisse  - `safeConsistLengthInformationNecessary[uri]`: Le informazioni sulla lunghezza di sicurezza da bordo sono necessarie per l'accesso alla linea e al SIL.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `specificInformation[string]`: Informazioni specifiche  - `standardCombinedTransporRollerUnits[uri]`: Numero di profilo di trasporto combinato standard per unità a rulli  - `standardCombinedTransportContainers[uri]`: Numero di profilo di trasporto combinato standard per i container  - `structureCheckLocation[number]`: Localizzazione ferroviaria di strutture che richiedono controlli specifici  - `switchProtectControlWarning[boolean]`: Esistenza di una commutazione tra i diversi sistemi di protezione, controllo e segnalazione durante il funzionamento  - `switchRadioSystem[boolean]`: Esistenza di switch over tra sistemi radio diversi  - `systemSeparationInfo[string]`: Informazioni sulla separazione del sistema  - `tNvcontact[number]`: T_NVCONTATTO  - `tNvovtrp[number]`: T_NVOVTRP  - `temperatureRange[uri]`: Intervallo di temperatura  - `tenClassification[uri]`: Classificazione TEN (di binario, di piattaforma, di binario di raccordo)  - `tenGISId[string]`: Identità TEN GIS  - `tiltingSupported[boolean]`: Indicazione se le funzioni di inclinazione sono supportate dall'ETCS.  - `trackDirection[uri]`: Direzione di marcia normale  - `trackId[string]`: Identificazione del tracciato  - `trackLoadCapability[uri]`: Capacità di carico dei binari  - `trackPhaseInfo[uri]`: Informazioni sulla fase del tracciato  - `trackRaisedPantographsDistanceAndSpeed[uri]`: Traccia della distanza e della velocità del pantografo sollevato  - `trackSystemSeparationInfo[uri]`: Informazioni sulla separazione dei sistemi di binario  - `trainDetectionSystem[uri]`: Sistema di rilevamento dei treni  - `trainIntegrityOnBoardRequired[boolean]`: Conferma dell'integrità del treno da parte del personale di bordo (non del macchinista) necessaria per l'accesso alla linea  - `tsiPantographHead[uri]`: Teste di pantografo conformi alle STI accettate  - `tsiSwitchCrossing[boolean]`: Conformità alla STI dei valori in servizio per scambi e incroci  - `type[string]`: Tipo di dati NGSI. Deve essere Traccia  - `usesGroup555[boolean]`: Uso GSM-R del gruppo 555  - `vNvallowovtrp[number]`: V_NVALLOWOVTRP  - `vNvsupovtrp[number]`: V_NVSUPOVTRP  - `vehicleTypesCompatibleTrafficLoad[string]`: Elenco dei tipi di veicoli già identificati come compatibili con il carico di traffico e la capacità di carico dell'infrastruttura e dei sistemi di rilevamento dei treni  - `vehiclesCompatibleTrafficLoad[string]`: Elenco dei veicoli già identificati come compatibili con il carico di traffico e la capacità di carico dell'infrastruttura e dei sistemi di rilevamento dei treni  - `verificationCCS[string]`: Dichiarazione di verifica CE per la pista (CCS)  - `verificationENE[string]`: Dichiarazione di verifica CE per la pista (ENE)  - `verificationINF[string]`: Dichiarazione di verifica CE per binari/accompagnamento [INF]  - `voiceRadioCompatible[uri]`: Voce di compatibilità del sistema radio  - `wheelSetGauge[uri]`: Scartamento nominale  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
modello di dati mappato dall'ontologia ERA https://data-interop.era.europa.eu/era-vocabulary (Agenzia dell'Unione Europea per le Ferrovie)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### Traccia dei valori-chiave NGSI-v2 Esempio    
Ecco un esempio di traccia in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### Traccia NGSI-v2 normalizzata Esempio    
Ecco un esempio di traccia in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.    
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
#### Traccia dei valori chiave NGSI-LD Esempio    
Ecco un esempio di traccia in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### Traccia NGSI-LD normalizzata Esempio    
Ecco un esempio di traccia in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    

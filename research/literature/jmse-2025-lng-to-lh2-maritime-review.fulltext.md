> **Machine-generated Markdown** — converted from the source PDF with
> [Microsoft markitdown](https://github.com/microsoft/markitdown) v0.1.6 on 2026-07-21.
>
> **Source (open access):** Passalacqua, M.; Traverso, A. *From LNG to LH2 in
> Maritime Transport: A Review of Technology, Materials, and Safety Challenges.*
> Journal of Marine Science and Engineering **2025, 13(9), 1748**. DOI
> `10.3390/jmse13091748`. Thermochemical Power Group (TPG), DIME — University of
> Genova, Italy.
>
> **Original PDF:** `research/sources/raw/jmse-2025-lng-to-lh2-maritime-review.pdf`
> · **Curated dossier:** `2025-jmse-lng-to-lh2-maritime-review.md`
> · **staging.csv id:** `jmse-2025-lng-to-lh2-review`
>
> ⚠️ Faithful text extraction of a two-column PDF — subscripts (e.g. "LH₂" may
> render as "LH" then "2") and table layout can be imperfect. **Verify any figure
> against the original PDF before citing or promoting.**

---

Review
From LNG to LH in Maritime Transport: A Review of
2
Technology, Materials, and Safety Challenges
MatteoPassalacqua* andAlbertoTraverso*
ThermochemicalPowerGroup(TPG),DIME—UniversityofGenova,ViaMontallegro1,16145Genova,Italy
* Correspondence:matteo.passalacqua@edu.unige.it(M.P.);alberto.traverso@unige.it(A.T.)
Abstract
Theadoptionoflow-carbonfuelsinmaritimepropulsionrequiresoperationalautonomy,
materialsuitability,andcompliancewithsafetystandards,makingliquidfuelslikeLNG
andLH themostviableoptions. LNGiswidelyusedforreducingGHG,NOx,andSOx
2
emissions,whileLH ,thoughnewtothemaritimesector,leveragesaerospaceexperience.
2
ThispaperexplorestheoperationalrequirementsandchallengesofLH cryogenichan-
2
dlingsystemsusingLNGpracticesasareference. Keycomparisonsaremadebetween
LNGandLH supplysystems,focusingoncryogenicmaterials,hydrogenembrittlement,
2
andstructuralintegrityundermaritimeconditions. Mostmaritime-approvedmaterials
are suitable for cryogenic use, and hydrogen embrittlement is less critical at cryogenic
temperaturesduetoreducedatomicmobility. RiskassessmentssuggestLH ’ssafetyrecord
2
stemsfromlimitedoperationaldataratherthansuperiorinherentsafety. Thepaperalso
addresses crucial safety and regulatory considerations for both fuels, underscoring the
needforstrictadherencetostandardstoensurethesafeandcompliantintegrationofLH
2
inthemaritimeindustry.
Keywords: alternativefuels; maritimesector; liquefiedhydrogen; fuelsupplysystems;
hydrogensafety
AcademicEditors:Wei-HsinChen,
AristotleT.Ubando,Chih-CheChueh, 1. Introduction
LiwenJinandYanjunSun
Inthesedays,hydrogenismostlystoredandhandledincompressedform,thereason
Received:30July2025 beingthesimplertechnologicalrequirementswithrespecttoliquefied,cryo-compressed,or
Revised:1September2025
chemical-basedstorage(informofmethanol,ammonia,liquidhydrogencarriers,etc.). In
Accepted:2September2025
somecases,metalhydridesarepreferredthankstothelowerpressuresrequired,butinthis
Published:10September2025
casethestorageisweightyandtheadsorption/desorptionreactionsareenergyintensiveand
Citation: Passalacqua,M.;Traverso,
requirethoroughthermalmanagement.Inthisscope,liquefiedhydrogenisdeemedamong
A.FromLNGtoLH2inMaritime
themostsuitableformsofphysical-basedhydrogenstorageformaritimeapplications,thanks
Transport:AReviewofTechnology,
Materials,andSafetyChallenges.J. toitsunmatchedgravimetricenergydensityandnoneedforchemicalconversionpriorto
Mar.Sci.Eng.2025,13,1748. https:// utilizationinprimemoversorpowergenerationsystems[1]. LH ismostcommonlyused
2
doi.org/10.3390/jmse13091748 inaerospaceapplications, wherethecombinationofhighenergydensityandlowweight
Copyright:©2025bytheauthors. representsthebestsolutionforrocketsandspacelaunchers. Therefore, thetechnological
LicenseeMDPI,Basel,Switzerland. maturity achieved in these fields indicates the potential for technology transfer to more
Thisarticleisanopenaccessarticle commerciallyrelevantsectors,suchaspowergenerationandtransports[1].
distributedunderthetermsand
Inthecontextofthemaritimeindustry,itappearsthatthisisatwo-sidedissue. While
conditionsoftheCreativeCommons
it is imperative that industry and regulatory bodies leverage the extensive knowledge
Attribution(CCBY)license
accumulatedinthedomainofLNG,asectorwithamoreestablishedpresence,itisevident
(https://creativecommons.org/
licenses/by/4.0/). thathydrogenisadistinctmoleculewithitsownphysicalcharacteristics.Hence,challenges
J.Mar.Sci.Eng.2025,13,1748 https://doi.org/10.3390/jmse13091748

J.Mar.Sci.Eng.2025,13,1748 2of22
associatedwithstorage,handling,andsafetyshouldbetakenintocarefulconsideration
andtackledwithaquitedifferentprocedure,whilethemeasuresundertakenwithLNG
shouldinfactberegardedjustasamerestartingpointforfuturemaritimeuptake.
Hydrogeniswidelyexploredasanalternativefuelformaritimetransport. Thanksto
theirefficiency,fuelcellsareexpectedtobeakeytechnologyindecarbonizingthemaritime
sector,bothinPEMFC(protonexchangemembranefuelcells)andSOFC(solidoxidefuel
cells) architectures [2]. An extensive number of projects is currently dealing with fuel
cellintegrationsonboard,especiallyusingPEMFCscoupledwithbatteriesorSOFCsfor
hotelingorauxiliarypowerunits[2].
Despitebeingthemostabundantelementintheuniverse,hydrogenmustbeobtained
from molecules at a cost in terms of both energy and emissions. Methane reforming is
themostcommonhydrogenproductionmethod: Outof97Mttotalproductionin2023,
morethan80%wassourcedfromhigh-carbonprocesses(morethan60%fromunabated
methanereformingandaround20%fromcoalgasification)[3]atanaverageSEC(specific
energyconsumption)of46.2kWh /kg[4]. Waterelectrolysisisconsideredthebenchmark
th
technologyforzero-emissionproduction. However,thetotalinstalledelectrolyzercapacity
is a mere 1.4 GW worldwide, of which less than 20% is actually operational [3]. It is
expectedthattheongoingresearchandcommitmenttosustainableenergyproductionwill
increasetheshareofalternativefuelsobtainedfromgreensources.
This paper investigates the suitability of liquefied natural gas (LNG) and liquid
hydrogen(LH )formaritimepropulsion,withtheaimofprovidingacomparisonoftheir
2
technicalperformance,operationalchallenges,materialcompatibility,andsafetychallenges
inordertoassesstheirrolesinthesector’stransitiontowardlow-carbonshipping.
2. OverviewofCryogenicFuelUtilizationinMaritimeApplications
Ageneralstate-of-the-artassessmentforLNGandLH hydrogenhandlingsystemsin
2
themarineenvironmentdepictsageneraltwo-foldsituation.
LNG is a well-established technology in the marine sector from container ships to
cruise ships, having a high TRL and being the preferred alternative for short-term de-
carbonization. Althoughitisdemandingintermsofcomponentsandmaterialsforthe
handlingsystemowingtothecryogenictemperatures,thewiderandwideruptakefosters
marketsolidityandavailability. Moreover,naturalgas-runningprimemoverscounton
longtimetechnologicalmaturity,irrespectiveofthefuelsource. Hence,LNGisaready-
to-goalternativeforimmediateuptakeofmass-producedlowemissionpowersolutions.
Furthermore,establishedengineeringbestpracticesexistforLNGapplications[5].
Hydrogeningaseousformstillhaslimiteduptakeinthemarinesector,andnoconcrete
examplesinliquefiedform. Whileconventionalfossilfuelsstillplayakeyrolealongside
thenewcomerLNGindeep-seasegmentsthankstotheirenergydensity,short-seasegments
maybenefitmorefromhydrogenpenetrationinthenearfuture. However,despitesome
prototypesthathavebeenconstructedandtested,theTechnologyReadinessLevel(TRL)
islow,andcomponentsandmaterialsmustbedesignedtowithstandextremeconditions
suchashighpressuresinthecaseofGH storageorcryogenictemperaturesinthecase
2
ofliquefiedhydrogen(LH ). Hence,thecriticalitiesexistingforLNGareevenworsefor
2
hydrogen,especiallywhenhydrogenstorageinliquefiedformisconsidered. Furthermore,
achieving equivalent onboard energy storage necessitates significantly increased tank
volumes,whichintroducesconstraintsonvessellayoutandhasdirectimplicationsforship
design,includingreducedpayloadcapacity,alteredhullgeometry,andcomplexintegration
of cryogenic containment systems. Operationally, these storage penalties translate into
shorter voyage ranges or the need for more frequent refueling while also introducing

J.Mar.Sci.Eng.2025,13,1748 3of22
safety,boil-offmanagement,andefficiencyconsiderationsthatarelesspronouncedinLNG
systems.
Despitethisevidentdifferenceintechnologicaladvancement,severalanalogiescan
be found between the best practices adopted with the two liquid cryogenic fuels, and
the growing experience with LNG may prove crucial to overcome the main challenges
associatedwithonboardcryogenichydrogenhanding.
2.1. LiquefiedNaturalGas(LNG)
Natural gas is mainly composed of methane, but in general it is a mixture of hy-
drocarbonswithdifferentLHVs,densities,andboilingpoints,asthecompositionvaries
consistentlydependingonthegeographicalzoneofextraction. However,acontentof~90%
methaneisgenerallyconsideredrealisticonaverage[6]. InTable1thethermophysical
featuresofnaturalgasarereported(puremethanehashigherLHVandlowerdensity).
Table1.MainthermophysicalpropertiesofLNG.
Parameter Value
Densityatambientconditions[kg/m3] 0.72
LHV[MJ/kg] 50
Energydensity[MJ/m3] 40
Boilingpoint@1atm[◦C] −162
Meltingpoint@1atm[◦C] −182
Criticaltemperature[◦C] −83
Criticalpressure[MPa] 4.6
Thermalconductivity[W/mK] 0.034
Natural gas in its liquefied form (LNG) represents the current state-of-the-art for
deep-seaandcruiseshipstargetingGHGemissionsreduction. AsitisclearfromFigure1,
mostvesselsstillrunonconventionalfuels,butLNGiscurrentlythefirstalternativeeither
forshipsalreadyinoperationorfornewconstruction.Thisisaconsequenceofthematurity
of the natural gas market, of the high TRL of LNG production, storage, and utilization
and,lately,italsohassomegeopoliticalimplications. Moreover,naturalgascouldevenbe
sourcedfrombiomassvalorization. Biomethanehasgainedmoreandmoreattentionin
transportationthankstoitsreducedcarbonfootprintascomparedtonaturalgas[7],butits
utilizationonlargescalemaritimetransportisquestionableduetoitslimitedsupplyand
thecurrentdifficultyofexpandingscalabilitytothesamevolumesasfossilLNG.
Today, LNG-powered ships make use of three types of tanks, according to IMO
classification(IGCcode): TypeA,employingaprismaticdesignandacompletesecondary
barrier,non-pressurized. Thesederivedirectlyfromstandardoilandbulktankersandare
typicallyshapedasthecross-sectionofthevesseltheyequip;TypeB,employingspherical
(Mosstype)orprismaticdesignandapartialsecondarybarrier,non-pressurized;TypeC,
cylindrical-shapedmono-lobedortwo-lobed,pressurized.
Type A and Type B designs are used for bulk LNG tankers or generally for bulk
transporters,whilethethirdisgenerallyusedforsmallervesselswithLNGpropulsion[8].
SphericalTypeBvesselsaremostlyusedbyJapaneseLNGcarriers,whileEuropeantankers
tendtorelyonmembraneTypeAtank[9]. Avisualcomparisonofthethreedesignsis
reported in Figure 2. Comparing Type A and Type C tanks, the former have 30 to 40%
greatervolumeefficiencies[9].

J.Mar.Sci.Eng.2025,13,1748 4of22
Figure1.Alternativefueluptakeinthemaritimesector[8].
Figure2.OutlookoftanktypesforonboardLNGstorage.
LNGtankerssometimesemploymembranetanks,namelyasandwichconstruction
insuchafashionthattheshiphullbecomestheoutertank,andtheinsulationisplaced
inbetweenthehullandtheinternalmembranalliner. Sometimes,asecondarymembrane
madeofcompositematerialisexploited.Thisdesignallowsforquickerandeasierassembly
onboard,butitcanonlysuitvesselswherethecryogenconstitutesthepayload.
2.2. LiquefiedHydrogen(LH )
2
Hydrogenincryogenicliquefiedformhasfavorablepropertiesthatmakeitconvenient
fortransportation,asectorinwhichhighenergydensityistypicallyrequired. Asopposed
toanyotherhydrogencarrier(ammonia,LOHCetc.),itdoesnotrequireanyconversion
beforeitsutilizationinaprimemover. However,someseriouschallengesareassociated
withcryogenicstorageonboard,beginningwithevaporationcontrolandboil-offhandling.
InTable2therelevantpropertiesofhydrogenarereportedandcomparedtothatofmethane.

J.Mar.Sci.Eng.2025,13,1748 5of22
Table2.Thermophysicalpropertiesofhydrogenandmethane.ObtainedfromREFPROP[10].
Parameter Hydrogen Methane
LHV[MJ/kg 120 50
HHV[MJ/kg] 141 55
Boilingpoint@1atm[K] 20.3 111.2
Flammabilityconcentrationlimitsinair[%vol] 4–75 5–15
Diffusioncoefficientinair[cm/s] 0.61 0.16
Criticalpoint[Mpa/◦C] 1.3/−234 4.6/−83
It is evident that methane is around six times denser than hydrogen and easier to
handleincryogenicformthankstoitshigherboilingpoint. Indeed,thelowertheboiling
point,themoredifficultitistomaintainthecryogenicgasinliquefiedform,meaningthat
the evaporated BOG is more relevant in terms of percentage of stored fuel mass (BOR,
boil-offrate,hasunits[kg /kg ]).
BOG LH2
Theutilizationofliquefiedhydrogensetsanadditionalchallenge.Inambientconditions,
ahydrogenmoleculeconsistsof75%ortho-hydrogen(o-H )and25%para-hydrogen(p-H ).
2 2
Thelatterisalsonamednormalhydrogen.Thetwoformsdifferonlyintheiratomicstructures;
namely, the protons have the same (parallel) or opposite (antiparallel) spin, resulting in
higher or lower internal energy, respectively. At equilibrium, LH consists of 100% para-
2
hydrogen,p-H .Ortho-hydrogen,o-H ,isthermodynamicallyunstableatlowtemperatures
2 2
andspontaneouslyconvertstop-H ,releasing527kJ/kgofheat[11],whichismorethan
2
the latent heat of vaporization of LH (446 kJ/kg) at ambient pressure. This means that
2
theliquefactionofnormalhydrogenresultsinaspontaneousexothermicconversionofthe
bulkliquidtopara-hydrogen,releasinganamountofheatsufficienttovaporizebacksome
mass. (Atequilibrium,thereactionheatwouldexceedthevaporizationheat,resultingin
fullre-gasification.However,theslowkineticsreducetheeffectiverateofreaction,limiting
the re-vaporization impact). The technical solution consists in promoting ortho- to para-
conversionpriortocondensationbymeansofacatalyticmetal-basedortho-parareactorinside
theliquefactionplant[11].Despitethisclearhindrancetousinghydrogeninaliquefiedform,
itdoesnotrepresentanissueaslongasthebulkliquidismaintainedbelowthepara-ortho
inversiontemperature,whichsitsaround100K.Onthecontrary,thisimprovesdormancy,
sinceLH isconvertedfromp-H too-H throughanendothermicreactionduringheatingup.
2 2 2
However,thisisnotsufficienttopreventboil-off,asthekineticsofp-H too-H conversionare
2 2
considerablyslowerthanvaporization.Nevertheless,somestudiesconsideracatalyticpara-
orthoconverterasapotentialenhancerofthermalinsulationforimproveddormancy[12–14].
Nevertheless,hydrogenreliquefactionisenergy-intensiveand,especiallyfortransportation,
thisoftenprovesanti-economical.SpecificEnergyConsumption(SEC)valuesobtainedfrom
numericalsimulationsaregenerallyaround6–8kWh/kgH ,whilerealplantSECsitsaround
2
12–15kWh/kgH ,confirmingthelargediscrepancybetweensimulationsandrealindustrial
2
liquefiers[11,15,16]. However,toprovetheinterestinsuchnovelfuels,theresearchisalso
exploringthetechno-economicsofLH uptakeinthemaritimesector[17,18].Generalresults
2
showthatsuchfuelisstillfarfrombeingeconomicallyattractivewhencomparedtoother
alternatives, further penalizing its current appeal for ship makers. However, it is known
thatsomeshipbuildersareactuallywillingtopursuetheircommitmenttowardsahydrogen
poweredpassengership[19].
Asidefromthemaritimesector,LH isalsoaninterestingalternativeforaircraftappli-
2
cations,sinceitguaranteesthehighestrangeascomparedtoanyotherhydrogenstorage
methods. This interest is confirmed by several projects ongoing on this topic. Airbus
isinvestigatinghydrogenpoweredaircraftwithintheZEROeproject[20],exploringthe
feasibilityofthreedifferentaircraftdesigns. Furthermore,theyhaveaccumulatedconsider-
ableexpertiseinthedomainofaerospaceengineering,evidencedbytheirinvolvementin

J.Mar.Sci.Eng.2025,13,1748 6of22
thedevelopmentofliquidhydrogenfuelsystemsforspaceflightvehicles. Furthermore,
Airbus is also involved in the investigation of modified ground operations, aiming to
developessentialtechnologiesandstandardsforhydrogenrefuelingatairports[21]. Early
findingsconfirmthatadedicatedLH refuelingareashouldbeprovidedatairports,rather
2
thanhavingLH trucksmovingaroundtheapron. Rolls-Roycehaspartneredwithother
2
relevantcompaniesinthesectortodevelophydrogencombustionaeroenginesforboth
medium and short haul aircraft [22]. In the aviation sector, however, the large volume
requiredbyhydrogenstorageappearstobethemostchallengingobstacle,especiallyfor
longhaulaircraft. Therefore,researchersfocusonshort-haulaircraftorrotorcraft[23],also
highlightingthepotentialforrecuperatedcyclestoimprovespecificfuelconsumption.
3. StorageandHandlingSystemsforMaritimeCryogenicFuels
Conceptually,twoalternativesarepossibleforLNGandcryogenicfuelsingeneral: a
conventionalpump-drivensystemorapump-freelayoutwithapressurebuildup(PBU)
unit. Inthefirstcase, theliquefiedgasisdrawnfromapump, usuallysubmergedand
insulated, and conveyed to the vaporizer via vacuum-insulated piping. In the second
system,thecryogenictankispressurizedviaapressurebuildupsystem,whichregulates
thenaturalboil-offtendencyviathethermalloadfromthePBUheatexchanger. Figure3
depictstheconceptualschemeofbothalternatives. Thepump-drivensystemallowsfor
higher delivery pressures and wider range of deliverable mass flows to the user, but
includesacritical,expensive,andlow-TRLcomponentlikeacryogenicpump. ThePBU-
drivensystemofferslowerperformanceintermsofmaximumpressureachievable,butitis
simplerandallegedlymorereliable. Inaddition,thepressurizedlayoutallowsforslightly
higherstoragetemperaturesandpossiblylessstringentinsulation,eventhoughsaturation
temperatureandconsequentlyBOGratesonlyhaveminordependenceonstoragepressure,
especiallyinthecaseofliquefiedhydrogen,asshowninTable3.
Figure3.Conceptualschemesofcryogenicfuelhandlinglayouts:pump-driven(top)andpressure-
drivenwithPBU(bottom)systems.

J.Mar.Sci.Eng.2025,13,1748
7of22
Table3.Hydrogenandnaturalgassaturationpointvariationwithstoragepressure.Obtainedfrom
REFPROP[10].
|               | Hydrogen        |      |               | NaturalGas      |      |
| ------------- | --------------- | ---- | ------------- | --------------- | ---- |
|               | Temperature[◦C] |      |               | Temperature[◦C] |      |
| Pressure[MPa] |                 |      | Pressure[Mpa] |                 |      |
|               | 0.1             | −253 | 0.1           |                 | −162 |
|               | 0.6             | −245 | 0.6           |                 | −134 |
|               | 1               | −241 | 1             |                 | −124 |
|               |                 | −240 |               |                 | −120 |
|               | 1.2             |      | 1.2           |                 |      |
|               |                 |      | 2             |                 | −107 |
|               |                 |      | 3             |                 | −96  |
−87
4
3.1. LH 2 SystemAvailabilityandComparisonwithLNG
The distance between LNG and liquid hydrogen for maritime use is net and clear,
especiallyintermsoftechnologyreadinesslevel(TRL),bothatthecomponentlevelandthe
fullsystemlevel.Ontheonehand,maritimeLNGcomponentsandsystemsareofferedbya
numberofmanufacturers,basedonbothreciprocatingpumpsandsubmergedturbopumps
forawiderangeofnominalmassflows. Forinstance,bothWartsilaandMANCryooffer
a complete and scalable assembly with a cryogenic pump and Type C tank up to 9 bar
storagepressureinthefirstcase[24]andaPBUconfigurationinthesecondcase[25].
Ontheotherhand,theavailabilityofLH 2 fullsystemsislimited. Nonetheless,there
aresomeproductsavailableonthemarketforLH . Lindespecializesinstoragesystems
2
andtransferlinesforrefuelingstations,whileCryostarandNikkisofocusmoreonend
userapplicationswithawiderangeofreciprocatingpumpsandvaporizers[26,27]. Chart
Industriesalsooffersawiderangeofcryogenicpumps,heatexchangers,andcryogenic
storage tanks [28]. At present, Cryostar is the only known manufacturer to be offering
submerged transfer pumps for liquefied hydrogen [26], with mass flow ratings up to
500m3/h(~10kg/s). ItisreportedthatasuperyachtconstructedbyFeadshipwillbethe
firstvesseltohaveacompletelybelow-deckliquidhydrogenstorageandvaporization
system[29]. Additionally,agroupofpartnersincludingRINA,Wartsila,andHelbiohave
studiedandproposedasolutionfortheonboardproductionofhydrogenbasedonLNG
reforming[30]. Thehydrogenfromsyngasisusedinamixwithvaporizednaturalgas,
eliminatingtheneedforstorage. TheCO isliquefiedviathecoldLNGstreamandstored
2
inatankforshoredisposal. Alternatively, itmaybeusedasaninertfluidforonboard
purposes[30].
From Table 4, it is evident that a large delay in LH technology readiness exists
2
comparedtoLNGformaritimeapplications. Simpleconstructionelements,suchaspiping,
heat exchangers, and tanks are unlikely to be significant impediments to the uptake of
liquidhydrogen. However,technologicalchallenges,particularlythoserelatedtopumps
andpipefittings,arelikelytohindertheadvancementofthisfield. DNVhasoutlinedan
expectedmaturationtimelineforenergyconvertersandcorrespondingsafetyregulations
fortheonboarduseofalternativefuels[31].
Table4. CurrentTechnologyReadinessLevels(TRL)ofthemaincomponentsinacryogenicfuel
handlingsystem.
|     | Tank&Insulation | Pump | HeatExchanger | Piping | Valves/Fittings |
| --- | --------------- | ---- | ------------- | ------ | --------------- |
| LNG | 9               | 9    | 9             | 9      | 9               |
| LH2 | 6–7             | 5–6  | 7–8           | 7–8    | 8               |

J.Mar.Sci.Eng.2025,13,1748 8of22
3.2. TheProblemofBoil-Off(BOG):HandlingMethodsandComparisonwithLNG
Regardlessofinsulationperformance,allgasesstoredinliquefiedformwillgenerate
acertainamountofboil-offgas(BOG),buildingpressureinsidethetank. Topreventtank
failure,suchevaporatedfractionsmustberemoved. Therefore,itiscrucialtounderstand
thebestsolutionsformakinguseoftheBOGwithoutfurtheraffectingconversionefficiency.
Sensitivityassessmentsontheinfluenceofseveralparametersinamarineenvironment
highlightthatforLNG,ambienttemperatureandstoragesizehavelimitedinfluenceson
theboil-offrate(BOR),whiletheLH BORisstronglyaffectedbytheseparameters[17].
2
Here,efficiencyisdefinedastheratiooftheoutputandinputenergycontentinthebulk
fuel. Overall,forlargevolumespertainingtoLH bulkcarriersratherthanLH fueltanks,
2 2
BOGtreatmentorutilizationallowstherecoveryofaround4–6%oftheenergylostthrough
spontaneousevaporation.
Althoughitistruethatpreventingoverpressuresincryogenictanksisdesirablefroma
safetypointofview,asmallamountofbuilt-uppressuresetsevaporationbackandreduces
theabsolutemassofevaporatedBOGforthesameheattransferintothecryogenictank. To
date,state-of-the-artautomotiveandmarineLNGandLH storagetanksallowforMAWP
2
levelsintherange5–15bara,withhigherlevelsinthecaseofPBU-typehandlingsystems.
LNG has a peculiar feature to deal with: since it consists of a mixture of different
hydrocarbonswithdifferentboilingpoints,achangeincompositionoccursduringevap-
oration,leadingtoanincreasinglyhigherconcentrationofheavyfractions. Thisprocess
is referred to as “LNG weathering”. As may be derived from [32], the energy content
variesgreatlyduringevaporation,dependingontheinitialcompositionandthepresence
ofnitrogeninthegas. Furthermore,BOGalsohasaverydifferentcompositionthanbulk
liquefiednaturalgas[32],henceitsthermophysicalpropertiesalsochangeconsiderably.
Topreventoverpressures,theBOGmustbehandledbymeansofseveralalternatives.
Continuousventingisclearlytoowastefulandisneverusedinnormaloperationexcept
forsecurityreasonsintheeventofanemergency.
Reliquefactionrequiresanadditionalsystem,whichtypicallyincludesacompressor,a
coldsource,andanexpansiondevice,asdepictedinFigure4.
Figure4.Conceptualschemeofareliquefactionsystem.
The refrigeration cycle displayed in Figure 4 may be either a conventional reverse
cycleoracryocooler. Standardreversecycles(e.g.,chillers,refrigerators,andheatpumps)
arerecuperativecycles,wherebytheworkingfluidevolvesinonedirectionbetweentwo
fixedpressurelevels. ThiscategoryincludesJoule–Thomson,RBC,andClaudecoolers.
Conversely,regenerativecyclesemployoscillatingflowandpressurewithcomplementary
phaseanglestoattainrefrigerationatthecoldend. Pulse-tubecryocoolersandStirling
chillersareexamplesofthiscategory.Anyway,BOGpre-compressionmightbebeneficial,at

J.Mar.Sci.Eng.2025,13,1748 9of22
theexpenseofanadditionalBOGcompressorpowerinadditiontothepowerconsumption
oftherefrigerationcycle[33].
ItmustberecalledthatBOGreliquefactionisanenergyintensiveprocess: forlarge
hydrogenliquefactionplants,numericalestimatesfromprocesssimulationarebetween6
and8kWh/kgLH [11,15,34],whilerealSECsarehigher. Areviewoftherelevantliterature
2
suggeststhatLNGliquefactionplantstypicallyhaveSECsthatareoneorderofmagnitude
lower[34]. Whenfocusingonthemaritimesector,wheretheplantmustbemorecompact
andtheefficienciesofthecomponentsarelower,itcanbeeasilyforecastthatSECvalues
willbehardlyacceptable, notevenforlargevolumessuchasintheSuisoFrontierLH
2
tanker[35]. Indeed,duringthetripfromAustraliatoJapan,roughly10%oftheloadedLH
2
isdispersedthroughtheventmast. Traditionalcryogeniccyclesaresuitableforlargescale
land-basedgasliquefactionplants,whileregenerativecryocoolersaremorecompactand
mightbesuitableforLH reliquefactionfortransport. Nevertheless,astudyconducted
2
byNASAtoassessthepotentialforazeroboil-offscenariorevealedthatstate-of-the-art
cryocoolersnecessitateanaveragepowerinputof0.45kWperWofcoolingpower[36].
Inlightofthis,eventhoughcryocoolersarecompactandrelativelylightweight,todate
BOGreliquefactiondoesnotappeartobeaneconomicallyviablesolutiononboardLH
2
poweredships.
ThesolutionofdirectBOGutilizationasfuelisviableandcurrentlyemployedonboard
dual-fuelships. ForthecaseofatypicalLNGcarrier,thefuelsupplyatthemaximumrated
powerisalmostequaltothegeneratedBOGquantity[37],whileforpassengershipsor
cruiseshipsthesmallersizeofthetankmightnotcreatesufficientBOGtoruntheengines.
RegardingLH ,sinceBOGissignificantlyhigherthanLNGandgrantingthatreliquefaction
2
isnotconsideredanoption,apartofthestoredhydrogenmassislikelytobelost. Finally,
sinceBOGmustbeheateduptoroomtemperaturepriortoitsuse,asignificantproportion
ofavailablecoldexergyfromthefuelcouldbeutilizedforthepurposeofenergystorage,
withtheobjectiveofeithercooling/heating[38],powerproduction[39],orasathermal
sinkforauxiliarythermalengines[40].
4. MaterialsforCryogenicHydrogenStorage
4.1. MechanicalPropertiesatCryogenicTemperatures
Severecryogenicconditionsposeproblemsinselectingamaterialcapableofwith-
standing mechanical stress within an acceptable range. In general, exceptionally low
temperaturestendtomakematerialsverybrittle. Inparticular, astheDuctiletoBrittle
TransitionTemperature(DBTT)isovercome,theabilityofamaterialtowithstanddynamic
stresses(i.e.,impactsorsuddenchangesinpressure)ishighlyreduced.
Metallicmaterialsusuallyhaveexcellentfracturetoughnessinambientconditions.
However, only some of those retain acceptable figures in cryogenic conditions and are
chosen for such sectors. The most suitable metals for cryogenics are austenitic steels
andhigh-resistancealuminumalloys. Otherthanthat,titaniumalloysandnickelalloys
showadequateperformanceaswell;however,theyareconsistentlymoreexpensive. At
cryogenictemperatures, thematerialhasimprovedmechanicalresistance, butitisalso
more brittle [41,42]. This is a common trend for most steels, especially martensitic and
ferritic,whileforausteniticonessuchasAISI316thedeviationislessevident[41].
Onthecontrary,othermetallicalloysdisplayabehaviorwhichisquitedifferentas
comparedtosteels,e.g.,6061-T6aluminumalloy. Generally,thetrendofincreasingyield
pointisconservedbut,inthiscase,theplasticrangeisalsoenhanced.Atpresent,aluminum
alloysarethemainmaterialsforliquidhydrogentanksforspacerockets[43],buttitanium
alloysarealsoemployedforcomponents(e.g.,turbopumps)ofrocketengines[43].

J.Mar.Sci.Eng.2025,13,1748 10of22
Materialsthatshowsuitablepropertiesatlowtemperaturesgenerallyalsohavelower
thermalconductivitythanothersimilarmetalalloys.ThisistrueforAISI316[18]andTi-6Al-
4V[41,42]butalsoholdsforothermetallicmaterials. Althoughnotdecisive,thisisaclear
advantageforcryogenicapplicationsintermsofreducedheatflowtotheliquefiedgas[43].
Regardingthemarinefield,thecorrosiveenvironmentcallsforspecificcharacteristics
ofthematerialtobeutilized. AISI316hasadequatecharacteristicsatcryogenictemper-
atures [18]. The Korean Register quantifies that tensile strength is more than twice for
AISI 316 and 316L at 20 K with respect to room temperature [44]. This is undoubtedly
convenient,sincesuchmaterialhasawiderangeofestablishedmarine-relatedapplications
anditscostisstillacceptable[45]. ThefactthatitprovesadequateisconfirmedontheSuiso
FrontierLH tanker,whereboththeinnervesselandtheoutercontainmentarerealized
2
utilizingausteniticstainlesssteel[46]. Itisalsoknownthatnitrogen-enrichedstainless
steelalloys,commerciallyknownasNitronic®,offerconsiderablecorrosionresistanceand
tensilestrengththankstotheirnitrogen-enhancedausteniticstability,bothatveryhigh
temperaturesandatcryogenicconditions[47,48]. Hence, thesemightbeconsideredas
alternativestomoreconventionalmaterialswhenaveryharshenvironmentispresent.
Compositematerialshavedistinctivecharacteristics. Atpresent,thesematerialsare
widely used for high pressure storage tanks and lightweight applications. In [49], the
authors report data for various unidirectional epoxy composites, showing that even at
temperaturesofafewKelvins,notonlydotheysufferalmostnodegradationintensile
strength,theyalsoperformbetter. Asanexampleofarealworldapplicationofcompos-
ites,theSuisoFrontieremploysglassfiber-reinforcedplastic(GFRP)fortheinnervessel
saddles[46].
4.2. HydrogenEmbrittlement
Hydrogenembrittlementreferstothemechanisminvolvinghydrogenpenetrationinto
asolidmaterialstartingfromitssurface,aneventthatcanseriouslyreducetheductilityand
loadcapabilityofsusceptiblematerials. Hydrogendiffusesintothemetalgrainboundaries
andformsvoids,whicharepreferrednucleationsitesforcrackpropagationunderload.
AccordingtoNASA[50],hydrogenembrittlementcanbeclassifiedintothreecategories:
• HydrogenEnvironmentalEmbrittlement(HEE)
• HydrogenInternalEmbrittlement(IHE)
• HydrogenReactionEmbrittlement(HRE)
Adistinctionamongthesecategoriesbasedoncompetingfactorsisreportedin[45].
Usually, this phenomenon is represented in terms of the HEE index, namely a non-
dimensional parameter which equals unity when HE has no influence and decreases
asmuchasthematerialisaffected.
AsconfirmedbyNASA[50],hydrogenembrittlementisparticularlyenhancedunder
veryhighpressures,sincethenaturaltendencyofhydrogentoescapethroughthemetallic
lattice is enhanced by the pushing effect of the pressure and promotes HEE effects at
the tip of a propagating crack. For materials exposed in an aqueous environment, a
degradationmechanismknownasStressCorrosionCracking(SCC)mayappear[50]. In
thisphenomenon,materialatthecracktipisremovedbyacorrosiveprocesscausedbyan
aqueousenvironmentorcontactwithmoisture,enhancingcrackpropagationandpossible
relatedfailure. Infact,thisprocessistypicalofmaterialswithlowcorrosionresistance,
suchasaluminumalloys,whilesteelsandcorrosion-resistantmetalsarelessprone[50].
Theeffectofcryogenictemperaturesonhydrogenembrittlementisstillnotcompletely
clear. AccordingtoNASA[51],rapidcoolingofametalfromhigherthanambienttoroom
temperaturecanresultinIHEduetothereducedhydrogensolubilityatambientconditions.
ThisappearstoberelevantforLH ,e.g.,duringbunkeringortankrefill. However,itisnot
2

J.Mar.Sci.Eng.2025,13,1748 11of22
clearwhethercoolingfromambienttocryogenictemperaturesenhancesHE.Furthermore,
instablecryogenicconditionsthematerialislesspronetohydrogenpenetrationintothe
metal lattice due to the reduced mobility of hydrogen [51]. The idea that hydrogen’s
mobilityisexceptionallylowatcryogenictemperaturesissharedamongotherauthors[51].
NASAresearchers[50]observedthatHEEismostseverenearroomtemperatureor
slightlylower. Thiscanbeexplainedasfollows: atverylowtemperatures,thediffusivity
of hydrogen is too sluggish to fill a sufficiently high number of vacancies in the lattice,
but at high temperatures, hydrogen mobility is enhanced, and trapping is diminished.
For advanced metal alloys, the minimum of the HEE index is moved toward higher
temperatures. TheaforementionedAISI316exhibitsamaximumdecreaseinHEEindex
(bysome30%)ataround−73◦C[50]. Anotherinterestingresultisthatapreciserange
ofnickelcontent(13–33%)inthealloyexistsforthematerialtobeespeciallyresistantto
embrittlement;thisisapparentlyvalidforbothsuperalloysandstainlesssteels[50].
TheAmericanInstituteofAeronauticsandAstronautics(AIAA)hasdefinedaranking
ofmetallicmaterialsthatbestresisthydrogenembrittlement[51].Thisrankingalsoincludes
some composite materials and polymers. It appears that most of the metal alloys are
sufficientlyresistanttohydrogenembrittlement,whileonlyacoupleofpolymerssustain
hydrogen-richenvironments[51].
Inconclusion,aluminumalloysandausteniticstainlesssteelappeartobesufficiently
capableasfueltankmaterialforcryogenichydrogenservice. Thechoicebetweenthem
dependsonotherparameterssuchasfatigueresistance,mechanicalresistance,andthermal
conductivity. Withthefocusonmaritimeuses, itisevidentthatresistancetocorrosion
is an additional requirement. This might suggest austenitic steels, in particular AISI
316 (or X5CrNiMo17-12-2 as per the European designation) or its low-carbon version
(316LorX2CrNiMo17-12-2),whicharebothalreadywellknowntothemaritimeindustry.
Alternatively,titaniumalloysandnickelalloysareequallysuitableforuseincryogenic
temperature,butsufferfromenhancedhydrogenembrittlementowingtotheconfiguration
oftheircrystallatticeandtheircostissignificantlyhigher.
4.3. InsulationofCryogenicTanks
Cryogenictanksrequirehigh-performanceinsulationtopreventheattransfertoward
thebulkliquid. SincetheTRLofcryogenictanksisincreasing,researchpushestoward
betterandbetterinsulationtechniques,asprovenbyafewEuropeanProjectsinvestigating
novelsolutionsforLH tankinsulation[52]. Asageneralconsideration,everycryogenic
2
tank today available has both active and passive insulation. Active insulation consists
ofadoublelinerarrangementinwhichavacuumiscreatedinbetweenlayerstoreduce
thethermalconductivity. Sincethisishardlysufficienttoguaranteeacceptablethermal
flux, further passive insulation technologies are adopted. In this scope, some methods
appeartobethemostpromisingforfuturetechnologicaldevelopment[53]. Experimental
valuesfortheoverallthermalconductivityofpassiveinsulationtechnologiesarefound
in[54]dependingonvacuumpressure;theresultswereobtainedusingliquidnitrogenasa
cryogenmedium. Table5containsasummaryofthepossibleinsulationmethodsthatare
applicabletoLH tanks.
2
Multi-layer insulation is undoubtedly the readiest technology for cryogenic tank
insulation,andalsothemostwidespread[53].Italsoappearstobealsothemostsuitablefor
maritimefueltankscontainingLH ,consideringtheirgoodperformance,theirsimplicity,
2
andtechnologicalreadinesslevel.
Avapor-cooledshieldconsistsofathermalshieldfromtheenvironmentcreatedby
allowing the cold BOG to flow around the tank. In case of marine applications, and in
generalwhereverBOGmaybeusedforpowergeneration,aVCScouldbeaninteresting

J.Mar.Sci.Eng.2025,13,1748 12of22
solutiontosimultaneouslymaintainingthebulkliquidatcoldtemperaturesandexploiting
theBOG,possiblyincombinationwithpara-orthoconversion[14].
Table5.Overviewofthemostcommoninsulationmethodsforliquefiedgastanks.
Insulation Reference Comment
Combinesreflectivelayersandspacerstoreduce
Multi-LayerInsulation(MLI) [53–55] heattransfer.Widelyusedandreadily
applicableforcryogenictanks.
Spray-onFoam(SOFI) [53]
EffectiveforLNG,butimpracticalforLH2
marineuseduetorequiredthickness.
UsesBOGtocooltank.WorkswellwithMLI,
Vapor-cooledShield(VCS) [14,55,56] especiallyinmaritimesystems.Performanceis
enhancedwithpara-orthocatalysis.
Durableandvacuum-insensitive.Random
Glassmicrospheres [53,56,57]
packingreducesidealperformance.
Lightweight,lessdurable.UsedinlargeLH2
Perlitepowder [53,58] sphericaltanksliketheonereceivingtheSuiso
Frontierpayload.
Verylightbutcostly.Limitedtoresearch-scale
Aerogels [53,54]
cryogenicuse,noknownindustrialapplications.
Themainconcernaboutglassmicrospheresistheirbrittleness,althoughthespheresdo
notusuallyfailduetovibrationorthermalcycling[57]. Moreover,theirperformanceisnot
affectedbyvacuumlossorvacuumpressurevariations[53]. Theoretically,aface-centered
cubicarrangementmaximizestheinsulationpotential,sincethesphereshavetheleasttotal
contactareaperunitvolume[57]. Inpractice,thespheres’arrangementisrandom,and
thereislittlechancetocontroltheiractualdisposition.
Perlitepowderislighterbuthasahigherthermalconductivitythanglassmicrospheres.
Italsohasincreasedfragilityandislessresistanttothermalcycles[50]. Perlitepowderhas
alreadysomelargesizeapplications(>3m3)forliquidnitrogen[58]. Aerogelshavevery
lowdensity,buttheirthermalconductivityissomewhathigherthanglassmicrospheresand
perlitepowder[53]andtheyareextremelyexpensive. Today,theirapplicationislimitedto
researchscalecryogenictanks[56].
5. SafetyAspectsforLH : PrecautionsandRecommendations
2
Cryo-fuelutilizationasalternativemarinefuelposesseveresafetyissues,especially
withLH2ascomparedtoLNG.Land-basedliquidhydrogenstorage,handling,andutiliza-
tionisthoroughlyregulatedbyseveralprominentinstitutes(ISO,NASA,etc.) andprecise
prescriptiverulesorregulationsareinplace. Sincethisisnotyetthecasefortransports
ingeneral, andspecificallyforthemaritimesector, thereisstillavastspacetobefilled
withstandardsforthefuturerealizationofhydrogen-poweredships. Moreover,timelines
of estimated maturity level seem to convey the idea that the biggest hurdle is indeed
representedbyregulatoryimmaturityratherthanatechnologicalunderdevelopment[8].
Thesedays,projectapprovalandcertificationfollowsaprocessbasedonequivalent
risk. This so-called Alternative Design (AD) approach requires the risk to be as low as
reasonably possible (ALARP) or, in other words, quantitatively equal to that of ships
designedunderstandardprescriptions[59]. Itseemsclearthatitcannotbeemployedasa
standardforhydrogen-fueledships,sinceitwouldcreateanunsustainablycomplicated
process (HAZID, HAZOP, explosion analysis, quantitative risk analysis etc.) with low
repeatability. However, in a first tentative phase the AD assessment process is more
flexible than prescriptive rules. Hence, insofar as the authority’s requirements are met,
a certain freedom is left to designers [59]. As previously mentioned, LNG aspects are
dealtwiththroughanestablishedsetofrulesandguidelines. Althoughithasmorethana
fewsimilaritiestoLNG,liquefiedhydrogenalsopresentsnumerousdifferentandmore
challengingissuestodealwith.Someresearcherstriedtosummarizeacomparisonbetween
LNG and LH in terms of practical aspects, further assessing their main criticalities, as
2

J.Mar.Sci.Eng.2025,13,1748 13of22
reported in Table 6 [60]. It is confirmed that LH still faces major criticalities, and the
2
comparisonisunfavorableundermanyaspects.
Table6.SummarycomparisonbetweenLNGandLH intermsofpracticalfeasibility.“LNG”:the
2
givencharacteristicconstitutesanadvantageforLNG.“LH ”:thegivencharacteristicconstitutesan
2
advantageforLH .“0”:thechallengesaresimilarforthetwofuels.Adaptedfrom[60].
2
Property LH2vs.LNG Comment
Reactivitywithmaterials LNG
Higherreactivity.H2requireshighquality
materials.
Heatcapacity LH2
LH2hashigherh
li
e
q
a
u
t
i
c
d
a
s
p
t
a
o
c
r
i
a
ty
g
,
e
advantageousin
Asaconsequenceoflowertemperatures(provided
Heatfluxfromthesurroundings LNG
equalinsulation)
Flammableconditionsaremoreeasilyformedwith
Flammabilityrangeinair LNG
hydrogen
HydrogencloudsaremoreeasilyignitedthanNG
Ignitionenergy LNG
clouds
Naturalgashasslightlyhigherignition
Ignitiontemperature LNG/0
temperature
Liquidphase∆Tbetween1and10bar LNG
13◦Cvs.30◦C(seeTable4).Requiresmore
efficientcontrolofheatleakage
Higherforhydrogen,i.e.,greaterriskofspreading
Laminarflamespeedinair LNG
fire
Bothhavedensityhigherthanairatnear
Densephasebehaviorofleakages LH2/0 condensationtemperature,buthydrogentendsto
escapefaster
Inthescopeofthemaritimesector,theInternationalMaritimeOrganization(IMO)has
twosetsofguidelinesthatarerelevanttoLNGandLH : theIGC-codeandtheIGF-code.
2
Theseregulatethedesignofashipforcarryingliquefiedgasesinbulkandshipspropelled
bylow-flashpointfuels,respectively.
In addition to that, since hydrogen is not specifically described as a cargo in the
IGC Code, in 2016 IMO issued the Interim Recommendation for Carriage of Liquefied
HydrogeninBulk,MSC.420(97)[61]. Thisdocumenthasbeenupdatedeversince,anda
morerecentamendmentisexpectedtobeissuedasaresultoftheCommitteeonCarriageof
CargoesandContainers(CCC)resolution. Themainrecommendationsregardtheinerting
ofhazardousspaces(tankconnectionspaceandfuelpreparationroom),devotingparticular
attentiontoallowtheubicationoffueltanksandfuellinesinanenclosedsub-deckspace
rather than on the open deck. The inerting of enclosed spaces and the purging of the
pipingaftermaintenanceofthelinesaretwocrucialtasksforthesafetyoftheship. As
discussed in the following, LH enclosed storages set a unique condition owing to its
2
extremethermodynamicconditions.
5.1. InertizationofEnclosedSpaces
It is clear that flammability limits strongly vary with respect to temperature and
pressure of the enclosure [62]. However, the available data almost always applies to
ambient conditions or high temperatures [63]. However, the following considerations
mightbedrawn:
• AdecreaseinpressurecorrespondstoanincreaseinLFL,adecreaseinUFL,andan
increaseinminimumignitionenergy. Thus, sub-atmosphericpressuresarebenefi-
cial[64],buttheeffectisnotappreciablefromasafetypointofview.
• Highertemperaturesincreasetheflammabilityrange(lowerLFLandhigherUFL).
ThebehavioroftheH /airmixtureatcryogenictemperaturesisstillnotclear,butthe
2
flammabilityrangeisexpectedtoreduce. Someauthorshaveconcludedthatat100K
(−173◦C)theflammabilityrangeofhydrogenisnarrower,butagain,notappreciably
forsafetyconcerns[64]. Fromthisperspective,cryogenicstoragedoesnotrepresent
anenhancedsafetymeasurewithrespecttopressurizedgaseousstorage.

J.Mar.Sci.Eng.2025,13,1748 14of22
Theinertingofexplosiveatmospheresisachievedbyintroducinginertgasessuchas
nitrogen,helium,argon,orcarbondioxide. Severalworkshaveexploredtheeffectiveness
ofdifferentinertgasesandconcludedthat,takingthemaximumexplosionpressureand
maximumrateofpressureriseasindicators,theeffectivenessofinertgasesonconfined
hydrogenexplosioninhibitionrankedfromstrongtoweakisCO ,N ,Ar,andHe[51,65,66].
2 2
Others confirmed the trend without assessing CO but including laminar flame speed
2
influence[67]. In[51],steamisalsoassessedasinert,butitisstraightforwardtoobserve
thatthisisnotviableatcryogenictemperatures. Besides,nosafetyprovisionevensuggests
whichinertinggasisthemostappropriateformarineapplication,irrespectiveofthestorage
conditions. The authors in [51] also report the best diluent for each tube configuration:
seemingly,widetubesandlargespacesbenefitfromCO utilization,butnoconsideration
2
onthethermodynamicconditionsismade.
Thebesttheoreticalsolutionfromathermodynamicalperspectivecouldbehelium:
having the lowest boiling point, this substance is gaseous even at −253 ◦C. However,
heliumhasahighercostascomparedtotheothers,cannotbeproducedonboard,andits
storageinlargevolumesmaybeanti-economical. InertinghazardousspaceswithCO
2
causesnoissuesifthehydrogenisincompressedformandiftheinertedspacesarenot
accessiblebypersonnel[51]. Seemingly,thebestchoiceremainsnitrogenevenforLH ,
2
providedthatcondensedN iscollectedinaninsulateddriptray,evacuatedfromtheroom,
2
anddisposedof[51]. Itisalsoobservedthatnitrogencondensationorsolidificationcan
occuronlyintheeventofdirectcontactwithliquefiedhydrogen[55],whichcanoccuronly
incaseofahydrogenleakinliquefiedform.
WithreferencetoLH leakage,aresearchstudyconductedbySANDIALaboratories
2
discoveredthathydrogenescapesassuperheatedgasonlyforstoragepressureshigher
thanaround7bar; otherwise, italwaysconsistsofatwo-phaseleak[67]. Theaffecting
parametersaretheubicationoftheleakage(saturatedvapororsaturatedliquid)andthe
localtemperatureclosetotheleakage. Theleakageswhichreachthefurthesthazardousdis-
tanceintermsofLFLaretheonesoriginatingfromliquidbulkatlowstoragepressure[67].
SomeauthorstheoreticallyappliedtheIGFCode’sAlternativeDesignspecificationsfor
ashort-seahighspeedhydrogenferry[68]employingCGH storedat250barinTypeIV
2
cylinders,assessingtheriskassociatedtothefollowingitems: storagetank,highpressure
piping,lowpressurepiping,engine,andventmast. Theyfoundthattheestimatedrisk
relatedtothehydrogensystemisverylow,andmuchlowerthantheacceptablerisklevel
relatedtohydrogen(twoordersofmagnitude).
5.2. Pre-NormativeResearchOutcomesandAssociatedRisk
ExtensiveworkhasbeenconductedintheframeworkofthePRESLHYproject[64,69].
TheriskeventsassociatedwithLH systemfailurecangenerallybeclassifiedbasedon
2
fireoccurrence(ignited/unignited)orimmediate/delayedcombustion. Releasesfroman
LH tankcouldalsobesinglephaseormulti-phase. Inthecontextofmaritimeoperations,
2
itshouldbepointedoutthatscenariosinvolvingthereleaseofliquidhydrogenwithin
sub-deckenclosuresarelikelytobeofminimalconcern. Thisisconfidentlytruebecause
suchanoccurrenceistobeavoidedinthefirstplace,sincetheassociatedlosspotentialis
veryhighandcouldpossiblyleadtoanunacceptablerisklevel.
Table7reportsthemainriskeventsthatanLH systemcanundergo. Itappearsthat
2
themostprobableoutcomesareeitherunignitedreleases,bothinformofpoolspilland
two-phasejets,andignitedevents,i.e.,poolfireandjetfire. BLEVEisusuallyevaluated
under the assumption of complete burning of the whole tank content, which is overly
conservativeasdemonstratedbyexperiments[70]. PPPonlyoccursinenclosedspaces,
andonlyiftheH leakissufficientlylarge[71].
2

J.Mar.Sci.Eng.2025,13,1748
15of22
Table7.OverviewontypicalfailureconsequencesofLH systems,characteristics,andoutcomes.
2
| FailureConsequence |     | Characteristics |     | Reference |     |     | Comment |     |
| ------------------ | --- | --------------- | --- | --------- | --- | --- | ------- | --- |
LH2spillsformrapidlyvaporizingpoolswith
Liquidpoolrelease Unignited [72–74] behaviordependentonsurfacetype,lasting
generally<5sonsolidground.
LargeLH2releasescanformdensevaporplumes
neargroundbeforebuoyancydominatesdueto
| Plume/jetrelease |     | Unignited |     | [75] |     |     |     |     |
| ---------------- | --- | --------- | --- | ---- | --- | --- | --- | --- |
convectiveheatingfromthegroundandairmixing.
Verylikelyoccurrence.
Occurswithoutcombustionfromsuddenboiling
Rapidphasetransition(RPT) Unignited,delayed [70,76,77] duetovaporfilmcollapse.ItismorelikelyinLH2
releasesinoronwater,wheredensityislowand
heatcapacityishigh.
Initiallyconduction-dominated,then
convection-dominated.Largerpoolsshowing
| Poolfire |     | Ignited,rapidordelayed |     | [73,78,79] |     |     |     |     |
| -------- | --- | ---------------------- | --- | ---------- | --- | --- | --- | --- |
higherbutpossiblyfragmentedburnratesandrisk
ofsecondaryexplosionpost-ignition.
Ignitedcryogenicjetreleasesgeneratehigh
radiativeheatflux.Usuallyoriginatefromignition
| Jetfire |     | Ignited,rapid |     | [80,81] |     |     |     |     |
| ------- | --- | ------------- | --- | ------- | --- | --- | --- | --- |
ofaplumerelease.Verylikelytooccuras
escalationfromaplume/jetrelease.
Lowinitialtemperaturesreducethelikelihoodof
Deflagration/
Ignited,delayed [82,83] detonationbylimitingtheflameaccelerationdue
| Detonation |     |     |     |     |     | tolowerZeldovichnumber. |     |     |
| ---------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
Resultsinfiresforminglargefireballs,withsize
scalingas
BLEVE Unignited,delayed [67,70] D∝m0.45duetoprolongedevaporation.Notas
typicalasaconsequencebecauseriskmagnitudeis
usuallyoverestimated.
OccursduringventilatedindoorLH2releases,
PressurePeakingPhenomenon(PPP) Unignited/ignited [71,84–86] whereventsizeandenclosurevolumeinfluence
pressurepeakanddelay.Releaseratehasaminor
influenceonpressurepeaking.
Itisknownthatthereexistascarcityofdataandgeneralexperiencewithhydrogen
release,especiallyLH . Therefore,itisimportanttoidentifywhatarethemostprobable
2
incidents or accidents, both in terms of causes and outcomes. In [72] were identified
287occurrencesanditwasconcludedthat:
|     | •   | Explosionoccursin96%ofGH |     | releasesandabout50%ofLH |     |     | releases. |     |
| --- | --- | ------------------------ | --- | ----------------------- | --- | --- | --------- | --- |
|     |     |                          |     | 2                       |     |     | 2         |     |
• Hotsurfacesconstitutetheignitionsourceinmostcases(21%forGH and11%forLH ).
2 2
• Therewere199injuriesoutof201GH accidentsand10injuriesoutof86LH acci-
2 2
dents.
PRESHLY project identified 18 incidents related to LH2 storage and containment
systemsduringtransportationandliquefaction/storage[64,69]. Thecausesandoutcomes
ofsuchincidentsarereportedinTables8and9,respectively.
Table8.OverviewofthecausesandoutcomesofLH 2 failureeventsduringtransportation.Adapted
from[69].
|     |     | Event | Occurrences |     |     | Event |     | Occurrences |
| --- | --- | ----- | ----------- | --- | --- | ----- | --- | ----------- |
Design/constructionfailure
|     |     | orinadequateHAZID    |     | 0(0%)  |                          | Norelease |     | 2(11%)  |
| --- | --- | -------------------- | --- | ------ | ------------------------ | --------- | --- | ------- |
|     |     | Equipmentfailure     |     | 6(33%) | Accumulationordispersion |           |     | 12(67%) |
|     |     | Incorrectoperationor |     | 8(44%) |                          | Fire      |     | 4(22%)  |
proceduralinefficiency
|     |     | Impactorroadaccident |     | 3(17%) |     | Explosion |     | 1(5%) |
| --- | --- | -------------------- | --- | ------ | --- | --------- | --- | ----- |
|     |     | Naturalcause         |     | 1(5%)  |     | BLEVE     |     | 0(0%) |
Table9.OverviewofthecausesandoutcomesofLH failureeventsduringliquefactionandstorage.
2
Adaptedfrom[69].
|     |                            | Event | Occurrences |     |     | Event     |     | Occurrences |
| --- | -------------------------- | ----- | ----------- | --- | --- | --------- | --- | ----------- |
|     | Design/constructionfailure |       | 12(31%)     |     |     | Norelease |     | 5(13%)      |
orinadequateHAZID
|     |     | Equipmentfailure |     | 8(21%) | Accumulationordispersion |     |     | 14(36%) |
| --- | --- | ---------------- | --- | ------ | ------------------------ | --- | --- | ------- |
Incorrectoperationor
|     |     |     | 18(46%) |     |     | Fire |     | 9(23%) |
| --- | --- | --- | ------- | --- | --- | ---- | --- | ------ |
proceduralinefficiency
|     |     | Impactorroadaccident |     | 0(0%)  |     | Explosion |     | 13(33%) |
| --- | --- | -------------------- | --- | ------ | --- | --------- | --- | ------- |
|     |     | Naturalcause         |     | 5(13%) |     | BLEVE     |     | 1(3%)   |

J.Mar.Sci.Eng.2025,13,1748 16of22
Equipmentfailureincludedunexpectedburstdiskfailure,lossofvacuum,oraloose
flangeconnection. Ofthefivecasesduringtransit,twowererelatedtoroadtrafficaccidents
andtheotherthreeconcernedventingduetoburstdiskfailureand/orlossofvacuum.
Injury to personnel occurred in 3 (17%) cases, 2 of which were cold burns. Property or
equipmentdamageoccurredin7(39%)cases.
Itwasnotedthatoutofsixmajorincidentsinvolvingstoragevessels,threeoccurred
during decommissioning/commissioning (warm-up/cool-down). There were several
incidentswhereunexpectedignitionuponventingoccurred,resultinginfireorexplosion.
Injuryoccurredin3(8%)incidentsandnon-trivialdamagein23(59%)cases.
FromTables8and9itappearsthatmorefailuresoccurduringliquefactionandstorage
ascomparedtocryogenictransportation. Thiscouldbejustifiedassumingthatproduced
LH isnotoftentransported. Moreover,BLEVEseemsnottobeastypicalassuggestedby
2
academic/researchassessments,whichoftenassumethatthewholetankcontentignites
completelyandsimultaneously. Inreality,evenafteratankrupture,LH remainsinliquid
2
formandtheevaporatedfractioniscoldandconcentrated,henceitsignitionisunlikelyto
occurallatonce: asmallflashfireisamorerealisticscenario.
5.3. OpenChallengesforSafeMaritimeHydrogenOperation
WhileinabsenceofarigidregulationitisnotyetpossibletostandardizeH -fueled
2
shipdesign,someconsiderationsonthemostrelevantchallengestobeovercomeforasafe
hydrogenutilizationonboardmaybedrawn.
• Hydrogentankcollocation.TheIGF-codesuggeststhatthetankbeplacedontheopen
decktopreventanexplosiontoinvolvethewholehull. However,forsomelargeships
thisistroublesome,andanencloseddeckubicationisunavoidable. Inthescopeof
MarHySafeproject,aconceptualschemeforenclosedLH storageonboardthoseships
2
wasproposedforallapplicationswhereopendecktanksproveanti-economical[59].It
resultsthatopendecktanksarenotandprobablywillnotbethestandardfordeep-sea
largecruisevessels.
• Preventionofflammablecloudformation. Directlyrelatedtothepreviouspoint,an
enclosedspaceisverylikelytoquicklybecomeanignitablevolume;thus,anadequate
ventilationsystemisnecessary. However,thethresholdof30airchangesperhour
(ACH)proposedbytheIMO’sInterimGuidelinesforSafetyofShipsUsingHydrogen
asFuelsoundstoooptimistic,sinceitisextremelyfarbelowthetheoreticalminimum
forhydrogen[87]. Normally,airflowisselectedtoensurehydrogenconcentrationto
belessthan25%ofthelowerflammabilitylimit,thatis1%v/vhydrogen. Thisisalso
thetypicaltriggeringvalueforhydrogensensors. In[88]itisevaluatedthatafuelcell
enclosureof3m×3m×2mrequiresaround1500ACHtostaybelowasupposedly
safe1%withafull-bore6.2g/sleakagefromtheFCfeedline. Whileitistruethat
inalargeICE/GTpoweredshipgloballyhazardousconcentrationsarereachedina
longerperiodbecauseofthelargerspaces,massflowratesarealsolarger. Toprovidea
concreteexampleofaworst-casescenario,itwasevaluatedthatittakesaround80sto
reachaflammableconcentrationfromafull-boreruptureofa35MW-fuelpipeinside
a15,000m3engineroom. TostayunderhydrogenLFL,thiswouldrequire~45ACH.
Ifthe1%safetymarginscenarioisapplied,thisvalueskyrockets4timeshigher. For
reference,currentengineroomrequirementsforahighlyhazardousfuellikeammonia
aresetat45ACH[89]. However,thelikelihoodofsucheventoccurringisverylow,
thusfromariskassessmentperspectiveitcouldproveirrelevant.
• Inertingoftheenclosures.Asmentioned,inertingiscrucialforsafetyreasons.Theuse
ofnitrogenisstraightforwardforCGH storageandutilizationinenclosedspaces.The
2
problemforLH operationaboutcondensationoftheinertgasisafact,buttheissue
2

J.Mar.Sci.Eng.2025,13,1748 17of22
canbeovercomequiteeasilywithacollectingdrippan,providedthatcondensationor
solidificationdoesnotaffectanyfuelhandlingcomponentornormalengineoperation.
Alternatively, helium can be used as it guarantees a gaseous phase throughout all
operatingtemperatures,butitiscostlyandcannotbeproducedonboardasnitrogen.
However,morepreciseprescriptionsshouldbeissuedregardingthepossibleneedfor
acompletespaceinertization.
• Safeventing. Hydrogenstoragefacilitiesshouldbeequippedwithventingsystems
for both normal operating requirements and emergency situations. Vent lines for
hydrogen(includingpressurerelieflinesandboil-offfromcryogenicsystems)should
beroutedtoasafelocationoutside. Ventlinesarealsousedtodisposeofhydrogen
purgedfromthesystemformaintenance. Theventshouldbedesignedtoprevent
moistureoricefromaccumulatingintheline,tobesafelyinerted,andshouldhave
acrosssectionlargeenoughtoaccommodatetheventedmassflowwithoutchoking
occurrences. NFPA2establishesthatthedischargemustbeatleast3maboveany
adjacentequipmentandawayfrompersonnelareas,airintakes,andoverhangs[88].
AccordingtoNASA/AIAA,flaringmaybeconsideredforhydrogenventrateslarger
than0.2kg/s[90].
• Explosionprotection. Inside confined spaces, the explosion risk is one of the most
relevant. Explosionsshouldbeavoidedatalltimesbyensuringasufficientventilation
thatpreventstheaccumulationofflammablemixtures. Incasesafetymeasuresarenot
sufficienttoavoidanexplosion,thecontainmentshouldbedesignedinsuchaway
thatthewallsarecollapsibleenoughtoreleasethepressurewavetowardtheoutside
withnoorminimalharmtopeople.
• Fireprotection.Hydrogenfiresareverydifficulttodetectbecauseahydrogenflameis
colorless.Forthisreason,specificflamesensorsandtemperaturesensorsareparamount.
However, any ignition source should be eliminated or confined. Walls must be fire-
compliant (A-60 class), and an extinguisher fluid must be provided. Given the fast
combustionreaction,ineventofahydrogenfirethemosteffectiveactionistosuppress
thehydrogensourceratherthansuffocatetheflame.Thisisespeciallytrueineventofjet
fires,whileflashfiresandBLEVEsarelesspredictableandeasiertoextinguish.
6. Conclusions
Inthescopeofmaritimedecarbonizationthroughutilizationofalternativefuels,itis
undoubtedthatthematuritylevelofLH storageandhandlingsystemsislowascompared
2
toitsLNGcounterpart. Despitethepossibilityofexploitingthevastexperienceaccumu-
latedwithLNGintermsofcryogenicstorage,BOGhandling,andspacearrangement,the
practicaldesignofLH handlingsystemsrequirestailoredsolutions.
2
First, theproblemofcryogenicstorageisaddressed, concludingthatLH requires
2
higherperforminginsulationandbetterthermalmanagementthanLNG.Furthermore,
pressurizedliquidstoragedoesnotincreaseremarkablytheboilingpoint,thusboil-offis
notreducedsignificantly. IncontrasttoLNG,intheframeworkofamarineapplication,
hydrogenboil-offreliquefactionisstilleconomicallyunviable,evenforlargebulkcarriers.
Hence,fromtheeconomicpointofviewthebestsolutionistheutilizationoftheBOGfor
directpowerproductionpurposeswheneversafelypossible.
Thereviewofsuitablematerialsforhydrogenstorageconcludedthatmetallicma-
terials,whicharealreadywidelyemployedonboard,mayalsobeeffectivelyusedwith
cryogenicfuels. Forinstance,aluminumalloysandAISI316and316Lstainlesssteelsretain
morethansufficientmechanicalfeaturesevenatverylowtemperatures. Ontheotherhand,
theuseofaluminumalloysisconsideredinappropriateduetotheirlimitedresistanceto
thecorrosiveeffectstypicalofmarineenvironments. Theenhancedweightefficiencyof

J.Mar.Sci.Eng.2025,13,1748 18of22
aluminumalloysmakesthemparticularlywell-suitedforapplicationsinaircraft. Moreover,
cryogenicconditionsseemnottoperceivablyenhancehydrogenembrittlementonthema-
terial,whichhoweverremainsaseriouschallengethathindershydrogenuptake. Further
researchisrequiredoncomposites’andpolymers’sensitivitytohydrogenembrittlement.
Insulationtechniquesareadvancedenoughtoguaranteesufficientperformancefor
maritimeLH fueltanks,wheretheneedforincreaseddormancyisnotascriticalasinthe
2
caseoflargescalelandstorage. However,somesolutionshavethepotentialtomitigate
heatdispersionwithrelativelysimplearrangements.
Despitethelackofalargenumberoftestcases,researchonsafetyisprovidingmore
andmorevaluableresults,highlightingthatonlysomeriskeventsarereallypertainingto
actualLH equipment. Asageneralconclusion,behaviorofLH releasesdependsonthe
2 2
massleakedfromthetank. Iftheleakedmassislimited,theleakagetendstoevaporate
quicklyanddisperse,possiblyignitinginthepresenceofsufficientenergy,whilealarge
mass of liquid is prone to stratify giving rise to pools of slowly evaporating hydrogen.
Themostprobablehazardouseventsareexplosionanddelayedflashfire,whileBLEVEis
muchlesscriticalthanexpectedfromresearchoutcomesbecausetheactualconditionsare
generallylessseverethanphysicalassumptions.
Safety is allegedly the most relevant concern for hydrogen storage and utilization
onboardships.TheaimistosurpasstheAlternativeDesigninfavorofamorestandardized
designprocess. Themainrisksarelinkedtotheformationofflammablemixturesincase
ofafuelleak,owingtothehightendencyofhydrogengastoescapeandquicklyfillany
enclosedvolume. Forthesereasons,adequateventilationshouldbeprovided,ventcircuits
mustbepresent,andadequatelysizedand,asalastoptionifexplosionisunavoidable,
wallsshouldopposetheblastwithaslittleresistanceaspossible.
Finally,notwithstandingthetechnologicalmaturityofhydrogen-readymaritimesys-
temsbeingatalowlevelincomparisonwithtraditionalpropulsionorgenerationsystems,
the absence of a developed market with particular regard to LH handling systems is
2
anothercrucialaspectthathindershydrogenuptaketowardzero-emissionpowergener-
ation. Itisoftheutmostimportancethatthetechnicalandregulatoryadvancementsin
thisdomainareaccompaniedbyadefinitivecommitmentfromallstakeholderstowardthe
developmentanddeploymentofzero-emissionpowersystems.
AuthorContributions:Conceptualization,M.P.andA.T.;validation,A.T.;formalanalysis,investiga-
tion,resources,datacuration,M.P.;writing—originaldraftpreparation,M.P.;writing—reviewand
editing,A.T.;supervision,M.P.;projectadministration,A.T.;fundingacquisition,A.T.Allauthors
havereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Nonewdatawerecreatedoranalyzedinthisstudy.
Acknowledgments:ActivitiesdescribedinthispaperhavebeendevelopedwithinFincantieriproject
“Wave2theFuture”(W2F),fundedbytheEuropeanUnion—NextGenerationEU.W2Fprojectispart
ofIPCEIHy2Tech.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
Abbreviations
ACH AirChangesperHour
AD AlternativeDesign
AIAA AmericanInstituteofAeronauticsandAstronautics
ALARP AsLowAsReasonablyPossible

J.Mar.Sci.Eng.2025,13,1748 19of22
BOG Boil-offGas
BOR Boil-offRate
BLEVE BoilingLiquidExpandingVaporExplosion
DBTT DuctiletoBrittleTransitionTemperature
DNB DeparturefromNucleateBoiling
DDT DeflagrationtoDetonationTransition
GT GasTurbine
GFRP GlassFiber-ReinforcedPlastic
GHG GreenhouseGas
HGM HollowGlassMicrospheres
HEE HydrogenEnvironmentalEmbrittlement
HRE HydrogenReactionEmbrittlement
ICE InternalCombustionEngine
IHE InternalHydrogenEmbrittlement
IMO InternationalMaritimeOrganization
LH LiquefiedHydrogen
2
LNG LiquefiedNaturalGas
LOHC LiquidOrganicHydrogenCarrier
LFL LowerFlammableLimit
LHV LowerHeatingValue
MAWP MaximumAllowableWorkingPressure
MDO MarineDieselOil
MGO MarineGasolineOil
MLI Multi-LayerInsulation
PBU PressureBuildupUnit
RBC ReverseBraytonCycle
SEC SpecificEnergyConsumption
SOFI Spray-OnFoamInsulation
TRL TechnologyReadinessLevel
UFL UpperFlammableLimit
VCS VaporCooledShield
References
1. Ustolin,F.;Campari,A.;Taccani,R.AnExtensiveReviewofLiquidHydrogeninTransportationwithFocusontheMaritime
Sector.J.Mar.Sci.Eng.2022,10,1222.[CrossRef]
2. Elkafas,A.G.;Rivarolo,M.;Gadducci,E.;Magistri,L.;Massardo,A.F.FuelCellSystemsforMaritime:AReviewofResearch
Development,CommercialProducts,Applications,andPerspectives.Processes2023,11,97.[CrossRef]
3. InternationalEnergyAgency(IEA).GlobalHydrogenReview;InternationalEnergyAgency:Paris,France,2024.
4. Al-Breiki,M.;Bicer,Y.LiquifiedHydrogenvsLiquefiedRenewableMethane:Evaluatingenergyconsumptionandinfrastructure
forsustainablefuels.Fuel2023,350,128779.[CrossRef]
5. Kanbur,B.B.;Xiang,L.;Dubey,S.;Choo,F.H.;Duan,F.ColdutilizationsystemsofLNG:Areview.Renew.Sustain.EnergyRev.
2017,79,1171–1188.[CrossRef]
6. Korpys,M.;Wojcik,J.;Synowiec,P.Methodsforsweeteningnaturalandshalegas.Chemik2014,68,211–215.
7. Milojevic´,S.;Stopka,O.;Orynycz,O.;Tucki,K.;Šarkan,B.;Savic´,S.ExploitationandMaintenanceofBiomethane-PoweredTruck
andBusFleetstoAssureSafetyandMitigationofGreenhouseGasEmissions.Energies2025,18,2218.[CrossRef]
8. LNGContainmentSystems: FindingtheWayforTypeA.Availableonline: https://www.dnv.com/expert-story/maritime-
impact/LNG-containment-systems-finding-the-way-for-Type-A.html(accessedon17July2023).
9. Mokhatab,S.;Mak,J.Y.;Valappil,J.V.;Wood,D.A.HandbookofLiquefiedNaturalGas;Elsevier:Oxford,UK,2014.
10. Lemmon,E.W.;Bell,I.H.;Huber,M.L.;McLinden,M.O.NISTStandardReferenceDatabase23:ReferenceFluidThermodynamicand
TransportProperties-REFPROP,Version10.0;NationalInstituteofStandardsandTechnology,StandardReferenceDataProgram:
Gaithersburg,MD,USA,2018.[CrossRef]
11. Zhang,T.;Uratani,J.;Huang,Y.;Xu,L.;Griffiths,S.;Ding,Y.Hydrogenliquefactionandstorage:Recentprogressandperspectives.
Renew.Sustain.EnergyRev.2023,176,113204.[CrossRef]

J.Mar.Sci.Eng.2025,13,1748 20of22
12. Peng,J.K.;Ahluwalia,R.K.Enhanceddormancyduetopara-orthohydrogenconversionininsulatedcryogenicpressurevessels
forautomotiveapplications.Int.J.HydrogenEnergy2013,38,13664–13672.[CrossRef]
13. Shi,C.;Zhu,S.;Wan,C.;Bao,S.;Zhi,X.;Qiu,L.;Wang,K.Performanceanalysisofvapor-cooledshieldinsulationintegratedwith
para-orthohydrogenconversionforliquidhydrogentanks.Int.J.HydrogenEnergy2023,48,3078–3090.[CrossRef]
14. Leng,Y.;Zhang,S.;Wang,X.;Pu,L.;Xu,P.Comparativestudyonthermodynamicperformanceofliquidhydrogenstorage
insulationsystemincorporatingvapor-cooledshieldwithpara–orthohydrogenconversionbyone-dimensionalandquasi-two-
dimensionalmodel.EnergyConvers.Manag.2024,321,119068.[CrossRef]
15. Aasadnia,M.;Mehrpooya,M.Large-scaleliquidhydrogenproductionmethodsandapproaches:Areview.Appl.Energy2018,
212,57–83.[CrossRef]
16. Bi,Y.;Ju,Y.DesignandanalysisofanefficienthydrogenliquefactionprocessbasedonHeliumreverseBraytoncycleintegrating
withsteammethanereformingandliquefiednaturalgascoldenergyutilization.Energy2022,252,124047.[CrossRef]
17. Song,Q.;Tinoco,R.R.;Yang,H.;Yang,Q.;Jiang,H.;Chen,Y.;Chen,H.Acomparativestudyonenergyefficiencyofthemaritime
supplychainsforliquefiedhydrogen,ammonia,methanolandnaturalgas.CarbonCaptureSci.Technol.2022,4,100056.[CrossRef]
18. Kim,S.;Oh,S.;Kang,S.Techno-economicassessmentofliquefiedhydrogentankershipsutilizingvariouspropulsionsystems.
EnergyConvers.Manag.2025,336,119895.[CrossRef]
19. FincantieriandVikingAnnouncetheWorld’sFirstHydrogen-PoweredCruiseShip.Availableonline:https://www.fincantieri.
com/en/media/press-releases/2025/fincantieri-and-viking-announce-the-world-s-first-hydrogen-powered-cruise-ship-and-
sign-contracts-for-two-new-units(accessedon1August2024).
20. AirbusZEROe:OurHydrogenPoweredAircraft.Availableonline:https://www.airbus.com/en/innovation/energy-transition/
hydrogen/zeroe-our-hydrogen-powered-aircraft(accessedon1August2024).
21. GroundOperationofLiquidHydrogenAircraft(GOLIAT).EUHorizon2020.Availableonline:https://cordis.europa.eu/project/
id/101138379(accessedon1August2024).
22. RollsRoyce,Hydrogen.Availableonline:https://www.rolls-royce.com/innovation/net-zero/decarbonising-complex-critical-
systems/hydrogen.aspx/1000(accessedon1December2024).
23. Zhang,C.;Yu,G.;Liang,Y.;Ling,G.Explorationandperformanceassessmentofrecuperatedrotorcraftpowerplantutilizing
hydrogenasfuel.EnergyConvers.Manag.2025,336,119872.[CrossRef]
24. WartsilaMarineSolutions.LNGShippingSolutions2Gas:AGreenSolution;WartsilaMarineSolutions:Helsinki,Finland,2017.
25. MANES.MANCryoCryogenicSolutionsforOnshoreandOffshoreApplications.Availableonline:https://www.man-es.com/
docs/default-source/document-sync-archive/man-cryo-eng.pdf?sfvrsn=f1030ce2_3(accessedon8November2023).
26. Cryostar.ReciprocatingPumps.Availableonline:https://cryostar.com/reciprocating-pumps/(accessedon1August2024).
27. NikkisoCEIG.ReciprocatingPumpSVG.Availableonline:https://www.nikkisoceig.com/product/sgv/(accessedon1August2024).
28. CHARTIndustries.Availableonline:https://www.chartindustries.com/(accessedon1August2024).
29. MANCryoSuppliesFuelSystemforWorld’sFirstHydrogen-PoweredSuperyacht.Availableonline:https://www.man-es.com/
docs/default-source/press-releases-new/pr-feadship_h2_en.pdf?sfvrsn=a007b9e0_1(accessedon24July2024).
30. Wartsila.WartsilaandRINAPartnerwithStakeholderstoDeliveraViableHydrogenSolutiontoMeetIMO2050Target.Available
online:https://www.wartsila.com/media/news/25-11-2021-wartsila-and-rina-partner-with-other-stakeholders-to-deliver-a-
viable-hydrogen-fuel-solution-to-meet-imo-2050-target-3013516(accessedon5December2023).
31. DNV.MaritimeForecastto2050;DNV:Bærum,Norway,2022.
32. Migliore,C.;Tubilleja,C.;Vesovic,V.Weatheringpredictionmodelforstoredliquefiednaturalgas(LNG).J.Nat.GasSci.Eng.
2015,26,570–580.[CrossRef]
33. Kwak,D.H.;Heo,J.H.;Park,S.H.;Seo,S.J.;Kim,J.K.Energy-efficientdesignandoptimizationofboil-offgas(BOG)re-liquefaction
processforliquefiednaturalgas(LNG)-fuelledship.Energy2018,148,915–929.[CrossRef]
34. Rivard,E.;Trudeau,M.;Zaghib,K.Hydrogenstorageformobility:Areview.Materials2019,12,1973.[CrossRef][PubMed]
35. HESC—TheSuisoFrontier.Availableonline:https://www.hydrogenenergysupplychain.com/about-the-pilot/supply-chain/
the-suiso-frontier/(accessedon22November2023).
36. Colozza,A.J.HydrogenStorageforAircraftApplicationsOverview;NASA:BrookPark,OH,USA,2002. Availableonline: http:
//www.sti.nasa.gov(accessedon1May2024).
37. Kochunni,S.K.;Chowdhury,K.Conceptandevaluationofenergy-efficientboil-offgasreliquefiersinLNGcarriershipspropelled
bydual-fuelengines.Cryogenics2022,123,103453.[CrossRef]
38. Zang,H.;Tang,J.;Qi,M.;He,T.Carnotbatterystoragesystemintegratedwithliquidhydrogencoldenergy:Thermodynamics,
economicanalysisandoptimization.EnergyConvers.Manag.2025,325,119400.[CrossRef]
39. Mazzoni,S.;Rajoo,S.;Romagnoli,A.Aboil-offgasutilizationforimprovedperformanceofheavydutygasturbinesincombined
cycle.Proc.Inst.Mech.Eng.PartAJ.PowerEnergy2019,233,96–110.[CrossRef]
40. Bisio,G.;Massardo,A.;Agazzani,A.CombinedHeliumandCombustionGasTurbinePlantExploitingLiquidHydrogen(LH2)
PhysicalExergy.ASMEJ.Eng.GasTurbinesPower1996,118,257–264.[CrossRef]

J.Mar.Sci.Eng.2025,13,1748 21of22
41. Duthil,P.MaterialPropertiesatLowTemperature.arXiv2015,arXiv:1501.07100.[CrossRef]
42. ASMInternational.AtlasofStress-StrainCurves;ASMInternational:Almere,TheNetherlands,2002.
43. Qiu,Y.;Yang,H.;Tong,L.;Wang,L.Researchprogressofcryogenicmaterialsforstorageandtransportationofliquidhydrogen.
Metals2021,11,1101.[CrossRef]
44. Park,J.;Chun,K.;Lee,T.;Kim,Y.;Kim,J.GuidelinesforSelectionofMetallicMaterialsofContainmentSystemforAlternativeFuelsfor
Ships;KoreanRegister:Busan,RepublicofKorea,2022.
45. Chun,K.W.Technicalguideformaterialsofcontainmentsystemforhydrogenfuelsforships.J.Adv.Mar.Eng.Technol.2022,46,
212–217.[CrossRef]
46. Muragishi,O.;Inatsu,S.;Uraguchi,R.;Yamashiro,K.;Imai,T.;Ohashi,T.;Shimogaki,T.;Yoshida,T.;Koumoto,T.Hydrogen
Transportation-DevelopmentofLiquefiedHydrogenCarrier.Hydrog.Transp.–Dev.Liq.Hydrog.Carr.2021,182,35–40.
47. Nitronic®40StainlessSteel.Availableonline:https://www.electralloy.com/images/pdf/Product_Sheets/Electralloy/Nitronic-
40.pdf(accessedon1May2024).
48. Nitronic®60StainlessSteel.Availableonline:https://www.electralloy.com/images/pdf/Product_Sheets/Nitronic/Nitronic60_
main.pdf(accessedon1May2024).
49. Schutz,J.B.Propertiesofcompositematerialsforcryogenicapplications.Cryogenics1998,38,3–12.[CrossRef]
50. Lee,J.A.HydrogenEmbrittlement;NASA:Huntsville,AL,USA,2016.Availableonline:https://ntrs.nasa.gov/api/citations/2016
0005654/downloads/20160005654.pdf(accessedon1May2024).
51. Gregory,F.D.SafetyStandardsforHydrogenandHydrogenSystems;NASA:Washington,DC,USA,1997.
52. NICOLHy.NovelInsulationConceptsforLiquefiedHydrogenStorageTanks.Availableonline:https://nicolhy.eu/The-Project/
(accessedon1December2024).
53. Yatsenko,E.A.;Goltsman,B.M.;Novikov,Y.V.;Izvarin,A.I.;Rusakevich,I.V.Reviewonmodernwaysofinsulationofreservoirs
forliquidhydrogenstorage.Int.J.HydrogenEnergy2022,47,41046–41054.[CrossRef]
54. Scholtens,B.E.;Fesmire,J.E.;Sass,J.P.;Augustynowicz,S.D.;Heckle,K.W.Cryogenicthermalperformancetestingofbulk-filland
aerogelinsulationmaterials. InProceedingsoftheAIPConferenceProceedings,Chattanooga,TN,USA,16–20July2008;pp.
152–159.[CrossRef]
55. Jiang,W.B.;Zuo,Z.Q.;Huang,Y.H.;Wang,B.;Sun,P.J.;Li,P.Couplingoptimizationofcompositeinsulationandvapor-cooled
shieldforon-orbitcryogenicstoragetank.Cryogenics2018,96,90–98.[CrossRef]
56. Wang,P.;Liao,B.;An,Z.;Yan,K.;Zhang,J.MeasurementandcalculationofcryogenicthermalconductivityofHGMs.Int.J.Heat
MassTransf.2019,129,591–598.[CrossRef]
57. Chan,C.K.;Mem,P.;ASME.ConductanceofPackedSpheresinVacuum.1973.Availableonline:http://asmedigitalcollection.
asme.org/heattransfer/article-pdf/95/3/302/5663791/302_1.pdf(accessedon1November2024).
58. Linde,A.G.DatenblattLITSF2D;TheLindeGroup:Woking,UK,2023.
59. DNV.HandbookforHydrogen-FuelledVessels;DNV:Bærum,Norway,2021.
60. Nerheim,A.R.;Æsøy,V.;Holmeset,F.T.Hydrogenasamaritimefuel–canexperienceswithLNGbetransferredtohydrogen
systems?J.Mar.Sci.Eng.2021,9,743.[CrossRef]
61. InternationalMaritimeOrganization.InterimRecommendationsforCarriageofLiquefiedHydrogeninBulk.MSC.420(97);International
MaritimeOrganization:London,UK,2016.
62. Dwyer,J.;Hansel,J.G.;Philips,T.TemperatureInfluenceontheFlammabilityLimitsofHeatTreatingAtmospheres;AirProductsand
Chemicals,Inc.:Allentown,PA,USA,2003.
63. Pio,G.;Salzano,E.Flammabilitylimitsofmethane(LNG)andhydrogen(LH2)atextremeconditions.Chem.Eng.Trans.2019,77,
601–606.[CrossRef]
64. Verfondern,K.;Cirrone,D.;Molkov,V.;Makarov,D.;Coldrick,S.;Ren,Z.;Wen,J.;Proust,C.;Friedrich,A.;Jordan,T.Handbookof
HydrogenSafety: ChapteronLH2Safety.—Pre-NormativeResearchforSafeUseofLiquidHydrogen(PRES-LHY),ProjectDeliverable
6.1—FCHJUHorizon2020;HySafe:UnionGrove,WI,USA,2020.
65. Li,Y.;Bi,M.;Gan,B.;Yan,C.;Ren,J.;Gao,W.InhibitionofConfinedHydrogenExplosionbyInertGases.InProceedingsofthe
InternationalConferenceonHydrogenSafety,Seoul,RepublicofKorea,24–26September2019.
66. Yang,W.;Zheng,L.;Wang,C.;Wang,X.;Jin,H.;Fu,Y.Effectofignitionpositionandinertgasonhydrogen/airexplosions.Int.J.
HydrogenEnergy2021,46,8820–8833.[CrossRef]
67. Winters, W.S. Modeling Leaks from Liquid Hydrogen Storage Systems; OSTI: Albuquerque, NM, USA, 2009. Available online:
http://www.ntis.gov/help/ordermethods.asp?loc=7-4-0#online(accessedon1December2024).
68. Aarskog,F.G.;Hansen,O.R.;Strømgren,T.;Ulleberg,Ø.ConceptriskassessmentofahydrogenDrivenhighspeedPassenger
ferry.Int.J.HydrogenEnergy2020,45,1359–1372.[CrossRef]
69. PRESHLYEuropeanProject.Horizon2020FCHJU.Availableonline:https://preslhy.eu/(accessedon1March2025).
70. Willoughby,D.;Royle,M.ReleasesofUnignitedLiquidHydrogen,HSLReportXS/11/70;HealthandSafetyExecutive:Bootle,UK,2012.

J.Mar.Sci.Eng.2025,13,1748 22of22
71. VanWingerden,K.;Kluge,M.;Habib,A.K.;Ustolin,F.;Paltrinieri,N.Medium-scaleteststoinvestigatethepossibilityandeffects
ofBLEVEsofstoragevesselscontainingliquifiedhydrogen.Chem.Eng.Trans.2022,90,547–552.[CrossRef]
72. Brennan,S.;Molkov,V.PressurePeakingPhenomenonforindoorhydrogenreleases.Int.J.HydrogenEnergy2018,43,18530–18541.
[CrossRef]
73. Verfondern,K.;Dienhart,B.Poolspreadingandvaporizationofliquidhydrogen. Int. J.HydrogenEnergy2007,32,256–267.
[CrossRef]
74. Ustolin,F.;Giannini,L.;Pio,G.;Salzano,E.;Paltrinieri,N.OntheMechanicalEnergyInvolvedintheCatastrophicRuptureof
LiquidHydrogenTanks.Chem.Eng.Trans.2022,91,421–426.[CrossRef]
75. Cirrone,D.;Makarov,D.;Proust,C.;Molkov,V.Numericalstudyofthesparkignitionofhydrogen-airmixturesatambient
temperatures.Int.J.HydrogenEnergy2024,79,353–363.[CrossRef]
76. Spiegler,P.;Hopenfeld,J.;Silberberg,M.;Bumpus,C.F.;Norman,A.Onsetofstablefilmboilingandthefoamlimit.Int.J.Heat
MassTransf.1963,6,987–989.[CrossRef]
77. Odsæter,L.H.;Skarsvag,H.;Aursand,E.;Ustolin,F.;Reigstad,G.;Paltrinieri,N.LiquidHydrogenSpillsonWater—Riskand
ConsequencesofRapidPhaseTransition.Energies2021,14,4789.[CrossRef]
78. Friedrich,A.;Breitung,W.;Stern,G.;Veser,A.;Kuznetsov,M.;Fast,G.;Oechsler,B.;Kotchourko,N.;Jordan,T.;Travis,J.R.;etal.
Ignitionandheatradiationofcryogenichydrogenjets.Int.J.HydrogenEnergy2012,37,17589–17598.[CrossRef]
79. Babrauskas,V.Estimatinglargepoolfireburningrates.FireTechnol.1983,19,251–261.[CrossRef]
80. Panda,P.P.;Hecht,E.S.Ignitionandflamecharacteristicsofcryogenichydrogenreleases.Int.J.HydrogenEnergy2017,42,775–785.
[CrossRef]
81. Cirrone,D.;Makarov,D.V.;Molkov,V.Cryogenichydrogenjets:Flammableenvelopesizeandhazarddistancesforjetfire.In
ProceedingsoftheInternationalConferenceonHydrogenSafety(ICHS),Adelaide,Australia,24–26September2019.
82. Zabetakis,M.G.SafetywithCryogenicFluids;PlenumPress:NewYork,NY,USA,1967.
83. Makarov,D.;Shentsov,V.;Kuznetsov,M.;Molkov,V.HydrogenTankRuptureinFireintheOpenAtmosphere:HazardDistance
DefinedbyFireball.Hydrogen2021,2,134–146.[CrossRef]
84. Cirrone,D.;Makarov,D.;Lach,A.W.;Gaathaug,A.V.;Molkov,V.ThePressurePeakingPhenomenonforIgnitedUnder-Expanded
HydrogenJetsintheStorageEnclosure:ExperimentsandSimulationsforReleaseRatesofupto11.5g/s.Energies2022,15,271.
[CrossRef]
85. Shentsov,V.;Kuznetsov,M.;Molkov,V.Thepressurepeakingphenomenon:Validationforunignitedreleasesinlaboratory-scale
enclosure.InProceedingsoftheInternationalConferenceofHydrogenSafety,Yokohoma,Japan,19–21October2015;Available
online:http://www.ichs2015.com/images/papers/148.pdf(accessedon1March2025).
86. Lach,A.W.;Gaathaug,A.V.;Vaagsaether,K.Pressurepeakingphenomena:Unignitedhydrogenreleasesinconfinedspaces—
Largescaleexperiments.Int.J.HydrogenEnergy2020,45,32702–32712.[CrossRef]
87. BureauVeritas.HydrogenFuelledShips.ReportNR678.2023.Availableonline:https://erules.veristar.com/dy/data/bv/pdf/
678-NR_2023-11.pdf(accessedon1March2025).
88. G-55;StandardforHydrogenVentSystems.CGA,2021.Availableonline:https://webstore.ansi.org/standards/cga/cga2021-24
47147?srsltid=AfmBOop5x3W-PG4Xux-Aj2wAfk6yVZRSrHZ%E2%80%A6(accessedon1November2024).
89. BureauVeritas.Ammonia-FuelledShips—TentativeRules.ReportNR671.2022.Availableonline:https://erules.veristar.com/
dy/data/bv/pdf/671-NR_2022-07.pdf(accessedon1March2025).
90. G095A-2017;GuidetoSafetyofHydrogenandHydrogenSystems.ANSI/AIAA:Reston,VA,USA,2018.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.

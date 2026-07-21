> **Machine-generated Markdown** — converted from the source PDF with
> [Microsoft markitdown](https://github.com/microsoft/markitdown) v0.1.6 on 2026-07-21.
>
> **Source:** Towhid, MD. Shajratul Alam; Hossain, Sumaiya Binte. *Advances and
> challenges in cryogenic liquefied hydrogen (LH2) maritime transportation:
> Thermal performance, tank design, boil-off gas management, and techno-economic
> considerations.* Renewable and Sustainable Energy Reviews **233 (2026) 116850**.
> DOI `10.1016/j.rser.2026.116850`. Published online 28 Feb 2026 (June 2026 issue).
> Bangladesh University of Engineering and Technology (BUET) / North South
> University, Dhaka, Bangladesh. (Full text — Elsevier, not open access.)
>
> **Original PDF:** `research/sources/raw/rser-2026-lh2-maritime-transportation.pdf`
> · **staging.csv id:** `rser-2026-lh2-maritime-review`
>
> ⚠️ Faithful text extraction of a two-column PDF — subscripts and table layout
> can be imperfect. **Verify any figure against the original PDF before citing or
> promoting.**

---

Renewable and Sustainable Energy Reviews 233 (2026) 116850
Contents lists available at ScienceDirect
Renewable and Sustainable Energy Reviews
journal homepage: www.elsevier.com/locate/rser
Advances and challenges in cryogenic liquefied hydrogen (LH2) maritime
transportation: Thermal performance, tank design, boil-off gas
management, and techno-economic considerations
| MD. Shajratul Alam Towhida,* |     | , Sumaiya Binte Hossainb |     |     |     |
| ---------------------------- | --- | ------------------------ | --- | --- | --- |
aDepartment of Naval Architecture and Marine Engineering, Bangladesh University of Engineering and Technology (BUET), Dhaka, 1000, Bangladesh
bDepartment of Pharmaceutical Sciences, North South University, Dhaka, 1229, Bangladesh
| A R T I C | L E  I N F O | A B S T R | A C T |     |     |
| --------- | ------------ | --------- | ----- | --- | --- |
Keywords: The importance of maritime liquid hydrogen (LH2) transportation is increasing rapidly to achieve a future global
Boil-off gas (BOG) carbon-neutral energy trade. But, the extreme thermo-physical properties of LH2 introduce major engineering
Cryogenic tank insulation
constraints for design and operation. Key challenges, such as boil-off gas (BOG), self-pressurization, cooling
Heel management
demand, and high-cost due to the need of complex and optimized cryogenic tank insulation, significantly impacts
Maritime liquid hydrogen transportation
Self-pressurization behavior LH2 transportation efficiency. This review systematically synthesizes the current state of LH2 carrier technolo-
Thermodynamic modeling gies. It covers liquid energy career benchmarking, tank architecture, cool down strategies of tanks, thermody-
namic modeling, BOG management, and techno-economic feasibility, which have not been accumulated in any of
the recent reviews. Comparative analysis confirms that LH2 exhibits the highest BOG losses (~3.44% per day)
and transportation cost (~3.74 $/GJ) among major hydrogen carriers. These happen due to the low volumetric
density of hydrogen and severe heat ingress into the tanks. Single-node equilibrium assumptions can under-
predict internal wall energy by up to 60% at low fill levels (≤5%). Conversely, validated multi-zone non-equi-
librium models show that increased tank diameter can reduce relative BOG losses from ~1.8% to ~0.2% per day.
Thermal management studies also indicate that controlled tank warming during ballast voyages can reduce heat
accumulation by 41.6-54.3%. Several significant research gaps such as sloshing-coupled thermodynamics, full-
scale experimental validation, insulation-material optimization, heel-level tuning, and integrated techno-
economic assessment under carbon pricing scenarios are identified in this review. Co-optimization of thermo-
dynamics, operation, naval architecture, and onboard propulsion is the core finding from the key insights of this
review, which is necessary to achieve energy-efficient, safe, and cost-effective LH2 shipping. To establish LH2
maritime transport as a viable media of future global green-energy logistics, these scientific and engineering
challenges need to be addressed.
| ABBREVIATIONS |     |                       |     | (continued) |                         |
| ------------- | --- | --------------------- | --- | ----------- | ----------------------- |
|               |     |                       |     | HDR         | Heat Distribution Ratio |
| Acronym       |     | Description           |     | CAPEX       | Capital Expenditure     |
| LH2           |     | Liquefied Hydrogen    |     |             |                         |
|               |     |                       |     | NPV         | Net Present Value       |
| BOG           |     | Boil-Off Gas          |     | GH2         | Gaseous Hydrogen        |
| LNG           |     | Liquefied Natural Gas |     | DME         | Dimethyl Ether          |
LOHC Liquid Organic Hydrogen Carriers COGAS Combined Gas and Steam
| MLI |     | Multi-Layer Insulation |     | MGO | Marine Gas Oil     |
| --- | --- | ---------------------- | --- | --- | ------------------ |
| PUF |     | Polyurethane Foam      |     | SCC | Social Carbon Cost |
MAWP Maximum Allowable Working Pressure VLE Vapor–Liquid Equilibrium
| TMZM |     | Thermal Multi-Zone Model |     |     |                              |
| ---- | --- | ------------------------ | --- | --- | ---------------------------- |
|      |     |                          |     | CFD | Computational Fluid Dynamics |
MHTB Multi-Purpose Hydrogen Test Bed IMO International Maritime Organization
(continued on next column)
* Corresponding author.
E-mail addresses: towhidbuet13@gmail.com, shajratulalamtowhid@gmail.com (MD.S. Alam Towhid), sumaiyahossain099@gmail.com, sumaiya.hossain@
northsouth.edu(S.B. Hossain).
https://doi.org/10.1016/j.rser.2026.116850
Received 23 November 2025; Received in revised form 10 February 2026; Accepted 22 February 2026
Available online 28 February 2026
1364-0321/© 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
known as heel with an aim to maintaining the tank's low temperature.
During the return or ballast voyage, the tank gradually warms up as
vapor and wall temperature rise. Typical voyages and the resulting
phenomena may last for several weeks. Over time, this warming can
1. Introduction cause vapor stratification in the ullage space. It influences tank pres-
surization behavior and increases pre-cooling demand before the next
The increasing demand for long-distance energy transport in an loading operation [18–21]. For LNG carriers, pre-cool down practices
efficient and sustainable way is a major concern for global trade. The with intermittent heel spraying (8-12 h chill down) are well known and
urgency of de-carbonization has been intensified throughout couple of influence turnaround time. But, in the case of LH2, tanks differ in
decades which has intensified the focus to use hydrogen as a clean and insulation type, inner-wall thickness, and cryogenic temperature, thus
sustainable energy carrier. Among various storage and transport forms, making it difficult to transfer operational paradigms of LNG to LH2
liquefied hydrogen (LH2) has emerged as a promising option for large- directly [22–25].
scale and long-distance maritime energy transport. These have been From modeling perspective, the accurate prediction of several key
intensified due to its high volumetric density and zero-carbon combus- performance parameters is mandatory for tank and ship design. These
tion profile. The regions with limited renewable energy sources would include self-pressurization, boil-off rates, and cool down behavior, of-
be greatly affected by this form of energy transport as it enables bulk fering practical challenges. Different models have been proposed for
energy delivery globally. This LH2 transportation technology also sup- better thermodynamic performance of LH2 transportation. Reduced
ports the development of a global hydrogen economy. order (lumped-mass/two-node) models provide computationally effi-
The transportation of the energy of natural gas has been historically cient tools for predicting long-duration behaviors. Although, these
dominated either through pipelines in gaseous form or as liquefied models have been validated against experimental test beds (e.g., NASA
natural gas (LNG) for long distance shipping. However, the use of Multi-Purpose Hydrogen Test Bed (MHTB)), they face limitations at low
pipelines for energy transport becomes infeasible both in economically fill levels as vapor thermal stratification and transient heat transfer
and technically for distances beyond roughly 2000 km. On the other become dominant at this case [26–29]. Experimental studies and
hand, LNG offers better feasibility for long-distance shipping due to its multi-node or non-equilibrium models have demonstrated that
superior volumetric efficiency. LNG provides about a 600-fold reduction isothermal assumptions under-predict pressure rise and misinterpret
in volume compared to its gaseous form [1–3]. However, LNG transport interface heat transfer. Along with these, varying tuning coefficients and
faces several notable drawbacks. The most significant ones include its heat transfer correlation across studies create model uncertainty
low boiling temperature ((cid:0) 162 ◦C) which contribute to boil-off gas [28–31]. Additionally, several under-resolved factors including the ef-
(BOG) losses, and carbon content that creates greenhouse gas emissions fect of tank thermal mass, inner-wall conduction, partitioning of heat
[4,5]. These limitations have encouraged the researchers to explore leakage between vapor and liquid exist [32,33].
alternative solutions which offer carbon-free carriers. They proposed Economically, LH2 carriers offer higher transport cost due to BOG
other ways to transport the energy of natural gas by other liquefied losses, insulation CAPEX, and the cost of liquefaction. Studies show that
natural form such as ammonia, methanol, and hydrogen. These forms of this cost is comparatively higher than for alternative carriers such as
transportation can mitigate boil-off gas (BOG) formation and reduce ammonia, methanol, dimethyl ether (DME) etc. This is primarily due to
environmental impact [6]. the greater BOG losses and higher storage costs, which are sensitive to
Based on the advantages and challenges, and decades of experience voyage distance, atmospheric temperature, liquefaction cost, and car-
in LNG shipping, researchers have recognized LH2 transport by sea as bon pricing [34–39]. However, strategic utilization of BOG can mate-
the most promising large-scale method for intercontinental hydrogen rially affect the vessel's net present value and optimal design choices.
trade. LH2 reduces its volume by nearly three orders of magnitude to BOG has the potential to be used as onboard fuel and to be adopted for
70.8 kg/m3. This feature makes maritime export feasible where pipe- re-liquefaction or recovery systems [40]. Again, techno-economic ana-
lines or high-pressure gaseous transport are impractical [7]. Several lyses demonstrate that co-optimizing tank maximum allowable working
pilot and design efforts have been conducted in recent years. These pressure (MAWP) and cruising speed can alter net present value (NPV)
include the HESC Suiso Frontier demonstration voyage and classifica- outcomes by hundreds of millions USD. This is possible under plausible
tion society approvals for very large LH2 carrier designs. These steps fuel-price and carbon-price scenarios [41,42].
have underscored the tangible momentum toward commercial LH2 Several research gaps thus emerge at the intersection of thermody-
shipping [8–13]. namics, operations and economics. The first one is the modeling fidelity
Although LH2 transportation offers significant advantages, it in- at low heel percentages which includes vapor stratification, wall thermal
troduces critical challenges which range from thermodynamic and inertia, and their impact on pressurization. The most reduced-order
operational constraints to economical perspectives. Low boiling tem- models need consistent calibration and analytical correction factors
perature of LH2 ((cid:0) 253 ◦C) is the root cause of most of the challenges [43–45]. Secondly, experimental data are very limited, and the only
that demands high-performance insulation, vacuum creation, and opti- operational sea trial (Suiso Frontier) used a small Type-C tank. But it
mized structural materials of stable mechanical properties under cryo- may not represent future large carriers. So, scalability and upscaling
genic conditions [8,14,15]. Although proper insulation based on recent evidence for thousands-to hundreds-of-thousands-m3 LH2 tanks are
developments is ensured, the significant low boiling temperature of LH2 needed. Integrated ship system studies and practical methods for BOG
causes unavoidable heat ingress into the tanks. This phenomenon pro- management are other areas of research gaps. But very few studies have
duces BOG as a continuous evaporation loss which reduces delivered worked with accumulating all of the challenges and research gaps of
cargo capacity and drives tank pressurization [16,17]. Additionally, hydrogen transportation. Most of the studies of energy transportation
large LH2 tanks offer relatively low maximum allowable working are based on LNG carriers. Either they have worked with a specific
pressure (MAWP), and further complicate BOG retention. This often technical area of LNG storage or transportation or they have focused on
forces controlled venting unless re-liquefaction or utilization options are the techno-economic side. Additionally, review articles on both the LNG
available [18,19]. and LH2 transportation are not plenty. Lu et al. (2025) conducted a
Operationally, ship-borne LH2 tanks experience repeated loading- review on key influencing factors on hydrogen storage and trans-
unloading cycle. It starts with loading, then goes to laden voyage, portation costs [46]. Their study extensively focused on technical areas
then faces unloading, and finally ballast (return) voyage. This cycle of storage and economic areas of transportation, but did not exclusively
differs significantly from typical static, ground storage of LH2. After include the technical and operational sides of LH2 transportation.
unloading, LH2 carriers usually hold a small amount of liquid which is Mekonnin et al. (2025) presented an overview of the current state of
2

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
hydrogen storage methods, and materials. They assessed the potential recent review articles associated with hydrogen storage and trans-
benefits of and challenges of various storage techniques, but did not portation [53–60]. All these studies have brought significant impact on
focus on transportation [47]. Chilunda et al. (2025) presented an hydrogen storage and transportation technologies. However, research
overview of electrochemical cycling of liquid organic hydrogen carriers on hydrogen energy is still at its early phase. From 2017 to 2023, only 81
(LOHC) for hydrogen storage and transportation [48]. They conducted a papers have been published regarding hydrogen energy. Among those,
comparative carbon footprint assessment of electrochemical LOHC the groups of operation research, techno-economic-environmental as-
cycling processes against thermochemical and hybrid LOHC cycling sessments, life cycle assessments, and other groups include 51, 21, 5,
processes, but did not work with LH2. Shu et al. (2025) conducted an and 4 numbers of publications respectively [46]. But, from the authors’
elaborated study combining multiple hydrogen production techniques, point of view, there is no single comprehensive review available which
efficient hydrogen storage materials, different ways of hydrogen trans- has worked with the detailed thermodynamic and operational chal-
port and applications of hydrogen, but focus was not given to technical lenges and advancements, and integrated cost analysis of ship-borne
and operational challenges of LH2 transportation [49]. Naseem et al. LH2 transportation.
(2025) presented a detailed review on hydrogen production methods This review brings the technical, operation, and cost strands together
(renewable and non-renewable), hydrogen storage strategies, and ad- and focuses on ship-borne LH2 transportation. It systematically starts
vancements in the transportation of hydrogen [50]. Although they with challenges of ship-borne LH2 transportation, then discusses the
included transportation in their study, but it eventually did not include core studies and ways of LH2 storage technologies to get insights for
the detailed complex technical and operational issues of LH2 trans- transportation, and finally dive depth into the technical and operational
portation. Yang et al. (2025) conducted a review focusing on hydrogen discussions of maritime LH2 transportation. It has synthesized current
production, storage, and transportation from renewable energy [51]. knowledge on LH2 tank thermodynamics, practical ballast and cool
They also did not dive into the depth of technical and operational down strategies. This review is unique for its comprehensive and tech-
challenges of LH2 transportation. Otsubo (2025) provided a compre- nically detailed approach to LH2 transportation which is significantly
hensive review of hydrogen compressor technologies and evaluated the impactful for researchers and commercials. Conventional reviews pri-
impact of long-distance hydrogen transportation on compressor energy marily summarized information about existing technologies or eco-
consumption and electrification requirements [52]. He also did not nomic aspects, but have not analyzed from in-depth technical
focus the technical side of LH2 transportation. There are also several perspectives. Whereas, the core objective of this review is not only
Table-1
Scope and contribution of existing reviews relative to the present study.
Reference Primary scope Thermodynamic analysis Maritime operations Techno-economic Key limitation relative to present review
No. Discussions
[61] LH2 transfer operations & Qualitative boil-off Transfer & venting Not addressed Focuses on transfer safety. No voyage-scale
safety was the core study discussions are conducted operations only. Avoiding thermodynamics or economics were
area other critical areas discussed
[62] LH2 storage technologies Boil-off and insulation Transportation losses were Partial. Only tank This study lacks maritime operational
was analyzed techniques were reviewed noted. But a critical and in cost was discussed. coupling. Ship-level implications were not
depth analysis was not considered.
present
[63] Insulation structures for Different thermal protection Mobile tanks were Not addressed This study treated insulation in isolation, no
LH2 tanks was the main techniques, especially passive mentioned operational or cost linkage was considered.
focus & active systems were
analyzed.
[64] This study compared LNG- Qualitative thermal Shipboard handling Qualitative Did not quantify LH2 boil-off evolution.
LH2 for maritime use requirements were techniques & materials economics was Operational penalties were also not included
mentioned. were included considered
[65] LH2 adoption in maritime High-level energy losses were Bunkering, regulations, and High-level cost Treated boil-off as a static issue. Real-world
transport analyzed safety as operational barriers were BOG, and its utilization was not discussed as
challenges were discussed included its significant thermodynamic involvement.
[66] Entire LH2 supply chain Liquefaction & storage losses Transport discussed Cost of liquefaction Maritime shipping treated as one segment.
was invlolved were quantified generically. In depth of BOG was The study touched almost every sides of the
technical analysis was not emphasized. supply chain, so automatically only
considered. maritime transportation was not deeply
analyzed
[67] LH2 in transportation It Qualitative boil-off Maritime challenges were Economic barriers This study lacks thermodynamic-operational
was focused on maritime discussions has been highlighted were discussed. coupling, which is necessary to understand
focus cases. conducted. real-world scenario.
[60] Hydrogen in transport. Only storage challenges were Maritime scenarios were Policy-oriented Maritime LH2 shipping was not a core focus
This study focused on road outlined largely absent study
& aviation transportation.
[59] Hydrogen permeation Material-level mechanisms Hydrogen transportation Not addressed This study was not dedicated to cryogenic
barriers were the core has been discussed through pipelines only LH2 shipping systems
focused area
[58] Hydrogen storage for Comparative storage options Maritime propulsion & High-level emissions No quantitative thermodynamic or
maritime decarbonization were discussed ports were outlined were focused operational modeling were considered
was the focused area
[68] This study focused on both Comparative storage & Seaborne transport were Cost comparison This study treated LH2 shipping
hydrogen storage & transport techniques were discussed across modes was macroscopically, It did not consider
transportation analyzed included operational thermodynamics
This This study is dedicated to Coupled boil-off, pressure, Voyage, heel management, Operational cost & This study is the first integrated
review LH2 maritime shipping heat ingress are extensively operations are included energy penalties are thermodynamic-operational-economic
systems only discussed explained in depth synthesis considering all the possible factors
and areas of cryogenic LH2 maritime
transportation
3

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
present the state-of-the-art information but also help readers to under- more hydrogen on each trip [71]. These issues are well-understood for
stand the total technical and operational mechanisms for achieving a LNG shipping by recent studies. But how these performance indicators
holistic knowledge of maritime LH2 transportation technology. Sce- would behave or fluctuate in the case of LH2 transportation is still
narios and thermo-physical analysis of low feel level tank states have mostly unresolved. Additionally, the common challenges of energy
received especial focus. This review systematically integrates loading, transportation along with the specific challenges for maritime LH2
cool down, voyage, and unloading scenarios which include discussions transportation would need different strategies to be overcome while
on BOG generation, operational strategies, and tanks pressurization dealing with LH2 transportation technology. These challenges are
control, covering all thermodynamic behavior of various ships. It also originated from the unique properties of hydrogen such as colder storage
emphasizes the influence of tank geometry and insulation design which temperature, different insulation needs, and stricter pressure limits. The
is the basic performance decider for these mentioned performance var- possible pathway for solving the challenges of LH2 transportation is still
iables. To understand the novelty of this article more explicitly, a an under-developed area. The optimized heel requirements and the
comparative table summarizing overlaps and key gaps of the most recent appropriate behavior of heat transfer and stratification compared to
reviews with key insights would be effective. Table-1 represents the LNG are unclear.
most recent relevant review articles. It includes the primary scope, To minimize BOG losses, proper balance between storage conditions
thermodynamic analysis, maritime operations discussion, techno- and operational strategies is mandatory. It becomes a major challenge
economic analysis, and key limitations. This table clearly shows the during long voyages because hydrogen's flammability and cryogenic
overlaps and gaps of the most recent reviews relative to the present requirements make design and operation more complex. BOG genera-
study. tion is also affected by the ship's cruising speed and the storage tank's
Along with providing a holistic understanding of maritime LH2 maximum allowable working pressure (MAWP). These parameters also
transportation systems, this review offers critical insights into opti- fluctuate during long voyages. To suppress vapor pressure and reduce
mizing their efficiency, safety, and economic feasibility. All these in- BOG generation, the increase of the tank pressure is an option, although
clusions have been based on consolidating the latest research and it imposes limits on allowable fill levels. Again, increasing tank pressure
analytical findings. comes with complex structural arrangement and cost requirements.
Conversely, to minimize BOG losses, voyage duration can be shortened
2. Challenges of shipborne liquefied hydrogen (LH2) by higher cruising speed, which again significantly raises fuel demand
transportation and operational costs. So, optimizing balance among these parameters is
a practical and crucial challenge.
2.1. Thermal management, tank design and structural constraints, and
operational challenges 2.2. Optimization of BOG utilization and system integration
In the liquid hydrogen (LH2) systems, hydrogen is stored in cryo- The efficient management of generated BOG is another related
genic form. One of the most significant challenges in LH2 storage system challenge of liquid hydrogen transportation. Either it can be wasted or
is the creation of boil-off gas due to heat transfer inside the cryogenic collected effectively to use for secondary use. The generated BOG can be
tank from the surroundings. This results in significant amount of used as onboard fuel which would lower the dependence on fossil fuel.
hydrogen loss during storage or transportation. The boil-off losses But this approach would bring some technical and economic complex-
happen due to the heat transfer inside the storage tanks. To minimize it, ities. Engine compatibility to use BOG as fuel is the first challenge for
the necessity for high-performance insulation systems over the whole utilizing BOG. Engines should be designed in such a way that it would be
storage tanks is mandatory [69]. But, even strong insulation is ensured, run by the generated BOG. After considering engine compatibility, sys-
some heat will always leak in. This causes the evaporation of some part tem integration is raised as another challenge. Additionally, it comes
of the stored LH2. To transport hydrogen as liquid form, it needs to be with crucial questions including capital cost consideration and complex
stored at a very low cryogenic temperature ((cid:0) 253 ◦C) to ensure carrying operational management. So, finding an optimal balance among tank
much more hydrogen compared to hydrogen gas in the same volume. pressure, ship speed, and BOG utilization is a critical design and oper-
Due to this very low cryogenic temperature, a slight increase of tem- ational challenge for efficient LH2 transportation.
perature causes the significant evaporation of the liquid hydrogen or the
BOG. Using pressurized tanks can be the options to prevent BOG gen- 2.3. Heel management and cool down
eration as pressurized tanks can keep BOG inside the tanks and have
invulnerable behavior against leakage. However, several pressure cyl- Another significant operational challenge for LH2 transportation is
inders are needed to be installed in the ship to store these liquefied the heat ingress for extended periods during the return or ballast voyage
energy without BOG ventilation. But this approach brings wasting ship after unloading the cargo. After unloading, the tanks become empty and
space, increasing the tank weight, operational, and instruments they are exposed to heat ingress which often last for 3 weeks. This causes
complexity, and capital expenditure (CAPEX). So the storing tanks are a gradual rise in tank wall and vapor temperatures. To safely operate the
designed as lightweight cryogenic tanks to handle very low pressures new LH2 receiving stage at the next loading cycle, the tanks must be
(low maximum allowable working pressure or MAWP), reduce cost, cooled again below a certain threshold before reloading to very low
weight, and ensure excellent insulation [70]. Due to this design temperatures [72]. To pre-cool down, a small amount of LH2 is sprayed
constraint, it becomes much more difficult to hold and manage the inside the tank. This lowers the temperature of the tank below the
boil-off gas (BOG) that forms inside the tanks. Again, maintaining threshold temperature. The process is similar to LNG ships where it takes
extremely low temperatures and proper pressure during all stages, such usually 8-12 h [73–75]. This time depends on tank size and design. This
as storage, loading, and shipping, is difficult in practical cases. step is performed carefully and made lengthy as rapid cooling may
To solve this, ships usually keep a small amount of liquid hydrogen induce thermal stress on tank materials. Sometimes, ships start this
inside the tank after unloading. This amount is called heel which keeps pre-cooling process while they are at sea and sailing back to the loading
the tanks cold during the empty return trip. It also helps to cool the tanks terminal, and don't wait for the arrival to the terminal. But, to perform
down before the next loading. But, keeping too much heel reduces the this, the ships must keep a certain amount of heel after unloading to be
amount of hydrogen delivered. On the other hand, keeping too little heel used later for cooling. Again, the identification of heel storage amount
may not be enough to control tank temperature. So, the core challenge is for cooling requirement becomes a basic challenge. This heel require-
to find a balance to minimize heat transfer into tanks, reduce boil-off ment creates a trade-off between operational efficiency and delivery
losses, and keep the heel volume as small as possible to transport capacity [76]. After return voyage, the temperature difference between
4

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
tank wall and surroundings also affects the amount of heat transfer into large-scale Type-B or membrane-type tanks, introducing new unknowns
the tank at the beginning of the next trip. But, the temperature of the regarding insulation performance, venting strategy, and thermal stress
surroundings fluctuate at different maritime zones and at different management [78]. Without reliable modeling frameworks and validated
weather conditions. So, identifying the temperature difference is also data, optimizing heel mass and cool down strategies remain uncertain.
challenging. It is only possible to predict a temperature difference range At the same time, the BOG control for next-generation LH2 carriers re-
by considering the intense conditions. So, the determination of onboard mains underdeveloped for next generation LH2 carriers.
cooling requirement always remains a non-specified area, which ulti-
mately affects tank design, heel requirement, and BOG utilization. These 3. Overview of hydrogen storage technologies
operational factors, such as temperature rise during empty voyages, cool
down duration, and heel optimization, represent key technical chal- 3.1. Hydrogen storage technologies and their challenges
lenges in efficient LH2 transportation.
Hydrogen storage technologies vary depending on the operating
principles, storage need, energy and infrastructural availability, and the
2.4. Modeling and design uncertainties for large scale LH2 transportation
duration needed. So, it is important to present them in a concise manner
to better understand the technologies. Inspired from the study of
Beyond operational issues, another critical challenge is the accurate
Mekonnin et al. (2025) [47], Table-2is prepared. It represents the most
modeling and design of large-scale LH2 tanks. Most existing thermo-
acceptable, common, and widely studied and used hydrogen storage
dynamic models for LH2 tanks are simplified and based on lots of
techniques. It includes storage technologies as compressed gas, liquid
assumption, such as uniform temperatures within the liquid and vapor
state, ammonia, liquid organic hydrogen carriers, and metal hydrides.
regions. However, when fill levels are low during ballast voyages, both
The table focuses on the major technical advantages and challenges.
strong vapor stratification and transient heat transfer occur. But those
Table-2 represents that no single hydrogen storage technology
simplified models cannot capture these real-life complex phenomena.
currently satisfies all the required standard criteria. These include high
This underestimation lead to inaccurate analysis of internal energy, wall
density, low cost, safety, energy efficiency, and scalability. Hydrogen
temperature, and pressurization rates, particularly when then tanks are
can be stored in all the three states as gaseous, liquid, and solid states to
mostly empty. Additionally, there is no standardized heat transfer cor-
increase energy density. Both above and underground storage facilities
relation for hydrogen under cryogenic conditions. Different studies
are needed for short and long term storage [91]. Figure-1displays the
consider different tuning parameter, resulting in significant uncertainty
different hydrogen carrier options for storage, taken from the study of Lu
of accurate prediction. Moreover, limited experimental validation data
et al. (2025) [46]. In summary, compressed gaseous hydrogen (CGH2)
for larger tanks act as a driving force for this inaccuracy. Moreover,
stored in above-ground is the most common technology for hydrogen
small Type-C tanks were used in cryogenic liquid carriers (as used in the
storage. Due to their available mature technology of pressure vessels and
Suiso Frontier) [77]. But, this type is facing transition towards future
Table-2
Hydrogen Storage Technologies and Their Challenges. It also includes the core working principle, operating conditions, and key advantages.
Storage Method Working Principle Hydrogen Operating Conditions Key Advantages Main Challenges
Density
(Gravimetric/
Volumetric)
Compressed Gas In this method, hydrogen is stored physically ~4–6 wt%, High pressurized This technique is High pressurized hydrogen
(350–700 bar, as compressed gas. Storage can be done both ~20–40 g/L hydrogen is stored. commercially mature. needs heavy cylinders to
Type III/IV above-ground and under-ground. To store it Pressure varies from It offers rapid refueling withstand the pressure. It also
cylinders) for long-time and for large-scale different 350 to 700 bars. capacity and relatively needs high compression energy
[79–85] techniques such as salt caverns, aquifers, Temperature remains simple technology demands for pressurizing. Low
depleted oil and gas reservoirs etc. exist [18.9]. as ambient temperature volumetric density and risk of
embrittlement are also the
challenges.
Liquid Hydrogen Hydrogen is stored as liquid state at cryogenic ~7–8 wt%, ~70 Due to the cryogenic Liquid hydrogen offers The liquefaction process of
(LH2) [86–89] temperatures (~20 K) g/L temperature, advanced high volumetric hydrogen consumes around 30
insulation is required to density. It is also to 40% of stored hydrogen
resist any heat ingress favorable for large- energy. Boil-off losses,
inside the storage tank. scale transport stratification, complex
insulation etc. are the major
challenges. Challenges are
described elaborately in Section
2.
Ammonia (NH3) In this technique hydrogen is not stored as 108 kg H2/m3 The storage pressure is Ammonia has high Toxicity is the most significant
[86–89] unique compound, rather it is chemically equivalent not too high like CGH2. volumetric density. It challenge. The cracking is also
bound in ammonia (17.6 wt% H2) The compound is stored offers zero-carbon energy-intensive. Additionally,
with mild pressure of carrier and are while decomposing H2,
around 10 bars or acceptable with impurities are traced in most of
refrigerated liquid existing global the cases.
infrastructure
Liquid Organic In this method, liquid Hydrogen is stored and 5–7 wt% Ambient liquid state, This system offers high Dehydrogenation needs high
Hydrogen released by reversible catalyst-assisted safety. There is no issue energy input. The catalysts are
Carriers hydrogenation–dehydrogenation technique. reactions of boil-off gas degraded over time and have
(LOHCs) [86, This storage system uses reusable catalyst for generation. It is also limited cycle life.
87,90] hydrogenation, and a catalyst for compatible with
dehydrogenation. existing fuel logistics.
Metal Hydrides In this process, hydrogen is absorbed into solid 1–7 wt% Temperature is slightly This system offers high This system uses heavy
(e.g., MgH2, crystalline lattices higher, around 200 to volumetric density. It is materials. It has slow kinetics
LaNi5H6) [86, 400 ◦C. Pressure also also compact and safe. and difficulties of heat
87] remains moderate. management and cost
5

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-1. Schematic diagram of most common and acceptable hydrogen storage technologies. It can be stored in all three forms of matter: solid, liquid, and gaseous
states. The active states or phases are shown three colors. Blue, green, and yellow colors represent gaseous state, liquid state, and solid state respectively [46].
commercial availability have made this technique widely acceptable emerging method but brings complex tank design and operational
than other storage technologies [79–85]. CGH2 tanks are designed to requirement for very low temperature and ultra-high pressure. Although
carry high pressurized CGH2, but still the Low storage capacity is the LH2 transportation has its own challenges and limitations too, it has
main challenge of CGH2 tank options. Storing as salt caverns at under- emerged one of the most acceptable technologies through overcoming
ground is one of the most potential storage technologies due to their most of the challenges of these summarized technologies.
technological and commercial availability. This technology has also
been researched plenty of times [46]. 5. Thermodynamic understanding of heel management: from
LNG carriers to LH2 systems
3.2. Foundational studies on the thermodynamic and operational
There are several studies regarding heel management of LNG carriers
behavior of LH2 storage tanks
in ballast voyage. Studies suggest that, in 2018, most LNG carriers were
membrane-type covering 70% of the total LNG carriers. Hasan et al.
It is essential to first examine the technical and operational charac-
(2009) demonstrated that the quantity of LNG required to cool a
teristics of LH2 storage for the better understanding of LH2 trans-
membrane-type tank from ambient temperatures may range from 800 to
portation technology, as transportation occurs through storing first.
1600 m3. It is also estimated as 0.5-1% of total carrying capacity. They
Many of the fundamental processes including thermal stratification,
concluded that it is common practice to carry a heel of around 5% [105].
BOG formation, pressurization, and chill-down phenomena follow the
Krikkish (2018) carried out theoretical and experimental analysis where
same principles for both LH2 storage and transportation. For this reason,
he studied the nature of pressure fluctuations inside a LNG tank. He
Table-3is added presenting the fundamental studies of LH2 storage with
showed that due to uneven tank wall heat fluxes the pressure fluctuation
their focused area and key finding, although this review is focused on
happens. He also stated that the liquid temperatures remained stable
LH2 transportation. The table has covered some of the key studies
while gas temperatures varied. He concluded that the system tends to-
conducted in the first couple of years of foundational research of LH2
wards thermodynamic equilibrium in ballast voyages [106]. Krikkis
storage technologies. The studies have covered LH2 tank thermody-
et al. (2021) [107]conducted a study on how LNG behaves inside ship
namics, filling operations, and heat transfer mechanisms to better un-
tanks during the laden voyage (when the ship is full of cargo) and the
derstand the thermal behavior, phase transitions, and pressure
ballast voyage (when the ship is empty after unloading, but still carries a
evaluation. These all are crucial for designing and operating efficient
small amount of liquid to keep tanks cold). They developed a combined
cryogenic storage systems in LH2 carriers.
heat transfer and thermodynamic model to understand how the insu-
lation of the tanks interacts and impacts the thermodynamic properties
4. Comparison of alternative hydrogen transportation
of the LNG cargo. They highlighted several technical challenges in LNG
technologies
shipping. Many of these challenges are also relevant for future hydrogen
carriers. These include: multiple boiling regimes occurring at the same
To analyze why the researchers are opting more for LH2 trans-
time on the tank surface due to the non-uniform heat gain on different
portation studies recently, the other transportation technologies need to
parts of the tank wall; the difficulty to predict sudden pressure changes
be studied. Table-4represents the four major hydrogen transportation
inside the tanks during laden voyage which are linked to turbulent vapor
technologies other than LH2 transportation. It includes transportation
release from non-uniform boiling on the insulation surface; the difficulty
through pipelines, NH3 shipping, liquid organic hydrogen carrier
of predicting cargo behavior during laden voyages due to multi-phase
(LOHC) shipping, and cryo-compressed hydrogen. The table explains
and multi-boiling behavior. They commented that the loading and dis-
description, efficiency or losses, infrastructural needs, and limitations of
charging cycle is crucial for understanding how tanks behave across
each transportation techniques.
both voyages. During ballast voyage, the cargo is much closer to ther-
From Table-4it can be said that hydrogen transportation models are
modynamic equilibrium. They also stated that the liquid temperature
highly context dependent and have no universal optimal solution.
stays almost constant but the gas temperature varies significantly. In
Pipelines offer efficiency for regional transport but become less-feasible
some tanks, they observed small-scale rollover phenomenon due to this
for long distance transport (over 2000 km). This technology also re-
[106–108]. Additionally, the boil-off rate is not fixed per day. Rather, it
quires costly material upgrades. Ammonia and LOHC can utilize existing
is directly linked to the ship's propulsion system and speed-power curve.
infrastructure but their application is limited due to the challenges of
They concluded that a single tank usually carries the main heel, while
cracking and dehydrogenation. Cryo-compressed technology is an
6

MD.S. Alam Towhid and S.B. Hossain                                                                                                                                    R  e n  e  w  a  b  le    a  n  d   S  u  s t a  i n  a b  l e    E n  e  r g y    R  e  v i e  w  s   2  3 3 (2026) 116850
| Table-3  |     |     |     | Table-3 (continued) |     |     |     |
| -------- | --- | --- | --- | ------------------- | --- | --- | --- |
Summary of key studies on thermodynamic behavior and operational challenges
|     |     |     |     | Author(s)  | Study Focus  | Key Issues Addressed  | Key Findings |
| --- | --- | --- | --- | ---------- | ------------ | --------------------- | ------------ |
of LH2 storage systems in its development phase.
|     |     |     |     |     | stratification  | and large diameters  | critical velocity  |
| --- | --- | --- | --- | --- | --------------- | -------------------- | ------------------ |
Author(s) Study Focus Key Issues Addressed Key Findings during filling reduce mixing thresholds
depend on
| Molkov,  | This study  | They addressed  | Their model  |     |     |     |     |
| -------- | ----------- | --------------- | ------------ | --- | --- | --- | --- |
Dadashzadeh,  focused on the  temperature rise  predicted  injector direction.
Makarov  physical model  during fast fuelling,  temperature  Wall
temperatures
| (2019) [92] | of onboard  | and pressure buildup  | fluctuation  |     |     |     |     |
| ----------- | ----------- | --------------------- | ------------ | --- | --- | --- | --- |
hydrogen  inside tank. Other  within ±5 ◦C. It  were also affected
|     | storage tank     | challenges they        | incorporated real  |                   |                   |                      | with this.      |
| --- | ---------------- | ---------------------- | ------------------ | ----------------- | ----------------- | -------------------- | --------------- |
|     |                  |                        |                    | Ma, Zhu, Li, Xie  | They studied the  | Key focused          | Their CFD plus  |
|     | thermal          | specified include      | gas behavior, and  |                   |                   |                      |                 |
|     |                  |                        |                    | (2020) [98]       | phenomena of      | challenges include;  | structural      |
|     | behavior during  | short fuelling times,  | entrainment        |                   |                   |                      |                 |
fuelling complex heat  theory for  chill-down and  rapid wall cooling  analysis
transfer, and  velocity. It was  thermal stress in  causes large thermal  predicted
|     |     |                 |               |     | LH2 tank during  | stress, filling rate  | temperature  |
| --- | --- | --------------- | ------------- | --- | ---------------- | --------------------- | ------------ |
|     |     | limitations of  | suitable for  |     |                  |                       |              |
previous models automated  ground filling affects stress  gradients and
|                  |                 |                 | fuelling protocols |     |     | distribution, and risk  | stress. They   |
| ---------------- | --------------- | --------------- | ------------------ | --- | --- | ----------------------- | -------------- |
|                  |                 |                 |                    |     |     | of structural failure   | revealed that  |
| Liu & Li (2019)  | Core objective  | They addressed  | Their results      |     |     |                         |                |
bottom was
| [93] | was to analyze  | thermal  | demonstrated  |     |     |     |     |
| ---- | --------------- | -------- | ------------- | --- | --- | --- | --- |
thermal physical  stratification, and  that phase change  critical at start,
performance in  phase change effects.  significantly  and middle was
critical later.
|     | LH2 tank under  | Other key issues the   | affects pressure.  |     |     |     |                 |
| --- | --------------- | ---------------------- | ------------------ | --- | --- | --- | --------------- |
|     | constant wall   | considered include     | Additionally,      |     |     |     | They also       |
|     | temperature     | rapid pressurization,  | gravity            |     |     |     | commented that  |
filling rate
|     |     | influence of gravity,  | accelerates  |     |     |     |     |
| --- | --- | ---------------------- | ------------ | --- | --- | --- | --- |
correlates with
|     |     | wall temperature,  | stratification, and  |                 |                   |                      |               |
| --- | --- | ------------------ | -------------------- | --------------- | ----------------- | -------------------- | ------------- |
|     |     | and liquid height  | wall temperature     |                 |                   |                      | stress        |
|     |     |                    | impacts              | Zhou, Zhu, Hu,  | They studied the  | They specified that  | Results       |
|     |     |                    |                      | Wang, Xie,      | effect of ullage  | heat ingress causes  | demonstrated  |
stratification
|     |     |     | rate. They      | Zhang (2019)  | pressure on LH2  | pressurization, and    | that evaporation     |
| --- | --- | --- | --------------- | ------------- | ---------------- | ---------------------- | -------------------- |
|     |     |     | commented that  | [99]          | evaporation rate | safety valve pressure  | occurs in 3 stages,  |
|     |     |     |                 |               |                  | influences             | and rated ullage     |
liquid height
|     |     |     |     |     |     | evaporation. They  | pressure mainly  |
| --- | --- | --- | --- | --- | --- | ------------------ | ---------------- |
affects
|     |     |     | development |     |     | also considered the  | affects liquid-  |
| --- | --- | --- | ----------- | --- | --- | -------------------- | ---------------- |
Petitpas (2018)  They worked  Intrinsic losses from  Results revealed  complex internal  invariant period.
flow patterns.
| [94] | with BOG losses  | heat ingress were the  | that losses mainly  |     |     |     |     |
| ---- | ---------------- | ---------------------- | ------------------- | --- | --- | --- | --- |
during LH2  main concern of their  occurred from  Liu, Feng, Lei, Li  Their objective  They addressed the  They found that
transfer at  study. They also  vapor  (2018) [100] was to  disturbance of  sloshing mixes
|     |            |                     |                   |     | investigate  | stratification by    | layers which      |
| --- | ---------- | ------------------- | ----------------- | --- | ------------ | -------------------- | ----------------- |
|     | refueling  | considered complex  | compression.      |     |              |                      |                   |
|     |            |                     |                   |     | thermal      | sloshing. They also  | affects pressure  |
|     | stations   | thermodynamics,     | These losses can  |     |              |                      |                   |
unclear loss  exceed 12%.  stratification  considered heat leaks  and temperature
mechanisms, and  They commented  under sloshing  and phase change  distribution.
|     |     |             |                   |     | excitation in   | impact and safety   | Their results    |
| --- | --- | ----------- | ----------------- | --- | --------------- | ------------------- | ---------------- |
|     |     | cost impact | that liquid       |     |                 |                     |                  |
|     |     |             | density remained  |     | non-isothermal  | risks of LH2 tanks. | provided design  |
|     |     |             | non-ideal.        |     | LH2 tank        |                     | insights for     |
sloshing
| Zuo, Sun, Jiang,  | They analyzed  | Their core concerns  | Study  |     |     |     |     |
| ----------------- | -------------- | -------------------- | ------ | --- | --- | --- | --- |
suppression.
| Qin, Li, Huang  | thermal         | were thermal         | demonstrated        |     |     |     |     |
| --------------- | --------------- | -------------------- | ------------------- | --- | --- | --- | --- |
| (2019) [95]     | stratification  | stratification, and  | that self-spinning  |     |     |     |     |
|                 | suppression in  | inefficient mixing.  | spray bar reduces   |     |     |     |     |
the remaining tanks are kept close to or entirely empty. And, vapor-only
|     | LH2 tanks. They  | They also specified  | temperature  |     |     |     |     |
| --- | ---------------- | -------------------- | ------------ | --- | --- | --- | --- |
considered self-  payload/power  differences, and  tanks may reach ambient temperature over the continuation of the
|     | spinning spray  | constraints in  | causes 70%  |     |     |     |     |
| --- | --------------- | --------------- | ----------- | --- | --- | --- | --- |
voyage, but the heel carrying tank will remain significantly colder
|     | bar for this  | spacecraft | payload savings. |     |     |     |     |
| --- | ------------- | ---------- | ---------------- | --- | --- | --- | --- |
[107]. Overall, this study suggested that LNG ship transportation cannot
suppression
Liu, Li, Zhou  They focused on  They specified  Results exhibited  be understood by studying the laden and ballast voyages separately
(2018) [96] thermal  challenges such as  that gravity  only, rather they are connected by the loading and discharging cycle.
stratification in  strong stratification  reduces  Although, the main challenges are based on managing heat transfer and
|     | LH2 tanks under  | in low gravity,  | stratification in  |     |     |     |     |
| --- | ---------------- | ---------------- | ------------------ | --- | --- | --- | --- |
pressure fluctuations during laden voyage, the ballast voyage is easier to
|     | different gravity  | localized  | 1g, and  |     |     |     |     |
| --- | ------------------ | ---------- | -------- | --- | --- | --- | --- |
model due to its equilibrium-close behavior. The study also emphasized
|     | levels | evaporation, and  | microgravity  |     |     |     |     |
| --- | ------ | ----------------- | ------------- | --- | --- | --- | --- |
that boil-off rates depend on not only cargo properties but also on ship
|     |     | surface tension  | increases  |     |     |     |     |
| --- | --- | ---------------- | ---------- | --- | --- | --- | --- |
effects which are  layering. They  operations. Kulista and Wood (2020) marked intermittent spraying in
dominant at  CFD based results  the 3 days prior to arrival for loading as a common practice [109]. These
microgravity. were validated  understandings are very important sight for future hydrogen transport
with AS-203
|     |     |     | flight data. They  | studies regarding heel management. |     |     |     |
| --- | --- | --- | ------------------ | ---------------------------------- | --- | --- | --- |
concluded that
|     |     |     | surface tension  | 6. Effect of tank geometry on the thermodynamic performance  |     |     |     |
| --- | --- | --- | ---------------- | ------------------------------------------------------------ | --- | --- | --- |
effects are
of LH2 storage systems
significant.
| Melideo,  | They studied the  | Their concern  | Results showed  |     |     |     |     |
| --------- | ----------------- | -------------- | --------------- | --- | --- | --- | --- |
Baraldi, De  effect of injector  include: high initial  that upward  To understand the thermal performance of liquid hydrogen storage
Miguel  diameter,  gas temperature  injectors reduced  tanks, Wang and Merida (2024) [110] conducted an analytical study
Echevarria,  direction, and  increases  stratification, and  where they compared different tank shapes (spherical, vertical cylin-
Acosta Iborra  gas temperature  stratification,  smaller diameter  drical, and horizontal cylindrical). They focused to analyze the impacts
| (2019) [97] | on thermal  | downward injectors  | promoted mixing.  |     |     |     |     |
| ----------- | ----------- | ------------------- | ----------------- | --- | --- | --- | --- |
of geometry on pressure rise, boil-off gas (BOG) generation, and overall
|     |     | worsen stratification,  | Additionally,   |     |     |     |     |
| --- | --- | ----------------------- | --------------- | --- | --- | --- | --- |
thermal behavior. They developed a non-equilibrium thermodynamic
7

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Table-4
Summary of major transportation options and limitations of hydrogen.
Transportation Description Efficiency/Losses Infrastructure Needs Limitations
Method
Pipelines [101] In this technique, hydrogen is Transport through pipelines Pipelines demand some basic Ley limitations include: risk of
transported under pressure through offer high efficiency for engineering pre-requisites. They need embrittlement and leakage. Long-
natural gas pipelines. These pipelines regional transport. hydrogen-compatible materials to distance pipelines also need very
are dedicated or repurposed for avoid the risk of embrittlement, and high capital investment.
transportation only. compressors to create sufficient
pressure difference for smooth flow.
NH3 Shipping [102] Hydrogen is transported as ammonia. This technique is efficient for This process needs mature global Key drawback is the toxicity
Later, it is cracked at destination. bulk transport. However, ammonia infrastructure. hazards of NH3. Additionally,
during unloading or extracting cracking offers significant cost, and
hydrogen from ammonia, purity concerns.
significant energy is required
for cracking
Liquid Organic In this technique, hydrogen is This method offers no boil-off LOHC shipping is compatible with The most significant drawback is
Hydrogen Carrier transported through liquid carriers and losses. It also provides fuel transport infrastructure. the high dehydrogenation energy
(LOHC) Shipping transported like oil. It relies heavily on reversible reaction cycle. input. Additionally, catalyst
[103] catalysts, which are used for degradation and limited cycle life
hydrogenation (storage) and are major constraints.
dehydrogenation (release)
Cryo-compressed This process needs hybrid of cryogenic This cryo-compressed This system needs advanced tank This technology is still
Hydrogen [104] storage. Hydrogen is stored and hydrogen has higher density technology, as the combination of experimental, and complete
transported through highly than either compressed or pressurization and cryogenic infrastructure has not been
pressurization. liquid hydrogen alone. This temperature brings several design established yet.
helps to carry more amount in a and operational challenges.
small space
model and did not assume that liquid vapor phases are always at the chain (land storage → loading → ocean transport → unloading). Addi-
same temperature. They found that spherical tanks performed best tionally, to analyze the factors which affect the losses was also a major
because they had the lowest pressure increase rate in self-pressurized objective of that study. They performed a technical analysis and sensi-
conditions. It happened due to their smallest surface area for the same tivity study to calculate daily BOG rates for each carrier, evaluate BOG
volume which reduced heat transfer from the environment. As a result, generation at different stages of transport, see how external factors such
spherical tanks showed the lowest BOG rate. Horizontal cylindrical as temperature, pressure, voyage time, heel percentage, and pumping
tanks performed better than vertical ones as horizontal tank-type offers time affect BOG formation, and compare how much energy each carrier
slow pressure rise than vertical cylinders. This occurred due to more can effectively deliver after accounting for those losses. Figure-2shows
effective heat transfer between vapor and liquid phases inside the tank. the total supply chain of hydrogen transportation and the challenge of
They found that higher fill levels help to suppress evaporation and BOG generation in every phase. Heat ingress happens in every phase
pressure rise because a higher initial liquid level increases the thermal which causes significant amount of hydrogen losses through boil-off
mass of the liquid. So, it takes more heat to raise the temperature and [111].
cause evaporation. Additionally, the BOG rate was lowest in spherical They found that hydrogen showed highest daily BOG losses as
tanks at atmospheric pressure. But, both horizontal- and around 3.438%, and methanol showed lowest daily BOG losses as
vertical-cylindrical tanks showed almost the same BOG rate under at- around 0.049%. LNG demonstrated the second highest daily BOG losses
mospheric condition. as 0.471%, but it is still far less than for the case of hydrogen. Among the
Although their study offered valuable insights regarding the effects different stages of the supply chain, ocean transportation phase offered
of LH2 tank size on the thermal performance of the tanks, some unre- the main source of losses due to the long exposure time and large tank
solved challenges exist. Spherical tanks showed better thermodynamic surface area. They concluded that DME carried the most energy effi-
performance, but such tanks with good geometry still faced continuous ciently, Methanol had the least storage losses, and Hydrogen had the
heat ingress, which indicates the insulation limitations for perfect worst performance in terms of mass loss due to evaporation [111].
elimination of BOG. Their study mostly considered stationary storage or These findings are based on large-scale, long-distance marine
simplified thermal loads. But, moving ships experience different prac- transportation under fully refrigerated conditions. All the energy car-
tical phenomena, such as sloshing, vibrations, varying external condi- riers are assumed to be transported at atmospheric pressure (≈1 bar) in
tions, which were not considered in their study. Moreover, they cryogenic tanks. They assumed a fixed ship storage capacity of 160,000
addressed BOG management, but the risks of hydrogen leaks and ex- m3. It consists of four spherical tanks with a radius of 21.23 m. These
plosions in real-world environments were not studied. These unresolved assumptions enable a fair comparison across carriers. For LH2, this
challenges open the pathway for potential future research directions corresponds to a total stored mass of approximately 2.84 ×106 kg. The
including BOG suppression strategies, large-scale validation, dynamic baseline voyage duration is assumed to be 30 days. This duration rep-
behavior studies, optimization of advance insulation materials and tank resents long-haul overseas routes and identified as the dominant
geometry etc. contributor to total BOG generation. Passive insulation is considered,
with an overall heat transfer coefficient of approximately 0.1 W/m2K for
7. Comparative analysis of liquid energy carriers and boil-off hydrogen tanks. In the reference case, no active BOG re-liquefaction or
gas (BOG) losses utilization is assumed. Under these conditions, the extremely low boiling
temperature of hydrogen results in a large temperature gradient be-
Al-Breiki and Bicer (2020) compared five potential energy carriers tween the stored medium and the ambient environment. The study
that can transport energy (especially from natural gas) over long dis- assumed ambient temperature variations between 10 ◦C and 50 ◦C, and
tances in liquid form [111]. The five carriers include Liquefied Natural considered an increase of BOG rates by approximately 0.1%. But,
Gas (LNG), Dimethyl Ether (DME), Methanol, Ammonia, and LH2. The increasing storage pressure from 1 bar to 70 bar, reduces total BOG
study focused on how much BOG each carrier loses during the supply losses by about 0.3%. Additionally, higher heel percentages and longer
8

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-2. Schematic diagram of supply chain of Hydrogen transportation system. The supply chain starts from the land storage of hydrogen, and then continues to
loading process, ocean transportation, unloading process, and finishes with land storage again. Among these phases ocean transportation offers the most significant
BOG generation due to long term exposure to environment and large tank surface area [111].
pumping times during loading and unloading phases further increases reduce the BOG generation and the transportation cost, several options,
LH2 boil-off. This is occurred due to the increased thermal interaction such as storing LH2 under higher pressure to decrease venting, or using
and auto-refrigeration effects. The absolute magnitude of the daily BOG BOG as fuel for the ship instead of venting, or sailing the ship faster to
rate is sensitive to tank design, insulation performance, storage pressure, shorten voyage time, can be adopted. But all these choices affect eco-
voyage duration, and BOG management strategies. But, hydrogen nomic (NPV) and cargo delivery. To make a comparative cost assess-
consistently exhibited the highest boil-off losses among the evaluated ment of the transportation of different natural-gas-derived energy
carriers across all examined scenarios [111]. carriers, Al-Breiki and Bicer (2020) conducted another analytical study,
considering both BOG losses and the social carbon cost (SCC) [112].
8. TECHNO-ECONOMIC analysis of LH2 transportation and boil- They analyzed five liquefied carriers: LNG, DME, methanol, ammonia,
off gas (BOG) utilization strategies and LH2. Figure-3 demonstrates the graphical abstract of their study
which represents the overall cost structure. It is segmented into two
8.1. Comparative cost assessment of liquid energy carriers sections: the upper section showing the cost of the conversion of natural
gas into liquefied forms, and the lower section showing the trans-
Transporting LH2 is expensive and technically difficult. The eco- portation costs to demanded regions. All the costs are classified into
nomic feasibility of large-scale LH2 transport comparing to other Capital Cost, Operations Cost, Boil-Off Gas Cost, and Social Carbon Cost,
natural-gas-derived energy carriers shows significant challenges. To where the Operation Cost for transportation includes various charges (e.
Figure-3. Graphical abstract of the study conducted by Al-Breiki and Bicer (2020) [112]. It is segmented into two critical cost-phases of the supply chain: Production
Cost of converting natural gas energy into a liquefied form of energy (upper section), and Transportation Cost (lower section). The cost analysis includes five energy
carriers: LNG, LH2, liquid ammonia, methanol, and DME. All are derived from natural gas.
9

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
g., port charges, fuel cost, insurances etc.). The generated BOG during BOG losses of LH2 are the primary reasons for this most intensive cost
production of a liquefied energy carrier is managed by two ways; either requirement. But, in the case of short-distance routes, low hydrogen
it is vented to the environment or sent to a re-liquefaction facility. In this production costs, or high carbon pricing regimes, the scenario changes
study, this lost BOG is accounted for within the total production cost. much. In that cases, LH2 and liquid ammonia become increasingly
The same approach is applied in the case of transportation where the lost competitive relative to LNG. These results indicate that absolute cost
mass due to BOG is accounted as a cost. The figure is added to represent values are sensitive to future market and policy conditions, but the
the holistic cost assessment instead of just showing simple costs qualitative ranking of energy carriers and the dominant cost drivers
regarding fuel prices or shipping fares. The most significant feature of (liquefaction energy demand, BOG management, carbon pricing) would
this figure is the addition of BOG cost and Social Carbon Cost (SCC) remain robust across potential future scenarios. And these robust con-
which is the two major challenging factors for liquid energy trans- clusions are not newly assumed in this work, rather they are evaluated
portation, especially for LH2 transportation. from the original study of Al-Breiki and Bicer (2020) [112].
Figure-4shows the results of the cost analysis of the mentioned five
different energy carriers in $/GJ. In every case, the costs are divided into
8.2. THERMODYNAMIC-ECONOMIC coupling for BOG utilization
Capital Costs, Operating Costs, and BOG Costs. It demonstrates that LH2
exhibited the highest transportation cost of about 3.74 $/GJ, even after
To analyze the cost constraints and the most effective option to
accounting for carbon externalities. This amount is substantially higher
handle BOG, Wang et al. (2025) conducted a study using thermody-
than LNG (0.74 $/GJ) or liquid ammonia (1.09 $/GJ). Among these five
namic storage model and ship fuel consumption model to simulate
cases, the cost of LH2 in all the three departments (Capital Costs,
voyages [113]. They analyzed the feasibility to recover and use of BOG
Operating Costs, and BOG Costs) is the highest. Several factors, such as
instead of being vented and wasted. They examined the potential to use
the low volumetric energy density, extreme cryogenic temperature
requirement ((cid:0) 253 ◦C), and significant BOG losses during long voyages this BOG for ship propulsion or onboard power generation as a sec-
ondary energy source to enhance voyage efficiency and reduce fuel cost.
due to extremely sensitive to heat, are primarily responsible for this high
Their study looked at a 160,000 m3 LH2 carrier. Their thermodynamic
transport cost of LH2. The study also indicated that the inclusion of SSC
and economic model combined three sub-models which are presented by
favors carbon-free carriers such as hydrogen and ammonia. But the
Figure-5. It includes a storage BOG model to estimate BOG generation
economic advantage of LH2 does not show sufficient potential, as the
rates, a propulsion model based on ship cruising power, and a ship
BOG-related energy and mass losses dominate the cost structure [112].
resistance model to determine fuel consumption [113].
The cost figures are derived under some clear baseline assumptions.
Figure-6demonstrates the overall powertrain of the ship, which is a
For the comparative carrier assessment, the assumptions are: base nat-
ural gas price is 2 $/GJ, ship capacity is 160,000 m3, fixed cruising speed combined gas and steam (COGAS) turbine system that generates elec-
tricity [113]. The engine powers a generator and then the generator
is 20 knots, and a representative long-haul distance is 12,000 km. The
powers an electric motor that turns the propeller. The figure highlights
sea-route is assumed from Qatar to Japan [105]. Liquefaction, storage,
and transportation costs explicitely account for BOG generation. This is
that (cid:0)power is needed for both propulsion (Pthrust )and for auxiliary sys-
true for both production and shipping phases and is treated as an eco- tems Pauxiliary). The powertrain includes a fuel cell which is an optional
nomic loss rather than an externality. Fuel prices for marine operations component to provide the auxiliary power. It potentially uses BOG
are based on heavy fuel oil at 0.58 $/kg. At the same time, the envi- directly with high efficiency. In the figure, Paux,fc is the electrical power
ronmental externalities are incorporated through a social cost of carbon for the ship's auxiliary purpose, supplied by the fuel cell. Paux,COGAS is the
(SSC) baseline of 46 $/t CO2eq and consistent with widely adopted auxiliary power supplied by the COGAS engine's generator. Pbrake,COGAS is
mid-range estimates [112]. the total mechanical power output from the COGAS engine's rotating
But, variations exist in key uncertain parameters. These include shaft, which is split between propulsion and auxiliary needs. Pthrust,COGAS
natural gas price (1-4 $/GJ), shipping distance (2400–12,000 km), ship is the portion of the COGAS engine's electrical output that is dedicated to
capacity (100,000–250,000 m3), and social carbon cost (13-137 $/t the propulsion motor to drive the ship forward. Peff.thrust is the final useful
CO2eq). Across these ranges, LH2 transportation consistently remains power after accounting all losses. It actually pushes the ship through the
the most cost-intensive option on a per-unit-energy basis. This is espe- water.
cially true for long-haul routes. This is primarily due to its Low volu- They proposed four operational modes to simulate how BOG can be
metric energy density, high liquefaction energy demand, and significant utilized during voyages which are represented by Figure-7. Mode A
offered conventional operation using marine gas oil (MGO). In this case,
all BOG was vented and burned in a gas combustion unit. Mode B was
similar to Mode A but included a proton exchange membrane (PEM) fuel
cell, which was powered by BOG for auxiliary power generation. Mode C
was based on full BOG-fuelled propulsion. In this case, all generated
BOG fed the combined gas and steam (COGAS) engine. Forced BOG
generation was applied when the BOG rate was lower than the propul-
sion demand. This was done by vaporizing additional LH2. Mode D
offered hybrid approach. It used BOG for propulsion which was sup-
plemented by an onboard LH2 fuel tank when natural BOG generation
was insufficient, especially during ballast voyages [113].
Figure-6 and Figure-7are added to understand the possible pathway
to use BOG while transporting LH2 instead of wasting. They demon-
strate that BOG is a fuel, not just waste. They also exhibit that system
integration is the key which indicates the choice of propulsion system
(COGAS, fuel cell) is deeply interrelated with cargo tank management.
Figure-7 also shows the operational flexibility by depicting different
Figure-4. Graphical representation of the transport cost ($/GJ) of energy
modes of BOG uses based on the fluctuation of BOG generation.
transportation. It includes the transportation cost of LNG, liquid ammonia,
methanol, DME, and liquid hydrogen. The costs include three distinct types of They also investigated how tank pressure (MAWP), and cruising
costs: capital cost (represented by green color), operating cost (represented by speed affect BOG losses, fuel costs, and net present value (NPV). LH2
white color with blue lines), and BOG cost (represented by yellow color) [112]. transportation offers complex pathway and inherent losses at every
10

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-5. Thermodynamic and economic model including three sub-models: storage model, propulsion model, and ship model. It shows the relationship between
ship parameters, the ship and its resistance, propulsion, cryogenic storage models, and broader economic model. The authors of this model stated that the dependence
of fuel consumption estimation on the storage model output was applied only when hydrogen was used as a fuel [113].
streams and expected losses [113]. The losses include both liquid and
gaseous phase across a single round-trip journey. It starts from pro-
duction and liquefaction to the laden voyage, unloading, and the return
ballast voyage.
The comparison between conventional marine gas oil (MGO) and
hydrogen was also done to understand how they affect the mentioned
terms. Their study focused on some challenges; higher tank pressure
reduces BOG but lowers allowable fill level, higher speed reduces losses
but increases fuel costs, and uncertainty in carbon pricing and hydrogen
market price. They built a physics-based analytical model to simulate
tank heat gain and BOG with different MAWPs, and to analyze fuel use at
different ship speeds. They also conducted some case studies for various
voyage distances, hydrogen prices, and fuel prices. Their study
demonstrated that higher MAWP improves storage efficiency but lowers
fill level. Ship speed didn't affect much to BOG reduction. The main
effect of ship speed is more annual deliveries. In the case of fuel choice,
MGO is cheaper when carbon price is not considered. But hydrogen fuel
becomes competitive when carbon price is considered. Another key
finding was when ship needs more fuel than natural boil-off provides,
forced boil-off is required. But this technique showed less efficiency. For
short voyages, there's no big need to store hydrogen under high pressure.
And, when hydrogen pricing is high, it's better to keep as much liquid
hydrogen as possible rather than lose it as BOG. In both cases, operating
the storage tanks at atmospheric pressure is more economical than
operating at increased pressure. Additionally, optimizing both ship
Figure-6. Integrated powertrain architecture for a COGAS-electric LH2 carrier.
speed and MAWP could add up to 180 million USD net present values
It shows the general power flow from fuel to propeller. It integrates both the
main COGAS engine and a potential fuel cell for auxiliary power [113]. (NPV). They concluded that hydrogen production cost, and voyage
distance are the main drivers for economic benefits, not ship parameters
[113].
stage. To analysis the losses Figure-8is added which maps the hydrogen
Figure-7. Operational modes for BOG utilization in LH2 carrier propulsion. It comprises schematic of the four fuel management strategies: (a) conventional MGO,
(b) COGAS engine's power with BOG for auxiliary power via fuel cell, (c) BOG for main propulsion, and (d) BOG with an LH2 fuel tank to cover fuel deficits [113].
11

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-8. Schematic diagram of the LH2 export pathway. It was analyzed by Wang et al. [113] and they focused on the loss mechanism. The diagram presents the
continuous BOG formation during storage (liquefaction, heel) and voyages, and the discrete losses during different operational phases such as loading, unloading, and
tank chill down The grey and blue colors represent gaseous and liquid streams, respectively.
This study was the first one to analyze the interaction between tank 8.4. Operational challenges and economic implications of LH2 shipping
MAWP, fuel type, and speed. Previous studied didn't combine all these for maritime operators
three variables. But this study offers some unresolved challenges. The
data on LH2 ship construction cost (CAPEX), and how MAWP and The discussed theoretical and simulation-based studies provide
insulation affect it were limited. Several variables including hydrogen valuable insights on BOG losses and transportation costs for LH2. But
selling price, carbon tax, and fuel costs fluctuate a lot which show un- shipping companies face real-world operational challenges which can
certainty in hydrogen markets. Hydrogen engines and onboard BOG significantly affect performance and economics. Ferrari et al. (2023)
management are not still mature which paves the way to conduct more showed in their study that there is a rise in maritime transport costs
studies on hydrogen engines. during the 2021-2022 global shipping surge. They showed it to
demonstrate the increasing shipping rates by up to 30-40% container-
8.3. Scenario-based assessment of carbon pricing and route length ized and bulk cargo. This led to reduced trade flows and increased
commodity prices [114]. Regions with limited port infrastructure and
Wang et al. (2025) explicitly evaluated fluctuating carbon prices in inflexible logistics experienced disproportionate impacts. These high-
their study. They also included multiple shipping routes in their anal- light that operational constraints, such as port congestion, limited berth
ysis. In their study they examined a range of carbon price scenarios, availability, and reduced options for alternative shipping routes, can
which was approximately 70 to 250 $/t-CO2eq, through their impact on amplify the economic burden of transporting sensitive energy carriers
effective marine fuel cost [106]. The results demonstrate a clear un- like LH2.
derstanding that without carbon pricing conventional marine gas oil In addition, shipping companies' strategic decisions under cost
(MGO) remains economically preferable. But, under moderate to high pressures can further influence operational outcomes. Wu et al. (2025)
carbon prices, such as around 70-150 $/t-CO2eq and above, analyzed the digitalization of the shipping industry. They demonstrated
hydrogen-fuelled propulsion becomes increasingly favorable. This yields that investment costs and operational efficiency interact to produce non-
NPV gains of up to 180 million USD under high-carbon-price scenarios linear effects on freight rates and profitability [115].For example, uni-
[113]. lateral adoption of efficiency-enhancing digital technologies can yield a
Similarly, they assessed route-dependent scenarios by varying ‘winner-takes-all’ advantage. On the other hand, simultaneous adoption
voyage distances between 4000 and 12,000 km [113]. These assess- by multiple operators may reduce collective profits due to competitive
ments correspond to representative short-, medium-, and long-haul pressures [115]. This scenario is analogous to LH2 shipping. As, in this
shipping routes. Shorter routes reduce cumulative boil-off losses and case, individual carriers may hesitate to implement advanced BOG
favor lower tank pressurization. On the other hand, long-haul routes management. Additionally, high upfront costs and market uncertainties
amplify the importance of cruising speed optimization and boil-off are two other major challenges for shipping companies. Due to these,
management. Although absolute cost and NPV values vary across they would show less attraction to adopt high-efficiency propulsion, or
these scenarios, the dominant economic drivers remain constant. These optimized scheduling.
include voyage distance, hydrogen production cost, boil-off gas utili- In summary, it can be concluded that LH2 shipping is not only
zation strategy, and carbon pricing. All these assessments indicate that challenged by its inherent technical constraints but also by the broader
the qualitative techno-economic conclusions for LH2 shipping are robust operational and economic environment. Port infrastructure limitations,
across a wide range of long-term operation al scenarios. This is also true long-haul voyage distances, fluctuating fuel costs, and carbon pricing
for LH2 based policy scenarios. policies can all materially affect shipping companies’ decision making.
The analyses presented in Section 5-8are based primarily on theo- Based on these, the companies shipping efficiency and profitability also
retical models, numerical simulations, and extrapolation from LNG fluctuate. Therefore, optimizing LH2 transportation requires an inte-
operational experience. These models provide insights into heel man- grated approach that considers both technical performance of storage
agement, tank geometry, BOG generation, and economic feasibility of and BOG utilization systems. They would need practical operational
LH2 shipping. But, they are not directly validated against full-scale factors among carriers. Overall, these factors include infrastructure
operational LH2 carriers. The current limited availability of full-scale readiness, route planning, regulatory frameworks, and cooperative
vessels have made it difficult to real-world experimental validation. strategies. The combined approach would help the shipping companies
Therefore, the results should be interpreted as predictive and indicative, to mitigate challenges and gain profit efficiently.
rather that fully verified at commercial or pilot-ship scale.
12

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
9. Cooldown strategy and thermal management of LH2 carrier They used analytical methods in MATLAB to build a thermal model for
tanks LH2 and LNG tanks [76]. They used this model from a previous study of
them, which is described in the later part of the manuscript. The model
Studies in literature with considering the cool down strategy, man- included 2D insulation and lumped vapor/liquid masses. This model was
agement, and associated challenges of the cryogenic tanks of LH2 car- used to resolve tank wall, insulation, liquid, and vapor interactions
riers are very limited. Wang et al. quote this demonstration in their study during the entire round trip (ballast +laden) voyage. Figure-9repre-
at 2024 [76]. The authors of this study have also not found any specific sents the analytical lumped mass model of their study [76]. This pro-
detailed study based on cool down management of LH2 cryogenic tanks. vides a robust framework for simulating the heat and mass transfer
But there are sufficient studies to analyze the cool down challenges of within a cryogenic cargo tank. This approach involves two inter-
LNG carrier tanks. In 2008, Lee et al. conducted scaled down experi- connected components. The first one is the phase discretization and
ments using 200 m3 prismatic LNG tank model. In this experiment, stratification modeling (left panel). It involves two distinct lumped
liquid nitrogen was employed as a substitute cryogen to replicate the masses: one for the liquid and another one for the vapor. The vapor mass
thermal behavior of LNG systems. The experiments simulated the initial is further divided into vertical sub-layers. It is done to accurately capture
cool down from ambient temperature to cryogenic conditions. Results thermal stratification phenomenon in the vapor space (ullage) which is a
showed a significant time lag between the temperature drop in the vapor key factor for heat transfer and evaporation rates. The second compo-
region and the response of the insulation layer. It also highlighted that nent is the thermal resistance network (right panel) which represents the
vapor-space cooling occurs much faster than heat removal from the tank conductive and convective heat transfer through the tank's insulation
walls and insulation [116]. Lu et al. (2016) performed numerical system and walls. This ultimately solves the total heat flux into the liquid
modeling of the cool down process in a large prismatic LNG tank [117]. and vapor masses.
They focused on coupled heat transfer and phase change processes. The They considered different cool down strategies such as continuous
simulation predicted limited vapor phase thermal stratification as spray vs. intermittent spraying and allowed tanks to warm up to different
cooling and evaporation effectively mixed the vapor. They demon- temperature limits. They also included the effect of tank wall and
strated that the inner tank wall reached the liquid stratification tem- insulation thickness of tanks due to the wall being thicker in the case for
perature within approximately 2 h. This marked the end of the rapid LH2 tanks. They looked at heat transfer, residual energy, and boil-off
cooling stage. After about 12 h of continuous cooling, a linear temper- generation during ballast voyage, pre-cool-down before reloading, and
ature gradient developed within the inner insulation layer. This indi- laden voyage. The outcomes of keeping tank cold vs. letting it warm up,
cated the establishment of quasi-steady conductive heat transfer [117]. and spray cool-down modes were compared [76]. Figure-10illustrates
The study provided valuable insights into transient wall and insulation the overall process of bulk carriage and unloading. It shows how the
temperature distributions. These are critical for assessing thermal stress, cargo is handled throughout a complete voyage cycle. It includes four
cool down time, and cryogenic efficiency. The findings also supported phases of the total voyage. The first phase starts with laden voyage (full
the design of optimized spray-cooling strategies. There are other studies tank). The ship departs with fully loaded cryogenic tanks toward
on thermodynamic response in LNG storage tanks under static pressur- receiving terminal. It carries LNG or LH2. Then, comes the second phase:
ization and sloshing conditions [118]. These studies solely investigated unloading process. At the destination, the liquid cargo is discharged to
the thermodynamic and cool down characteristics of cryogenic tanks of port storage facilities. The third phase is the ballast voyage which rep-
LNG carriers. But due to the different thermal behavior of LH2, the resents the return trip. The ship returns with nearly empty tanks. It
findings from these studies cannot guarantee the cool down timing, heel contains only a small remained heel. During this stage, thermal strati-
management, or other thermodynamic estimations of cryogenic LH2 fication occurs due to the low fill level [120,121]. The upper vapor
tanks. layers warm faster and increases the tank's internal temperature. The
To analyze cool down management of ship-borne cryogenic storage final phase is the pre-cool down before reloading. The remaining heel
tanks of LH2 carrier during ballast voyage, Wang et al. (2025) first liquid at the third phase is sprayed inside the tanks through internal
conducted a study comparing LNG vs LH2 ballast voyage strategies. spray bars to cool down the tank walls. This is conducted before the
Figure-9. Schematic of the analytical lumped mass model for cryogenic tank thermodynamics. Figure (a) represents the discretization of the tank's vapor and liquid
phases. It illustrates the lumped mass approach with vapor sub-layers and used to model thermal stratification. Figure (b) shows the corresponding thermal resistance
network for the insulation and tank walls to calculate heat ingress to the system. The assumptions of this model include: considering axisymmetric conditions, and
neglecting sloshing and para-ortho hydrogen conversion [76,119].
13

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-10. The schematic representation of the overall process of bulk carriage and unloading. It includes four phases: laden voyage (full tank), unloading process,
ballast voyage (return trip), and pre-cool down before loading. Stratification occurs at the third phase when the ship is onboard with little heel in the tanks. Spraying
of tank walls are conducted in the fourth phase [76].
arrival of the ship at the loading terminal. This ensures safe and efficient kinds of secondary level heat transfer. But, the heat transfer amount
reloading of the next LH2 batch, and these 4 phases repeat again [76]. through these structures are not too less to be ignored and can contribute
Figure-10is added to understand the operational management pro- significantly to total heat ingress. So, the accurate thermodynamic
cess of a full LH2/LNG shipping cycle. It shows how temperature control prediction needs all of these practical heat transfer ways to be analyzed
and pre-cooling are managed between unloading and reloading. for better tank performance and re-liquefaction load sizing. Moreover,
The results demonstrated that allowing the tanks to warm up during this study assumes a certain heel mass and sprays frequencies for cooling
ballast voyage helps reduce overall round-trip losses. This reduction is objective, but does not optimize them or specify them for ultimate
approximately 32-56.3% for LNG and 41.6-54.3% for LH2. This is effectiveness. So, how much heel volume is actually needed for specific
because less energy is spent maintaining cryogenic conditions in empty voyages to obtain minimum round trip losses remains an open practical
tanks. But this increases excess boil-off during loading and laden voyage. and operational question. Lastly, the study does not couple the BOG
This value was found up to 17% for LNG, and up to 5% for LH2. The utilization for propulsion or power generation systems. This coupling is
results also exhibited that LH2 warms up more slowly than LNG due to important to analyze the performance strategy of thermal management.
the thicker insulation need of LH2 tanks along with heavier tank walls. In current LH2 transport systems, heel management practices are
Additionally, this slower warm up is also affected by hydrogen's higher primarily limited to small-scale vessels. The Suiso Frontier employs a
heat capacity. Results indicated that inner tank wall thickness is a key Type-C tank. It relies on maintaining a minimal liquid heel during ballast
factor in thermal response. They concluded that optimal strategy de- voyages to preserve cryogenic conditions. This also limits tank cooldown
pends on voyage length, ship's BOG handling equipment (compressors, requirements prior to reloading. In this case, conservative operational
re-liquefaction), and fuel consumption profile [76]. control is followed for heel management. Active thermal optimization is
These results of the reduction in heat accumulation associated with not followed that much. And, excess boil-off gas is managed through
controlled tank warm-up are based on analytical thermal-mass transfer controlled venting. Additionally, most advanced heel management
modeling. These values or results are not experimentally validated yet. strategies including controlled tank warm-up during ballast voyages and
So, the findings should therefore be interpreted as a modeling-based intermittent spry cooling before loading are still analytical or concep-
recommendation. Based on this, future work should focus on experi- tual. Due to the absence of large-scale LH2 carriers, these strategies
mental testing or ship-scale measurements. This testing should include cannot be tested in real-world scenarios. As stated before, Wand et al.
the verification of the predicted trade-offs between ballast-voyage heat (2024) and Wang et al. (2025) numerically showed that such advanced
accumulation and excess boil-off during loading and the laden voyage. strategies would reduce round-trip heat accumulation by approximately
This study is the first approach to systematically compare ballast 41-54% compared to passive thermal management [27,54]. These ap-
voyage management for both LNG and LH2 carriers. It significantly proaches have not been experimentally implemented yet, but they
highlights some of the key design parameters and their contribution for provide the first quantitative framework for LH2-specific heel manage-
thermodynamic performance of LH2 tanks. Key insights are related to ment. These studies also highlight the significant potential of applying
how design parameters, such as membrane vs. Type-B tanks, insulation these strategies in real-world large-scale LH2 carriers with systematic
thickness, and wall thermal mass, influence cool down efficiency and experimental studies, and omitting conservative strategies in current
BOG generation. One of the major challenges-finding balance between limited small-scale demonstration vessels. To the authors' best knowl-
reducing ballast BOG losses and the resulting increase in excess BOG edge, there are some vessels currently under construction with advanced
during loading plus next voyage is also examined in the study. This study innovations as LH2 carriers where active heel management would be
presents the first approach where this unique and numerical trade-off is considered. These include Kawasaki 40,000 m3 carrier (scheduled for
analyzed based on technical and operational perspectives. sea trials by 2030), Samsung Heavy Industries LH2 carrier (aimed at
Although this study demonstrates comprehensive approaches, commercialization by 2030), HD Hyundai LH2 carrier (scaling to 40,
fundamental results, and ways to overcome some key challenges of LH2 000 m3 by 2032). These informations are collected from online news. To
transportation, it offers some unresolved challenges and paves the way the authors’ findings, any dedicated research articles have not been
for future research directions. Several assumptions were considered found validating these information.
while modeling the system. The major ones include negligible droplet-
vapor interaction, lack of full scale experimental data on LH2 tank 10. Thermodynamic modeling and stratification behavior at low
cool down, heel management, heat transfer behavior during ballast fill levels in cryogenic LH2 tanks
voyages, etc. It also assumes idealized spray impingement for spray
cooling, and neglects droplet dynamics (size distribution, evaporation, 10.1. Design fundamentals of LH2 tanks at low fill levels
vapor interaction, etc.). Additionally, in practical case heat transfer
through support structures and ports occur, but this study ignores these When LH2 carriers have storage tanks with low fill levels, it becomes
14

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
very challenging to accurately predict heat transfer, stratification, and 10.2. Development of thermodynamic models and validation approaches
pressurization behavior by simplified thermodynamic models. In the
case of LH2 storing high-vacuum adiabatic low-pressure tanks are Although the studies conducted for LNG carriers give valuable in-
commonly used to minimize vapor losses. However, when the liquid sights towards LH2 transport, works on explicitly addressing heel car-
occupies a smaller volume relative to the vapor space, even minor heat rying practices in LNG are scarce. Most of the studies available are
ingress can cause significant self-pressurization and BOG [122–125]. operational or descriptive rather than analytical. So, the proper guide
Figure-11illustrates the fundamental design and structure of LH2 tank towards LH2 heel management and pertinent issues is also scarce [132].
that is used for storage and transportation purposes [123]. It comprises Studies show that the Suiso Frontier is the only operational LH2 carrier.
an inner vessel which is the primary container that holds LH2. It effec- It has small-scale Type-C tank of 12.50 m3, which is not representative of
tively shows how a storage tank is specially designed to minimize BOG, future large-scale commercial LH2 vessels [133–135]. So, the lack of
which is the most significant challenge for both LH2 storage and design data and performance validation for large LH2 tanks design and
transportation. The insulation layer is basically multi-layer insulation thermodynamic analysis is significant. There is also the absence of
(MLI) to effectively restrict heat transfer. It is located between the inner standardized heat transfer correlations for cryogenic hydrogen. Wang
vessel and the outer shell, and maintained under a high vacuum. Heat et al. (2024) developed a thermodynamic non-equilibrium model to
transfer through conduction, convection, and radiation are eliminated analyze how heat transfer, pressure rise, and BOG generation differ
by this MLI. The structural supports are designed with mostly depending on different variables such as tank geometry, operating
non-conductive materials to make those thermally inefficient and pressure, and initial liquid level [136]. They compared thermal perfor-
reduce heat transfer through these secondary parts. Additionally, un- mance among different tank shapes and investigated the effect of tank
avoidable heat ingress causes excess hydrogen vapor which are vented geometry on pressure rise rate, evaporation rate, and BOG losses. They
by pressure relief device. The transfer pipe is used for loading and demonstrated that non-equilibrium thermodynamic modeling better
unloading the LH2. The grounding point prevents static charge accu- captures the temperature differences between liquid and vapor phase. It
mulation and ensures safety [123]. is different from equilibrium models that assume uniform temperature.
At low fill levels, vapor volume increases and the rate of pressure rise In a previous study by Wang et al. (2023), they developed an analytical
accelerates. It is caused due to reduced thermal buffering of the liquid theoretical model to explain and quantify the heat distribution ratio
phase. This phenomenon emphasizes the need for accurate thermody- (HDR) [137]. Their investigation specially focused on the physical
namic modeling. To further enhance storage performance and reduce mechanism behind how heat leaks differently into vapor and liquid due
BOG, cryo-compressed hydrogen is being explored [126–131]. This to the inner wall's thermal conduction, the distinct thermal properties of
technology offers cryogenic storage and moderate pressure to achieve liquid and vapor hydrogen, and tank geometry and initial liquid fill
higher density. It combines the hybrid benefits and longer dormancy ratio. They developed the HDR model to replace the conventional and
periods. Figure-12 illustrates the design of a cryogenic-compressed less accurate uniform heat flux boundary assumptions. They analyzed
hydrogen storage system [131]. It is a hybrid technology that aims to the effect of different parameters such as fill level, total heat leakage,
overcome the key limitations of LH2 transport. The LH2 fill tube is used superheat, saturated pressure, and interfacial mass transfer rate on HDR.
for filling the tank with LH2. The vacuum pump out port is part of the They coupled the new HDR model with a Thermal Multi-Zone Model
insulation system. It creates a vacuum around the inner vessel, thus (TMZM) to achieve high-accuracy pressure predictions [137]. This
minimizing heat ingress and boil-off. The GH2 fill tube allows for approach reduced pressure prediction error by over 60% compared to
gaseous filling. The heat exchanger is a critical component that uses the uniform flux models. Their study uniquely developed a theoretical
cryogenic cold inside the tank. It cools the hydrogen gas being supplied model that quantifies how heat leakage is non-uniformly distributed
to the engine and improves efficiency by managing temperature. between vapor and liquid in LH2 tanks.
Overall, this design represents cryogenic liquid handling, gas pressure Matveev et al. (2023) conducted a study to analyze how the size of
management, integrated system operation, and critical safety systems, LH2 storage tank affects self-pressurization and venting behavior. They
which are prerequisites for LH2 storage and transportation. Although used a simplified lumped-element thermodynamic model that treats the
this design was provided with an aim to LH2 storage, it gives valuable liquid and vapor inside the tank as two uniform zones with average
insights for LH2 transportation. temperature and pressure [138]. They used this model to simulate how
heat leaks into the tank. This ultimately causes self-pressurization (when
the tank is closed), and constant-pressure venting (when hydrogen is
released to control pressure). They validated the model using NASA
experimental data from the Multi-Purpose Hydrogen Test Bed (MHTB)
tank [139] and applied it to tanks of different sizes (2-1200 m3). The
validation was performed against ground-based experimental data.
Following this laboratory-scale validation, the model was applied in a
parametric and scaling analysis to tanks of similar geometry with vol-
umes. This allowed assessment of size-dependent pressurization rates,
venting behavior, and boil-off losses. Figure-13shows the geometry of
MHTB tank. This tank is made of aluminum and also comparable to
space applications with full-scale cryogenic tanks. The total tank height
is 3.05 m. It has a vertical cylindrical insert of diameter 3.05 m and
height 1.525 m. The tank's top and bottom surfaces resemble
semi-elliptic caps, with a minor (vertical) axis that is twice as narrow
and two (horizontal) axes that have the same diameter as the cylindrical
section. A vacuum chamber holds the entire tank. The exterior of the
tank is coated with a 45-layer insulation blanket made of Dacron netting
Figure-11. Schematic of a typical cryogenic LH2 storage tank. The tank is
and Mylar sheets, as well as a 1.4-cm-thick spray-on insulation. The
specially designed with a double-walled vacuum-insulated feature. There is an
experimental tank configuration also incorporates the control, transfer,
inner vessel that holds the cryogenic LH2. It is protected by vacuum multi-layer
insulation (MLI)., andholds the outer layer surrounding it to reduce heat and instrumentation systems [138].
transfer. Pressure relief device and grounding point ensure operational features Results showed that larger tanks experience slower pressure rise and
and critical safety [123]. lower relative BOG losses. The reduction was measured about 1.8% to
15

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-12. Schematic diagram of a cryo-compressed hydrogen storage system. It highlights the dual-function nature for handling both cryogenic liquid and high-
pressure gas. It includes key features such as separate fill ports for LH2 and GH2, a heat exchanger, multiple safety devices, and vacuum insulation. The vacuum
insulation is essential for maintaining cryogenic temperatures [131].
liquid or wall-vapor heat exchange in self-pressurization modeling.
Additionally, most existing models treat vapor and liquid as single nodes
[140,141]. These models fail to capture vapor thermal gradients at low
fill levels. This failure causes up to 60% under-prediction of wall internal
energy, especially at ≤5% fill conditions [142]. Some studies introduced
multi-layer vapor models, but their validation was limited to small
laboratory-scale vertical cylindrical tanks [143,144]. Moreover, previ-
ous studies focused mainly on full-tank steady-state conditions. The
transient thermal behavior when the tank is mostly vapor-filled, has not
been experimentally validated [145–152].
To meet up the mentioned research gaps and analyze the heel
required in LH2 transportation, and heat transfer and stratification
behavior in LH2 tanks compared to LNG tanks, Wang et al. (2024)
developed a new thermodynamic analytical model [142]. Their objec-
tive was to predict heat transfer into LH2 tanks, vapor stratification at
Figure-13. Geometry of Multi-Purpose Hydrogen Test Bed (MHTB) tank [138, low fill levels, and the effect of tank pressurization and insulation type.
139]. This tank is comparable to a full-scale cryogenic tank. It was extensively Their study focused on a 21-day ballast voyage scenario. They studied
used for experimentation by NASA and gives valuable insights for LH2 trans- how different insulation types perform to reduce heat ingress. They
portation by sea going vessels.
especially compared LH2 spherical tanks with perlite or polyurethane
foam (PUF) to LNG membrane tanks; as practices are mature for LNG but
0.2% per day for 2-1200 m3 tanks. They also demonstrated that BOG not for LH2.
losses scale approximately with the inverse of tank diameter. The In their study they mentioned one limitation of single-node models.
model's predictions agreed well with NASA's experimental data obtained Single node-models can only return a single mass-averaged vapor tem-
from MHTB tank. Although these findings are derived from stationary perature. At low fill levels, where substantial vapor thermal stratifica-
storage analysis, are highly applicable for LH2 carriers or LH2 trans- tion may be anticipated, this presents a problem. If the vapor is treated
portation. Because, in both cases BOG and maintaining pressure stability as uniform in temperature at the mass-averaged temperature, the in-
are two major challenges. However, the BOG and pressure pattern ternal energy of the wall will be underestimated for a partially filled tank
during transportation would vary due to the non-stationary feature and with a linear temperature distribution in the ullage (sub-portion a;
long-term exposure to surroundings. Fig. 14) and wall temperatures equal to the adjacent vapor and liquid.
It is important to clarify that the majority of thermodynamic models Sub-portion b of Figure-14quantifies the consequence of the simplifi-
developed for LH2 storage and transportation have been validated cation. It shows that when the hot vapor with a maximum temperature
against ground-based experimental facilities. Full-scale shipboard over 100 K exists, the simple single-node model significantly under-
measurements do not exist at full scale yet. In particular, the validation predicts the internal energy which is stored in the tank's steel wall.
of lumped-element and multi-zone self-pressurization models has pri- The wall in contact with the hot top vapor gets much warmer. Due to
marily relied on laboratory-to-pilot scale cryogenic tanks. These are that, the energy required to heat steel increases non-linearity at cryo-
operated under controlled conditions, such as the NASA Multi-Purpose genic temperatures. Prediction errors may surpass 60% at a fill level of
Hydrogen Test Bed (MHTB). 5% when maximum vapor temperatures surpass around 100 K. This is
These studies give valuable insights for thermodynamic modeling of explained by the fact that the specific heat of metals like stainless steel is
cryogenic tanks of LH2 carriers. But, in most of the cases they used highly sensitive to temperatures in the cryogenic range [142].
inconsistent tuning parameters for natural convection heat transfer They considered a double-walled cryogenic tank and it was initially
correlations. There is no consensus on accurate coefficients for vapor- close to 100% fill level under constant pressure venting, representing by
16

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-14. Impact of vapor thermal stratification on tank energy calculations at low fill level. (a) Represents the comparison between a realistic, stratified vapor
temperature profile against a simplified single-node model's mass-averaged temperature. (b) Shows the resulting under-prediction of the inner shell's internal energy.
It demonstrates a critical error that exceeds 60% at high stratification [142].
Figure-15. They assumed the inner shell temperature to be uniform and are represented by Equation (1), Equation (2), and Equation (3)
equal to the saturation temperature of the liquid for simplicity. They also respectively [142].
assumed the tank to be in a quasi-steady state condition [142]. This ∫
fi th g r u o r u e g h h e t l h p e s t t o an u k n w de a r l s l t s a . n It d a w ls h o e s r h e o t w he s h h o ea w t t c h o e m h e e s a f t r o in m g r a e n s d s l h e o a w ds i t t o m B o O v G es , θ 1 = Q 0 t s Q tea e d n y vir s o ta n t m e, e f nt × ald t t (1)
especially after the cargo is unloaded.
ana D ly u ti e c a t l o m t o h d e e l c w on h s ic tr h a i i s n t r s e p o re f se si n n t g e l d e - b n y o F d i e g u m re o - d 9 e [ l 7 , 6 t ] h . e T y h e p e ro x p p o la s n e a d t io an n θ 2 =∫ 0 tQ U en r v e i s r i o d n u m al entdt (2)
of the figure is presented in Section-9.
Uresidual =Utank (cid:0) Utank,steadystate,f (3)
10.3. Comparative heat transfer analysis for LH2 and LNG transportation The figure shows that the overall environmental heat transfer into
systems the tank remained nearly constant during the simulation period. It in-
dicates that only a limited reduction in heat load happened due to
Wang et al. accumulated the analysis of the heat buildup in near- allowing the tank to gradually warm up. Specially, the environmental
empty LH2 and LNG tanks during ballast voyage (return trip) in heat transfer for perlite-insulated LH2 tank decreased by only 3.6% after
Figure-16[142]. The figure represents the variation in Q Q ˙ e s n te v a ir d o y nm st e a n te ta ,f l , Q˙ e Q nv r ir e o si n d m ua en l tal 2 st 1 e a d d a y y - s s . t a B t u e t , c t o h n e d c it u io m n u s l a a t t i v 5 e % h e fi a l t l . t r T a h n e s f r e e r d w u a c s ti o 2 n .3 % in l i o n w st e a r n c ta o n m e p o a u r s e d a n t d o
, θ 1 , and θ 2 over 21 days for both LH2 and LNG cases at 5% heel under cumulative heat transfer for the polyurethane foam (PUF)-insulated LH2
atmospheric venting. U represents internal energy. θ 1, θ 2, and Uresidual
Figure-15. (a) Diagram of heat flow path within a double walled tank. Environmental heat constantly flows to the outer shell. Then passes through insulation, inner
shell, and finally enters the liquid hydrogen and creates BOG. Figure-(b) shows the heat pulse after unloading. The heat that was going into the liquid suddenly has
nowhere to go and causes a pulse of heat to build up inside the tank's structure. Figure-(c) shows the total heat stored in the tank walls cumulatively. When new, cold
LH2 is loaded, this heat is released into it. This causes a large and immediate burst of BOG [142].
17

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
Figure-16. Variation of thermal behavior in cryogenic storage tanks at 5% heel. These are measured under atmospheric venting conditions. (a)illustrates the ratio of
instantaneous environmental heat transfer to its steady-state value. (b)represents the ratio of tank heat gain to environmental heat transfer. (c)shows the dimen-
sionless cumulative environmental heat transfer, while (d)depicts the residual heat within the tank wall. The results correspond to a 21-day simulation period
following ship departure. It highlights the comparative thermal responses of LH2 and LNG tanks during low-fill operation [142].
tank is slightly higher, 8.7% and 5.7% respectively over the same period. Overall, this analysis highlighted that self-warming during low-fill
These findings demonstrate that the benefit of reduced environmental storage provides limited thermal relief on LH2 tanks than LNG sys-
heat transfer through tank warming is minimal. This is also true for the tems. This finding opens the pathway for precise thermodynamic
case of storage at low fill levels over several weeks. In contrast, the modeling. It also emphasizes effective insulation strategies when oper-
warming effect is more significant for the case of LNG carrier. The PUF- ating LH2 tanks at low fill levels.
insulated LNG tank experiences a 24% reduction in cumulative envi-
ronmental heat transfer after 21 days. The non-independent LNG tank
10.4. Long-term performance, aging, and lifecycle considerations of LH2
has a relatively thin inner wall. It stores only 7.9% of the total thermal
marine insulation systems
energy. This allows it to warm up more quickly and thus reduce heat
ingress from the environment. In comparison, the LH2 tank's inner wall
Unlike stationary onshore storage, shipborne LH2 tanks are contin-
contained about 76.6% of the total stored heat energy [142]. This results
uously exposed to dynamic mechanical loads. They also face cyclic
in slower wall temperature rise and smaller reduction in heat transfer
pressurization, sloshing-induced stresses, vibration, and a corrosive salt-
during same period.
laden environment. All of these can accelerate insulation degradation
They concluded that the LNG tanks demonstrated a tendency to
over the vessel lifetime. Vacuum-based insulation systems, such as
reach a quasi-steady thermal state within approximately 3 weeks. In this
evacuated perlite and multi-layer insulation (MLI), offer superior ther-
state, the heat transfer from the environment to the outer shell and from
mal performance at the beginning of service life. But their effectiveness
the inner wall to the internal fluid became balanced. Conversely, the
is highly sensitive to vacuum integrity. Over extended operational pe-
LH2 tanks continued to accumulate heat throughout the same period.
riods, gradual vacuum degradation may occur. There are various rea-
This reflected their higher insulation thickness and lower thermal con-
sons behind this. The most significant ones are: permeation, micro-
ductivity [142]. This continuous heat buildup in LH2 tanks emphasizes
leakage, seal aging, and outgassing of residual gases. These reasons
the need for careful design considerations. As proper design is manda-
are prominent especially during repeated warm-up and cool-down cy-
tory to prevent excessive pressure rise or BOG losses during extended
cles associated with ballast voyages. Even modest increase in annular
low-fill operation.
pressure can lead to a significant rise in effective thermal conductivity.
18

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
This increases heat ingress, self-pressurization rates, and cumulative at low fill levels. The cases of ballast voyages, cooldown periods, or
boil-off losses. So, periodic monitoring, re-evacuation, or insulation extended dormancy represent low fill levels phenomena. In these cases,
refurbishment is required to maintain long-term vacuum performance. strong vapor thermal stratification develops. This leads to non-uniform
However, these would introduce additional operational complexity and wall temperatures and significant heat storage within the tank structure.
lifecycle costs [142,153]. Single-node models are unable to capture these gradients. Previous
In contrast, non-vacuum insulation systems such as PUF show lower discussions demonstrate that they can under-predict wall internal en-
sensitivity to vacuum loss. But they are more susceptible to aging ergy by more than 60% at fill levels below approximately 5%. This even
mechanisms. These are related to moisture ingress, thermal cycling, and becomes more significant when upper vapor temperature exceed 100 K.
mechanical fatigue. Under marine conditions, repeated exposure to In summary, multi-zone models are therefore critical for accurately
temperature gradients, vibration, and structural deformation can induce predicting transient heat accumulation, excess boil-off during reloading.
microcracking and degradation of the foam matrix. These would create a There applications is also needed to perfectly assess cooldown re-
gradual increase in thermal conductivity over time. Moisture absorption quirements, and the resulting loads on boil-off gas handling systems.
further intensifies this effect. Particularly in humid maritime environ-
ments. This leads to irreversible deterioration of insulation performance 10.6. Ship-scale integration constraints of spherical cryogenic tanks
and increases boil-off rates [142,153].
From a lifecycle perspective, insulation aging directly influences Spherical cryogenic tanks offer superior intrinsic thermal perfor-
some major factors. These include long-term BOG generation, energy mance due to their minimal surface-area-to-volume ratio. But this
losses, and the effective cost of transported hydrogen. Short-term advantage does not offer that much impact while considering ship-scale
thermo-economic models typically assume constant insulation perfor- structural, stability, and operational constraints. Studies on structural
mance. But long-term degradation may shift the relative competitive- trade of spherical LH2 tanks demonstrate that vacuum-jacketed double-
ness of insulation concepts. This is especially prominent for long-haul wall configurations require independent load-bearing outer shells.
routes and high-utilization vessels. Consequently, insulation selection These are designed against external atmospheric pressure. Due to this,
represents not only a thermal design choice but also a strategic decision. extra structural features, such as stability-driven stiffening, increased
These would certainly affect maintenance schedules, vessel downtime, shell thickness, and additional structural mass, need to be considered
and lifetime operating expenditure [142,153]. [154]. These additions increase the overall thermal inertia of the tank
system. They also introduce extra conductive heat paths through sup-
10.5. Applicability and validation of reduced-order and multi-zone ports, penetrations, and attachment points. All of these contribute to
thermodynamic models passive heat ingress beyond that predicted idealized thermal models.
At the ship-integration level, spherical tanks are typically deck-
Based on the discussions on single-node and multi-zone models in mounted or semi-deck-mounted. This is especially observed in both
Section-9 and Section-10, several comments can be provided on the LH2 demonstrator vessels and LNG MOSS-type carriers. This arrange-
improvement of multi-zone models with real-world data to demonstrate ment significantly reduces volumetric packing efficiency, and results in
more practicality. According to analysis, current multi-zone and thermal unused hull volume and lower effective cargo density at the vessel scale
stratification models for LH2 tanks remain largely analytical. The scar- [155]. Additionally, the elevated vertical position of spherical tanks
city of full-scale experimental data has made its deployment feasibility raises the ship's center of gravity (CoG). This elevation brings the ne-
less practical. Current multi-zone models show potential predictive cessity to increased ballast and hull reinforcement to maintain intact and
capability in practice only by significantly improving through validation damage stability. These stability corrections subsequently increase
against real-world measurements. Different sectors of validation, such as displacement and wetted surface area. Based on the propulsion basics,
spatially resolved wall temperatures, vapor temperature gradients, and higher displacement and bigger wetted surface area increases the total
transient boil-off rates during ballast voyages and pre-cooldown oper- resistance and propulsion power demand [156]. These lead to higher
ations, need to be conducted. Data from instrumented large-scale LH2 fuel consumption and indirect operational energy penalties.
tanks (although very limited) would allow to standardize and fix some of Spherical tanks require additional structural supports, saddles, skirts,
the core issues like the refinement of interfacial heat transfer co- and deck foundations. These further increases parasitic loads and
efficients, vapor-wall convection correlations, and stratification decay introduce thermal bridges that bypass insulation layers and contribute
rates. Some of the key datasets need to be collected by distributed to steady passive heat losses. Experience from LNG MOSS carriers shows
temperature sensors along tank walls, vapor ullage thermocouples, and that these system-level penalties partially offset the low boil-off
heat flux measurements across insulation layers. Additionally, major advantage of spherical geometry [156]. This is truer for large-capacity
ship-scale operational data would enable calibration of model assump- vessels where deck space utilization and longitudinal weight distribu-
tions. These assumptions are related to spray impingement, mixing ef- tion become one of the most crucial design factors. These ship-scale
ficiency, and transient heat storage within tank structures. Spray cooling integration challenges are true for both LNG and LH2 carriers. This
effectiveness, heel distribution, and boil-off compressor loading profiles critique highlights that the thermodynamic superiority of spherical
are some of the major operational data in this case. Such datasets are tanks must be evaluated at the whole-ship level rather than at the iso-
currently unavailable for commercial-scale LH2 carriers. lated tank level.
Moreover, discussions can also be conducted on the area of accep- In summary, spherical LH2 tanks minimize local heat ingress, but
tance of reduced-order models and multi-zone models. Based on the their requirement for heavier structural systems, increased ballast,
understanding of model analyses, reduced-order single-node equilib- center of gravity and center of buoyancy elevation, reduced free deck
rium models are most likely to be acceptable in situations where tanks space, and higher propulsion energy demand substantially alters their
operate near steady-state conditions, with high fill levels, limited vapor potential performance advantage. These are true for both small-
space, and weak thermal stratification. Under such conditions, vapor demonstrate level and large-scale realistic marine operating conditions.
and liquid temperatures are relatively uniform. And, lumped-parameter
approaches can also provide important estimates of average pressure 11. Transferability of LNG heel management practices to LH2
rise and boil-off rates with minimal computational cost. This makes transportation systems
single-node models suitable for preliminary design studies. It is also
suitable for parametric sensitivity analyses, and operational assessments After analyzing heel management and thermodynamic behavior of
where detailed spatial resolution is not required. However, multi-zone LH2 carriers in parallel with LNG carriers, one key question arises:
or stratified models are likely to be essential when LH2 tanks operate which practices and strategies of LNG carriers are transferable to LH2
19

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
carriers, as they have different temperature and pressure limits. LNG high wettability, and low latent heat of LH2 compared to other cryo-
carrier operations provide valuable operational insights of maritime genic fuels, the thermal buffering capacity of LH2 is reduced. This en-
energy transportation. But all LNG heel management practices are not hances heat and mass transfer during interface motion [159]. As a result,
transferable to LH2 systems because of their different fundamental even short sloshing events can disrupt thermal stratification. It can also
thermophysical differences. Some practices are largely transferable. generate pressure oscillating, and increase localized evaporation during
These include maintaining a minimum heel to avoid full tank warm-up, long-voyages.
and intermittent spray cooling prior to loading. Moreover, recognizing At the ship scale, coupled thermodynamic-motion models show that
the coupled nature of ballast and laden voyage can also be a transferable LH2 carriers experience boil-off rates nearly nine times higher than LNG
area. These principles are rooted in general cryogenic thermodynamics carriers with similar insulation [160]. The most valuable finding in the
and remain valid for both LNG and LH2 carriers. case of sloshing effect is that the LH2 boil-off is approximately twice as
However, several LNG practices are not directly transferable; rather sensitive to sloshing effects under changing sea states [160]. Moreover,
they would need significant modification for LH2. While LNG tanks industry-led benchmark studies confirm that static heat ingress models
tolerate higher wall temperatures and higher MAWP, LH2 tanks operate are insufficient under dynamic sloshing conditions. They also highlight
at much lower temperature (20 K). LH2 tanks also go through stricter the need to explicitly account for coupled sloshing, heat transfer, and
pressure constraints. Due to these major mismatches, aggressive spray phase change in large-scale LH2 tanks [161].
cooling strategies, rapid cool-down rates, and assumptions of rapid wall
thermal equilibrium used in LNG are not directly applicable to LH2. 13. Future research directions
Moreover, LNG membrane tanks have lower wall thermal mass. This
allows faster warm-up and cool-down. In contrast, LH2 tanks exhibit The following potential future research can be conducted based on
significant thermal inertial due to thicker walls and insulation. ship-borne LH2 transportation.
Several LNG practices are fundamentally unsuitable for LH2 systems.
Allowing tanks to approach near-ambient temperatures during ballast a. Insulation is one of the most critical factors for tanks of LH2 carriers.
voyages, relying on high pressure operation to suppress BOG, neglecting Although, recent studies have taken into concern the impact of
vapor stratification effects are some of the fundamentally non- proper insulation and efficiency analysis, proper insulation thickness
transferable practices. Such practices would lead to excessive heat and material have still not been specified. Future works need to be
storage in the tank structure for LH2 carriers. They would also lead to conducted investigating the effect of different insulation thicknesses
severe BOG surges during reloading. All of these phenomena are with different insulation materials and how they will respond to the
demonstrated by recent analytical studies. efficiency of heat ingress reduction.
Based on these, cooling intensity, duration, and spatial distribution b. Spraying by cold LH2 before loading to maintain low heat gain in the
must be actively controlled and significantly reduced in the case of LH2. tank has been proposed to reduce BOG. Intermittent spraying can be
Any LNG-derived warming or cool-down practice of LNG should be an effective method in this case. The amount of spraying, the dura-
paired with tight pressure control. LNG assumptions of rapid wall tion of spraying, and spraying patterns such as continuous or discrete
equilibrium need to be efficiently replaced with time-dependent, inertia- spraying can be investigated to find out the optimal spraying tech-
aware thermal models. niques. Although the pattern will vary based on the LH2 tank size,
surrounding temperature, voyage duration, and tank material etc., a
12. Sloshing-coupled thermodynamics in LH2 maritime database can be produced for different patterns and variables by
transport continuous studies.
c. Tank size is a critical factor for LH2 carriers as ships undergo space
Ships face six degrees of motion in real-sea. These motions create constraints. Additionally, larger carriers increase the deadweight of
sloshing in LH2 tanks. The variation in stratification, rapid fluctuations the ship which affects resistance and fuel consumption for propul-
of internal vapor pressure, and heat transfer behavior changes with sion. Moreover, heavy structural design needs to be considered to
sloshing phenomenon. During long voyages, steady heat ingress through uphold the huge tanks. So, optimizing tanks size and shape is one of
tank insulation is the major driving factor of the long-term average boil- the most crucial factors. More experimental data on thermodynamic
off rate. Recent studies show that sloshing can introduce short-term efficiency across a broader range of tank sizes need to be
thermodynamic effects of comparable importance in LH2 tanks. Phase investigated.
change based CFD studies demonstrate that sloshing-induced interface d. The studies in Section-12indicate that sloshing-induced thermody-
deformation and repeated liquid-wall contact can significantly increase namic effects are intermittent, but their cumulative impact during
evaporation rates. This ultimately causes pressure fluctuations. But, to real maritime operation is significant. So, accurately estimating total
what scale these increased evaporation phenomena and pressure fluc- boil-off requires real-world sloshing phenomena to be integrated.
tuations would occur depend strongly on excitation amplitude, fre- Fully coupled hydrodynamic-thermodynamic models need to be
quency, and liquid fill level [157]. validated under representative ship motions. This sloshing-coupled
Numerical investigations of LH2 tanks under sinusoidal sloshing thermodynamics is a key research gap for LH2 maritime transport.
indicate that evaporation increases with acceleration amplitude and e. Optimizing fill level is another crucial concern. Although studies
decreases with increasing sloshing frequency. This acceleration is the have been conducted based on fill level effect and different scenarios
imposed acceleration of the LH2 tanks due to 6 DoF external motion of with different amount of fill levels, the optimized findings of fill level
the vessel. At the same time, higher storage pressure reduces pressuri- is still an underdeveloped sector. How much fill level is feasible to get
zation rates [158]. Considering realistic ship motion with conventional better techno-economical advantage is a potential research area.
excitation levels, the same study also reported that daily evaporation Again, the variation of fill level depending on potential BOG gener-
rates range from approximately 2.6% to 5.1% [158]. This highest ation and self-pressurization due to variable voyage duration, tank
margin of 5.1% represents a larger boil-off loss than the conventional geometry, tank material and insulation, and surrounding tempera-
boil-off loss measured without considering sloshing impact in the study ture etc. needs to be analyzed to better design of tank models and
of Al-Breki and Bicer (2020) [111]. These values suggest that sloshing analyze whole transportation scenario.
induced evaporation can locally match or exceed the contribution from f. Maritime LH2 transportation includes thermodynamics, operation,
steady conductive heat ingress over similar time periods [158]. and economics. So, integrated ship system studies that combine
Studies further explain the high sensitivity of LH2 to sloshing by its storage thermodynamics, powertrain options including MGO, BOG
fundamental fluid properties [149]. Due to the extremely low viscosity, and fuel cells, and voyage economics need to be conducted. Realistic
20

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
uncertainty in hydrogen production cost and carbon pricing should LH2 transportation faces different unique and critical thermody-
also be considered. namic phenomena. Recent advancements in thermodynamic modeling
g. Practical methods for BOG management should be studied. It needs have begun to address those issues. Non-equilibrium, multi-zone models
to include the analysis ranging from passive design (tank sizing/ demonstrate that vapor-phase thermal stratification at low fill levels can
insulation) to active systems (re-liquefaction, BOG-to-fuel systems, lead to >60% under-prediction of internal wall thermal energy. This
optimized heel and pre-cool strategies). These also need demon- happens when simplified single-node models are used. This under-
stration at representative scales. prediction affects crucial estimations such as BOG estimation, pressure
h. Specifically, studies are limited for describing ship capital costs in rise prediction, and re-liquefaction system sizing. Studies show that LH2
terms of tank MAWP or insulation type due to a lack of publicly tanks store almost 76% of accumulated heat in the inner wall during
available data. A broader range of tank MAWP and tank insulation ballast voyages and do not reach to a quasi-steady condition. Whereas,
techniques may be the focus of future research. Additionally most of LNG offers only around 7.9% heat accumulation in these cases. This
the studies are based on number of assumptions. The assumption higher percentage of LH2 compared to LNG causes persistent heat
should be specified for practical research output. ingress and delayed thermal stabilization. Studies show that if tank is
i. LH2 carriers can integrate dynamic wave energy conversion tech- allowed to warm during ballast voyage, round-trip losses can be reduced
nologies which can be a significant research area. Insights from the by a high amount of percentage (42-54%). At the same time this tech-
studies based on WEC can be applied to develop hull-integrated or nique introduces substantial excess BOG generation during both loading
bow-mounted oscillating water column modules [162]. These would and the subsequent laden voyage, which limits the potential of this
harvest wave-induced pneumatic energy during navigation. Such technique. It also indicates to perform integrated thermal management
systems could also provide auxiliary renewable power for rather than optional approach for efficient LH2 transportation.
re-liquefaction units, BOG compression, navigation loads, and on- The results from studies with different comparative modeling of
board hydrogen processing equipment. Research can be conducted insulation types confirm the limitation of insufficient thermal relief by
on the feasibility of this system to investigate how ship motion, hull current technologies. This is more acute during low-fill level conditions.
geometry, and variable sea states influence oscillating water column This drawback suggests the importance to conduct study for the opti-
aerodynamic performance. Specially, it is needed to analyze struc- mization of insulation technology including insulation thickness,
tural integration when coupled with cryogenic hydrogen systems. structural heat-leak sources, and tank material thermal conductivity.
j. Waste heat recovery from propulsion engines or hydrogen fuelled Moreover, although some studies have dealt with heel volume man-
power systems offer promising opportunity for future research. agement, but their optimization is still an unresolved area. This heel
Towhid et al. (2025) demonstrated waste heat driven onboard management optimization is needed as this factor is crucial for the key
desalination [163]. The same principles can be applied to LH2 car- thermodynamic and operational performance, such as pressure stability
riers where significant low-to medium grade waste heat is available inside tank, spray-cooling requirements, BOG recovery potential, etc.
and can be used for cryogenic tank operations. Future research Moreover, several complex performance variables were neglected in
should explore the close-loop water-energy system onboard LH2 previous studies. These include para-ortho conversion heat release,
carriers where desalinated water could be used for electrolysis sloshing-induced convection, droplet-vapor interactions during spray
feedstock at receiving terminals, cooling loops, or tank maintenance cooling, heat ingress through support structures, dynamic voyage vari-
operations. ations etc., all of which are crucial in real-sea transportation conditions.
In the LH2 supply chain, transportation remains the single largest
14. Conclusion cost element. This conclusion is demonstrated from techno-economic
assessments. Different strategies have been taken for BOG optimiza-
Liquid hydrogen (LH2) is increasingly recognized as an acceptable tion, but still LH2 shipping exhibits the highest cost per delivered energy
and efficient energy carrier. It is significant for enabling long-distance among major carriers. LH2 shipping yields a relatively high trans-
and large-scale energy transportation to achieve a future world with portation cost of around 3.74 $/GJ. This high cost is driven by high
net zero emission. LH2 carrier technology has significant strategic in- insulation demand, parasitic cooling loads, and BOG-dominant energy
terest, but it remains in an early development stage. The technical losses. The feasibility of LH2 transportation from the tech-economic
readiness level (TRL) of LH2 carriers is substantially lower than that of perspective depends on some fluctuating and unresolved phenomena,
LNG and other liquid energy carriers. This review consolidates the such as strong carbon pricing frameworks, mature liquefaction infra-
current state-of-the-art developments on LH2 transportation research. It structure, significant improvements in large-scale carrier design with
includes thermodynamic behavior, boil-off gas (BOG) management, optimized MAWP, tank sizing, propulsion hybridization with BOG or
tank design, cool-down strategies, optimized model build-up, and fuel cells, etc.
techno-economic considerations related to ship-borne LH2 trans- Non-equilibrium stratification modeling, heat distribution ratio
portation. All these sectors have been analyzed and accumulated to (HDR) formulations, and thermal multi-zone frameworks are some of
identify key scientific and engineering bottlenecks. the recent research advances in the LH2 transportation field. These
Different transportation techniques such as LNG, ammonia, LOHCs, advancements have significantly reduced computational inaccuracy.
DME, and methanol have their own advantages. But LH2 surpasses these These have also improved the predictive understanding of transient
technologies by its superior gravimetric density. However, it also suffers thermodynamics in LH2 tanks. Experiment-informed modeling indicates
from the lowest volumetric energy density and the highest refrigeration that larger tank diameters can cut relative BOG losses from around 1.8%
demand. The main challenge offers the largest BOG losses driven by to around 0.2% per day due to thermal inertia. This is validated against
extreme cryogenic conditions ((cid:0) 253 ◦C). It is evident that LH2 trans- NASA's MHTB tank data.
portation offers the highest BOG losses among major liquid carriers. Overall, this review demonstrates that the transition from LNG-based
During long-distance ocean shipments, this loss could become around design towards LH2-specific design is a time-demanded approach for
3.44% per day. Studies based on the commercial analysis reveals that ensuring zero-emission goal. This is also a fundamental scientific re-
ship-borne LH2 transportation technologies are significantly under- quirements based on complex engineering principles. The optimization
developed. Currently, only short-distance pilot operations and a single of maritime LH2 transportation needs more fundamental studies which
small-scale LH2 carrier (Suiso Frontier) is available commercially. It would include high-fidelity heat transfer correlations. For successful
indicates the huge lack of operational and experimental datasets which implementation, full scale experiments with considering sloshing-
are responsible for persistent uncertainty in model validation and inclusive transient models need to be performed. These are more
techno-economic feasibility. important for partially filled tanks which are the major center of focus
21

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
for all kinds of analysis. This technology needs integrated ship-energy [21] Krikkis RN. A thermodynamic and heat transfer model for LNG ageing during ship
systems which can be achieved by the accumulated study of thermo- transportation: towards an efficient boil-off gas management. Cryogenics 2018;
92:76–83.
dynamics, propulsion, and re-liquefaction for commercialization. [22] Krikkis RN, Wang B, Niotis S. An analysis of the ballast voyage of an LNG carrier:
Several key basics for holistic LH2 transportation study and develop- the significance of the loading and discharging cycle. Appl Therm Eng 2021;194:
ment, such as optimized cool-down strategy, heel management, and 117092.
[23] Moon, K., et al. (year unknown). Comparison of spherical and membrane large
insulation effects over varying voyage durations, need to be optimized
LNG carriers in terms of cargo handling.
further. For successfully deploying maritime LH2 transportation, shared [24] Lee JN, et al. A method for the prediction of heat capacity of LNG cargo tanks
industrial data and standardized performance metrics need to be accu- during cool-down and warm-up. SNAME Maritime Convention; 2008.
[25] Edeskuty FJ, Liebenberg D, Novak J. Problems in the operation of large cryogenic
mulated. Addressing these research gaps and working with the potential
systems. Los Alamos Scientific Laboratory; 1963.
optimization technique, ship-borne LH2 transportation technology can [26] Fu J, Wang J. Theoretical and experimental comparisons of self-pressurization in
turn into a cornerstone of the global renewable energy supply chain. a cryogenic storage tank for IoT application. International conference on internet
of things as a service. 2020. p. 296–309.
[27] Wang Z, M´erida W. Thermal performance of cylindrical and spherical liquid
CRediT author statement hydrogen tanks. Int J Hydrogen Energy 2024;53:667–83.
[28] Wang HR, et al. Theoretical investigation on heat leakage distribution between
vapor and liquid in liquid hydrogen tanks. Int J Hydrogen Energy 2023;48(45):
MD. Shajratul Alam Towhid: Conceptualization, Methodology, 17187–201.
Investigation, Writing - Original Draft, Writing - Review & Editing, [29] Matveev KI, Leachman JW. The effect of liquid hydrogen tank size on self-
Visualization. Sumaiya Binte Hossain: Investigation, Writing - Review pressurization and constant-pressure venting. Hydro 2023;4:444–55.
[30] Wang C, Ju Y, Fu Y. Dynamic modeling and analysis of LNG fuel tank
& Editing. pressurization under marine conditions. Energy 2021;232:121029.
[31] Ludwig C, Dreyer ME, Hopfinger EJ. Pressure variations in a cryogenic liquid
storage tank subjected to periodic excitations. Int J Heat Mass Tran 2013;66:
223–34.
Declaration of competing interest [32] Krenn A, Desenberg D. Return to service of a liquid hydrogen storage sphere. IOP
Conf Ser Mater Sci Eng 2020;755(1):012023.
The authors declare that they have no known competing financial [33] Wang Z, Sharafian A, M´erida W. Non-equilibrium thermodynamic model for
liquefied natural gas storage tanks. Energy 2020;190:116412.
interests or personal relationships that could have appeared to influence
[34] Al-Breiki M, Bicer Y. Investigating the technical feasibility of various energy
the work reported in this paper. carriers for alternative and sustainable overseas energy transport scenarios.
Energy Convers Manag 2020;209:112652.
[35] Al-Breiki M, Bicer Y. Comparative cost assessment of sustainable energy carriers
Data availability
produced from natural gas accounting for boil-off gas and social cost of carbon.
Energy Rep 2020;6:1897–909.
Data will be made available on request. [36] Wang A, et al. Analysing future demand, supply, and transport of hydrogen.
Guidehouse. 2021.
[37] Makepeace R, et al. Techno-economic analysis of green hydrogen export. Int J
References Hydrogen Energy 2024;56:1183–92.
[38] Rezaei M, Akimov A, Gray EM. Techno-economics of renewable hydrogen export:
[1] Pospíˇsil J, Charva´t P, Arsenyeva O, Klimeˇs L, S ˇ pila´ˇcek M, Klemeˇs JJ. Energy a case study for Australia-Japan. Appl Energy 2024;374:124015.
[39] Schuler J, Ardone A, Fichtner W. A review of shipping cost projections for
d fo e r m o a p n e d r a o t f i v li e q t u h e e f r a m ct a io l n e n a e n r d g y re s g t a o s r i a fi g c e a . t i R o e n n o e f w n S a u tu s r t a a l i n g a E s n a e n rg d y t h R e e v p o 2 t 0 e 1 n 9 ti ; a 9 l 9 o :1 f – L 1 N 5 G . hydrogen-based energy carriers. Int J Hydrogen Energy 2024;49:1497–508.
[40] Al-Breiki M, Bicer Y. Investigating the technical feasibility of various energy
[2] Shah YT. Chemical energy from natural and synthetic gas. first ed. CRC Press;
carriers for alternative and sustainable overseas energy transport scenarios.
2017.
Energy Convers Manag 2020;209:112652.
[3] Nwaoha C, Wood DA. A review of the utilization and monetization of Nigeria's
natural gas resources: current realities. J Nat Gas Sci Eng 2014;18:412–32. [41] M Hy a d k r e o p g e e a n c e E R ne , r e g t y a 2 l. 0 T 2 e 4 c ;5 h 6 n : o 1 - 1 ec 8 o 3 n – o 9 m 2. ic analysis of green hydrogen export. Int J
[4] Kurle YM, Wang S, Xu Q. Dynamic simulation of LNG loading, BOG generation,
[42] Rezaei M, Akimov A, Gray EM. Techno-economics of renewable hydrogen export:
and BOG recovery at LNG exporting terminals. Comput Chem Eng 2017;97:
47–58. [43] a W c a a n s g e Z s , t u M dy ´er f i o d r a A W u . s t T r h a e li r a m -J a a l p p a e n r . f o A r p m p a l n E c n e e r o g f y c y 2 l 0 in 2 d 4 r ;3 ic 7 a 4 l : a 1 n 2 d 4 0 s 1 p 5 h . erical liquid
[5] J n i a a t u W ra , l L g in a s Y l , i q Y u a i n d g s F tr , a L n i s m C. i s A si o n n o v p e i l p l e if li t n -o e f s f . d E i n a e m rg et y e r R e m p o 2 d 0 el 2 f 0 o ;6 r : b 4 o 7 i 8 li – n 8 g 9 b . ubbles in hydrogen tanks. Int J Hydrogen Energy 2024;53:667–83.
[44] Wang HR, et al. Theoretical investigation on heat leakage distribution between
[6] Seddon D. Gas transport. In: Gas usage and value: the technology and economics
of natural gas use in the process industries. PennWell Corp; 2006. p. 85–103. v 1 a 7 p 1 o 8 r 7 – a 2 n 0 d 1 l . iquid in liquid hydrogen tanks. Int J Hydrogen Energy 2023;48(45):
[7] Alkhaledi AN, Sampath S, Pilidis P. A hydrogen fuelled LH2 tanker ship design.
[45] Matveev KI, Leachman JW. The effect of liquid hydrogen tank size on self-
Ships Offshore Struct 2022;17(7):1555–64. pressurization and constant-pressure venting. Hydro 2023;4:444–55.
[8] Urabe H. Kawasaki technical review no. 182: special issue on hydrogen energy
[46] Lu X, Krutoff A-C, Wappler M, Fischer A. Key influencing factors on hydrogen
supply chain. Kawasaki Heavy Industries, Ltd; 2021.
storage and transportation costs: a systematic literature review. Int J Hydrogen
[9] Prevljak NH. ClassNK grants AiP to KHI for large liquefied hydrogen carrier. Energy 2025;105:308–25.
[10] B O a f h fs t h i´c o r F e . E T n o e ta rg lE y n 2 e 0 rg 2 i 2 e . s, BV, GTT and LMG marin to develop large-scale LH2 [47] Mekonnin AS, Wacławiak K, Humayun M, Zhang S, Ullah H. Hydrogen storage
technology and its challenges: a review. Catalysts 2025;15(3):260.
carrier. Offshore Energy 2023.
[48] Chilunda MD, Talipov SA, Farooq HMU, Biddinger EJ. Electrochemical cycling of
[11] Habibic A. McDermott firm gets DNV's blessing for liquid hydrogen cargo
liquid organic hydrogen carriers as a sustainable approach for hydrogen storage
[12] c B o a n h t t a i´c in F m . e M n o t s s s y s M te a m ri . t i O m f e fs 's h L o H re 2 E c n a e r r r g ie y r 2 c 0 o 2 n 3 ta . inment system gets DNV's nod. and transportation. ACS Sustainable Chem Eng 2025;13(3):1174–95.
[49] Shu K, Guan B, Zhuang Z, Chen J, Zhu L, Ma Z, Hu X, Zhu C, Zhao S, Dang H,
Offshore Energy 2023.
[13] Bahti´c F. DNV okays HD KSOE's hydrogen system for liquefied hydrogen carrier. Zhu T, Huang Z. Reshaping the energy landscape: explorations and strategic
perspectives on hydrogen energy preparation, efficient storage, safe
Offshore Energy 2023. transportation and wide applications. Int J Hydrogen Energy 2025;97:160–213.
[14] Leachman JW, et al. Fundamental equations of state for parahydrogen, normal
[50] Naseem K, Qin F, Khalid F, Suo G, Zahra T, Chen Z, Javed Z. Essential parts of
hydrogen, and orthohydrogen. J Phys Chem Ref Data 2009;38.
hydrogen economy: hydrogen production, storage, transportation and
[15] Bradley PE, Radebaugh R. Properties of selected materials at cryogenic
application. Renew Sustain Energy Rev 2025;210:115196.
temperatures. 2013.
[51] Yang J, Lam TY, Luo Z, Cheng Q, Wang G, Yao H. Renewable energy driven
[16] Bruce STM, Hayward J, Schmidt E, Munnings C, Palfreyman D, Hartley P.
electrolysis of water for hydrogen production, storage, and transportation. Renew
National hydrogen roadmap. CSIRO; 2018.
Sustain Energy Rev 2025;218:115804.
[17] Hinkley JT, Heenan AR, Low ACS, Watson M. Hydrogen as an export commodity
– E n c e a r p g i y ta 2 l 0 ex 2 p 2 e ;4 n 7 d ( i 8 tu 5 r ) e :3 a 5 n 9 d 5 9 en –7 er 5 g . y evaluation of hydrogen carriers. Int J Hydrogen [52] O te t c s h u n b o o l o Y g . i e H s y a d n ro d g a e p n p c li o c m at p io re n s s s i i o n n t h a e n d o i l l o a n n g d -d g is a t s a n in c d e u t s r t a r n y s — po A r t t a e t c io h n n : i c e a m l e re rg v i i n ew g .
Energy Convers Manag X 2025;25:100836.
[18] Mokhatab S, editor. Handbook of liquefied natural gas. Gulf Professional
Publishing; 2014. p. 1–106. [53] Shao L, Lin X, Yang X, Zhao Y, Zhang J, Cheng T, Zou J. Magnesium-based
hydrogen storage tanks: a review of research, development and simulation
[19] Mokhatab S, et al. Chapter 1 – LNG fundamentals. In: Handbook of liquefied
natural gas. Gulf Professional Publishing; 2014. p. 1–106. models. Renew Sustain Energy Rev 2025;211:115332.
[54] Wang S, Li Z, Gao M, Liu Y, Pan H. Low-temperature and reversible hydrogen
[20] Krikkis RN, Wang B, Niotis S. An analysis of the ballast voyage of an LNG carrier:
storage advances of light metal borohydrides. Renew Sustain Energy Rev 2025;
the significance of the loading and discharging cycle. Appl Therm Eng 2021;194:
208:115000.
117092.
22

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
[55] Nemukula E, Mtshali CB, Nemangwele F. Metal hydrides for sustainable hydrogen [88] Karatas M. Hydrogen energy storage method selection using fuzzy axiomatic
storage: a review. Int J Energy Res 2025. design and analytic hierarchy process. Int J Hydrogen Energy 2020;45(32):
[56] Abdulkadir BA, Setiabudi HD. Recent advances in multi-walled carbon nanotubes 16227–38.
for high-efficient solid-state hydrogen storage: a review. Chem Eng Technol 2024. [89] Hong X, Thaore VB, Karimi IA, Farooq S, Wang X, Usadi AK, et al. Techno-enviro-
[57] Boretti A. A narrative review of metal and complex hydride hydrogen storage. economic analyses of hydrogen supply chains with an ASEAN case study. Int J
Research 2025;2(2):100226. Hydrogen Energy 2021;46(65):32914–28.
[58] Jayabal R. Hydrogen energy storage in maritime operations: a pathway to [90] Wulf C, Zapp P. Assessment of system variations for hydrogen transport by liquid
decarbonization and sustainability. Int J Hydrogen Energy 2025;109:1133–44. organic hydrogen carriers. Int J Hydrogen Energy 2018;43(26):11884–95.
[59] Liu J, Guo Y, Xing X, Zhang X, Yang Y, Cui G. A comprehensive review on [91] Ochoa Bique A, Zondervan E. An outlook towards hydrogen supply chain
hydrogen permeation barrier in the hydrogen transportation pipeline: networks in 2050 — design of novel fuel infrastructures in Germany. Chem Eng
mechanism, application, preparation, and recent advances. Int J Hydrogen Res Des 2018;134:90–103.
Energy 2025;101:504–28. [92] Molkov V, Dadashzadeh M, Makarov D. Physical model of onboard hydrogen
[60] Elgendi M, Huh J, Sekar M, Mahmoud MA, Abdelkareem MA, Olabi AG. storage tank thermal behaviour during fuelling. Int J Hydrogen Energy 2019;44
Opportunities and sustainability challenges of hydrogen as a fuel in the (8):4374–84.
transportation sector: a review. Renew Sustain Energy Rev 2025;217:115705. [93] Liu Z, Li Y. Thermal physical performance in liquid hydrogen tank under constant
[61] Schiaroli A, Claussner L, Campari A, Cirrone D, Linseisen B, Friedrich A, Torres de wall temperature. Renew Energy 2019;130:601–12.
Ritter EL, Kuznetsov M, Ustolin F. A comprehensive review on liquid hydrogen [94] Petitpas G. Simulation of boil-off losses during transfer at a LH2 based hydrogen
transfer operations and safety considerations for mobile applications. Int J refueling station. Int J Hydrogen Energy 2018;43(46):21451–63.
Hydrogen Energy 2025;107:164–82. [95] Zuo ZQ, Sun PJ, Jiang WB, Qin XJ, Li P, Huang YH. Thermal stratification
[62] Naquash A, Agarwal N, Lee M. A review on liquid hydrogen storage: current suppression in reduced or zero boil-off hydrogen tank by self-spinning spray bar.
status, challenges and future directions. Sustainability 2024;16(18):8270. Int J Hydrogen Energy 2019;44(36):20158–72.
[63] Yin L, Yang H, Ju Y. Review on the key technologies and future development of [96] Liu Z, Li Y, Zhou G. Study on thermal stratification in liquid hydrogen tank under
insulation structure for liquid hydrogen storage tanks. Int J Hydrogen Energy different gravity levels. Int J Hydrogen Energy 2018;43(19):9369–78.
2024;57:1302–15. [97] Melideo D, Baraldi D, De Miguel Echevarria N, Acosta Iborra B. Effects of some
[64] Passalacqua M, Traverso A. From LNG to LH2 in maritime transport: a review of key parameters on the thermal stratification in hydrogen tanks during the filling
technology, materials, and safety challenges. J Mar Sci Eng 2025;13(9):1748. process. Int J Hydrogen Energy 2019;44(26):13569–82.
[65] Ustolin F, Campari A, Taccani R. An extensive review of liquid hydrogen in [98] Ma Y, Zhu K, Li Y, Xie F. Numerical investigation on chill-down and thermal stress
transportation with focus on the maritime sector. J Mar Sci Eng 2022;10(9):1222. characteristics of a LH2 tank during ground filling. Int J Hydrogen Energy 2020;
[66] Zhang T, Uratani J, Huang Y, Xu L, Griffiths S, Ding Y. Hydrogen liquefaction and 45(46):25344–56.
storage: recent progress and perspectives. Renew Sustain Energy Rev 2023;176: [99] Zhou R, Zhu W, Hu Z, Wang S, Xie H, Zhang X. Simulations on effects of rated
113204. ullage pressure on the evaporation rate of liquid hydrogen tank. Int J Heat Mass
[67] Ustolin F, Campari A, Taccani R. An extensive review of liquid hydrogen in Tran 2019;134:842–51.
transportation with focus on the maritime sector. J Mar Sci Eng 2022;10(9):1–36. [100] Liu Z, Feng Y, Lei G, Li Y. Fluid thermal stratification in a non-isothermal liquid
[68] Xie Z, Jin Q, Su G, Lu W. A review of hydrogen storage and transportation: hydrogen tank under sloshing excitation. Int J Hydrogen Energy 2018;43(50):
progresses and challenges. Energies 2024;17(16):4070. 22622–35.
[69] Alkhaledi AN, Sampath S, Pilidis P. A hydrogen fuelled LH2 tanker ship design. [101] Raj A, Sofia Larsson IA, Ljung A-L, Forslund T, Andersson R, Sundstro¨m J,
Ships Offshore Struct 2022;17(7):1555–64. Lundstro¨m TS. Evaluating hydrogen gas transport in pipelines: current state of
[70] Mokhatab S, editor. Handbook of liquefied natural gas. Gulf Professional numerical and experimental methodologies. Int J Hydrogen Energy 2024;67:
Publishing; 2014. p. 1–106. 136–49.
[71] Kulitsa M, Wood D. Boil-off gas balanced method of cool down for liquefied [102] AlZohbi G. Ammonia from hydrogen: a viable pathway to sustainable
natural gas tanks at sea. Adv Geo-Energy Res 2020;4:199–206. transportation? Sustainability 2025;17(18):8172.
[72] Chapter 1: LNG fundamentals. In: Mokhatab S, editor. Handbook of liquefied [103] Niermann M, Timmerberg S, Drünert S, Kaltschmitt M. Liquid Organic hydrogen
natural gas. Gulf Professional Publishing; 2014. p. 1–106. carriers and alternatives for international transport of renewable hydrogen.
[73] Krikkis RN, Wang B, Niotis S. An analysis of the ballast voyage of an LNG carrier: Renew Sustain Energy Rev 2021;135:110171.
the significance of the loading and discharging cycle. Appl Therm Eng 2021;194: [104] Jaramillo DE, Moreno-Blanco J, Aceves SM. Evaluation of cryo-compressed
117092. hydrogen for heavy-duty trucks. Int J Hydrogen Energy 2024;87:928–38.
[74] Moon K, et al. Comparison of spherical and membrane large LNG carriers in terms [105] Hasan MMF, Zheng AM, Karimi IA. Minimizing boil-off losses in liquefied natural
of cargo handling. Gastech conference proceedings. 2005. gas transportation. Ind Eng Chem Res 2009;48(21):9571–80.
[75] Lee JN, et al. A method for the prediction of heat capacity of LNG cargo tanks [106] Krikkis RN. A thermodynamic and heat transfer model for LNG ageing during ship
during cool-down and warm-up. SNAME Maritime Convention; 2008. transportation towards an efficient boil-off gas management, cryogenics. 2018.
[76] Wang J, Webley PA, Hughes TJ. Cooldown strategies for ship-borne cryogenic [107] Krikkis RN, Wang B, Niotis S. An analysis of the ballast voyage of an LNG carrier:
storage tanks during the ballast voyage. Energy 2025;334:137568. the significance of the loading and discharging cycle. Appl Therm Eng 2021;194:
[77] Kawasaki Heavy Industries Ltd. Kawasaki technical review No. 182 special issue 117092.
on hydrogen energy supply chain. 2021. [108] Qu Y, et al. A thermal and thermodynamic code for the computation of boil-off
[78] Wang J, Webley PA, Hughes TJ. Thermodynamic modelling of low fill levels in gas – industrial applications of LNG carrier, cryogenics. 2019.
cryogenic storage tanks for application to liquid hydrogen maritime transport. [109] Kulitsa M, Wood D. Boil-off gas balanced method of cool down for liquefied
Appl Therm Eng 2024;256:124054. natural gas tanks at sea. Advanced Geo-Energy Research 2020;4:199–206.
[79] Forghani K, Kia R, Nejatbakhsh Y. A multi-period sustainable hydrogen supply [110] Wang Z, M´erida W. Thermal performance of cylindrical and spherical liquid
chain model considering pipeline routing and carbon emissions: the case study of hydrogen tanks. Int J Hydrogen Energy 2024;53:667–83.
Oman. Renew Sustain Energy Rev 2023;173:113051. [111] Al-Breiki M, Bicer Y. Investigating the technical feasibility of various energy
[80] Parolin F, Colbertaldo P, Campanari S. Development of a multi-modality carriers for alternative and sustainable overseas energy transport scenarios.
hydrogen delivery infrastructure: an optimization model for design and Energy Convers Manag 2020;209:112652.
operation. Energy Convers Manag 2022;266:115650. [112] Al-Breiki M, Bicer Y. Comparative cost assessment of sustainable energy carriers
[81] Matsuo Y, Endo S, Nagatomi Y, Shibata Y, Komiyama R, Fujii Y. A quantitative produced from natural gas accounting for boil-off gas and social cost of carbon.
analysis of Japan's optimal power generation mix in 2050 and the role of CO2-free Energy Rep 2020;6:1897–909.
hydrogen. Energy 2018;165:1200–19. [113] Wang J, Alkhaledi AN, Hughes TJ, Webley PA. Technoeconomic investigation of
[82] Sun K, Li K-J, Zhang Z, Liang Y, Liu Z, Lee W-J. An integration scheme of optimal storage pressure and boil-off gas utilisation in large liquid hydrogen
renewable energies, hydrogen plant, and logistics center in the suburban power carriers. Appl Energy 2025;384:125356.
grid. IEEE Trans Ind Appl 2022;58(2):2771–9. [114] Ferrari E, Christidis P, Bolsi P. The impact of rising maritime transport costs on
[83] Mohseni S, Brent AC. Economic viability assessment of sustainable hydrogen international trade: estimation using a multi-region general equilibrium model.
production, storage, and utilisation technologies integrated into on- and off-grid Transp Res Interdiscip Perspect 2023;22:100985.
micro-grids: a performance comparison of different meta-heuristics. Int J [115] Wu M, Zhang S, Zhou X, Wang Y, Zhao S. Analysis of competitive strategies and
Hydrogen Energy 2020;45(59):34412–36. cost effects in the digitalization of the shipping industry. Mathematics 2025;13
[84] Reuß M, Dimos P, L´eon A, Grube T, Robinius M, Stolten D. Hydrogen road (23):3802.
transport analysis in the energy system: a case study for Germany through 2050. [116] Lee JN, et al. A method for the prediction of heat capacity of LNG cargo tanks
Energies 2021;14(11):3166. during cool-down and warm-up. SNAME Maritime convention proceedings. 2008.
[85] Aunedi M, Yliruka M, Dehghan S, Pantaleo AM, Shah N, Strbac G. Multi-model [117] Lu J, et al. Numerical prediction of temperature field for cargo containment
assessment of heat decarbonisation options in the UK using electricity and system of LNG carriers during pre-cooling operations. J Nat Gas Sci Eng 2016;29:
hydrogen. Renew Energy 2022;194:1261–76. 382–91.
[86] Tlili O, Mansilla C, Linbn J, Reuß M, Grube T, Robinius M, et al. Geospatial [118] Sun X, et al. Study on thermodynamic response in liquefied natural gas storage
modelling of the hydrogen infrastructure in France in order to identify the most tanks under static pressurization and sloshing conditions. Asia Pac J Chem Eng
suited supply chains. Int J Hydrogen Energy 2020;45(4):3053–72. 2024;19(3):e3044.
[87] Reuß M, Grube T, Robinius M, Preuster P, Wasserscheid P, Stolten D. Seasonal [119] Leachman J, et al. Fundamental equations of state for parahydrogen, normal
storage and alternative carriers: a flexible hydrogen supply chain model. Appl hydrogen, and orthohydrogen. J Phys Chem Ref Data 2009;38.
Energy 2017;200:290–302.
23

MD.S. Alam Towhid and S.B. Hossain R e n e w a b le a n d S u s t a i n a b l e E n e r g y R e v i e w s 2 3 3 (2026) 116850
[120] Krikkis RN, Wang B, Niotis S. An analysis of the ballast voyage of an LNG carrier: [143] Daigle M, et al. Temperature stratification in a cryogenic fuel tank. J Thermophys
the significance of the loading and discharging cycle. Appl Therm Eng 2021;194: Heat Tran 2013;27:116–26.
117092. [144] Wang J, Webley PA, Hughes TJ. Thermodynamic modelling of pressurised storage
[121] Krikkis RN. A thermodynamic and heat transfer model for LNG ageing during ship and transportation of liquid hydrogen for maritime export. Int J Hydrogen Energy
transportation: towards an efficient boil-off gas management. Cryogenics 2018; 2024;62:1273–85.
92:76–83. [145] Fesmire J, Swanger A. Overview of the new LH2 sphere at NASA Kennedy space
[122] Morales-Ospino R, Celzard A, Fierro V. Strategies to recover and minimize boil-off centre. DOE/NASA advances in liquid hydrogen storage workshop. 2021.
losses during liquid hydrogen storage. Renew Sustain Energy Rev 2023;182: [146] Krenn AG. Diagnosis of a poorly performing liquid hydrogen bulk storage sphere.
113360. AIP Conf Proc 2012;1434(1):376–83.
[123] Xie Z, Jin Q, Su G, Lu W. A review of hydrogen storage and transportation: [147] Krenn A, Desenberg D. Return to service of a liquid hydrogen storage sphere. IOP
progresses and challenges. Energies 2024;17:4070. Conf Ser Mater Sci Eng 2020;755(1). Article 012023.
[124] Chu C, Wu K, Luo B, Cao Q, Zhang H. Hydrogen storage by liquid organic [148] Liebenberg DH, Murley E. Initial warmup of 500,000-gallon liquid hydrogen
hydrogen carriers: catalyst, renewable carrier, and technology — a review. dewar. Los Alamos Scientific Laboratory; 1967.
Carbon Resource Conversion 2023;6:334–51. [149] Sass JP, et al. Glass bubbles insulation for liquid hydrogen storage tanks. AIP Conf
[125] Kurtz J, Sprik S, Bradley TH. Review of transportation hydrogen infrastructure Proc 2010;1218(1):772–9.
performance and reliability. Int J Hydrogen Energy 2019;44:12010–23.(a) [150] Liebenberg DH, Stokes RW, Edeskuty FJ. Chilldown and storage losses of large
Naquash A, Agarwal N, Lee M. A review on liquid hydrogen storage: Current liquid hydrogen storage dewars. Advances in cryogenic engineering. Boston, MA:
status, challenges and future directions. Sustainability 2024;16:8270. Springer; 1966.
[126] Petitpas G, B´enard P, Klebanoff LE, Xiao J, Aceves S. A comparative analysis of [151] Edeskuty FJ. Liquid hydrogen in nuclear rocket testing. Los Alamos Scientific
cryo-compression and cryo-adsorption hydrogen storage methods. Int J Hydrogen Laboratory; 1965.
Energy 2014;39:10564–84. [152] Edeskuty FJ, Liebenberg D, Novak J. Problems in the operation of large cryogenic
[127] Brunner T, Kircher O. Cryo-compressed hydrogen storage. In: Hydrogen science systems. Los Alamos Scientific Laboratory; 1963.
and engineering: materials, processes, systems and technology. Hoboken: John [153] Lu J, Chen L, Zhou X. Thermodynamic modeling of multilayer insulation schemes
Wiley & Sons; 2016. p. 711–32. coupling liquid nitrogen cooled shield and vapour hydrogen cooled shield for LH2
[128] Agnolucci P, McDowall W. Designing future hydrogen infrastructure: insights tank. Processes 2025;13(8):2574.
from analysis at different spatial scales. Int J Hydrogen Energy 2013;38:5181–91. [154] Arnold SM, Bednarcyk BA, Collier CS, Yarrington PW. Spherical cryogenic hydrogen
[129] Xiao R, Tian G, Hou Y, Chen S, Cheng C, Chen L. Effects of cooling-recovery tank preliminary design trade studies. National aeronautics and space
venting on the performance of cryo-compressed hydrogen storage for automotive administration, glenn research center. Paper presented at the 48th structures,
applications. Appl Energy 2020;269:115143. structural dynamics, and materials conference. 2007. Waikiki, HI, United States.
[130] Li S, Han F, Liu Y, Xu Z, Yan Y, Ni Z. Evaluation criterion for filling process of [155] Xu Y, Zhang H, Zhuk D, Zhang S, Ma J. Analysis of liquefied natural gas storage
cryo-compressed hydrogen storage vessel. Int J Hydrogen Energy 2024;59: tanks under different applications. Journal of Engineering Mechanics and
1459–70. Machinery 2025;10(2).
[131] Ahluwalia RK, Hua TQ, Peng JK, Lasher S, McKenney K, Sinha J, Gardiner M. [156] Li B, Zhang Y, Li D, Ding L. Study on vapour insulation technology in MOSS-type
Technical assessment of cryo-compressed hydrogen storage tank systems for tanks of LNG carriers. Lecture Notes in Electrical Engineering 2011;132:397–402.
automotive applications. Int J Hydrogen Energy 2010;35:4171–84. Springer.
[132] Hasan MMF, Zheng AM, Karimi IA. Minimizing boil-off losses in liquefied natural [157] Lee W, Lee S, Lee Y, Mellacheruvu P, Hudson D, Richardson E. Sloshing
gas transportation. Ind Eng Chem Res 2009;48(21):9571–80. phenomena in LH2 tanks: computational analysis of pressure changes and boil-off
[133] McDermott, Liquid hydrogen cargo containment system concept approval (DNV gas. In: Proceedings of the global conference on naval architecture and ocean
classification). Offshore Energy News 2023. engineering 2024; 2024. Southampton, United Kingdom.
[134] TotalEnergies BV. GTT and LMG marin collaboration on large-scale liquid [158] Lv H, Chen L, Zhang Z, Chen S, Hou Y. Numerical study on thermodynamic
hydrogen carrier development. Offshore Energy News; 2023. characteristics of large-scale liquid hydrogen tank with baffles under sloshing
[135] Offshore Energy. Moss Maritime's LH2 carrier containment system gets DNV's conditions. Int J Hydrogen Energy 2024;57:562–74.
nod. 2023 (Industry report). [159] Zheng Z, Xu A, Jiang W, Wang B, Sun P, Li P, Huang Y. Simulation of sloshing and
[136] Wang Z, M´erida W. Thermal performance of cylindrical and spherical liquid settling behavior of liquid hydrogen in an insulated tank during coastal period. Int
hydrogen tanks. Int J Hydrogen Energy 2024;53:667–83. J Hydrogen Energy 2025;97:117–29.
[137] Haoren W, Bo W, Ruize L, Xian S, Yingzhe W, Quanwen P, Yuanxin H, Weiming Z. [160] Smith JR, Gkantonas S, Mastorakos E. Modelling of boil-off and sloshing relevant
Theoretical investigation on heat leakage distribution between vapor and liquid to future liquid hydrogen carriers. Energies 2022;15(6):2046.
in liquid hydrogen tanks. Int J Hydrogen Energy 2023;48(45):17187–201. [161] Lee Y, Bakkers N, Kim Y, Lee W, Park J-C, Jeong S-M, Mellacheruvu P, Dinesh R.
[138] Matveev KI, Leachman JW. The effect of liquid hydrogen tank size on self- Benchmark study on sloshing of liquefied hydrogen (parts I & II). In: Proceedings
pressurization and constant-pressure venting. Hydro 2023;4(3):444–55. of MARSTRUCT 2025; 2025. Lisbon, Portugal.
[139] Hastings LJ, Flachbart RH, Martin JJ, Hedayat A, Fazah M, Lak T, Nguyen H, [162] Towhid MSA, Hossain SB, Costa BT, Chakraborty B, Zanj A. Toward high-
Bailey JW. Spray bar zero-gravity vent system for On-Orbit liquid hydrogen efficiency oscillating water column (OWC) systems: a focused review on turbine
storage. Cleveland, OH, USA: Lewis Research Center; 2003. NASA/TM-2003- optimization, airflow control, and chamber interactions. Renew Sustain Energy
212926. Rev 2026;226(Part E):116476.
[140] Wang C, Ju Y, Fu Y. Dynamic modeling and analysis of LNG fuel tank [163] Towhid SA, Islam MR, Khalikujjaman M, Costa BT. Waste heat recovery-based
pressurization under marine conditions. Energy 2021;232:121029. seawater desalination for sustainable maritime operations: a study on heat
[141] Al Ghafri SZS, et al. Modelling of liquid hydrogen boil-off. Energies 2022;15. transfer, techno-economic feasibility, and environmental impact. Journal of ETA
Article 1234. Maritime Science 2025;13(3):260–76.
[142] Wang J, Webley PA, Hughes TJ. Thermodynamic modelling of low fill levels in
cryogenic storage tanks for application to liquid hydrogen maritime transport.
Appl Therm Eng 2024;256:124054.
24

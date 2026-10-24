# AR/VR-Guided Manual Assembly: Patent Research, Business Plan and Marketing Plan

**Project area:** AR/VR-guided manual assembly, computer vision and future human–cobot collaboration
**Initial market:** India (with later international expansion)
**Prepared:** 24 October 2026
**Format:** M.Tech academic presentation and entrepreneurship proposal

---

## How to read this document (please read first)

**1. What the confidence tags mean.** Each important claim has one of three tags:

| Tag | Meaning |
|---|---|
| **[Certain]** | Confirmed by an official record, or by several independent sources that agree. |
| **[Likely]** | Strong inference, or confirmed by only one secondary source (for example Google Patents, Justia or a trade article). |
| **[Guessing]** | An assumption or estimate made for planning. Every financial number in Parts 3–5 is in this group unless it says otherwise. |

**2. An important limit on this research.** The research environment could not open official patent office websites directly. These were blocked: patents.google.com, USPTO Patent Center, Espacenet, the EPO Register and WIPO PATENTSCOPE. Patent facts were collected through a web search index, which quotes from those same pages: Google Patents, USPTO full-text PDFs (image-ppubs.uspto.gov), Justia Patents, PTAB case trackers and company pages.

- **Titles, numbers, inventors and the technical summaries** are well supported. Several sources agree on them.
- **Legal status (in force, expired, lapsed)** is **not verified from an official record** for any patent here. It is marked [Likely] at most.
- **Before you present this,** spend about 30–45 minutes on the checklist in **Section 4.7**. Confirm each status yourself on USPTO Patent Center and the EPO Register. A legal status should not be quoted in a viva unless you have seen it on the official register.

**3. Nothing here is legal advice.** It is not a patentability opinion and not a freedom-to-operate (FTO) opinion. A registered Indian patent agent or patent attorney must do those before you build or sell a product.

---

## 1. Executive Summary

**The uncomfortable finding first.** The most common picture of "AR assembly" is a worker wearing a headset. That is probably the wrong starting product for Indian shop floors.
- [Certain] Microsoft stopped making HoloLens 2 in 2024. Its industrial AR apps, Dynamics 365 Guides and Remote Assist, stop being available after **31 December 2026**.
- [Likely] Headsets are expensive, uncomfortable over an 8-hour shift and hard to manage at scale.

The patents and the market both point to a better starting product: a **fixed, station-mounted assistant**. It has an overhead camera, AI step-checking and projected or on-screen instructions. VR training and cobot links can be added later.

**What was done:**
- **Patents (Part 1).** We picked 5 real patents that cover the key technology areas:
  1. Projected-light guided assembly (LightGuide, US 7,515,981 B2)
  2. AR glasses for assembly help and monitoring (Amazon, US 10,366,521 B1)
  3. Machine-learning step recognition with an AR overlay (US 11,715,300 B1, inventors Guo, Huang and Ren)
  4. VR assembly training with a haptic glove (Permco, US 12,592,164 B2)
  5. AR/VR interaction with collaborative robots (Raytheon, US 11,529,737 B2)
- **Comparison (Part 2).** All five use step-by-step digital work instructions. Most also use camera sensing and some form of step confirmation. **None of them puts low-cost CV verification, VR pre-training and a cobot hand-over interface into one affordable product sized for Indian plants.**
- **Business concept (Part 3).** We propose **StepSure**: a per-station AI assembly copilot. One "recipe" (the digital assembly process) drives three things: shop-floor guidance, VR onboarding and, later, cobot hand-over.
- **Plan (Parts 4–5).** Start with one paid pilot. Charge per station per year, with hardware sold close to cost.
  - Break-even needs about **12–13 customers of 5 stations each** (about 62 stations). [Guessing]
  - Under the stated assumptions, that is realistic in year 3, not year 1. [Guessing]
  - Year 1 needs about **₹1.1 crore** of funding. [Guessing]

---

## 2. Introduction to AR/VR-Guided Industrial Assembly

**Manual assembly is still most of the work at many plants.** Automotive component, electronics and electrical plants in India still assemble many products by hand. Examples are wire harnesses, switchgear, pumps, seats and sub-assemblies. The usual problems are:

- **Wrong part, missed step, wrong order or wrong torque.** These cause rework, scrap and customer complaints.
- **Slow onboarding.** New and contract workers need days or weeks of buddy training.
- **Paper or PDF work instructions.** These go out of date and workers do not read them while working.
- **No record** of who did which step, and when.

**What AR, VR and computer vision add, in simple words:**

| Technology | What it does on the shop floor |
|---|---|
| **AR (augmented reality)** | Shows the next instruction on top of the real work. It can be projected onto the table, shown on a screen or shown in glasses. |
| **VR (virtual reality)** | Lets a trainee practise the whole assembly in a 3D virtual workplace before touching real parts. |
| **Computer vision (CV) and AI** | A camera watches the work. AI models recognise parts, hands and the current assembly state. The system can then confirm that a step was done correctly, or warn the worker. |
| **Digital twin** | A live digital copy of the station or product. It lets the same process data drive training, guidance and analytics. |
| **Human–cobot collaboration** | A collaborative robot does part of the job next to the worker. AR shows the worker what the robot is about to do, and where it is safe to stand. |

**Evidence that AR guidance helps.** [Certain] In a classic controlled experiment (Tang et al., CHI 2003), showing 3D instructions on the actual work pieces cut assembly errors by **82%**. The comparison was against a paper manual, a computer screen and a head-mounted display that was not registered to the work. **Caution:** it was a lab study with simple tasks, so results in a real factory will be smaller and more variable.

---

## 3. Research Methodology and Patent-Search Strategy

### 3.1 Search questions

We looked for granted patents, or published applications, that teach any of these:
- (a) AR step-by-step assembly guidance
- (b) VR assembly training
- (c) assembly verification and error detection
- (d) CV or AI object recognition and pose estimation for assembly
- (e) AR/VR interaction with cobots
- (f) digital twins for immersive industrial training

### 3.2 Databases and how they were used

| Database | Planned use | What actually happened |
|---|---|---|
| Google Patents | Full-text search, family view, claims | Reached only through search-index quotes. Direct access was blocked. |
| USPTO (Patent Public Search, Patent Center) | Official US text and legal status | Full-text PDF titles and abstracts reached through the search index. **Status not checked directly.** |
| Espacenet / EPO Register | European family members and status | Not reachable. Family members found through Google Patents quotes. |
| WIPO PATENTSCOPE | PCT applications | Not reachable. PCT numbers noted where found. |
| Justia Patents, PTAB trackers | Secondary check of inventors, assignees and litigation | Used. |

### 3.3 Keywords and classes used

- **Keywords:** "augmented reality" + assembly + instructions / verification / "step recognition"; "light guided assembly"; "virtual reality training simulator" + assemble; "collaborative robot" + "augmented reality" + trajectory.
- **Relevant CPC classes for your own follow-up searches:**
  - G06T 19/006 (mixed reality)
  - G09B 19/24 (training: use of tools)
  - G09B 9/00 (simulators)
  - G05B 19/418 (total factory control)
  - B25J 9/1671 (robot programming using simulation or AR)
  - G06V 20/20 and G06V 10/82 (scene recognition, neural networks)
  - G06Q 10/06 (operations management)

### 3.4 Selection criteria

1. **Real and checkable.** It must have a valid publication number and appear in at least two independent sources.
2. **Directly relevant** to guided manual assembly or its planned extensions.
3. **Covers a different technology area** from the other picks, so the five together cover AR, CV/AI, VR and cobots.
4. **A mix of patent ages.** This lets us show how expiry, continuations and litigation change what is "free to use".

### 3.5 Disclosure versus claims (key concept)

This idea is central to the whole analysis, so it is explained here in plain words.

- **The disclosure** is the description and drawings. It is everything the patent *teaches*: the background, embodiments, examples and variations. Once published, the disclosure is **prior art** that anyone can learn from and cite.
- **The claims** are the numbered sentences at the end. They alone define what the owner can *stop others from doing*. You infringe only if your product or method includes **every element** of at least one claim, or an equivalent of it.
- **So a patent can describe far more than it protects.** For example, the Amazon patent's description talks about safe walking paths. If no granted claim covers safe paths, that feature is taught but not protected *by that patent*. It may still be protected by a related patent in the same family.
- **A published application (A1) is not a granted patent.** Its claims may be narrowed, changed or rejected before grant.
  - US kind codes: **A1** = application publication. **B1** = granted with no earlier publication. **B2** = granted after an earlier publication.
  - In Europe, **B1** = granted. **B2** = maintained in amended form after an opposition.
- **Patents are territorial.** [Certain] A US patent can be enforced only in the US. It does not stop anyone in India unless an Indian patent in the same family exists.
  - **Exception risk for exporters.** [Likely] US law (35 U.S.C. §271(g)) can reach *products imported into the US* that were made by a process patented in the US. An Indian supplier that exports to the US could in principle be exposed. This needs advice from counsel.
- **Expiry in one country is not expiry everywhere.** Also, a "basic" patent may expire while continuations or improvement patents on the same product stay in force. LightGuide below is an example.

---

## 4. Analysis of the 5 Patents

### 4.1 Patent 1: Light Guided Assembly System (LightGuide)

| Field | Details | Confidence |
|---|---|---|
| **1. Title** | Light guided assembly system | [Certain] |
| **2. Number and links** | **US 7,515,981 B2** (granted). Pre-grant publication **US 2008/0121168 A1**. PCT family member WO 2007/044558.<br>Google Patents: https://patents.google.com/patent/US7515981B2/en<br>USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7515981 | [Certain] |
| **3. Inventors** | Paul Ryznar, James Ryznar | [Likely] (Google Patents listing) |
| **4. Applicant / owner** | Original: OPS Solutions LLC. Current: LightGuide, Inc. (entity conversion from OPS Solutions LLC recorded in 2021 for the related family) | [Likely] |
| **5. Dates** | Priority 7 Oct 2005. Filed 6 Oct 2006 (application US 11/909,002). A1 published 29 May 2008. Granted April 2009 (the patent number falls in the range issued on 7 April 2009). | Filing/priority [Likely]. Grant month [Likely]. Exact grant day [Guessing], verify. |
| **6. Legal status** | **Not verified on an official register.** A US term runs 20 years from the filing date, which gives about **October 2026**, plus any term adjustment. So it has **just expired or is about to**, if fees were paid. Litigation is recorded **in the family**: IPR2024-00141 (Amazon.com v. LightGuide), filed 4 Nov 2023, ended by settlement March 2024 with no final decision; and W.D. Wash. case 2:23-cv-00053. | [Likely]. Check Patent Center (§4.7). |
| **7. Jurisdiction** | United States. A PCT filing exists. Later family members are in Europe (EP 2673592, held as **B2**, meaning maintained in amended form after opposition) and the US (US 9,658,614 B2; US 10,528,036). | [Likely] |
| **8. Problem addressed** | Operators make sequence and part-selection errors. Paper instructions are not used during work, and training is slow. | [Certain] |
| **9. Technology and working principle** | One or more light sources or projectors above the workstation project visual indicators directly onto the work area. Examples are arrows, highlighted bins, locations and text. A controller steps the operator through the assembly sequence in order. Each step can be confirmed before the next indicator appears. | [Likely] (summary of disclosure; read claim 1 for the exact protected elements) |
| **10. Key features and innovation** | Instructions appear *on the work*, so the worker does not need glasses or to look at a screen. The work cycle is driven step by step. Bins and parts are pointed out. Later family members add a link to MES (Manufacturing Execution System) and more. | [Likely] |
| **11. Industrial uses and customers** | Automotive and Tier-1 sub-assembly, electrical and electronics assembly, kitting, aerospace and defence, and quality inspection stations. | [Likely] |
| **12. Relevance to your project** | **Very high.** This is the "fixed station" form of AR, which suits a 2D camera plus projector set-up. It is the main prior art that any projected-AR product must be compared against. | [Certain] |
| **13. Business opportunity** | Projected AR fits Indian shop floors well: no headset, shared by all shifts, works with gloves. The 2005 basic patent is near the end of its US term, so the general idea may be more open in the US. **But** continuations and improvement patents stay in force, so this does *not* mean "free to use". | [Likely] |
| **14. Limits and gaps** | Projection gets washed out under bright light and fails on shiny or black surfaces. Calibration is needed when fixtures move. Verification is usually simple (sensors, light curtains or operator input) rather than AI that understands the scene. Commercial pricing is reported to be high, but this was not verified. | [Likely] |

### 4.2 Patent 2: Augmented Reality Assembly Assistance and Monitoring (Amazon)

| Field | Details | Confidence |
|---|---|---|
| **1. Title** | Augmented reality assembly assistance and monitoring | [Certain] |
| **2. Number and links** | **US 10,366,521 B1** (granted with no earlier publication, kind B1).<br>Google Patents: https://patents.google.com/patent/US10366521B1/en<br>USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10366521 | [Certain] |
| **3. Inventors** | Jason Leonard Peacock, Joshua John Watson, Scott Michael Wilcox | [Likely] (Google Patents and Justia agree) |
| **4. Applicant / owner** | Amazon Technologies, Inc. | [Likely] |
| **5. Dates** | Application US 15/460,015. The number series points to a filing around **March 2017**. The patent number is in the range issued **30 July 2019**. | [Likely] for both. Verify exact dates. |
| **6. Legal status** | Google Patents shows "Active". Google itself says this is its own assumption, not a legal finding. The expected end of term is about 2037, plus any term adjustment, if maintenance fees are paid. | [Likely]. Verify. |
| **7. Jurisdiction** | United States. No foreign family members were confirmed in this research. | [Likely] |
| **8. Problem addressed** | Workers who assemble complex products need the right information at the right moment. The example in the patent is aerial vehicles (drones). Managers also need to know that each step was done correctly, and workers need to stay out of unsafe areas. | [Certain] |
| **9. Technology and working principle** | Workers wear AR glasses. Assembly information is shown in their view for the current step. Camera image data from the glasses (or the workplace) is used to **verify the assembly** step. The disclosure also shows **safe walking paths and restricted areas** in the glasses (FIG. 9). | [Certain] (taken from the USPTO full-text figure list and abstract) |
| **10. Key features and innovation** | Guidance and monitoring are combined in one wearable loop. Assembly is checked against expected information. Safety zones are overlaid. | [Likely] |
| **11. Industrial uses and customers** | Drones and aerospace, electronics, and any assembly done at many locations or on large products where a fixed station is not practical. | [Likely] |
| **12. Relevance to your project** | **High.** Very close to an "AR guidance + verification" project. It is useful prior art for showing that *the general idea* of AR guidance plus camera verification is already known. Your novelty has to be in *how* you do it. | [Certain] |
| **13. Business opportunity** | Mobile and large-product assembly (bus bodies, gensets, tractors), where fixed projectors cannot reach. Safety-zone overlays become a link to cobot cells. | [Likely] |
| **14. Limits and gaps** | Depends on head-mounted glasses: cost, comfort, battery, hygiene when shared across shifts, and a narrow field of view. Microsoft's exit from HoloLens shows the supply risk. The surveillance angle can raise worker and union concerns. | [Likely] |

### 4.3 Patent 3: Product Assembly Step Recognition Using AR (machine learning)

| Field | Details | Confidence |
|---|---|---|
| **1. Title** | Systems and methods for providing product assembly step recognition using augmented reality | [Certain] |
| **2. Number and links** | **US 11,715,300 B1** (granted). Pre-grant publication **US 2023/0245448 A1**.<br>Google Patents: https://patents.google.com/patent/US11715300B1/en<br>USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11715300<br>Justia (A1, with claims): https://patents.justia.com/patent/20230245448 | Number [Certain]. Kind code B1 [Likely]. |
| **3. Inventors** | Yuliang Guo, Xinyu Huang, Liu Ren | [Likely] (Justia) |
| **4. Applicant / owner** | **Not confirmed.** The inventors appear together on Robert Bosch GmbH patents, so Bosch is the probable assignee. Confirm on the front page of the patent. | [Guessing] about the assignee. Must verify. |
| **5. Dates** | Filed 28 Jan 2022. A1 published 3 Aug 2023. The grant number is in the range issued 1 Aug 2023, which explains why it is a B1. | Filing and A1 dates [Likely]. Grant date [Likely]. |
| **6. Legal status** | Probably in force (recent grant). The expected end of term is about January 2042, plus any term adjustment. Not checked on an official register. | [Likely] |
| **7. Jurisdiction** | United States. Foreign family not confirmed. | [Likely] |
| **8. Problem addressed** | An AR assistant has to know *which step* the worker is on, and *which parts* are involved, using only camera images. Then it can show the right guidance without the worker pressing "next". | [Certain] |
| **9. Technology and working principle** | **(i)** A first machine-learning model is trained on an **augmented dataset built from 2D images and matching 3D digital (CAD) models**. **(ii)** At run time it turns a camera image into **feature vectors**. **(iii)** These are matched to a database of **feature-vector templates**. This identifies the **base component** and the **constituent (incoming) component**, and from them the current assembly step. **(iv)** A **second ML model verifies** that decision. **(v)** The AR display shows the components and a **position indicator** for where the part goes, and updates it as new images arrive. | [Certain] (consistent in the abstract and claim summaries from USPTO and Justia) |
| **10. Key features and innovation** | CAD-to-training-data generation (synthetic data). Template matching, which allows new products to be added without full retraining. Two-model cross-checking to reduce false step detection. Live AR position cue. | [Likely] |
| **11. Industrial uses and customers** | Mixed-model assembly lines, electronics, automotive sub-assemblies, and consumer products assembled at home. | [Likely] |
| **12. Relevance to your project** | **Very high.** This is almost exactly the "AI object recognition + AR guidance" core of your project. **It is also the biggest FTO risk** for any CV step-recognition feature, especially if you plan to sell in the US. | [Certain] about relevance. [Likely] about the risk. |
| **13. Business opportunity** | Building training data from CAD cuts setup time per new product, and that is the main pain point for a vendor. Any product will need a *different* way to recognise steps, for example action recognition from hand movement, or depth-based state comparison. Or it will need a licence, or a design-around confirmed by counsel. | [Likely] |
| **14. Limits and gaps** | Parts are often hidden by hands. Very similar-looking variants (for example, two connectors that differ only by colour code). Synthetic-to-real "domain gap". Needs GPU compute. Does not check *process quality* such as torque, clip engagement or connector click. | [Likely] |

### 4.4 Patent 4: Virtual Reality Training Simulator (assembly training with haptic glove)

| Field | Details | Confidence |
|---|---|---|
| **1. Title** | Virtual reality training simulator | [Certain] |
| **2. Number and links** | **US 12,592,164 B2** (granted. The B2 code means a pre-grant publication existed; its number was not found in this research).<br>USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12592164<br>Google Patents: https://patents.google.com/patent/US12592164B2/en | Number [Certain]. Kind B2 [Likely]. |
| **3. Inventors** | **Not found in this research.** Take them from the front page of the patent. | Not verified |
| **4. Applicant / owner** | Permco, Inc. (a US hydraulic pump maker), per Justia's assignee listing | [Likely] |
| **5. Dates** | Application filed 1 Sep 2022. Granted and published 31 Mar 2026. | [Likely] (from one secondary database). Verify. |
| **6. Legal status** | Newly granted, so probably in force. The expected end of term is about September 2042, plus any term adjustment. | [Likely] |
| **7. Jurisdiction** | United States. | [Likely] |
| **8. Problem addressed** | Training workers to assemble a product (hydraulic pumps) by hand takes a long time. It uses real parts and the time of skilled trainers. | [Likely] (trade press on Permco's VR training; patent abstract) |
| **9. Technology and working principle** | A VR headset shows a virtual workbench, tools and components. The system shows an **ordered list of steps** and **highlights the tool and location** for each step. In one embodiment a **haptic glove** gives touch feedback, used to teach workers to **feel surface defects such as burrs**. | [Likely] (from the abstract, summarised through Justia) |
| **10. Key features and innovation** | Step-sequenced VR assembly. Highlighting of tools and positions. Haptic defect detection, which goes beyond visual-only VR. | [Likely] |
| **11. Industrial uses and customers** | Pump, valve and hydraulics makers, engine and gearbox assembly, ITIs and training centres, and the onboarding departments of large OEMs. | [Likely] |
| **12. Relevance to your project** | **High.** It matches the VR training half of your project. It shows that VR assembly training *with ordered steps* is patented in the US as recently as 2026. | [Certain] about relevance. |
| **13. Business opportunity** | Re-use the same process "recipe" for VR pre-training and for floor guidance, so content is written once. VR training for ITIs and skilling centres in India, where trainee numbers are large. | [Likely] |
| **14. Limits and gaps** | Haptic gloves are expensive and fragile. Building VR content for each product is costly. Skills learned in VR do not fully transfer to real work without real practice. Motion sickness. | [Likely] |

### 4.5 Patent 5: VR/AR Interaction with Collaborative Robots (Raytheon)

| Field | Details | Confidence |
|---|---|---|
| **1. Title** | System and method for using virtual/augmented reality for interaction with collaborative robots in manufacturing or industrial environment | [Certain] |
| **2. Number and links** | **US 11,529,737 B2** (granted). Pre-grant publication **US 2021/0237275 A1**. European family member **EP 4096874**.<br>Google Patents: https://patents.google.com/patent/US11529737B2/en<br>A1: https://patents.google.com/patent/US20210237275A1/en<br>USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11529737 | [Certain] |
| **3. Inventors** | Kristen M. Stone | [Likely] |
| **4. Applicant / owner** | Raytheon Company. Google notes that its assignee list can be wrong, so confirm in the USPTO assignment records. | [Likely] |
| **5. Dates** | Priority 30 Jan 2020 (provisional). Filed 31 Mar 2020 (US 16/836,569). Granted 20 Dec 2022. The EP application was filed 14 Dec 2020. | [Likely] |
| **6. Legal status** | Google Patents shows "Active". Expected end of term about March 2040, plus any term adjustment. EP status unknown: one quote mentions EP 4096874 **B1** with a 2026 date, which suggests a grant, but this was not confirmed. Check the EPO Register. | [Likely] for US. Not verified for EP. |
| **7. Jurisdiction** | United States, plus a European application or patent. | [Likely] |
| **8. Problem addressed** | Programming and working safely next to cobots is hard for shop-floor staff. Workers cannot see what the robot is about to do. | [Certain] |
| **9. Technology and working principle** | A wearable AR/VR headset shows the cobot's **planned movement path** over the real (or virtual) cell before it moves. A **training simulation** in VR produces information that is sent to the robot workstation to help **program the path**. | [Certain] (abstract-level summary) |
| **10. Key features and innovation** | The robot's intent is made visible. VR simulation is used as a programming input. Training and operation happen in the same environment. | [Likely] |
| **11. Industrial uses and customers** | Aerospace and defence, automotive cobot cells, electronics test and pack, and robot system integrators. | [Likely] |
| **12. Relevance to your project** | **High for the future extension.** It covers exactly the "AR-assisted human–cobot collaboration" stage. Any cobot hand-over feature must be checked against its claims. | [Certain] about relevance. |
| **13. Business opportunity** | Indian cobot use is growing, and integrators need simple ways to show and check robot motion to operators. A **plug-in** that shows the robot's next move on the same station projector or screen, without a headset, may be a practical alternative. It still needs FTO clearance. | [Guessing] |
| **14. Limits and gaps** | Needs accurate registration between the robot frame and the display frame. Safety certification is the bottleneck: the AR display is *not* a safety function under ISO 10218 or ISO/TS 15066 (the rules for collaborative robot operation). Headset reliance again. | [Likely] |

### 4.6 Other patents found (for your literature review)

These were found during the search. They were not chosen as the main five, either to keep the technology areas varied or because key facts could not be confirmed.

| Number | Title (short) | Why it matters | Confidence |
|---|---|---|---|
| US 8,860,760 B2 | AR system for tracking parts and visually cueing a user to find parts in a scene (Teledyne Scientific & Imaging; inventors Steven L. Chen, Austin Eliazar; granted 14 Oct 2014) | Early CV parts-tracking for AR assembly, including cues for parts *outside* the camera view. Strong prior art. | [Likely] |
| US 9,658,614 B2 / US 10,528,036 | Light guided assembly system and method (LightGuide; priority 11 Feb 2011; granted 23 May 2017) | Shows the LightGuide family **continues** after the 2005 patent. Expected US end of term about 2032. | [Likely] |
| EP 2673592 B2 | European member of the LightGuide family | **B2 in Europe = maintained in amended form after opposition.** Its claims were narrowed in Europe. | [Likely] |
| US 10,388,176 B2 (+ US 11,170,657, US 11,769,421) | Simulator for skill-oriented training (VRSIM family; priority 28 Nov 2012) | VR skill training with lesson plans and performance criteria. Expected end of term June 2034. | [Likely] |
| US 9,589,390 | Wire harness assembly | AR glasses plus camera check that a task is complete before the next instruction. Very relevant for Indian harness makers. | [Likely] |
| US 11,393,153 | Object occlusion in AR-based assembly instructions | Changes how virtual parts are drawn once a step is detected as complete. | [Likely] |
| US 2024/0241503 A1 | AR-based management of manual assembly processes | Multi-camera 3D reconstruction to locate parts. **Application only, not granted.** | [Likely] |
| EP 3318944 | Virtual reality and augmented reality for industrial automation | VR/AR views of plants and digital twins. Assignee not confirmed (probably Rockwell Automation). | [Guessing] about the assignee |
| US 11,986,963 | AR coordination of human–robot interaction | AR head-mounted display to show robot intent and to teleoperate, with hazard checks. | [Likely] |

### 4.7 Verification checklist (do this before presenting)

For each of the five, open the official record and write the result into the tables above.

1. **USPTO Patent Center** (https://patentcenter.uspto.gov). Search by **application number** and check:
   - Status, issue date, any term adjustment (PTA)
   - Maintenance fees, under "Fees" (paid at 3.5, 7.5 and 11.5 years; a missed fee means the patent lapses)
   - Terminal disclaimers
   - Application numbers: 11/909,002; 15/460,015; the application for 11,715,300; the application for 12,592,164; 16/836,569
2. **USPTO Assignment Search** (https://assignment.uspto.gov) to confirm the current owner. This is critical for 11,715,300 and 12,592,164.
3. **Espacenet** (https://worldwide.espacenet.com) to see the "INPADOC patent family" and find any **Indian (IN)** family member.
4. **Indian Patent Office InPASS** (https://iprsearch.ipindia.gov.in/PublicSearch) to search by applicant (LightGuide, Amazon Technologies, Robert Bosch, Permco, Raytheon) together with keywords. **This is the most important check for an India-first business.**
5. **EPO Register** (https://register.epo.org) for EP 4096874 and EP 2673592: grant, opposition, and lapse by country.
6. **PTAB** (https://ptacts.uspto.gov) for IPR2024-00141, to see which patent was challenged.

---

## 5. Comparative Patent Analysis

### 5.1 Comparison table

| Patent number and title | Core technology | Target industry | Main advantage | Limitation / market gap | Relevance to your project | Commercial opportunity |
|---|---|---|---|---|---|---|
| **US 7,515,981 B2**: Light guided assembly system | Projected light indicators + step sequencing controller | Automotive, electrical, kitting | No headset. Instructions appear on the work. | Projection washes out; simple sensor-based checking; costly | Very high (station-mounted AR) | Low-cost projected guidance for Indian lines |
| **US 10,366,521 B1**: AR assembly assistance and monitoring | AR glasses + camera-based assembly check + safety-zone overlay | Drones, aerospace, electronics | Mobile; combines guidance and monitoring | Headset cost and comfort; supply risk; privacy | High (guidance + verification) | Large or mobile product assembly; safety overlays |
| **US 11,715,300 B1**: Assembly step recognition using AR | ML trained on CAD-generated data; feature-vector template matching; second model checks the result; AR position cue | Mixed-model assembly, electronics, auto | Recognises the step automatically; adds new products quickly through templates | Occlusion; look-alike variants; no process-quality check | Very high (CV/AI core); **highest FTO risk** | Fast setup from CAD, but needs a different method or a licence |
| **US 12,592,164 B2**: Virtual reality training simulator | VR workbench, ordered steps, tool and location highlighting, haptic glove | Hydraulics, pumps, heavy engineering | Safe, repeatable training without real parts; touch feedback | Content cost; glove cost; limited transfer of skill to real work | High (VR training half) | VR onboarding for OEMs, ITIs, skilling centres |
| **US 11,529,737 B2**: VR/AR interaction with cobots | Headset shows planned robot path; VR simulation feeds robot programming | Aerospace, defence, auto cobot cells | Robot intent visible; easier programming | Registration accuracy; not a safety function; headset | High (future cobot extension) | Robot-intent display plug-in for integrators |

### 5.2 Technologies shared across the patents

1. **Step-by-step digital work instructions.** All five. This is the shared foundation and **is not new on its own**. [Certain]
2. **Camera or sensor feedback to confirm progress.** Patents 1, 2 and 3 (and US 9,589,390). [Likely]
3. **3D/CAD models used to drive visuals.** Patents 3, 4 and 5. [Likely]
4. **Highlighting the "where": location, tool, part.** Patents 1, 3 and 4. [Certain]
5. **Head-mounted displays** in patents 2, 4 and 5. **Projection or fixed displays** in patent 1. [Certain]

### 5.3 Unmet customer needs and market gaps

These are [Likely] unless marked otherwise.

- **Cost fit for Indian plants.** The solutions described are built for US/EU budgets. An Indian Tier-2 supplier needs a station cost and subscription that pays back within about 6–12 months.
- **Setup effort per new product or variant.** Every system needs process authoring. Patent 3's CAD-to-data idea shows this is *the* pain point. Indian suppliers run many low-volume variants.
- **Verification that goes beyond "the part is present".** None of the five checks connector clicks, clip engagement, screw count *and* torque together. Torque tools and vision are usually separate systems.
- **One content source for training, guidance and the cobot.** The patents keep these as separate systems (VR trainer in 4, floor guidance in 1–3, robot in 5). Customers pay three times for the same process knowledge.
- **Languages and low literacy.** Indian shop floors need icon-first, Hindi/Tamil/Marathi/Kannada voice and text. None of the patents deals with this. [Guessing] that this is a real differentiator; validate in interviews.
- **Headset fatigue and the 2026 HoloLens/Guides exit.** [Certain] Customers who used Dynamics 365 Guides need another platform before 31 Dec 2026.

### 5.4 Ways to combine complementary technologies

**"One recipe, three outputs."** A single digital process definition (steps, parts, tools, checks, CAD references) drives three things:
- (a) projected or screen guidance at the station (the patent 1 approach)
- (b) CV-based checking (the patent 2/3 space, done differently)
- (c) automatic VR training content (the patent 4 approach)

Later, (d) the same recipe drives robot hand-over steps with a visible robot-intent overlay (the patent 5 space).

The combination itself must still be checked against prior art. **We do not claim it is patentable or free to use.**

### 5.5 Possible differences from existing products

| Area | Possible difference | Status |
|---|---|---|
| Hardware | Station-mounted, no headset by default; headset optional | Idea. Validate with pilots. |
| Verification method | Hand-action recognition plus depth-based checking of the assembly state, and a torque-tool/scanner link, instead of the template matching in patent 3 | Idea. Needs FTO review against patent 3 and its family. |
| Content | Authoring from existing SOP sheets and CAD, plus automatic VR scene generation | Idea |
| Localisation | Icon-first UI, Indian-language voice prompts | Idea |
| Pricing | Per-station subscription in INR; hardware close to cost | Idea |

### 5.6 Technical and IP risks to investigate further

1. **FTO in the countries you will sell in.** Start with an India search on InPASS. Then the US and EU if you export or serve multinational customers whose plants are abroad.
2. **Patent 3 (step recognition).** Its claims need careful element-by-element mapping against your CV pipeline.
3. **LightGuide continuation family.** It has been litigated (IPR, district court), which shows the owner enforces its patents. Expiry of the 2005 basic patent does **not** clear the 2011+ family.
4. **Patent 5 family.** Check before building the cobot overlay.
5. **Process-patent reach (35 U.S.C. §271(g))** for customers who export to the US. [Likely] a risk; get counsel's view.
6. **Open-source licences** (for example YOLO-family models are under AGPL-3.0, which can force you to open your own code). These are commercial-use limits separate from patents. [Likely]
7. **Your own patentability in India.** Section 3(k) of the Patents Act excludes a "computer programme per se". The 2025 Computer-Related Inventions (CRI) guidelines and Delhi High Court case law allow inventions that show a **technical effect**. [Likely] Any filing should be drafted around a technical effect, such as better detection accuracy under occlusion or control of tools and robots.

---

## 6. Identified Market Gap

**[Likely] Gap statement:** Mid-sized Indian automotive and electronics suppliers lack an **affordable, quick-to-set-up, headset-free** system that:
- (1) guides each manual assembly step,
- (2) **checks** each step with a camera and connected tools before the next one,
- (3) reuses the same process data for **VR pre-training** of new and contract workers, and
- (4) is ready to add **cobot hand-over** later.

**Why now:**

- [Certain] **Indian auto components are big and growing.** Turnover was **₹6.73 lakh crore (US$80.2 bn) in FY25**, up 9.6%, with a 14% CAGR from FY20 to FY25 (ACMA).
- [Likely] **Indian electronics production is big and growing.** It was about **₹11.3 lakh crore in FY25**, up about 19%. Mobile phones alone were about ₹5.45 lakh crore (Economic Survey, as reported).
- [Likely] **People problems.** About 80% of Indian employers report difficulty finding skilled workers (ManpowerGroup 2025). Auto component attrition is about 18–20% at management level, and higher on the shop floor (Autocar Pro). High churn means constant retraining.
- [Certain] **Platform exit.** Microsoft Dynamics 365 Guides ends on 31 Dec 2026, so some multinational plants in India must move to another platform.
- [Likely] **Local competition is mostly VR training.** AutoVRse (Bengaluru) says it has 100+ enterprise clients, including Bosch, TVS Motor and Ashok Leyland (self-reported). It is focused on training rather than on-line step verification.

---

## 7. Proposed Business Concept: **StepSure**

> **Name check:** "StepSure" is a working name. Search the Indian trademark registry (https://tmrsearch.ipindia.gov.in) in classes 9 and 42 before using it.

### 7.1 Business name and product concept

**StepSure: AI Assembly Copilot.** A station-mounted kit and software platform:
- It **guides** each step of manual assembly using projection or a screen.
- It **checks** each step with a camera and connected tools.
- It **trains** new workers in VR using the same process recipe.
- Later, it **coordinates** with a cobot at the same station.

### 7.2 Customer problem and proposed solution

| Customer problem | StepSure solution |
|---|---|
| Wrong part, missed screw, wrong connector → rework and customer complaints | Camera + AI checks each step. The next step unlocks only when the check passes. Errors are flagged before the part leaves the station. |
| New and contract workers take weeks to reach line speed | VR pre-training generated from the same recipe, then guided first shifts on the line |
| Paper SOPs out of date; many variants | Digital recipe with version control; variant picked by barcode or QR scan |
| No traceability | Each step is logged with time, operator ID and a photo; export to MES/ERP |
| Plans to add cobots, but operators fear them | Phase 3: robot's next move shown on the station display; guided hand-over steps |

### 7.3 Product features and workflow

**Modules:**
1. **Recipe Studio** (web): import the SOP sheet (Excel/PDF) and CAD (STEP/GLB). Define steps, parts, tools and checks, and add multilingual text and voice.
2. **Station Runtime** (edge PC): camera input, AI checks, projector or screen output, tool and scanner I/O.
3. **Verify Engine:** checks that a part is present and correctly placed, counts screws or fasteners, follows the hand path into the correct bin, and reads torque-tool "OK" signals. *Design rule: do not copy the template-matching pipeline in patent 3; choose the method after FTO advice.*
4. **VR Trainer** (Quest-class standalone headset): auto-built from the recipe, with a practice mode and an assessment mode.
5. **Insights dashboard:** first-pass yield by step, cycle time, operator learning curves.
6. **Cobot Bridge (Phase 3):** connects to cobot controllers, for example through ROS 2 or vendor APIs. It shows the robot's intent and runs hand-over steps. It is *not* a safety function; safety stays with certified robot safety systems.

**Shop-floor workflow (per unit):**

```
Scan job/variant (QR) → Station loads recipe → Step n: project/show part bin + location + animation
 → Operator picks & places → Camera + tool signal checks step n
   ├─ PASS → log (time, photo) → Step n+1
   └─ FAIL → red cue + voice prompt in local language → retry / supervisor override (logged)
 → All steps PASS → unit released → data to dashboard / MES
```

**Onboarding workflow:** Recipe → VR training (practice, then a timed assessment) → guided mode on the line with extra prompts → normal mode once the operator meets the quality and time targets.

### 7.4 Hardware and software requirements

**Per station (estimates, [Guessing] unless marked):**

| Item | Typical spec | Planning cost (₹) | Basis |
|---|---|---|---|
| Depth/RGB camera (overhead) | RGB-D, 30 fps, USB 3 | 35,000 | Estimate for an industrial RGB-D camera, landed. Get quotes. |
| Edge AI computer | Jetson Orin-class or mini-PC with a GPU | 55,000 | [Likely] Jetson Orin Nano Super dev kit list price rose from US$249 to **US$399** in July 2026 (≈ ₹35,000 at an assumed ₹88/US$), plus import, GST and enclosure |
| Display | 24" industrial monitor and/or short-throw projector | 20,000 | Average of a screen-only and a projector set-up |
| Mount, enclosure, lighting control | Aluminium profile frame, diffuser | 15,000 | Estimate |
| I/O: scanner, foot pedal, torque-tool link, UPS | — | 10,000 | Estimate |
| **Landed kit cost** | | **1,35,000** | Sum |

**VR training seat:** Meta Quest 3S-class standalone headset, about **₹34,000** in India (Smartprix listing, not an official Meta price, [Likely]). Optional; one headset serves many trainees.

**Software stack (planned):** Python, PyTorch and ONNX/TensorRT for vision. Unity or Unreal for VR, checking the engine licence terms for revenue limits. A web Recipe Studio (React + REST API). Cloud: PostgreSQL + object storage, with an on-premise option for customers who will not allow cloud. OPC UA and MQTT for factory systems. ROS 2 for the cobot bridge.

### 7.5 Target customer segments

| Segment | Example sub-sectors | Why they buy | Priority |
|---|---|---|---|
| **A. Tier-1/Tier-2 auto component suppliers** | Wire harness, switches, lamps, seats, brake and steering sub-assemblies | OEM quality audits, defect penalties, high variant count | **Phase 1 (pilot)** |
| **B. Electronics/EMS and electrical** | Box build, meters, switchgear, EV chargers, BMS packs | Fast growth under PLI schemes; many new workers | Phase 1–2 |
| **C. OEM plants (2W/4W/CV, tractors)** | Engine dressing, gearbox, door trim | Scale, traceability, cobot plans | Phase 2 |
| **D. Industrial training centres** | ITIs, NSDC partners, SAMARTH Industry 4.0 centres, university labs | VR training seats, curriculum | Phase 1 (VR only, quick revenue and credibility) |

### 7.6 Unique value proposition

> **"Every step checked, every new worker productive in days — without headsets, at an Indian price."**

### 7.7 Competitive advantage over existing alternatives

[Guessing] until pilots prove it:

- **Compared with paper SOPs or screen PDFs:** verification and traceability, not just display.
- **Compared with headset-first AR:** no fatigue, shared by all shifts, lower cost per station, no dependence on one headset vendor.
- **Compared with projection-only systems:** AI checking that understands the scene, plus VR training from the same recipe.
- **Compared with VR-only training vendors:** connects training to the actual line and to quality results.
- **Compared with foreign platforms:** INR pricing, local languages, on-site support in auto clusters (Pune, Chennai–Hosur, NCR, Bengaluru, Aurangabad).

### 7.8 Business model

**Hybrid: per-station software subscription (main source) + hardware close to cost + one-time onboarding + VR seats.** Consulting is used only to win and expand accounts, not as the main business.
- Licensing *to* integrators comes later, once the product is stable.
- Licensing *from* patent holders is an option if FTO shows it is needed.

### 7.9 Revenue streams and pricing (all assumptions)

| Stream | Price (ex-GST) | Basis and assumption |
|---|---|---|
| **Paid pilot** | **₹7 lakh** for 2 stations × 12 weeks (hardware on loan) | Covers about 50–60% of pilot cost. A paid pilot screens out "free trial tourists". [Guessing] |
| **Station subscription** | **₹20,000 per station per month** (₹2.4 lakh/yr, billed annually) | One prevented defect escape or a few days faster onboarding per month should cover it. **Must be validated with pilot data.** [Guessing] |
| **Station kit** | **₹1.6 lakh** one-time (about 18% margin over ₹1.35 lakh cost) | Hardware sold close to cost to reduce the buying barrier. [Guessing] |
| **Onboarding / recipe set-up** | **₹3 lakh** per customer (first product family) | About 10 engineer-days plus travel. [Guessing] |
| **VR training licence** | **₹30,000 per headset per year** (+ headset at cost) | For ITIs and training departments. [Guessing] |
| **Cobot Bridge add-on (Phase 3)** | ₹5,000 per station per month | Future. [Guessing] |

GST on software and services is generally 18%. Confirm the rates with a chartered accountant.

### 7.10 Initial investment and operating costs (INR)

**Year 1 spend (from `reports/financial_model.py`):**

| Item | ₹ lakh | Basis |
|---|---|---|
| Fixed opex, months 1–6 (build team of 5) | 28.8 | ₹4.8 L/month: 2 founders on stipend (₹50k each), 2 CV/ML engineers (₹1 L each), 1 Unity/AR developer (₹70k), benefits, co-working, cloud |
| Fixed opex, months 7–12 (team of 7 incl. sales) | 45.6 | ₹7.6 L/month: adds an application engineer (₹60k) and a business development manager (₹80k), travel ₹80k, admin |
| Capex: 3 development station kits, 4 VR headsets, 2 GPU workstations, test fixtures | 10.1 | 3 × 1.35 + 4 × 0.34 + 2 × 1.5 + 1.65 for fixtures and mounts |
| Marketing (Part 4 budget) | 29.0 | See §9.11 |
| Legal and IP (incorporation, trademark, professional prior-art/FTO search) | 5.0 | Estimate. A full multi-country FTO opinion may cost more. |
| Software tools and licences | 2.0 | Estimate |
| Company-wide contingency (10%) | 12.1 | |
| **Total year-1 spend** | **≈ 132.6** | |
| Less base-case year-1 revenue (2 pilots + part-year subscriptions) | (20.0) | |
| **Funding need, year 1** | **≈ 112.6 (≈ ₹1.1 crore)** | |

**Salary basis:** [Likely] AmbitionBox lists computer vision engineers in India at ₹3.3–22 lakh per year; Indeed and Payscale averages are about ₹7–7.9 lakh. Glassdoor puts Unity developers at about ₹4.6 lakh median. We budget **above median** (₹12 lakh cost-to-company for CV engineers) to hire people who can ship.

**Funding sources:**
- [Certain] **Startup India Seed Fund Scheme:** grant up to **₹20 lakh** for proof of concept and prototype, plus up to **₹50 lakh** in debt or convertible instruments, given through approved incubators.
- **Other options:** an institutional incubator (for example at your institute or IIT/IISc), angel investors, and the paid pilot fee.

### 7.11 Prototype and commercialisation roadmap

| Phase | Months | Output | Exit criterion |
|---|---|---|---|
| 0. Discovery | M1–M2 | 20 plant interviews, 3 line videos, 1 pilot LOI (letter of intent) | At least 1 LOI signed |
| 1. Lab prototype (TRL 4) | M1–M5 | 1 station: guidance + 3 check types (part present, screw count, bin pick) on a real sub-assembly | ≥ 95% check accuracy on the test set; ≤ 300 ms per check |
| 2. Paid pilot (TRL 6–7) | M5–M9 | 2 stations at the pilot plant + VR trainer for that product | Agreed KPI targets met (§9.9) |
| 3. Product v1 | M9–M12 | Recipe Studio self-service, dashboard, MES export | 2nd and 3rd customers live |
| 4. Scale | Y2 | Multilingual voice, torque-tool integrations, integrator channel | 10+ customers |
| 5. Cobot Bridge | Y2–Y3 | Robot-intent overlay + hand-over steps with 1 cobot brand | One joint cell with an integrator; FTO cleared |
| 6. International | Y3+ | South-East Asia, Middle East supplier bases; US/EU only after FTO | Local partner signed |

### 7.12 Potential partnerships

| Partner type | Examples (to approach; no relationship exists) | Value |
|---|---|---|
| Manufacturing pilot partners | Mid-size Tier-1/Tier-2 suppliers in Pune, Chennai, NCR clusters; EMS firms | Real data, case study |
| Industry associations | ACMA, CII, IMTMA, ELCINA | Credibility, events, member introductions |
| Industry 4.0 centres | SAMARTH Udyog Bharat 4.0 centres: CMTI Bengaluru (SMDDC), IISc I4.0India smart factory, C4i4 Pune, IITD-AIA Foundation | Demo sites, MSME reach. [Likely] They give advisory help, not funding. |
| System integrators | Automation and cobot integrators (Universal Robots' partner network; Indian cobot maker Systemantics) | Channel for OEM plants and cobot cells |
| Hardware | Camera vendors, edge-compute distributors, VR headset resellers | Pricing, supply, co-marketing |
| Academic | Your institute's M.Tech/PhD labs | Research on CV robustness, student pipeline, funded projects |

### 7.13 Risks, limits and mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| CV accuracy fails on real lines (glare, occlusion, look-alike parts) | Lost trust, failed pilot | Control lighting in the enclosure; combine CV with tool and scanner signals; supervisor override with logging; start with high-contrast steps |
| Patent infringement (esp. patents 1, 3, 5 families) | Injunction or licence cost in that country | Professional FTO before the pilot; design-around; India-first; licence if needed |
| Customer won't pay a subscription ("we buy capex") | Revenue model breaks | Offer a 3-year prepaid option or capex licence + annual maintenance contract (AMC) |
| Long B2B sales cycles (6–12 months) | Cash runs out | Paid pilot; ITI/VR revenue as early cash; seed grant |
| Worker and union concerns about surveillance | Rollout blocked | Policy: data used for quality and training only, not individual discipline; blur faces; involve worker representatives |
| Hardware supply and price rises (e.g., Jetson price rise in 2026) | Margin squeeze | Support 2+ compute platforms; pass hardware price changes through |
| Founders lack sales experience | Slow growth | Add an industry advisor; BD hire with auto-supplier network |
| Cobot safety liability | Legal risk | Cobot Bridge is *information only*; safety stays with certified systems under ISO 10218 / ISO TS 15066; work through certified integrators |

### 7.14 How the 5 patents inform the concept (without assuming freedom to use)

| Patent | What we **learn** from it (disclosure) | What we must **not assume** |
|---|---|---|
| US 7,515,981 (LightGuide) | Projection on the work is accepted on shop floors; step-locked flow | That expiry of this patent makes projected guidance free. Later family patents (US 9,658,614; US 10,528,036; EP 2673592 B2) may still apply, and their claims must be checked |
| US 10,366,521 (Amazon) | Guidance + checking + safety zones belong together | That a headset-free version is automatically outside its claims. Claim mapping is needed |
| US 11,715,300 (step recognition) | CAD-to-training-data is the key to fast setup; cross-checking with two models reduces false passes | That any CV step recognition is fine. This is the closest patent to our core and needs the most careful FTO |
| US 12,592,164 (Permco VR) | Ordered-step VR with tool highlighting works for assembly training | That VR assembly trainers with ordered steps are free in the US |
| US 11,529,737 (Raytheon cobots) | Showing the robot's intent increases trust; VR sim → programming | That a screen or projector overlay avoids it. Check the claims and the EP family |

---

## 8. Business Model (summary canvas)

| Block | Content |
|---|---|
| Customer segments | Tier-1/2 auto suppliers; electronics/EMS; OEM plants; training centres |
| Value proposition | Fewer assembly errors, faster onboarding, full traceability; headset-free; Indian price; cobot-ready |
| Channels | Direct B2B sales, demos, trade fairs, associations, integrators, academic partners |
| Customer relationships | Paid pilot → annual contract → expansion to more stations; customer success reviews every quarter |
| Revenue streams | Station subscription (main); kits; onboarding; VR seats; later the Cobot Bridge |
| Key resources | CV/AI team, recipe library, pilot case studies, field engineers |
| Key activities | Recipe authoring, model training, deployment, support |
| Key partners | Associations, Industry 4.0 centres, integrators, hardware suppliers, incubator |
| Cost structure | Salaries (≈ 70% of opex), hardware cost of goods, travel, cloud, marketing, IP and legal |

---

## 9. Marketing Plan for India

### 9.1 Market problem and evidence of demand

- **Size of the base:**
  - [Certain] Auto components turnover was ₹6.73 lakh crore in FY25 (ACMA).
  - [Likely] Electronics production was about ₹11.3 lakh crore in FY25.
- **People problem:**
  - [Likely] About 80% of employers report talent shortages (ManpowerGroup 2025).
  - [Likely] Shop-floor attrition in auto components is above 18–20% (Autocar Pro).
  - [Likely] Weak practical skills on advanced machinery are linked to high attrition (NCAER).
- **Evidence the solution works:** [Certain] AR instructions cut errors by 82% in a controlled experiment (Tang et al., 2003). Vendor claims, such as Retrocausal's projected 60% fewer manual-assembly quality issues, are **vendor projections and not independent evidence**.
- **Evidence customers buy:**
  - [Likely] AutoVRse reports 100+ enterprise clients for industrial VR training in India.
  - [Certain] Large firms are now looking for a Dynamics 365 Guides replacement.
- **What is still missing:** direct evidence that Indian Tier-2 suppliers will pay **₹20,000 per station per month**. This is the **first thing to test** in discovery interviews (Phase 0).

### 9.2 Ideal customer profile and decision-makers

**Ideal customer profile (ICP):**
- An Indian auto or electrical component maker with ₹200–2,000 crore turnover.
- At least 3 manual assembly lines with at least 5 stations each.
- An OEM customer applying strict quality targets (PPM, the number of defective parts per million).
- High variant count, and more than 20% contract workforce.
- Has an IATF 16949 quality certificate and an existing quality-complaint problem.

| Role | What they care about | Their role in the purchase |
|---|---|---|
| Plant Head / COO | Output, OEM rating | Final approval |
| Quality Head | PPM, customer complaints, audit results | **Champion** (main internal supporter) |
| Production/Line Manager | Cycle time, worker availability | User sponsor |
| HR / Training Manager | Onboarding time, attrition | Supports the VR module |
| IT/OT Head | Network, data security, MES link | Technical gatekeeper |
| Purchase | Price, payment terms | Negotiates |

### 9.3 Segmentation and target market

The step-by-step funnel is [Guessing]. Refine it with association member lists.

1. **Total universe:** Indian manufacturers with manual assembly.
2. **Target segment:** auto components and electrical/electronics suppliers in 4 clusters: Pune–Chakan, Chennai–Hosur–Sriperumbudur, NCR (Gurugram–Manesar–Noida), Bengaluru.
3. **Year-1 serviceable list:** about **400 named accounts** that match the ICP, built from the ACMA/ELCINA/CII member lists and LinkedIn.
4. **Year-1 goal:** 2 paid pilots → 3 paying customers.

### 9.4 Competitor analysis

| Competitor / alternative | Type | Strengths | Weaknesses vs StepSure | Source confidence |
|---|---|---|---|---|
| **Paper/PDF SOPs + buddy training** | Status quo | Free, familiar | No checking, no data, slow onboarding | [Certain] |
| **LightGuide** (US) | Projected AR guidance | Mature, patent portfolio, enterprise customers | Price and support in India not verified; foreign vendor | [Likely] |
| **Retrocausal** (US) | AI video assembly copilot (Assembly Copilot, Pathfinder) | Strong AI action recognition, hardware-independent | Guidance UX and VR not core; India presence unknown | [Likely] |
| **PTC Vuforia (Expert Capture, Studio)** | Enterprise AR authoring | Big ecosystem, CAD link | Priced per user by quote; heavy enterprise focus | [Likely] |
| **Microsoft Dynamics 365 Guides** | HoloLens AR guides | Was the market reference | **Ends 31 Dec 2026**: a replacement opportunity | [Certain] |
| **AutoVRse** (Bengaluru) | VR industrial training | Indian, 100+ clients (self-reported), auto OEM logos | Training-centric; not live on-line checking | [Likely] |
| **TeamViewer Frontline, Taqtile, Augmentir, others** | Connected-worker / AR platforms | Global platforms | Not researched in detail here. Check before the viva. | Not verified |
| **In-house machine-vision (Cognex/Keyence poka-yoke)** | Point vision inspection | Very accurate for fixed checks | Checks the product, not the step sequence; no guidance or training | [Likely] |

### 9.5 Positioning statement and USP

> **For** quality and production heads at Indian component suppliers **who** lose money to assembly mistakes and slow onboarding, **StepSure** is an **AI assembly copilot** that **guides, checks and records every manual step and trains new workers in VR from the same recipe**. **Unlike** headset-based AR or VR-only training, StepSure is **headset-free on the line, priced per station in INR, and ready for cobots.**

**USP in one line:** *Checked steps, not just shown steps.*

### 9.6 Pricing and packaging strategy

| Package | Includes | Price (ex-GST) [Guessing] |
|---|---|---|
| **Pilot** | 2 stations, 12 weeks, 1 product family, VR trainer for that product, KPI report | ₹7 lakh (counted against year-1 fees if converted) |
| **Line Starter** | 5 stations, kits, onboarding, 1 VR seat | ₹8 L kits + ₹3 L onboarding + ₹12 L/yr |
| **Plant** | 20+ stations, MES integration, priority support | Volume price ₹16,000–18,000 per station per month |
| **Training Centre** | 10 VR seats + course content | ₹3 L/yr licence + headsets at cost |

**Pricing principles:**
1. Price on value: show cost-of-defect savings from pilot data.
2. Annual billing in advance.
3. Discounts of 3–5% for 3-year contracts, which is better than giving away the pilot for free.

### 9.7 Marketing channels

| Channel | How it will be used | Timing |
|---|---|---|
| **Industrial demonstrations** | A mobile demo rig (station + VR) taken to plant visits and cluster meetings. Live "find the error" challenge for line managers. | Ongoing from M4 |
| **LinkedIn** | Founder posts with weekly line-floor videos; Sales Navigator lists of quality and plant heads; small ad budget for case-study retargeting | Ongoing |
| **Trade fairs** | [Certain] **IMTEX 2027, 21–27 Jan 2027, BIEC Bengaluru** (IMTMA), with Digital Manufacturing running alongside. Startup pavilion or partner booth. Automation Expo Mumbai typically runs mid-year; 2027 dates not yet verified. | M3 (Jan 2027), M9–10 |
| **Manufacturing associations** | ACMA cluster programmes, CII/IMTMA quality and Industry 4.0 workshops, ELCINA events | M2 onward |
| **Academic–industry partnerships** | Joint workshop with your institute + a SAMARTH Industry 4.0 centre; student hackathon on assembly CV; published pilot study | M4, M10 |
| **Direct B2B sales** | Founder-led sales to 400 ICP accounts; integrator referrals | Ongoing |

### 9.8 Customer acquisition strategy

1. **Problem-first outreach.** Do not lead with "AR". Lead with "your PPM from manual assembly" and "days to train a new operator".
2. **Free 2-hour "Assembly Error Audit".** Film one station with permission and show where errors happen. Turn it into a pilot proposal.
3. **Paid pilot with agreed KPIs** (§9.9). Turn it into a published case study, with the customer's permission.
4. **Expand within each account** from 2 to 5 to 20 stations, then sister plants.
5. **Referrals inside clusters.** Suppliers to the same OEM talk to each other. Use the case study within each OEM's supplier base.

### 9.9 Pilot-project strategy (one manufacturing company)

- **Choosing the pilot company:**
  - An ICP company within 3 hours' travel.
  - A quality head who will champion the project.
  - A clear defect history on one sub-assembly with 10–25 steps.
  - Willing to share before-and-after data.
- **Scope:** 2 stations, 1 product family, 12 weeks. Weeks 1–3 setup and recipe. Weeks 4–5 shadow mode. Weeks 6–12 live.
- **Baseline first.** Measure 4 weeks of "before" data. Without a baseline the pilot proves nothing.
- **Success KPIs (agreed in writing):**
  - Assembly errors reaching end-of-line inspection: **reduced ≥ 40%** [Guessing]
  - Days for a new operator to reach standard cycle time: **reduced ≥ 30%** [Guessing]
  - Cycle-time overhead from checks: **≤ 3%**
  - Station uptime: **≥ 98%**
  - Operator acceptance survey: **≥ 70% positive**
- **Commercial terms:**
  - ₹7 lakh, paid 50% upfront and 50% at the week-6 go-live.
  - If the KPIs are met, there is a pre-agreed conversion price.
  - IP terms: the customer owns its process data; StepSure owns the software and general models.
  - NDA, and a data-protection clause in line with India's DPDP Act (the Digital Personal Data Protection Act) for operator data.

### 9.10 Sales funnel and lead generation (year 1, [Guessing])

| Stage | Number | Conversion rate assumed |
|---|---|---|
| Target accounts (ICP list) | 400 | — |
| Engaged (reply, meeting or event conversation) | 120 | 30% |
| Demo / error audit done | 40 | 33% |
| Site assessment + proposal | 10 | 25% |
| Paid pilots | 2–4 | 20–40% |
| Converted to annual contract | 2–3 | ~70% of pilots |

**Lead sources:** IMTEX (about 40% of engaged leads), association events (25%), LinkedIn (20%), referrals and academic partners (15%). [Guessing]

### 9.11 First-year marketing budget (INR)

| Item | ₹ lakh | Basis [Guessing] |
|---|---|---|
| IMTEX 2027 participation (startup pavilion/small stall, build, travel, collateral) | 7.0 | Estimate. Get the IMTMA rate card. |
| Mobile demo rig (station kit + VR headset + transport case) | 2.0 | Kit cost + case |
| LinkedIn ads + Sales Navigator (1 seat) | 4.0 | ₹3 L ads + ₹1 L tools |
| Content: demo videos, website, case study, brochures (English + 2 Indian languages) | 2.5 | Freelancer rates |
| Plant visits and demo travel (Pune, Chennai/Hosur, NCR, Bengaluru) | 5.0 | About 25 trips |
| Association memberships and cluster events | 2.0 | Estimate |
| Academic workshop + hackathon + SAMARTH centre demo | 1.5 | Venue, prizes, materials |
| Pilot support (extra VR seats, operator incentives) | 2.0 | Estimate |
| CRM and marketing tools | 0.5 | SaaS tiers |
| Marketing contingency | 2.5 | ~10% |
| **Total** | **29.0** | |

### 9.12 Key performance indicators

| KPI | Definition | Year-1 target [Guessing] |
|---|---|---|
| Qualified leads | ICP accounts with a meeting held | 120 |
| Demo → pilot conversion | Paid pilots / demos | ≥ 5% |
| **Pilot → paid conversion** | Contracts / completed pilots | ≥ 66% |
| **Customer acquisition cost (CAC)** | (Marketing + sales cost) / new customers | Year 1 ≈ ₹10–11 L (high, expected); Year 2 target < ₹6 L |
| **Annual recurring revenue (ARR)** | Subscriptions in force × 12 | ≥ ₹25 L at month 12 |
| Stations live | Paid stations in production | ≥ 10 |
| **Net revenue retention** | ARR from last year's customers this year / their ARR last year | ≥ 110% (expansion) |
| **Logo retention** | Customers renewing | ≥ 90% |
| Customer outcome | Average error reduction at live sites | ≥ 40% |
| CAC payback | CAC / monthly gross profit per customer | < 18 months |

### 9.13 12-month launch timeline (Nov 2026 – Oct 2027)

| Month | Product | Market / sales |
|---|---|---|
| **M1 Nov 2026** | Team set-up; lab station v0 | Build ICP list; 10 discovery interviews; incubator and SISFS application |
| **M2 Dec 2026** | Recipe format; first checks working | 10 more interviews; pilot LOI target; IMTEX registration |
| **M3 Jan 2027** | Demo rig ready | **IMTEX 2027 (21–27 Jan)**: demos, lead capture |
| **M4 Feb 2027** | VR trainer v0 from recipe | Follow up IMTEX leads; 15 error audits |
| **M5 Mar 2027** | Prototype validation (≥ 95% check accuracy) | **Pilot contract signed**; baseline measurement starts |
| **M6 Apr 2027** | Pilot installation | Academic workshop with a SAMARTH centre |
| **M7 May 2027** | Shadow mode → live | BD manager joins; 2nd pilot proposal |
| **M8 Jun 2027** | Dashboard v1 | Association event talks |
| **M9 Jul 2027** | Pilot KPI review | 2nd pilot starts; case-study draft |
| **M10 Aug 2027** | Recipe Studio self-service beta | Case study published; mid-year automation fair (dates to confirm) |
| **M11 Sep 2027** | MES export; multilingual voice | Pilot 1 converted to annual contract; integrator partnership |
| **M12 Oct 2027** | v1.0 release | 3 paying customers target; Year-2 plan and seed/pre-Series-A preparation |

### 9.14 Expected business outcomes (realistic assumptions)

| Scenario | End of year 1 | Basis |
|---|---|---|
| **Low** | 1 pilot, 0–1 conversion, ARR < ₹10 L | Long sales cycle; pilot slips |
| **Base** | 2 pilots, 3 customers, 10–12 stations, ARR ₹24–29 L, year-1 revenue ≈ ₹20 L | Funnel in §9.10 |
| **High** | 4 pilots, 5 customers, 25 stations, ARR ≈ ₹60 L | Strong case study + integrator channel |

**Uncomfortable truth:** **the company is not profitable in year 1 in any scenario.** Break-even (§10.5) needs about 12–13 five-station customers. In the base case that comes in **year 3**, not earlier. [Guessing]

---

## 10. Financial and Feasibility Analysis

All numbers can be re-run with `python3 reports/financial_model.py`. **Every input is an assumption** unless it is in the "verified" table below.

### 10.1 Verified market prices vs assumptions

| Item | Value | Type |
|---|---|---|
| Jetson Orin Nano Super Developer Kit | US$249 at launch (Dec 2024) → **US$399** (July 2026) | **Verified (secondary: CNX Software, HWBusters)** [Likely] |
| Meta Quest 3S (India listing) | ₹33,990 | Price-comparison site, not an official Meta price [Likely] |
| Meta Quest 3 (India listing) | ₹58,499 | Same [Likely] |
| RealWear Navigator 520 | US$3,750 (RealWear store) | [Likely] |
| Vuzix M400 | about US$1,800 | Reseller listing [Likely] |
| Computer vision engineer salary, India | ₹3.3–22 L/yr range; about ₹7–7.9 L average | AmbitionBox, Indeed, Payscale [Likely] |
| Unity developer salary, India | about ₹4.6 L median | Glassdoor [Likely] |
| Startup India Seed Fund | Grant ≤ ₹20 L; debt/convertible ≤ ₹50 L | Government scheme pages [Certain] |
| USD/INR | **₹88 per US$ used for planning** | **Assumption. Not verified. Update to the current RBI reference rate.** [Guessing] |
| Everything else (kit cost, subscription price, pilot price, opex, conversion rates) | See tables | **Estimates / assumptions** [Guessing] |

### 10.2 Prototype development cost

| Item | ₹ lakh |
|---|---|
| Team, months 1–6 (₹4.8 L × 6) | 28.8 |
| 3 development station kits (₹1.35 L each) | 4.05 |
| 4 VR headsets (about ₹34k each) | 1.36 |
| 2 GPU workstations for training (₹1.5 L each) | 3.0 |
| Test fixtures, sample parts, mounts | 1.65 |
| Software tools | 2.0 |
| Legal/IP (part-year) | 3.0 |
| **Prototype phase total** | **≈ 43.9** (≈ ₹44 lakh) |

A cheaper **academic prototype** (one station, student team, lab hardware) can be built for about **₹3–5 lakh** of hardware. That is enough for your M.Tech demonstration, but not for a paid pilot. [Guessing]

### 10.3 Monthly operating expenses (from month 7)

| Item | ₹/month |
|---|---|
| Founders' stipends (2 × ₹50k) | 1,00,000 |
| CV/ML engineers (2 × ₹1 L) | 2,00,000 |
| AR/Unity developer | 70,000 |
| Application/field engineer | 60,000 |
| Business development manager | 80,000 |
| Benefits/statutory (~10% of salaries) | 51,000 |
| Co-working (about 6 seats) | 50,000 |
| Cloud + GPU | 30,000 |
| Travel and site visits | 80,000 |
| Tools, accounting, compliance, misc | 39,000 |
| **Total** | **≈ 7,60,000** |

### 10.4 Pilot price and annual subscription

- **Pilot:** ₹7 lakh (2 stations, 12 weeks). The estimated pilot cost to us is ₹11–13 lakh (engineer time, travel, hardware wear). **We accept a loss on the first pilot** in return for data and a reference customer. [Guessing]
- **Annual subscription:** ₹2.4 lakh per station per year. A typical 5-station customer is worth **₹12 lakh ARR**, and **₹23 lakh in the first year** including kits and onboarding.

### 10.5 Revenue scenarios and break-even

Steady state: 5 stations per customer, fixed costs **₹1.2 crore per year** from year 2 (9–10 people), and 80% gross margin on subscriptions.

| Customers | Stations | ARR (₹ L) | Recurring gross profit (₹ L) | Operating profit (₹ L) |
|---|---|---|---|---|
| **5** | 25 | 60 | 48 | **−72** |
| **10** | 50 | 120 | 96 | **−24** |
| **20** | 100 | 240 | 192 | **+72** |

- **Break-even:** fixed cost ÷ recurring gross profit per customer = 120 ÷ 9.6 ≈ **12.5 customers (about 62 stations)**.
- **Hardware and onboarding margins** (about ₹2.7 L gross profit per new customer) help in the year a customer is won. They are not counted in steady-state break-even.
- **Sensitivity:**
  - If the subscription has to drop to ₹15,000 per station per month, break-even rises to about **17 customers**.
  - If the average customer has 10 stations, break-even falls to about **6–7 customers**.
  - **Station count per customer is the most important variable.** [Guessing]

### 10.6 Major financial and technical risks

| Risk | Type | Why it matters | Early warning sign |
|---|---|---|---|
| Willingness to pay below ₹20k per station per month | Financial | Break-even moves out by 1–2 years | Discovery interviews cluster below ₹12k |
| Sales cycle > 9 months | Financial | Cash gap; funding needed sooner | No pilot signed by M5 |
| Customers want capex, not subscription | Financial | Revenue gets lumpy | Purchase teams insist on a one-time PO |
| CV accuracy < 95% on real lines | Technical | Pilot KPIs fail | Shadow-mode false alarm rate > 5% |
| Model/setup effort per new product > 10 days | Technical | Onboarding margin disappears | Recipe for 2nd product takes as long as the 1st |
| Hardware price rises (e.g., the 2026 Jetson rise) | Financial | Kit margin squeezed | Supplier notices |
| FTO finds a blocking claim in India/US | IP | Redesign or licence cost | Agent's search report |
| Key engineer leaves | Operational | Delay | Single person holds model knowledge |

**Feasibility conclusion.** [Guessing]
- **Technically:** feasible with today's tools.
- **Commercially:** feasible *if* pilots prove at least about a 40% error reduction *and* customers expand past 5 stations each.
- **Financially:** needs about ₹1.1 crore before meaningful revenue, and break-even is about 2.5–3 years out.

---

## 11. Implementation Roadmap (consolidated)

```
2026 Q4  Discovery • lab prototype • SISFS/incubator • IMTEX prep
2027 Q1  IMTEX demos • validated prototype • pilot signed
2027 Q2  Pilot live • BD hire • academic workshop
2027 Q3  Pilot KPIs • case study • 2nd pilot • Recipe Studio beta
2027 Q4  v1.0 • 3 customers • integrator partner • raise next round
2028     Scale to 10+ customers • multilingual • torque/MES integrations
2028–29  Cobot Bridge with 1 integrator (after FTO) • break-even target
2029+    South-East Asia / Middle East; US/EU only after FTO
```

---

## 12. Risks and Limitations of This Study

1. **Legal status is not verified on official registers** because the patent websites could not be reached directly. Use the §4.7 checklist.
2. **The patent sample (5 + 9 others) is not a full landscape.** There are hundreds of related filings, especially from China (CN), Korea (KR) and Europe (EP). A proper landscape study would use Derwent, PatSnap or Orbit.
3. **No claim-by-claim analysis was done.** Infringement and FTO depend on the exact claim wording, which was summarised, not mapped element by element.
4. **Market numbers come from industry bodies and press.** Some, such as attrition rates and vendor client lists, are self-reported or secondary.
5. **All financial numbers are planning assumptions** and have not been validated with customers.
6. **Competitor coverage is partial.** Several global AR platforms were not researched in depth.

---

## 13. Conclusion

- **The technology is real, patented and active.** The five patents cover projected guidance, AR glasses with checking, ML step recognition, VR assembly training and AR cobot interaction, from 2005 priority to a 2026 grant. This field is busy and patents are enforced (the LightGuide family has been to court and to the PTAB). [Likely]
- **The gap is not "AR for assembly"; that already exists.** The gap is an *affordable, headset-free, check-every-step* system for Indian suppliers that reuses one process recipe for training, guidance and future cobot work. [Likely]
- **StepSure** is a realistic way to test that gap: one paid pilot, per-station pricing, India-first. **The big unknowns are willingness to pay and real-line CV accuracy.** Both can be tested within 6 months for under ₹50 lakh.
- **Before any build or sale,** get a professional freedom-to-operate opinion, at minimum on the US 11,715,300 family and the LightGuide continuation family, and check for Indian family members. [Certain] This is necessary.

---

## 14. References (direct links)

### Patents (main five)

1. US 7,515,981 B2, *Light guided assembly system*. https://patents.google.com/patent/US7515981B2/en · USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7515981 · Pre-grant publication US 2008/0121168: https://patexia.com/us/publication/20080121168 · FreePatentsOnline: https://www.freepatentsonline.com/7515981.html
2. US 10,366,521 B1, *Augmented reality assembly assistance and monitoring*. https://patents.google.com/patent/US10366521B1/en · USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10366521 · Justia: https://patents.justia.com/patent/10366521
3. US 11,715,300 B1, *Systems and methods for providing product assembly step recognition using augmented reality*. https://patents.google.com/patent/US11715300 · USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11715300 · A1: https://patents.justia.com/patent/20230245448
4. US 12,592,164 B2, *Virtual reality training simulator*. USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12592164 · Assignee listing: https://patents.justia.com/assignee/permco-inc · https://www.goveda.com/patent/US-12592164-B2
5. US 11,529,737 B2, *System and method for using virtual/augmented reality for interaction with collaborative robots in manufacturing or industrial environment*. https://patents.google.com/patent/US11529737 · A1: https://patents.google.com/patent/US20210237275A1/en · USPTO PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11529737

### Other patents and legal records

6. US 9,658,614 B2. https://patents.google.com/patent/US9658614B2/en · EP 2673592 B2: https://patents.google.com/patent/EP2673592B2 · LightGuide patent list: https://lightguidesys.com/patents/
7. IPR2024-00141 (Amazon.com v. LightGuide). https://ai-lab.exparte.com/case/ptab/IPR2024-00141/amazoncom-v-lightguide-inc
8. US 8,860,760 B2. https://patents.google.com/patent/US8860760B2/en
9. US 10,388,176 B2. https://patents.justia.com/patent/10388176 · US 11,170,657 B2: https://patents.google.com/patent/US11170657
10. US 9,589,390. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9589390
11. US 11,393,153. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11393153
12. US 2024/0241503 A1. https://patents.justia.com/patent/20240241503
13. EP 3318944. https://data.epo.org/publication-server/rest/v1.2/patents/EP3318944NWA3/document.html
14. US 11,986,963. https://patents.google.com/patent/US11986963

### Official databases for verification

15. USPTO Patent Center: https://patentcenter.uspto.gov · Patent Public Search: https://ppubs.uspto.gov/pubwebapp/ · Assignments: https://assignment.uspto.gov
16. Espacenet: https://worldwide.espacenet.com · EPO Register: https://register.epo.org
17. WIPO PATENTSCOPE: https://patentscope.wipo.int
18. Indian Patent Office public search (InPASS): https://iprsearch.ipindia.gov.in/PublicSearch · Trademark search: https://tmrsearch.ipindia.gov.in

### Research, market and pricing sources

19. Tang, A., Owen, C., Biocca, F., Mou, W. (2003). *Comparative effectiveness of augmented reality in object assembly.* CHI 2003, pp. 73–80. https://researchwith.njit.edu/en/publications/comparative-effectiveness-of-augmented-reality-in-object-assembly/
20. ACMA, FY2024-25 Industry Performance Review press release. https://acma.in/uploads/press-release/Press%20Release%20FY25.pdf
21. Electronics production FY25 (Economic Survey, as reported). https://ianslive.in/india-cruising-towards-300-billion-electronics-production-by-2026-centre--20250326140304 · https://www.bisinfotech.com/india-electronics-manufacturing-reaches-13-11-lakh-crore-milestone/
22. ManpowerGroup 2025 talent shortage (India). https://www.peoplematters.in/news/performance-management/india-faces-record-talent-shortages-80-of-employers-struggle-to-fill-roles-44082
23. Autocar Pro, auto component talent problem. https://www.autocarpro.in/news/indias-auto-component-industry-runs-into-a-deeper-talent-problem-134442
24. NCAER publications (auto-sector skills). https://ncaer.org/publication/page/22/
25. Microsoft Dynamics 365 Guides compatibility and retirement. https://learn.microsoft.com/en-us/dynamics365/mixed-reality/guides/admin-apps-solution-compatibility · Analysis: https://www.directionsonmicrosoft.com/reports/dynamics-365-retiring-guides-and-remote-assist-move-before-dec-2026/ · HoloLens discontinuation: https://videogameschronicle.com/news/microsoft-is-discontinuing-its-hololens-mixed-reality-headsets
26. AutoVRse funding and clients. https://evreporter.com/autovrse-raises-2-4-million-to-expand-ai-and-vr-training-for-automotive-manufacturing/
27. Retrocausal. https://www.edge-ai-vision.com/2022/03/retrocausal-raises-3-4-million-to-increase-manufacturers-assembly-line-quality-efficiency-and-first-time-yield/ · https://www.dcvelocity.com/articles/47653-retrocausal-unveils-retroactivity-software-for-improved-quality-control-in-manufacturing-assembly
28. PTC Vuforia Expert Capture pricing model. https://www.g2.com/products/vuforia-expert-capture/pricing
29. Permco VR training (trade press). https://www.digitalengineering247.com/article/vr-models-streamline-training-for-manufacturer/design
30. NVIDIA Jetson price rise (July 2026). https://cnx-software.com/2026/07/22/nvidia-increases-the-price-of-jetson-modules-and-devkits-by-up-to-101 · https://hwbusters.com/news/nvidia-jetson-prices-jump-up-to-101-the-249-orin-nano-super-is-now-399/
31. Meta headset India listings. https://www.smartprix.com/vr_headsets/meta-brand
32. RealWear Navigator 520. https://shop.realwear.com/products/realwear-navigator-520
33. Salaries: https://www.ambitionbox.com/profile/computer-vision-engineer-salary · https://www.payscale.com/research/IN/Job=Computer_Vision_Engineer/Salary · https://www.glassdoor.co.in/Salaries/unity3d-developer-salary-SRCH_KO0,17.htm
34. Startup India Seed Fund Scheme. https://www.indiascienceandtechnology.gov.in/funding-opportunities/startups/startup-india-seed-fund-scheme-sisfs · https://www.myscheme.gov.in/schemes/sisfs-fs
35. SAMARTH Udyog Bharat 4.0. https://samarthudyog-i40.in/ · IISc smart factory: https://www.iisc.ac.in/events/cefc-i4-0indiaiisc-smart-factory-at-iisc/
36. IMTEX 2027. https://imtex.in · Automation Expo: https://automationindiaexpo.com/post/automation-expo-2026-mumbai-dates-highlights-visitor-guide · ACMA Automechanika: https://www.jetro.go.jp/en/database/j-messe/tradefair/detail/139787
37. India cobot integrators (promotional list). https://www.industrialautomationindia.in/top-10-companies/top-10-cobot-system-integrators-automation-providers-india-2026
38. India CRI Guidelines 2025 / Section 3(k). https://www.khuranaandkhurana.com/patentability-of-cri-s-in-india-assessing-the-2025-ipo-guidelines · https://www.intepat.com/blog/cri-guidelines-2025-patent-india-3k
39. Recent academic work on AI-assisted AR assembly (background). https://arxiv.org/abs/2511.05394 · https://www.arxiv.org/abs/2601.11535

---

*Prepared as an academic and entrepreneurship study. Not legal, patent or investment advice.*

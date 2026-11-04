# Presentation Guide for the Professor
## Two Virtual Reality Competency Trainers on a Common XR Platform — IEOM 2026, Bangalore

**How to use this document.** It explains the deck slide by slide so you can present it without memorising it. Each slide has five parts: (1) what the slide is for, (2) every line explained, (3) the figures and tables explained, (4) a ready speaking script, and (5) likely questions with answers. At the end there is a single continuous script, a master Q&A list, the core concepts to hold in your head, a glossary, and advice on the hard questions about novelty and limitations.

**The one idea that ties the whole talk together.** Modern VR software (the "interaction framework" or "SDK") now lets you pick up and manipulate virtual objects without writing code. But picking things up is not *training*. To make a competency trainer you must still build four things yourself: a **task** to follow, **validation** of what the trainee did, **guidance**, and **scoring**. This paper builds two such trainers, measures exactly how much code that extra layer takes (**5,186 lines across 21 files**), and shows that both trainers — built by different people for different tasks — independently arrived at the same design rule: **derive the task from the 3-D scene, not from hard-coded values.** Everything on every slide supports that story.

**Important scope note to repeat aloud.** This is an *implementation and engineering* study. It does **not** claim the trainers improve learning. There was **no user study**. State this openly; it protects you from the most common criticism.

---

# SLIDE 1 — Title

### 1. Slide overview
Identifies the paper, the authors and the venue. The audience should register the topic (two VR trainers on one platform) and who is speaking.

### 2. Line-by-line
- **"6th IEOM India International Conference · Bangalore · Nov 2026"** — the venue. IEOM = Industrial Engineering and Operations Management, an applied/industrial audience, so they will care about practical engineering effort and real-world use, not only theory.
- **Title: "Design and Implementation of Two Virtual Reality Competency Trainers for Manual Assembly and Hand-Tool Selection on a Common Extended Reality Platform"** — unpack the key words:
  - *Competency trainer* = a VR application that not only lets you practise but also checks whether you did the task correctly (it assesses competence).
  - *Manual assembly* = putting a product together by hand; here, an electric motor.
  - *Hand-tool selection* = choosing the correct tool (e.g. the right spanner) for a job.
  - *Common Extended Reality (XR) platform* = both trainers are built on the same VR software and hardware stack, which is what makes comparing them fair.
- **Authors:** Prof. V Vasu and Binet N B (NIT Warangal, Mechanical Engineering); Mula Hruthik (independent AR/VR developer). Superscripts ¹ and ² mark the two affiliations.

### 3. Figures/tables
Background image of the VR workspace — sets the visual tone; nothing to explain numerically.

### 4. Speaking script
> "Good morning. I am presenting joint work from NIT Warangal with Binet N B and Mula Hruthik. The paper concerns two virtual-reality competency trainers — one for manual assembly of an electric motor, one for selecting the correct hand tool — both built on the *same* extended-reality platform. Our central question is a practical one: modern VR software lets you grab and move virtual objects out of the box, but what does it actually take to turn that into a *trainer* that checks competence? Let me begin with why this matters for manufacturing."

### 5. Likely questions
- **"Why two different tasks instead of one studied deeply?"** → "Because the comparison is the contribution. Two independent builds on one platform let us separate genuine design decisions from platform quirks, and reveal principles a single system cannot."

---

# SLIDE 2 — Background & Motivation

### 1. Slide overview
Explains why VR is used for industrial training, and frames the central gap: the VR framework gives you *interaction* but not *training logic*. The four boxes (Task, Validation, Guidance, Scoring) name exactly what is missing.

### 2. Line-by-line
- **"Bridging the gap between basic VR interaction and structured competency training."** — The slide's thesis in one line. "Basic VR interaction" = grabbing, pointing. "Structured competency training" = a designed programme that teaches and assesses. The paper is about the bridge between them.
- **"While current frameworks provide basic interactions like grasping, they lack the training logic required for competency."** — Commercial SDKs (software development kits) handle the physics of grabbing an object. They have no concept of a *task* or of *right vs. wrong*.
- **"The path from simple interaction to a full trainer remains undocumented."** — No prior paper reports how to build, or how much effort it takes to build, that missing logic. This is the research gap.
- **The four boxes:**
  - **Task** — "A structured procedure for the operator to perform." The ordered steps of the job (e.g. the 26 assembly steps).
  - **Validation** — "Verification of the operator's actions during training." Checking each action: was it correct?
  - **Guidance** — "Instructional support provided throughout." Hints and cues that help the trainee (highlights, 3-D references).
  - **Scoring** — "Quantitative assessment of the operator's performance." Turning performance into a number.

Significance: these four are precisely what the authors had to *write*; the slide plants them so the audience recognises them later on the result slides.

### 3. Figures/tables
Four labelled boxes — a concept diagram, not data. Explain each box as above.

### 4. Speaking script
> "Manual assembly and tool work remain highly skill-dependent, so product quality depends directly on operator competence — and that competence has to be trained. Virtual reality is an attractive medium: it is safe, repeatable, uses no material, and cheap standalone headsets have removed the old cost barrier. But here is the crucial distinction. Today's VR frameworks give you *interaction* — you can reach out and grasp a virtual object. They do not give you *training*. A trainer additionally needs four things: a defined task to follow, validation of what the trainee actually did, guidance during the task, and scoring at the end. None of these come from the framework, and the path to building them is undocumented. That gap is what this paper addresses. Let us see what the literature does and does not cover."

### 5. Likely questions
- **"Isn't assessment already part of commercial training tools?"** → "Some bespoke tools include it, but the general-purpose interaction SDKs we build on do not. Di Pasquale's 2024 review confirms structured assessment is still uncommon even in published VR assembly trainers."
- **"Why is VR better than video or a real bench?"** → "Versus a real bench: no material cost, no hazard, unlimited repetition. Versus video: it is interactive and can instrument the trainee's actions. Wang 2022 showed VR reached competency in fewer attempts than video."

---

# SLIDE 3 — Literature & Research Gap

### 1. Slide overview
Positions the paper against prior work. The table shows that earlier studies *validate* VR training but do not *quantify the engineering* behind it. The box states the gap.

### 2. Line-by-line (one line per study)
- **Di Pasquale et al. (2024) — systematic review of VR assembly:** surveyed many systems; key point — structured competency assessment is still rare. Justifies why assessment matters.
- **Yang et al. (2023) — VR in manufacturing education:** confirms effectiveness broadly, across disciplines; general support, not task-specific.
- **Wang et al. (2022) — VR engine-assembly trainer in Unity:** a concrete result — trainees reached competency in *fewer attempts* than with a video demonstration. Evidence VR works for assembly specifically.
- **Alfaro-Viquez et al. (2025) — Meta Quest 3 welding trainer:** the *closest* system to ours and the most recent; reduced execution time, but the paper omits the custom software stack behind it — i.e. it does not report the very thing we measure.
- **Lin et al. (2024); Eswaran (2024) — AR instruction authoring:** they derive the task specification as *data* from the product's CAD model rather than hard-coding it. This is the key prior idea our shared principle connects to.
- **This paper — two Quest trainers on a common platform:** our distinct move — we *quantify* the custom training layer and *compare* design decisions.
- **"Critical Research Gap… the engineering effort required to build and quantify a complete competency trainer remains unclear."** — The gap in one sentence: others prove it works; nobody measures what it costs to build.

### 3. Figures/tables
A 6-row comparison table (Study | Scope | Key establishment). It is a positioning map: the first five rows are prior art, the last row is this paper, and the right-hand column shows that none of the prior rows report build effort. *Do not read every row aloud* — group them.

### 4. Speaking script
> "The literature strongly supports that VR training works. Review papers by Di Pasquale and by Yang confirm its effectiveness, though Di Pasquale notes that structured assessment is still uncommon. For specific evidence, Wang reached competency in fewer attempts than video training. The system closest to ours is Alfaro-Viquez's 2025 Quest 3 welding trainer — effective, but it does not report the custom software behind it. Finally, Lin and Eswaran contribute an idea we return to: they derive the task directly from the CAD model rather than hard-coding it. So the pattern is clear — everyone validates *that* VR training works; nobody reports *what it takes to build one*. That engineering gap is exactly what we quantify. This leads to our objectives."

### 5. Likely questions
- **"How is your work different from Alfaro-Viquez 2025?"** → "Theirs is a user evaluation of one system; it measures training effect but not the software layer. Ours compares two systems and measures the implementation — 5,186 lines across 21 files. Different question entirely."
- **"Did you do a formal systematic review?"** → "No. We cite the relevant reviews and the closest systems to position the engineering contribution. A full systematic review was not the aim."

---

# SLIDE 4 — Objectives & Contributions

### 1. Slide overview
States the four research objectives and the three contributions. Sets the promises the rest of the talk keeps.

### 2. Line-by-line
**Objectives:**
1. **"Describe two VR competency trainers for distinct industrial tasks on a single XR platform."** — Document both systems on one platform (so they are comparable).
2. **"Identify what commercial SDKs supply vs. custom code, and quantify development effort."** — Draw the line between framework-provided and author-written, and put a number on the author-written part.
3. **"Compare task specification, validation and guidance; isolate the shared design principle."** — Compare how each system defines, checks and guides the task, and find what they have in common.
4. **"Report automated verification methods usable when interaction cannot be tested on-device."** — Explain how to verify the software when you cannot use the headset for every test.

**Contributions:**
- **"Boundary Made Explicit — 5,186 lines of code across 21 source files."** — The headline number: the size of the custom training layer. *This is the paper's main quantitative result.*
- **"Design Decisions Isolated — one shared principle: derive task specification from the scene."** — Two independent builds reached the same rule, which strengthens it.
- **"Device-Free Verification — programmatic scene checks and seeded headless simulation."** — You can verify behaviour without wearing the headset, by running the logic in software.

### 3. Figures/tables
Two columns (Objectives | Contributions). Each objective maps to a contribution: Obj 2 → boundary quantified; Obj 3 → shared principle; Obj 4 → device-free verification; Obj 1 underpins all.

### 4. Speaking script
> "We set four objectives. First, describe both trainers on one platform. Second, separate what the commercial SDK supplies from what we had to write, and quantify that effort. Third, compare how each system specifies, validates and guides its task, and isolate any shared design principle. Fourth, report how to verify such software when you cannot exercise every interaction on the headset. These map to three contributions: we make the framework boundary explicit — 5,186 lines across 21 files; we isolate one shared design principle — derive the task from the scene; and we give device-free verification methods. One point of scope, which I will stress throughout: this is an implementation account. We make no claim about learning outcomes. Here is how we set up the comparison."

### 5. Likely questions
- **"Is lines-of-code a fair measure of effort?"** → "It is a simple, reproducible lower bound. It excludes scene authoring, 3-D assets and testing, so real effort is higher. We use it to contrast with *zero* lines of interaction code — everything interactive was configured, not coded."
- **"What do you mean by 'shared design principle'?"** → "Both systems, built separately, stopped hard-coding the task and instead read it from the 3-D scene. Reaching it independently suggests it is a genuine engineering principle, not a coincidence."

---

# SLIDE 5 — Research Approach

### 1. Slide overview
Explains the method: treat the two trainers as *parallel cases* on a shared platform, characterise each the same way, measure the code boundary, and verify in software. The table proves the platforms are nearly identical, so differences are due to design, not tools.

### 2. Line-by-line
- **"Parallel Cases — two trainers built independently for different tasks; never merged."** — They were developed separately and are analysed side by side; they are not one combined system. This is the comparative method.
- **"Characterise Each System — task model, validation rule, guidance strategy, assessment behaviour."** — The four lenses applied equally to both, so the comparison is apples-to-apples.
- **"Locate Framework Boundary — census of interaction components; custom code counted in lines/files."** — How they measured the boundary: count the interaction components the SDK provided, and count the lines/files they wrote.
- **"Verify Without a Device — programmatic scene checks; seeded headless session simulation."** — How correctness was checked off-headset (expanded on later).

### 3. Figures/tables — the platform table
Six rows comparing **System A** and **System B**:
- **Engine:** Unity 6000.0.43f1 vs 6000.3.10f1 — same engine (Unity 6), different minor patch.
- **Render pipeline:** URP 17.0.4 vs 17.3 — URP = Universal Render Pipeline, Unity's graphics pipeline; near-identical.
- **Interaction SDK:** Meta Interaction SDK 201.0 vs 203.0 — the framework that supplies grasping etc.; same SDK, minor version.
- **XR backend:** OpenXR 1.14.3 vs 1.16.1 — OpenXR = the open industry standard that lets the app talk to the headset; same standard.
- **Hardware:** Meta Quest 3 vs Quest 3 & 3S — same standalone headset family.
- **Task model:** *Authored sequence, 26 steps* (A) vs *Seeded generation from rack scan* (B) — **this is the one deliberate difference**: A's task is written out; B's is generated. Everything else is held constant.

**Observation to state:** because every row but the last is effectively identical, any behavioural difference between the systems is attributable to design choices, not to the platform. The last row previews the two different task strategies.

### 4. Speaking script
> "Our method treats the two trainers as parallel cases. They were built independently, for different tasks, and never merged. We characterise each through the same four lenses — task model, validation rule, guidance strategy and assessment behaviour — then locate the framework boundary by counting interaction components against custom code, and finally verify behaviour without a device. The table shows why the comparison is fair: both systems run on Unity 6, the Universal Render Pipeline, the Meta Interaction SDK, OpenXR and the Quest 3 — differing only by minor versions. The single deliberate difference is the task model: System A uses an authored 26-step sequence, System B generates its task from a scan of the tool rack. Because the platform is otherwise constant, differences in behaviour reflect design, not tooling. One honest qualification — the two systems had different developers, so we compare only structural decisions tied to task requirements, not coding style. Let us look at System A."

### 5. Likely questions
- **"Different developers — doesn't that confound the comparison?"** → "Yes, it is a limitation we state. We mitigate it by comparing only structural decisions traceable to the task, not style. And the shared principle is *stronger* precisely because two different developers reached it independently."
- **"Why not identical SDK versions?"** → "The systems were built at different times; versions drifted by minor releases only. None of the differences we analyse depend on those version gaps."

---

# SLIDE 6 — System A: Guided Assembly of a 26-Component Electric Motor

### 1. Slide overview
Explains the first trainer and its core mechanic: a placement-validation loop that checks the right part is placed near its correct position, with three guidance channels.

### 2. Line-by-line
- **Title — "26-Component Electric Motor":** the product being assembled; 26 parts, of which only 2 are unique (the rest are identical groups: spacers, hex nuts, threaded rods, bearings).
- **"Step 1: Record Placement Targets."** — At scene start, while the motor is still assembled, the system records the 3-D position and orientation (the *pose*) of every component. These stored poses become the *targets* the trainee must match. This is the "derive from the scene" idea in action.
- **"Step 2: Trainee Interaction."** — Parts are scattered; the trainee grasps a part and releases it where they think it goes.
- **"Validation Check."** — On release, two conditions are tested: (a) is this the component required at the current step? (b) is it within a tolerance (default **0.15 m**) of its stored target pose?
- **"Yes → Snap and Lock."** — If both conditions hold, the part snaps exactly to the stored pose and locks in place.
- **"No → Reject Part."** — If either fails, the placement is rejected and the part stays free to try again.
- **"Guidance System."** — Three channels run at once: the active component is highlighted; a 3-D target display shows the assembled reference; a progress panel tracks step/time.
- **(From the paper, worth saying)** the sequence lives in an external **JSON** file — 26 assembly steps plus 26 disassembly steps — so the order can be changed without recompiling. Two caveats for later: the 8 "fasten" steps are *not* simulated as fastening (they resolve through the same placement path), and System A records *no* assessment data.

### 3. Figures/tables — Fig. 1 and the flow
- **Fig. 1** — the VR workspace: the highlighted active component, with the 3-D "Assembly Reference" model floating above the bench. It illustrates two of the three guidance channels.
- **The Yes/No flow** — a decision diagram: Interaction → Validation Check → (Yes) Snap and Lock / (No) Reject Part. Explain it as the per-step loop the trainee repeats 26 times.
- **"0.15 m" (= 15 cm)** — the acceptance tolerance. It is a *configurable* radius; the part snaps to the exact pose once inside it. System A trains sequence and part identity, not fine positioning precision.

### 4. Speaking script
> "System A is a guided assembly trainer for a 26-component electric motor. Importantly, the assembly sequence is not written into the code — it lives in an external JSON file of 26 steps, so it can be revised without recompiling. The validation mechanic works in two stages. At scene start, while the motor is still whole, the system records the pose — position and orientation — of every component; these become the placement targets. The trainee then works from scattered parts. When they release a part, the system asks two questions: is this the correct component for the current step, and is it within fifteen centimetres of its stored target pose? If both hold, the part snaps to the exact pose and locks; if either fails, it is rejected and remains free. Throughout, three guidance channels operate together: the active component is highlighted, a three-dimensional reference of the finished motor is displayed, and a progress panel tracks the trainee. Two points I will return to: the eight fastening steps are represented but not physically simulated, and System A records no assessment data. Let me show the system running."

### 5. Likely questions
- **"Why 0.15 m — isn't that coarse for a motor?"** → "It is the default acceptance radius, and it is configurable. On acceptance the part snaps to the *exact* pose, so final placement is precise. System A trains the correct sequence and part identity, not millimetre positioning. A tighter value can be set without code changes. (The paper does not report that 0.15 m was empirically tuned.)"
- **"Why hold the sequence in JSON?"** → "So the task is data, not code. The order can be edited, or reversed for disassembly, without recompiling — and it decouples the task from the engine."
- **"If fastening isn't simulated, is it really assembly?"** → "System A trains the assembly *sequence and placement*. Fastening is named in the schema but resolved as placement; simulating it in detail is exactly what System B does, and combining them is our proposed future work."

---

# SLIDE 7 — Walkthrough: Guided Assembly (VIDEO)

### 1. Slide overview
A recorded demonstration of System A in the headset. Purpose: show the placement loop and guidance working in reality, which static slides cannot convey.

### 2. Line-by-line
Only the heading "Walkthrough: Guided Assembly". No text to explain — the content is the video.

### 3. Figures/tables
The video itself. While it plays, point out: the highlighted active part, the 3-D reference model, a part snapping and locking on correct placement.

### 4. Speaking script
> "Rather than describe it further, let me show System A in operation." *(Play the clip; stay largely silent.)* "Notice the highlighted component and the three-dimensional reference above the bench — and the part snapping into place once it is both correct and close enough. That is the placement-validation loop you just saw as a diagram." *(Transition:)* "System B tackles a very different problem."

### 5. Likely questions
- **"What hardware runs this?"** → "A standalone Meta Quest 3 — no PC tether. The interaction uses bare-hand and controller grasping from the Meta Interaction SDK."
- **"Is this real-time?"** → "Yes, captured in-headset. (Note: the paper does not report a frame-rate figure; if pressed I will say so rather than guess.)"

---

# SLIDE 8 — System B: Hand-Tool Selection from a Dynamic Rack of 88 Tools

### 1. Slide overview
Explains the second trainer: selecting the correct tool from 88, driving a fastener, across three staged difficulty levels, with a weighted score. Carries the paper's key engineering message about custom code.

### 2. Line-by-line
- **Title — "Dynamic Rack of 88 Tools":** 88 grabbable tools; "dynamic" because the set of valid answers is read from the scene at runtime, not fixed in code.
- **"1. The Task — select the right tool from a rack of 88; fit it and rotate it to drive the fastener."** — The trainee must identify the correct instrument, engage it on the fastener, and physically rotate to drive it.
- **"2. Rack & Validation":**
  - **"Deliberate gaps — legal sizes scanned at start."** — The rack intentionally omits some sizes (no 31 mm spanner, no 20 mm socket). So the system *scans* the rack at session start to learn which sizes legitimately exist, instead of trusting a hard-coded table. This is "derive from the scene" for System B.
  - **"Accepted only if type, size and torque match."** — A tool is correct only if its *type* (spanner/socket/…), its *size* (within tolerance) and, where relevant, its *set torque* all match the requirement.
  - **"Wrong tool — fastener won't turn; tool logged."** — A wrong choice produces no effect (the fastener does not turn), and the rejected tool is recorded for the debrief.
- **Scoring Structure (100 points total):**
  - **"90 s exploration — no task, unscored"** — a free familiarisation stage so that scoring does not just measure unfamiliarity with the environment.
  - **"Formal Test — tool not named, scored"** — the assessment stage; the required tool is *not* named, so it tests tool knowledge.
  - **"Selection 60 / Proc 20 / 10 / 10"** — the weighting: **Selection 60**, **Procedure 20**, **Execution 10**, **Efficiency 10**. Selection dominates because choosing the right tool is the skill; efficiency is smallest on purpose.
- **"Action accepted only if tool type, size and torque all match. Rejection halts turn; tool retained for debrief."** — restates the strict acceptance rule and the debrief logging.

### 3. Figures/tables
- **Fig. 2** — a 24 mm combination spanner seated on a fastener by its working end, with a floating job label. Shows the engagement the acceptance test evaluates.
- **The scoring breakdown (60/20/10/10)** — a weighted rubric summing to 100. Efficiency is weighted least deliberately: rewarding speed on a torque operation would encourage unsafe haste.
- **(From the paper)** the rack holds 88 tools across families — e.g. 26 combination spanners and 26 ring spanners (6–32 mm), 14 sockets (8–22 mm), 9 T-handle hex keys, 8 open-end attachments, 4 torque instruments, 1 ratchet. System B is **2,764 lines across 11 files.**

### 4. Speaking script
> "System B trains hand-tool selection. The trainee faces a fastener and must choose the correct instrument from a rack of eighty-eight tools, fit it, and physically rotate it to drive the fastener. Crucially, the rack has deliberate gaps — there is no 31-millimetre spanner and no 20-millimetre socket — so the system scans the rack at session start to establish which sizes are genuinely available, rather than trusting a hard-coded table. A tool is accepted only if its type, its size within tolerance, and where applicable its set torque all match; a wrong tool simply does not turn the fastener, and it is logged for the debrief. Training is staged: a ninety-second unscored exploration so we measure tool knowledge rather than unfamiliarity, then a formal scored test in which the tool is not named. Scoring out of a hundred weights selection at sixty, procedure at twenty, and execution and efficiency at ten each — efficiency is smallest by design, because rewarding speed on a torque operation would teach unsafe habits. And here is the core engineering point: none of this logic — the task, the validation, the scoring — came from the SDK. Across both systems it took five thousand one hundred and eighty-six lines of custom code in twenty-one files. The framework lets you grab a tool; everything that makes it a trainer, we wrote. Let me show it running."

### 5. Likely questions
- **"Why scan the rack instead of a config table?"** → "Robustness. If a size is physically missing but present in a hard-coded table, the system would demand a tool that isn't there, and the trainee would be marked wrong for the *configuration's* error. Scanning the scene keeps the valid-answer set and the physical rack in sync."
- **"How is torque validated in VR?"** → "Each torque instrument has a set value and a tolerance; driving is modelled by constrained rotation. Acceptance requires the set torque to be within tolerance of the requirement. In verification, torque accumulation was checked numerically (see backup)."
- **"Why weight efficiency so low?"** → "Deliberately. On a torque task, speed is not the goal — correct selection and procedure are. Rewarding speed would reinforce the wrong behaviour."

---

# SLIDE 9 — Walkthrough: Tool Selection (VIDEO)

### 1. Slide overview
Recorded demonstration of System B. Purpose: show selection, engagement and the "wrong tool won't turn" feedback in reality.

### 2. Line-by-line
Heading only — "Walkthrough: Tool Selection". The video is the content.

### 3. Figures/tables
The clip. Point out: the trainee choosing a tool, seating it on the fastener, and the fastener turning only when the tool is correct.

### 4. Speaking script
> "Here is System B in operation." *(Play; stay silent.)* "Observe that the spanner only drives the fastener when it is the correct size — the tool choice itself is the assessment, with immediate physical feedback." *(Transition:)* "With both systems shown, let us compare the design decisions behind them."

### 5. Likely questions
- **"Can the trainee brute-force by trying every tool?"** → "Trying wrong tools is captured and penalised through the selection score, and wrong picks are logged for the debrief, so trial-and-error is visible and costs points."

---

# SLIDE 10 — Result: Design Decisions

### 1. Slide overview
The analytical heart of the paper: a side-by-side comparison of the five design problems both systems faced, and — the key message — that both independently solved the task-specification problem the same way (derive it from the scene).

### 2. Line-by-line (the five design problems)
- **Task specification — A: authored JSON (26 steps, 4 action classes) | B: generated from rack scan under coverage constraints.** How the task is defined. A writes it out; B generates it, ensuring every tool family appears ("coverage") and other constraints. *The 4 action classes are: place, insert, fasten, remove.*
- **Ground-truth source — A: component poses from the CAD model at scene start | B: tool types/sizes from the tagged rack.** Where "the correct answer" comes from. Both read it from the scene — A from the product model, B from the tagged tools.
- **Trainee validation — A: correct part within 0.15 m of target pose | B: correct type, size tolerance and torque tolerance.** How correctness is judged in each.
- **Guidance strategy — A: 3 concurrent channels (highlight, 3-D target, progress) | B: staged (90 s observe → named tool → unguided test).** How help is given: A shows everything at once; B removes help in stages.
- **Failure behaviour — A: placement rejected, component stays free | B: fastener does not turn, rejected tool kept for debrief.** What happens on a mistake.

**The hidden headline (state it explicitly):** across the top two rows, both systems *derive the task specification from the scene rather than hard-coding it* — and they reached this independently. A revised CAD model needs no re-targeting in A; a changed rack is automatically respected in B. This matches Lin et al. (2024).

### 3. Figures/tables
A 5-row, 2-column comparison table (Design Problem | System A | System B). Read it as: same problem, two solutions, one shared underlying rule in the first two rows.

### 4. Speaking script
> "This slide is the analytical core. Both systems faced the same five design problems and solved them differently. For task specification, System A authors a JSON sequence of twenty-six steps across four action classes; System B generates its task from a rack scan under coverage constraints. For ground truth, A captures component poses from the CAD model; B enumerates tool types and sizes from the tagged rack. Validation differs — proximity to a target pose versus matching type, size and torque. Guidance differs — three concurrent channels versus a staged removal of help. And failure differs — a rejected placement versus a fastener that will not turn. But notice the shared principle, which both developers reached independently: neither system hard-codes its task — both derive it from the three-dimensional scene. In A, a revised product model needs no re-targeting; in B, a changed rack is automatically respected. The motivation is identical in both: a hard-coded specification goes stale, and then a configuration error is wrongly blamed on the trainee. This is consistent with Lin's data-driven approach from 2024. Now, how do we know these systems behave as specified?"

### 5. Likely questions
- **"Is the shared principle just a coincidence of one team?"** → "The developers worked independently and we compare only task-driven structural decisions. Independent convergence is the strongest evidence that it is a genuine principle, not style."
- **"What are the four action classes?"** → "Place, insert, fasten and remove. In System A, fasten currently resolves through the placement path rather than being simulated."
- **"Does 'coverage constraint' mean every tool appears?"** → "Every playable tool family appears at least once; neighbouring identical families are separated after shuffling; a size does not recur within a window; and the assessment set excludes the training set."

---

# SLIDE 11 — Proposed VR Trainer Integration

### 1. Slide overview
Proposes — as future work, not built — how to combine the two systems into one trainer by routing each action to the system that handles it, from a single task file.

### 2. Line-by-line
- **"Unified Task Definition — combine placement and fastening into one file."** — A single task file describing a full work instruction, covering both placement (A) and fastening (B).
- **"Route by Action — direct user to System A or B."** — A dispatcher reads the action field of each step: place/insert/remove → System A's placement validation; fasten → System B's fastening mechanic.
- **(From the paper, the second proposal)** a **shared assessment layer**: extend System B's grasp-state capture (which records wrong pickups) to System A's placement errors, which A currently discards.
- **Why it is feasible:** both systems already broadcast state through event interfaces, so they can be connected without rewriting their internal logic.

> **Inconsistency to be aware of (and fix before presenting):** on the current slide the box "Unified Task Definition — combine placement and fastening into one file" is **repeated four times**. Only one box should say that; the others should read "Route by Action" and "Shared assessment layer — extend System B's grasp-state logging to System A." This is a copy-paste artefact, not part of the research. See the Inconsistencies section at the end.

### 3. Figures/tables
A flow concept: one task file → route by action → System A or System B. Present it as the dispatch idea. (Figure 4 in the paper draws implemented elements solid and proposed elements dashed; stress that the integration is *dashed* — proposed, not implemented.)

### 4. Speaking script
> "The comparison reveals a complementarity we can exploit — and I stress this is a proposal, not an implemented system. System A names fastening in its schema but resolves it as placement; System B simulates fastening in detail but presents each fastener in isolation, with no assembly around it. Each implements what the other omits. We therefore propose two steps. First, a unified task definition: one file describing a complete work instruction, with a dispatcher that routes placement actions to System A and fastening actions to System B. Second, a shared assessment layer: extend System B's capture of wrong pickups to cover System A's placement errors, which A currently discards. This is technically coherent because both systems already communicate state changes through event interfaces, so no internal logic need be rewritten. Let me conclude."

### 5. Likely questions
- **"Have you implemented the integration?"** → "No. It is a proposal, drawn dashed in our figure. It builds on interfaces both systems already expose, which is why we consider it coherent rather than speculative."
- **"What is the main technical risk?"** → "Aligning the two task schemas and the event timing so that a single work instruction drives both validators consistently. Both already use events, which lowers that risk."

---

# SLIDE 12 — Conclusion & Future Work

### 1. Slide overview
Summarises the four completed objectives, lists future work, and delivers the take-home message.

### 2. Line-by-line
**Research objectives completed:**
- **"Both trainers described by task model, validation, guidance and assessment."** — Objective 1 met.
- **"[SDK] supplies basic interaction; training layer required 5,186 lines in 21 files."** — Objective 2 met; the headline number restated. *(The slide's "DK" is a typo for "SDK".)*
- **"Shared principle: derive task specifications dynamically from scene data."** — Objective 3 met.
- **"Device-free verification: 685 generated jobs verified via headless testing."** — Objective 4 met; 685 = the torque jobs generated (200 seeds × 8 jobs per session, torque jobs) and checked automatically, with no headset.

**Next steps (future work):**
- **"Unified Work Instruction — action-field dispatch spanning placement and torque fastening."** — Build the slide-11 integration.
- **"Extended Telemetry — integrate System B's grasp-state telemetry into System A's placement verification."** — Add assessment to System A.
- **"User Evaluation — formal empirical study of learning outcomes and skill transfer."** — The study not yet done; directly addresses the main limitation.

**Key takeaway:** "Interaction can now be configured out of the box. But the competency trainer — task models, validation, guidance, assessment — still has to be engineered." — The whole paper in two sentences.

### 3. Figures/tables
Two columns (Completed | Future). Note the slide footer shows "13" while it is the 12th slide — a stale page number; see Inconsistencies.

### 4. Speaking script
> "To conclude, all four objectives are met. We described both trainers through task, validation, guidance and assessment. We showed the SDK supplies only basic interaction, while the training layer required five thousand one hundred and eighty-six lines across twenty-one files. We identified a shared principle — derive the task specification dynamically from scene data. And we verified behaviour without a device, checking six hundred and eighty-five generated jobs through headless testing. Future work follows directly: implement the unified work instruction with action-field dispatch; extend System B's telemetry into System A to give it assessment; and conduct a formal user study of learning outcomes and skill transfer. The take-home message is this: interaction can now be configured out of the box, but the competency trainer — the task models, validation, guidance and assessment — still has to be engineered. Thank you."

### 5. Likely questions
- **"Where are the 685 jobs from?"** → "System B generates jobs from seeds; 200 seeds at 8 jobs per session produced 685 torque jobs, each checked against defect conditions with zero defects found. Because generation is seeded, this needs no headset."
- **"Your strongest limitation?"** → "No user study. We therefore make no learning claim. It is the first item of future work."

---

# SLIDE 13 — Thank You / Questions

### 1. Slide overview
Closes the talk, acknowledges funding, invites questions.

### 2. Line-by-line
- **"Thank You — Questions?"** — invites Q&A.
- **Acknowledgement (from notes):** the ASEAN collaborative project between the Department of Mechanical Engineering, NIT Warangal, and Universiti Malaysia Pahang Al-Sultan Abdullah, under which part of this work was done.

### 3. Figures/tables
None.

### 4. Speaking script
> "Part of this work was carried out under the ASEAN collaborative project between NIT Warangal and Universiti Malaysia Pahang Al-Sultan Abdullah. Thank you for your attention — I would be glad to take your questions."

### 5. Likely questions
Handled in the master Q&A below.

---

# PART B — Complete continuous presentation script (introduction → conclusion)

*(Read naturally, not word-for-word. Approx. 10–10.5 minutes of speech, leaving room for the two video clips within the 12-minute slot.)*

"Good morning. I am presenting joint work from NIT Warangal with Binet N B and Mula Hruthik, on two virtual-reality competency trainers built on a single extended-reality platform — one for manual assembly of an electric motor, one for selecting the correct hand tool. Our central question is practical: modern VR software lets you grab and move virtual objects out of the box, but what does it actually take to turn that into a trainer that assesses competence?

Manual assembly and tool work remain highly skill-dependent, so product quality depends on operator competence, and that competence must be trained. VR is an attractive medium — safe, repeatable, no material cost — and standalone headsets have removed the old cost barrier. But there is a crucial distinction. Today's frameworks give you *interaction* — grasping, pointing. They do not give you *training*. A trainer additionally needs a defined task, validation of the trainee's actions, guidance, and scoring. None of these come from the framework, and the path to building them is undocumented.

The literature supports that VR training works — Di Pasquale and Yang confirm its effectiveness, though structured assessment is still uncommon; Wang reached competency in fewer attempts than video; and the closest system, Alfaro-Viquez's 2025 welding trainer, is effective but does not report its custom software. Lin and Eswaran contribute an idea we return to: deriving the task from the CAD model rather than hard-coding it. So everyone validates *that* VR training works; nobody reports *what it takes to build one*. That gap is ours to fill.

We set four objectives: describe both trainers on one platform; separate SDK-supplied interaction from custom code and quantify it; compare how each system specifies, validates and guides its task, and isolate any shared principle; and report verification methods usable off-device. These yield three contributions — the framework boundary made explicit at 5,186 lines across 21 files; one shared design principle; and device-free verification. I stress the scope: this is an implementation account, with no claim about learning outcomes.

Methodologically, we treat the trainers as parallel cases, characterised identically and compared on a shared platform. Both run Unity 6, URP, the Meta Interaction SDK, OpenXR and the Quest 3 — differing only by minor versions. The single deliberate difference is the task model. Because the platform is otherwise constant, behavioural differences reflect design, not tooling. One qualification: different developers, so we compare only task-driven structural decisions.

System A assembles a twenty-six-component motor. Its sequence lives in an external JSON file, so it can change without recompiling. At scene start, while the motor is whole, it records every component's pose; these become placement targets. The trainee works from scattered parts; on release, the system checks whether the part is correct for the step and within fifteen centimetres of its target — if so it snaps and locks, otherwise it is rejected. Three guidance channels run together: a highlight, a 3-D reference, and a progress panel. Two caveats: the eight fastening steps are represented but not simulated, and System A records no assessment data. *(Play System A clip; note the highlight, the 3-D reference, and a part locking.)*

System B trains tool selection from a rack of eighty-eight tools. The rack has deliberate gaps, so the system scans it at session start to learn which sizes genuinely exist, rather than trusting a hard-coded table. A tool is accepted only if its type, size and, where relevant, torque all match; a wrong tool simply does not turn the fastener, and is logged for the debrief. Training is staged — ninety seconds of unscored exploration, then a scored test in which the tool is not named — and scoring out of a hundred weights selection at sixty, with efficiency deliberately lowest at ten, because rewarding speed on a torque task teaches unsafe habits. And here is the core engineering point: none of this logic came from the SDK. Across both systems it took five thousand one hundred and eighty-six lines in twenty-one files. The framework lets you grab a tool; everything that makes it a trainer, we wrote. *(Play System B clip; note the fastener turning only for the correct tool.)*

Comparing the design decisions: both systems faced the same five problems and solved them differently — in task specification, ground truth, validation, guidance and failure behaviour. But both, independently, derived the task from the scene rather than hard-coding it: System A from the CAD model, System B from the rack scan. The motivation is identical — a stale specification would be blamed on the trainee rather than the configuration — and it matches Lin's data-driven approach.

How do we trust the software without testing every interaction on the headset? System B's logic can run headlessly, and because job generation is seeded, we generated and checked six hundred and eighty-five torque jobs automatically, finding zero defects. This establishes software correctness — not learning outcome.

The comparison also suggests an integration, which I present as a proposal, not an implemented system. Each system implements what the other omits, so we propose a unified task file with a dispatcher routing placement to System A and fastening to System B, plus a shared assessment layer extending System B's logging to System A. Both already communicate through events, so this is coherent rather than speculative.

In conclusion, all four objectives are met: both trainers described; the training layer measured at 5,186 lines; a shared principle — derive the task from the scene; and 685 jobs verified headlessly. Future work is to implement the unified instruction, extend telemetry to give System A assessment, and run a formal user study. The take-home message: interaction can now be configured out of the box, but the competency trainer still has to be engineered. Part of this work was supported by the ASEAN project between NIT Warangal and Universiti Malaysia Pahang Al-Sultan Abdullah. Thank you — I welcome your questions."

---

# PART C — 18 most likely technical questions, with answers

1. **There is no user study — how do you know the trainers work?**
   "Correct, and we state it. Our goal is different: to document and quantify what must be built above the interaction framework, which a single-system user study cannot reveal. Reviews already show VR training is effective. A user study on these systems is our first item of future work."

2. **What is the actual research contribution — isn't this just software documentation?**
   "Three contributions: we make the framework/custom boundary explicit and measure it (5,186 lines, 21 files); we isolate, from two independent builds, one shared design principle — derive the task from the scene; and we give device-free verification methods. The literature leaves all three undocumented."

3. **Two different developers built the systems — doesn't that confound the comparison?**
   "It is a stated limitation. We mitigate it by comparing only structural decisions traceable to task requirements, not coding style. And independent convergence on the shared principle is *stronger* evidence precisely because the developers differed."

4. **Is lines-of-code a valid measure of effort?**
   "It is a simple, reproducible lower bound — it excludes scene authoring, assets and testing. Its value here is the contrast with *zero* lines of interaction code: everything interactive was configured, not written."

5. **Why a 0.15 m placement tolerance — that seems coarse?**
   "It is a configurable acceptance radius; on acceptance the part snaps to the exact pose, so final placement is precise. System A trains sequence and part identity, not millimetre positioning. The value can be tightened without code changes. The paper does not claim it was empirically tuned."

6. **How is the task specification 'derived from the scene'?**
   "System A records component poses from the assembled CAD model at scene start; System B scans the tagged tool rack at session start. Neither hard-codes the answer, so product or rack changes are respected automatically."

7. **How did you verify the systems without a headset?**
   "System B's session logic runs headlessly through a reflection-driven layer, behind a gate of structural scene assertions and a clean-console requirement. Seeded generation let us check 685 torque jobs for three defect classes — missing instrument, unreachable target, undialable target — with zero defects."

8. **Does that verification prove correctness?**
   "It proves the systems behave as specified for the defect conditions we defined. It cannot prove the absence of unknown defect classes, and it says nothing about learning outcome. We state both limits."

9. **Why scan the rack instead of using a configuration file?**
   "Robustness. The rack has deliberate gaps; a hard-coded table would eventually request a tool that is physically absent, and the trainee would be penalised for a configuration error. Scanning keeps the valid-answer set synchronised with the physical scene."

10. **How is torque modelled and validated in VR?**
    "Torque instruments carry a set value and tolerance; driving uses constrained single-axis rotation. A tool is accepted only if the set torque matches the requirement within tolerance. In verification, torque accumulation past the half-turn wrap point was checked numerically and was monotonic."

11. **Why is efficiency weighted only 10 of 100?**
    "By design. On a torque operation, speed is not the objective — correct selection and procedure are. Rewarding speed would reinforce unsafe behaviour. Selection dominates at 60 because tool knowledge is the trained skill."

12. **Is the integrated A+B system implemented?**
    "No — it is a proposal, drawn dashed in our figure. It builds on event interfaces both systems already expose: a dispatcher routes placement to A and fastening to B, and B's logging is extended to A. That is why we regard it as coherent."

13. **What industrial value does this have — training time or cost savings?**
    "We do not measure training time; there was no user study. The value is for *builders* of such trainers: interaction is no longer the main cost, the training layer is; and deriving the task from the scene prevents configuration drift from being blamed on trainees. Evidence of operational benefit comes from the cited literature, e.g. Wang 2022."

14. **Did you measure frame rate or performance on the Quest 3?**
    "The paper reports scene complexity for System B — about 458 mesh instances, 2.1 million triangles, 63 materials. It does not report a frame-rate figure; I will not quote one I cannot support."

15. **Why is System A called a 'competency' trainer if it records no assessment data?**
    "Fair point, and we are explicit about it. System A guides and validates placement but does not score; adding assessment via the proposed shared layer is exactly our future work. System B does assess."

16. **How do you prevent trial-and-error from gaming System B?**
    "Wrong selections produce no effect and are logged, and they cost selection points. The assessment stage also withholds the tool name and excludes the training set, so recall of practised items cannot substitute for the selection rule."

17. **Only torque jobs were swept (685) — were other jobs verified?**
    "The three defect conditions in that sweep are torque-specific. Other properties — label fit, determinism, training/assessment separation — were checked separately. (If the exact non-torque coverage is queried, I will acknowledge what the paper specifies rather than overstate.)"

18. **How does this generalise beyond these two tasks and one platform?**
    "A limitation we state: two systems, two developers, one platform. But the *boundary* we characterise is set by the interaction framework, so it applies to any trainer built on such an SDK; and the shared principle is a general maintainability rule, consistent with Lin 2024."

---

# PART D — Core concepts the professor must understand before presenting

1. **Interaction framework / SDK vs. training layer.** The SDK (Meta Interaction SDK) provides grasping, pointing, hand poses, locomotion — *configured, not coded*. The training layer (task, validation, guidance, scoring) is *written by the authors*. The paper's whole point is this boundary, measured at 5,186 lines.
2. **"Derive the task from the scene."** Instead of hard-coding the correct answer, read it from the 3-D environment at runtime — A from CAD poses, B from a rack scan. Prevents the specification going stale.
3. **Pose.** An object's position *and* orientation in 3-D. System A stores poses as targets.
4. **Seeded, headless verification.** "Seeded" = a random generator started from a fixed number, so runs are reproducible. "Headless" = running the logic in software without the headset or graphics. Together they let 685 jobs be checked automatically.
5. **The weighted rubric (60/20/10/10).** Selection 60, Procedure 20, Execution 10, Efficiency 10 — efficiency lowest on purpose.
6. **Scope discipline.** Implementation study; no learning claim; no user study. Repeat when challenged.

---

# PART E — Glossary of difficult terms (simple explanations)

- **XR (Extended Reality):** umbrella term for VR/AR/MR.
- **VR (Virtual Reality):** a fully computer-generated environment viewed through a headset.
- **Competency trainer:** a trainer that also *assesses* whether the task was done correctly.
- **Interaction framework / SDK:** pre-built software for grabbing, pointing, etc.
- **Meta Interaction SDK:** Meta's such framework, used here.
- **Unity / Game engine:** the software the applications are built in.
- **URP (Universal Render Pipeline):** Unity's graphics-rendering system.
- **OpenXR:** an open standard that lets an app talk to any compliant headset.
- **Standalone headset (Quest 3 / 3S):** a headset that runs on its own, no PC.
- **JSON:** a plain-text data format; here it stores the assembly step list.
- **Pose:** position + orientation in 3-D space.
- **Tolerance:** an allowed margin (e.g. 0.15 m, or a size/torque band).
- **Torque:** rotational force; set torque = the target value a tool must apply.
- **Grasp-state capture / telemetry:** recording when and what the trainee grabs.
- **Headless simulation:** running the logic without rendering or a headset.
- **Seed / seeded generation:** a fixed starting number making random output repeatable.
- **Coverage / interleaving / exclusion set:** rules ensuring every tool family appears, identical ones are separated, and the test set differs from the practice set.
- **Action classes (place/insert/fasten/remove):** the categories a task step can belong to.
- **Dispatch / route by action:** send each step to the subsystem that handles its action type.

---

# PART F — Handling the hard questions (novelty & limitations)

**On novelty ("this is just engineering / a demo"):**
Lead with the measurement and the comparison, not the demo. "The novelty is not a new interaction technique. It is (1) making the framework-vs-custom boundary explicit and quantifying it — 5,186 lines, 21 files — which no prior paper reports; and (2) using two independent builds to isolate a shared design principle. A demonstration shows a system runs; we measure what it *costs* to build and why its design decisions recur."

**On the absence of a user study:**
Do not apologise; reframe. "We deliberately scope this as an implementation study. A learning claim requires a controlled user study, which is our stated future work. What a user study cannot show — and what we contribute — is the shape and cost of the application layer every such trainer requires."

**On generalisability (two systems, one platform):**
"A stated limitation. But the boundary we measure is imposed by the interaction framework, so it transfers to any trainer built on such an SDK; and 'derive the task from the scene' is a general maintainability principle, independently reached here and consistent with Lin 2024."

**On System A having no assessment:**
"Acknowledged openly in the paper. System A guides and validates but does not score; System B does. Unifying them — giving System A assessment via System B's logging — is precisely our proposed next step."

**On the torque-figure anomaly (be ready, see below):**
If a reviewer computes that 0.060 N·m/degree × 500° = 30 N·m, not the 54.99 N·m stated: "Thank you — the relationship between the per-degree rate, the handle travel and the reported reading needs restating; I will confirm the exact figure from our logs. The method — numeric simulation of torque accumulation past the wrap point — is unaffected." *(Do not invent a reconciling number on stage.)*

---

# PART G — Inconsistencies found in the deck (fix before the conference)

1. **Slide 11 repeats one box four times.** "Unified Task Definition — combine placement and fastening into one file" appears 4×. It should be three *distinct* ideas: (a) Unified Task Definition, (b) Route by Action, (c) Shared assessment layer (extend System B's grasp-state logging to System A). Copy-paste artefact — fix it.
2. **Slide 12 footer reads "13"** though it is the 12th slide (and the "Thank You" slide reads as 13). A stale page number from the earlier 14-slide version. Renumber.
3. **Slide 12 says "DK supplies basic interaction"** — "DK" is a typo for "SDK".
4. **The main result (5,186 lines / framework boundary) no longer has its own slide.** In the earlier deck it did. It now appears only as bullets on Slides 4 and 12. This is the paper's headline finding — the script above re-emphasises it verbally on Slide 8 and in the conclusion. Consider restoring a dedicated "Framework Boundary" slide if time allows.
5. **Torque numbers in the paper do not reconcile** (0.060 N·m/° and 500° of travel vs. a reported 54.99 N·m). Not shown on these slides, but a reviewer may raise it — see Part F. Verify against the source logs before presenting.
6. **"Shea and Morgan (1979)"** is cited in the paper for interleaving but is missing from its reference list; **Schmidt and Bjork (1992)** covers the same idea and is listed. If asked about the interleaving basis, cite Schmidt and Bjork.

*These are deck/paper issues to correct; none of them changes the research findings.*

---

*Prepared as a presenter's reference. Every number and claim is taken from the paper and the current deck; where the paper is silent (e.g. frame rate, whether 0.15 m was tuned, the torque reconciliation), that is stated explicitly rather than filled in.*

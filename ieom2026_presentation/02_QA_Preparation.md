# IEOM 2026 — Q&A Preparation

Every answer below is based only on the paper. Section numbers point to where the evidence is, so you can say "as in Section 5.4…". A **⚠** marks a question where the honest answer is a limitation. Say the limitation plainly; don't argue against it.

---

## 1. Most likely questions and suggested answers

### Q1 ⚠ "There is no user study. How do you know the trainers work?"
**Answer:** "That's right, and we say so in the paper. We make no claim about learning outcome, skill acquisition or transfer (Sections 4 and 6). The paper has a different goal. Earlier reviews already show that VR training is effective. What they don't report is what you must *build* above the interaction framework to get a trainer, and how much effort that takes. A single-system user study can't show that cost. Comparing two implementations can. A user study is the natural next step."

### Q2 "What is the research contribution? Isn't this just a software description?"
**Answer:** "There are three contributions. First, we make the framework boundary explicit and measure it: 5,186 lines across 21 files, all for capabilities the framework doesn't supply (Section 3.4, Table 3). Second, the two systems were built independently on the same platform. That lets us separate design decisions from platform constraints, and both systems reached the same principle: derive the task specification from the scene (Section 5.1). Third, we give verification methods for when interaction can't be tested outside the headset (Sections 3.6 and 5.4). The literature leaves the application layer undocumented. That is the gap."

### Q3 ⚠ "The two systems were written by different people. Couldn't the differences just be personal coding style?"
**Answer:** "Yes, that could happen, and Section 3.1 says so. For that reason we only compare decisions that are structural and that trace back to the task each system handles. Each decision is reported with the requirement that motivated it. Coding-style differences are excluded. The shared principle is the strongest finding *because* two different developers reached it independently."

### Q4 "Why is the placement tolerance 0.15 m? That's 15 cm, which is very coarse for a motor assembly."
**Answer:** "The tolerance is configurable. 0.15 m is the default (Section 3.2). It is an acceptance radius: when a part is released inside it, the part snaps to its exact stored pose and locks. System A trains sequence and part identity: the right component, at the right step, in the right place. It does not train fine positioning precision. A tighter value can be set in configuration without changing code." *(Don't claim the 0.15 m value was tuned or validated. The paper doesn't say it was.)*

### Q5 "Is lines of code a valid measure of development effort?"
**Answer:** "It's a simple measure, not a complete one. We use it to show how big the training layer is compared with zero lines of interaction code: every interaction capability was obtained by configuration. The counts are exact, not estimates. They don't include scene authoring, 3D assets or testing time, so they are a lower bound on the real effort."
*(Note: the paper doesn't discuss the limits of LOC as a measure. This answer is your reasoning; present it as such.)*

### Q6 "How did you verify the systems if you can't test hand tracking outside the headset?"
**Answer:** "Both systems build and check scene content programmatically. System B adds a three-layer gate: structural assertions over the scene graph, a clean play-mode console as a hard gate, and a headless layer that runs complete sessions through reflection (Section 3.6). Generation is seeded, so we generated 200 seeds at 8 jobs per session, which gave 685 torque jobs. We checked each one against three defect conditions and found zero defects (Table 5). System A's sequence is authored, so a sweep isn't possible. We verified it by enumeration against the component manifest." → *Backup slide 15*

### Q7 ⚠ "Does the verification prove the system is correct?"
**Answer:** "It shows the system behaves as specified for the defect conditions we knew about. It can't show that no other kind of defect exists (Section 5.4). And it shows software correctness, not training effectiveness."

### Q8 "Why derive the task specification from the scene instead of hard-coding it?"
**Answer:** "For maintenance. In System A, target poses are captured from the product model when the scene starts, so a revised model needs no repositioning of targets. In System B, the rack has deliberate gaps (no 31 mm spanner, no 20 mm socket), so a hard-coded size table would eventually ask for a tool that isn't on the wall. In both cases a stale specification would show up as a *trainee* error when it is really a *configuration* error (Section 5.1). This agrees with Lin et al. 2024, who derive assembly instructions from CAD."

### Q9 "Is the integrated system implemented? What would it take?"
**Answer:** "No. It is a proposal, and we mark it as one throughout (Sections 3.5 and 5.3; dashed boxes in Figure 4). It builds on interfaces both systems already have. System A's JSON schema already has an action field that includes 'fasten'. System B already implements fastening with tool selection and torque. Both broadcast state changes through event interfaces. Dispatching on the action field would send fasten steps to B's mechanic. The second proposal extends B's grasp-state capture to A's placement errors, without changing A's assembly logic."

### Q10 "How does System B score the trainee, and why those weights?"
**Answer:** "Each job is worth 100 points: 60 for selection, 20 for procedure, 10 for execution and 10 for efficiency. Selection dominates because tool knowledge is what we train. Efficiency is deliberately the smallest, because rewarding speed on a torque operation would reinforce the wrong behaviour. Wrong selections are captured by polling the grasp state of every tool for a rising edge, which gives one event per pickup, and the wrong tool is kept for the debrief (Section 3.3)." → *Backup slide 16*

### Q11 (industrial / IEOM angle) "What is the value for industry? Training time, cost, ROI?"
**Answer:** "The paper doesn't measure training time or cost savings, because there was no user study. Its practical value is for whoever *builds* such trainers. It shows that the interaction layer is no longer the main cost, that the training layer is where the effort goes, and that deriving the task from the scene avoids false trainee errors when the product or tool set changes. Evidence for operational benefits from VR training comes from the literature we cite, for example Wang et al. 2022, not from our own data."

### Q12 "Did you measure frame rate or performance on Quest 3 / 3S?"
**Answer:** "The paper reports scene complexity for System B: 458 mesh instances, about 2.1 million triangles and 63 materials, with about 1.17 million triangles in the 88 tools (Section 4). Frame rate isn't reported in the paper." *(Don't give a frame-rate number unless you have measured it.)*

---

## 2. Short answers (if time is very short)

| Question | One-line answer |
|---|---|
| No user study? | "Correct, and stated. This is an implementation account; a user study is the next step." |
| Novelty? | "We make the framework boundary explicit and measure it at 5,186 lines, which earlier papers don't report." |
| Why two systems? | "Same platform, independent builds, so differences reflect design decisions, not the platform." |
| Generalisable? | "Two systems, one platform: a limitation we state. The boundary itself is set by the framework, so it applies to any trainer built on it." *(the second sentence is your inference)* |
| Is the integration built? | "No. It is proposed, and drawn dashed in Figure 4." |

---

## 3. ⚠ Weak points in the paper that may attract hard questions

**Fix these in the camera-ready version if it is still possible. If not, prepare a one-sentence answer for each.**

1. **Torque numbers don't match (Table 5).** All four instruments respond at **0.060 N·m per degree**, and 12 stops to **500° of handle travel** reads **54.99 N·m**. But 0.060 × 500 = **30 N·m**, and 54.99 N·m would need about 917°. A careful reviewer can do this sum in their head. *Prepare:* the real explanation (for example, a different instrument range, an offset, a different travel figure, or a typo). The paper doesn't give one, so I can't supply it.

2. **The Table 3 row count doesn't match the text.** The text says "the lower **7** rows… the upper **5** rows" (12 rows). The printed Table 3 has **8** rows (4 framework, 4 authors), and Figure 3 has 6 + 5 = 11 boxes. *Prepare:* say that Figure 3 is the full breakdown, and correct the text.

3. **Missing reference.** Section 3.3 cites **"Shea and Morgan (1979)"** for interleaving, but it isn't in the reference list. Section 2.3 cites Schmidt and Bjork (1992) for the same idea. *Fix:* add the reference, or change the citation.

4. **"1 of 10 slots identical" (session determinism, Table 5)** while sessions are described as **8 jobs**. A reviewer may ask what a "slot" is. *Prepare:* explain whether the 10 slots include training and assessment jobs, or something else. The paper doesn't say.

5. **Only torque jobs were swept.** 200 seeds × 8 jobs = 1,600 jobs, but the defect sweep reports **685 torque jobs**. Someone may ask whether non-torque jobs were checked. *Prepare:* the three defect conditions are torque-specific; say whether other jobs were covered by the label/layout checks.

6. **94 grabbables vs 88 tools** (Section 3.4). Someone may ask what the other 6 are. The paper doesn't say. Know the answer (fasteners or workpiece items?).

7. **System A "implements none of the three" stages and records no assessment data.** So System A is a *guided* trainer, not a *competency* trainer in the assessment sense. A reviewer may question the word "competency" for System A. *Answer:* the paper says this openly (Section 3.2), and the proposed shared assessment layer is meant to fill this gap.

8. **The title says "Design and Implementation", but there is no user evaluation.** IEOM audiences often expect validation with users. Q1 covers this. Don't apologise; restate the scope.

---

## 4. Things the deck adds that are not stated explicitly in the paper

So that you are never caught out:

- **"Future work" (slide 13)**: the paper has no future-work section. The three next steps on the slide come from Section 5.3 (the two proposals) and the stated limitation in Section 6 (no user study). They are worded as "from the stated proposals and limitations".
- **The take-home line** ("Interaction can now be configured; the competency trainer still has to be written") summarises Section 5.2 in my words. It doesn't quote the paper.
- **The "Practical implications" column (slide 12)** restates findings from Sections 1.1, 3.6 and 5.1 as advice to practitioners. It adds no new claims.
- **Figure 3 was redrawn** natively on slide 8 so it is readable. The content matches Figure 3 in the paper.

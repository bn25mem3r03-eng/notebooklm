# IEOM 2026 Bangalore — Speaker Timing Plan and Checklist

**Paper:** Design and Implementation of Two Virtual Reality Competency Trainers for Manual Assembly and Hand-Tool Selection on a Common Extended Reality Platform
**Slot:** 15 min = 12 min talk + 3 min Q&A
**Deck:** `IEOM2026_VR_Competency_Trainers.pptx`. It has 14 main slides and 2 backup slides. The full speaker notes are in the PowerPoint notes pane of every slide.

---

## 1. Slide-by-slide timing

The notes contain about 1,325 spoken words. At a calm conference pace (130–140 words per minute) that takes about **9.5 to 10.5 minutes**. Pointing and pauses bring it to about 10:30. That leaves **about 1:30 of buffer** before the 12-minute mark. Don't spend the buffer on purpose; it is there for nerves, a slow clicker, or a question in the middle of the talk.

| # | Slide | Time | Ends at | The one message to land |
|---|-------|------|---------|-------------------------|
| 1 | Title | 0:20 | 0:20 | Two VR trainers on one platform. What does it take to make a trainer? |
| 2 | Background & motivation | 0:45 | 1:05 | The framework gives you grasping. A trainer needs a task, validation, guidance and assessment. |
| 3 | Literature & gap | 0:50 | 1:55 | Nobody reports what is built above the framework, or what it costs. |
| 4 | Objectives & contributions | 0:40 | 2:35 | 4 objectives, 3 contributions. Scope: implementation, not learning outcome. |
| 5 | Research approach | 0:40 | 3:15 | Parallel cases on the same platform, so differences come from design decisions. |
| 6 | System A | 1:00 | 4:15 | Targets come from the assembled model. Check: right part, within 0.15 m. |
| 7 | System B | 1:00 | 5:15 | 88-tool rack, scanned at start. Type, size and torque must match. 3 stages. |
| 8 | Result 1: boundary | 0:55 | 6:10 | Interaction was configured. The training layer was written: 5,186 lines in 21 files. |
| 9 | Result 2: design decisions | 1:05 | 7:15 | Shared principle: derive the task specification from the scene. |
| 10 | Result 3: verification | 0:55 | 8:10 | 685 jobs, 0 defects, checked headlessly. This shows software correctness, not learning. |
| 11 | Discussion: proposed integration | 0:50 | 9:00 | Each system has what the other lacks. This is a proposal, not implemented. |
| 12 | Contributions / implications / limitations | 0:45 | 9:45 | Say the limitations plainly: no user study. |
| 13 | Conclusion & future work | 0:30 | 10:15 | Interaction can be configured. The trainer still has to be written. |
| 14 | Thank you / Questions | 0:15 | 10:30 | Read the acknowledgement, then invite questions. |
| 15 | *Backup:* verification gate & data provenance | — | — | Use for "how did you verify / where do the numbers come from" |
| 16 | *Backup:* task models in detail | — | — | Use for "what is the part list / how are jobs generated / why these weights" |

### Time checkpoints (glance at a watch or the presenter-view timer)
- **Slide 5 starts at ≤ 2:40.** If you are later than that, shorten System A and System B (skip the scoring explanation on slide 7).
- **Slide 8 starts at ≤ 5:30.** This is the core result. Do not rush it.
- **Slide 11 starts at ≤ 9:15.** If you are late, say the two proposals in one sentence each and move on.
- **Slide 14 by 11:00 at the latest.**

### If you are running late, cut these first (in order)
1. Slide 3: skip the walk through the table rows. Only read the dark "GAP" box.
2. Slide 7: skip the scoring weights (60/20/10/10). They are on the backup slide.
3. Slide 9: do not read the table. Go straight to the dark "shared principle" box.
4. Slide 5: skip the Table 1 versions. Say "same engine, framework and device".

**Never cut:** slide 8 (the main result), the shared principle on slide 9, and the limitations on slide 12.

---

## 2. Final checklist

### One week before (now: the conference is 5–7 November 2026)
- [ ] **Fix or prepare answers for the four inconsistencies in the paper.** They are listed in `02_QA_Preparation.md`, section 3. The torque figure (0.060 N·m/° × 500° ≠ 54.99 N·m) is the most likely to be caught.
- [ ] Check the IEOM presenter instructions for slide size (the deck is 16:9 widescreen), file format and the upload deadline.
- [ ] Check that the presenter is **Binet N B**. The notes are written in first person for Binet. If someone else presents, change the first sentence of slide 1's notes.
- [ ] Add university or conference logos to slide 1 if IEOM or NIT Warangal requires them. The deck has none.
- [ ] Rehearse aloud with a timer **at least 3 times**. The target is 10:00–10:45. If you go over 11:15, use the cut list above.
- [ ] Rehearse once standing, with a clicker, without reading the notes.
- [ ] Practise Q&A answers out loud, especially Q1 (no user study) and Q2 (why is this research?).

### The day before
- [ ] Open the .pptx on the **conference's** laptop, or one like it (Windows + PowerPoint). The fonts are Cambria and Calibri, which ship with Office.
- [ ] Bring a **PDF export** and the .pptx on a USB drive, and also keep them in cloud/email.
- [ ] Check that Figures 1, 2 and 4 are readable on a projector. If Figure 4 is too small in the room, point to the boxes as you describe them.
- [ ] Set up presenter view so the notes and timer are visible to you only.

### In the room (5 minutes before)
- [ ] Load the deck, start the slideshow, and click through slides 1 → 2 to check the clicker.
- [ ] Know how to jump to the backup slides: type **15** then Enter, or **16** then Enter, during the slideshow.
- [ ] Have water nearby. Silence your phone.

### During the talk
- [ ] Say **"proposal, not implemented"** on slide 11, and **"no user study"** on slides 4 and 12. Reviewers listen for over-claiming.
- [ ] Say the numbers exactly: **5,186 lines / 21 files**, **26 components**, **88 tools**, **0.15 m**, **685 jobs**, **0.060 N·m per degree**.
- [ ] Point at the figure you are describing.

### Q&A (3 minutes = about 3 questions)
- [ ] Repeat each question briefly before you answer, so the room hears it and you get thinking time.
- [ ] Keep each answer to 30–45 seconds. Start with the direct answer, then give one supporting fact.
- [ ] If you don't know, say: "The paper doesn't report that. It is a good point for the user study."

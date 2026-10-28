#!/usr/bin/env python3
"""Generate the AR/VR guided assembly seminar report in the senior's NITW format."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = "/home/user/notebooklm/reports/ARVR_Guided_Assembly_Seminar_Report.docx"

doc = Document()

# ---- base style: Times New Roman 12, justified, 1.5 spacing ----
normal = doc.styles["Normal"]
normal.font.name = "Times New Roman"
normal.font.size = Pt(12)
normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
pf = normal.paragraph_format
pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
pf.space_after = Pt(6)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

for sec in doc.sections:
    sec.top_margin = Inches(1.0)
    sec.bottom_margin = Inches(1.0)
    sec.left_margin = Inches(1.1)
    sec.right_margin = Inches(1.1)


def set_font(run, size=12, bold=False, italic=False, color=None):
    run.font.name = "Times New Roman"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)


def para(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, size=12, bold=False,
         italic=False, space_after=6, space_before=0, color=None):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    if text:
        r = p.add_run(text)
        set_font(r, size=size, bold=bold, italic=italic, color=color)
    return p


def rich(parts, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, bullet=False, number=False):
    """parts: list of (text, bold, italic). bullet/number uses list style."""
    style = None
    if bullet:
        style = "List Bullet"
    elif number:
        style = "List Number"
    p = doc.add_paragraph(style=style)
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    for t, b, i in parts:
        r = p.add_run(t)
        set_font(r, bold=b, italic=i)
    return p


def bullet(text_parts):
    return rich(text_parts, bullet=True, space_after=4)


def heading_chapter(num, title):
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run(f"Chapter {num}")
    set_font(r, size=16, bold=True)
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_after = Pt(18)
    r2 = p2.add_run(title)
    set_font(r2, size=16, bold=True)


def subhead(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    set_font(r, size=12, bold=True)
    return p


def page_number_footer():
    for sec in doc.sections:
        footer = sec.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = fp.add_run()
        fld1 = OxmlElement("w:fldChar"); fld1.set(qn("w:fldCharType"), "begin")
        instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve"); instr.text = "PAGE"
        fld2 = OxmlElement("w:fldChar"); fld2.set(qn("w:fldCharType"), "end")
        run._r.append(fld1); run._r.append(instr); run._r.append(fld2)
        set_font(run, size=11)


# =====================================================================
# TITLE PAGE
# =====================================================================
para("A Seminar and technical writing report on", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=36, space_after=18)
para("An AR/VR and AI-Guided Manual Assembly", align=WD_ALIGN_PARAGRAPH.CENTER, size=16, bold=True, space_after=2)
para("Solution for Indian Manufacturing", align=WD_ALIGN_PARAGRAPH.CENTER, size=16, bold=True, space_after=24)
para("Submitted in partial fulfilment of the requirements of the degree of", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Master of Technology by", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
para("«Your Name»", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, space_after=4)
para("Roll No. «24MEM3Rxx»", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=28)
para("[Insert NIT Warangal emblem here]", align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, color=(130,130,130), space_after=28)
para("Department of Mechanical Engineering", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
para("NATIONAL INSTITUTE OF TECHNOLOGY WARANGAL", align=WD_ALIGN_PARAGRAPH.CENTER, size=14, bold=True, space_after=18)
para("2025-26", align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)

# =====================================================================
# ABSTRACT
# =====================================================================
doc.add_page_break()
para("Abstract", align=WD_ALIGN_PARAGRAPH.CENTER, size=16, bold=True, space_before=12, space_after=14)
para(
    "Indian manufacturing still assembles a large share of its products by hand, from automotive "
    "wire harnesses and switchgear to pumps and electronic sub-assemblies. Manual assembly brings "
    "recurring problems: wrong or missed parts, incorrect sequence, slow onboarding of new and "
    "contract workers, out-of-date paper work instructions, and little traceability. This report "
    "proposes StepSure, a station-mounted AI assembly copilot that guides each manual step, verifies "
    "it with a camera and connected tools before the next step unlocks, trains new workers in virtual "
    "reality from the same digital process recipe, and is designed to add human-cobot collaboration "
    "later. The concept is informed by five real, independently verifiable patents covering projected "
    "AR guidance, AR glasses with assembly verification, machine-learning step recognition, VR "
    "assembly training, and AR/VR interaction with collaborative robots. Importantly, this report "
    "distinguishes a patent's technical disclosure from the scope of its granted claims, flags which "
    "records are granted patents and which are applications, and treats every financial figure as a "
    "clearly labelled planning assumption rather than a forecast. The report follows an "
    "academic-industrial structure covering the problem and opportunity, a patent portfolio overview, "
    "the unique value proposition, market analysis, business model, an intellectual-property and "
    "commercialization strategy, financial projections, and a 36-month implementation roadmap. Under "
    "the stated assumptions, the concept is technically feasible today and could reduce assembly "
    "errors and onboarding time materially, but it is not profitable in year one and reaches "
    "break-even only after roughly twelve to thirteen customers; both the willingness to pay and "
    "real-line computer-vision accuracy must be validated through a paid pilot before any wider "
    "commitment.",
)
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(8)
p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
r = p.add_run("Keywords—"); set_font(r, bold=True)
r2 = p.add_run("Augmented reality, virtual reality, guided manual assembly, computer vision, pose "
               "estimation, assembly verification, human-robot collaboration, cobots, digital twin, "
               "freedom to operate, Indian manufacturing, Industry 4.0.")
set_font(r2)

# =====================================================================
# CONTENTS (static, matches chapter order)
# =====================================================================
doc.add_page_break()
para("Contents", align=WD_ALIGN_PARAGRAPH.CENTER, size=16, bold=True, space_before=12, space_after=18)
contents = [
    ("Abstract", "ii"),
    ("Chapter 1  Introduction", "1"),
    ("Chapter 2  Problem and Opportunity", "3"),
    ("Chapter 3  Patent Portfolio Overview", "5"),
    ("Chapter 4  Unique Value Proposition (UVP)", "9"),
    ("Chapter 5  Market Analysis", "11"),
    ("Chapter 6  Business Model", "13"),
    ("Chapter 7  IP and Commercialization Strategy", "15"),
    ("Chapter 8  Financial Projections", "17"),
    ("Chapter 9  Implementation Roadmap", "19"),
    ("Chapter 10  Conclusion", "21"),
    ("References", "22"),
]
for name, pg in contents:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    tab = p.paragraph_format.tab_stops
    from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
    tab.add_tab_stop(Inches(6.1), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    r = p.add_run(name + "\t" + pg); set_font(r)

# =====================================================================
# CHAPTER 1 INTRODUCTION
# =====================================================================
heading_chapter(1, "Introduction")
para(
    "India's manufacturing sector is growing quickly and is central to national programmes such as "
    "Make in India and the production-linked incentive (PLI) schemes. Yet a large share of actual "
    "assembly work is still done by hand. Automotive component suppliers, electrical and electronics "
    "manufacturers, and general engineering plants assemble wire harnesses, switches, lamps, pumps, "
    "seats, meters and sub-assemblies manually, often across many low-volume product variants. As "
    "product mixes widen and quality expectations from original equipment manufacturers (OEMs) rise, "
    "manual reliance produces bottlenecks and quality escapes, creating an urgent need for "
    "affordable, worker-friendly digital assistance on the shop floor."
)
para(
    "The common problems in manual assembly are well known: the wrong part is picked, a step is "
    "missed, the sequence is wrong, or a fastener is left loose; new and contract workers take days "
    "or weeks of buddy training to reach line speed; paper and PDF work instructions go out of date "
    "and are rarely read during work; and there is no reliable record of who did which step and when. "
    "Attrition on Indian shop floors makes this worse, because the training burden never ends."
)
para(
    "Augmented reality (AR), virtual reality (VR) and computer vision (CV) offer a practical answer. "
    "AR shows the next instruction on top of the real work, by projection, on a screen, or in glasses. "
    "VR lets a trainee practise the whole assembly in a 3D virtual workplace before touching real "
    "parts. Computer vision and artificial intelligence (AI) let a camera recognise parts, hands and "
    "the current assembly state, so the system can confirm that a step was done correctly or warn the "
    "worker. A digital twin keeps a live digital copy of the station so the same process data can "
    "drive training, guidance and analytics. Later, the same platform can coordinate a collaborative "
    "robot (cobot) working next to the operator."
)
para(
    "The evidence that AR guidance helps is long-standing. In a controlled experiment, Tang et al. "
    "(CHI 2003) found that overlaying 3D instructions on the actual work pieces reduced assembly "
    "errors by 82 percent compared with a paper manual, a computer screen and an unregistered "
    "head-mounted display [9]. This was a laboratory study with simple tasks, so real-factory gains "
    "will be smaller and more variable, but the direction is clear."
)
para(
    "The technical foundation of the proposed solution is informed by five real patents, each "
    "covering a different part of the problem:"
)
rich([("Projected-light guided assembly ", True, False), ("[1]", False, False),
      (": instructions projected directly onto the work.", False, False)], number=True, space_after=4)
rich([("AR glasses for assembly assistance and monitoring ", True, False), ("[2]", False, False),
      (": wearable guidance with camera-based verification.", False, False)], number=True, space_after=4)
rich([("Machine-learning assembly step recognition ", True, False), ("[3]", False, False),
      (": AI that recognises the current step and overlays a position cue.", False, False)], number=True, space_after=4)
rich([("Virtual reality assembly training ", True, False), ("[4]", False, False),
      (": step-sequenced VR training with haptic feedback.", False, False)], number=True, space_after=4)
rich([("AR/VR interaction with collaborative robots ", True, False), ("[5]", False, False),
      (": showing a robot's planned motion and aiding programming.", False, False)], number=True, space_after=4)
para(
    "This report is explicitly patent-informed, not patent-protected. It uses the published technical "
    "disclosures of these patents to shape an architecture, while keeping a clear separation between "
    "what a patent teaches (its disclosure, which is public) and what it legally protects (its granted "
    "claims, which are narrower). It covers the problem and opportunity, a patent portfolio overview, "
    "the unique value proposition, market analysis, the business model, an IP and commercialization "
    "strategy, financial projections and an implementation roadmap, aiming at a realistic, affordable "
    "solution for Indian manufacturing."
)

# =====================================================================
# CHAPTER 2 PROBLEM AND OPPORTUNITY
# =====================================================================
heading_chapter(2, "Problem and Opportunity")
subhead("A. Existing Challenges in Manual Indian Assembly")
para("Manual assembly lines in India face a set of connected operational and economic challenges that "
     "limit quality and productivity.")
subhead("1) Quality escapes from human error:")
para("A wrong part, a missed screw, a wrong connector or an incorrect torque passes down the line as "
     "rework or scrap, and sometimes reaches the OEM as a field complaint. For a Tier-1 or Tier-2 "
     "supplier, defective-parts-per-million (PPM) penalties and lost OEM ratings are a direct cost.")
subhead("2) Slow onboarding and high attrition:")
para("New and contract workers typically need days to weeks of buddy training to reach standard cycle "
     "time. Industry reporting places shop-floor attrition in auto components above 18-20 percent, so "
     "the training burden is continuous [11]. About 80 percent of Indian employers report difficulty "
     "finding skilled staff [10].")
subhead("3) Out-of-date paper instructions and high variant count:")
para("Paper and PDF standard operating procedures (SOPs) are hard to keep current, and are rarely "
     "consulted during the work itself. Indian suppliers run many low-volume variants, so the right "
     "instruction for the exact variant is often unclear at the station.")
subhead("4) No verification and no traceability:")
para("Most stations cannot confirm that each step was done correctly, and keep no per-unit record of "
     "who did which step and when. Vision inspection, where present, usually checks the finished "
     "product rather than guiding and checking each step in sequence.")
subhead("5) The headset and platform risk:")
para("Headset-first AR has struggled on Indian shop floors because of cost, comfort over a full shift, "
     "hygiene when shared across shifts, and narrow field of view. The risk is concrete: Microsoft "
     "stopped producing HoloLens 2 in 2024, and its industrial AR applications, Dynamics 365 Guides "
     "and Remote Assist, stop being available after 31 December 2026 [8]. Plants that invested in that "
     "platform must migrate.")
subhead("B. Opportunity for an India-Specific Assembly Assistant")
para("These constraints create a large opportunity for an affordable, headset-free, check-every-step "
     "assistant tuned to Indian conditions. The underlying demand is substantial:")
bullet([("Large, growing base: ", True, False),
        ("Indian auto-component turnover reached ₹6.73 lakh crore (about US$80.2 billion) in "
         "FY25, up 9.6 percent, with a 14 percent five-year CAGR (ACMA) [6].", False, False)])
bullet([("Electronics scale-up: ", True, False),
        ("Indian electronics production was about ₹11.3 lakh crore in FY25, with mobile phones "
         "alone about ₹5.45 lakh crore (Economic Survey, as reported) [7].", False, False)])
bullet([("Proven effect: ", True, False),
        ("AR guidance cut assembly errors by 82 percent in a controlled study [9].", False, False)])
bullet([("A platform gap to fill: ", True, False),
        ("The Dynamics 365 Guides retirement leaves customers looking for a replacement [8].", False, False)])
para("The opportunity is strongly aligned with Make in India, the push toward Industry 4.0, and the "
     "Startup India Seed Fund Scheme, which offers up to ₹20 lakh for proof-of-concept and "
     "prototype development through approved incubators [12].")

# =====================================================================
# CHAPTER 3 PATENT PORTFOLIO OVERVIEW
# =====================================================================
heading_chapter(3, "Patent Portfolio Overview")
para(
    "The proposed approach is patent-informed. The design draws on the technical disclosures of five "
    "real patents to shape its architecture, while taking care to avoid infringement through amended "
    "mechanisms, different control logic and India-specific design choices, confirmed by a "
    "professional freedom-to-operate (FTO) review before any build or sale."
)
para(
    "A note on kind codes, because it matters for this report's rigor. In the United States, a code "
    "ending in B1 or B2 means a granted patent; A1 means a published application that is not yet "
    "granted. The legal status of each record below (in force, lapsed or expired) was not verified on "
    "an official register for this report and is marked accordingly; these should be confirmed on the "
    "USPTO Patent Center, Espacenet and the Indian Patent Office InPASS search before the final "
    "submission.", italic=False
)

patents = [
    ("1) Patent 1 – Light Guided Assembly System [1]:",
     "US 7,515,981 B2 (granted). Inventors: Paul Ryznar and James Ryznar. Owner: LightGuide, Inc. "
     "(formerly OPS Solutions LLC). Priority 2005; US term of about 20 years from filing points to "
     "roughly 2026, so it is near expiry if maintenance fees were paid; the later family members "
     "US 9,658,614 B2 and US 10,528,036, and EP 2673592 B2, run later. Status not officially verified.",
     "This patent projects visual indicators (arrows, highlighted bins, locations, text) directly onto "
     "the work area and steps the operator through the assembly in order. ",
     "Contribution to the proposed system: it is the headset-free, station-mounted form of AR that "
     "suits a fixed overhead camera plus projector or screen. It is the primary prior art any "
     "projected-AR product must be compared against. Expiry of the 2005 patent does not make the idea "
     "free to use, because the later family patents remain in force and have been litigated."),

    ("2) Patent 2 – AR Assembly Assistance and Monitoring [2]:",
     "US 10,366,521 B1 (granted). Inventors: Jason L. Peacock, Joshua J. Watson, Scott M. Wilcox. "
     "Owner: Amazon Technologies, Inc. Filed about 2017; expected term to about 2037 if fees are paid. "
     "Status not officially verified.",
     "Workers wear AR glasses that show the information for the current step. Camera image data is used "
     "to verify the assembly step, and the disclosure also shows safe walking paths and restricted "
     "areas in the glasses. ",
     "Contribution: it demonstrates that guidance and camera-based verification belong together, and "
     "adds safety-zone overlays that later connect naturally to cobot cells. It is important prior art "
     "showing the general idea of AR guidance plus verification is already known, so novelty must lie "
     "in how verification is done, not that it is done."),

    ("3) Patent 3 – Assembly Step Recognition Using AR [3]:",
     "US 11,715,300 B1 (granted). Inventors: Yuliang Guo, Xinyu Huang, Liu Ren (assignee probably "
     "Robert Bosch GmbH; confirm on the front page). Filed 2022; expected term to about 2042. Status "
     "not officially verified.",
     "A first machine-learning model, trained on data generated from 2D images and matching 3D CAD "
     "models, turns a camera image into feature vectors; these are matched to feature-vector templates "
     "to identify the base and incoming components and the current step; a second model verifies that "
     "decision; and an AR position indicator shows where the part goes. ",
     "Contribution: this is almost exactly the AI object-recognition core of the proposed system, and "
     "therefore its single biggest FTO risk, especially for any sale into the United States. The "
     "proposed system must use a different recognition method (for example hand-action recognition or "
     "depth-based state comparison) or secure a licence, confirmed by counsel."),

    ("4) Patent 4 – Virtual Reality Training Simulator [4]:",
     "US 12,592,164 B2 (granted). Owner: Permco, Inc. (inventors to be taken from the front page). "
     "Filed 2022; granted 2026; expected term to about 2042. Status not officially verified.",
     "A VR headset shows a virtual workbench, tools and components; the system shows an ordered list "
     "of steps and highlights the tool and location for each; one embodiment uses a haptic glove to "
     "teach workers to feel surface defects such as burrs. ",
     "Contribution: it matches the VR-training half of the proposed system and shows that ordered-step "
     "VR assembly training was patented in the US as recently as 2026. The design reuses one process "
     "recipe for both VR pre-training and floor guidance, so content is authored once."),

    ("5) Patent 5 – VR/AR Interaction with Collaborative Robots [5]:",
     "US 11,529,737 B2 (granted). Inventor: Kristen M. Stone. Owner: Raytheon Company. European family "
     "member EP 4096874. Priority 2020; granted 2022; expected US term to about 2040. Status not "
     "officially verified.",
     "A wearable AR/VR headset shows the cobot's planned movement path over the real or virtual cell "
     "before it moves, and a VR training simulation feeds information to the robot workstation to help "
     "program the path. ",
     "Contribution: it covers exactly the future human-cobot extension of the proposed system. Any "
     "robot-intent overlay or hand-over feature must be checked against its claims and its European "
     "family. Note that such an overlay is an information aid, not a safety function; safety remains "
     "with certified robot safety systems under ISO 10218 and ISO/TS 15066."),
]
for title, biblio, tech, contrib in patents:
    subhead(title)
    rich([("Record: ", True, False), (biblio, False, False)], space_after=4)
    para(tech + "")
    rich([("Contribution: ", True, False), (contrib.split("Contribution", 1)[-1].lstrip(":").strip() if False else contrib.split(": ", 1)[-1] if contrib.startswith("Contribution") else contrib, False, False)], space_after=8) if False else rich([(contrib, False, False)], space_after=8)

# =====================================================================
# CHAPTER 4 UVP
# =====================================================================
heading_chapter(4, "Unique Value Proposition (UVP)")
para("StepSure offers a differentiated solution for Indian manual assembly across five parameters. The "
     "working name should be cleared on the Indian trademark registry before use.")
subhead("1) Checked steps, not just shown steps:")
para("Unlike display-only guidance, every step is verified by a camera and connected tools (part "
     "present and correctly placed, fastener count, hand path to the correct bin, torque-tool OK "
     "signal) before the next step unlocks. This is the core value and the main point of difference "
     "from projection-only and PDF-on-screen systems.")
subhead("2) Headset-free on the line:")
para("The default is a fixed overhead camera with a projector or screen, so there is no headset "
     "fatigue, the station is shared across all shifts, it works with gloves, and there is no "
     "dependence on a single headset vendor, an important lesson from the HoloLens and Dynamics 365 "
     "Guides exit. VR is used for training only, where a headset makes sense.")
subhead("3) One recipe, three outputs:")
para("A single digital process recipe (steps, parts, tools, checks, CAD references) drives projected "
     "or screen guidance, computer-vision checking, and automatically generated VR training content. "
     "Later it also drives cobot hand-over steps. Customers author the process once instead of paying "
     "three times for the same knowledge.")
subhead("4) Built for Indian conditions:")
para("Icon-first user interface with Hindi, Tamil, Marathi and Kannada voice and text for low-literacy "
     "and multilingual shop floors; pricing per station in INR; hardware sold close to cost; and "
     "on-site support in the main auto clusters (Pune, Chennai-Hosur, NCR, Bengaluru, Aurangabad).")
subhead("5) Cobot-ready:")
para("The same recipe and the safety-zone concept extend to a future Cobot Bridge that shows a robot's "
     "next move on the station display and runs guided hand-over steps, positioning the product for "
     "the shift toward human-cobot collaboration without forcing it on day one.")
para("In one line: every step checked, every new worker productive in days, without headsets, at an "
     "Indian price.", bold=True)

# =====================================================================
# CHAPTER 5 MARKET ANALYSIS
# =====================================================================
heading_chapter(5, "Market Analysis")
subhead("1) Market Overview:")
para("Indian auto-component turnover was ₹6.73 lakh crore (about US$80.2 billion) in FY25, growing "
     "at a 14 percent five-year CAGR [6], and electronics production was about ₹11.3 lakh crore in "
     "FY25 [7]. Both sectors employ large and growing manual-assembly workforces, which is the base "
     "StepSure serves. The served market for a first product is narrower: an estimated 400 named "
     "accounts in four clusters that match the ideal customer profile.")
subhead("2) Adoption Gap:")
para("Digital work-instruction and verification adoption on Indian manual lines is low, and much of "
     "what exists is either expensive imported AR or training-only VR. The gap is not AR for assembly, "
     "which already exists, but an affordable, headset-free, check-every-step system reusing one "
     "recipe for training, guidance and future cobot work.")
subhead("3) Competitive Landscape:")
para("The market includes several alternatives, each with a different focus:")
bullet([("Paper / PDF SOPs plus buddy training (status quo): ", True, False),
        ("free and familiar, but no checking, no data, slow onboarding.", False, False)])
bullet([("LightGuide (US): ", True, False),
        ("mature projected-AR guidance with a patent portfolio; India pricing and support unverified.", False, False)])
bullet([("Retrocausal (US): ", True, False),
        ("strong AI action-recognition assembly copilot; guidance UX and VR not core; India presence unknown.", False, False)])
bullet([("PTC Vuforia (Expert Capture, Studio): ", True, False),
        ("large enterprise AR authoring ecosystem; priced per user by quote.", False, False)])
bullet([("Microsoft Dynamics 365 Guides: ", True, False),
        ("the former market reference, ending 31 December 2026, which is a migration opportunity [8].", False, False)])
bullet([("AutoVRse (Bengaluru): ", True, False),
        ("Indian industrial VR training with 100+ enterprise clients (self-reported); training-centric, not live line checking [13].", False, False)])
bullet([("In-house machine vision (point inspection): ", True, False),
        ("accurate for fixed checks, but checks the product, not the step sequence, and gives no guidance or training.", False, False)])
para("StepSure occupies a position none of these fully covers: verified step-by-step guidance plus "
     "VR training from one recipe, headset-free, priced in INR.")
subhead("4) Customer Segments:")
bullet([("Tier-1 and Tier-2 auto-component suppliers (harness, switches, lamps, brake and steering sub-assemblies) – the pilot segment.", False, False)])
bullet([("Electronics and EMS and electrical (box build, meters, switchgear, EV chargers, BMS packs).", False, False)])
bullet([("OEM plants (two- and four-wheeler, commercial vehicles, tractors) for scale and traceability.", False, False)])
bullet([("Industrial training centres (ITIs, NSDC partners, university labs) for VR training seats.", False, False)])

# =====================================================================
# CHAPTER 6 BUSINESS MODEL
# =====================================================================
heading_chapter(6, "Business Model")
para("The revenue model is a hybrid designed to lower customer CapEx and build recurring revenue. All "
     "prices below are planning assumptions that must be validated with pilot data.")
subhead("1) Per-station software subscription (main stream):")
para("The core recurring revenue is a per-station subscription of about ₹20,000 per station per "
     "month (₹2.4 lakh per station per year), billed annually. One prevented defect escape or a few "
     "days of faster onboarding per month should justify it.")
subhead("2) Hardware kit near cost:")
para("Each station kit (camera, edge AI computer, display or projector, mount and I/O) is sold at "
     "about ₹1.6 lakh, a modest margin over an estimated ₹1.35 lakh landed cost. Hardware is "
     "priced close to cost to reduce the buying barrier.")
subhead("3) Onboarding and recipe set-up:")
para("A one-time fee of about ₹3 lakh per customer for the first product family covers process "
     "digitisation, recipe authoring, and WMS/ERP or MES integration.")
subhead("4) VR training licence:")
para("For ITIs and training departments, about ₹30,000 per headset per year, with headsets supplied "
     "at cost. One headset serves many trainees.")
subhead("5) Cobot Bridge add-on (future):")
para("A later add-on of about ₹5,000 per station per month for robot-intent display and guided "
     "hand-over, once FTO is cleared.")
para("A paid pilot (about ₹7 lakh for two stations over twelve weeks) is the entry point; it "
     "screens out non-serious prospects and funds a reference case study. Goods and services tax (GST) "
     "on software and services is generally 18 percent; confirm rates with a chartered accountant.")

# =====================================================================
# CHAPTER 7 IP AND COMMERCIALIZATION
# =====================================================================
heading_chapter(7, "IP and Commercialization Strategy")
para("The strategy leverages existing patented concepts while building defendable, India-specific IP, "
     "and it rests on a correct reading of what patents actually protect.")
subhead("1) Disclosure versus claims, and non-infringement:")
para("A patent's disclosure (its description and drawings) is public and may be learned from and "
     "cited; its granted claims alone define what the owner can stop others from doing, and "
     "infringement requires every element of at least one claim. Patents are also territorial: a US "
     "patent is enforceable only in the US and does not stop anyone in India unless an Indian family "
     "member exists. The proposed non-infringement measures therefore include proprietary mechanical "
     "and mounting designs, a different computer-vision recognition method from the template matching "
     "in [3], and India-specific gripper and lighting design. None of this can be assumed safe without "
     "a professional FTO opinion, which must be obtained before any build or sale, starting with an "
     "Indian InPASS search and then the US and EU if exporting.")
subhead("2) Patentability of the firm's own IP in India:")
para("Section 3(k) of the Patents Act excludes a computer programme per se, but the 2025 "
     "Computer-Related Inventions guidelines and Delhi High Court case law allow inventions that show "
     "a technical effect. Any StepSure filing should be drafted around a technical effect, such as "
     "improved detection accuracy under occlusion or the control of tools and robots, rather than a "
     "better information display alone.")
subhead("3) Technology transfer and alliances:")
bullet([("OEM integrators and automation vendors: ", True, False),
        ("bundle StepSure with existing lines (conveyors, torque tools, MES).", False, False)])
bullet([("Industry bodies and Industry 4.0 centres: ", True, False),
        ("ACMA, CII, IMTMA, and SAMARTH Udyog Bharat 4.0 centres for demos and MSME reach (advisory, not funding).", False, False)])
bullet([("Government schemes: ", True, False),
        ("Startup India Seed Fund Scheme for proof-of-concept and prototype support [12].", False, False)])
subhead("4) Future indigenous patent filings:")
bullet([("A depth-plus-action verification method robust to hands blocking the view.", False, False)])
bullet([("India-specific multilingual SKU and label recognition using computer vision.", False, False)])
bullet([("A headset-free robot-intent overlay for cobot hand-over at a manual station.", False, False)])

# =====================================================================
# CHAPTER 8 FINANCIAL PROJECTIONS
# =====================================================================
heading_chapter(8, "Financial Projections")
para("The financial model focuses on scaling the high-margin per-station subscription. Every figure is "
     "a clearly labelled assumption, not a forecast, and can be reproduced from the accompanying model "
     "script. A standard customer is assumed to run five stations.")
# table
tbl = doc.add_table(rows=1, cols=4)
tbl.style = "Light Grid Accent 1"
hdr = tbl.rows[0].cells
heads = ["Metric", "Year 1 (Development & Pilot)", "Year 2 (Early Scale-Up)", "Year 3 (Expansion & Break-Even)"]
for c, h in zip(hdr, heads):
    c.paragraphs[0].add_run(h).bold = True
    for rr in c.paragraphs[0].runs:
        set_font(rr, size=11, bold=True)
rows = [
    ("Projected revenue", "₹0.2–0.3 Cr (2 paid pilots)", "₹1.2–1.5 Cr (3–5 customers)", "₹3–4 Cr (10–15 customers)"),
    ("Gross margin", "~45% (incl. hardware)", "~65% (subscription-led)", "~70%"),
    ("Key driver", "Paid pilots, validation", "Tier-1/2 adoption, referrals", "Multi-plant expansion"),
    ("Break-even", "N/A", "N/A", "~12–13 customers (≈62 stations)"),
]
for name, y1, y2, y3 in rows:
    cells = tbl.add_row().cells
    for cell, val, boldv in zip(cells, [name, y1, y2, y3], [True, False, False, False]):
        cell.paragraphs[0].text = ""
        r = cell.paragraphs[0].add_run(val)
        set_font(r, size=11, bold=boldv)
para("")
para("Basis and assumptions (all in INR):", bold=True, space_after=4)
bullet([("Subscription ₹20,000/station/month; a 5-station customer is ₹12 lakh of annual "
         "recurring revenue (ARR) and about ₹23 lakh in the first year including kit and onboarding.", False, False)])
bullet([("Year-1 spend is about ₹1.33 crore (team, capex, marketing, legal/IP, 10% contingency); "
         "with about ₹20 lakh of pilot revenue, the year-1 funding need is about ₹1.1 crore.", False, False)])
bullet([("Steady-state fixed cost about ₹1.2 crore per year (9–10 people); recurring gross "
         "profit per 5-station customer about ₹9.6 lakh; break-even ≈ 1.2 Cr ÷ 9.6 L ≈ "
         "12.5 customers.", False, False)])
bullet([("Sensitivity: if subscription falls to ₹15,000/station/month, break-even rises to about "
         "17 customers; if the average customer runs 10 stations, it falls to about 6–7. Stations "
         "per customer is the most important variable.", False, False)])
para("Salary basis: computer-vision engineers in India average about ₹7–7.9 lakh per year [14] "
     "and Unity developers about ₹4.6 lakh [15]; the model budgets above median to hire people who "
     "can ship. The uncomfortable truth is that the business is not profitable in year one in any "
     "scenario; break-even arrives in year three in the base case.")

# =====================================================================
# CHAPTER 9 IMPLEMENTATION ROADMAP
# =====================================================================
heading_chapter(9, "Implementation Roadmap")
subhead("1) Phase 1 – Prototype Development (0–6 months):")
bullet([("Build one station: guidance plus three check types (part present, fastener count, bin pick) on a real sub-assembly.", False, False)])
bullet([("Target ≥ 95 percent check accuracy and ≤ 300 ms per check.", False, False)])
bullet([("Author the VR trainer from the same recipe; secure Startup India seed funding or an incubator.", False, False)])
subhead("2) Phase 2 – Paid Pilot (6–12 months):")
bullet([("Install two stations at one pilot plant on a real product family, after measuring a 4-week baseline.", False, False)])
bullet([("Gather data on error reduction, onboarding time, cycle-time overhead and uptime against agreed KPIs.", False, False)])
bullet([("Convert the pilot to an annual contract and publish a case study with permission.", False, False)])
subhead("3) Phase 3 – Product and Scale-Up (12–24 months):")
bullet([("Release v1.0 with self-service Recipe Studio, dashboard and MES export, plus multilingual voice.", False, False)])
bullet([("Add torque-tool and scanner integrations; win the second and third customers; build an integrator channel.", False, False)])
subhead("4) Phase 4 – Cobot Bridge and Expansion (24–36 months):")
bullet([("Ship the Cobot Bridge (robot-intent overlay and hand-over) with one cobot brand, after FTO clearance.", False, False)])
bullet([("Reach the break-even customer count; begin indigenous Indian patent filings; explore Southeast Asia and the Middle East.", False, False)])

# =====================================================================
# CHAPTER 10 CONCLUSION
# =====================================================================
heading_chapter(10, "Conclusion")
para("AR/VR and AI-guided manual assembly is a real, patented and actively enforced field, spanning "
     "projected guidance, AR glasses with verification, machine-learning step recognition, VR assembly "
     "training and AR cobot interaction, from a 2005 priority to a 2026 grant. The market gap is not AR "
     "for assembly, which already exists, but an affordable, headset-free, check-every-step system for "
     "Indian suppliers that reuses one process recipe for training, guidance and future cobot work. "
     "StepSure is a realistic way to test that gap: one paid pilot, per-station pricing, India first. "
     "The two decisive unknowns are the customers' willingness to pay and real-line computer-vision "
     "accuracy, both testable within six months for under ₹50 lakh. Before any build or sale, a "
     "professional freedom-to-operate opinion is necessary, at minimum on the step-recognition patent "
     "family [3] and the LightGuide continuation family, including a check for Indian family members. "
     "Handled with that discipline, the concept can improve the quality and competitiveness of Indian "
     "manual assembly while contributing to the nation's Industry 4.0 goals.")

# =====================================================================
# REFERENCES
# =====================================================================
doc.add_page_break()
para("References", align=WD_ALIGN_PARAGRAPH.LEFT, size=16, bold=True, space_before=12, space_after=12)
refs = [
    "US Patent 7,515,981 B2, “Light guided assembly system,” granted 2009. "
    "https://patents.google.com/patent/US7515981B2/en",
    "US Patent 10,366,521 B1, “Augmented reality assembly assistance and monitoring,” Amazon "
    "Technologies Inc., 2019. https://patents.google.com/patent/US10366521B1/en",
    "US Patent 11,715,300 B1, “Systems and methods for providing product assembly step recognition "
    "using augmented reality,” 2023. https://patents.google.com/patent/US11715300B1/en",
    "US Patent 12,592,164 B2, “Virtual reality training simulator,” Permco Inc., 2026. "
    "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12592164",
    "US Patent 11,529,737 B2, “System and method for using virtual/augmented reality for interaction "
    "with collaborative robots in manufacturing or industrial environment,” Raytheon Co., 2022. "
    "https://patents.google.com/patent/US11529737",
    "ACMA, “Industry Performance Review FY2024-25,” 2025. "
    "https://acma.in/uploads/press-release/Press%20Release%20FY25.pdf",
    "Government of India, Economic Survey (electronics production FY25), as reported, 2025.",
    "Microsoft, “Dynamics 365 Guides and Remote Assist retirement (after 31 December 2026),” "
    "Microsoft Learn, 2025. "
    "https://learn.microsoft.com/en-us/dynamics365/mixed-reality/guides/admin-apps-solution-compatibility",
    "A. Tang, C. Owen, F. Biocca, W. Mou, “Comparative effectiveness of augmented reality in object "
    "assembly,” Proc. CHI 2003, pp. 73-80.",
    "ManpowerGroup, “2025 Global Talent Shortage Survey (India),” 2025.",
    "Autocar Professional, “India’s auto component industry runs into a deeper talent "
    "problem,” 2025.",
    "Government of India, DPIIT, “Startup India Seed Fund Scheme (SISFS),” 2021. "
    "https://www.indiascienceandtechnology.gov.in/funding-opportunities/startups/startup-india-seed-fund-scheme-sisfs",
    "AutoVRse, company and client information, 2025. "
    "https://evreporter.com/autovrse-raises-2-4-million-to-expand-ai-and-vr-training-for-automotive-manufacturing/",
    "AmbitionBox / Payscale, “Computer Vision Engineer salary, India,” 2025-26.",
    "Glassdoor, “Unity Developer salary, India,” 2026.",
]
for i, r in enumerate(refs, 1):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    run = p.add_run(f"[{i}] {r}")
    set_font(run, size=11)

page_number_footer()
doc.save(OUT)
print("saved", OUT)

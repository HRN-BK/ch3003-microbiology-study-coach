# CH3003 Microbiology — Final Exam Study Coach: PLAN.md

Version 1.0, written 2026-09-25. Default exam date **2026-10-23** (editable in the app). Study window: 28 days, Day 1 = Fri 2026-09-25.
Student: HCMUT, lectures in English, native Vietnamese. Goal: the highest possible score on the final exam. Budget: about 150 min/day (90/120/150/180 selectable).
What the student does: press **"Học hôm nay"**. The app decides the rest. A **"Bài học"** library also lets the student read any detailed lesson at any time.

This file is the spec for the content (authored as Python modules in `content/*.py` using the helpers in `content/_lib.py`) and the app (`app.html` → `index.html` via `build.py`; `python3 build.py --json` also writes `data/db.json` for inspection). Built as a sibling of the CH3437 Cell Biology coach (`05_CH3437_Cell_Biology/.../study-coach`), reusing its engine.

---

## 0. Exam facts and scope

From `DCMH.CH3003_Microbiology (Lab)_July-19_2026.pdf` (HK261):
- Final exam: **multiple choice (MCQ) only, 70 minutes, 65 %** of the grade. Midterm 0 %. Labs 25 % and the major assignment 10 % are graded separately and are **out of scope**.
- The syllabus does not state the number of questions. Mocks use **50 questions / 70 minutes** (an assumption, stated in the app).

Sources, all in `03_CH3003_Microbiology/`:

| Week | Chapter (syllabus) | Source file | Family |
|---|---|---|---|
| 1 | Ch.1 History of microbiology | `1.History of Microbiology.pptx` | HIS |
| 2–3 | Ch.2 Bacteria (morphology, structures, classification, reproduction, archaea) | `2-3.Bacteria.pptx` | BAC |
| 4–5 | Ch.3 Fungi: yeasts and molds | `7. Yeasts.pptx`, `8. Molds.pptx` | FUN |
| 6 | Ch.4 Control of microbial growth | `4.The Control of Microbial Growth.pptx` | CTL |
| 7–8 | Ch.5 Microbial growth and development | `5.Microbial Growth.pptx`, `6.The Growth of Bacterial Cultures.pptx` | GRO |
| 9–10 | Ch.6 Protists | `9-10.Protists.pptx` | PRO |
| 11 | Ch.7 Viruses, viroids, prions | `11.Viruses_Viroids_Prions.pptx` | VIR |
| 12 | Ch.8 Identification of microorganisms | `12.Identification of Microorganisms.pptx` | IDT |
| 13–15 | Ch.9 Applications: SCP, ethanol, penicillin | `Microbiology_Week-13/14/15_*` | APP |

Note: slide-file numbering differs from syllabus week order in weeks 4–8 (the file "4.Control" is taught in week 6). The app follows the syllabus order.

Many slides are figure-only (Tortora *Microbiology: An Introduction* for Ch.1–5, 7, 8; Campbell *Biology* for protists). Facts behind those figures come from the standard textbook figure and are tagged **[fig]** in lessons. Background facts that are not on slides but help understanding are tagged **[mở rộng]** and are never the tested point of a mock question. The reviewed Microbiology lessons in `study-hub copy/src/data/microbiology/` are used as a cross-check.

---

## 1. Knowledge units (45)

Each unit = 15–30 minutes. Priority **P** (H/M/L), difficulty **D** (1 recall, 2 concept, 3 calculation/multi-step).

| ID | Title | P | D | Min |
|---|---|---|---|---|
| HIS-01 | Microbial world; Hooke & Leeuwenhoek | M | 1 | 15 |
| HIS-02 | Spontaneous generation vs biogenesis | H | 2 | 20 |
| HIS-03 | Golden Age: fermentation, pasteurization, germ theory, Koch's postulates | H | 2 | 25 |
| HIS-04 | Vaccines and chemotherapy: Jenner, Pasteur, Ehrlich, Fleming | M | 1 | 15 |
| BAC-01 | Size, shape and arrangement of bacteria | H | 1 | 20 |
| BAC-02 | Glycocalyx, flagella/archaella, axial filaments, fimbriae & pili | H | 2 | 25 |
| BAC-03 | Peptidoglycan and the Gram-positive wall | H | 2 | 25 |
| BAC-04 | Gram-negative wall, LPS, Gram stain mechanism, atypical walls | H | 2 | 25 |
| BAC-05 | Plasma membrane and transport | H | 2 | 25 |
| BAC-06 | Cytoplasm, nucleoid, plasmids, ribosomes, inclusions, endospores | H | 2 | 25 |
| BAC-07 | Reproduction and classification of bacteria | M | 2 | 20 |
| BAC-08 | Archaea | M | 2 | 15 |
| FUN-01 | Yeast cell structure (*S. cerevisiae*) | H | 2 | 25 |
| FUN-02 | Yeast metabolism and reproduction | H | 2 | 25 |
| FUN-03 | Yeast vs bacteria; yeast classification and counting | H | 2 | 20 |
| FUN-04 | Mold structure: hyphae, septa, mycelium | H | 1 | 20 |
| FUN-05 | Mold spores, sexual cycle and phyla | H | 2 | 25 |
| FUN-06 | Lichens; comparing molds, yeasts and bacteria; mold biomass | M | 2 | 15 |
| CTL-01 | Sterilization vs disinfection; death rate; D-value; efficacy factors | H | 3 | 25 |
| CTL-02 | Heat: moist heat, autoclave, pasteurization, dry heat | H | 2 | 25 |
| CTL-03 | Filtration, cold, desiccation, osmotic pressure, radiation | H | 2 | 20 |
| CTL-04 | Chemical agents I: phenolics, chlorhexidine, oils, halogens, alcohols, heavy metals | H | 2 | 25 |
| CTL-05 | Chemical agents II: surfactants, preservatives, food antibiotics, aldehydes, peroxygens; culture preservation | H | 2 | 25 |
| GRO-01 | Physical requirements: temperature, pH, osmotic pressure | H | 2 | 20 |
| GRO-02 | Chemical requirements: C, N, S, P, trace elements, growth factors | H | 2 | 20 |
| GRO-03 | Oxygen classes and toxic forms of oxygen | H | 2 | 20 |
| GRO-04 | Culture media and pure cultures | H | 2 | 25 |
| GRO-05 | Binary fission, generation time, growth curve | H | 3 | 30 |
| GRO-06 | Direct counts: counting chambers, plate count, dilutions, filtration, MPN | H | 3 | 30 |
| GRO-07 | Indirect methods: turbidity/OD, dry weight, metabolic activity; batch growth curve | H | 3 | 20 |
| PRO-01 | Protist overview: supergroups, nutrition, reproduction; fungi–algae–protozoa | H | 1 | 20 |
| PRO-02 | Excavata: diplomonads, parabasalids, euglenozoans | H | 2 | 25 |
| PRO-03 | Stramenopiles: diatoms, brown algae, oomycetes | M | 2 | 20 |
| PRO-04 | Alveolates and Rhizaria: dinoflagellates, apicomplexans, ciliates, forams | H | 2 | 25 |
| PRO-05 | Archaeplastida (red, green algae) and slime molds | M | 2 | 20 |
| VIR-01 | Virus basics, host range, size, classification and naming | H | 1 | 20 |
| VIR-02 | Virion structure and morphology | H | 2 | 20 |
| VIR-03 | Multiplication: phages (lytic, lysogenic) and animal viruses (HIV) | H | 2 | 30 |
| VIR-04 | Viroids, virusoids and prions | H | 1 | 15 |
| IDT-01 | Phenotypic identification: Bergey's, biochemical tests, keys | H | 2 | 25 |
| IDT-02 | Molecular identification: 16S rDNA, PCR, sequencing, BLAST, trees | H | 2 | 25 |
| APP-01 | Industrial fermentation; primary vs secondary metabolites | M | 2 | 20 |
| APP-02 | Single-cell protein (SCP) | H | 2 | 25 |
| APP-03 | Ethanol production | H | 3 | 25 |
| APP-04 | Penicillin production | H | 2 | 25 |

Unit content fields (`units[]`):
- `hookVi` — a real-world opening situation in Vietnamese with English terms; followed by an ungraded `predictQuestion`.
- `lesson[]` — **detailed lesson**: 4–8 sections `{h, body}`; body is light Markdown (paragraphs, `- ` bullets, `| table |`, `**bold**`). Vietnamese explanation, English terms in bold, fully covering the slide content of the unit.
- `extension[]` — **"Mở rộng & thực tế"**: 2–4 sections linking to real life, industry, medicine, food, lab practice or other courses.
- `keyCards[]` — 3–6 short English cards `{title, bodyEn, glossVi}` for fast recall inside sessions.
- `traps[]` — misconceptions; each has at least 1 MCQ with `trap` set.
- `source` — deck and slide numbers.

---

## 2. Question bank

- Total ≈ 400 MCQs: **learn pool** ≈ 250 (5–7 per unit) and **mock pool 150** (3 disjoint mocks × 50).
- Mock blueprint (50 Q / 70 min): HIS 4 · BAC 8 · FUN 7 · CTL 6 · GRO 8 · PRO 5 · VIR 5 · IDT 3 · APP 4. Each mock has at least 4 `calc` and at least 5 `not` items.
- Types: `recall`, `concept`, `application`, `calc`, `data`, `not`. Stem in English (≤ 60 words; ≤ 110 for `data`); exactly 4 options; no "all/none of the above"; answer index balanced.
- `explanation` and `distractorNotes` in Vietnamese with English terms; explanation says why the key is right and why the most tempting distractor is wrong. `calc` items carry `steps`.
- Schema (same as CH3437): `{id:"Q-<unit>-<nnn>", unit, type, difficulty, stem, options[4], answer, explanation, vocab[], pool:"learn|mock", source, trap, distractorNotes[4], steps[]}`.

## 3. Worked examples (≈ 18)

Fade levels 0–3 as in CH3437. Topics: generation time (3), serial dilution and CFU (3), counting chamber (2), MPN reading, OD and %T, D-value and thermal death (2), dilution design, growth-curve phases from data, ethanol theoretical and practical yield (2), SCP biomass yield / C:N, penicillin fed-batch yield. Every number recomputed by `build.py` checks or by hand.

## 4. Vocabulary and flashcards

- ≈ 250 terms `{term, vi, def, example, unit, aliases[]}`; the app generates EN→VI and VI→EN cards.
- 4–6 `fact | number | trap` flashcards per unit.

## 5. 28-day plan (recomputed on every press, adaptation rule of CH3437 §4.3, single track)

- `D` = study days left. Reserve `M = clamp(round(D/3), 2, 7)` final days: mock → drill/repair → mock → marathon → mock → light → final sheet.
- Learning days `L = D − M`; new units/day = `ceil(remaining / L)` (≈ 2–3), load cap 100 min with express mode for P:L/M units.
- Daily learning session: spaced review (≤ 35) → new units (hook → lesson → key cards → 5 MCQs) → break → calculation drill (worked examples + calc MCQs) → mixed practice (≈ 9, weighted by weakness, no two in a row from the same family) → vocabulary.
- Leitner 1/3/7/14 days, capped at exam − 1. Wrong answers re-queued 3–6 items later.

## 6. App

- Single offline `index.html` (vanilla JS, inline CSS), built by `build.py` from `app.html` + `content/*.py` with validation (unique IDs, 4 distinct options, answer 0–3, unit exists, vocab tags resolve, WE step answers numeric; mock pool ≥ 150 split into 3 sets so that every set satisfies the blueprint per family, has ≥ 4 calc and ≥ 5 NOT items).
- Screens: Home ("Học hôm nay", days left, today's plan, stats), Session, Mock (timer 70 min, flag, grid, no feedback until submit, results by family + repair), Progress heat map (45 units in 9 families), **Bài học** library (all lessons + extensions, readable any time; locked-free), Formula sheet, Settings (exam date, minutes, export/import, reset, "Thi thử ngay").
- Vietnamese UI, English content, vocab tooltips (off during mocks), light/dark theme, mobile-first, 44 px targets.
- Storage key `ch3003.coach.v1`.

## 7. Verification

- `python3 build.py` passes all checks.
- Recompute every calc item and worked example (`work/check_calc.py`).
- Browser test: Day 1 session, a missed-day resume (dev shift), Mock 1, lesson library, mobile width 390 px, dark mode.

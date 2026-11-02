---
name: paper-voice
description: "Write or rewrite manuscript prose in the SW-refresh register (modelled on Burgoyne & Nielsen 2027, Fluid Phase Equilib. 612, 114824): many short numbered sections with one idea each, short declarative sentences, plain verbs, lists only for real enumerations, a closing number on every results section, and no signs of AI writing. Use for ALL drafting, rewriting, abstracts, captions and response-to-reviewer text in this project, and always run checks/voice_check.py before showing prose."
---

# paper-voice (SW-refresh register)

## Project slots (filled at setup, see SETUP.md)

Read this block first. Every example in the rest of this file (gases, models, sources, table and figure numbers,
numbers) comes from the earlier paper that this register was measured on. Examples show sentence shapes only.

- Field and the paper's question: reservoir simulation surrogates (graph neural networks, an extended MeshGraphNet), evaluated on the Egg and Norne models against OPM Flow; data section after the model section (DEFAULT, owner to confirm)
- Target journal and its author guidelines: Artificial Intelligence in Geosciences (KeAi), as in `06_journal_paper/REVISION_2026-10-27_final/final_for_supervisor_v4/main.tex`; the HBKU thesis in `06_thesis/latex`; author guidelines not recorded in the repo (OPEN)
- Anchor papers for the register: the owner's final Egg journal paper v4 (`06_journal_paper/REVISION_2026-10-27_final/final_for_supervisor_v4/`) (DEFAULT, owner to confirm)
- English variety (replaces "follow the target journal" in S9): American, as used in the final Egg journal paper (DEFAULT, owner to confirm)
- Use "Recommendation:" closing lines: no (DEFAULT, owner to confirm)
- Abstract policy (counts only, or numbers allowed): numbers allowed, final numbers only, as in the final Egg journal paper abstract (DEFAULT, owner to confirm)
- Where the older rules live: `RULES.md` Part A holds the older default rules (R1 to R14, bans 1 to 13, checks C1
  to C8) that this file calls "paper-voice". `RULES.md` Part B holds the author's rulings on the style clashes of
  Part 9 (S1 to S19). Those rulings win over Part 9. `checks/voice_check.py` runs the mechanical checks of Part 8.

The register of one paper: Burgoyne, M. & Nielsen, M.H. (2027), "Refreshed Søreide–Whitson
framework for gas solubility in water and brine with extension to hydrogen", Fluid Phase
Equilibria 612, 114824 (17 pages; the earlier project kept a local copy,
which this project does not have). The author
asked for it (2026-10-04, for an earlier paper) for its sentences, its bullet points, and its habit of breaking the
paper into very small sections that each carry one idea.

This skill controls style only. Where it conflicts with paper-voice or with a project ruling,
see Part 9. The content-honesty rulings (paper-voice R14, bans #12 and #13) still apply until
the author rules otherwise.

Working order: plan the section tree first (Part 1). Draft against rules A1-A6, S1-S9, L1-L6
and P1-P4. Write each section type to its template (Part 5). Then run checks K1-K13 (Part 8).
Nothing ships until every check passes.

Quote convention: «...» (SWR p. N) marks words quoted from the paper, with its PDF page. Every
other example is constructed. In constructed examples, numbers are written as placeholders
(`<n>`, `<x>%`) so they cannot leak into a draft as facts.

How the numbers were measured is set out in Part 10. "Body" means the running prose and list
items from the Introduction to the end of the Appendix. It excludes the abstract, tables,
captions, equations, nomenclature, references and back matter: 6,351 words, 261 prose
sentences, 21 list items.

---

## Part 1 - Document architecture

**Measured.** 52 numbered headings over 6,351 body words, so **one heading per ~122 words**.
- Depth: 9 first-level, 39 second-level and 4 third-level headings (third level only under 2.2).
- 47 leaf sections carry prose. Words per leaf section: median 96, mean 135, p25 59, p75 167,
  range 7-558. 25 of 47 are 100 words or less; 39 of 47 are 200 words or less; 3 exceed 400.
- Paragraphs per leaf section: median 2, mean 2.3, range 1-8.
- Five first-level parents (2, 4, 5, 6, 7) carry no prose before their first child. The
  heading leads straight into x.1.
- Heading length: mean 3.0 words, median 3, maximum 8. Headings are noun phrases with no
  verb and no claim.

**A1. One idea per section.** Each leaf section answers one question about one object: one
gas, one model component, one comparison, or one limitation family. In the paper, 4.2-4.8 cover
one gas each, 5.2-5.7 one gas each, and 2.2.1-2.2.4 one aspect of the water alpha function
each (formulation, deficiencies, investigation, brine term). Two gases share a section only
when they get identical treatment («4.7. C2H6 and C3H8 BIP correlations», SWR p. 4).

**A2. Split by object first, then by question.** The paper splits results by object (gas) and
then by model part (aqueous BIP, non-aqueous BIP, salting-out, embedded salinity). A section
that would cover "CO2 and H2S salting-out" becomes two sections.

**A3. Small is normal.** A leaf section of one to three sentences is legitimate. Examples: 2.2.4
(27 words), 5.8 (7 words, a pointer to Table 6) and 7.2 (12 words, a pointer to Table 8). Do
not pad a section to make it look substantial.

**A4. A long section is held together by run-in heads.** The three sections over 400 words (4.10,
7.1, 7.7) stay one-idea at the paragraph level. 4.10 and 7.1 use italic run-in paragraph heads
(«Scatter in pointwise kNA_ij.», «Volatility trend.», «K-value initialisation.»). 7.7 gives each
limitation its own paragraph. A section passing ~250 words needs run-in heads or one paragraph
per sub-point.

**A5. Heading phrasing.**
- Use a bare noun phrase: «Dual-flash scheme», «Deficiencies», «Limitations».
- Per-object headings follow one pattern: «CO2 BIP correlation», «H2S salting-out».
- Results chapters carry a typed prefix: «4. Results: Freshwater BIP correlations».
- A side test gets an «Investigation:» prefix: «2.2.3. Investigation: Effect of alpha function
  on solubility».
- A summary section is titled «Summary of ...».
- A heading never states a finding. Write "H2 salting-out", not "H2 salting-out follows the
  boiling-point correlation".

**A6. Skeleton.** Introduction (short) → Theoretical background (each model component its own
section) → Methodology → several typed Results chapters → Discussion (implementation,
comparisons, consistency, limitations, validity) → Conclusions (numbered list) → Appendix.
There is no literature-review chapter. Prior work enters only where a component is described.

---

## Part 2 - Sentence level

**Measured on 261 prose sentences.**
- Length: mean 23.0 words, median 21, sd 12.7, p10 9, p25 14, p75 29, p90 39, maximum 87.
- Length bands: 21% are 12 words or less, 44% are 13-25, 21% are 26-35, and 13% exceed 35.
- By part:

  | Part | Mean words | Median words |
  |---|---|---|
  | Abstract | 27.3 | 28 |
  | Background | 21.8 | 22.5 |
  | Methodology | 25.1 | 21 |
  | Results | 22.0 | 20 |
  | Discussion | 23.8 | 22 |

- Every sentence over 60 words is an inline enumeration: (i)/(ii)/(iii), (1)/(2)/(3), or a
  colon followed by a run of source exclusions.

**S1. Short and declarative.** Target mean 20-23 words. A plain subject-verb-object
sentence is the default. One sentence in five should be 12 words or less. The short ones do
real work: «A simple linear correlation suffices:» (SWR p. 4). «This is retained in the present
work.» (SWR p. 2).

**S2. Long only for an inline enumeration.** Over 35 words is allowed only when the sentence
lists parallel items after a colon. Use (i)/(ii)/(iii) for criteria or bases, and (1)/(2)/(3)
for comparators. If the items are 3 or more and each runs past ~12 words, use a list instead
(Part 3).

**S3. Openers.**
- Start with the subject. «The» opens 28% of sentences.
- A scoping «For X, ...» opens 11%: «For hydrogen at 25 °C, ...», «For CO2, ...».
- A figure or table opens 7%: «Fig. 3c shows N2 Sechenov coefficients.»
- «This/These» opens 8%, pointing back to the previous sentence's object.
- «We» opens only 3 of 261 sentences.
- Connector openers are rare: 15 in 261 sentences, about 6%. «However» opens one sentence and
  «Therefore» opens none.
- Transitions are carried by headings and run-in heads, not by connective words.

**S4. Voice.**
- The agent is mostly impersonal. «This work» appears 18 times; «we» appears 8 times and «our»
  3 times in 6,351 words.
- «We» is kept for a decision or an action: «we fitted», «we adopt», «we retain», «we replace»,
  «We found no experimental measurements ...».
- Passive voice appears in 23% of sentences, for procedure and for what was retained or
  excluded: «Three data sources are excluded», «Coefficients were fitted by ...».

**S5. Tense.**
- The present tense is the default everywhere. It covers what a model does, what a figure
  shows and what the paper presents: «Fig. 1e shows», «This achieves MAE = ...», «This work
  presents».
- Use the past tense for actions taken («we regressed», «were evaluated», «were excluded») and
  for history («S&W fitted the salinity coefficients to ...»).
- The Conclusions are written in the present tense.

**S6. Hedging is sparse and bounded.**
- Measured: «approximately» 6, «may» 5, «expected» 3, «slightly» 2, «typically» 2,
  «largely/roughly/appears/could» 1 each. That is about 3.5 hedges per 1,000 words.
- These words appear zero times: «somewhat», «relatively», «likely», «probably», «suggest»,
  «possibly».
- A hedge is tied to a condition: «Accuracy is expected to degrade outside these ranges» or
  «may exhibit a positive bias due to censoring effects».

**S7. Numbers in sentences.**
- 49% of sentences carry at least one number. The mean is 1.6 numbers per sentence and p90 is 5.
- Metric equalities stay inline: «MAE = 0.0089» (19 times).
- The sample size goes in parentheses: «(611 freshwater points)», «(n = 109)».
- Ranges use an en dash with the unit once: «273–473 K», «10%–17%».
- Ratios use «2×». Approximate values use «≈» or «∼».
- A comparison carries its comparator in the same sentence: «compared to MAE = 0.017 for the
  original S&W correlation».
- Units appear on every dimensional value. Temperatures in prose are in °C; critical
  temperatures are in K.

**S8. Punctuation.**
- Em-dashes in prose: zero.
- 69 colons, used for: equation lead-ins (27 of 28 equations), list lead-ins, «Recommendation:»
  labels, and one-clause elaboration («... are then independent: updating one does not require
  re-fitting the other.», SWR p. 3).
- Semicolons appear in 14% of sentences, joining two closely linked clauses.
- There are 0.92 parenthesis groups per sentence. They hold numbers, sample sizes, conditions,
  citations and equation numbers, not asides.

**S9. Plain verbs, fixed nouns.** Use the same noun for the same thing throughout: «pointwise-
regressed», «embedded», «drop-in compatible». Verbs are plain: shows, achieves, retains,
reproduces, excludes, suffices. Boosters are absent: «novel», «significantly», «notably»,
«importantly» and «clearly» each appear zero times. «Robust» appears once, in the technical
sense of L1 regression versus outliers. The paper uses British spelling (vapour, behaviour,
parameterised, whilst); follow the target journal.

---

## Part 3 - Bullet and numbered lists

**Measured.** There are 6 lists with 21 items, and they hold 8% of body words. Items run 2-5 per
list. Words per item: median 16, mean 26, range 8-84.

| Where | Kind | Items | Item grammar | End punctuation |
|---|---|---|---|---|
| 1 Introduction (motivations) | numbered | 3 | label + full sentences | period |
| 2.4 Dual-flash scheme | numbered | 2 | label + colon + full sentences | period |
| 3.2 Our approach | numbered | 3 | imperative steps | period |
| 4.1 Functional forms | bullets | 5 | label + colon + subjectless verb phrase | period |
| 7.6 Limitations | bullets | 4 | noun-phrase fragments | none |
| 8 Conclusions | numbered | 4 | label + colon + 1-2 full sentences | period |

**L1. When to use a list.** Use one when the content is 2-5 parallel items of the same kind:
- motivations;
- steps of a procedure;
- one choice per gas;
- limitations;
- contributions.

Use prose when the items depend on each other or need numbers compared across them.

**L2. Numbered or bulleted.** Number a list when order or count matters: steps, the
two-flash scheme, contributions, motivations. Use bullets for an unordered catalogue: forms per
gas, limitations.

**L3. Lead-in.** Every list follows a lead-in that ends with a colon. The lead-in may be a full
sentence («Three decades of accumulated experimental data and evolving application
requirements motivate a reassessment of the S&W framework:», SWR p. 1). It may also be a bare
phrase: «Our approach:», «Key limitations of this work include:» (SWR p. 3, p. 13). The
Conclusions list follows a full summary sentence instead of a colon lead-in.

**L4. Labelled items.** Long items open with a short label (2-4 words) and then a colon or
period: «Hydrogen support.» or «Drop-in BIP updates:». After the label come complete sentences,
and each item carries at least one number where one exists. Short items may be fragments:
«Linear in Tr (N2): adequate for the near-linear behaviour observed.» (SWR p. 4).

**L5. Parallel grammar.** All items in one list share one grammar: all imperatives, all
label + sentence, or all noun phrases. Do not mix kinds within a list.

**L6. Punctuation.** Items that are sentences, or that carry a verb phrase, end with a period.
Pure noun-phrase items, as in the Limitations list, take no terminal period. Keep one
convention per list.

---

## Part 4 - Paragraphs

**Measured.** There are 108 prose paragraphs. Sentences per paragraph: mean 2.4, median 2, p90 4,
maximum 7. 36 paragraphs (33%) are a single sentence. 21 of 111 paragraphs, and 16 of 47
leaf sections, open with «Fig. N ...» or «Table N ...».

**P1. Two or three sentences.** A paragraph is a claim and its support. A paragraph of five or
more sentences is rare (p90 = 4). Split it, or give it a run-in head.

**P2. The topic sentence is first and is often a pointer.** The first sentence names the object
or the figure: «Fig. 3b compares experimental H2S Sechenov coefficients against model
predictions.» The next paragraph delivers the numbers. A one-sentence pointer paragraph is
normal in this register (see the conflict note in Part 9).

**P3. One-sentence paragraphs carry decisions.** A retention, an exclusion or a scope statement
stands alone: «This is retained in the present work.» Most «Recommendation: ...» lines close a
Results subsection as a separate paragraph; in 5.4, 5.5 and 5.7 the line closes the last
paragraph instead.

**P4. Transitions come from structure.** Paragraphs do not open with "Furthermore", "Moreover"
or "In addition". The next idea starts a new paragraph, a run-in head, or a new section.

---

## Part 5 - How each part is written

**Introduction (244 words: 2 short paragraphs and a 3-item numbered list).**
1. Say what the framework is and where it is used.
2. Say that updates since have been piecemeal, in one sentence.
3. Give the motivations as a labelled numbered list.

Use no roadmap paragraph ("Section 2 describes ...") and no long literature survey. The
Introduction has four citations.

**Theoretical background.**
- Each model component gets its own subsection.
- The pattern is: purpose sentence, then equation, then «where ...» gloss, then one or two
  sentences on what the form implies.
- Deficiencies of the inherited model go in their own subsection, stated with a number:
  «MARE of 1.18% over 10–340 °C».
- An alternative that was tested and rejected gets its own «Investigation:» subsection, with
  the result and the decision to retain the original.

**Equations (28 numbered).**
- 27 of 28 are introduced by a sentence ending in a colon: «The proposed correlation is:»,
  «For N2:».
- 20 are followed directly by a «where ...» gloss. The other 8 reuse symbols already defined.
- The gloss gives parameter values inline: «where Tr = T/Tc with Tc = 304.20 K».
- No equation is derived in the body.

**Methods.**
- Start with the global scope bound, with a one-line reason: «restricted to temperatures at
  or below 200 °C (473 K)».
- Then the exclusions, each with a parenthesised reason.
- Then one subsection per step: pointwise regression, deconvolution, correlation fitting,
  data sources.
- Define each error metric once, as a numbered equation.
- When more than one sample basis exists, state each basis once as an (i)/(ii)/(iii)
  enumeration.

**Per-object result, model fit (template from 4.2-4.8; 25-75 words).**
1. The figure pointer: «Fig. 1c shows the N2 results.»
2. A one-clause reason for the form, ending in a colon.
3. The equation, then the «where» gloss with Tc.
4. The score sentence: «This achieves MAE = <x> over <n> points, compared to MAE = <y> for the
   original correlation.»

Constructed: "Fig. <k> shows the CH4 results. A rational form is required: [Eq.] where Tr = T/Tc.
This achieves AAD = <x>% over <n> points."

**Per-object result, model choice (template from 5.2-5.7).**
1. The figure pointer.
2. What the original framework did for this gas.
3. How far the default misses, with magnitude and metric (2×, MAE).
4. Which published model agrees best, with its metric.
5. The calibrated adjustment, with before-to-after numbers.
6. A closing «Recommendation: Use <model> with <adjustment> for <system> in <range>.»

Constructed: "Recommendation: Use the boiling-point correlation for H2 between <T1> and <T2> °C."

**Comparisons with another model (7.3).**
1. One sentence on what the other model is and why it is a fair reference.
2. All three scores on the same rows in one sentence: «Spycher & Pruess achieves MARE = 13.0%
   versus 16.4% for this work and 23.0% for the original S&W» (SWR p. 12).
3. A breakdown by condition, with paired numbers in parentheses.
4. One sentence on the cause.
5. A one-sentence trade-off verdict: «The S&W framework trades some CO2 accuracy for the
   ability to treat eight gases with a consistent methodology and a single flash routine.»
   (SWR p. 12).

**Limitations (7.6 and 7.7).** First, a short bullet list of noun-phrase limitations with no
periods. Then a separate «Validity ranges and error analysis» section. That section gives:
- the validated ranges in one sentence;
- each structural limitation in its own paragraph, with its mechanism;
- the size of the limitation, as a number;
- one flat closing sentence: «This limitation is negligible for sparingly soluble gases.»
  (SWR p. 13).

A use boundary is stated as a rule about the model: «are not validated for such conditions».

**Conclusions (268 words).**
1. One summary sentence (28 words) naming the scope and the data basis.
2. A numbered list of 4 labelled contributions, 48-53 words each, each with its key number.
3. One closing sentence (37 words) giving the compatibility and the before-to-after numbers.

Use no future-work paragraph and no restated motivation.

---

## Part 6 - Abstract, highlights, captions, tables

**Abstract (191 words, 7 sentences, mean 27.3 words, 3 paragraphs).**
- P1 (3 sentences) gives the context and the gap, what is presented (gas count, data
  basis), and compatibility.
- P2 (3 sentences) gives the method in one sentence, what that design buys, and the main side
  finding, joined by a colon.
- P3 (1 sentence) gives the extension and the first-time addition.

The abstract carries no accuracy percentages. Its only numbers are counts and a year
(«eight gases», «approximately 2000», «1992»). Seven keywords follow.

**Highlights.** The paper as distributed in this PDF has no Highlights section; that was
checked by reading all 17 pages. If a journal requires highlights, write 3-5 items in the
Conclusions-list grammar: a label, then one clause with one number, each item at most 85
characters. That rule is constructed, not measured.

**Figure captions (6 captions: mean 59 words, range 45-90).**
- Open with a title fragment, for example «Solubility parity plots for CO2, H2S, and N2.»
- Then a key in "Symbol: meaning." form: «Grey symbols: ... Black dashed lines: ... Green
  solid lines: ...».
- Then one sentence on anything unusual: an omitted gas, an excluded source, the meaning of
  shaded bands.
- The metric is shown in the legend, not restated in the caption.

**Table captions (10 captions: mean 28.5 words, range 6-57).**
- Open with a title fragment.
- Then one or two sentences define the column basis («MAE(kij) is evaluated against
  pointwise-regressed values; MARE(%) is evaluated on predicted solubility»).
- Lettered footnotes (a, b, c, d) carry exceptions and exclusions.
- Tables carry the full coefficient sets, ranges and comparisons. The prose quotes only the
  one number that matters and points to the table.
- A «Status» column (Retained / Updated) records decisions inside the table.

---

## Part 7 - DO / DON'T

DO
- Give every distinct object or question its own numbered section, with a 1-5 word noun-phrase
  heading.
- Open a results subsection with the figure that shows it.
- End every per-object result with its score sentence or a «Recommendation:» line.
- Use a colon lead-in before every list and every display equation.
- Gloss every equation with «where ...», giving the parameter values inline.
- Put the comparator in the same sentence as the number, with the point count in parentheses.
- State retentions and exclusions as one flat sentence each, with the reason in parentheses.
- Use labelled numbered items for contributions, motivations and the Conclusions.
- Put long material in tables, with lettered footnotes, and quote one number in prose.
- Let structure carry the transitions: new section, new paragraph, run-in head.

DON'T
- Combine two objects or two questions in one section; split them.
- Write a paragraph of five or more sentences without a run-in head.
- Exceed 35 words except in an inline (i)/(ii)/(iii) enumeration.
- Open sentences with connectors such as Furthermore, Moreover or Additionally (6% at most).
- Use vague hedges (somewhat, relatively, likely, probably, suggest) or boosters (novel,
  significant, notably, clearly).
- Use em-dashes or parenthetical asides; parentheses hold data, conditions and citations only.
- Mix item grammars inside one list, or end some items with periods and others without.
- Write a roadmap paragraph, a literature-review chapter, or a future-work paragraph.
- Put accuracy percentages in the abstract.

---

## Part 8 - Checklist to run on a draft (any failure blocks the prose)

**K1. Heading density.** Body words divided by number of headings must be 160 or less (SWR: 122).
```
grep -cE '^#{1,4} ' FILE ; wc -w FILE
```
**K2. One idea per section.** Write each leaf section's idea as one noun phrase of 8 words or
fewer; that is its heading. If the phrase needs "and" between two unrelated objects, or a
paragraph's topic sentence names a different object from the heading, split the section. Two
objects with identical treatment are the only exception.

**K3. Section size.** A leaf section over 250 words must have run-in heads or one paragraph per
sub-point. A leaf section over 560 words (the paper's maximum) must be split.

**K4. Sentence length.** Mean 18-24 words, and 15% or more of sentences 12 words or less.
Every sentence over 35 words must be an inline enumeration; otherwise split it or make it a
list.
```
grep -oE '[^.!?]+[.!?]' FILE | awk '{print NF}' | sort -n | awk '{a[NR]=$1;s+=$1} END{print "n="NR, "mean="s/NR, "max="a[NR]}'
```
**K5. Paragraph size.** No paragraph over 7 sentences, and 4 or fewer as the norm.

**K6. Lists.** Each list has a colon lead-in (the Conclusions list may follow a summary
sentence), 2-5 items, one item grammar, and one end-punctuation convention. Labelled items
use "Label: sentence." or "Label. Sentence." consistently.

**K7. Equations.** Every display equation is preceded by a colon and followed by «where ...»,
or the text states that its symbols were defined at Eq. (N).

**K8. Result closure.** Every per-object results subsection contains a score sentence (metric
= value, with n) or a «Recommendation:» line.

**K9. Connectors and boosters.** Zero hits for the booster list. Connector openers stay at
6% of sentences or less.
```
grep -nE '^(Furthermore|Moreover|Additionally|In addition|Notably|Importantly|Interestingly)' FILE
grep -nEi '\b(novel|significantly|notably|importantly|clearly|somewhat|relatively|likely|probably|suggests?)\b' FILE
```
**K10. Numbers.** Every number has a unit or is a count. Every metric sits next to its
comparator and its n. Ranges use an en dash with the unit once.

**K11. Captions and tables.** Figure captions open with a title fragment and give a symbol
key. Table captions define the column basis. Exceptions go in lettered footnotes.

**K12. Project rulings still bind.** Run paper-voice checks C6 and C7 (self-reference; the
comparative-superiority family) and the R14 exposure statement on every comparison. Also check
gas naming. This register's habits trip those checks (Part 9). Where they collide, the ruling
wins unless the author has ruled for this register.

**K13. No signs of AI writing.** Run every line of the grep block in `AI-SIGNS.md` (this
folder) on the draft and read each hit. Then walk its numbered items by hand for the signs a
grep cannot see: Title Case headings, heading levels, small tables, English variety, and every
DOI resolving to the cited paper. Fix each hit as the next section says.

---

## No signs of AI writing (author rule, 2026-10-04)

Every draft and rewrite is checked against `AI-SIGNS.md` in this folder. It is a 52-item
checklist taken from the Wikipedia page "Signs of AI writing" (raw wikitext, revision
1378298730, fetched 2026-10-04), with a grep block and overlap rules. It covers word lists,
sentence patterns, formatting, citations and response-letter habits.

- A hit is fixed by rewriting the sentence so that it states the fact and its number. Never fix
  it by swapping in another listed word or a synonym; that hides the sign and keeps the empty
  sentence.
- This register uses several forms that the page lists as signs: lists, labelled items
  (L4), short headings, colon lead-ins, and the «Recommendation:» line. Follow the overlap
  rules at the end of `AI-SIGNS.md`. In short, labels are plain text and never bold; a
  «Recommendation:» line names the gas, the model and a number; headings are in sentence case.
- Where `AI-SIGNS.md` and a rule in this file disagree, the stricter one wins.

---

## Part 9 - Conflicts with paper-voice, CLAUDE.md and author memory rules (noted, not resolved)

None of the files below was changed. Each conflict is a candidate question for the author.

1. **Sentence fragments (paper-voice ban #7).** SWR uses fragments by design: list items (4.1,
   7.6), run-in heads («Volatility trend.»), «Our approach:», «For N2: [Eq.]» and
   «Recommendation:» labels.
2. **Colons (paper-voice ban #6).** SWR uses 69 colons, including colon elaborations that work
   like a reveal: «indistinguishable when the BIP is refitted: the kij absorbs upstream model
   differences» (SWR p. 1).
3. **Sentence ceiling (paper-voice R1, ~35 words).** In SWR, 13% of sentences exceed 35 words
   and the maximum is 87; all of those are inline enumerations. This skill allows that one
   exception; paper-voice does not.
4. **Figure references with no paired statistic (paper-voice R9 and C5).** SWR's standard
   opener «Fig. 1e shows the CH4 results.» has no number. The number arrives two sentences
   later.
5. **Captions that name another figure (R-MS-163 in paper-voice C5).** SWR writes «Layout as in
   Fig. A.5» (SWR p. 16).
6. **Paragraph shape (paper-voice R4).** In SWR, 33% of paragraphs are one sentence and many
   carry no closing number.
7. **Parentheses (paper-voice ban #1).** SWR has 0.92 parenthesis groups per sentence. They
   are data, not asides, but a literal reading of ban #1 flags them.
8. **Clause fusing (paper-voice R2 and R6).** In SWR, 14% of sentences join two clauses with a
   semicolon.
9. **Comparative wording (paper-voice ban #13, R14, D46).** SWR writes «agrees best», «comparable
   or better predictive accuracy», «The dedicated model's advantage», «improving acid-gas
   accuracy», «validating the simpler approach», and «statistically significant» with no
   interval stated. It quotes paired scores but no confidence interval and no campaign count
   G. Under this project's rulings those words stay banned and the interval and G stay
   required.
10. **Addressing the user (paper-voice ban #12).** «Recommendation: Use ...» (7 times) and
    «Users with specific multicomponent H2-rich gas mixtures should validate ...» (SWR p. 12)
    address the reader. «Each table caption states the basis used.» (SWR p. 4) is a statement
    about the paper's own conduct. A project-compatible form of the recommendation line
    describes the model: "The recommended model for H2 is ...".
11. **One number per sentence (author memory rule, 2026-10-01, "Paper: results only,
    simple").** SWR averages 1.6 numbers per sentence, with p90 = 5. It also tells
    before-and-after stories against the original framework («reduces the yH2O MARE from 11.7%
    to 8.6%»). Comparisons with a published original differ from the banned stories about our
    own fixes, but the number density conflicts.
12. **Gas naming (author memory rule, 2026-09-30, "Name each gas").** SWR writes «C1–nC4»,
    «C1–C4 hydrocarbons» and «heavier hydrocarbons». The project rule requires C2H6, C3H8 and
    n-C4H10 written out.
13. **Plain language (CLAUDE.md section 2, "Plain language everywhere ... Jargon and code-names
    get a plain gloss").** SWR defines each abbreviation once (BIP, MARE, PR-EOS, VLLE, UHS)
    and then uses symbols such as kAQij and Δkij(T,m) in running prose, with no further gloss.
    The CLAUDE.md rule covers chat, docs and commit bodies, while manuscript register falls to
    the paper-voice skills. So this conflict matters only if the author reads that rule as
    covering manuscript prose. The plain-gloss rule still governs any chat or doc text written
    about the manuscript.
14. **Agreements, for completeness.** Both registers ban em-dashes (SWR has none), marketing
    adjectives, vague hedges, rhetorical questions and first-person singular. Both require
    units, a «where» gloss for equations, and topic-first paragraphs.

---

## Part 10 - How the numbers were measured (reproducible)

- Text: `pdftotext -layout` (Poppler 26.02) on the local PDF, written to
  `work/tmp/voice-swr/swr-layout.txt` (scratch, untracked). The two-column layout was
  transcribed by hand into `work/tmp/voice-swr/body.txt`, one `## <number> <title>` line per
  heading.
- In `body.txt`, display equations became `[EQ]` and list items `* `. Tables, captions,
  nomenclature, references, funding and CRediT were left out, and math was flattened to plain
  tokens.
- `work/tmp/voice-swr/measure.py` and `m2.py` compute the statistics. The sentence split
  protects «Eq.», «Eqs.», «Fig.», «Figs.», «et al.» and «e.g.,» and splits on terminal
  punctuation followed by a capital, digit or symbol.
- A word is any token containing a letter or digit; `[EQ]` is not counted.
- Run-in heads are stripped before sentence counting. Passive voice is counted with a "be +
  participle" regex.
- Number counts strip chemical formulas, equation, figure, table and section numbers, and
  citation brackets.
- Caption counts come from `work/tmp/voice-swr/caps.txt`.
- Precision: sentence and passive counts depend on the regexes and are good to about ±5%.
  Heading, section, list, equation and caption counts are exact.
- The scratch files are not tracked. To reproduce, regenerate them with the same commands.

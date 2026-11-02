# RULES: the author's standing writing rules

Written by Abdulsalam Abd over many sessions on an earlier paper, generalised for any paper. In this file "I", "me" and "my" are the author speaking to you, the assistant. Quotes are his, verbatim. Where a quote names a model or a gas, it is an example from the earlier paper.

Part A holds the older default rules. Part B holds his own rulings.

## Part A. Older default rules (still apply)

The SW-refresh skill sits on top of an older default skill called paper-voice. The SW-refresh skill says: "style
only; the content-honesty rules still apply". The older rules are generalised here. Where they clash with the
SW-refresh skill, Part B (S1 to S19) says which one wins.

### 4.1 Register rules R1 to R14

- R1. Sentence length. Mean about 20 words, hard ceiling 35. After any clause-heavy sentence of 25 to 35 words, reset
  with a declarative of 10 to 14 words.
- R2. One idea per sentence. Split any sentence that carries two independent claims.
- R3. "We" for the authors' choices and actions, passive for procedure. "We adopt the constant-slope form." "The leg
  was regressed on 1,880 rows."
- R4. A paragraph is claim, then evidence, then a quantitative verdict. It closes on a number. A paragraph with no
  closing number reads as opinion.
- R5. Topic sentence first. A reader skimming first sentences must get the argument.
- R6. Connectors are set off by a comma and never fuse clauses. "However, the approach is valid." Do not write "and"
  or "but" where a connector belongs. (SW-refresh adds: connector openers are rare, 6 % of sentences at most. Let
  structure carry transitions.)
- R7. Every number carries a unit and an anchor, once, then it is left alone. Value, unit, comparison, stop. A bare
  number is never allowed.
- R8. An equation gets a purpose clause in (ending with a colon) and a "where ..." gloss out that defines every symbol.
- R9. A figure is narrated in adjacent prose and pinned to a number. (SW-refresh and my ruling S4: the figure pointer
  hangs on a number already in its sentence, for example "The deviation is 5.8 % (Figure 2).")
- R10. Hedges are bounded, never vague. Allowed: a stated boundary ("should still apply far from the critical
  point"). Banned: somewhat, fairly, relatively, quite, likely, probably, suggests.
- R11. Disagreement register. Quantify the disagreement ("disagree by up to 38 %"). Propose causes, never assert them
  ("it is presumed"). Never write "wrong", "erroneous", "fails", "flawed" of another model. Write "is not consistent
  with", "does not reproduce". State honest inability flatly ("We are not able to explain these differences.").
- R12. Uncertainty register. Report uncertainty with its coverage factor. Sign and quantify every deviation ("+12.5
  percentage points", "too low by 23 %"). Never "some error".
- R13. Honesty markers. State limits flatly: "Unfortunately, we could not test ...", "we make no attempt to resolve
  these discrepancies", "we have no reliable criterion to determine which". No apology, no hiding.
- R14. Comparison hygiene. Every accuracy comparison states the exposure of both sides: fitted to the same data,
  held-out, or out of sample. Never put an in-sample number of ours next to another model's out-of-sample or unknown
  number. Never present our own uninformed baseline as a competitor. Improvement over our own default is stated as
  such ("relative to the uncorrected model"). A model that was never scored may be called relevant, never inferior.

### 4.2 Banned list (all hard)

1. Em-dashes and parenthetical asides. Zero em-dashes. Break the aside into its own sentence or set it with commas.
2. Nested qualifications. At most one qualifier per sentence.
3. Meta-commentary: "it is worth noting", "importantly", "notably", "interestingly", and any sentence about the
   paper's own rhetoric.
4. Marketing adjectives (novel, robust, powerful, comprehensive, significant, cutting-edge) unless a number follows
   that earns them.
5. Rhetorical flourishes, triads for rhythm, "not X but Y". State the positive fact.
6. Colons that introduce a dramatic reveal. A colon introduces a list, an equation or a definition only.
7. Sentence fragments in running prose (the exceptions are list items, list labels and run-in heads, S1).
8. The word "arguably".
9. First-person singular (I, my).
10. Contractions.
11. Rhetorical questions.
12. Self-referential conduct. The paper never legislates its own behaviour. Banned: "must be stated at the outset",
    "never crossed", "this paper does not claim", "we are careful to", "the reader should", and planning vocabulary in
    prose ("the framing", "the argument", "referee"). Say what the model or the data do and do not do, then stop.
    Correct form: "The model does not include a solid phase."
13. The comparative-superiority family. Banned in either direction: beats, outperforms, better than, wins, loses to,
    superior to, inferior to. Permitted verdicts: improves, at par, statistically indistinguishable, trails by X
    points. A confidence interval that includes zero is a non-rejection, never "a tie" or "equal". Required
    rendering: "the difference is not resolvable at G independent groups", with G stated. Never "validated", "robust",
    "stable" or "generalizes" about something that was not shown to transfer to unseen data. Exception I allowed for
    the earlier paper: "agrees best" with a table pointer in the same sentence, in the Discussion only (rule S9, Part B).

### 4.3 What each mechanical check covers

C1 sentence length. C2 banned tokens, first person, contractions. C3 every number has a unit and a comparator. C4
every equation has a "where" gloss. C5 every figure pointer has a number. C6 self-reference. C7 comparison wording.
C8 signs of AI writing. `checks/voice_check.py` runs all of them. A FAIL blocks the prose. A REVIEW is read by a
person and either fixed or justified.

### 4.4 Content honesty that still binds

- Never state something false. Omitting process detail is fine (WORKING-RULES.md and rule M5 below).
- Reference-matching or reproduction stalls (an undisclosed constant, an ambiguous convention) are flagged to me and
  discussed. Never power through them and never write around them.
- Legal sources only. A blocked download is handed to me as a link with the full title and a verified DOI.
- Numbers from a source are extracted as printed. A number you cannot read is marked illegible, never guessed.

---

## Part B. The author's rulings

### B1. Writing rules

Process rules (structure by questions, feasibility first, disclosures, cost remarks, briefs) are in `WORKING-RULES.md`. Figure and table rules are there too.

- M4. Every number in the paper comes from a record you can regenerate or point to. Never type a number from memory.
  A number from an untracked diagnostic is not allowed.

- M5. Report at a high level. My words (after reading my own trial draft): "We are making our life tough with all
  these checks and hard rules and limitations on our model. Check the SW-refresh paper and see how their reporting is
  smooth, [not] a magnifying glass on every turn and action and decision. Not everything needs to be disclosed, not
  every limitation needs to be said, and not every number needs to reach the paper. Think high level." And: "the
  paper is too long and has unnecessary details". The code ships with the paper, so a reader can inspect everything
  there. The paper is a simple, easy entry point. So: report the model, the data in summary, and the results at the
  level a reader needs. Leave internal checks, guards, rejected alternatives, process steps and intermediate numbers
  out of the paper unless a reader truly needs them to use or trust the model. When a reviewer comment asks for more
  disclosure, first ask whether the paper needs it at all. Honesty still holds: never state something false.

- M6. Results only, no development story. My words: "we should not say in the paper that we ran without the
  correction and discuss how results enhanced. the whole premise now is that we have an extension to [the parent]
  model and these are our results." On a sentence with three numbers: "too many numbers. sentence is complex". The
  paper presents one model, not its history. No "falls from X to Y", no "after the fix was added", no old-versus-new
  deltas. A model that extends an earlier published model is stated once as a model choice.

- M7. No internal references in the paper. The paper never mentions internal project tags, ruling or ticket numbers,
  file names, tool or agent names, or the fact that numbers might change. It reads as the final paper and does not
  alarm the reader that a refit or update is under way. My words for the earlier paper: "The paper should not mention
  any internal references of course and internal projects tags. And should stick to the scope and the goal of the
  paper. Stale numbers are fine by me and the draft should not mention that. The paper when read should not alarm the
  reader that a refit is happening and he will think that this is the final paper." Words to keep out of prose:
  ledger, ruling, ratified, provisional, tentative, stale, pending, draft, handoff, backlog, lane, scratch, rebuild,
  and similar process words.

- M8. Plain language. In chat, always explain in simple words, short sentences, one idea per sentence. My words: "Your
  language is very complicated... Everything is a mess." and "Repeat ur answers in simple words." Translate code-names
  and statistics jargon ("average error", not "AAD"; "checked on data it never saw", not "leave-one-out"). The
  technical record on disk may stay technical. Option labels and context inside question prompts are plain too.

- M9. Define every statistical term (and every symbol) in the paper before its first use, in simple words: what it is,
  why we need it, and what it tells the reader. I caught "signed bias" used before it was defined. Run a
  paper-wide inventory of terms and symbols once per draft. Define each symbol once, then use it. Use one symbol per
  quantity everywhere: equations, glosses, nomenclature and text. When a reader may have forgotten where a quantity
  comes from, remind them in one clause (the source, or the standard it is computed from).

- M10. No draft watermark. Manuscript PDFs get a title banner under the title that says the draft status, never a
  diagonal watermark.

### B2. Claims and comparisons

- C1. One headline claim in agreed wording, no negative statement about a competing paper by name. No priority claims
  ("first", "first-ever", "novel") of any kind.
- C2. Compare published models on the FULL dataset only. Never frame, offer or quote a score "inside a model's own
  stated range", even if a record prints it. My words, after I had said it many times: "we agreed that we are not
  comparing the own stated range. i am saying this for the millionth time. we are comparing the full dataset." Apply
  published models as printed (their own published parameters), say once that ours are fitted values, and force every
  model over the same full data range with a footnote.
- C3. Comparison wording follows ban 13 and R14. "Agrees best", with a table pointer in the same sentence, is
  allowed in the Discussion only (my answer to clash 9). Do not put row or cell counts in comparison text: my words,
  "We will not be mentioning rows and tiny details in paper though."
- C4. One side-by-side sentence per item is allowed in the comparison sections only. It may carry two numbers, ours and
  one published model's, for example "For gas A the deviation is 5.69 % here and 5.96 % for Author (2012)." Never a
  sentence that pairs "%" with than, against, versus, relative to, or compared with. Reword as "exceeds ... by".
- C5. State the exposure of both sides in the comparison section: ours fitted, published models as printed, same rows,
  full data range. A specialist model fitted to most of the same data is said to be so, and the table is not
  presented as a contest.
- C6. A held-out test is named for what it is. A hold-out within one source is "within-source", not "independent".
  Say plainly what each held-out score means and what it leaves out.
- C7. Limits are stated about the model or the data, flatly, never as advice to the user. Write "The term is not tested
  above 45.8 MPa". Do not write "Users should validate ...". A limit that exists for a reason is said with its reason
  and its size, then stops. I asked once that the paper say whether a restriction is physical or a limit of the data
  that exist.
- C8. An honest number that will alarm a reader is not hidden. State what it means and when it applies, in one or two
  sentences. My words about a 72 % difference: "I know we are being honest but 72% will alarm any reader". Reframe
  the context, never the number.
- C9. Attribute accurately. Do not credit a compilation or a database with work that the project did (for example
  data exclusions, roles, screening). My words: "Aquasol db doesn't have any exclusions because it's just a
  compilation. Exclusions live in our project."
- C10. A statement of order or ranking ("A salts out more than B") is checked against the numbers before it stays in
  the text. A mechanical ranking check found one false sentence in my draft.
- C11. Never understate. If a figure says "within 2.4 %" and the largest value is 2.43 %, write 2.43 %, or say
  "at most". Printed precision follows the rounding rule (slot F10).
- C12. Where the draft names a model that extends an earlier published one, give the reason once for choosing it over
  refitting or extending other models. Do not over-explain the parent model in the "this work" section; the parent is
  described where it is used.

### B3. Style clashes the author ruled (answers S1 to S19; "A" means the first option, usually the one marked RECOMMENDED)

These resolve the conflicts between the SW-refresh register and the older rules. The stricter rule wins.

- S1. Fragments only in list items, list labels and run-in heads. Running prose has complete sentences.
- S2. Colons only before lists and display equations. No reveal colons and no colon elaboration in prose.
- S3. The 35-word ceiling holds. An enumeration that would pass 35 words becomes a list. (This overrides the SW-refresh
  allowance for long inline (i)/(ii)/(iii) sentences.)
- S4. A figure pointer hangs on a number already in its sentence: "The deviation is 5.80 % (Figure 2)."
- S5. A caption names no other figure by number. Write "drawn as for the first gas", not "as in Fig. A.5".
- S6. One-sentence paragraphs are allowed (pointers, retentions, exclusions). Every results subsection still ends on a
  number.
- S7. Parentheses hold data, sample sizes, conditions, citations and equation numbers only. No asides.
- S8. No semicolon joins two clauses in prose. Split into two sentences. A semicolon is allowed inside a list item.
- S9. "Agrees best" is allowed with a table pointer in the same sentence, in the Discussion only. The rest of ban 13 stays.
- S10. Limits are stated about the model (see C7). There are no "Recommendation:" lines in a paper with one model per
  item. (Ask me again in slot F7 for this paper.)
- S11. One number per sentence by default, two at most. No before-and-after stories. The one exception is C4.
- S12. Name each item in full (see R-names below).
- S13. Define each symbol once, then use it.
- S14. A short future-work bullet list may close the Conclusions (2 to 5 items, one item grammar). It states open work as
  open questions. It never hints at a refit, an update of numbers, or ongoing fitting. There is no future-work section
  in the Discussion. (This overrides the SW-refresh rule of no future-work paragraph.)
- S15. A status column in a table is allowed only against the parent published model ("parent model gas, fitted here"
  or "new in this work"). Never a column about the project's own history (no Retained or Updated wording). The header
  is never "Status".
- S16. Short plain noun-phrase headings. The finding goes into the first sentence of the section, not into the
  heading. Side tests carry the prefix "Investigation:". Per-item sections only where an item has its own finding.
- S17. Results are organised by question, then by object, with a brief subsection per object when there are several.
  The data section comes before the model section when the data audit is a selling point (my choice for the earlier
  paper; ask me again for this one, slot F1).
- S18. The abstract carries counts only (items, sources, rows), no percentages (my choice for the earlier paper; ask
  again, slot F8).
- S19. Each results section opens with its core table (for example the coefficients) before the per-object text.

### B4. Rules named in the slots (fill after asking the author)

- R-units. For the earlier paper's final version: "For later paper, we need to use SI units everywhere." Clarified:
  "What i mean final version of this paper." So the final paper states temperature in K, pressure in MPa and
  composition in mol/kg or mole fraction in text, tables, figures and the supporting information, with original units
  in a footnote where a table reproduces a published one. Slot F5 decides this paper's convention. Draft trial tables
  may use other units only when I say so.
- R-names. In the earlier paper, never a group shorthand such as "C2-C4", "C1-C4" or "heavier hydrocarbons". Write
  each species by its formula or name, every time, in the paper, tables, plan files and chat. Slot F6 decides which
  items in this paper must be named in full.
- R-rounding. For the earlier paper: percentages to two decimals, fitted coefficients to six decimals, counts exact, spans shortened endpoint by endpoint, values with fewer decimals printed at their own precision. Slot F10 decides this paper's rule.

### B5. Recurring corrections the author made when reading drafts (patterns, not content)

Check every draft against these before showing it to me.

1. "Feels over-written and like AI." The sentence is too polished, abstract or grand. Rewrite it simpler, with the
   concrete fact and its number, and tone down any claim to what the data show. Also: "it is overclaimed".
2. A section that over-explains something described elsewhere (the parent model in the "this work" section) and does
   not say why we chose this approach over the alternatives. Cut the explanation, add the reason.
3. Confusing wording about model mechanics (which term acts on which side of the equation, what a coefficient sets).
   Rewrite as short statements, one object per sentence, plain verbs.
4. An equation, constant or method is used but its source is not stated where the reader needs it. Put the citation, or
   the equation, at the point of use. For a new form, print the full equation, not only a pointer to a reference.
5. Two symbols for one quantity, or a quantity whose computation is not recalled. Use one symbol and add the reminder
   clause.
6. A statistical term used before it is defined (see rule M9).
7. A statement that credits a source with something it does not do (see C9).
8. A number that is honest but alarming (see C8).
9. A statement of fact that the data contradict, found only by recomputing (see C10 and C11).
10. Caption too long, figures too large, tables inconsistent (WORKING-RULES.md, Figures and tables).
11. A parameter described as "fixed" in the sense of "determined". I dislike the word "fix" for that use. Use "set",
    "determine" or "fit", throughout the paper.
12. Print the generic form of an equation once; let a table show which terms are zero for which item. Drop item-specific
    term lists from the text.
13. Close a long results section with a short verdict on what the reader should take away.
14. Unclear counts: a table of counts must say what it counts and why a total is not the sum, if it is not.
15. Back matter in this order: data and code availability (short: what the companion code and data contain, with
    links), supporting information (its link after publication and its contents in order), author contributions,
    declaration of competing interest, acknowledgements, references. The nomenclature may live in the supporting
    information.
16. An appendix or supporting information decision is owed once: what a reader needs to use the model (equations,
    constants, all fitted parameters, preferably as one master table of coefficients) goes in the paper's appendix or
    main text; supporting information holds extra information only. Check what the parent paper did.
17. Reference-list hygiene before submission: every in-text citation is in the list and the reverse, no entry printed
    twice, no entry used only by a table left out, every DOI resolves to the cited paper.
18. A subsection split by object is brief (3 to 6 sentences) and still ends on a number.
19. When a rewritten paragraph's substance is settled, keep the substance and drop numbers if that makes it easier to
    read.

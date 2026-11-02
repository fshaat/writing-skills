---
name: academic-writing-human
description: Use when drafting or revising journal papers, HBKU thesis chapters, reports, abstracts or response letters so the text is specific, precise, varied and honest rather than generic. Covers thesis-chapter and section-by-section structure, citation verification, a revision procedure, and AI-style tells that paper-voice lacks. Complements `paper-voice` (sentence register and the main AI-signs checklist, which take precedence) and `journal-revision` (the owner's personal rules and LaTeX layout).
---

# Academic writing that reads as written by a person

## Purpose and limits

This skill is about writing well: every sentence says something specific, checkable and true.
It is **not** a tool for evading AI detectors or for hiding how a text was produced.

- The author remains responsible for every claim, number, citation and conclusion, whoever or whatever drafted the words.
- Follow the AI-use disclosure policy of the institution (HBKU) and of the target journal or publisher. Checked 2026-10-28:
  Elsevier wants a "Declaration of generative AI and AI-assisted technologies in the writing process" above the references
  (grammar and spelling checks exempt); Nature Portfolio wants LLM use documented in the Methods; IEEE wants it in the
  Acknowledgments; SPE wants it in the methodology or acknowledgement section, may reject undisclosed AI content, and holds
  authors responsible for errors and incorrect references introduced by the tool. None allows an AI tool as an author.
  Policies change: read the current guide for authors before every submission.
- Removing surface tells without fixing the content underneath (missing numbers, unsupported claims) is not the goal.
  Wikipedia's AI Cleanup page warns that doing so "could just make detection harder" while leaving the problem.

## Precedence and division of labour (read first)

Where two skills disagree, the higher one wins:

1. **The owner's own rules**: `.claude/skills/journal-revision/SKILL.md`,
   `00_plans/02_journal_paper_Egg_benchmark/07_PREFERENCES_AND_WRITING_RULES.md` and `08_MISTAKES_TO_NOT_REPEAT.md`,
   plus the memory rule that journal edits are minimal: edit only the commented passages and their identical copies,
   keep the original layout, add no ablation, regeneration or implementation disclosures, report the fastest measured
   configuration only. A finished paper is never restructured into a new register.
2. **`paper-voice`** (`.claude/skills/paper-voice/`, shared by Dr Abdulsalam Abd): the SW-refresh register, which is the
   **default register for new journal papers in this field** (petroleum and fluid-phase engineering). Its `SKILL.md`,
   `RULES.md` and `AI-SIGNS.md` (52 signs from Wikipedia rev 1378298730) set sentence length, numbers per sentence,
   headings, lists, captions, comparison wording and the main AI-signs checklist. Run its `checks/voice_check.py`.
3. **This skill**: general guidance, thesis chapters, section-by-section structure, citation verification, the revision
   procedure, and the extra tells in `references/ai_tells.md` that `AI-SIGNS.md` does not list.

Where this file and `paper-voice` look alike (no em dashes, no boosters, numbers with units), follow `paper-voice`'s exact
wording and thresholds. Where the owner's rules and `paper-voice` clash, flag it to the owner with one recommendation
(for example: the owner allows one to three key numbers per paragraph and the words "very small" and "large"; `paper-voice`
wants one number per sentence and bans most qualitative comparison words).

## 1. Principles

These restate what good style guides agree on (Sword, Pinker, Strunk and White). `paper-voice` makes several of them measurable.

1. **Say something specific in every sentence.** A sentence that would fit any paper on any topic is cut or given its missing fact.
2. **Lead with the result.** The first sentence of a paragraph carries its message.
3. **Put numbers, units and conditions in the text,** with the data set, horizon, hardware or precision under which the number holds.
4. **Name methods and data.** "a graph neural network with 15 message-passing layers trained on 90 Egg realizations",
   not "a deep learning approach on a benchmark".
5. **Hedge only where uncertainty is real, and give its size.** A hedge with a number is information; "may potentially" is not.
6. **One claim per sentence.** Vary sentence length; do not write five sentences of the same length in a row.
7. **Active voice where the actor matters** ("we trained in BF16"); passive for routine procedure.
8. **One job per paragraph.** A paragraph that needs a bold inline header is a list in disguise, or two paragraphs.
9. **Domain terms over generic adjectives;** plain verbs over zombie nouns ("we compared", not "a comparison was performed"; Sword).
10. **Write for a reader who was not in the lab** (Pinker's "curse of knowledge"): define each acronym, give grid sizes, say what a rollout is.

## 2. Tells to remove

Run `paper-voice`'s `AI-SIGNS.md` first (its grep block and its overlap rules). Then check the **additional** tells in
`references/ai_tells.md`, each with its source: the Kobak et al. (2025) excess-vocabulary words missing from `AI-SIGNS.md`,
the Liang et al. (2024) peer-review adjectives, zombie nouns, hedge stacks, false balance, unconditioned numbers,
scope inflation, tour-guide sentences, uniform paragraph openings and fabricated quotes.
`references/examples.md` has before and after passages from reservoir simulation and machine learning.
**All numbers in the examples are placeholders, not results of this project.** Never copy them into a paper.

A sign is a prompt to look harder, not proof. Fix it by stating the fact and its number. Never swap in a synonym.

## 3. Section by section

The journal default is `paper-voice` Parts 1 and 5 (many short numbered sections, one idea each, typed results chapters,
numbered Conclusions). The notes below add what it does not cover for a GNN surrogate of OPM Flow.

**Abstract.** Problem, method with names, data with sizes, scope. Whether accuracy numbers appear is the owner's choice per
paper (`paper-voice` S18 uses counts only; the Egg paper used headline numbers). No "In this paper, we".

**Introduction (gap → contribution).** The engineering need (cost of one OPM Flow run, number of runs an optimisation
needs), what cited surrogates do, the specific gap, and the contributions as checkable facts. No "rapidly evolving
landscape" opening and no roadmap paragraph.

**Methods (reproducible detail).** Grid and active cell count, realizations and the split, node and edge inputs and
outputs, which inputs are planned controls and which are simulator responses, loss, optimiser, learning rate, epochs,
precision, hardware, software and simulator versions. Every equation displayed, numbered and glossed.

**Results (numbers first, figures referenced).** Each paragraph opens with the result and its number, then points to the
figure or table. Say what the reader should look at, not what the figure obviously shows. Text, captions and tables carry
the same numbers.

**Discussion (honest scope).** Explain why the results came out as they did, compare with cited work on equal terms
(same data, same exposure; `paper-voice` R14), and state the tested scope as a fact about the model: "The model is tested
on the Egg model only." In journal text, follow the owner's rule against hypotheticals and self-weakening caveats.

**Conclusion (no restating).** The main finding with its key number, what it means in practice, and its boundary.
Not a copy of the abstract; no "In conclusion".

### HBKU thesis chapter

`paper-voice` measures a journal register. A thesis chapter is longer and must stand on its own for examiners.
Scope is Egg and Norne only (see the thesis memory note). Source: `06_thesis/latex`.

- **Opening (one paragraph).** What the chapter establishes and why the thesis needs it, linked to the previous chapter in
  one sentence. No subsection roadmap.
- **Literature chapter.** Organise by question (what surrogates exist, how they are evaluated, where they fail), not by
  paper. Every paragraph makes a claim about the field and cites the primary papers that support it. End with the gap
  this thesis fills, stated once.
- **Methods chapters.** Full reproducible detail; more than a paper allows. Derivations may sit in the chapter or an
  appendix as the supervisor prefers.
- **Results chapters.** One question per section; the number first; every figure discussed where it appears.
- **Limitations.** A thesis normally has a limitations section. State each limit flatly with its size, as a fact about the
  model or data, and stop. Confirm the extent with the supervisor before writing it.
- **Closing (one paragraph).** The facts the next chapter uses. Cross-reference instead of repeating other chapters.
- **Consistency.** One term per concept across all chapters, one symbol per quantity, a nomenclature list, and the same
  numbers wherever the thesis and the journal paper report the same experiment.
- Follow the HBKU thesis template and graduate-studies rules for structure, declaration pages and AI-use statements.

## 4. Citations

- **Never invent a reference**, DOI, page, author list or quote. A claim with no verifiable source is rewritten or removed.
- Cite only sources that were found and checked. Resolve each DOI (`https://doi.org/<doi>`) and compare title, authors,
  journal and year: DOIs that point to unrelated papers are a documented LLM failure (`AI-SIGNS.md` item 35).
- Check that the cited source says what the sentence claims. Do not attribute your interpretation to an author.
- Quote exactly, with the page; otherwise paraphrase.
- Prefer primary literature (the paper that introduced the method or reported the measurement) over reviews and summaries.
- No "studies show" or "it is well known" without the specific citations.
- Before submission: every `\cite` key is in the .bib file and the reverse; no duplicates; no entry with a missing DOI,
  volume or page that the journal requires.
- A source behind a paywall is given to the owner as a link with full title and verified DOI, never guessed at.

## 5. Revision procedure

Run on new text, or only on the passages the owner asked to change.

1. **Read it aloud,** or with text to speech. Mark every sentence you would not say to a colleague.
2. **Cut the first paragraph or sentence** of each section if it only sets the scene; see whether the text starts better without it.
3. **Run the checks.** `paper-voice`'s `checks/voice_check.py` and the `AI-SIGNS.md` grep block, then the extra patterns in
   `references/ai_tells.md`. For LaTeX sources a quick scan from Git Bash:
   `grep -n -i -E -w "delve[sd]?|intricate|pivotal|underscore[sd]?|showcas(e|es|ing)|crucial|comprehensive|seamless(ly)?|leverag(e|es|ing)|harness(es|ing)?|realm|elucidat(e|es|ing)|unveil(s|ed|ing)?|commendable|meticulous(ly)?|paradigm" chapter.tex`
   Read each hit. Keep a word only when it is the exact technical term.
4. **Every paragraph contains a fact or a number.** A paragraph with neither is deleted or merged.
5. **Check figure and table references.** Each is cited before it appears, the text says what it shows, and the numbers in
   text, captions and tables agree. For journal LaTeX run the owner's `order_check.py` and `cite_cap.py` (`journal-revision`).
6. **Check every claim is supported** by a number from this work, an equation, or a verified citation. List the rest and fix them.
7. **Check rhythm and openings.** No three paragraphs in a row opening the same way; sentence lengths vary.
8. **Check every number** against the run that produced it (a results file, a log, a table). Never type a number from memory.
9. **Check formatting.** No stray bold, Markdown, emoji, title case, or bullets in running prose.
10. For journal deliverables, finish with the owner's compile, layout and proof checks (`journal-revision` step 4) and look at every changed page.

## 6. Whole-document pass (thesis or long report)

Use this when the owner asks for a full chapter or thesis to read as a person's work. It is a rewrite from the meaning up,
not a word swap. The edit is done paragraph by paragraph and is checked by script.

**What detectors measure (guide of 2026-11-02, `references/humanizer_guide_20261102.md`).** They score predictability, not
authorship. Scores are unreliable in both directions, no method can promise a low score, and a low score proves nothing.
So there is no detector target in this skill. The target is prose an examiner trusts: specific, varied and true.
HBKU runs iThenticate through the supervisor for similarity, and its guidelines (Section 3.2.9) require any AI use to be
disclosed on the Declaration page. **Keep that disclosure in place. Never remove or soften it.**

**Never do these.** They are deception, and they make the text worse:
- invisible characters, look-alike letters, or planted typos and slang;
- synonym spinning or paraphrasing tools;
- tuning the text against a detector score;
- inventing a personal anecdote, a number, a date or a source to look human.

**Do these, adapted to a thesis.** The guide is written for emails and marketing; this table sets what carries over.

| Guide habit | In a thesis |
|---|---|
| Vary sentence length | Yes. Burstiness of at least 0.45 and at least 15 % short sentences per chapter, reached by splitting or joining sentences for sense |
| Add details only you know | Yes, only true ones from the record: the run, grid, date, commit, setting, what failed and how it was noticed |
| Cut stock transitions | Yes. Most paragraphs need no connector. Keep "however" or "therefore" where the logic turns |
| Say what you think | Yes, as a judgment with its evidence: "This result rules out X because Y" |
| Cut the adjective, add a fact | Yes. This is the most useful single edit |
| Use "is" and "has" for "serves as" and "features" | Yes |
| Avoid habitual triads and "not just X but Y" | Yes |
| No dramatic one-line closer, no fake-depth "-ing" tail | Yes |
| Contractions, friendly tone, "I'd skip this" | **No.** Keep the formal academic register |
| No en dashes | Prose only. Numeric ranges keep their en dash (states 4--120) |
| Ban "enhance", "robust", "key", "critical" | Read each. Keep the exact technical sense ("critical saturation"), rewrite the rest |

**Procedure for each chapter.**
1. Record the numbers: keep the old file. Every number, citation and label must survive.
2. For each paragraph: what is its one claim? Lead with it. Rewrite in plain, formal sentences from that claim.
3. Vary the openings. No paragraph opens with the chapter's topic noun by habit; no more than two opening with the same word in a row.
4. Delete tour-guide sentences ("This section describes...") unless a chapter opening truly needs one.
5. Run `checks/tex_style_check.py --list FILE.tex` and read each hit. Targets per 1000 words: stock words under 3, stock phrases under 1,
   connector openers under 2, no fake-depth tails, no em dashes.
6. Run `checks/tex_fact_guard.py OLD.tex NEW.tex`. Every LOST or NEW item must be an intended change. Otherwise restore it.
7. Read the chapter once from start to finish. Writers repeat themselves between sections, and that shows only in a full read.

## 7. Files

- `references/ai_tells.md`: tells not in `paper-voice/AI-SIGNS.md`, with sources and a grep block.
- `references/examples.md`: before and after passages in reservoir simulation and ML.
- `references/humanizer_guide_20261102.md`: the owner's Humanizer Setup Guide, what was taken from it, and what was not.
- `checks/tex_style_check.py`: LaTeX-aware stock-word, phrase, opener and rhythm metrics, per chapter.
- `checks/tex_fact_guard.py`: lists every number, citation, label, reference and figure changed between two versions.

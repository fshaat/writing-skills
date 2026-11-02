# Additional AI-style tells (not in paper-voice/AI-SIGNS.md)

Run `.claude/skills/paper-voice/AI-SIGNS.md` first. It holds the 52-item checklist from Wikipedia "Signs of AI writing"
(rev 1378298730) with a grep block and overlap rules. This file lists **only what that checklist lacks**, numbered A1 onward
so the two lists never collide. Do not duplicate items here; if `AI-SIGNS.md` gains an item, delete nothing, mark it
"now covered by AI-SIGNS item N".

A tell is a prompt to look harder, not proof. Fix it by stating the fact and its number, never by a synonym swap.
Numbers in the examples are placeholders, not project results.

## Sources (checked 2026-10-28)

- [K] Kobak, D., González-Márquez, R., Horvát, E.-Á., Lause, J. (2025). Delving into LLM-assisted writing in biomedical
  publications through excess vocabulary. *Science Advances* 11(27), eadt3813. https://doi.org/10.1126/sciadv.adt3813 ;
  preprint https://arxiv.org/abs/2406.07016 ; word lists in Fig. S6 (291 "rare" and 10 "common" excess style words;
  66 % verbs, 14 % adjectives). At least 13.5 % of 2024 PubMed abstracts were processed with an LLM.
- [L1] Liang, W. et al. (2024). Monitoring AI-modified content at scale: a case study on the impact of ChatGPT on AI
  conference peer reviews. ICML 2024. https://arxiv.org/abs/2403.07183 . 6.5 % to 16.9 % of review text substantially
  LLM-modified; "commendable", "meticulous" and "intricate" rose 9.8-, 34.7- and 11.2-fold; reviews with "et al." (a
  citation proxy) showed lower estimated LLM use.
- [L2] Liang, W. et al. (2024). Mapping the increasing use of LLMs in scientific papers. COLM 2024.
  https://arxiv.org/abs/2404.01268 . Up to 17.5 % of computer-science abstracts LLM-modified by Feb 2024.
- [W] Wikipedia: Signs of AI writing. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- [S] Sword, H. (2012). *Stylish Academic Writing*. Harvard University Press; "zombie nouns", summarised at
  https://www.manchester.ac.uk/discover/news/steven-pinker-on-zombie-nouns-and-the-curse-of-prior-knowledge/
- [P] Pinker, S. (2014). *The Sense of Style*. Viking; "curse of knowledge" and classic style, summarised at
  https://www.psychologicalscience.org/observer/the-curse-of-knowledge-pinker-describes-a-key-cause-of-bad-writing
- [SW] Strunk, W., White, E.B. *The Elements of Style* ("omit needless words", "use definite, specific, concrete language").
- [Pol] Publisher policies: Elsevier https://www.elsevier.com/about/policies-and-standards/the-use-of-generative-ai-and-ai-assisted-technologies-in-writing-for-elsevier ;
  IEEE https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/ ;
  SPE https://jpt.spe.org/spe-policy-on-ai-generated-content-in-publications ;
  Nature Portfolio https://www.nature.com/nature-portfolio/editorial-policies/ai (login redirect when fetched; wording
  taken from secondary summaries); ACS: primary page not retrieved, secondary summaries disagree on Methods versus
  Acknowledgments, so check the journal's own guide.

Caveat: [K], [L1] and [L2] estimate LLM use across a corpus. They do not identify single documents, and a listed word is
often legitimate. The aim here is precise writing, not avoiding a word list.

## A. Vocabulary

A1. **Kobak excess words missing from AI-SIGNS item 9** [K]. Watch when several cluster:
comprehensive, notably, insights, potential (as a noun of promise), elucidate, realm, seamless(ly), unveil, harness,
leverage, paving (the way), unparalleled, unravel, uncharted, transformative, revolutionize, pinpoint, shedding (light),
noteworthy, nuanced, multifaceted, invaluable, imperative, burgeoning, compelling, culminating, discern, endeavor,
facilitate, formidable, foundational, grappling, poised, pressing, propelling, streamline, surpass, swiftly,
underexplored, unexplored, utilize, methodologies, avenue(s), spurred, strategically, exceptional(ly), impressive,
remarkable, innovative, versatility, adept, encapsulate, necessitate.
Bad: "We leverage a comprehensive methodology to elucidate the nuanced interplay of permeability and saturation."
Better: "We train on 90 permeability realizations and report the saturation error per realization."

A2. **Peer-review adjectives** [L1]: commendable, meticulous, intricate (also in A1/AI-SIGNS), and praise with no object.
Bad (response letter): "We thank the reviewer for this commendable and meticulous comment."
Better: "We added the per-well water-cut error to Table 6, as the reviewer asked."

A3. **Grand-claim nouns**: paradigm shift, game changer, new era, unlocks, holy grail, revolution.
Bad: "GNN surrogates represent a paradigm shift in reservoir management."
Better: "A surrogate run takes <t1> s against <t2> s for OPM Flow on the same case."

A4. **Generic quantifiers in place of a count**: various, numerous, a wide range of, a plethora of, multiple (when the
number is known). [SW]
Bad: "tested on a wide range of geological scenarios". Better: "tested on 10 held-out Egg realizations".

A5. **Zombie nouns** (nominalisations that hide the actor and the verb) [S].
Bad: "An investigation of the effect of time-step size on error accumulation was performed."
Better: "We measured how the rollout error grows with time-step size."

A6. **Undefined jargon and in-group labels** (the curse of knowledge) [P]: rollout, teacher forcing, halo, BF16, run or
lane codes used without a gloss. Better: define at first use in plain words (also the owner's rule 14).

## B. Sentence and paragraph structure

B1. **Hedge stacks**: two or more hedges on one claim ("may potentially suggest", "could possibly indicate"). [W]
(human writers hedge; stacking is the tell). Keep at most one hedge, tied to a number or condition.
Bad: "These results may potentially suggest some improvement." Better: "The error is below <x> bar on 9 of 10 test cases."

B2. **False balance**: "On the one hand ... on the other hand", "While X, it is also important to consider Y", used
when no trade-off was measured. Better: give the trade-off in numbers or drop it.

B3. **Unconditioned numbers**: a metric with no data set, horizon or comparator ("R² of 0.98"). Better: "mean spatial
R² of <x> for pressure at the last report state, averaged over the 10 test realizations".

B4. **Scope inflation**: a result on one model extended to "reservoir engineering", "the industry", "real fields".
Better: name the model and field tested and stop.

B5. **Tour-guide and announcement sentences** beyond AI-SIGNS item 26: "This section is organised as follows",
"Let us now turn to", "As mentioned above", "As we will see". Better: start with the content.

B6. **Uniform paragraph openings**: three or more paragraphs in a row opening with the same word or pattern
("The model ...", "Figure N shows ...", "In addition, ..."). Vary by leading with the specific finding.

B7. **Uniform sentence length and rhythm**: low variance in sentence length (LLM text tends to be regular; see the
syntax note in [W] "Signs of human writing"). `paper-voice` K4 gives the targets; also mix short and long.

B8. **Paragraphs that restate the figure**: "Figure 5 shows the pressure map. The pressure is high near injectors and low
near producers." Better: state what is surprising or measured: "The largest pressure error, <x> bar, sits at the
injector in the high-permeability channel (Figure 5)."

B9. **Closing moral sentence** at the end of a paragraph ("This demonstrates the importance of careful design.").
Better: end on the last fact or delete the sentence.

## C. Content and honesty

C1. **Fabricated or unchecked quotes and page numbers.** A quotation attributed to a paper must be copied from that paper
with its page. [W] (book citations without pages; misattributed analysis) [Pol] (authors responsible for incorrect references).

C2. **Generic citations**: a citation to a review or textbook for a specific numerical claim, or several citations
bundled after a generic sentence. Better: one primary source per specific claim. [L1] notes LLM-heavy reviews cite less.

C3. **Missing numbers where the work has them**: "the surrogate is much faster" when the timing table exists.
Better: quote the measured number (owner rule: fastest measured configuration only).

C4. **Mixing planned controls and realized responses** in method descriptions (project-specific, AGENTS.md): calling a
simulator response an "input". Better: state which inputs are planned controls from the deck and which quantities are outputs.

## D. Deeper tells (added 2026-10-28 from two owner-supplied articles)

Sources: [R] A. Romero, "10 Signs of AI Writing That 99% of People Miss", The Algorithmic Bridge, 3 Dec 2025;
[V] vrid.ai blog, "Signs of AI Writing: 27 Red Flags You Keep Missing", 11 Feb 2026. Both are opinion/blog sources,
not research. [V] is a vendor page whose statistics (detector accuracy, citation rates) are unverified; use its
patterns, never its numbers. Only tells that apply to academic prose are kept.

D1. **Abstraction trap.** Abstract nouns where a concrete quantity or object exists ("the framework offers a
comprehensive understanding of the landscape"). Test: can the reader picture or measure it? Better: name the cell,
the well, the variable and the number. [R][V]

D2. **Harmless filter.** Only bland, approving adjectives ("vital", "crucial", "dynamic"); no honest negative judgment.
Better: state failures plainly ("the model fails on low-permeability cases: WWPR R² 0.31"). [R]

D3. **Latinate bias.** "utilize, facilitate, demonstrate, commence, approximately" where "use, help, show, start, about"
fit. Keep the Latinate word only when it is the technical term. [R][V]

D4. **Equivocation seesaw.** Every claim balanced by a hedge in the same sentence ("While X has benefits, it is
important to note that Y presents challenges"). Better: state the claim, then its limit with its evidence, in
separate sentences. [R][V]

D5. **"Despite its strengths, X faces challenges" formula.** Better: name the specific limitation and its size. [V]

D6. **Treadmill effect.** Paragraphs restate the previous one without adding a fact. Test: each paragraph must add
at least one new number, method detail or result; delete paragraphs that do not. [R][V]

D7. **Length over substance.** Text two to five times longer than its content. Better: cut to the facts; a results
paragraph is usually 3 to 6 sentences. [R][V]

D8. **Over-explicit subtext / over-explanation.** Explaining what the expert reader already knows, or stating the
implication after every result. In academic prose define each term once, at first use, and trust the reader after
that. [R][V]

D9. **Meta-commentary and roadmaps inside sections.** "In this section we will explore…", "As we have seen…".
A one-paragraph roadmap at the end of an Introduction is a field norm; elsewhere, delete. [V]

D10. **Metronome rhythm.** Every sentence 15 to 20 words. Better: mix short and long sentences (paper-voice's
short-sentence rule still applies; vary within it). [V]

D11. **Formulaic paragraph shape.** Every paragraph is topic sentence, then support, then summary sentence. Drop
the summary sentence; vary the openings. [V]

D12. **"-ing" sentence openers and "From X to Y" sweeps.** "Leveraging graph structure, the model…"; "from small
fields to giant reservoirs". Better: subject first; list the actual cases. [V]

D13. **Personified data and methods.** "The data tells us", "the model chose", "the results speak for themselves".
Better: "the R² is 0.95", "we chose". [R][V]

D14. **Symmetrical list items.** Every bullet the same length and shape. Real lists are uneven; in a paper, prefer
prose unless the items are a true enumeration. [V]

D15. **Ghost citations.** "Studies show", "experts agree" with no reference. Name the source with DOI (see C2). [V]

D16. **Nice-nice comparison.** Comparing methods and ending "both have their strengths". Better: say which wins
on which metric, with the number. [V]

D17. **Format bleed.** Markdown stars, hashes or bracket links left in a LaTeX or Word manuscript. Grep for
`\*\*|^#+ |\]\(` before submission. [V]

Not adopted, because they conflict with academic norms: "use I and you", "write fragments", "imperfect grammar
reads as human", "turn every list of three into four". Academic prose stays grammatical, and uses "we" where the
journal allows it.

## Grep block (case-insensitive; run after the AI-SIGNS.md block)

```
\b(comprehensive|notably|insights?|elucidat(e|es|ed|ing)|realms?|seamless(ly)?|unveil(s|ed|ing)?|harness(es|ed|ing)?|leverag(e|es|ed|ing)|pav(e|es|ing) the way|unparalleled|unravel(s|ed|ing|ling)?|uncharted|transformative|revolutioni[sz](e|es|ing)|pinpoint(s|ed|ing)?|shed(s|ding)? light|noteworthy|nuanced?|multifaceted|invaluable|imperative|burgeoning|compelling|culminat(e|es|ing)|endeavou?rs?|facilitat(e|es|ed|ing)|formidable|foundational|grappl(e|es|ing)|poised|propelling|streamlin(e|es|ed|ing)|surpass(es|ed|ing)?|swiftly|underexplored|unexplored|utili[sz](e|es|ed|ing)|methodologies|avenues?|exceptional(ly)?|impressive|remarkabl[ey]|innovative|versatil(e|ity)|adept|encapsulat(e|es|ing)|necessitat(e|es|ing))\b
\b(commendable|meticulous(ly)?|paradigm shift|game[- ]changer|new era|holy grail|unlock(s|ing)?)\b
\b(various|numerous|a (wide|broad) (range|variety|array) of|a plethora of|myriad)\b
\b(may|might|could) (potentially|possibly)\b|\b(potentially|possibly) (suggest|indicate)s?\b
\bon the one hand\b|\bon the other hand\b|\bit is (also )?important to consider\b
\b(this (section|chapter) is organi[sz]ed as follows|let us (now )?turn|as (mentioned|discussed|noted) (above|earlier|previously)|as we will see)\b
\b(was|were) (performed|conducted|carried out)\b
\bthis (demonstrates|shows|highlights) the (importance|need|value)\b
\b(despite (its|their) [a-z]+, [a-z ]+ faces?|both (have|offer) their (strengths|merits))\b
\b(the (data|results|model) (tells?|speaks?|chose|wants?))\b|\bspeak for themselves\b
\b(in this (section|chapter),? we (will )?(explore|discuss|examine))\b|\bas we have seen\b
\b(studies (show|suggest)|experts (agree|believe)|research (shows|suggests))\b
\b(commence[sd]?|approximately|demonstrat(e|es|ed|ing))\b
^(Leveraging|Harnessing|Utili[sz]ing|Offering|Providing|Combining) 
\bfrom [a-z ]+ to [a-z ]+\b
\*\*|^#+ |\]\(
```

Count: 36 additional tells (A1 to A6, B1 to B9, C1 to C4, D1 to D17). Together with the 52 items of `AI-SIGNS.md`, 88 tells are covered.

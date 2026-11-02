# Before and after: reservoir simulation and ML

All numbers are placeholders (`<x>`, `<n>`) or clearly invented. Never copy them into a paper; take every number from
the run that produced it. For journal text the "after" versions follow `paper-voice` (short declarative sentences, one
number per sentence by default, no before-and-after stories about our own fixes) and the owner's rules in
`journal-revision`. Tell codes refer to `paper-voice/AI-SIGNS.md` items (S#) and to `ai_tells.md` (A#, B#, C#).

## 1. Abstract opening

Before:
> In the rapidly evolving landscape of reservoir management, machine learning has emerged as a transformative tool.
> This paper delves into a novel, robust and comprehensive graph-based framework that not only accelerates simulation
> but also enhances predictive accuracy, paving the way for real-time decision making.

Tells: S1 (evolving landscape), A1 (transformative, comprehensive, paving the way), S9 (delve, robust), S11 (not only
... but also), S13 (rule of three), B4 (scope inflation).

After:
> Optimising well controls on a heterogeneous reservoir needs hundreds of OPM Flow runs. This work trains a graph neural
> network surrogate on <n> realizations of the Egg model. Each node is a grid cell, and each edge is a cell face. The
> surrogate predicts pressure and water saturation for the full production period from the planned well controls.

## 2. Significance inflation in a results paragraph

Before:
> Permeability plays a pivotal role in the displacement process, underscoring the crucial importance of capturing
> heterogeneity, which highlights the intricate interplay between geology and flow.

After:
> The high-permeability channels carry most of the injected water. The saturation error is largest where a channel
> meets a producer, at <x> (Figure <k>).

## 3. Hedge stack and unconditioned number

Before:
> The results may potentially suggest that the model achieves an R² of 0.98, which could indicate strong
> generalisation.

Tells: B1, B3, and "generalisation" claimed without an out-of-sample test (`paper-voice` ban 13).

After:
> The mean spatial R² for pressure at the last report state is <x> over the <n> held-out test realizations.

## 4. Zombie nouns and passive without an actor

Before:
> An evaluation of the computational performance of the surrogate was conducted, and a significant reduction in
> run time was observed.

After:
> One surrogate prediction takes <t> s on one RTX 3090 (Table <k>).

(One number per sentence. A second sentence can give the OPM Flow time if the owner wants the comparison in text.)

## 5. False balance

Before:
> On the one hand, GNNs offer remarkable flexibility; on the other hand, they require considerable training effort.

After:
> Training took <h> h on two GPUs. After training, each prediction takes <t> s.

## 6. Restating the figure

Before:
> Figure 7 shows the water saturation maps. Water saturation is high near the injectors and low near the producers.
> This demonstrates the importance of accurate saturation prediction.

Tells: B8, B9.

After:
> The water front reaches producer PROD<k> by the last report state in both OPM Flow and the surrogate (Figure 7).
> The largest saturation difference, <x>, lies along the front.

## 7. Vague attribution and generic citation

Before:
> Studies have shown that graph neural networks generalise well to unseen meshes [1-5].

Tells: S6 (vague attribution), C2 (bundled citations for a specific claim).

After (only if the source was read and says this):
> <Author> et al. (<year>) trained a mesh-based graph network on <their data> and report <their metric> on meshes not
> seen in training.

If no checked source says it, delete the sentence.

## 8. Limitations, journal versus thesis

Journal (owner's rule: no hypotheticals, no self-weakening caveats; `paper-voice` C7: state limits about the model):
> The surrogate is trained and tested on the Egg model.

Thesis chapter (if the supervisor wants a limitations section):
> The surrogate is trained and tested on the Egg model, a <n>-cell two-phase case with fixed fluid properties. It has
> not been tested on a model with faults or gas. Chapter <k> applies the same method to the Norne field.

Before (both): "Despite these limitations, the framework shows great promise for future applications." (S7, S1) Delete.

## 9. Response to a reviewer

Before:
> We sincerely thank the reviewer for this commendable and insightful comment. We have meticulously revised the
> manuscript to ensure clarity and comprehensiveness.

Tells: A2, S40, S41.

After:
> We added the per-well water-cut error to Table <k> (Section <m>, lines <a> to <b>).

## 10. Thesis chapter opening

Before:
> This chapter delves into the methodology. Section 3.1 presents the data, Section 3.2 presents the graph, Section 3.3
> presents the model, and Section 3.4 presents the training.

After:
> This chapter defines the graph, the model and the training used in every later chapter. Each grid cell is a node,
> each shared face is one edge with a message in each direction, and the inputs at each step are the planned well
> controls and the previous predicted state.

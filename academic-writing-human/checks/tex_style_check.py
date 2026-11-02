#!/usr/bin/env python3
"""Style check for LaTeX prose (thesis and paper chapters). Python standard library only.

Usage:  python -I tex_style_check.py [--list] FILE.tex [FILE.tex ...]

Reports, per file, per 1000 words:
  words     stock AI vocabulary from the Humanizer guide, AI-SIGNS item 9 and Kobak et al. (2025)
  phrases   stock phrases and copula dodges ("serves as", "plays a role", "not only ... but")
  openers   connector openers (Moreover, Furthermore, Additionally, In addition, Overall, ...)
  ingtail   sentences closed by ", highlighting/underscoring/... -ing" (fake depth)
  dash      em dashes in prose
  triads    "X, Y, and Z" lists (informational; many are legitimate)
Rhythm:
  mean, sd  sentence length in words
  burst     sd / mean of sentence length. Below 0.40 reads as uniform.
  short     share of sentences of 12 words or fewer. Below 15 % reads as uniform.
  runs      runs of 4 or more consecutive sentences within 3 words of each other in length
  repeat    paragraphs whose first word equals that of the previous paragraph

A hit is a prompt to read the sentence, not an error. Exact technical terms stay.
Exit status is always 0: this is a reading aid.
"""
import re, statistics, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WORDS = r"""delve|delves|delving|intricate|intricately|pivotal|underscore|underscores|underscoring|testament|tapestry|
landscape|showcase|showcases|showcasing|foster|fosters|fostering|enhance|enhances|enhancing|boast|boasts|vibrant|
meticulous|meticulously|seamless|seamlessly|robust|robustly|leverage|leverages|leveraging|elevate|unlock|unlocks|realm|
crucial|crucially|game-changer|comprehensive|comprehensively|notably|importantly|insights|elucidate|unveil|harness|
harnesses|harnessing|paving|unparalleled|unravel|transformative|revolutionize|pinpoint|shedding|noteworthy|nuanced|
multifaceted|invaluable|imperative|burgeoning|compelling|culminating|discern|endeavor|facilitate|facilitates|
facilitating|formidable|foundational|grappling|poised|pressing|propelling|streamline|surpass|swiftly|underexplored|
utilize|utilizes|utilizing|utilise|utilises|methodologies|avenue|avenues|spurred|strategically|exceptional|exceptionally|
impressive|remarkable|remarkably|innovative|versatility|adept|encapsulate|necessitate|necessitates|interplay|
holistic|synergy|cutting-edge|state-of-the-art|significantly|effectively|ultimately|essentially|fundamentally|
key|critical|critically|vital|paramount|profound|profoundly"""
WORD_RE = re.compile(r"\b(" + re.sub(r"\s+", "", WORDS) + r")\b", re.I)
PHRASES = [r"serves? as", r"stands? as", r"plays? an? \w* ?role", r"not (only|just|merely)\b.{0,80}\bbut\b", r"it is worth noting",
           r"it should be noted", r"it is important to", r"at its core", r"in today'?s", r"a testament to", r"in order to",
           r"this (chapter|section) (aims|seeks)", r"due to the fact", r"a wide range of", r"a variety of", r"in the context of",
           r"with respect to", r"as well as", r"the fact that", r"sheds? light", r"paves? the way", r"rather than simply",
           r"experts? (say|agree)", r"studies show", r"it is well known", r"challenges and", r"future outlook"]
PHRASE_RE = re.compile("|".join(PHRASES), re.I)
OPENER_RE = re.compile(r"^(Moreover|Furthermore|Additionally|In addition|Overall|In conclusion|In summary|Notably|Importantly|"
                       r"Interestingly|Consequently|Thus|Hence|Therefore|However|Similarly|Taken together)\b")
ING_RE = re.compile(r",\s+(highlighting|underscoring|emphasizing|emphasising|reflecting|demonstrating|showcasing|illustrating|"
                    r"indicating|suggesting|confirming|revealing|ensuring|enabling|making|providing|contributing)\b[^.]*\.$", re.I)
TRIAD_RE = re.compile(r"\b[\w-]+, [\w-]+,? and [\w-]+\b")
ABBR = re.compile(r"\b(e\.g|i\.e|et al|Fig|Eq|Eqs|Figs|cf|vs|No|Dr|approx)\.$")


def prose(tex):
    """Strip LaTeX down to paragraphs of running prose."""
    tex = re.sub(r"(?<!\\)%.*", "", tex)
    for env in ("figure", "figure\\*", "sidewaysfigure", "table", "table\\*", "sidewaystable", "tabular", "tabularx", "longtable",
                "equation", "equation\\*", "align", "align\\*", "gather", "displaymath", "threeparttable", "landscape", "tikzpicture"):
        tex = re.sub(r"\\begin\{" + env + r"\}.*?\\end\{" + env + r"\}", "\n\n", tex, flags=re.S)
    tex = re.sub(r"\\\[.*?\\\]", " X ", tex, flags=re.S)
    tex = re.sub(r"\$[^$]*\$", "X", tex)
    tex = re.sub(r"\\todo(\[[^\]]*\])?\{(?:[^{}]|\{[^{}]*\})*\}", "", tex)
    tex = re.sub(r"\\(chapter|section|subsection|subsubsection|paragraph)\*?\{[^}]*\}", "\n\n", tex)
    tex = re.sub(r"\\(label|input|include|clearpage|FloatBarrier|begin\{[a-z*]+\}|end\{[a-z*]+\})(\{[^}]*\})?", "\n\n", tex)
    tex = re.sub(r"\\item\b(\[[^\]]*\])?", "\n\n", tex)
    tex = re.sub(r"\\(cite|citep|citet|citealp|citeauthor|citeyear)(\[[^\]]*\])*\{[^}]*\}", "CITE", tex)
    tex = re.sub(r"\\(figref|tabref|eqnref|secref|chapref|ref|eqref)\{[^}]*\}", "N", tex)
    tex = re.sub(r"\\figsref\{[^}]*\}\{[^}]*\}", "N", tex)
    tex = re.sub(r"\\(textit|textbf|emph|texttt|textsc|mbox|url)\{([^{}]*)\}", r"\2", tex)
    tex = re.sub(r"\\[a-zA-Z]+\*?", "", tex)
    tex = tex.replace("~", " ").replace("{", "").replace("}", "")
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", tex)]
    return [p for p in paras if len(p.split()) >= 8]


def sentences(par):
    out, cur = [], []
    for tok in par.split(" "):
        cur.append(tok)
        if re.search(r"[.?!]$", tok) and not ABBR.search(tok):
            out.append(" ".join(cur)); cur = []
    if cur:
        out.append(" ".join(cur))
    return [s for s in out if len(s.split()) >= 3]


def check(path, listing):
    paras = prose(open(path, encoding="utf-8").read())
    sents = [s for p in paras for s in sentences(p)]
    n = sum(len(s.split()) for s in sents) or 1
    lens = [len(s.split()) for s in sents] or [0]
    per = lambda c: round(1000 * c / n, 1)
    words = [m.group(0).lower() for s in sents for m in WORD_RE.finditer(s)]
    phr = [(m.group(0).lower(), s) for s in sents for m in PHRASE_RE.finditer(s)]
    opn = [s for s in sents if OPENER_RE.match(s)]
    ing = [s for s in sents if ING_RE.search(s)]
    dash = sum(s.count("\u2014") + s.count("---") for s in sents)
    tri = sum(len(TRIAD_RE.findall(s)) for s in sents)
    runs, i = 0, 0
    while i < len(lens) - 3:
        j = i + 1
        while j < len(lens) and abs(lens[j] - lens[i]) <= 3:
            j += 1
        if j - i >= 4:
            runs += 1
            i = j
        else:
            i += 1
    firsts = [p.split()[0] for p in paras]
    rep = sum(a == b for a, b in zip(firsts, firsts[1:]))
    mean, sd = statistics.mean(lens), statistics.pstdev(lens)
    print(f"{path.replace(chr(92), '/').split('/')[-1]:32s} {n:6d}w  words {per(len(words)):5.1f}  phrases {per(len(phr)):4.1f}  "
          f"openers {per(len(opn)):4.1f}  ingtail {len(ing):3d}  dash {dash:2d}  triads {per(tri):4.1f} | "
          f"mean {mean:4.1f} sd {sd:4.1f} burst {sd / (mean or 1):4.2f} short {100 * sum(l <= 12 for l in lens) / len(lens):3.0f}% "
          f"runs {runs:2d} repeat {rep:2d}")
    if listing:
        from collections import Counter
        print("  words:", dict(Counter(words).most_common(30)))
        print("  phrases:", dict(Counter(p for p, _ in phr).most_common(20)))
        print("  openers:", dict(Counter(s.split()[0] for s in opn).most_common(12)))
        for s in ing[:12]:
            print("  ingtail:", s[-110:])


if __name__ == "__main__":
    args = sys.argv[1:]
    listing = "--list" in args
    for f in [a for a in args if a != "--list"]:
        check(f, listing)

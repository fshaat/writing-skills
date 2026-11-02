#!/usr/bin/env python3
"""Portable manuscript voice check (SW-refresh register). Python standard library only.

Usage:  python voice_check.py [--max-words 35] [--leak LEAK.txt] [--signs AI-SIGNS.md] FILE.md [FILE.md ...]

Runs, on each Markdown file:
  VOICE  sentence length, banned tokens, first person, contractions, self-reference, comparison wording,
         "%" paired with than/against/versus, semicolons, numbers per sentence, bare numbers, figure pointers
  K1     words per heading (limit 160)
  K4     sentence statistics (target mean 18-24 words, 15 % or more of sentences of 12 words or less)
  K9     connector openers and booster/hedge words
  SIGNS  every pattern in the grep block of AI-SIGNS.md (case-insensitive)
  LEAK   optional file, one regex per line, for project-internal tags (HARD)

Exit status: 0 = no FAIL; 1 = at least one FAIL; 2 = an input or pattern error.
FAIL blocks the prose. REVIEW is read by hand and either fixed or justified. INFO is listed for reading.
Skipped as non-prose: fenced code, HTML comments, tables, headings, block quotes, inline code spans.
"""
import argparse, re, statistics, sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BANNED = re.compile(r"(--|\u2014|\bnotably\b|\bimportantly\b|\barguably\b|\bit is worth noting\b|\bnot only\b|"
                    r"\bsomewhat\b|\bfairly\b|\bquite\b|\brelatively\b)", re.I)
FIRST = re.compile(r"\b(I|my|it's|don't|can't|won't|isn't|doesn't)\b")
BOOST = re.compile(r"\b(novel|robust|powerful|comprehensive|cutting-edge|significantly|clearly|likely|probably|suggests?)\b", re.I)
CONNECT = re.compile(r"^\s*(Furthermore|Moreover|Additionally|In addition|Notably|Importantly|Interestingly)\b")
SELFREF = [re.compile(p, re.I) for p in (
    r"\b(this paper|this work)\s+(does not claim|should|must|never|claims)\b", r"\bthe reader\b", r"\breferee\b",
    r"\bframing\b", r"\[COMMITMENT\]", r"\bthe register\b", r"\bwe are careful to\b", r"\bmust be stated at the outset\b",
    r"\bnever crossed\b", r"\bthe argument\b")]
SUPER = re.compile(r"\b(beats?|outperform(s|ed)?|better than|superior to|inferior to|wins?|loses? to|we win)\b", re.I)
TIE = re.compile(r"\b(a )?(dead )?tie(d|s)?\b|\bon a par statistically\b|\bequal to (the|our)\b|\bmatches the specialist\b", re.I)
LICENSED = re.compile(r"\b(validated|robust|stable|generali[sz]es)\b", re.I)
PCT_CMP = re.compile(r"%[^.]*\b(than|against|versus|vs\.?|relative to|compared with)\b", re.I)
CMP_WORD = re.compile(r"\b(versus|vs\.?|against|relative to|compared with|than|trails|improves|at par)\b", re.I)
REFNUM = re.compile(r"\b(Fig\.?|Figure|Table|Section|Sec\.|Eq\.?|Equation|Algorithm)s?\s?S?\d+(?:\.\d+)*[a-z]?", re.I)
FIGREF = re.compile(r"\bFig(?:ure)?s?\.? ?S?\d+[a-z]?(?:\s*(?:and|,|-|\u2013)\s*S?\d+[a-z]?)*", re.I)
FORMULA = re.compile(r"\b(?:n-|i-)?(?=[A-Za-z]*\d)(?:[A-Z][a-z]?\d*)+\b")
YEAR = re.compile(r"\(\s*(18|19|20)\d\d[a-z]?\s*\)|\b(18|19|20)\d\d\b|\[\d+(?:[,\-\u2013]\s*\d+)*\]")
NUM = re.compile(r"\d+\.?\d*%?")
UNIT = re.compile(r"(%|\bK\b|\bMPa\b|\bkPa\b|\bbar\b|\batm\b|\bmol\b|\bkg\b|\u00b0C|\bpp\b|\bpoints?\b|\brows?\b|\bsources?\b|"
                  r"\bcampaigns?\b|\bfolds?\b|\bwords?\b|\bh\b|\bmin\b|\bs\b|\bparameters?\b|\bcoefficients?\b|\bterms?\b|"
                  r"\bcells?\b|\bfiles?\b|\bsamples?\b|\bmodels?\b|\bstudies\b|\bpapers?\b|\bitems?\b|\bpercent\b|"
                  r"\bdays?\b|\byears?\b|\bmD\b|\bcP\b|\bSm3\b|\bstb\b|\bwells?\b|\bcases?\b|\brealizations?\b|"
                  r"\bsteps?\b|\bintervals?\b|\bnodes?\b|\bedges?\b|\blayers?\b|\bepochs?\b|\bGPUs?\b|\d+x\b|×)")  # F12 (DEFAULT, owner to confirm): reservoir-simulation units and count nouns
COMPAR = re.compile(r"(\bversus\b|\bvs\.?\b|\bagainst\b|\brelative to\b|\bcompared with\b|\bthan\b|\bover\b|"
                    r"\bin[- ]sample\b|\bheld-out\b|\bfrom\b.*\bto\b)", re.I)
SENT = re.compile(r"[^.!?]+[.!?]+")
MARK = re.compile(r"^\s*(?:\d+[.)]|[-*+])\s+")
EQ_OPEN = re.compile(r"(\$\$|\\begin\{equation\}|\\\[)")
EQ_CLOSE = re.compile(r"(\$\$|\\end\{equation\}|\\\])")
TITLECASE = re.compile(r"^#+\s+(?:[A-Z][a-z]+\s+){2,}[A-Z][a-z]+")


def pcre(p):
    """Turn a grep -P pattern into a Python pattern."""
    return re.sub(r"\\x\{([0-9A-Fa-f]+)\}", lambda m: chr(int(m.group(1), 16)), p)


def lines_of(text):
    out, code, com = [], False, False
    for n, line in enumerate(text.splitlines(), 1):
        if com:
            if "-->" in line:
                com, line = False, line.split("-->", 1)[1]
            else:
                continue
        if "<!--" in line and "-->" not in line.split("<!--", 1)[1]:
            line, com = line.split("<!--", 1)[0], True
        line = re.sub(r"<!--.*?-->", "", line)
        s = line.strip()
        if s.startswith("```"):
            code = not code
            continue
        if code or not s:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        s = line.strip()
        if not s or s.startswith(">") or set(s) <= set("-*_ |:"):
            continue
        out.append((n, line, not s.startswith(("|", "#"))))
    return out


def sentences(par):
    t = re.sub(r"\b(Fig|Figs|Eq|Eqs|Sec|vs|et al|Table|cf|e\.g|i\.e|Ref|No|Vol)\.", lambda m: m.group(0).replace(".", "\x00"), par)
    t = re.sub(r"(\d)\.(\d)", "\\1\x00\\2", t)
    return [s.strip().replace("\x00", ".") for s in SENT.findall(t) if s.strip()]


def load_signs(path):
    txt = Path(path).read_text(encoding="utf-8")
    m = re.search(r"^## Grep block.*?^```\n(.*?)^```", txt, re.S | re.M)
    if not m:
        sys.exit("ERROR: no grep block found in " + str(path))
    pats = []
    for ln in m.group(1).splitlines():
        if not ln.strip() or "<<FILL" in ln:
            continue
        ln = re.sub(r"^-P ", "", ln)
        try:
            pats.append((ln, re.compile(pcre(ln), re.I)))
        except re.error as e:
            sys.exit("ERROR: pattern does not compile: %s (%s)" % (ln, e))
    return pats


def check(path, maxw, signs, leaks):
    text = re.sub(r"<!--.*?-->", "", Path(path).read_text(encoding="utf-8"), flags=re.S)
    fails, reviews, infos = [], [], []
    ls = lines_of(text)
    prose = [(n, MARK.sub("", l), bool(MARK.match(l))) for n, l, p in ls if p]
    paras, buf, prev, start = [], [], None, 0
    for n, l, newitem in prose:
        if prev is not None and (n != prev + 1 or newitem) and buf:
            paras.append((start, " ".join(buf)))
            buf = []
        if not buf:
            start = n
        buf.append(l.strip())
        prev = n
    if buf:
        paras.append((start, " ".join(buf)))
    counts = []
    conn = 0
    for start, par in paras:
        ss = sentences(par)
        if len(ss) > 7:
            reviews.append(("K5", start, "paragraph of %d sentences (limit 7, norm 4 or fewer)" % len(ss)))
        for s in ss:
            w = len(s.split())
            counts.append(w)
            if w > maxw:
                fails.append(("C1", start, "%d words: %s" % (w, s[:80])))
            if CONNECT.search(s):
                conn += 1
            if ";" in s:
                reviews.append(("S8", start, "semicolon in prose (split into two sentences): " + s[:80]))
            if PCT_CMP.search(s):
                fails.append(("D11", start, "percent paired with than/against/versus: " + s[:80]))
            elif CMP_WORD.search(s) and "%" in s:
                infos.append(("C7", start, "comparison sentence, confirm both sides, same rows, exposure: " + s[:80]))
            st = FORMULA.sub(" ", YEAR.sub(" ", REFNUM.sub(" ", s)))
            nn = len(NUM.findall(st))
            if nn > 2:
                reviews.append(("N", start, "%d numbers in one sentence (default one, two at most): %s" % (nn, s[:80])))
            if NUM.search(st) and not (UNIT.search(st) or COMPAR.search(st)):
                reviews.append(("C3", start, "number without unit or comparator: " + s[:80]))
            if FIGREF.search(s):
                rest = FORMULA.sub(" ", REFNUM.sub(" ", FIGREF.sub(" ", s)))
                if not NUM.search(rest):
                    reviews.append(("C5", start, "figure pointer without a number in its sentence: " + s[:80]))
    for n, l, p in ls:
        for m in BANNED.finditer(l):
            fails.append(("C2", n, "%s: %s" % (m.group(0), l.strip()[:80])))
        for m in FIRST.finditer(l):
            fails.append(("C2", n, "%s: %s" % (m.group(0), l.strip()[:80])))
        for m in BOOST.finditer(l):
            reviews.append(("K9", n, "%s (boosters and vague hedges stay out unless tied to a number or a condition): %s" % (m.group(0), l.strip()[:60])))
        for rx in SELFREF:
            for m in rx.finditer(l):
                fails.append(("C6", n, "%s: %s" % (m.group(0), l.strip()[:80])))
        for m in SUPER.finditer(l):
            fails.append(("C7", n, "%s: %s" % (m.group(0), l.strip()[:80])))
        for m in TIE.finditer(l):
            fails.append(("C7", n, "tie rendering %s: %s" % (m.group(0), l.strip()[:80])))
        for m in LICENSED.finditer(l):
            reviews.append(("C7", n, "%s needs a licence from the author: %s" % (m.group(0), l.strip()[:60])))
        if TITLECASE.search(l):
            reviews.append(("S15", n, "heading may be Title Case (use sentence case): " + l.strip()[:60]))
    raw = text.splitlines()
    i = 0
    code = False
    while i < len(raw):
        s = raw[i].strip()
        if s.startswith("```"):
            code = not code
        elif not code and EQ_OPEN.search(s):
            j = i
            single = s.count("$$") >= 2 or "\\end" in s or "\\]" in s
            if not single:
                j = i + 1
                while j < len(raw) and not EQ_CLOSE.search(raw[j]):
                    j += 1
            k = j + 1
            while k < len(raw) and not raw[k].strip():
                k += 1
            gloss = raw[k].strip() if k < len(raw) else ""
            if not re.search(r"\bwhere\b|\bsymbols? (are|were) defined\b", gloss, re.I):
                fails.append(("C4", i + 1, "display equation not followed by a where-gloss: " + repr(gloss[:50])))
            prevtxt = next((raw[q].strip() for q in range(i - 1, -1, -1) if raw[q].strip()), "")
            if not prevtxt.endswith(":"):
                reviews.append(("K7", i + 1, "display equation not introduced by a colon: " + repr(prevtxt[-50:])))
            i = j
        i += 1
    for n, line in enumerate(text.splitlines(), 1):
        for pat, rx in signs:
            if rx.search(line):
                reviews.append(("SIGN", n, "%s :: %s" % (pat[:50], line.strip()[:70])))
        for pat, rx in leaks:
            if rx.search(line):
                fails.append(("LEAK", n, "%s :: %s" % (pat[:40], line.strip()[:70])))
    words = len(text.split())
    heads = len(re.findall(r"^#{1,4} ", text, re.M))
    k1 = words / heads if heads else None
    mean = statistics.fmean(counts) if counts else 0
    short = 100 * sum(1 for c in counts if c <= 12) / len(counts) if counts else 0
    over = sum(1 for c in counts if c > maxw)
    if k1 and k1 > 160:
        reviews.append(("K1", 0, "%.0f words per heading (limit 160)" % k1))
    if counts and not (18 <= mean <= 24):
        reviews.append(("K4", 0, "mean sentence length %.1f words (target 18-24)" % mean))
    if counts and short < 15:
        reviews.append(("K4", 0, "%.0f %% of sentences have 12 words or less (target 15 %% or more)" % short))
    if counts and 100 * conn / len(counts) > 6:
        reviews.append(("K9", 0, "connector openers %d of %d sentences (limit 6 %%)" % (conn, len(counts))))
    print("== %s: %s" % (path, "FAIL" if fails else "no FAIL"))
    print("   words %d, headings %d, words per heading %s; sentences %d, mean %.1f, %.0f %% short, %d over %d words, connector openers %d"
          % (words, heads, ("%.0f" % k1) if k1 else "n/a", len(counts), mean, short, over, maxw, conn))
    for lvl, rows in (("FAIL", fails), ("REVIEW", reviews), ("INFO", infos)):
        for chk, n, d in sorted(rows, key=lambda r: (r[1], r[0])):
            print("   %-6s %-5s L%-4d %s" % (lvl, chk, n, d))
    print("   totals: FAIL %d  REVIEW %d  INFO %d" % (len(fails), len(reviews), len(infos)))
    return len(fails)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--max-words", type=int, default=35)
    ap.add_argument("--signs", default=None, help="path to AI-SIGNS.md (default: found in the paper-voice folder)")
    ap.add_argument("--leak", default=None)
    a = ap.parse_args()
    here = Path(__file__).resolve().parent
    cands = [Path(a.signs)] if a.signs else [here.parent / "AI-SIGNS.md"]
    found = next((p for p in cands if p.is_file()), None)
    if found is None:
        print("ERROR: AI-SIGNS.md not found; pass --signs PATH", file=sys.stderr)
        return 2
    signs = load_signs(found)
    leaks = []
    if a.leak:
        for ln in Path(a.leak).read_text(encoding="utf-8").splitlines():
            if ln.strip() and not ln.startswith("#"):
                leaks.append((ln, re.compile(pcre(ln), re.I)))
    bad = 0
    for f in a.files:
        if not Path(f).is_file():
            print("ERROR: no such file " + f, file=sys.stderr)
            return 2
        bad += check(f, a.max_words, signs, leaks)
    print("EXIT %d" % (1 if bad else 0))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

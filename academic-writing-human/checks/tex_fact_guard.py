#!/usr/bin/env python3
"""Fact guard for a rewritten LaTeX file: what changed between OLD and NEW? Standard library only.

Usage:  python -I tex_fact_guard.py OLD.tex NEW.tex

Compares, as multisets, the items a language edit must not lose or invent:
  numbers (with decimals, in text and math), \\cite keys, \\label, \\ref-style targets, \\includegraphics files, \\todo count.
Every item listed as LOST or NEW must be explained by an intended change (for example an update from the journal).
Exit status: 0 when both multisets match, 1 when anything differs.
"""
import re, sys
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def strip(t):
    return re.sub(r"(?<!\\)%.*", "", t)


def items(t):
    t = strip(t)
    cites = [k.strip() for g in re.findall(r"\\cite\w*(?:\[[^\]]*\])*\{([^}]*)\}", t) for k in g.split(",")]
    labels = re.findall(r"\\label\{([^}]*)\}", t)
    refs = re.findall(r"\\(?:figref|tabref|eqnref|secref|chapref|ref|eqref)\{([^}]*)\}", t)
    refs += [x for g in re.findall(r"\\figsref\{([^}]*)\}\{([^}]*)\}", t) for x in g]
    figs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", t)
    # numbers: drop command arguments that hold names, keep what the reader sees
    body = re.sub(r"\\(cite\w*|label|figref|tabref|eqnref|secref|chapref|ref|eqref|figsref|includegraphics|input|url|href)(\[[^\]]*\])*(\{[^}]*\})+", " ", t)
    body = re.sub(r"\\(begin|end)\{[^}]*\}", " ", body)
    body = re.sub(r"\\[a-zA-Z]+\[[^\]]*\]", " ", body)
    nums = re.findall(r"(?<![A-Za-z_\\])\d[\d,]*(?:\.\d+)?", body)
    nums = [n.rstrip(",") for n in nums]
    return dict(numbers=Counter(nums), cites=Counter(cites), labels=Counter(labels), refs=Counter(refs), figures=Counter(figs),
                todos=Counter({"todo": len(re.findall(r"\\todo\b", t))}))


old, new = (items(open(p, encoding="utf-8").read()) for p in sys.argv[1:3])
bad = 0
for k in old:
    lost, added = old[k] - new[k], new[k] - old[k]
    if lost or added:
        bad = 1
        print(f"{k}: LOST {dict(lost)}\n{' ' * len(k)}  NEW  {dict(added)}")
print("fact guard:", "differences above" if bad else "identical")
sys.exit(bad)

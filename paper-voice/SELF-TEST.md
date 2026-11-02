# SELF-TEST

Write the paragraph below to a file `selftest-bad.md`. It is deliberately full of AI signs. Then do three things.

1. Run `python .claude/skills/paper-voice/checks/voice_check.py selftest-bad.md`. It must exit with status 1, and the output must
   show FAIL lines for the em dash, "not only", "outperforms", "novel", the 35-word ceiling and the contraction, and
   REVIEW lines from the AI-signs grep block. If it does not, the check is broken: tell the author and do not continue.
2. Rewrite the paragraph into the SW-refresh register, in a file `selftest-good.md`. Use only facts in the paragraph.
   Where a number is missing, write `<n>` as a placeholder. Fix each hit by rewriting the sentence to state the fact
   and its number, never by swapping in a synonym. Use a plain heading in sentence case, short sentences, no list
   unless there are 2 to 5 parallel items, and end on a number.
3. Run the check on `selftest-good.md`. It must exit 0 with no FAIL. Read every REVIEW line and fix or justify it.
   Show the author both files and both outputs.

The bad paragraph (constructed; the topic is invented so no facts are at stake):

```
## Results And Discussion

Furthermore, our novel framework stands as a testament to the crucial role of robust modelling — highlighting its
significant potential and ensuring reliable predictions across a rich tapestry of conditions. It's not only a
calibration tool; it's a paradigm shift for the field. The new model clearly outperforms the previous approach, which
is likely due to its intricate treatment of the underlying physics, and it can be used for a wide range of
applications, and the average error is 4.2 which is relatively small compared to what experts argue is typical. In
conclusion, this work paves the way for future research and underscores the importance of continued investigation.
```

Expected from the check on the bad file (exit status 1): FAIL lines for C1 (a sentence of 48 words), C2 (the em dash, "not only", the contraction "It's", "relatively") and C7 ("outperforms"); REVIEW lines for the Title Case heading, the semicolon, the boosters (novel, robust, clearly, likely), and the AI-signs patterns (stands as, testament, highlighting, ensuring, rich, intricate, "experts argue", "underscores", "in conclusion"). The number 4.2 has no unit: the rewrite must give it one or mark it `<n>`.

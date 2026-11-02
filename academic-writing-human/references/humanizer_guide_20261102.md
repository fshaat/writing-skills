# The Humanizer Setup Guide: what this skill took from it

Source: "The Humanizer Setup Guide", a Google Doc shared by the owner on 2026-11-02, no author shown.
https://docs.google.com/document/u/0/d/1hqQzQYOyBVXvuohXotVM3ZzokhCv-xrMJI8tgjZjPvA/mobilebasic

The guide is written for emails, LinkedIn posts and About pages. Its claims (detector statistics, star counts, blind tests) are
the guide's own and were not checked against their sources, except where stated. It points to `blader/humanizer` on GitHub.
That third-party skill was not installed.

## Taken

- Detectors measure predictability, not authorship, and none can promise a score. The guide itself says so.
- "Cut the adjective, add a fact."
- Rewrite from the meaning up, not word by word. One sign alone means little; several in one paragraph is the signal.
- Facts locked: never invent a detail. Ask for it, or leave it out.
- Write in two passes: content first, then voice.
- Mix sentence lengths. Cut stock transitions. Add details only the author knows. State a view.
- Words added to `checks/tex_style_check.py`: boast, vibrant, elevate, unlock, game-changer, tapestry, testament, foster, showcase.
- Structures added to the check: "serves as", "stands as", "not just X but Y", "-ing" fake-depth tails, template wrap-ups.

## Not taken, and why

- Contractions, friendly tone and "talk to a client you like": wrong register for a thesis.
- Banning all en dashes: numeric ranges need them. Em dashes stay banned.
- Testing on gptzero, zerogpt or quillbot as the success measure: scores are unreliable, and tuning to them damages the prose.
  The owner may test on their own; this skill does not optimize for it.
- Using it where rules restrict AI. The guide warns against this too. HBKU requires AI use to be disclosed on the Declaration
  page, so the disclosure stays in the thesis.

# Writing skills

Two skills for writing papers, thesis chapters, reports and reviewer responses so the text is specific, precise and reads as written by a person. They are instructions for Claude Code (or any assistant), plus checking scripts.

| Skill | What it does |
|---|---|
| `paper-voice/` | Sentence register: short numbered sections, short declarative sentences, plain verbs, a closing number on every results section, and a checklist of AI-writing signs. Run `paper-voice/checks/voice_check.py` on any prose before using it. |
| `academic-writing-human/` | Structure and honesty: thesis-chapter and section-by-section structure, citation verification, a revision procedure, and a second list of AI-style tells. Run `academic-writing-human/checks/tex_style_check.py` and `tex_fact_guard.py` on LaTeX. |

`paper-voice` takes precedence on sentence register when the two disagree.

## Use with Claude Code

Copy both folders into your project's `.claude/skills/` (or `~/.claude/skills/` for every project). Claude Code then lists them and applies them when you ask for drafting or revision; you can also invoke them by name.

## Use without Claude Code

Open `paper-voice/SKILL.md` and `RULES.md`, and `academic-writing-human/SKILL.md`, and follow them as a checklist. The scripts need only Python 3:

```
python paper-voice/checks/voice_check.py your_text.md
python academic-writing-human/checks/tex_style_check.py chapter.tex
```

## Scope

These skills make writing clear, specific and checkable. They do not hide how a text was produced, and they are not a tool for defeating detectors; good writing is the point.

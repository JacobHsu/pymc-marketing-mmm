# PyMC-Marketing — Claude Code Instructions

## Environment

- Activate conda env `pymc-marketing-dev` before running any commands.
- Run `pre-commit` every time you create or modify a file.
- Temporary or test scripts that are not meant to be committed should be created in the `sandbox/` folder.

## Documentation Rule

Every time a code change is verified to work, **immediately update the relevant docs**:

- Bug fix or workaround discovered → add to the relevant README `## 常見問題` section
- New required step discovered (e.g., `conda install gxx`) → add to the setup/startup section
- Default value changed → update the description text to match
- New parameter added → add to the parameter table and summary

The target doc files for the Streamlit demo are:
- `sandbox/streamlit_demo/README.zh-CN.md` — setup, startup, FAQ
- Page files (`pages/*.py`) — inline `st.markdown` descriptions

Do not wait until the end of a conversation. Update docs **in the same step** as the code change.

## Skills (shared with Cursor)

Domain knowledge and workflow skills live in `.cursor/skills/`. Read the relevant
skill file **before** starting work in that domain.

| Skill | When to read | Entry file |
|---|---|---|
| **mmm-modeling** | Building, fitting, diagnosing, or optimizing Media Mix Models with PyMC-Marketing | `.cursor/skills/mmm-modeling/SKILL.md` (references in `references/` subdirectory) |
| **code-best-practice** | Writing or reviewing PyMC-Marketing code (style, typing, docstrings, PyTensor, testing) | `.cursor/skills/code-best-practice/SKILL.md` |
| **research** | Structuring a research task before implementation | `.cursor/skills/research/SKILL.md` |
| **make-plan** | Creating an implementation plan from research | `.cursor/skills/make-plan/SKILL.md` |
| **implement** | Implementing code from a plan | `.cursor/skills/implement/SKILL.md` |
| **commit** | Creating git commits for session changes | `.cursor/skills/commit/SKILL.md` |

### How to use skills

1. When a task matches a skill's trigger (the "When to read" column), read the
   entry file in full.
2. The entry file may reference additional files (e.g., `references/model_fit.md`).
   Read those as needed for the specific sub-topic.
3. Follow the patterns and constraints described in the skill.

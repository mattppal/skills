---
name: skill-creator
description: Create or update agent skills with proper SKILL.md structure, frontmatter, and best practices. Use when building new private skills for this repository and the vercel-labs/skills CLI.
---

# Skill Creator

Create well-structured agent skills that work with the open `skills` CLI and install cleanly into supported agents.

## Skill Structure

Every skill requires this directory structure:

```
skills/
└── skill-name/
    ├── SKILL.md          # Required - main skill definition
    ├── references/       # Optional - docs loaded only when needed
    ├── scripts/          # Optional - deterministic helper scripts
    └── assets/           # Optional - templates or files used in outputs
```

## SKILL.md Format

```markdown
---
name: skill-name
description: Brief description of what the skill does and when to use it. Max 1024 chars.
---

# Skill Title

[Main instructions for the agent when this skill is activated]
```

### Frontmatter Requirements

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Lowercase letters, numbers, hyphens only. Max 64 chars. |
| `description` | Yes | What it does + when to use it. Max 1024 chars. |
| `metadata.internal` | No | Set `true` only for skills hidden from normal discovery. |

## Writing Effective Descriptions

The description determines when an agent activates the skill. Be specific:

**Good descriptions:**
- "Transform changelogs and user showcases into Twitter posts. Use for social media content with casual voice."
- "Design evidence-based powerlifting programs. Use for strength training, workout planning, progressive overload."

**Bad descriptions:**
- "Helps with content" (too vague)
- "For writing" (won't trigger reliably)

Include:
- Specific functionality and capabilities
- Trigger terms users would mention
- When Claude should activate it

## Skill Content Best Practices

### Structure
```markdown
# Skill Title

Brief context paragraph.

## Context
Who/what this skill represents, target audience.

## [Main Sections]
Core instructions, templates, guidelines.

## Examples
Input/output examples when helpful.

## Quality Checklist
Verification criteria for outputs.
```

### Content Guidelines
- Be specific and actionable
- Include templates and examples
- Define clear output formats
- Add quality checklists when appropriate
- Reference supporting files only when they are needed
- Keep `SKILL.md` concise; move large examples or domain references into `references/`

## Skill Locations

Use `skills/<skill-name>/` as the canonical source layout in this repo. The `skills` CLI installs from there into each agent's preferred directory, such as `~/.codex/skills/` for Codex or `~/.claude/skills/` for Claude Code.

## Creating a New Skill

1. **Identify the need**: What task should agents handle automatically?
2. **Define triggers**: What words/contexts should activate it?
3. **Create directory**: `mkdir -p skills/skill-name`
4. **Write SKILL.md**: Include frontmatter + instructions
5. **Add supporting files**: Optional reference docs
6. **List with CLI**: Run `npx skills add . --list`
7. **Install locally**: Run `npx skills add . --global --agent codex --skill skill-name`

## Example: Minimal Skill

```markdown
---
name: code-review
description: Review code for bugs, security issues, and best practices. Use when asked to review or audit code.
---

# Code Review Skill

Review code systematically for:

## Checklist
- [ ] Logic errors and edge cases
- [ ] Security vulnerabilities (injection, auth, etc.)
- [ ] Performance concerns
- [ ] Code style and readability
- [ ] Error handling

## Output Format
Provide findings as:
1. **Critical**: Must fix before merge
2. **Important**: Should fix soon
3. **Suggestions**: Nice to have improvements
```

## Common Patterns

### Voice/Persona Skills
Define character, tone, writing style for consistent outputs.

### Task-Specific Skills
Step-by-step instructions for specific workflows.

### Template Skills
Output formats, document structures, boilerplate.

### Analysis Skills
Checklists, criteria, evaluation frameworks.

# Matt Palmer's Agent Skills

A private collection of agent skills for content creation, course development, travel planning, and personal productivity.

This repo is formatted for the open `skills` CLI from [`vercel-labs/skills`](https://github.com/vercel-labs/skills). Skills live in `skills/<skill-name>/SKILL.md`, which lets the CLI install them into Claude Code, Codex, Cursor, and other supported agents.

## Install

From a private GitHub repo, use an SSH URL so your local Git credentials handle authentication:

```bash
npx skills add git@github.com:<owner>/<repo>.git --global
```

Install into a specific agent:

```bash
npx skills add git@github.com:<owner>/<repo>.git --global --agent codex
npx skills add git@github.com:<owner>/<repo>.git --global --agent claude-code
```

List available skills before installing:

```bash
npx skills add git@github.com:<owner>/<repo>.git --list
```

Install only one skill:

```bash
npx skills add git@github.com:<owner>/<repo>.git --global --skill brand-voice
```

For local testing from this checkout:

```bash
npx skills add . --list
npx skills add . --global --agent codex --skill brand-voice
```

## What Are Agent Skills?

Skills are reusable instruction packages that agents automatically activate based on the `name` and `description` in `SKILL.md` frontmatter. Unlike slash commands, skills are model-invoked: the agent decides when to use them based on the request and the skill description.

## Available Skills

| Skill | Description | Use Case |
|-------|-------------|----------|
| `brand-voice` | Apply Matt Palmer's voice, tone, and content pillars | Any writing needing authentic brand voice |
| `twitter-content` | Transform changelogs and showcases into Twitter posts | Social media content creation |
| `blog-writing` | Write blog posts in formal voice with proper structure | Tech blogs, tutorials, professional content |
| `video-to-content` | Convert video/podcast transcripts to various formats | Content repurposing |
| `course-builder` | Create educational course content and lesson plans | Online courses, workshops |
| `trip-planner` | Build detailed travel itineraries | Vacation planning |
| `strength-program` | Design evidence-based training programs | Powerlifting/hypertrophy programming |
| `technical-writing-revision` | Rewrite technical writing for clarity, structure, and precision | Docs, changelogs, blog posts, UI copy |

## Skill Structure

Each skill follows this structure:

```
skills/
├── brand-voice/
│   ├── SKILL.md          # Main skill definition
│   └── style-reference.md # Supporting documentation
├── twitter-content/
│   └── SKILL.md
├── blog-writing/
│   └── SKILL.md
└── ...
```

## Core Framework

All content skills inherit from the brand-voice foundation:

**Mission**: Empower ambitious individuals with actionable, evidence-based strategies for growth through accessible, secure AI-assisted development.

**Content Pillars**:
- Educational Excellence
- Actionable Strategies
- Evidence-Based
- Inspirational
- Community

**Voice Modes**:
- **Formal**: Blog posts, documentation, professional content
- **Casual**: Twitter, social media, community engagement
- **Authentic**: Personal stories, behind-the-scenes

**Quality Standard**: True → Relevant → Interesting → Clear

## Usage Examples

### Writing a blog post
Simply ask Claude to write a blog post—it will automatically activate the `blog-writing` skill:
```
Write a blog post about getting started with AI-assisted development
```

### Creating Twitter content
Provide a changelog or update, and Claude will use `twitter-content`:
```
Turn this changelog into a Twitter post:
- New dark mode feature
- Performance improvements
- Bug fixes
```

### Planning a trip
Describe your destination and preferences:
```
Plan a 5-day trip to Japan focused on hiking and food
```

## Archive

Original prompts are preserved in the `archive/` directory for reference. The skills consolidate and improve upon these individual prompts.

## Add or Update Skills

To add a new skill:

1. Create a new directory in `skills/`
2. Add a `SKILL.md` file with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Brief description of what this skill does and when to use it
   ---
   ```
3. Include clear instructions in the markdown body
4. Optionally add supporting files such as `references/`, `scripts/`, or assets

## Resources

- [`vercel-labs/skills`](https://github.com/vercel-labs/skills)
- [Vercel Agent Skills Repository](https://github.com/vercel-labs/agent-skills)

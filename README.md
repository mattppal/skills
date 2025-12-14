# Matt Palmer's Claude Skills

A collection of Claude Code skills for content creation, course development, and personal productivity.

## What Are Skills?

Skills are reusable prompt packages that Claude automatically activates based on context. Unlike slash commands (which you invoke manually), skills are **model-invoked**—Claude decides when to use them based on your request and the skill's description.

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

## Installation

These skills are located in `.claude/skills/`. To use them:

1. **Project-level**: Skills in this repo are automatically available when working in this directory
2. **Global**: Copy skill folders to `~/.claude/skills/` for cross-project availability

## Skill Structure

Each skill follows this structure:

```
.claude/skills/
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

## Contributing

To add a new skill:

1. Create a new directory in `.claude/skills/`
2. Add a `SKILL.md` file with YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Brief description (max 1024 chars)
   ---
   ```
3. Include clear instructions in the markdown body
4. Optionally add supporting files (examples, references)

## Resources

- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Creating Custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

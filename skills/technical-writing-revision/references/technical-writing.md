# Technical Writing Revision for Honolulu

Use this reference when rewriting docs, product copy, changelog entries, blog posts, and UI text in this repo.

## Goal

Rewrite text until structure matches meaning and readers can understand it without effort.

For this repo, that means clarity first, but not at the expense of technical accuracy. A technically precise sentence that reads awkwardly should be improved. A smooth sentence that weakens meaning should be rejected.

## Core Loop

Apply this loop until no meaningful improvement remains:

1. Identify the main problem.
2. Rewrite for clarity and structure.
3. Evaluate from the reader's point of view.
4. Repeat if the sentence, paragraph, or section still slows understanding.

## Sentence-Level Rules

### Prefer clear actors and verbs

- Put the main actor in the subject position when possible.
- Express the main action as a verb, not as a noun hidden in a phrase.
- Prefer `Conductor creates a workspace` over `workspace creation happens in Conductor`.

### Reduce drag before the main verb

- Shorten long openings.
- Remove interruptions between the subject and verb.
- Move secondary detail later in the sentence unless it is required up front.

### Control information flow

- Start with context the reader already has.
- End on the new, important, or difficult idea.
- Make each sentence connect cleanly to the one before it.

### Cut filler

- Remove phrases that add tone but not meaning.
- Replace vague wording with direct wording.
- Avoid stacked qualifiers when one precise term will do.

## Technical-Writing Adjustments

This skill is not a generic prose polisher. Apply these rules for technical content:

### Preserve technical meaning

- Do not simplify away constraints, caveats, or system behavior.
- Keep exact names for commands, routes, environment variables, UI labels, files, branches, and configuration keys.
- Verify before changing product claims, version references, or capability statements.

### Surface task-critical details

- Put prerequisites before steps that depend on them.
- Put the expected outcome near the action that produces it.
- State scope and limits explicitly when a reader could misapply the instruction.

### Prefer concrete instruction

- Use imperative phrasing for procedures.
- Use descriptive labels for reference material.
- If a page gives steps, make the sequence obvious.
- If a page describes options, organize by concept or field rather than by loose narrative flow.

### Keep examples executable

- Preserve code blocks, commands, JSON, and shell snippets exactly unless you are fixing them.
- Introduce examples with a short frame that explains when to use them.
- Do not bury key examples under long explanatory lead-ins.

## Paragraph and Section Rules

### Paragraphs

- Give each paragraph one clear job.
- Open with the point or transition the paragraph exists to deliver.
- Group sentences that belong together operationally or conceptually.

### Sections

- Start sections with a short frame that tells the reader what follows.
- Prefer informative headings over clever headings.
- Keep headings parallel within a page when possible.

### Document structure

- Make the first screen answer the reader's immediate question.
- For docs pages, surface task, concept, or feature scope early.
- For changelog entries, separate improvements from fixes and keep bullets specific.
- For blog posts, preserve voice, but keep sentences concrete and readable.

## Formatting Rules for This Repo

### MDX docs

- Keep titles short and descriptive.
- Use `##` and `###` headings to break long pages into scan-friendly chunks.
- Use numbered lists for sequences and bullets for unordered facts.
- Wrap commands, env vars, paths, filenames, route segments, and code identifiers in backticks.
- Use fenced code blocks with the correct language when possible.
- Keep link text descriptive enough to scan out of context.

### Changelog

- Keep the intro short.
- Use concrete bullets.
- Start bullets with a meaningful verb or change description.
- Avoid burying the user-visible effect.
- Separate improvements and fixes cleanly.

### UI copy

- Keep labels short.
- Make buttons and empty states action-oriented.
- Put the most important word early.
- Avoid internal jargon unless users already see it in the product.

## Failure Modes to Avoid

- Hiding the actor in abstract language
- Burying the action in nouns
- Front-loading too much context before the main point
- Mixing unrelated goals in the same paragraph or section
- Ending sentences on weak, empty, or generic words
- Replacing precise technical terms with softer but less accurate language
- Turning reference or procedural writing into marketing copy
- Over-formatting simple content

## Repo-Specific Guidance

- Pair with `conductor-product-context` when wording could affect product positioning.
- Pair with `conductor-marketing-context` when text describes implementation or workflow behavior.
- Pair with `diataxis-docs-architecture` when deciding whether content belongs in tutorial, how-to, reference, or explanation.
- Treat legal text as out of scope unless the user explicitly asks for editing there.

## Quick Checklist

- Can a reader identify who did what on the first pass?
- Are prerequisites and constraints in the right place?
- Does each paragraph have one job?
- Does the section heading prepare the reader for what follows?
- Are commands, paths, and labels preserved exactly?
- Is formatting helping the reader scan, not just decorating the page?
- Is the revised text more direct without losing technical meaning?

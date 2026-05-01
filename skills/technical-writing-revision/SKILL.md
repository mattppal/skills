---
name: technical-writing-revision
description: Rewrite technical writing in this repo so readers understand it on the first pass. Use when improving docs, MDX pages, changelog entries, blog posts, UI copy, onboarding text, help text, headings, lists, or formatting without changing the underlying meaning or product behavior.
---

# Technical Writing Revision

Use this skill to improve technical writing and formatting in the repo while preserving meaning, correctness, and product truth.

## Workflow

1. Read `references/technical-writing.md`.
2. Identify the document type before editing: tutorial, how-to, reference, explanation, changelog, blog, or UI copy.
3. Rewrite in passes:
   - sentence clarity
   - paragraph and section structure
   - formatting and scannability
   - technical accuracy and consistency
4. Preserve commands, identifiers, paths, shortcuts, version numbers, routes, and UI labels unless they are actually wrong.
5. If the task touches product claims, use `conductor-product-context`.
6. If the task changes docs structure or page placement, use `diataxis-docs-architecture`.

## Revision Rules

- Make the actor and action easy to find.
- Prefer direct verbs over abstract noun-heavy phrasing.
- Put prerequisites, constraints, and outcomes where readers expect them.
- Keep one dominant purpose per page or section.
- Use lists, headings, code fences, and tables only when they improve scanning.
- Keep formatting consistent with existing repo MDX and changelog patterns.
- Do not rewrite technical detail into vagueness.
- Do not make copy friendlier at the cost of precision.

# Contributing

Additions are welcome. One project per pull request keeps the discussion simple.

## The bar

An entry has to be something an agent actually uses to live or work — a runtime,
a computer, a memory, a skill, a way to reach a person, an identity, a way to
pay. Papers, courses, and demo notebooks belong somewhere else.

Beyond that, an entry must be:

- **Open source**, with the licence visible in the repository.
- **Alive** — pushed to within the last year, and not archived.
- **Real** — used by people who did not write it. Stars are a weak signal, not
  the test; a small project doing something nothing else does is a better entry
  than a large one duplicating five others.

Anything that only wraps a hosted API without adding a capability an agent needs
gets declined.

## The shape of an entry

```markdown
- **[name](https://github.com/owner/repo)** — what it does for an agent, in one line. `⭐ 1.2k`
```

Write the description yourself, in plain English, saying what the project does
*for an agent*. Copied marketing lines get rewritten before merge. Twelve to
eighteen words is the target; a description that needs a comma splice is too
long.

Star counts are not maintained by hand — `python3 scripts/check.py --update` rewrites
them, and a weekly job keeps them close enough.

## Before you open the pull request

```sh
python3 scripts/check.py
```

It fails on a dead link, an archived repository, or a project that has not been
pushed to in a year. The same check runs on every pull request.

## Sections

Sections describe what an agent needs, not what a vendor sells. If your entry
does not fit one, say so in the pull request rather than forcing it — a missing
section is a useful thing to learn.

## Disclosure

This list is published by the people who build Cue OS. Cue OS appears once, in
its own section, marked as ours. Everything else is here because it earned the
line, and a pull request that removes a project which no longer meets the bar is
as welcome as one that adds a project which does.

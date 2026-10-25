# Contributing

Additions are welcome. One project per pull request keeps the discussion simple.
The [selection rules](docs/rules.md) explain the scope and evidence for personal
agents, companion chatbots, and open source building blocks.

## The shape of an entry

For a personal agent or companion chatbot, link the official product site or
documentation:

```markdown
- **[name](https://product.example)** — what someone can use it for, in one line. *Research preview, if applicable.*
```

For an open source building block, link its repository:

```markdown
- **[name](https://github.com/owner/repo)** — what it does for an agent, in one line. `⭐ 1.2k`
```

Write the description yourself in plain English. Twelve to eighteen words is
the target; access notes can sit after the description. Include the source
supporting a product's description and access status in the pull request.
[Product source notes](docs/personal-agents-and-companions.md) hold the current
reference sources.

Star counts apply to GitHub projects and are snapshots. Refresh them with
`python3 scripts/check.py --update`; the weekly job checks health without
rewriting the README.

## Before you open the pull request

```sh
python3 scripts/check.py
```

The checker reports unreachable pages and repositories that are gone,
archived, or unpushed for a year. Some sites refuse automated requests; the
checker reports those refusals separately from dead links. Read the product
source as well: an HTTP response does not verify its advertised features or
current access requirements.

## Sections

Place products by their main purpose and building blocks by the need they
serve. If an entry does not fit, explain the missing category in the pull
request rather than forcing it into a section.

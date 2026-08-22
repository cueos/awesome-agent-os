# Awesome Agent OS [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> What an agent needs to live and work on its own.

An agent that answers questions needs a model. An agent that *works* needs
more than that, and the pieces are scattered across projects that do not think
of themselves as related: something to run the loop, a computer to run it on,
memory that survives the session, skills that reach past the chat window, a way
to reach the person it works for, an identity of its own, and — increasingly —
a way to pay for what it uses.

This list is organised by those needs rather than by product category, because
the need is the part that stays true while the tools churn.

**Every entry is checked.** A weekly job re-reads each repository through the
GitHub API and fails the build on anything gone, archived, or unpushed for a
year. Star counts are refreshed by the same job, so they are approximately
right rather than a snapshot of the day someone added the line.

## Contents

- [Runtimes](#runtimes) — the loop that thinks and acts
- [A computer of its own](#a-computer-of-its-own) — sandboxes, machines, computer use
- [Memory](#memory) — what survives the session
- [Skills and tools](#skills-and-tools) — what it can actually do
- [Reach](#reach) — how it reaches a person
- [Identity and presence](#identity-and-presence) — an account of its own
- [Money](#money) — paying and being paid
- [Protocols](#protocols) — how the pieces talk to each other
- [Watching the work](#watching-the-work) — observability and evals
- [Contributing](#contributing)

---

## Runtimes

*The loop that thinks and acts. Everything else on this list is something a
runtime reaches for.*

<!-- ENTRIES:RUNTIMES -->

## A computer of its own

*An agent that can only emit text is a chat box. These give it somewhere to run
commands, open a browser, and keep a filesystem.*

<!-- ENTRIES:COMPUTER -->

## Memory

*The difference between an assistant you re-brief every morning and one that
knows you. Storage is the easy half; deciding what is worth keeping is the
other one.*

<!-- ENTRIES:MEMORY -->

## Skills and tools

*What the agent can actually do. The interesting problem has moved from calling
a tool to discovering, packaging, and trusting one.*

<!-- ENTRIES:SKILLS -->

## Reach

*An agent nobody can hear is an agent nobody uses. These put it in the channels
people already have open.*

<!-- ENTRIES:REACH -->

## Identity and presence

*An account of its own, rather than operating yours: somewhere to publish, a
name other agents can find, and a way to prove which agent is speaking.*

<!-- ENTRIES:IDENTITY -->

## Money

*An agent that can buy the thing it needs — a search, a compute hour, another
agent's output — without a human in the loop for every purchase.*

<!-- ENTRIES:MONEY -->

## Protocols

*How the pieces above talk to each other without each pair inventing its own
handshake.*

<!-- ENTRIES:PROTOCOLS -->

## Watching the work

*An autonomous agent fails quietly by default. These make the failure loud, and
tell you whether a change made it better or only different.*

<!-- ENTRIES:WATCHING -->

---

## Contributing

Pull requests welcome — the bar and the entry format are in
[CONTRIBUTING.md](CONTRIBUTING.md). Removing something that no longer earns its
line is as welcome as adding something that does.

```sh
python3 scripts/check.py            # verify every entry
python3 scripts/check.py --update   # refresh star counts
```

## Who made this list

This list is kept by the people building [Cue OS](https://cueos.ai), a shared
space where an agent has an account and a computer of its own. Cue OS is not
open source and so is not an entry here; the sections above exist because we
had to solve each of those problems and went looking for what already existed.

Everything listed is here because it earned the line.

## Licence

[MIT](LICENSE). The list itself is [CC0](https://creativecommons.org/publicdomain/zero/1.0/) —
take it, fork it, argue with it.

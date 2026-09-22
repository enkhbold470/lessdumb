# lessdumb

An agent skill that makes Claude (or any agent that reads `SKILL.md`) question
requirements and delete parts before it simplifies, speeds up or automates
anything.

It runs the 5-step design process Elon Musk described on the 2021 Starbase
tour with Tim Dodd (Everyday Astronaut), in order:

1. **Make the requirements less dumb.** Every requirement gets a person as its
   owner, including the ones that came from someone smart.
2. **Delete the part or process.** If you aren't adding back about 10% of what
   you cut, you didn't cut enough.
3. **Simplify or optimise** what survived, looking at the whole system first.
4. **Accelerate cycle time** at the bottleneck.
5. **Automate**, last, and only what has been done by hand long enough to show
   its edge cases.

Agents tend to start at step 5. In our test, asked to script a 13-step manual
deploy, Claude without the skill scripted all 13, and kept the idle celery
restart and a `redis-cli FLUSHALL` nobody could explain as opt-in flags. With
the skill it deleted both before writing the script.

## What it does

The skill writes a short review under the five steps, then acts on the smaller
plan that survives: it builds the reduced feature, deletes the dead parts as
their own change, or hands back the shorter version of your proposal. It
stops only for questions that block, and for deletions that touch money,
security, user data or destructive operations.

It starts on its own when you ask to design, simplify, refactor, automate or
review a plan, and when you type `/lessdumb`.

## Install

**Claude Code, as a plugin:**

```
/plugin marketplace add enkhbold470/lessdumb
/plugin install lessdumb@lessdumb
```

**Claude Code, by hand:**

```sh
git clone https://github.com/enkhbold470/lessdumb
cp -r lessdumb/skills/lessdumb ~/.claude/skills/
```

**Other agents:** copy `skills/lessdumb/SKILL.md` wherever your agent loads
skills or rules from. It is plain Markdown with YAML frontmatter.

## Try it

Three test prompts live in [`evals/`](evals/), with their input files:

- `exporter.py`: a small CSV exporter, plus a request for retries, YAML config
  and a plugin system.
- `release-proposal.md`: a weekly release process with a change board and a
  code freeze, aimed at incidents that came from untested migrations.
- `deploy-steps.md`: a 13-step manual deploy the user wants scripted.

Run each prompt with and without the skill and compare what gets built.
`evals/evals.json` lists the checks.

## Why one skill

[wezendy/elon-musk-algorithm-skills](https://github.com/wezendy/elon-musk-algorithm-skills)
covers the same algorithm as six skills, with a gate before each step and a
form to fill in for each. lessdumb keeps it to one skill for two reasons. Six
overlapping triggers ("optimize this", "refactor", "script this") load gated
steps into everyday requests. And the review has to obey step 2 itself: a
review longer than the thing it reviews has added parts. Several ideas here
came from that repo: moving a guarantee before deleting the code that held it,
the 25% ceiling on add-backs, targeting the bottleneck, and planning how to
undo an automation.

## Contributing

Issues and pull requests are welcome. If you change `SKILL.md`, run the three
evals before and after and say in the PR what changed in the output.

## License

[MIT](LICENSE). Not affiliated with or endorsed by Elon Musk, SpaceX or Tesla.
The five steps are his; the wording and the mistakes in this skill are mine.

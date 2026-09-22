---
name: lessdumb
description: Run the 5-step design algorithm Elon Musk describes for SpaceX, in order: 1) make the requirements less dumb, 2) delete the part or process, 3) simplify or optimise, 4) accelerate cycle time, 5) automate. Then carry out the smaller plan that survives. Use this whenever the user says "follow Musk's 5 steps", "the algorithm", "make the requirements less dumb", "delete the part", "first principles this", or asks to cut scope, simplify, de-bloat or question a spec. Also use it on your own before building a non-trivial feature, refactor or system; before optimising or speeding something up; before automating a workflow, script, pipeline, hook or CI step; and when reviewing a plan, proposal, spec, PRD or roadmap, even if the user never mentions Musk. Skip it for function-level choices like naming or error-handling style.
---

# lessdumb

Five steps, and the order is the point. Each step stops you wasting effort on
the next one. "Possibly the most common error of a smart engineer is to
optimise a thing that should not exist." So question and delete before you
simplify, simplify before you go faster, and go faster before you automate.
"If you're digging your grave, don't dig faster."

When you catch yourself optimising, speeding up or automating something, check
that it survived steps 1 and 2 first.

Existing systems get all five steps. New work (nothing built yet) mostly lives
in steps 1 to 3: step 2 becomes "default to no" on every speculative
abstraction, option and feature, and steps 4 and 5 wait until something runs.

## 1. Make the requirements less dumb

"Your requirements are definitely dumb, it does not matter who gave them to
you." Requirements from a smart person, including you a minute ago, are the
most dangerous because they get questioned least.

- List the requirements in play: the stated ones and the ones you were about
  to assume (backwards compatibility, configurability, every edge case,
  scale, a particular tech).
- Give each one an owner who is a person: the user, a named teammate, a rule
  in the repo's docs with its reason. "The spec", "the team" and "best
  practice" are not owners. No owner and no live reason makes it a deletion
  candidate.
- State the requirement at its strongest before you challenge it, then ask
  what outcome it serves. A smaller requirement often gets the same outcome.
- Some requirements only the user can loosen. Ask in one line, propose the
  less dumb version as your default, and keep going. Rules that record a past
  incident (a CLAUDE.md or AGENTS.md invariant, a postmortem) are owned
  requirements: question them out loud, never drop them silently.

## 2. Delete the part or process

Start from the core and add back only what proves necessary.

- For each part, step, file, flag, option, abstraction, dependency, check,
  approval or meeting, ask what breaks without it. "In case" is not an answer:
  "you can make 'in case' arguments for so many things."
- Delete means delete. Turning a pointless step into an opt-in flag keeps the
  part and adds a branch. If a thing has no owner and no reason, remove it and
  say how to add it back.
- Calibrate with the add-back rate. If you are not adding back at least ~10%
  of what you cut, you did not cut enough. If more than ~25% comes back, you
  cut carelessly. For each deletion, name the signal that would bring it back.
- Before deleting code, ask what it guarantees: an ordering, a check, an error
  path. If that guarantee matters and lives nowhere else, move it first. Find
  callers and run the tests; do not guess.
- Anything guarding money, security, user data or a destructive operation
  needs its owner's yes. List it as proposed instead of removing it.

## 3. Simplify or optimise

Only now, and only what survived.

- Fewer layers, special cases, parameters and representations. The plain
  version of the clever thing. No abstraction for a single use.
- Look at the whole system before optimising a part. SpaceX engineers spent
  heavily on cutting engine weight while the payload's equivalent weight went
  unexamined. Find the biggest win across the system, not in the file you
  have open.

## 4. Accelerate cycle time

Shorten the loop between a change and knowing whether it worked, at the
bottleneck. Find the slowest wait, queue or manual step and speed up that one;
gains elsewhere don't show. Name any correctness shortcut the speed-up takes.
If you can't say which direction you're accelerating in, go back to step 1.

## 5. Automate

Last. Automate only steps that survived deletion, are already simple, and have
been done by hand enough times to show their edge cases. Say what stays
manual and how to rip the automation out if it turns out wrong. At Tesla, a
lot of work went into automating how the Model 3 battery mats were made before
anyone asked what the mats were for. They damped noise that no longer needed
damping. Ask "what is this for?" once more before you script it.

## Output: review, then act

The review obeys step 2 too. Keep it short, list only real findings, and write
"nothing to change" for a step that has none. Whatever you produce should come
out smaller than what went in (fewer parts, lines, steps, dependencies or
words). If it came out bigger, say why.

```markdown
**1. Requirements**
- <requirement> → <less dumb version> (owner: <who>)
- Question for you: <only what blocks>

**2. Deleted**
- <thing>: <why it needn't exist> (add back if: <signal>)
- Needs your OK: <guarded thing>

**3. Simplified** <what got simpler; the whole-system win>

**4. Faster loop** <the bottleneck and how we'll know sooner>

**5. Automate** <what, what stays manual, how to undo; or "not yet: why">

**Net:** <before → after, e.g. 13 steps → 8, 71 lines → 58>
```

Then act on the smaller plan: build the reduced feature, make the deletions as
their own reviewable change, or write the revised shorter document. Wait only
on the questions and guarded deletions that block. For a plan or proposal,
acting means handing back the revised version.

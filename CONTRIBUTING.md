# Contributing to Open Vision

Updated: 2026-11-02.

Open Vision is investigating **Mac-hosted visionOS Simulator streaming**, not distributing Apple's operating system or claiming current headset support. Start with the [README](README.md), [agent instructions](AGENTS.md) and [workstream](docs/workstream.md).

## Choose a bounded task

Read the [product requirements](docs/product-requirements.md) and the phase gates in the workstream, then use an existing `OV-*` item or propose a clearly scoped change. Refer to its ID in the pull request. Keep unrelated changes separate; do not create a permanent architectural abstraction to solve a one-off experiment.

The workstream is the single status ledger. Update it when evidence changes. An architecture proposal, successful compilation and successful hardware test are different outcomes.

## What cloud agents can do

- Review current public documentation, APIs, upstream history and licensing.
- Add dated evidence and narrow compatibility hypotheses.
- Implement explicitly assigned portable tooling or tests.
- Prepare native changes with their build/test requirements clearly stated.

Cloud agents without an authorized Mac/headset/account operator cannot validate Xcode Simulator rendering, real Apple Account service compatibility, PICO runtime behaviour, visual comfort or end-to-end latency. Mark those tests as not run and leave a reproducible procedure for a hardware operator.

## Evidence for changes

A pull request should explain:

1. The task ID and what changed.
2. Whether findings are researched, inferred, unverified or verified by a test.
3. Commands and results, with exact relevant versions.
4. Native/hardware tests not performed.
5. Any new dependency, its reason, licence and security implications.

Never copy private logs, account identifiers, hostnames, addresses, screen contents or credentials into a public issue or pull request. Publish a sanitized result instead.

## Checks

Python 3.10+ is sufficient for the current repository:

```sh
python3 scripts/check_docs.py
```

CI runs this same check on pushes and pull requests. It checks local Markdown targets, research references, required source metadata and basic publication hygiene. It is not a security audit or a working-streamer test.

No application build exists yet. Add real build instructions alongside the first implementation; do not invent placeholder commands.

## Safety and licences

Follow [the licensing policy](docs/licensing.md). Do not execute historical injection/setup scripts or weaken host security just because a README suggests it. Any installation, private machine access or security-sensitive experiment requires explicit authorization and a recovery plan.

Original contributions are accepted under the repository's [MIT licence](LICENSE). Do not submit material you lack rights to license. Third-party code must retain its applicable notices and obligations; upstream code with unclear permissions must not be copied in.

# Open Vision: simulator-to-headset validation

> **Status**: active
> **Opened**: 2026-11-02 · **Updated**: 2026-11-02
> **Scope**: this repository; a future explicitly authorized Apple-silicon Mac and VR headset test environment
> **IDs**: OV = Open Vision validation; never renumber or reuse IDs

## ▶ START HERE

You are continuing Open Vision: investigate streaming Apple's visionOS Simulator from an Apple-silicon Mac to existing VR hardware, initially the original consumer PICO 4. Preserve the authentic-Simulator goal; do not silently substitute a lookalike shell or flat remote desktop.

**State.** The public Open Vision repository contains a feasibility report, a source ledger and documentation/tooling only. The initial published commit and its fresh-checkout documentation CI passed; evidence is on OV-2. Research found a historical 2023 stereo/pose bridge for Quest, not a reproduced current PICO implementation. The owner selected the Mac-hosted Simulator direction and authorized repository creation/publication, not installation or modification of a personal host. Start with OV-3, which can be investigated from public sources without hardware access. OV-4 needs a separately authorized operator; OV-5 must not be declared working from static analysis.

**Before you act.** Read `AGENTS.md`, `docs/architecture.md`, `docs/licensing.md` and section 5.6 of `docs/research/report.md`. Run `python3 scripts/check_docs.py`. Check every version and licence before adopting a historical command or component.

**Working rules.**

- Separate researched evidence, inferred design, unverified assumptions and actual test results.
- Do not copy the old simulator bridge without permission; the inspected branch has no detected top-level licence.
- Never run archived injection scripts, disable SIP/library validation, change shared services, capture private content or spend money without specific authorization.
- Linux/cloud checks do not prove native Simulator rendering, PICO tracking or comfortable latency.
- Keep this document as the only task/status ledger. Update the item and this bootstrap when evidence changes.

## Items

### OV-1: preserve and publish the research `[x]` DONE 2026-11-02 · evidence: `docs/research/report.md`, `docs/research/sources.json` and four axis notes

The curated source ledger contains 42 entries checked on 2026-11-01. The report retains both the initial independent-workspace assessment and the later historical Simulator-streaming finding. These are documentary findings, not local hardware results.

### OV-2: prepare the shared repository `[x]` DONE 2026-11-02 · evidence: published commit `c0d2dc98330b3a3cb3ab57fb6fa3204226868c31` and [successful fresh-checkout CI](https://github.com/l-wermelinger/open-vision/actions/runs/41494902057)

The public repository is [l-wermelinger/open-vision](https://github.com/l-wermelinger/open-vision), default branch `main`. Its initial remote commit and commit tree match the local publication. The documentation check passed for 11 Markdown files and 42 sources. The public file tree excludes raw archives, local harness state, personal home paths and detected credentials. Commits use a GitHub noreply address.

Cloud agents can clone the repository and start with `AGENTS.md` and this document. This verifies repository/documentation availability, not application streaming or access to a Mac/headset.

### OV-3: establish a current compatibility and permission baseline `[ ]` first cloud-ready task

Inspect current Apple documentation and the relevant public upstream history. Produce a narrow assessment of available Simulator versions, stereo/view/pose integration points, API changes and reuse permissions. Distinguish a supported public API from a private hook. Identify what can be evaluated without a Mac and what must wait for OV-4.

**Done when:** the source-backed findings and exact reference revisions are recorded in the existing architecture/research files; permission blockers and a bounded, non-destructive native test are explicit. Do not invent a working combination from old README requirements.

### OV-4: inventory an authorized native test environment `[ ]` BLOCKED: host/headset operator and explicit access approval

Record Mac model/chip, macOS, Xcode, Simulator runtime, GUI/session constraints, headset SKU/firmware and relevant loader/client versions. Do not include serials, account details, hostnames or addresses in public results.

**Done when:** a sanitized reproducible inventory and an approved recovery/test procedure are recorded. Read-only inspection permission is not permission for installation, injection or security changes.

### OV-5: prove stereo rendering with headset pose return `[ ]` BLOCKED: OV-3 and OV-4

Demonstrate two correctly ordered eye views from the hosted simulator, with the viewpoint following real headset position/orientation. Validate projection, eye separation, coordinates, recentering and timing. A flat preview duplicated to both eyes does not count.

**Done when:** an exact tested version tuple, reproduction steps, sanitized evidence and measured rendering/streaming behaviour exist. If hardware is absent, leave this item open.

### OV-6: validate interaction, secure connection and recovery `[ ]` BLOCKED: OV-5

Establish an explicit input method, authenticated/encrypted transport where required, a host-local exit path and reliable disconnect/sleep/wake/recenter behaviour. Keep headset safety boundaries active. Controller/hand/eye input must be described by the capabilities actually implemented.

**Done when:** the tested input path and failure/recovery cases are reproducible; security and any host modifications are documented and authorized.

### OV-7: integrate real MacBook desktops `[ ]` BLOCKED: OV-5 and OV-6

Determine whether the selected Simulator environment supports native Mac Virtual Display. If not, assess an independent Mac companion plus simulator-compatible receiver for captured or genuinely extended desktops.

**Done when:** different content can occupy real additional desktops, input/focus mapping is correct, and disconnect restores the Mac's usable display arrangement. Distinguish this from screen cloning and from Apple's proprietary native integration.

## Decisions & declined

| Date | Decision | By | Reason / boundary |
|---|---|---|---|
| 2026-11-02 | Name the project Open Vision and publish a shared GitHub repository. | Owner | Cloud agents need self-contained context and research. |
| 2026-11-02 | Make Mac-hosted authentic visionOS simulation the primary direction. | Owner | The goal is Apple's simulated spatial environment streamed to normal VR hardware, not just a lookalike. |
| 2026-11-02 | Keep the independent Mac-workspace route as researched fallback, not the default implementation. | Project setup | Preserve useful prior art without overriding the selected goal. |
| 2026-11-02 | Apply MIT to original repository contributions; do not vendor third-party implementation code during setup. | Project setup | Upstream and Apple rights remain separate. |

## Open questions

- Which current macOS/Xcode/Simulator combination permits a viable stereo/pose bridge without unacceptable security changes?
- Can the historical unlicensed bridge be reused with permission, or must the adapter be independently implemented using appropriately licensed components?
- What is the applicable SDK/Simulator licence position for the intended development, use and distribution model?
- Which original-PICO client/runtime/codec combination can meet the actual timing and interaction requirements?
- What subset of apps and system functions is available in the selected Simulator runtime?
- Does native Mac Virtual Display work there, or is a separate desktop receiver required?
- What measured clarity, comfort and latency are acceptable for real work on the target headset?

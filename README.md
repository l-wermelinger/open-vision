# Open Vision

**Explore Apple's visionOS Simulator on a VR headset you already own, powered by your own Mac.**

Open Vision is a research-stage project investigating a bridge from the **visionOS Simulator on an Apple-silicon Mac** to an existing VR headset. A Mac mini or Mac Studio would run the simulated spatial environment; the headset would display stereoscopic views and return head tracking and input.

**Status, 2026-11-02: research and repository setup only. There is no working Open Vision host, headset client or downloadable release yet.**

This is not a visionOS firmware port, an Apple-device identity emulator, or a claim that the Simulator provides every retail Vision Pro app and service. Apple software is not included. Open Vision is independent and is not affiliated with Apple, PICO or Meta.

## The goal

```text
Your Apple-silicon Mac
  Xcode + Apple's visionOS Simulator
                |
     proposed stereo streaming bridge
                |
       your existing VR headset
                |
     headset pose and input return
```

The goal is the **whole simulated spatial view**, not merely a flat simulator window shown on a cinema screen. Correct per-eye rendering, head pose, projection, timing and interaction are essential.

The first target is the **original consumer PICO 4**. Other headsets are a longer-term goal, not an existing compatibility claim. The minimum Mac chip, macOS, Xcode and runtime versions are not established yet.

A later goal is working with real MacBook desktops inside the simulated environment. **Apple's native Mac Virtual Display has not been verified in Simulator**; a separate companion and simulator-compatible receiver may be necessary.

## Why this is worth investigating

A historical project, [VisionOSStereoScreenshots on its `alvr` branch](https://github.com/zhuowei/VisionOSStereoScreenshots/tree/alvr), documented streaming the visionOS Simulator from Apple silicon to Quest using a specific 2023 ALVR nightly. Its inspected source contains separate eye textures and incoming headset-pose integration. This is more than a theoretical diagram.

However, its documented configuration is old, later issues report compatibility failures, and it does not establish current PICO support. Its reuse permissions also need clarification. **Open Vision has not reproduced that demonstration.** See [the feasibility report, section 5.6](docs/research/report.md) and sources S37-S42 in the [source ledger](docs/research/sources.json).

## Start here

- [Architecture](docs/architecture.md): the selected direction, component boundaries and unresolved assumptions.
- [Workstream](docs/workstream.md): current state, stable-ID tasks and a paste-ready cloud-agent bootstrap.
- [Research report](docs/research/report.md): full findings, including the earlier independent-workspace alternative.
- [Source ledger](docs/research/sources.json): 42 curated sources with retrieval dates, uses and limitations.
- [Licensing and third-party boundaries](docs/licensing.md): what may and may not be reused.
- [Contributing](CONTRIBUTING.md) and [agent instructions](AGENTS.md): how to work safely and leave reproducible evidence.

The earlier locally rendered Mac-workspace approach remains documented as an alternative. It must not silently replace the selected authentic-Simulator goal.

## Working in this repository

There is no application build command yet. Cloud agents can research current APIs, inspect licence-compatible public references, review architecture and work on explicitly assigned tasks without access to a personal machine.

Run the documentation checks with **Python 3.10 or later**:

```sh
python3 scripts/check_docs.py
```

These checks validate repository documentation and research metadata. They do **not** establish that Simulator streaming works. macOS, Xcode and headset testing require an authorized hardware environment; Linux CI cannot substitute for those tests.

## Repository layout

```text
AGENTS.md                 Portable instructions for coding/cloud agents
CONTRIBUTING.md            Contribution, evidence and review rules
LICENSE                    MIT licence for original Open Vision contributions
docs/
  architecture.md         Proposed simulator-bridge architecture
  workstream.md           Single task/status ledger and session handoff
  licensing.md            Apple and upstream licence boundaries
  research/
    report.md             Complete feasibility research
    sources.json          Curated source-to-claim ledger
    notes/                Integrated findings by research axis
scripts/check_docs.py      Dependency-free documentation checks
.github/workflows/docs.yml Documentation CI
```

Local raw-page archives and research-harness state are deliberately excluded. Source URLs and checked dates are public; optional `snapshots` fields refer to uncommitted local evidence, not files required by a cloud checkout.

## Safety and licensing

Do not run archived injection scripts, disable SIP/library validation, change a shared Mac server, install software, access accounts or capture private screens without explicit authorization. Never expose streaming or remote input to an untrusted network without authenticated pairing and encryption.

The [MIT licence](LICENSE) covers original Open Vision files, not Apple's runtime or third-party projects. Publicly visible source without a licence is not automatically reusable. No third-party implementation is vendored in this repository.

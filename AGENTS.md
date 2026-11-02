# Open Vision agent instructions

Updated: 2026-11-02.

## Bootstrap

Read these files before making changes:

1. `README.md`
2. `docs/workstream.md`, especially the standalone START HERE handoff, phases and chosen task
3. `docs/product-requirements.md`, `docs/architecture.md` and `docs/licensing.md`
4. `docs/research/report.md`, especially section 5.6; use `docs/research/sources.json` for evidence

All required project context is in the repository. Do not depend on personal memory systems, absolute machine paths, local research-harness state or private services.

## The selected goal

Bridge Apple's **visionOS Simulator running on an Apple-silicon Mac** to existing VR hardware, starting with the original consumer PICO 4. Stream the simulated spatial environment stereoscopically and return headset pose/input. Do not silently replace this goal with a lookalike interface or generic flat remote desktop.

The owner has delegated remaining routine product decisions. Follow the product requirements rather than reopening preference questions. Controller pointing selects, trigger simulates pinch, native system-wide gestures come first, synthetic hand joints follow where compatibility requires them, and the owner's real Apple Account plus real service/persistence tests are mandatory for release.

The target is a lightweight native Mac Studio worker. Ordinary Linux containers cannot contain the actual Xcode/Simulator runtime; separate data/process lifecycle is not security-equivalent container confinement. Optional container helpers and macOS VMs are separate conditional choices. Do not fake fulfillment of the literal full-runtime-container request.

A locally rendered Mac-display workspace remains a researched alternative, not a substitute for the primary goal. Preferred native language/media choices are design defaults, not implemented or adopted dependencies.

## Evidence, not claims

- The repository currently contains research, documentation and documentation checks, not a working streamer.
- Historical Simulator-to-Quest stereo/pose streaming is researched evidence, not a reproduced Open Vision result.
- Record exact Mac/macOS/Xcode/runtime and headset/firmware/loader versions for every relevant test. Do not conflate original PICO 4 with Ultra, Pro or Enterprise.
- Distinguish researched, inferred, unverified and locally verified findings.
- A simulator-compatible build is not a retail visionOS device build. Arbitrary App Store app support, Apple Continuity and native Mac Virtual Display remain unverified.
- Head direction is not eye tracking; visible passthrough is not access to raw camera frames; mDNS discovery is not authentication or physical laptop pose.
- A successful Linux check or Android cross-build is not a native Mac/headset runtime test. If required hardware is absent, document the blocker rather than inventing a result.

## Implementation rules

Follow the phase gates and bounded delegation plan in `docs/workstream.md`: one coordinator, up to three concurrent focused workers, then at most one independent reviewer per phase exit. Workers own disjoint files or return read-only evidence; only the coordinator writes parent task status. If no delegation tool exists, execute the lanes sequentially and say so. Do not introduce paid providers or nested agent trees without approval.

Each worker takes a bounded `OV-*` assignment. Prefer a small end-to-end proof over a framework or plugin architecture. Do not create empty host/client directories or speculative dependencies before there is code to put in them.

Before copying/linking any upstream code, verify its licence and applicable obligations. The inspected historical Simulator bridge has no detected top-level licence. Do not vendor it without permission. Do not import leaked/decompiled Apple code, firmware, runtime images, proprietary assets or restricted fonts.

Phase 0 must address SDK/reuse permissions, version compatibility, actual account feasibility and the native/container resource boundary before a large runtime implementation. The first VR proof is two correct eye views with pose return and sane timing; native input, recovery, desktop integration, optimization and packaging follow their gates. Account checks must be repeated after integration and in the final package. A test account, Xcode sign-in or iCloud website alone does not meet the owner's account requirement. Keep calibration and headset safety controls available. Any networking must use explicit pairing/authentication and encryption before carrying private content or input on untrusted networks.

## Authorization boundaries

Delegated design and repository work do not grant access to anyone's Mac, headset, accounts or network. The owner manually enters real credentials and two-factor codes in Apple's supported UI; never collect them or place account state in images, CI artifacts, logs or agent context. Never disable account protections or spoof device credentials to make a check pass. Do not run archived injection scripts, disable SIP/library validation, install packages, modify shared servers, change display layouts, open router ports or use paid services without explicit approval for that action. Never request credentials in an issue or commit them.

Follow the current task's commit/push permissions. Never force-push or delete history without explicit authorization. No AI attribution trailers or generated-by headers in commits or files.

## Finish a task

Run `python3 scripts/check_docs.py` plus any checks appropriate to the actual code change. Leave runnable regression evidence for non-trivial logic. State which native/device tests were not possible.

Update the existing `docs/workstream.md` item, its evidence, decisions and START HERE state. Do not create a competing roadmap, handoff or versioned report. Update source entries when research changes, retaining dates and limitations. Keep raw downloads, captures, credentials and local logs out of Git.

# Open Vision agent instructions

Updated: 2026-11-02.

## Bootstrap

Read these files before making changes:

1. `README.md`
2. `docs/workstream.md`, especially START HERE and the chosen task
3. `docs/architecture.md` and `docs/licensing.md`
4. `docs/research/report.md`, especially section 5.6; use `docs/research/sources.json` for evidence

All required project context is in the repository. Do not depend on personal memory systems, absolute machine paths, local research-harness state or private services.

## The selected goal

Bridge Apple's **visionOS Simulator running on an Apple-silicon Mac** to existing VR hardware, starting with the original consumer PICO 4. Stream the simulated spatial environment stereoscopically and return headset pose/input. Do not silently replace this goal with a lookalike interface or generic flat remote desktop.

A locally rendered Mac-display workspace is researched as an alternative, not the selected primary architecture. No application framework, transport or upstream implementation has been adopted.

## Evidence, not claims

- The repository currently contains research, documentation and documentation checks, not a working streamer.
- Historical Simulator-to-Quest stereo/pose streaming is researched evidence, not a reproduced Open Vision result.
- Record exact Mac/macOS/Xcode/runtime and headset/firmware/loader versions for every relevant test. Do not conflate original PICO 4 with Ultra, Pro or Enterprise.
- Distinguish researched, inferred, unverified and locally verified findings.
- A simulator-compatible build is not a retail visionOS device build. Arbitrary App Store app support, Apple Continuity and native Mac Virtual Display remain unverified.
- Head direction is not eye tracking; visible passthrough is not access to raw camera frames; mDNS discovery is not authentication or physical laptop pose.
- A successful Linux check or Android cross-build is not a native Mac/headset runtime test. If required hardware is absent, document the blocker rather than inventing a result.

## Implementation rules

Work one assigned `OV-*` item at a time. Prefer a small end-to-end proof over a framework or plugin architecture. Do not create empty host/client directories or speculative dependencies before there is code to put in them.

Before copying/linking any upstream code, verify its licence and applicable obligations. The inspected historical Simulator bridge has no detected top-level licence. Do not vendor it without permission. Do not import leaked/decompiled Apple code, firmware, runtime images, proprietary assets or restricted fonts.

The first runtime proof is two correct eye views with pose return and sane timing. Input, recovery and desktop integration follow. Keep calibration and headset safety controls available. Any networking must use explicit pairing/authentication and encryption before carrying private content or input on untrusted networks.

## Authorization boundaries

Repository work does not grant access to anyone's Mac, headset, accounts or network. Do not run archived injection scripts, disable SIP/library validation, install packages, modify shared servers, change display layouts, open router ports or use paid services without explicit approval for that action. Never request credentials in an issue or commit them.

Follow the current task's commit/push permissions. Never force-push or delete history without explicit authorization. No AI attribution trailers or generated-by headers in commits or files.

## Finish a task

Run `python3 scripts/check_docs.py` plus any checks appropriate to the actual code change. Leave runnable regression evidence for non-trivial logic. State which native/device tests were not possible.

Update the existing `docs/workstream.md` item, its evidence, decisions and START HERE state. Do not create a competing roadmap, handoff or versioned report. Update source entries when research changes, retaining dates and limitations. Keep raw downloads, captures, credentials and local logs out of Git.

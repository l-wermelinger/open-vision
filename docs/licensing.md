# Licensing and third-party boundaries

Updated: 2026-11-02. This is a contribution policy, not a jurisdiction-specific legal opinion.

## Original Open Vision contributions

The repository's [MIT licence](../LICENSE) applies to original Open Vision documentation and tooling. It does not grant rights over Apple software or material belonging to upstream projects.

No third-party application implementation is currently vendored. Links, independently written research summaries and compatibility observations are not claims of ownership over upstream code.

## Apple software stays separate

Users must obtain Xcode and any visionOS Simulator runtime through Apple under the applicable terms. Do not upload runtime images, firmware, extracted frameworks, private SDK binaries, restricted fonts, icons or wallpapers to this repository or its releases.

Apple's published device-OS and developer agreements contain restrictions and exceptions. Simulator use must be assessed under the relevant SDK/tool agreement; an experiment working technically does not settle its licence status or authorize a general-purpose distributed product. The [research ledger](research/sources.json) records the agreements examined and their limitations.

Do not copy leaked/decompiled proprietary source or submit an AI-rewritten derivative as independently licensed code. Limited interoperability exceptions, where applicable, are not blanket redistribution permission.

Open Vision is not affiliated with or endorsed by Apple, PICO or Meta. The project name has not undergone trademark clearance.

## Reference projects are not adopted dependencies

| Reference | Research finding | Reuse boundary |
|---|---|---|
| VisionOSStereoScreenshots, `alvr` branch | Historical stereo/pose simulator streaming. No top-level licence found in the inspected branch; GitHub detected no repository licence. | Do not copy/vendor without clarifying permission and provenance. Publicly readable is not automatically open source. |
| XRGyroControls_OpenXR | Related historical bridge and security-sensitive setup instructions. | Audit current licence, components and host changes before any proposed reuse or execution. |
| ALVR / Monado | Streaming/runtime reference projects. | Inspect the exact version, component licences and integration mode. A fork or embedded server is not automatically equivalent to upstream support. |
| PippinVR, Sunshine, Nightfall | Sampled projects carry GPLv3 licences. | Preserve applicable notices and source obligations. Do not label a copied derivative as MIT-only. |
| DeskPad / Godot OpenXR Vendors | Sampled code carries MIT licences. | Preserve applicable notices and check any separate bundled dependencies/assets. |

Sources S10, S17-S24 and S38-S41 in the ledger support these observations as of their checked dates. Recheck the exact revision before adopting anything. No exhaustive dependency audit has been performed.

An original MIT component may remain MIT when combined with other software, but distribution of a combined work must still satisfy all applicable licences. Establish that analysis before integrating GPL or unlicensed code, not after publishing a release.

## Public research versus private evidence

The public research report and source ledger are independently written synthesis with source URLs and dates. Optional `snapshots` entries name local, uncommitted evidence files. Raw downloaded pages, source archives, licence PDFs, private captures and logs are deliberately not redistributed wholesale.

Contributors should add public source URLs and narrow, attributed findings. Preserve uncertainty and source-family relationships. Obtain permission where required rather than assuming that citation supplies a redistribution licence.

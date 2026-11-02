# Open Vision: phased implementation and agent handoff

> **Status**: active
> **Opened**: 2026-11-02 · **Updated**: 2026-11-02
> **Scope**: this repository; future explicitly authorized Mac Studio, development MacBook and original consumer PICO 4 test environments
> **IDs**: OV = Open Vision implementation/validation; never renumber or reuse IDs

## ▶ START HERE

You are continuing **Open Vision**, an independent project to stream Apple's real visionOS Simulator spatial environment from an Apple-silicon Mac to an existing VR headset. The target host is the owner's Mac Studio; the first headset is the original consumer PICO 4. The owner wants an almost fully usable supported environment, real Apple Account login, low resource overhead, natural hand-style interaction driven by controllers, and genuine MacBook extended desktops. Do not substitute a lookalike shell, flat remote desktop or demo-account-only experience.

**Autonomy contract.** The owner has delegated routine product and technical decisions. Follow `docs/product-requirements.md` instead of reopening preference questions. Make small, evidence-driven repository changes and move through the phases below while prerequisites pass. Ask only for missing private/device facts, explicit safety/financial/access approvals, or a material conflict with the required outcome. Delegation of design does not authorize account access, security downgrades or changes to a personal/shared machine.

### State and evidence

- **Verified repository state:** the public repository is `https://github.com/l-wermelinger/open-vision`, branch `main`. Initial research/docs were published in `c0d2dc98330b3a3cb3ab57fb6fa3204226868c31`; follow-up documentation commit `f5a7c9f19d8618d429132b3dfb902dded529c131` passed GitHub CI. These are historical reference commits, not an assertion that they are still the latest HEAD. See OV-2.
- **Current implementation boundary:** only documentation and documentation-check tooling exist. No Open Vision runtime, host build, PICO installation, live stereo test, current account sign-in or performance result has been demonstrated in this project.
- **Researched evidence:** a 2023 Quest/Xcode-beta implementation streamed separate eye views and consumed headset pose. It is not a current PICO implementation or an automatically licensed dependency. Sources S38-S40.
- **Resolved product choices:** controller pointing supplies target selection; trigger down/up simulates pinch; native system-wide gestures come first, followed by synthetic articulated-hand compatibility where required. Opaque simulated surroundings come before real-room passthrough. Target direct local Studio-to-PICO transport; a MacBook USB connection is not proof of that path.
- **Critical deployment exception:** ordinary Linux/OCI containers cannot supply the macOS/Xcode Simulator runtime. The selected low-overhead design uses a native macOS worker with isolated data/lifecycle and optional containerized auxiliaries only if useful. This is not literal full-runtime containerization. Sources S43-S45. A macOS VM is a separate unverified alternative, not a Docker workaround.
- **Critical release gate:** the owner's real Apple Account must work through the supported simulated system UI and at least one approved actual iCloud operation. Historical sign-in reports and macOS-VM iCloud documentation are not proof. SDK licensing also needs specific review, especially S48.

### Your first session

Run **Phase 0**. Dispatch the three bounded research lanes below if delegation is available. Integrate their findings yourself, identify the exact version/licence/account/container blockers, and prepare the smallest safe native validation procedure. If no host/operator access exists, complete public-source and repository work, then return one consolidated request for the specific native actions needed. Do not claim a gate passed because a worker wrote a convincing report.

Do not start downstream runtime implementation on a known failed licence, account, stereo or input premise. A temporary native experiment may be deliberately limited, but its limitations are not product acceptance. If a required feature proves unsupported, record the blocker on the relevant item and stop that dependent path rather than quietly changing the product.

### Read first, in order

1. `AGENTS.md`: portable working rules and authorization boundaries.
2. `docs/product-requirements.md`: authoritative delegated choices, R-01 through R-10, input defaults, real-account acceptance and lightweight implementation policy.
3. `docs/architecture.md`: runtime/process boundaries, proposed media/pose flow and researched versus unverified claims. It is a design, not code.
4. `docs/licensing.md`: original/upstream/Apple rights; the actual Xcode SDK terms matter, not just the device-OS licence.
5. `docs/research/report.md`, especially sections 5.6-5.7: historical simulator streaming and later deployment/licensing findings. Earlier local-workspace sections are an alternative, not the selected goal.
6. `docs/research/sources.json`: source URLs, checked dates, reference revisions and limitations. Sources S37-S48 are particularly relevant. Optional raw snapshots are not present in a public checkout.
7. The complete phase plan and item ledger in this file. Keep item status here, not in a second roadmap or handoff.

### Verify before trusting this handoff

This is a dated account of prior work, not evidence of today's machine state. From the repository root:

```sh
git status --short
git log -3 --oneline
git remote -v
python3 scripts/check_docs.py
git diff --check
```

Confirm the expected repository and review existing changes before editing. Do not reset, force-push or overwrite someone else's uncommitted decisions. The current check should pass local documentation/source-reference checks and explicitly state that native Simulator/headset tests are not performed. It is not a runtime test.

Recheck all versioned vendor behaviour against current primary documentation and actual source. The historical bridge depended on private layouts and an old ALVR nightly; a supported Xcode/runtime pair does not make those hooks compatible. Real account sign-in, system-wide input and hardware decoding must be observed, not inferred from settings or successful compilation.

### Subagent operating plan

Use **one coordinator plus up to three concurrent workers** by default. Parallelism is for independent evidence or disjoint implementation, not maximum agent count. If the harness cannot delegate, do the same lanes sequentially and report that fact; do not claim subagents were launched.

**Phase 0 lanes:**

| Lane | Assignment | Required result |
|---|---|---|
| A: Apple runtime/deployment | OV-3 and OV-9: current Xcode/Simulator interfaces, historical API changes, native/container/VM boundaries and graphics constraints. | Exact sources/revisions, supported versus private interfaces, minimal version-compatible test and failure conditions. |
| B: account/licensing/security | OV-8 and the permission part of OV-3: SDK terms, real-account/service distinctions, privacy, state persistence and a manual owner-operated test. | Permission questions and a concrete non-sensitive sign-in/service/persistence procedure; no credentials, account access or legal-certification claim. |
| C: PICO/media/input | Prepare OV-4, OV-5 and OV-6: exact original-PICO capabilities, codec/transport reuse, native gesture versus skeletal-hand integration and recovery. | A bounded stereo/pose/input proof, version uncertainties, required measurements and device-only tests. |

Workers return evidence to the coordinator; they do not independently rewrite the workstream or manipulate a shared native test environment. Assign explicit file ownership before any writing. Temporary scratch output stays in ignored local storage; integrate durable findings into the existing docs and ledger.

**Implementation phases:** use one builder for tightly coupled adapter work, or at most two builders with disjoint host/client/test ownership. Keep a shared wire/input contract under one coordinator. Use the remaining worker slot for focused verification when useful. Do not split the same file between agents or add a task engine to orchestrate them.

**Review:** at each phase exit, use at most one independent reviewer to challenge acceptance evidence, security, provenance and regressions. Finish/stop other workers first if needed to stay within the three-worker ceiling. Fix blockers and have the coordinator verify corrections; do not collect model votes as proof. Reviewers cannot certify account or hardware behaviour they did not observe.

Use only configured, authorized model/provider budgets. Explicitly choose the worker model when the harness supports that field. In a Claude-configured environment, Haiku is the default for bounded lookups and Sonnet is appropriate for difficult integration/review; other providers should use approved equivalents. Do not silently introduce paid aggregators or an expensive swarm. Nested delegation is off unless a concrete need and budget are documented.

### Safety, recording and session exit

- Repository scope is not machine access. OV-4 and account operations need an authorized operator. No passwords, two-factor codes, recovery material or private captures in prompts, tools, issues or commits.
- Never spoof hardware credentials/identity or weaken Apple Account security to make a test pass. Disabling SIP/library validation, creating users, modifying shared services, installing software or opening network exposure requires explicit action-specific approval and a reviewed recovery plan; none is a default.
- Never copy unlicensed reference code or distribute Apple runtime/framework/assets. S48 creates an SDK-use review gate for the intended end-user product, not just packaging.
- Keep one active session and stop only owned resources. Preserve unrelated workloads and persistent private account data.
- Use existing task IDs in commits/PRs. Respect the current execution task's commit/push permissions; never force-push or merge protected changes without approval.
- After each gate, update the item evidence, actual capability findings and this START HERE state. Do not create a handoff chain. If blocked, record the exact failing operation, versions, safe reproduction and missing approval/evidence, then stop the dependent path.

**Session success:** a bounded item gains reproducible evidence and appropriate checks, or a genuine blocker is precisely demonstrated. Report code checks separately from Mac/device/account tests. Never relabel a plan as a working release.

## Implementation phases

This section defines sequencing and exit criteria. **Statuses appear only on the item ledger below.**

### Phase 0: prove the premises before committing to the platform

Items: **OV-3, OV-4, OV-8, OV-9**.

Establish current source/licence findings, a sanitized native version tuple and GUI/session inventory, actual real-account feasibility on an authorized stock runtime, the honest container/native boundary and an initial resource baseline. Public research can proceed without hardware; the native portion cannot be replaced by assumptions.

**Exit:** a supported candidate tuple and reuse-rights path are documented; owner-operated real account plus one approved iCloud operation and relaunch have evidence; native deployment/resource boundaries are understood. Account/service/SDK blockers stop the affected product path before a large streamer is built. If host/account access is unavailable, leave those gates open and deliver the prepared test rather than claiming completion.

### Phase 1: build the smallest owned native host lifecycle

Item: **OV-10**; prerequisites are the relevant Phase 0 decisions and explicit installation/execution authorization.

Implement a small native supervisor around one project-owned Simulator device/profile, with start/status/stop, private persistent data boundaries, sanitized diagnostics and a safe recovery path. Start from non-personal test content. A per-user GUI session is a requirement to verify; do not promise a headless root daemon or reboot-autostart experience without evidence.

**Exit:** lifecycle tests pass without touching other Simulator devices or services; stopping removes owned heavy workers, not account data; installed versions and resource baselines are visible. No Docker image is claimed to contain the Apple runtime.

### Phase 2: show correct stereo views with live pose return

Item: **OV-5**; depends on Phase 1 and the reviewed adapter/transport permission path.

Prove separate eye views, correct controller/headset coordinate spaces, headset FOV/IPD calibration, pose timing, recentering and a real PICO decode/presentation path. Use licensed reuse and hardware media paths where possible. Use an authenticated/encrypted path before private content, or a specifically authorized isolated diagnostic connection carrying only clean test content.

**Exit:** reproduce a scene that follows headset translation and rotation on the exact PICO profile, with measured frame/latency breakdown and no flat-image substitution. Screen-capture videos alone do not prove stereo or latency.

### Phase 3: native controller-driven hand interaction and safe personal use

Item: **OV-6**; depends on Phase 2.

Implement controller-target/trigger-pinch semantics across Home View, Settings, window handles and a compatible app. Validate drag, scroll and multi-input support rather than assuming it. Add synthesized hand joints where required by the advertised hand-tracking app/API surface; do not claim full skeletal support from gesture events. Complete pairing/encryption, reconnect, sleep/wake and host-local recovery.

**Exit:** ordinary visionOS navigation no longer depends on host-mouse operation; failures can be recovered safely; the actual system-wide gesture path is demonstrated. Revalidate the owner's account/service/persistence on the integrated profile under the privacy procedure before private content is allowed into normal sessions.

### Phase 4: make the MacBook workspace genuinely useful

Item: **OV-7**; depends on Phase 3.

Test native Mac Virtual Display in the chosen environment. If unsupported, implement an appropriately licensed/native Mac companion and simulator-compatible receiver with real virtual desktops. Do not pretend the receiver is Apple's proprietary integration. Preserve ordinary Mac keyboard/trackpad workflows and consent for capture/input permissions.

**Exit:** first acceptance target is two different extended desktop surfaces without physical extra monitors, correct focus/pointer mapping and restored Mac display arrangement on exit/failure. Measure the additional MacBook-to-Studio-to-PICO capture/encoding cost; a visually impressive clone of one screen fails.

### Phase 5: reduce overhead and qualify sustained use

Item: **OV-11**; depends on a working measured pipeline, with baseline measurements collected throughout prior phases.

Optimize copies, hardware codec settings, resolution, rendering profile and lifecycle from evidence. Default to the lowest-cost comfortable supported profile rather than peak resolution. Avoid a second VM, engine, software encoder or cloud relay without a measured reason.

**Exit:** publish a sanitized resource/latency envelope for stopped, idle, connected and active-work states; pass the proposed 20-minute working session and three reconnect/sleep-wake cycles; identify impacts on other host workloads. Do not fabricate photon latency from a transport overlay. An early resource envelope must exist before this final optimization phase, not be invented here to excuse regressions.

### Phase 6: package only what has actually passed

Item: **OV-12**; depends on the end-goal acceptance gates.

Provide reproducible build/install/update/uninstall/recovery instructions, pinned compatible versions, a truthful per-feature support matrix, privacy defaults and original/upstream notices. Users obtain Apple software separately. Test final-package real account/service persistence and safe removal without deleting private data by default.

**Exit:** all required capabilities have evidence or the product is explicitly labelled incomplete/experimental. No “almost full visionOS” release claim hides missing account access, system-wide input, stereo or real workspace behaviour. Retest updates before changing supported version claims.

## Items

### OV-1: preserve the research `[x]` DONE 2026-11-02 · evidence: `docs/research/report.md`, `docs/research/sources.json` and four axis notes

The original curated ledger had 42 entries checked on 2026-11-01. It now also includes the dated deployment/VM/SDK references S43-S48. These are documentary findings, not native hardware or account results.

### OV-2: prepare the shared repository `[x]` DONE 2026-11-02 · evidence: publication `c0d2dc98330b3a3cb3ab57fb6fa3204226868c31` and [fresh-checkout CI](https://github.com/l-wermelinger/open-vision/actions/runs/41494902057)

Public repository: [l-wermelinger/open-vision](https://github.com/l-wermelinger/open-vision), default branch `main`. Initial remote commit/tree matched the local publication. Follow-up `f5a7c9f19d8618d429132b3dfb902dded529c131` also passed [CI](https://github.com/l-wermelinger/open-vision/actions/runs/41495331932). Those checks established documentation availability, not streaming or machine access. Raw archives and local harness state remain untracked.

### OV-3: current runtime and permission baseline `[~]` current platform/SDK terms researched; exact adapter, reuse rights and native tuple unresolved

Recheck exact current Xcode/runtime/adapter interfaces and upstream revisions; distinguish supported APIs from private hooks. Resolve the old bridge's reuse rights and review the actual SDK intended-use/network/modification conditions in S48. Record a narrow safe native test and what it can prove.

**Done when:** a source-backed candidate version/reuse path and unresolved legal/technical blockers are explicit. A generic reference to the device-OS licence or historical README is not sufficient.

### OV-4: authorized native environment inventory `[ ]` BLOCKED: operator and explicit access approval

Record sanitized Mac/chip/macOS/Xcode/runtime, GUI-session constraints, original-PICO firmware/loader/client/codec capabilities and network/USB topology. The owner reports a PICO connected to the development MacBook; that is not observed proof of authorization, VR transport or Mac Studio readiness.

**Done when:** an operator-approved inventory and recovery procedure exist with no serials, identities, addresses or private workload data in public evidence. Read-only inventory permission does not authorize installation or security changes.

### OV-5: stereo rendering and live pose return `[ ]` BLOCKED: relevant Phase 0 gates and OV-10

Demonstrate the actual two-eye, calibrated, timed, headset-driven spatial view on PICO. Record reproduction, version tuple, performance methodology and failure/recenter behaviour. No actual result exists yet.

**Done when:** Phase 2 exit criteria pass on hardware. Linux compilation, a Quest demo or a duplicated flat preview does not count.

### OV-6: natural interaction, secure connection and recovery `[ ]` BLOCKED: OV-5

Follow R-03 and the delegated input mapping. Prove system-wide native gestures first, then articulated-hand support for any apps/APIs advertised as needing it. Do not silently substitute a gamepad or mouse-only product. Complete authenticated encrypted personal sessions, safe reconnect/sleep/wake and integrated account revalidation.

**Done when:** Phase 3 exit criteria pass with evidence separating semantic gestures from synthetic skeletal hands. Account and safety tests require the authorized operator.

### OV-7: genuine MacBook extended desktops `[ ]` BLOCKED: OV-5 and OV-6

Test native Mac Virtual Display; if unavailable, implement a separate companion/receiver honestly. Meet the two-different-desktop first acceptance target, consent/input correctness and display restoration, with the extra media-path cost measured.

**Done when:** Phase 4 exit criteria pass on the chosen host/MacBook/headset profile. A screenshot or cloned display is not evidence of extension.

### OV-8: real owner Apple Account and service feasibility `[ ]` BLOCKED: OV-3 permission baseline and authorized account operator

Test stock simulated Settings account sign-in using normal two-factor authentication, an approved real iCloud canary and session persistence. Preliminary test accounts do not satisfy the owner's final requirement. Revalidate after integration and packaging; do not publish identity, credentials, private screenshots or account-state artifacts.

**Done when:** the real system-account/service/persistence capability is observed and sanitized evidence is recorded for the actual version/profile. An unsupported runtime, service or account policy is a blocker, not a reason to downgrade silently to a demo or website login.

### OV-9: honest container boundary and resource baseline `[~]` documented platform boundary; native baseline and isolation validation not performed

Sources S43-S45 establish the Linux-container/native-Xcode boundary. Sources S46-S47 establish a separate macOS-VM option, not nested Simulator/account/graphics feasibility. The selected native worker is defined in `docs/product-requirements.md` and `docs/architecture.md`.

**Done when:** the target's actual GUI/data/process isolation and resource baseline are observed, an explicit operating envelope is set, and the literal container limitation is acknowledged. A container supervising an external Mac worker is not full runtime containerization. No VM or container has been created.

### OV-10: bounded native host lifecycle `[ ]` BLOCKED: Phase 0 decisions and execution/installation authorization

Implement one owned device/session with start/status/stop, private persistent state and scoped cleanup. Do not kill unrelated host processes or erase account data. Keep personal profiles inactive during clean-content media experiments.

**Done when:** Phase 1 exit criteria and runnable lifecycle/recovery tests pass in the authorized environment.

### OV-11: lightweight sustained performance `[ ]` BLOCKED: working integrated path and OV-9 baseline

Measure and reduce idle/active CPU, memory, GPU/media workload, traffic, frame delivery and latency using a documented method. Qualify the chosen profile with sustained work and failure/recovery cycles. Do not invent universal resource guarantees or mistake overlays for measured photons.

**Done when:** Phase 5 exit criteria and the published operating envelope hold without unacceptable effects on existing workloads.

### OV-12: honest packaging and release qualification `[ ]` BLOCKED: required runtime, account, interaction, workspace and performance gates

Ship only properly licensed tooling and instructions, not Apple's runtime or private state. Qualify the final installed version, account persistence, upgrades/rollback, recovery and safe uninstall. Mark every unsupported/untested retail feature clearly.

**Done when:** Phase 6 exit criteria and R-01 through R-10 have appropriate evidence, with any unmet literal container boundary disclosed. Otherwise retain the experimental label and report the exact remaining blocker.

### OV-13: document delegated decisions, phases and standalone handoff `[x]` DONE 2026-11-02 · evidence: `python3 scripts/check_docs.py` passed for 12 Markdown files and 48 sources; `git diff --check` passed

This planning session resolves routine product choices in `docs/product-requirements.md`, records the seven phases and coordinator/worker plan here, and updates architecture/account/container/licensing instructions. The workstream START HERE is the handoff; no competing handoff file exists.

Repository documentation/link/source checks and publication hygiene passed. A separate plan-integrity check confirmed seven ordered phases, unique stable IDs OV-1 through OV-13, one START HERE handoff and available local evidence snapshots. No subagents were launched and no native/device/account tests were performed by documenting their future execution. This item does not complete any runtime phase.

## Decisions & declined

Append-only. Later rows explicitly supersede earlier unresolved/default wording, not historical evidence.

| Date | Decision | By | Reason / boundary |
|---|---|---|---|
| 2026-11-02 | Name the project Open Vision and publish a shared GitHub repository. | Owner | Cloud agents need self-contained context and research. |
| 2026-11-02 | Make Mac-hosted authentic visionOS simulation the primary direction. | Owner | Stream Apple's simulated spatial environment, not just a lookalike. |
| 2026-11-02 | Retain the independent Mac-workspace route as researched fallback. | Project setup | Preserve prior art without replacing the primary goal. |
| 2026-11-02 | MIT for original contributions; do not vendor third-party implementation during setup. | Project setup | Upstream and Apple rights remain separate. |
| 2026-11-02 | Controllers first, with Simulator-side natural hand/finger behaviour. | Owner | Requirement, not verified feasibility; mouse/gamepad-only substitution is not accepted. |
| 2026-11-02 | Controller pointing selects; trigger simulates pinch. | Owner | Not head-direction targeting. Remaining mappings were initially unresolved. |
| 2026-11-02 | Delegate remaining routine decisions and request phased implementation/handoff with bounded subagents. | Owner | Supersedes the preference-interview pause. Actual feasibility and safety gates remain. |
| 2026-11-02 | Native system-wide gestures first; synthesize articulated hands where compatibility requires them; opaque environment before passthrough. | Delegated engineering decision | No measured finger/eye tracking claim; no photoreal-hand prerequisite for ordinary work. |
| 2026-11-02 | Real owner Apple Account plus real service/persistence evidence is mandatory for release. | Owner / acceptance definition | Not just a demo, Xcode signing, StoreKit sandbox or website login. Never weaken account security. |
| 2026-11-02 | Native Mac Studio worker is the lowest-overhead default; no fake full-Simulator Linux container. | Delegated engineering decision, S43-S45 | Literal full-runtime containerization remains unmet; auxiliaries or a macOS VM are separate evaluated choices. |
| 2026-11-02 | Three independent feasibility lanes, then one/two builders and one phase reviewer within bounded concurrency. | Delegated execution plan | Evidence and disjoint ownership matter more than an agent swarm. No workers were launched by writing this plan. |

## Open questions

These are evidence/permission questions, not undecided routine product preferences.

- Which exact current Xcode/runtime tuple supports the required compositor/pose and system-wide gesture paths safely and lawfully?
- Are the intended SDK/end-user/remote-viewing uses permitted, and can the reference bridge be reused with permission?
- Does the owner's real account and a required iCloud service work in that actual Simulator profile, before and after bridge integration?
- Can the target GUI/session and process/data isolation coexist with existing host workloads, and what resource envelope is realistic?
- Which original-PICO loader/client/codec path provides calibrated stereo, stable timing and synthetic-input compatibility?
- Which apps require actual articulated-hand data, and can the chosen input path supply it system-wide rather than only inside our app?
- Does native Mac Virtual Display work there, or must a separate receiver/virtual-display companion be implemented?
- If literal all-in-container isolation is mandatory despite the native-runtime decision, what approved macOS-VM arrangement, if any, meets graphics/account/performance requirements?

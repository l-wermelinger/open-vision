# Product requirements and delegated decisions

Updated: 2026-11-02. **This is a requirements contract, not evidence of a working product.** The owner delegated remaining product decisions to the implementing agent. Task status and implementation phases live only in [workstream.md](workstream.md).

## 1. Outcome

Present as much of **Apple's actual visionOS Simulator environment** as is technically and legally supportable on an original consumer PICO 4, rendered by the owner's Mac Studio with low overhead. Preserve a path to another Apple-silicon Mac, such as a Mac mini, and later compatible headsets.

The owner must be able to sign into the supported simulated environment with their **real Apple Account**, not only a demo account, and use the Apple services actually demonstrated there. A dependable MacBook extended-display workflow remains a core end goal.

“Almost fully working” is not a waiver of missing features. It means a complete, tested experience within a published capability matrix, with unsupported retail-device features identified explicitly. A flat preview, a lookalike launcher, fabricated account acceptance or a showcase that cannot perform real work does not satisfy this contract.

## 2. Requirement priorities

| ID | Requirement | Acceptance boundary |
|---|---|---|
| R-01 | Authentic simulated environment | Apple's supplied system UI and compatible apps render from the Mac-hosted Simulator. Do not replace them with imitation assets or a new shell. |
| R-02 | Spatial presentation | Separate eye views, calibrated projection, six-degree-of-freedom head pose, stable recentering and a tested presentation path. Repeating one flat image in both eyes fails. |
| R-03 | Controller-first natural interaction | Controller aiming supplies target selection; trigger press/release becomes native pinch/select/drag behaviour. Prove it across system UI and apps, not just a custom test scene. |
| R-04 | Real Apple Account | The owner manually signs into the actual simulated system account UI, completes ordinary two-factor authentication, demonstrates at least one real iCloud operation, and verifies session persistence. Xcode signing, a StoreKit sandbox account or a web login alone does not count. |
| R-05 | Lightweight target deployment | One active Simulator device/session, native hardware-assisted rendering/encoding where supported, no unnecessary UI engine or VM, measured incremental load and a clean stopped state. No invented performance claim. |
| R-06 | Container request handled honestly | Record that ordinary Linux/OCI containers do not host Xcode/visionOS Simulator. Use a native macOS runtime boundary by default; containerize only genuinely useful auxiliary services. This is not literal full-runtime containerization. |
| R-07 | Actual MacBook workspace | Support genuinely extended desktops without physical monitors, with a first acceptance target of two different desktop surfaces, correct input/focus and safe display restoration. Verify native Mac Virtual Display first; implement a separate receiver only if necessary. |
| R-08 | Safe lifecycle and connection | Pair authorized peers, encrypt private media/control traffic, preserve headset safety controls, provide host-local stop/recovery, and test disconnect and sleep/wake. |
| R-09 | Reproducible compatibility | Pin the tested Mac/macOS/Xcode/runtime/headset/firmware/client tuple. Do not generalize original PICO results to Ultra/Enterprise, or historical Quest results to PICO. |
| R-10 | Honest distribution | Ship original/licensed tooling, not Apple runtimes, unlicensed upstream implementations, private account state or protected assets. Provide an accurate feature matrix and installation/recovery instructions. |

R-01 through R-10 are end-goal acceptance requirements, not checked-off capabilities. If an essential requirement is blocked, publish a bounded research result and say the product is incomplete; do not silently lower the goal.

## 3. Decisions the next agent should not reopen as preference questions

### Host and development machines

- **Target host:** the existing Mac Studio. The connected MacBook/PICO arrangement may be used as an explicitly authorized development fixture, not as proof of Mac Studio deployment.
- **Default final transport:** direct local-network Studio-to-PICO media/pose traffic. Prefer existing Ethernet for the host and available 5 GHz Wi-Fi for PICO when suitable; measure first and do not buy a router by default.
- A USB cable connected to the MacBook is useful for authorized deployment/debugging. It does not automatically create a Studio-to-PICO video path. Do not add an unmeasured MacBook relay to the normal architecture.
- A direct USB transport is an optional later profile after compatibility is demonstrated. Keep the implementation independent of a mandatory internet service.

### Container and isolation boundary

**Researched:** Docker Desktop on Mac runs Linux workloads, and Apple's `container` likewise runs Linux containers in lightweight VMs. Xcode's requirements are macOS/Apple-silicon specific. Sources S43-S45.

**Engineering decision:** run the actual Simulator and its tightly coupled bridge natively in an authorized macOS GUI user session, managed as a bounded per-user service. Isolate its device data, configuration, logs and child-process lifecycle. This is process/data isolation, not a security-equivalent container or a claim of full sandbox confinement.

Do not add Docker solely to supervise an application that must remain on macOS. If a later control/relay service benefits from an OCI image, it must communicate through a narrow authenticated host interface and must not receive host-wide privileges or account-state mounts. No auxiliary container is required for the first working release.

A real macOS VM is a separate alternative, not a Linux container. Evaluate it only if stronger isolation becomes necessary and graphics, Xcode, nested Simulator behaviour, account compatibility and resource costs are actually demonstrated. Apple's macOS-VM iCloud support does not prove visionOS Simulator iCloud support inside that VM. Sources S46-S47.

**Unmet literal request:** the entire Apple Simulator stack in a normal Linux container is not the selected supported design. If literal all-in-container execution is non-negotiable, record a blocker rather than fake a Docker deployment. Do not quietly relabel native macOS processes as a container.

### Input contract

| Physical action | Required simulated meaning | Implementation note |
|---|---|---|
| Move the headset | Viewpoint position/orientation | Not eye gaze and not target selection. |
| Aim the active controller | Native target/focus ray | Translate coordinate spaces explicitly; do not claim genuine eye tracking. |
| Trigger down/up | Pinch begin/end or native equivalent | Use hysteresis/debouncing appropriate to actual button/axis data. |
| Hold trigger while moving | Native pinch-and-drag | Interact with window handles and app content through their normal interaction path. |
| Two controller pinches | Native two-hand gesture where supported | Prove multi-input handling before advertising resizing/rotation. |
| Thumbstick motion | Native scroll/swipe or navigation gesture | Capability-gated mapping, not raw gamepad control of the simulated OS. |
| App-level menu action | Recover/recenter/disconnect controls | Do not hijack the PICO system/safety button. Keep remapping possible. |
| Physical Mac keyboard/trackpad | Text entry and normal Mac work | Allowed as productive input and local recovery, not a substitute for controller operation of visionOS. |

The controller-point/trigger choice came from the owner. Remaining mappings above are delegated defaults, subject to technical validation rather than further preference interviews. Select a sensible primary hand from actual input availability and offer left/right switching; do not assume handedness.

**First input milestone:** native system-wide semantic gestures, with no ordinary desktop cursor or gamepad-style interaction presented as the product. Apple's own pointer-to-simulated-gaze/gesture facilities may be investigated as an implementation mechanism; a controller clicking a flat desktop preview is not sufficient.

**Next compatibility layer:** synthesize calibrated wrist/hand/finger poses for APIs and apps that require articulated hands. Generate only the states supported by controller inputs, with continuity and a neutral resting pose. Document synthetic data as synthetic. A real hand-tracking app must receive usable joint data before it is listed as supported.

Do not hold standard system UI hostage to photorealistic hand rendering or custom eye-tracking hardware. Render lightweight virtual hands only where they help feedback or compatible apps require them; the native focus/selection feedback remains primary. Do not claim that semantic gestures alone provide full ARKit hand-skeleton support.

### Environment and polish

- Start with an opaque, comfortable simulated environment and an unmodified Apple interface. Real-room passthrough/occlusion is a later capability, not a prerequisite for the first complete workspace.
- Do not invent Apple-like overlays, use copied fonts/assets, or put a new launcher in front of the authentic interface.
- Prefer stable text, predictable focus, calibrated motion and a dependable exit over decorative effects.
- Preserve the headset's native safety boundary and system escape path.

## 4. Real Apple Account contract

Account compatibility is a **go/no-go investigation**, not a promise made by a successful video demonstration.

1. Establish the legal/SDK and version baseline first. The owner obtains Apple software and accepts applicable terms themselves.
2. On an authorized clean stock Simulator profile, let the owner perform ordinary account sign-in and two-factor authentication. Do not ask for passwords, recovery keys or verification codes in chat, tools, issues or agent prompts.
3. A separate ordinary test Apple Account may be used for preliminary safety checks, but it cannot satisfy R-04 by itself. The eventual owner account test is mandatory.
4. Test the actual simulated Settings/account state plus one owner-approved, non-sensitive iCloud synchronization operation, preferably a disposable iCloud Drive canary if that service exists in the runtime. Obtain approval before any cloud-data write. Do not read personal photos, contacts, messages or files to manufacture evidence.
5. Test relaunch/persistence. Then revalidate account behaviour after bridge integration and on the final deployment profile; a stock baseline is not proof that modified streaming preserves it.
6. Before authenticated content enters a stream, validate peer authorization and encryption. Use clean non-personal content in early stereo experiments. Keep credential entry, account screens and sensitive frames out of recordings and diagnostic archives.
7. Publish only sanitized pass/fail/service/version evidence. Keep simulator Keychain/session state private, local and persistent; never place it in a container image, release, CI artifact, cache shared with agents or committed fixture.

Do not disable two-factor authentication, Advanced Data Protection or other account protections; do not spoof device credentials/attestation or use stolen tokens. If the runtime or account policy rejects the required use, stop and report the exact capability boundary. A website sign-in fallback is not a system-account pass.

An account login does not imply support for App Store retail binaries, purchases/DRM, iMessage, FaceTime, Persona, Optic ID, AirDrop, Continuity or native Mac Virtual Display. Give each advertised service its own test and limitation. Managed-account policies and runtime-specific service availability must not be guessed.

## 5. Lightweight implementation policy

Prefer these implementation choices unless measurements or licence findings justify a documented deviation:

- A small Swift/macOS supervisor, a narrowly versioned native compositor adapter and a lean Android/OpenXR headset endpoint. Use Objective-C++/C++ only where the relevant native boundary needs it.
- Reuse an adequately licensed streaming/decoder path before creating a transport. No upstream project is adopted merely by this policy.
- Metal/native buffers and hardware encoding on Mac; hardware decoding on PICO. Avoid unnecessary frame copies and CPU readbacks. Software encoding is a diagnostic fallback, not the lightweight production target.
- H.264 is the initial compatibility candidate; evaluate HEVC only against actual decoder support, text quality, latency and power. Do not assume a codec or resolution fits the XR2 budget.
- Start from a 72 Hz headset presentation profile; negotiate actual supported stream rates and resolutions. A lower-rate diagnostic feed is not evidence of comfortable spatial use. Qualify 90 Hz only after a stable measured baseline.
- One active device, one active peer and no heavy resident worker when the session is stopped. Start/stop only project-owned resources; do not terminate unrelated Simulator, Xcode, model-server or homelab processes.
- No Electron control panel, general-purpose 3D engine, cloud relay, account broker, Docker daemon or VM added without a demonstrated need.

Performance evidence must include incremental idle/active CPU, resident/system memory, GPU/encoder load where observable, frame delivery/drops, latency estimates with measurement method, network throughput and effects on existing host workloads. Report p50/p95 where meaningful. Streaming overlay estimates are not automatically measured motion-to-photon latency.

Proposed validation runs are a 20-minute representative working session and at least three disconnect/reconnect plus sleep/wake cycles. These are test requirements, not existing measurements or a universal comfort guarantee. The first authorized baseline must establish an explicit resource/latency operating envelope before feature expansion; do not invent a universal MB, FPS or millisecond guarantee now.

## 6. Completion and stop rules

No product release claim until the relevant [workstream](workstream.md) gates pass, real owner account compatibility is rechecked, and the capability matrix identifies supported, unsupported and untested functions for the exact version tuple.

Stop the affected phase when a critical requirement cannot be met safely or legally. Continue independent repository research/tests where useful, but do not implement downstream features on top of a known failed account, stereo, input or licence premise. Escalate technical impossibilities and actual authorization needs, not routine product preferences the owner has already delegated.

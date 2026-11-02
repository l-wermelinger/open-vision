# Open Vision: feasibility research

- Research collected: **2026-11-01**
- Publication and scope update: **2026-11-02**
- Status: **Documentary findings only. No hardware validation or application implementation yet.**
- Initial headset assumption: **the original consumer PICO 4**, not Ultra, Pro or Enterprise.

**Current project direction:** host Apple's visionOS Simulator on an Apple-silicon Mac, such as a Mac mini or Mac Studio, and stream its spatial view stereoscopically to an existing VR headset with pose/input return. Section 5.6 contains the key historical evidence. The [requirements contract](../product-requirements.md), [architecture](../architecture.md) and [phased workstream/handoff](../workstream.md) describe the selected scope, delegated decisions and validation gates. Full retail visionOS functionality is not established by Simulator support. The Open Vision name has not undergone trademark clearance.

This report preserves the research progression. Sections 1 and 6-9 also examine an independently rendered Mac-workspace alternative; those recommendations must not override the subsequently selected authentic-Simulator goal.

## 1. Initial independent-workspace assessment

**Your most important goal is achievable: use your real MacBook through large, spatially arranged virtual screens, including genuine additional macOS desktops.** Existing commercial applications already demonstrate this on Pico 4. An open-source implementation is also a credible project.

**The independent-workspace alternative is not a visionOS port.** It would be a standalone Pico application, using Pico's existing tracking and compositor, plus a native macOS companion. The Mac runs your actual Apple applications. The headset displays and spatially arranges their output.

That can deliver:

- A quiet, polished workspace with floating and curved displays.
- Real extended Mac desktops, not three copies of the same screen.
- Your existing Mac keyboard, trackpad, applications and Apple account environment.
- Automatic discovery of a previously paired Mac.
- Passthrough around your desk, subject to Pico's hardware and runtime capabilities.
- An independently implemented interface inspired by spatial design principles.

It cannot turn the original Pico 4 into a Vision Pro optically, add missing eye-tracking cameras, run native visionOS applications, or acquire Apple's proprietary ecosystem entitlements by imitating the interface.

**For a dependable daily Mac workspace:** validate the work experience with existing software first, then investigate a Pico port of **PippinVR** before writing a streaming/display stack from scratch. Treat the Apple-like shell as the refinement layer, not the first engineering milestone.

**Follow-up finding, 2026-11-01:** the design proposal shifted to hosting Apple's visionOS Simulator on an Apple-silicon Mac and streaming it to Pico. Targeted research found a historical implementation of precisely this architecture: `VisionOSStereoScreenshots`, branch `alvr`, streamed stereo compositor output and used incoming headset pose data. This materially strengthens the authentic-simulator experiment compared with the initial assessment. It is not a working modern-Pico solution: the documented setup uses 2023 betas, current compatibility is unverified, and a later user reports failure on visionOS 26.2. See section 5.6. The two routes should not be conflated.

## 2. An important correction about Apple's feature

Apple's Mac Virtual Display is not a general facility for cloning a Mac into an unlimited collection of independent Mac monitors in space.

Apple currently documents:

- One connected Mac at a time.
- One Mac Virtual Display surface, with Standard, Wide or Ultrawide aspect ratios.
- Only the main display is shown when the Mac has several physical displays.
- A curved Ultrawide mode up to 10240 × 2880 backing pixels, corresponding to 5120 × 1440 points, on supported Apple silicon/macOS combinations.
- A laptop can show a Connect button when you look at it.

The basic requirement is macOS Sonoma 14 or later. Wide/Ultrawide requires Apple silicon, macOS Sequoia 15.2 or later and visionOS 2.2 or later. Apple's pairing experience additionally requires Wi-Fi, Bluetooth, the same Apple Account with two-factor authentication and iCloud Keychain. These are **Apple's product requirements**, not requirements we must reproduce for an independent local streaming application. [S02]

Your proposed two or three independently arranged Mac screens is a valid design, but it is partly a different product. We could offer both multiple desktops and one curved ultrawide desktop. Neither means every streamed Mac application becomes a native visionOS window.

## 3. What is possible, conditional or unavailable?

| Desired capability | Assessment | What it really means |
|---|---|---|
| Display the MacBook in VR | Achievable now | Existing Pico-compatible products support Mac desktop streaming. |
| Create additional Mac screens without buying monitors | Achievable | The host must create real virtual displays, then capture and stream them. |
| Place, resize and curve screens in space | Achievable | The headset owns the spatial layout and renders it locally. |
| Use the MacBook's keyboard and trackpad | Achievable | Leave them connected to the Mac initially. No remote input injection is necessary for basic work. |
| Use Safari, Xcode, Messages, Notes and other Mac apps | Achievable through the Mac | They run on macOS and are streamed. They do not run locally on Pico. |
| Discover a nearby Mac and offer Connect | Achievable with a companion app | Bonjour/mDNS discovery plus explicit initial pairing. Discovery identifies a network device, not its physical position. |
| Automatically draw a panel exactly above the real MacBook | Conditional | Requires reliable physical pose estimation or manual calibration. Network discovery alone cannot do it. |
| See the desk/keyboard through passthrough | Feasible, quality-limited | Seeing passthrough is different from obtaining camera pixels for computer vision. |
| Hand/pinch interaction | Plausible, runtime-dependent | Validate support and quality on this exact Pico and firmware. Keep controller/trackpad fallbacks. |
| Eye-targeting like Vision Pro | Not equivalent on original hardware | Original consumer Pico 4 has no built-in eye-tracking system. Head direction is not eye gaze. |
| Apple-quality passthrough and text sharpness | Not attainable by software alone | Camera, optics, display and compute differences remain. |
| Launch arbitrary visionOS/iPadOS binaries on Pico | No supported practical route | There is no compatible Apple app/framework/runtime environment on this headset. |
| Native AirDrop, Handoff, Optic ID and full Apple Continuity | Not an established feature path | Independent implementations of some protocols exist, but there is no public all-in-one entitlement or SDK for making Pico an Apple device. |
| Use Apple's official Mac Virtual Display protocol directly | Unverified, not a foundation | No documented general-purpose receiver API was established in this research. Protocol research would be a separate, risky workstream. |
| Replace Pico OS but retain all tracking and device features | Not a sensible starting point | Would require solving firmware, drivers, tracking, compositor and platform integration, not just writing a launcher. |
| Publish an open-source application | Achievable | Your application can be open source while macOS and Pico's underlying firmware/runtime remain proprietary. |

“Unverified” is not the same as physically impossible. The table deliberately separates absent hardware, missing public integration, legal restrictions and engineering work.

## 4. The physical ceiling: what software cannot fix

### 4.1 Text clarity is the first thing to test

Pico's original specification lists:

- 2160 × 2160 pixels per eye.
- Approximately 20.6 pixels per degree, as a manufacturer figure.
- Fast-LCD displays, pancake optics and 72/90 Hz refresh.
- Snapdragon XR2 Gen 1 and 8 GB RAM.
- Wi-Fi 6 on 2.4/5 GHz, not a promise of 6 GHz Wi-Fi 6E. [S01]

There are about **9.33 million panel pixels across both eyes**. Apple's current Vision Pro specification lists **23 million pixels**, micro-OLED, dedicated eye-tracking cameras, stereo main cameras, depth sensors and separate R1 sensor-processing hardware. This is not an exact sharpness ratio: field of view, optical distortion, panel utilization, subpixels and render resolution all matter. It is nevertheless a substantial hardware difference. [S03]

A simple illustration: at the advertised 20.6 pixels/degree, a virtual monitor spanning 50 degrees has roughly 1030 panel samples across that angular span. This is an intuition-building calculation, **not a measured usable-resolution benchmark**. A source stream labelled “4K” does not give a 4K virtual monitor its own 3840 physical pixels across the Pico's view.

Rendering at higher resolution and good filtering can reduce aliasing. Sharpening can make edges more legible. Neither adds physical display detail. AI enhancement cannot reliably reconstruct missing code characters and should not be sold as a solution to code readability.

**Practical consequence:** start with a large central working display, larger fonts and perhaps one side display. Three small dense 4K desktops are a poor first success criterion. The issue is not whether we can draw three rectangles; it is whether you enjoy reading them.

### 4.2 Passthrough cannot become Vision Pro's sensor system

The original Pico 4 uses one central colour camera for its colour view, unlike a stereo colour-camera system. UploadVR's launch review explains that its delivered stereo viewpoints are synthesized and describes scale/distortion limitations. That review is from 2022, so it is evidence about hardware and launch behaviour, **not proof that every software limitation remains unchanged in 2026**. [S31]

Software can improve reprojection and estimated geometry. It cannot recover all independently observed viewpoints and hidden surfaces that a different camera arrangement would have captured. We should expect a worse view of the physical keyboard and room than a Vision Pro, especially in difficult lighting and near-field situations.

Offloading room video to another machine does not remove sensor placement, network delay or information-loss limits. Keep headset tracking acquisition and safety boundaries local; a remotely rendered simulator still needs an explicit pose-return and presentation-timing path.

### 4.3 Eye tracking is a genuine hardware boundary

The original consumer Pico 4 must not be confused with Pico 4 Pro/Enterprise. The Enterprise variant has eye/face-tracking features and different provisioning. Sources that say “Pico 4 supports eye tracking” without identifying the variant are unsafe to use as specifications. [S01, S32]

Without eye-facing sensors, we cannot reproduce Vision Pro's gaze-targeted selection. We can offer:

- Trackpad/mouse interaction.
- Controller pointing.
- A head-directed cursor.
- Hand pointing and pinches where supported.

These can be polished. They are not eye tracking. An eye-tracking add-on would be another hardware project, not a software unlock.

### 4.4 Latency and comfort remain empirical

There are two different latency problems:

1. **Head motion to scene update:** the headset runtime should handle this locally at its supported refresh rate.
2. **Mac input to updated screen content:** capture, encoding, transport, decoding and presentation all contribute.

A 60 fps Mac stream does not require the whole spatial scene to run at 60 fps. The headset can reposition a display using fresh tracking while reusing the latest decoded desktop image. That is a reason to stream desktop surfaces, not have the Mac render an entire stereo environment.

No latency, battery-life or long-session comfort measurements were performed in this research. A claimed fast codec does not establish comfortable end-to-end work on your network.

## 5. Existing software: test before rebuilding

### 5.1 PICO Connect: the no-purchase baseline

PICO's official download page lists a macOS client and desktop access from Windows and Mac. It specifies PICO OS 5.11.2 or later for Connect. [S04]

**Use it to establish:** that your Mac and Pico can connect, what the basic desktop experience looks like, and whether your normal font sizes are usable.

**Do not assume:** that the original Pico 4 receives every multi-screen/PanoScreen capability advertised for Pico 4 Ultra. The opened download page does not establish genuine additional macOS desktops for this exact original-headset combination.

### 5.2 Immersed: closest ready-made match to your primary goal

Immersed's FAQ and PICO store listing explicitly include Pico 4 and Mac. Its documentation says PC and Mac can create virtual displays without extra physical monitors. This is directly relevant to your requested feature, not merely screen mirroring. [S05, S06, S36]

Useful caveats:

- The more specific help page lists Apple silicon Macs with macOS 11.7+, while the broader FAQ says macOS 11+. Use the stricter requirement until your actual Mac is checked.
- Immersed's restriction on **multiple physical monitors** is separate from its support for **multiple virtual displays**. The FAQ explicitly says it does not support multiple external displays or display emulators on Windows/Mac. This particularly matters when testing the Mac Studio with several physical monitors.
- A Pico 4 USB mode is documented as beta. Its setup is specific and includes unusual cable guidance. It is not evidence that every USB cable/configuration works. [S07]
- Pricing and entitlements have changed over time; the site contains both older subscription/streak language and newer navigation. Exact current free screen counts, resolutions and paid terms were **not verified**. Do not pay based on a remembered price in an old review.
- Pico hand tracking, passthrough features and current store availability must be checked on the device. General Quest feature announcements are not Pico feature guarantees.

**Verdict:** the best first benchmark for “can I genuinely work with extra Mac screens on my current headset?” It is proprietary and is not source material we can copy.

### 5.3 Virtual Desktop: a strong second benchmark

The official site lists Pico 4 and macOS support. Its published release history establishes that:

- The 2024 multi-monitor release specified up to **two simultaneous monitors on original Pico 4**, compared with three on Quest 3.
- The macOS streamer rewrite added built-in virtual-monitor creation, so old advice saying a Mac always needs BetterDisplay is obsolete.
- A 2026 update added 21:9 Mac virtual-monitor resolutions.
- The latest retrieved release was 1.34.22, published 2026-10-22. [S08, S09]

The two-monitor Pico figure is the explicit headset limit in the retrieved multi-monitor announcement. It should be treated as the **documented baseline**, not a freshly measured limit across every later release. Recheck the installed version before promising a particular count.

Its Mac desktop support does **not** mean Windows SteamVR game streaming works from a Mac. The official FAQ makes that distinction.

**Verdict:** useful for comparing clarity, latency, curved screens and interaction quality. Proprietary, generally a store purchase; no purchase was made and no local price was verified.

### 5.4 Open source: PippinVR is the most directly relevant finding

[PippinVR](https://github.com/triscuitcircuit/PippinVR) specifically targets the problem of proprietary macOS VR screen software. Its documented architecture is unusually close to this project's need:

- Native Mac server with virtual-display creation.
- Per-display capture and encoded streams.
- An Android/OpenXR headset client.
- Multiple movable display panels.
- USB/ADB transport in its APK mode.
- GPLv3 licensing. [S10, S14]

**But its documented headset support is Quest, not Pico.** The sampled client manifest contains Oculus-specific features and a required passthrough feature. The code negotiates `XR_FB_passthrough`; the build uses the Khronos Android OpenXR loader. This is a plausible portability starting point, but “uses OpenXR” does not mean “already works on Pico.” [S13]

There are two different Pippin paths:

- **QuestLink USB mode:** Quest-specific. Do not make this the Pico plan.
- **Sideloaded Android APK mode:** the plausible Pico adaptation route, after runtime, manifest, input, decoder and transport checks.

Repository snapshot on 2026-11-01:

- Created 2026-09-24.
- Last push 2026-10-31.
- Release v1.2.0 published 2026-10-31.
- 13 stars; one non-bot contributor in the retrieved contributor list.
- Examined main revision: `75ed33cce8235e1c05bb66c2942ad3653c1d4954`. [S11, S12]

This indicates a **very young project**, not a mature proven platform. Its README itself lists stale panels after disconnect and wake-related issues. The research sampled architecture and relevant source files; it did not compile the application or conduct a security audit.

**Verdict:** investigate adapting or contributing to this before inventing another Mac screen-streaming stack. An upstreamable Pico port could be a better open-source contribution than a permanent unrelated fork. Open Vision does not claim to have independently invented PippinVR's functionality; it is prior art for the independent-workspace alternative.

### 5.5 Other useful projects, and why they are not turnkey answers

| Project | Useful contribution | Why it is not already your solution |
|---|---|---|
| **DeskPad** | Small MIT-licensed macOS virtual-display example, including an explicit private-API header. | Not a VR client or screen-streaming product. [S17] |
| **Godot + OpenXR Vendors** | Open-source spatial UI/rendering foundation and vendor integration. | Still needs a high-quality hardware-decoding/network path and exact Pico validation. An old Pico passthrough issue was closed in January 2026; it illustrates SKU/deployment pitfalls, not proof of a current unresolved failure. [S18, S19] |
| **Sunshine + Moonlight-family clients** | Existing streaming, pairing, Mac ScreenCaptureKit and VideoToolbox support. Sunshine is GPLv3. | A single stream is not automatically several independently controlled Mac displays. Multi-stream/display orchestration still needs validation. [S20] |
| **Nightfall** | Active GPLv3 OpenXR/GameStream client with movable/curved screens and a Godot/native rendering pipeline. | README targets Quest and Linux PCVR, not confirmed Pico. Multiple monitors remain on its roadmap. Its stated progress percentage is the author's claim, not our readiness assessment. [S21] |
| **ALVR** | Pico-compatible open-source PCVR streaming reference. | Its current compatibility matrix explicitly marks macOS unsupported as a server. [S22] |
| **WiVRn** | Pico-compatible open-source Linux PCVR streaming and runtime integration. | Its documented host is Linux, not a native Mac multi-display companion. [S23] |
| **Monado** | Open-source XR runtime/compositor and driver architecture. | The published native hardware matrix is not a turnkey replacement operating system/driver stack for original Pico 4. Using Pico through a streaming client is different from replacing Pico firmware. [S24] |
| **UxPlay** | Existing open-source AirPlay mirroring/audio implementation. | Shows some Apple-protocol interoperability is possible. Not an implementation of Apple's Mac Virtual Display or an out-of-box Pico multi-desktop shell. [S34] |

BetterDisplay is useful as an optional display-management diagnostic tool, but its current commercial app must not be described as open source simply because it has a GitHub repository. No dependency on it is necessary to establish the proposed architecture.

### 5.6 Follow-up: stream the actual visionOS Simulator from Mac Studio

**This is a credible experimental direction, with historical proof of concept.** It is substantially different from emulating an Apple SoC on the Pico: Apple's simulator runs on an Apple-silicon Mac, while the headset is a remote display and tracking/input endpoint.

Apple's current Xcode documentation describes the simulated visionOS environment, Home View, Control Center, pointer-driven simulated gaze/gestures, viewpoint navigation and simulated room scenes. The former Simulator interaction URL now redirects to Device Hub documentation. These are developer simulation facilities, not a guarantee of every retail Vision Pro application or service. [S37]

The most important prior art is [zhuowei/VisionOSStereoScreenshots, branch `alvr`](https://github.com/zhuowei/VisionOSStereoScreenshots/tree/alvr). Its README documents streaming visionOS Simulator to an original Meta Quest, tested on Apple silicon with Xcode 15 beta 2 and macOS 14 beta 2, using a particular ALVR nightly from 2023-07-06. It hooks CompositorService inside the simulated `backboardd`, substitutes its own render textures, then feeds them into an embedded/special-purpose ALVR server. This is **not ordinary capture of a flat Mac window**, and it does not contradict the current mainstream ALVR server's unsupported-macOS matrix. [S38]

Sampled source provides stronger evidence than a demonstration title:

- The compositor hook allocates separate left/right eye textures and combines them for streaming.
- It reads incoming headset position and orientation and updates the eye-view transforms and field of view.
- The miniature server accepts tracking data but leaves button handling empty; the README explicitly says to use the Mac's keyboard and mouse, not Quest controllers.
- A hard-coded 0.065 m eye offset and private structure layouts illustrate prototype assumptions that would need correction/validation for a comfortable current implementation. [S39]

A 2023 firsthand tester reports streaming the UI to a Quest 2 from an M2 MacBook Air, while noting low resolution, lag, simulated backgrounds and absent controller/hand/eye interaction. This is a useful historical observation, not a current benchmark or evidence that all Apple services work. [S42]

**Current obstacles are concrete:**

1. **Version fragility:** the retrieved `alvr` branch head dates to July 2023. Repository issues describe private API changes, injection/sandbox problems, and a December 2025 report of an unsuccessful attempt on macOS/visionOS 26.2. That report does not prove an updated bridge cannot work; it does rule out promising that the old recipe is current and turnkey. [S40]
2. **Pico compatibility:** the demonstrated target is Quest. The exact client/protocol/runtime combination still needs testing or adaptation for the original Pico. Do not assume a current ALVR APK speaks the old embedded server protocol.
3. **Simulator scope:** included simulator UI and simulator-compatible builds do not establish access to arbitrary purchased visionOS apps, hardware-backed services or Apple's native Mac Virtual Display. The latter remains unverified in Simulator; genuine MacBook screen extension may still need our own simulator-compatible receiver application and a MacBook companion.
4. **Interaction and latency:** stereo video alone is insufficient. Pose return, predicted display timing, recentering and input mapping must be correct. Streaming a whole remotely rendered scene introduces a different head-motion latency problem from locally positioned desktop panels.
5. **Safety/security:** a related historical tool, `XRGyroControls_OpenXR`, documents disabling SIP and library validation. Those requirements belong to that tool and must not automatically be attributed to every ALVR bridge, but they are a serious reason not to run archived scripts blindly on the homelab server. No such changes have been made. [S41]
6. **Redistribution:** the inspected `alvr` branch tree has no top-level licence file and GitHub's repository metadata reports no detected licence. Public source is not itself an unrestricted open-source redistribution grant. Clarify permission/provenance before incorporating it into a public project, and review Apple SDK/Simulator terms. Do not redistribute Apple runtime images. [S38, S40]

The experimental architecture would be:

```text
Mac Studio: Xcode visionOS Simulator
  simulator compositor -> separate eye images -> encoder/stream bridge
                                            |
                                         network
                                            |
Pico 4: decode/present stereo views <-> return headset pose and mapped input
```

**Next evidence gate, if this route is chosen:** inspect the Mac Studio's installed macOS/Xcode/runtime versions without changing them; identify a version-compatible bridge; then demonstrate a stereo scene that follows head movement before adding MacBook streaming or custom eye tracking. Investigate modern supported hooks and isolation before accepting any security downgrade. Do not download old packages, inject code, alter the server or start an implementation without approval.

This finding changes the simulator route from a generic possibility into an architecture with a historical working example. It does **not** establish a production Vision Pro replacement, a modern Pico build, or a delivery schedule.

### 5.7 Follow-up: container placement, real accounts and the actual SDK terms

The owner subsequently required lightweight Mac Studio hosting, asked for container isolation and made real Apple Account compatibility mandatory rather than a demo-only feature. These are now explicit requirements, not established runtime results.

**Container boundary:** Docker Desktop on Mac runs Linux workloads, and Apple's own `container` project explicitly runs Linux containers in lightweight VMs. Apple's Xcode matrix requires macOS and Apple silicon for visionOS development. A normal Linux/OCI image therefore cannot directly supply the native Simulator stack. The selected engineering default is a native per-user Mac worker with separate device data and scoped lifecycle, plus an auxiliary container only if it earns its overhead. That is not literal full-runtime containerization or equivalent security confinement. Sources S43-S45.

A real macOS VM is a different possible isolation boundary. Apple documents iCloud access for properly created macOS 15+ VMs on compatible Apple-silicon hosts, including identity and reauthentication constraints. This prevents a blanket claim that virtualized Apple accounts are impossible. It does **not** prove visionOS Simulator account compatibility inside a guest, nested graphics support or acceptable overhead. Those remain separate tests. Sources S46-S47.

**Account boundary:** the selected runtime must be tested with the owner's real account through its actual simulated account UI, ordinary two-factor authentication, an approved non-sensitive real iCloud operation and persistence. Xcode developer signing, a StoreKit sandbox account or website login alone is not equivalent. Recheck after adding the bridge and in the final deployment. No such owner-account test was performed during research; historical S42 is not a current guarantee.

**Material SDK permission finding:** the retrieved Xcode and Apple SDKs Agreement defines simulators within Apple SDKs. Section 2.2.A(iii)-(iv) restricts relevant SDK/services use to testing/development for applicable Apple-branded products; section 2.7 includes network/server, non-Apple, modification and redistribution restrictions, with its stated legal/open-source qualifications. A general-purpose end-user workspace and its hooks therefore need specific SDK/intended-use review. Using an Apple host is not itself a legal determination. Source S48. This is not jurisdiction-specific legal advice or a conclusion about every statutory interoperability exception.

The implementation plan puts version/reuse/SDK review, authorized device inventory, real-account feasibility and the deployment/resource baseline in Phase 0. Standard system-wide controller-to-native-gesture behaviour precedes full articulated-hand compatibility; low-cost native media paths are preferred to an engine or VM. None of these decisions makes a presently unverified feature work.

## 6. Alternative architecture: a locally rendered Mac workspace

```text
MacBook or Mac Studio
  Real macOS apps and normal Mac input
      |
  Create/manage virtual displays
      |
  ScreenCaptureKit -> VideoToolbox hardware encoding
      |
  Explicitly paired transport (USB first, secured LAN later)
      |
Pico 4 application
  Hardware decode -> desktop textures / supported composition layers
      |
  Locally rendered panels, layout, interaction and environments
      |
  Existing Pico OpenXR runtime, tracking, passthrough and safety boundary
```

### 6.1 The Mac companion

A native Swift/AppKit or SwiftUI companion is a good fit. For a Pippin adaptation, start with the existing companion rather than rewriting it to satisfy a preferred language style.

Separate these jobs conceptually:

1. **Display creation:** make an extra desktop that macOS recognizes.
2. **Capture:** obtain images of that desktop or a selected application window.
3. **Encoding:** turn those images into a low-latency compressed stream.
4. **Connection management:** pair, connect, reconnect and stop safely.

Apple publicly documents **ScreenCaptureKit** for capture and **VideoToolbox** for hardware-assisted encoding/decoding. Screen capture requires user consent. These public frameworks are useful building blocks; neither is the entire virtual-display solution. [S15, S16]

The sampled Pippin implementation creates displays through `CGVirtualDisplay*` classes resolved at runtime. DeskPad similarly exposes an explicitly named `CGVirtualDisplayPrivate.h`. **The display-creation method in these candidates is private/undocumented.** That is a real compatibility and distribution risk, not a minor detail to hide. [S14, S17]

Consequences:

- Test on the user's actual macOS version before choosing a minimum supported version.
- Expect OS updates to require compatibility work.
- Fail gracefully if display creation is unavailable.
- Keep a plain mirrored-display fallback.
- Do not assume Mac App Store eligibility. Direct distribution and notarization need their own checks; notarization does not make a private API supported.
- Preserve and restore display arrangement on normal exit, disconnect and crash recovery. Never leave the user unable to find their windows.

Do not confuse Apple's physical external-monitor limits with the count of software virtual desktops. They are different mechanisms, but neither implies infinite free capacity. Capture, encoding, WindowServer load, RAM and headset decoding still constrain the useful count.

### 6.2 The headset application

The headset should own head-tracked placement and draw the panels locally. Use hardware decoding rather than moving every frame through CPU image copies if a viable existing path can be reused.

First portability checklist for Pippin's APK mode:

- Confirm supported Android/OpenXR loader and runtime versions on original Pico 4.
- Adjust Quest-specific manifest requirements and launch categorization appropriately.
- Bind Pico controller interaction profiles.
- Enumerate supported passthrough and composition extensions at runtime.
- Start with opaque VR if passthrough support needs investigation.
- Verify decoder formats, resolution limits and the number of simultaneous hardware-decoded streams.
- Verify USB/ADB connectivity from macOS to this actual Pico.
- Handle recenter, headset sleep/wake and reconnect correctly.

A capability probe, not a generic “Pico supported” checkbox, should drive optional features. PICO publishes Unity OpenXR tooling, but the existence of a vendor SDK does not force us to use Unity or grant every API to every Pico model. [S25]

If the existing native client proves unsuitable, **Godot with the OpenXR Vendors plugin plus a native decoding integration** is a reasonable alternative for the independent shell. Unity with the official Pico SDK is another integration-first option, but it adds a proprietary engine/toolchain dependency. Do not commit to either fallback before the direct reuse path has been measured.

The newer Kotlin PICO Spatial SDK samples explicitly target **PICO OS 6**. We have not established that those APIs run on an original Pico 4. Marketing for new PICO hardware/OS 6 is not evidence of compatibility with this headset. [S33]

### 6.3 Transport: reuse first, secure deliberately

For the first controlled validation, USB is attractive because it reduces Wi-Fi variability and Pippin already documents an ADB path. This is an engineering experiment, not a claim that ADB is an ideal consumer onboarding experience.

For a polished wireless product:

- Discover candidates through Bonjour/mDNS.
- Require explicit initial user approval and an authenticated pairing exchange.
- Encrypt desktop content and input/control messages.
- Store appropriate long-term credentials in the Mac Keychain and Android's secure storage facilities, subject to device support.
- Reconnect only to authorized peers; provide revoke/disconnect controls.
- Do not interpret “same Wi-Fi” or an mDNS name as authentication.
- Do not open router ports or enable internet access by default.
- Handle denied permissions, firewall/VPN interference and network loss without losing windows.

No security properties are inferred from Pippin's README. Before repurposing a wired/debug-oriented protocol for wireless use, examine it explicitly. We have not established its suitability for untrusted networks.

A new custom transport is not automatically the best choice. Compare reusing Pippin's existing wired path and an established secured streaming stack before deciding. WebRTC can provide established encrypted media transport, but codec control, native decoder integration, overhead and dependencies still need measurement.

### 6.4 What “native Apple stuff” should mean in this project

The strongest honest proposition is:

> Your real Apple apps, on your real Mac, presented in an independently built spatial workspace.

Keep Messages, Notes, Xcode, Safari, Keychain and iCloud on the Mac. You retain the Mac's actual logged-in environment, rather than building imitations of Apple apps or asking for Apple account credentials on the headset.

Later, ScreenCaptureKit window capture could make selected Mac windows appear as separate panels. But this is more than cropping desktop images: focus, menus, sheets, dialogs, window movement and coordinate mapping all need careful handling. Some protected content cannot be captured normally. An individual video panel is still not a local volumetric application.

Apple Watch unlock and other existing Mac-side integrations can remain Mac-side. They do not imply the Pico acquires Apple Watch pairing or Continuity capabilities. Similarly, ordinary Bluetooth audio support does not imply Apple's full AirPods ecosystem behaviour.

## 7. Recognizing the MacBook: split the problem in two

### Network recognition

A paired Mac companion can advertise a service. The Pico can show “Connect to this Mac” when that service becomes available. This is practical and does not require reverse-engineering Apple's display protocol.

mDNS discovers services on a reachable local network. It does not prove which device is beside you, determine a laptop's pose, or establish trust without pairing. Bluetooth signal strength is also not a reliable six-degree-of-freedom laptop tracker.

### Physical recognition and anchoring

To draw the display exactly above a physical MacBook, the application needs a relationship between the laptop and the headset's tracking coordinates.

Start with one of these:

1. Place the virtual display manually above the laptop.
2. Use a controller to calibrate a small number of desk/laptop reference points.
3. Save a layout relative to the room reference, while accounting for recentering and possible drift.

Automatic identification could later use a visual marker, the displayed laptop screen, or a recognition model. **That requires camera access and usable calibration, not just visible passthrough.** An external camera or phone is another possible research route, but introduces its own cross-device coordinate-registration problem.

The evidence is nuanced:

- Enterprise camera-access examples explicitly require Pico 4 Enterprise provisioning.
- PICO's newer Integration SDK includes `PXR_CameraImage` APIs.
- Neither observation establishes that unrestricted image access is available on the original consumer Pico 4 with the user's firmware and permissions. [S26, S27]

Therefore automatic laptop recognition is **conditional and unproven**, not something to promise and not something to declare universally impossible. A hardware capability test or vendor confirmation is the next evidence needed. Core Mac screen extension does not depend on solving it.

## 8. Why porting or copying visionOS is the wrong route

### Technical reason

An Apple firmware download is not the original visionOS source repository. Decompilation does not recover the complete original Swift/Objective-C code, build system, assets and behavioural specification in a form we can simply recompile for Android.

Both devices having ARM CPUs does not supply:

- Compatible boot/firmware and security mechanisms.
- Display, camera, sensor and power-management drivers.
- Pico tracking integrated into Apple's system.
- Apple frameworks, app services and compositor behaviour.
- The Apple hardware and credentials on which protected services depend.

Apple publishes certain open-source projects and components. That is not a publication of the complete visionOS spatial shell or permission to redistribute all of visionOS. Each genuinely open component has its own licence. [S35]

A simulator can help study documented interaction behaviour on a Mac. It does not make the simulator a production Pico operating system or solve headset tracking and display integration.

I am **not** claiming that every aspect of firmware research or emulation is forbidden by physics. I am saying that no supported practical port was established, and doing this would solve a vastly different problem from your actual Mac workspace.

### Legal reason

Apple's retrieved visionOS 26 licence restricts use to an Apple-branded device and restricts copying, decompilation, reverse engineering and derivative works, with express qualifications for applicable law and open-source components. The Apple Developer Program agreement similarly restricts use on non-Apple devices and reserves rights. [S28, S29]

The important distinction:

- Observing public behaviour and independently implementing a workspace is not the same as copying Apple's code.
- Limited interoperability analysis may have legal exceptions depending on jurisdiction and circumstances.
- Those exceptions are **not blanket authorization to copy visionOS into a public repository**, translate decompiled proprietary code, or redistribute Apple firmware/assets.
- “AI rewrote it,” “we changed the variable names,” “it is free,” and “it is open source” do not themselves establish permission.

This report is technical feasibility guidance, not a jurisdiction-specific legal opinion. Obtain suitable legal review before undertaking proprietary protocol reverse engineering, accepting decompiled code, or publishing a close commercial lookalike.

### A viable independent-implementation policy

- Use public documentation and observed workflows as behavioural references.
- Implement original source code, original assets and an original identity.
- Reuse genuinely open-source components under their licences and preserve attribution.
- Do not import leaked code, extracted Apple frameworks, firmware, icons, wallpapers or other restricted assets.
- Do not bundle SF Pro/San Francisco fonts or SF Symbols on Pico without an applicable licence. Use appropriately licensed alternatives. The Mac companion can use macOS's normal system UI; streamed Mac text is not a licence to extract and redistribute its font files. [S30]
- A clean-room development process can reduce copyright-contamination risk. It does not automatically resolve patents, trademarks, trade dress, design rights or contractual questions.
- If code is derived from GPLv3 PippinVR or Nightfall, preserve applicable GPL obligations. Do not simply put an MIT label on the derivative. Using separate programs and protocols presents a different licensing analysis from copying/linking their code.

**Apple-like quality is a sensible goal. An Apple-branded or pixel-for-pixel counterfeit OS is not the proposed project.**

## 9. Validation gates for the independent-workspace alternative

These are evidence gates, not a promised schedule. Nothing below has been executed on your headset.

### Gate A: is the original Pico good enough for your actual work?

Use PICO Connect and, where available, Immersed as baselines. Consider Virtual Desktop only after checking purchase terms or if you already own it.

Test with real tasks:

- A normal Xcode/VS Code or terminal session.
- Browser documentation beside the editor.
- Light and dark text themes.
- The font sizes and display distances you would genuinely tolerate.
- A central display and one side display, then more only if useful.
- Passthrough keyboard visibility versus an opaque environment.
- A sustained session long enough to notice discomfort, not just the initial novelty.

Record: exact headset SKU/firmware, Mac model/chip/macOS, app versions, stream resolution/rate, network or USB path, text legibility, tracking stability and subjective comfort. Do not turn a vendor's “4K” setting into a claimed measured result.

**Decision:** if the best existing implementation is fundamentally too blurry or uncomfortable, a custom shell cannot guarantee a fix. Improve measured rendering/encoding issues where possible, but do not blame every optical limitation on someone else's UI. No new hardware purchase is recommended from this research alone.

### Gate B: can we reuse PippinVR on Pico?

In a controlled development checkout:

1. Audit the small set of relevant build/runtime dependencies and licences.
2. Establish that Pippin's Mac companion can create and cleanly remove one virtual display on the actual Mac.
3. Run its APK path on the Pico after the necessary platform adaptation.
4. Verify one readable stream with normal Mac keyboard/trackpad input.
5. Verify two real extended displays and coordinate/layout correctness.
6. Verify disconnect, cancellation, app quit and headset sleep/wake cleanup.
7. Measure performance and decoder limits before adding more screens.

Prefer an upstreamable port. If the existing design has a blocking quality, security or portability problem, document it before choosing a narrower independent implementation.

**Decision:** select “contribute/adapt Pippin,” “reuse another proven stream pipeline,” or “build the minimum independent companion/client” based on this evidence. The research does not justify pre-creating a new compositor, protocol or plugin ecosystem.

### Gate C: add the qualities that make it your workspace

Once screen extension is reliable:

- Friendly pairing and automatic reconnect.
- Saved layouts, recentering and a dependable emergency disconnect.
- Restrained materials, original typography/icons and clear depth cues.
- Predictable grab/resize interactions and interruptible motion.
- Mac/VR pointer arrangement that does not strand the mouse between displays.
- Useful passthrough portals if supported, without pretending to understand camera content.
- A quiet environment optimized for reading rather than ornamental effects.

Performance and accessibility take priority over expensive blur, particle effects and elaborate room scenery. A translucent-looking panel can be independently implemented without copying Apple's assets.

### Gate D: optional features, not hidden prerequisites

Only after the above:

- Physical laptop recognition and precise anchoring.
- More displays or one large ultrawide surface.
- Per-application Mac panels.
- Hand-only workflows.
- Phone display integration with explicit consent.
- Additional headset vendors.

None of these should block the first reliable extended Mac screen.

## 10. Failure modes worth planning for

| Risk | Why it matters | Response |
|---|---|---|
| Dense text never becomes pleasant | Core value fails despite a beautiful shell. | Test actual work before investing in shell polish. |
| Too many hardware-decoded streams | XR2 Gen 1 capacity is finite. | Start with one/two, measure, degrade gracefully; do not promise unlimited displays. |
| Private macOS display API changes | Extra desktops may break after an OS update. | Explicit compatibility matrix, guarded creation, mirrored fallback and prompt regression testing. |
| Virtual displays remain active after disconnect | Windows or the mouse become hard to recover. | Host-local disconnect/restore action, lifecycle tests and crash recovery. |
| Discovery mistaken for authentication | Desktop contents or remote control could reach the wrong device. | Explicit authenticated pairing, encrypted transport, revoke controls. |
| “Works on Ultra” assumed to mean original Pico 4 | Different hardware and APIs. | Record exact SKU, firmware and enumerated capabilities in every result. |
| Passthrough mistaken for raw camera access | Automatic recognition roadmap becomes fiction. | Separate capability checks and a manual placement fallback. |
| Screen count confused with independent desktops | Three views may only mirror one screen. | Verify macOS display arrangement and move different windows to each desktop. |
| Captured windows have focus/dialog/DRM quirks | Per-app spatial windows feel broken. | Start with whole desktops; add window-level integration deliberately. |
| Open-source project depends on copied proprietary material | Publishing becomes legally and practically unsafe. | Provenance, licences, original assets and legal review where needed. |

## 11. What remains unknown

This research does not establish:

- Your exact Pico SKU, current firmware or advertised runtime extensions.
- Your MacBook chip/macOS version and compatibility with the sampled upstream code.
- Current regional store availability, precise free tiers or purchase prices.
- Your network conditions, actual encode/decode throughput or USB reliability.
- Whether current camera APIs can obtain suitable images on your original consumer unit.
- Whether the latest Pippin release builds and behaves correctly on your Mac, let alone Pico.
- Whether the project name is available legally or commercially.
- Whether you personally find the original Pico comfortable and clear enough for daily development.

These are implementation or device-validation gaps, not reasons to withhold the feasibility conclusion. No headset was connected, software installed, Mac display configuration changed, Apple account accessed, or production service modified during this work.

## 12. Method, evidence strength and limitations

The research covered four axes: original Pico hardware/runtime; existing commercial and open-source workspaces; macOS capture/display/transport architecture; and visionOS/legal/interoperability boundaries.

The initial passes covered broad discovery, then original-source checks and targeted counterchecks. A further focused pass examined the Mac-hosted Simulator proposal and its historical stereo/pose-streaming implementation. Sources include manufacturer specs, Apple support and developer documentation, vendor support pages, public GitHub source/release/API snapshots, an issue discussion and independent hardware reviews. English-language originals were sufficient for the material technical questions. No claim of exhaustive multilingual coverage is made.

Consequential checks included:

- Distinguishing real virtual displays from mirroring and physical multi-monitor support.
- Checking Virtual Desktop's release history rather than repeating obsolete Mac limitations.
- Opening Pippin's actual manifest and display code rather than assuming OpenXR implied Pico compatibility.
- Checking repository age, releases, contributors and licence, not just feature claims.
- Checking the closed status of the historical Godot passthrough issue.
- Separating enterprise camera access from newer API existence and from original-device availability.
- Reading Apple's published licence restrictions, including their exceptions.

Research used direct public-page/repository access and search-engine discovery. Some discovery services were unavailable or returned bot challenges/rate limits; the PICO developer passthrough page was largely a JavaScript shell. The attempted EU legal text fetch was not usable, so it is not relied on for a legal conclusion. No private accounts or machines were accessed.

Official specifications strongly support hardware boundaries. Official compatibility pages support advertised product capabilities, not measured performance. Repository source supports architectural plausibility, not product readiness. Older hands-on reviews illuminate hardware and user-experience constraints but are explicitly not treated as current firmware benchmarks. Sources sharing a vendor/repository are one evidence family, not independent corroborating votes.

The source-to-claim mapping, limitations, retrieval dates and relevant local snapshots are recorded in `sources.json`. The 2026-11-02 planning follow-up added original Docker/Apple container, Xcode, macOS-VM/iCloud and SDK-agreement references S43-S48. Downloaded pages/code excerpts are retained under `tmp/` for local verification only and are excluded from Git. They are not a licence to republish third-party material.

## 13. Final opinion

**This is a worthwhile open-source project if we define it as a beautiful, dependable Mac workspace for existing VR hardware.** The core feature is demonstrably useful and already feasible. Open source can add transparency, local-first operation, user ownership and an opportunity to support Pico well.

**It is the wrong project if success means reproducing the entire Vision Pro, running native Apple spatial apps, or matching its optics through code.** Unlimited development effort does not remove absent sensors and panel resolution, and translating proprietary code does not create redistribution rights.

For a dependable daily workspace, the strongest first contribution is likely **a well-tested Pico adaptation of existing Mac virtual-display software**, followed by independently designed interaction polish. That gives us a path to Mac productivity without first rebuilding an operating system.

For the selected goal of **authentic visionOS simulation**, the Mac-hosted Simulator bridge is the primary research direction, supported by historical evidence. Validate modern stereo/pose streaming first. The independent-shell route remains an alternative, not a substitute for the simulated environment the project aims to present.

## Major source entry points

- [Apple: Use your Mac with Apple Vision Pro](https://support.apple.com/en-us/118521)
- [PICO 4 specifications](https://www.picoxr.com/global/products/pico4/specs)
- [PICO Connect](https://www.picoxr.com/global/software/pico-link)
- [Immersed compatibility and FAQ](https://immersed.com/faq)
- [Virtual Desktop release history](https://github.com/guygodin/VirtualDesktop/releases)
- [PippinVR source and README](https://github.com/triscuitcircuit/PippinVR)
- [Historical visionOS Simulator stereo/ALVR bridge](https://github.com/zhuowei/VisionOSStereoScreenshots/tree/alvr)
- [Apple: interacting with simulated visionOS in Device Hub](https://developer.apple.com/documentation/xcode/interacting-with-your-visionos-app-in-device-hub)
- [DeskPad](https://github.com/Stengo/DeskPad)
- [Apple ScreenCaptureKit](https://developer.apple.com/documentation/screencapturekit)
- [Godot OpenXR Vendors](https://github.com/GodotVR/godot_openxr_vendors)
- [PICO Integration SDK camera API](https://github.com/Pico-Developer/PICO-Unity-Integration-SDK/blob/main/Runtime/Scripts/Features/PXR_CameraImage.cs)
- [Apple visionOS 26 software licence](https://www.apple.com/legal/sla/docs/visionOS26.pdf)
- [Apple Developer Program agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/)

Full source identifiers and their limitations are in `sources.json`.

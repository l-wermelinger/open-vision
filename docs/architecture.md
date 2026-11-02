# Architecture: Mac-hosted visionOS Simulator streaming

Updated: 2026-11-02. **Proposed architecture, not an implemented system.**

## Selected direction

The [product requirements](product-requirements.md) define the delegated decisions and acceptance contract. They are requirements, not measured capabilities. The [workstream](workstream.md) is the single phase/status ledger and contains the standalone agent handoff.

Open Vision aims to present the **spatial environment supplied by Apple's visionOS Simulator** on an existing VR headset. An Apple-silicon Mac hosts the simulator; a bridge transports stereo views and returns tracking/input. The owner's Mac Studio is the target host; a Mac mini or the development MacBook may be separate tested profiles, subject to version, performance and GUI/session validation.

The original consumer PICO 4 is the initial target. OpenXR support alone does not establish compatibility with its loader, interaction profiles, decoder, firmware or optional extensions.

This is not native visionOS on a PICO CPU. It is also not a replacement shell imitating visionOS. The simulator remains Apple software on the Mac, obtained separately under Apple's terms.

## Evidence and uncertainty

**Researched:** `VisionOSStereoScreenshots/alvr` historically implemented a Mac-hosted stereo/pose bridge for a particular 2023 Quest/Xcode configuration. The inspected code substitutes eye textures and updates eye transforms from incoming headset pose. Sources S38-S39.

**Researched:** the same project's history/issues show private-API fragility and a later unsuccessful attempt with visionOS 26.2. This is not proof that an updated bridge cannot work. Source S40.

**Unverified:** current macOS/Xcode/runtime compatibility, a modern PICO client combination, acceptable latency, controller/hand input, and native Mac Virtual Display in Simulator.

**Verified in this repository:** research and documentation exist. No application implementation or hardware test has been performed. Use the [workstream](workstream.md) for current task evidence and the [source ledger](research/sources.json) for source dates and limits.

## Runtime placement and the container request

**Researched:** Docker Desktop on macOS runs Linux workloads; Apple's `container` also runs Linux containers in lightweight VMs. Xcode and visionOS development have native macOS/Apple-silicon requirements. Ordinary Linux/OCI containers are therefore not a supported location for the actual visionOS Simulator. Sources S43-S45.

**Selected default:** a small native per-user macOS host worker controls one dedicated Simulator device in an authorized GUI session. Keep its configuration, data and lifecycle separate from unrelated workloads; stop only owned resources. This is process/data isolation, not security-equivalent container confinement. It avoids adding a Linux VM merely to supervise native GUI software.

Containerize an auxiliary relay/control component only if a measured need appears; do not move Apple account state or grant broad host privileges to that container. The first release should not require an ancillary container or cloud backend.

A real macOS VM is a distinct, conditional alternative. Prove graphics/Metal, nested Simulator behaviour, account access and total overhead before choosing it. Apple's documented iCloud support in suitably created macOS VMs does not prove that visionOS Simulator inside them supports the same account/services. Sources S46-S47.

**Explicit gap:** literal full-runtime Linux-container deployment is not fulfilled by the native default. If that packaging boundary is mandatory, mark it blocked rather than presenting an imitation Docker setup as success.

## Real account and SDK gates

Real owner Apple Account login is a release requirement, not an optional demo. Test the stock runtime/account/service combination early, then revalidate the integrated and packaged versions. Only the owner enters credentials and two-factor codes. Xcode signing, sandbox accounts and website login are not system-account evidence. Use private persistent account state, no exported credentials, no recorded sign-in screens and no unauthenticated personal-content stream. See the exact procedure in [product requirements](product-requirements.md).

The actual Xcode/SDK licence, not merely the device-OS licence, is relevant. Its simulator definitions and development-use/network/modification restrictions create a material review gate for this intended end-user workspace. No assertion of general authorization follows from running on an Apple Mac. Source S48. A positive technical experiment is not a legal determination.

## Proposed data flow

```text
Apple-silicon Mac
  visionOS Simulator / simulated compositor
       |
  simulator-compatible stereo/pose bridge
       |                              ^
  encoder                             | pose, input, control
       |                              |
  authenticated, encrypted local transport
       |                              |
  decoder + stereo presentation       | headset tracking/input
       |                              |
  existing VR headset and its native runtime
```

Headset tracking is measured by the headset. Camera/view transforms must reach the host rendering path, and pose timestamps must remain meaningful through encoding and presentation. The diagram does not prescribe a wire protocol or guarantee a usable latency budget. Prefer a Swift/macOS supervisor, a narrowly versioned native adapter and a lean Android/OpenXR endpoint, subject to licence/compatibility findings. Investigate reusable hardware encoding/decoding before adding dependencies or creating a protocol. No such implementation exists yet.

## Boundaries to prove

### 1. Host simulator adapter

Determine which current simulator version can provide per-eye images and accept view/input updates. Prefer supported interfaces where they meet the need. If private hooks are unavoidable, document the exact version dependency, licence constraints, failure modes and recovery procedure before execution.

The historical bridge hooks CompositorService inside simulated `backboardd`. That is prior art, not an adopted dependency or permission to copy its source. Its private struct layouts and fixed eye-offset assumptions cannot be treated as a current ABI or headset calibration model.

Do not assume every physical-device visionOS app can run as a simulator build, or that all retail apps and Apple services are present. Simulator scope needs a capability matrix, not a promise of the entire retail OS.

### 2. Stereo image and timing path

Capture two actual eye views; drawing the same flat preview to both eyes is not sufficient. Validate eye ordering, projection/FOV, IPD handling, coordinate handedness, timestamps, prediction, recentering and motion-to-photon behaviour.

Native hardware encoding is a candidate optimization, not a measured result. Measure capture, encode, network, decode and presentation costs separately. Do not publish the performance of a different headset or a static screen as this system's result.

### 3. Transport and headset endpoint

Evaluate a version-compatible existing streaming path before designing a protocol. The current mainstream ALVR server's macOS limitations do not rule out a special embedded/forked server, but current clients are not automatically compatible with the historical bridge.

The headset must decode/present the eye views and return pose. Preserve its runtime's safety boundary, exit path and tracking behaviour. Any reprojection or motion prediction must be validated, not inferred from an OpenXR label.

Use explicit pairing and authenticated encrypted transport before carrying private content or accepting input across untrusted networks. Discovery is not authentication. Internet exposure, automatic port forwarding and open remote-control listeners are not defaults.

### 4. Interaction and recovery

**Owner requirement:** controller-first physical interaction, translated so that the Simulator receives natural hand/finger interaction rather than ordinary gamepad control. This is a requirement to investigate, not an implemented or verified capability. Do not silently replace it with a mouse-only experience.

The owner accepted controller-point targeting with trigger-as-pinch, not head-direction targeting, and then delegated remaining design choices. Implement system-wide semantic pinch/select/drag first; add synthetic articulated hand data where compatible APIs/apps require it. Thumbstick scrolling, two-hand gestures and recovery mapping follow the capability-gated defaults in the product requirements. Controllers do not measure all finger joints; synthesized poses are not real tracking. Native focus feedback is preferred to a visible desktop mouse cursor or ornamental hand rendering. No custom eye-tracking hardware is a prerequisite.

System-wide interaction must be proved separately from injecting hands into our own test app. The historical ALVR bridge documented keyboard/mouse interaction, not full controller/hand support; that limitation does not satisfy the new requirement. Host input may be useful as an explicit debugging fallback, not an assumed product substitute. Provide disconnect, recenter and safe host-local recovery before calling a prototype usable.

### 5. MacBook workspace integration

This is a separate goal after a stable simulator bridge. Native Apple Mac Virtual Display **has not been established in Simulator**.

If it is unavailable, an independently implemented MacBook companion could capture actual desktop/virtual-display content and feed a simulator-compatible receiver application. That would add another streaming/input/lifecycle path; it does not become Apple's native protocol by resembling its UI.

ScreenCaptureKit captures content; it does not itself create extra macOS displays. The independent-workspace candidates examined in the research use private `CGVirtualDisplay` APIs, with their own compatibility risks. Sources S14-S17.

## Alternatives retained, not selected

A headset-local Mac workspace, potentially adapting PippinVR, could reduce dependence on Simulator internals and keep panel placement local. It remains useful prior art and a fallback, but it is not interchangeable with presenting Apple's simulated interface.

The [research report](research/report.md) preserves both routes. Its original independent-workspace recommendations describe that alternative; the current project direction is the simulator bridge.

## Scope limits

- No visionOS firmware port, Apple-device impersonation or entitlement bypass.
- No Apple runtime, proprietary assets or extracted frameworks distributed here.
- No guaranteed App Store, Continuity, native Mac Virtual Display or arbitrary-headset support.
- No claim that software restores missing panel resolution, eye cameras or stereo passthrough hardware.
- No security downgrade on a shared Mac merely to reproduce an archived demo.
- Preferred native technology choices are design defaults, not adopted dependencies or proof of current API compatibility. Do not add an engine, VM or software encoder without a measured reason.

Licensing is an implementation gate, not a footnote. Read [licensing.md](licensing.md) before reusing any reference code.

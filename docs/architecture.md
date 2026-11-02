# Architecture: Mac-hosted visionOS Simulator streaming

Updated: 2026-11-02. **Proposed architecture, not an implemented system.**

## Selected direction

Open Vision aims to present the **spatial environment supplied by Apple's visionOS Simulator** on an existing VR headset. An Apple-silicon Mac hosts the simulator; a bridge transports stereo views and returns tracking/input. A Mac mini or Mac Studio is a candidate host, subject to version, performance and GUI/session validation.

The original consumer PICO 4 is the initial target. OpenXR support alone does not establish compatibility with its loader, interaction profiles, decoder, firmware or optional extensions.

This is not native visionOS on a PICO CPU. It is also not a replacement shell imitating visionOS. The simulator remains Apple software on the Mac, obtained separately under Apple's terms.

## Evidence and uncertainty

**Researched:** `VisionOSStereoScreenshots/alvr` historically implemented a Mac-hosted stereo/pose bridge for a particular 2023 Quest/Xcode configuration. The inspected code substitutes eye textures and updates eye transforms from incoming headset pose. Sources S38-S39.

**Researched:** the same project's history/issues show private-API fragility and a later unsuccessful attempt with visionOS 26.2. This is not proof that an updated bridge cannot work. Source S40.

**Unverified:** current macOS/Xcode/runtime compatibility, a modern PICO client combination, acceptable latency, controller/hand input, and native Mac Virtual Display in Simulator.

**Verified in this repository:** research and documentation exist. No application implementation or hardware test has been performed. Use the [workstream](workstream.md) for current task evidence and the [source ledger](research/sources.json) for source dates and limits.

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

Headset tracking is measured by the headset. Camera/view transforms must reach the host rendering path, and pose timestamps must remain meaningful through encoding and presentation. The diagram does not prescribe a wire protocol or guarantee a usable latency budget.

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

Start with a clearly documented input method, such as the host keyboard/mouse. Then evaluate mapped headset-controller input. Hand tracking and custom eye tracking are not prerequisites for the first stereo/pose test.

The historical ALVR bridge documented keyboard/mouse interaction, not full controller/hand support. Provide disconnect, recenter and safe host-local recovery before calling a prototype usable.

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
- No framework/dependency or implementation language selected before a bounded compatibility investigation.

Licensing is an implementation gate, not a footnote. Read [licensing.md](licensing.md) before reusing any reference code.

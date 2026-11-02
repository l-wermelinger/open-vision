# Axis 3: Mac implementation, transport and security

Research date: 2026-11-01. Covered by report section 6 and failure-mode table. This axis examines the locally rendered Mac-workspace alternative; it is not the selected remotely rendered Simulator architecture.

Accepted evidence: S13-S18, S20-S21, S34.

Display creation, capture, encoding and headset rendering are separate. Public ScreenCaptureKit/VideoToolbox are useful, but sampled virtual-display creation uses undocumented CGVirtualDisplay classes. Start with normal Mac input so remote event injection is unnecessary. Head motion must be rendered locally, independent of desktop stream refresh.

USB/ADB is a plausible controlled first experiment, not proven consumer onboarding. Do not infer wireless authentication/encryption from an upstream wired-demo README. Protect the desktop, restore display arrangement and test crash/disconnect/sleep lifecycle. No latency, decoder-count or security audit was performed.

Planning follow-up, 2026-11-02: S43-S45 establish Linux-container versus native macOS/Xcode placement; S46-S47 describe a separate macOS VM/account capability without proving nested Simulator graphics or account support. The selected target is a native Mac Studio worker with bounded data/lifecycle and measured overhead, not a fake full-runtime Docker image. Containerized auxiliaries are optional and need a measured reason. Real account/service/persistence checks and the exact operating envelope remain native-validation gates. See the product requirements and phased workstream for delegated decisions.

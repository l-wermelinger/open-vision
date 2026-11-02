# Axis 3: Mac implementation, transport and security

Research date: 2026-11-01. Covered by report section 6 and failure-mode table. This axis examines the locally rendered Mac-workspace alternative; it is not the selected remotely rendered Simulator architecture.

Accepted evidence: S13-S18, S20-S21, S34.

Display creation, capture, encoding and headset rendering are separate. Public ScreenCaptureKit/VideoToolbox are useful, but sampled virtual-display creation uses undocumented CGVirtualDisplay classes. Start with normal Mac input so remote event injection is unnecessary. Head motion must be rendered locally, independent of desktop stream refresh.

USB/ADB is a plausible controlled first experiment, not proven consumer onboarding. Do not infer wireless authentication/encryption from an upstream wired-demo README. Protect the desktop, restore display arrangement and test crash/disconnect/sleep lifecycle. No latency, decoder-count or security audit was performed.

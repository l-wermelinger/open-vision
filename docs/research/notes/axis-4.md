# Axis 4: Apple baseline, legal limits and recommendation

Stand: 2026-11-01. Covered by report sections 2, 8-13.

Accepted evidence: S02, S28-S30, S35; architecture interpretation informed by other axes.

Apple documents one Mac virtual surface, including ultrawide modes, not unlimited separately arranged Mac screens. No public general Mac Virtual Display receiver API was established. This is a support/interoperability boundary, not proof that every protocol experiment is physically impossible.

visionOS licence section 2 restricts Apple-branded-device use and copying/derivatives, explicitly preserving applicable-law/open-source exceptions. No jurisdiction-specific legal conclusion is made. Independent behaviour implementation and licensed OSS reuse are the recommended path. Decompilation plus AI rewriting is not an automatic redistribution right. Preserve GPL duties for derivatives and avoid exporting Apple assets/fonts.

Initial recommendation: independent Mac workspace feasibility, not firmware or visionOS porting. Validate existing products, then Pippin APK portability, then shell polish.

Follow-up, 2026-11-01: the user specifically proposed a Mac Studio-hosted visionOS Simulator bridge. S37-S42 establish historical stereo/pose streaming using VisionOSStereoScreenshots/alvr on 2023 Apple-silicon/Xcode/Quest configurations. Actual source substitutes left/right compositor textures and eye transforms from incoming headset pose. This materially strengthens the authentic-simulator experiment, not merely a lookalike interface. Current Pico/version compatibility remains unverified; later issues report failures. No top-level licence was detected. A related historical tool requires SIP/library-validation changes, which have not been approved or performed. Apple's native Mac Virtual Display is not established in Simulator. See report section 5.6; do not treat the daily-workspace recommendation as a rejection of this distinct goal.

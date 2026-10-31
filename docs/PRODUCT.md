# Product plan

**ICP/JTBD:** insurance-accepting solo behavioral-health clinicians in one state who need wrong payer listings corrected without spending billable hours across portals and phone queues.

**MVP:** clinician-approved source profile; top-five-payer captures; field-level discrepancy review; evidence-backed correction packet; manual filing; case status and aging. Explicitly exclude autonomous submission, patient data, credentialing, billing, and nationwide coverage.

**Data model:** Provider, PracticeLocation, ApprovedProfileVersion, DirectoryCapture, Discrepancy, CorrectionCase, EvidenceArtifact, SubmissionAttempt, AuditEvent. Store provenance and effective dates; never overwrite captures.

**Economics:** test a $249 cleanup before $79/month monitoring. At 100 subscribers, report math suggests $7,900 MRR plus onboarding. Gross margin depends on minutes and retries per resolved case; kill recurring service if median operator time or ignored-ticket rate prevents >60% contribution margin.

**Validation:** send 25 permission-based scans, seek five paid cleanup deposits, resolve at least 70% of submitted discrepancies within 45 days, and measure median time-to-resolution and 90-day retention. A waitlist is not success.

**Moat:** not scanning. Potential moat is payer-specific resolution data, verified turnaround benchmarks, and trusted credentialing distribution. **Risks:** ignored tickets, free incumbents, portal terms, compliance/security, low search intent, and incorrect “truth.”

**Roadmap:** days 0–30 manual CA scan/cleanup and paid deposits; 31–60 consent, evidence store, and case timeline; 61–90 recurring rescans, verification-ping operations, outcome reporting, and a go/no-go on a second state.

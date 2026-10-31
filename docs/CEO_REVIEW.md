# CEO review

**Mode:** scope reduction. The report’s “platform” framing is too broad for unvalidated demand. The accepted slice is scan → field evidence → reviewed draft case.

**Premise challenge:** accuracy prevalence does not imply therapist budget; regulation pressures insurers more than clinicians; a free national directory could commoditize scanning. Prove paid correction outcomes before monitoring SaaS.

**Alternatives:** manual cleanup concierge (S/low risk, recommended); self-serve monitoring (M/medium); integrated verification network (XL/high). Current state → reviewed workflow demo → 12-month ideal: one-state operator with proven resolution economics and payer playbooks.

## Review findings
1. **Architecture:** keep truth, captures, and cases append-only and separate. Demo shares fixtures across UI/API.
2. **Errors:** name `capture_failed`, `profile_unapproved`, `listing_clean`, `submission_blocked`, `payer_rejected`, and `case_stale`; never convert them to success.
3. **Security:** NPI is public, but account/portal data is sensitive; require consent, tenant isolation, encryption, audit logs, secret rotation, and no PHI collection.
4. **Data/interaction:** handle missing profile, zero listings, stale captures, duplicate clicks, navigation mid-submit, and conflicting newer truth. Demo rejects empty/clean selection and disables repeat queueing.
5. **Code quality:** deterministic comparison stays pure; no premature agent abstraction.
6. **Tests:** cover happy path, clean listing, invalid/unknown input, profile switching, mobile overflow, build, and audits. Production still needs adapter contract and idempotency tests.
7. **Observability:** track scan success, discrepancies per scan, filing failures, case age, resolution rate/time, retry count, and operator minutes.
8. **Database/state:** use immutable capture/profile versions, unique idempotency keys, case-state constraints, and indexed tenant/status/next-action fields.
9. **API:** draft-only case endpoint now; production API needs auth, tenant scoping, versioning, rate limits, request IDs, and idempotency keys.
10. **Scale:** portal fragility and human ops break before compute; cap cohorts and instrument operator load.
11. **UX:** make evidence and simulation unmistakable, require approval, provide loading/error/empty states, keyboard focus, and mobile layout.

**Decision:** ship the complete demo, but do not automate insurer submissions or call it recurring SaaS until five paid cleanups and measurable resolution success. Deferred: live connectors, persistence, AI letters, billing. Not in scope: PHI, patient matching, autonomous legal/compliance claims.

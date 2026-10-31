# Phased build prompts

1. **Concierge proof:** ingest only clinician-approved profile data and operator-uploaded public captures; version sources, expose mismatches, generate reviewable correction packets, and audit every action.
2. **Case operations:** add encrypted multi-tenant storage, role-based access, consent records, evidence artifacts, idempotent filing adapters, explicit `blocked/failed/resolved` states, retries, and SLA alerts.
3. **Monitoring:** schedule 90-day rescans, detect regressions, measure resolution by payer, and notify clinicians without claiming accuracy when capture fails.
4. **Assisted drafting:** evaluate structured templates before any model. If AI is used, redact unnecessary data, constrain output to known fields, store model/version, require human approval, and test hallucination rates.

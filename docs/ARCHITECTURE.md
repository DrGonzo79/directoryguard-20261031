# Architecture

```text
fictional JSON fixtures ──> Next.js static UI ──> compare fields ──> reviewed demo case
          └───────────────> FastAPI /audit ─────> /cases (draft only)
```

The static frontend and FastAPI both consume `data/demo_providers.json`, preventing fixture drift. Domain operations compare phone, address, and accepting-new-patient state and reject clean listings. Production would separate encrypted provider profiles, immutable captures, discrepancy records, correction cases, evidence, consent, and audit events. It needs tenant isolation, least-privilege portal credentials, idempotent submissions, rate limits, structured logs, case-age/SLA metrics, and a dead-letter/retry queue. No AI is needed for truth comparison; later models may draft letters from structured fields but cannot choose truth or submit without approval.

Shadow paths: unknown provider → 404; invalid body → 422; insurer absent → 404; clean listing → 409; upstream capture failure (future) → visible `scan_failed`, never “verified.” Static demo keeps all state in memory and clearly labels simulation.

# DirectoryGuard

Runnable prototype for a therapist-facing directory accuracy and correction desk. It compares fictional insurer listings with a clinician-approved profile, identifies field-level mismatches, and creates a human-reviewed correction case. The static GitHub Pages demo uses the same fixtures as the tested FastAPI source.

## Run

Requires Node `26.12.1` and Python `3.12+`.

```bash
npm ci
npm run typecheck && npm run test:e2e && npm run build && npm audit --audit-level=high
uv sync --project api --locked --dev
uv run --project api pytest api/tests
uv run --project api uvicorn api.main:app --reload
```

Everything is fictional and simulated. The public demo does not access insurer portals, file requests, persist state, or process patient information. Python is runnable/tested source only and is not publicly deployed.

Source: [IdeaBrowser Idea of the Day](https://www.ideabrowser.com/hub/ideas/today), October 31, 2026. Derived analysis is in `research/notes.md`.

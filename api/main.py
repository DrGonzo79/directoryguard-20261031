from pathlib import Path
import json, re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="DirectoryGuard API", version="0.1.0")
PROVIDERS = {p["id"]: p for p in json.loads((Path(__file__).parents[1] / "data/demo_providers.json").read_text())}

class AuditRequest(BaseModel):
    provider_id: str = Field(min_length=1, max_length=80)

class CaseRequest(AuditRequest):
    insurer: str = Field(min_length=1, max_length=120)

def audit_provider(provider_id: str) -> dict:
    provider = PROVIDERS.get(provider_id)
    if not provider:
        raise HTTPException(404, "Unknown demo provider")
    findings = []
    source = provider["authoritative"]
    for listing in provider["listings"]:
        fields = [field for field in ("phone", "address", "acceptingNewPatients") if listing[field] != source[field]]
        findings.append({"insurer": listing["insurer"], "mismatched_fields": fields, "checked": listing["checked"]})
    return {"provider_id": provider_id, "findings": findings, "issue_count": sum(bool(f["mismatched_fields"]) for f in findings), "simulated": True}

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/audit")
def audit(req: AuditRequest): return audit_provider(req.provider_id)

@app.post("/cases")
def create_case(req: CaseRequest):
    provider = PROVIDERS.get(req.provider_id)
    result = audit_provider(req.provider_id)
    finding = next((f for f in result["findings"] if f["insurer"] == req.insurer), None)
    if not finding:
        raise HTTPException(404, "Insurer listing not found")
    if not finding["mismatched_fields"]:
        raise HTTPException(409, "Listing matches the approved profile")
    token = re.sub(r"[^A-Za-z]", "", req.insurer)[:3].upper()
    return {"case_id": f"DG-{provider['state']}-{provider['npi'][-4:]}-{token}", "status": "draft", "mismatched_fields": finding["mismatched_fields"], "simulated": True}

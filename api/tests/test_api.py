from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)
def test_health(): assert client.get("/health").json() == {"status":"ok"}
def test_audit_finds_field_level_mismatches():
    body=client.post("/audit",json={"provider_id":"maya-chen"}).json()
    assert body["issue_count"] == 2 and body["simulated"] is True
    assert body["findings"][0]["mismatched_fields"] == ["phone","acceptingNewPatients"]
def test_case_is_deterministic_and_draft():
    body=client.post("/cases",json={"provider_id":"maya-chen","insurer":"Anthem Blue Cross"}).json()
    assert body["case_id"] == "DG-CA-7890-ANT" and body["status"] == "draft"
def test_verified_listing_cannot_be_filed(): assert client.post("/cases",json={"provider_id":"maya-chen","insurer":"Aetna"}).status_code == 409
def test_unknown_provider_is_404(): assert client.post("/audit",json={"provider_id":"missing"}).status_code == 404
def test_invalid_input_is_422(): assert client.post("/cases",json={"provider_id":"","insurer":""}).status_code == 422

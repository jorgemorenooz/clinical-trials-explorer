import requests

BASE_URL = "http://127.0.0.1:62119"  # Replace if `minikube service fastapi --url` changes

def test_get_trials():
    response = requests.get(f"{BASE_URL}/trials")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "data" in response.json()

def test_get_invalid_id():
    response = requests.get(f"{BASE_URL}/trials/9999")
    assert response.status_code == 404

def test_post_invalid_trial():
    response = requests.post(f"{BASE_URL}/trials", json={})  # Empty payload
    assert response.status_code == 422

def test_post_valid_trial():
    payload = {
        "official_title": "A Study on Cognitive Enhancement",
        "acronym": "ACE",
        "disease_area": "Neurology",
        "trial_phase": "Phase II",
        "status": "Ongoing",
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "country": "Germany",
        "sponsor": "European Brain Institute",
        "description": "Testing a new neurostimulant in adults."
    }

    response = requests.post(f"{BASE_URL}/trials", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["official_title"] == payload["official_title"]
    assert json_data["country"] == "Germany"
    
def test_post_get_delete_trial():

    payload = {
        "official_title": "A Study on Cardio Regeneration",
        "acronym": "HEART-RX",
        "disease_area": "Cardiology",
        "trial_phase": "Phase III",
        "status": "Ongoing",
        "start_date": "2025-02-15",
        "end_date": "2026-02-15",
        "country": "France",
        "sponsor": "Institut du Cœur",
        "description": "Evaluating heart tissue regeneration therapy."
    }

    post_response = requests.post(f"{BASE_URL}/trials", json=payload)
    assert post_response.status_code == 200
    trial = post_response.json()
    trial_id = trial["id"]

    get_response = requests.get(f"{BASE_URL}/trials/{trial_id}")
    assert get_response.status_code == 200
    assert get_response.json()["acronym"] == "HEART-RX"

    delete_response = requests.delete(f"{BASE_URL}/trials/{trial_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Trial deleted"

    confirm_response = requests.get(f"{BASE_URL}/trials/{trial_id}")
    assert confirm_response.status_code == 404

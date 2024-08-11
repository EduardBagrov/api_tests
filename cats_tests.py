import requests
import pytest

base_url = "https://cat-fact.herokuapp.com"

def test_fetch_random_cat_fact():
    response = requests.get(f"{base_url}/facts/random")
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert 'text' in data, "Expected 'text' key in response"

def test_fetch_multiple_cat_facts():
    limit = 6
    response = requests.get(f"{base_url}/facts/random?amount={limit}")
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert isinstance(data, list), "Expected a list of facts"
    assert len(data) == limit, f"Expected {limit} facts, got {len(data)}"

def test_fetch_facts_with_filtering():
    animal_type = "dog"
    response = requests.get(f"{base_url}/facts/random?animal_type={animal_type}&amount=5")
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert isinstance(data, list), "Expected a list of facts"
    assert len(data) > 0, "Expected at least one fact in the response"
    for fact in data:
        assert 'text' in fact, "Expected 'text' key in each fact"
        print("Filtered Fact:", fact['text'])

def test_fetch_non_existent_fact():
    non_existent_id = "nonexistentid12345"
    response = requests.get(f"{base_url}/facts/{non_existent_id}")
    assert response.status_code == 400, "Expected status code 400 for non-existent fact"

def test_invalid_request_handling():
    response = requests.get(f"{base_url}/invalid_endpoint")
    assert response.status_code == 404, "Expected status code 404 for invalid endpoint"
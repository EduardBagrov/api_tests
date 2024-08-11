import requests
import pytest

base_url = "https://cat-fact.herokuapp.com"

def test_fetch_random_cat_fact():
    # Test case to fetch a random cat fact
    response = requests.get(f"{base_url}/facts/random")

    # Assert that the request was successful
    assert response.status_code == 200, "Expected status code 200"

    # Parse the JSON response
    data = response.json()

    # Assert that the response contains the 'text' key
    assert 'text' in data, "Expected 'text' key in response"

    # Print the fact for debugging
    print("Random Cat Fact:", data['text'])

def test_fetch_multiple_cat_facts():
    # Test case to fetch multiple cat facts
    limit = 5
    response = requests.get(f"{base_url}/facts/random?amount={limit}")

    # Assert that the request was successful
    assert response.status_code == 200, "Expected status code 200"

    # Parse the JSON response
    data = response.json()

    # Assert that the response contains the expected number of facts
    assert isinstance(data, list), "Expected a list of facts"
    assert len(data) == limit, f"Expected {limit} facts, got {len(data)}"

    # Print the facts for debugging
    for fact in data:
        print("Cat Fact:", fact['text'])

def test_fetch_facts_with_filtering():
    # Test case to fetch facts containing a specific animal type
    animal_type = "dog"
    response = requests.get(f"{base_url}/facts/random?animal_type={animal_type}&amount=5")

    # Assert that the request was successful
    assert response.status_code == 200, "Expected status code 200"

    # Parse the JSON response
    data = response.json()

    # Assert that the response contains facts
    assert isinstance(data, list), "Expected a list of facts"
    assert len(data) > 0, "Expected at least one fact in the response"

    # Verify that each fact adheres to the expected structure
    for fact in data:
        assert 'text' in fact, "Expected 'text' key in each fact"
        # Check that the animal type is mentioned or implied in the facts context if available
        print("Filtered Fact:", fact['text'])

def test_fetch_non_existent_fact():
    # Test case for a non-existent fact
    non_existent_id = "nonexistentid12345"
    response = requests.get(f"{base_url}/facts/{non_existent_id}")

    # Assert that the request returns a 404 Not Found status code
    assert response.status_code == 400, "Expected status code 400 for non-existent fact"

def test_invalid_request_handling():
    # Test case for an invalid endpoint
    response = requests.get(f"{base_url}/invalid_endpoint")

    # Assert that the request returns a 404 Not Found status code
    assert response.status_code == 404, "Expected status code 404 for invalid endpoint"
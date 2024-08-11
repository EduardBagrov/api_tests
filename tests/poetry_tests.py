import time
import requests
import pytest

base_url = "https://poetrydb.org"


def test_fetch_existing_poem_by_title():
    existing_title = "Sonnet 1: From fairest creatures we desire increase"
    response = requests.get(f"{base_url}/title/{existing_title}")

    assert response.status_code == 200
    data = response.json()
    assert data[0]['title'].lower() == existing_title.lower()

def test_non_existing_title():
    non_existing_title = "This Title Does Not Exist"
    response = requests.get(f"{base_url}/title/{non_existing_title}")

    assert response.status_code == 200, "Expected HTTP status code 200"

    data = response.json()
    assert 'status' in data, "Expected 'status' key in response"
    assert data['status'] == 404, "Expected status 404 in response"
    assert 'reason' in data, "Expected 'reason' key in response"
    assert data['reason'] == 'Not found', "Expected reason 'Not found' in response"

def test_fetch_poems_by_linecount():
    expected_line_count = 6
    response = requests.get(f"{base_url}/linecount/{expected_line_count}")
    assert response.status_code == 200, "Expected status code 200"

    data = response.json()

    assert isinstance(data, list), "Expected a list of poems"
    assert len(data) > 0, "Expected at least one poem in the response"

    mismatched_poems = []
    for poem in data:
        assert 'lines' in poem, "Expected 'lines' key to be in each poem"
        actual_line_count = len(poem['lines'])
        if expected_line_count != actual_line_count:
            mismatched_poems.append((poem.get('title', 'Unknown Title'), actual_line_count))

    if mismatched_poems:
        mismatch_details = "\n".join([f"Title: {title}, Lines: {count}" for title, count in mismatched_poems])
        pytest.fail(f"Found poems with incorrect line counts:\n{mismatch_details}")

def test_invalid_endpoint():
    response = requests.get(f"{base_url}/invalid_endpoint")
    assert response.status_code == 200, "Expected HTTP status code 200"

    data = response.json()
    print (data)
    assert 'status' in data, "Expected 'status' key in response"
    assert data['status'] == '405', "Expected status 405 in response"
    assert 'reason' in data, "Expected 'reason' key in response"
    assert data['reason'] == 'invalid_endpoint list not available. Only author and title allowed.', "Expected reason 'invalid_endpoint' in response"

def test_api_throttling():
    request_count = 20
    delay_between_requests = 0.05

    throttling_triggered = False

    for i in range(request_count):
        author = "William Shakespeare"
        response = requests.get(f"{base_url}/author/{author}")
        print(f"Request {i + 1}: Status Code {response.status_code}")

        rate_limit_remaining = response.headers.get('X-RateLimit-Remaining')
        rate_limit_reset = response.headers.get('X-RateLimit-Reset')
        print(f"Rate Limit Remaining: {rate_limit_remaining}, Reset: {rate_limit_reset}")

        if response.status_code == 429:
            print("Throttling triggered on request:", i + 1)
            throttling_triggered = True
            break
        elif response.status_code != 200:
            print(f"Unexpected status code: {response.status_code}")
            break

        time.sleep(delay_between_requests)

    assert not throttling_triggered, "Throttling was not triggered after multiple rapid requests"

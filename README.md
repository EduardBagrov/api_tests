This file contains description for API tests of poetry_db and cat facts

# Prerequisites

Before running the tests, ensure you have the following installed:

- **Python 3.6 or higher**: Download and install Python from [python.org](https://www.python.org/downloads/).
- **pytest**: A testing framework for Python. Install it using pip:
  ```bash
  pip install pytest requests


# Poetry DB API Tests
The PoetryDB API tests are designed to validate the API's ability to provide poetry data, including fetching poems by title, author, and line count.

# Test Cases


## Test Fetching a Poem by Title:
**Description**: Retrieves a poem using its title.

**Assertions**: Verifies that the response contains the correct poem title.

**Status**: ✅ Passing

## Test Fetching a Non-Existing Title:
**Description**: Attempts to fetch a poem using a non-existent title.

**Assertions**: Ensures that the API returns a 200 status code with a JSON response indicating the poem was not found: reason = 'Not found', status = 404

**Status**: ✅ Passing

## Test Fetching Poems by Line Count:
**Description**: Retrieves poems with a specific number of lines.

**Assertions**: Ensures that each poem returned has the correct line count.

**Status**: ❌ Failing

## Test Invalid Endpoint 
**Description**: Checks how the API handles requests to invalid endpoints.

**Assertions**: Verifies that the API returns a `405` status code for invalid endpoints.

**Status**: ✅ Passing

## Test API Throttling
**Description**: Simulates rapid requests to trigger throttling.

**Assertions**: Ensures that the API responds with a `429 Too Many Requests` status code when rate limits are exceeded.

**Status**: ⚠️ Not Tested Properly (Needs environment setup to verify rate limiting, for 20 requests it works fine)



# Cat Facts API Tests

This repository contains a suite of tests for the Cat Facts API, which provides random cat facts and allows for filtering based on animal types. The tests are designed to validate the functionality and reliability of the API.


## Test case to fetch a random cat fact
**Description**: This test retrieves a random cat fact using the /facts/random endpoint.

**Assertions**: It verifies that the response contains a text key with a valid cat fact.

**Status**: ✅ Passing


## Test case to fetch multiple cat facts
**Description**: This test fetches multiple random cat facts using the /facts/random?amount={limit} endpoint.

**Assertions**: It checks that the correct number of facts is returned and that each fact contains the text key.

**Status**: ✅ Passing


## Test case to fetch facts with Filtering:
**Description**: This test filters facts by a specific animal type, such as "dog".

**Assertions**: It ensures that each fact returned is associated with the specified animal type.

**Status**: ✅ Passing


## Test case to fetch a non-existent fact:
**Description**: This test attempts to fetch a cat fact using a non-existent ID.

**Assertions**: It ensures that the API returns a 400 Not Found status code.

**Status**: ✅ Passing


## Test case to fetch for an invalid endpoint:
**Description**: This test checks how the API handles requests to invalid endpoints.

**Assertions**: It verifies that the API returns a 404 Not Found status code for invalid endpoints.

**Status**: ✅ Passing




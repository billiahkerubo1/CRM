from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_get_customer():
    # Send a GET request to the /v1/customers/{customer_id} endpoint
    customer_id = 1  # You can adjust the customer ID as needed
    response = client.get(f"/v1/customers/{customer_id}")

    # Check the response status code
    assert response.status_code == 200  # 200 indicates a successful request

    # Check the response data
    response_data = response.json()
    assert response_data is not None  # Ensure the response has data

    # Add more specific assertions based on your application's response structure
    assert "customer_id" in response_data  # Check for specific fields
    assert "first_name" in response_data
    assert "last_name" in response_data
    # Add more assertions for other fields as needed

    # You can also test for specific values in the response
    assert response_data["customer_id"] == customer_id  # Check if the customer ID matches

    

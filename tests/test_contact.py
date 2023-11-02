# tests/test_contact.py
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

def test_create_contact_for_customer():
    # Send a POST request to create a new contact for a customer
    customer_id = 1  
    contact_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone_number": "123-456-7890"
    }
    response = client.post(f"/contact/{customer_id}", json=contact_data)

    # Check the response status code
    assert response.status_code == 200  

    # Check the response data
    response_data = response.json()
    assert response_data is not None  # Ensure the response has data

    # Add more specific assertions 
    assert "contact_id" in response_data  # Check for specific fields
    assert "first_name" in response_data
    assert "last_name" in response_data
    
def test_get_contact():
    # Send a GET request to the /contacts/{contact_id} endpoint
    contact_id = 1  
    response = client.get(f"/contacts/{contact_id}")

    # Check the response status code
    assert response.status_code == 200  

    
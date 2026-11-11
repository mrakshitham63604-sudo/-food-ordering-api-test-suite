from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Test 1: Home API
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Food Ordering API"
    }


# Test 2: Get Menu API
def test_get_menu():
    response = client.get("/menu")

    assert response.status_code == 200
    assert len(response.json()) == 4


# Test 3: Add Item to Cart
def test_add_to_cart():
    client.delete("/cart")

    response = client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    assert response.status_code == 200
    assert response.json()["cart"][0]["name"] == "Pizza"
    assert response.json()["cart"][0]["quantity"] == 2


# Test 4: Invalid Food ID
def test_invalid_food_id():
    response = client.post(
        "/cart",
        json={"food_id": 999, "quantity": 1}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Food item not found"


# Test 5: Invalid Quantity
def test_invalid_quantity():
    client.delete("/cart")

    response = client.post(
        "/cart",
        json={"food_id": 1, "quantity": 0}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Quantity must be greater than zero"


# Test 6: Get Cart
def test_get_cart():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    response = client.get("/cart")

    assert response.status_code == 200
    assert response.json()["total_price"] == 500
    assert len(response.json()["cart"]) == 1


# Test 7: Clear Cart
def test_clear_cart():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    response = client.delete("/cart")

    assert response.status_code == 200
    assert response.json()["message"] == "Cart cleared successfully"

    cart_response = client.get("/cart")

    assert cart_response.status_code == 200
    assert cart_response.json()["cart"] == []
    assert cart_response.json()["total_price"] == 0
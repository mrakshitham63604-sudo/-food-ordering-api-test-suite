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

    assert cart_response.json()["cart"] == []
    assert cart_response.json()["total_price"] == 0


# Test 8: Place Order Successfully
def test_place_order():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    response = client.post("/orders")

    assert response.status_code == 200
    assert response.json()["message"] == "Order placed successfully"
    assert response.json()["order"]["total_price"] == 500

    cart_response = client.get("/cart")

    assert cart_response.json()["cart"] == []
    assert cart_response.json()["total_price"] == 0


# Test 9: Place Order with Empty Cart
def test_empty_cart_order():
    client.delete("/cart")

    response = client.post("/orders")

    assert response.status_code == 400


# Test 10: Get All Orders
def test_get_orders():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    client.post("/orders")

    response = client.get("/orders")

    assert response.status_code == 200
    assert len(response.json()) > 0


# Test 11: Get Order by ID
def test_get_order_by_id():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    order_response = client.post("/orders")

    order_id = order_response.json()["order"]["order_id"]

    response = client.get(f"/orders/{order_id}")

    assert response.status_code == 200
    assert response.json()["order_id"] == order_id
    assert response.json()["total_price"] == 500
    # Test 12: Invalid Order ID
def test_invalid_order_id():
    response = client.get("/orders/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"
    # Test 13: Successful Payment
def test_successful_payment():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    order_response = client.post("/orders")
    order_id = order_response.json()["order"]["order_id"]

    payment_response = client.post(
        "/payments",
        json={
            "order_id": order_id,
            "amount": 500,
            "payment_method": "UPI"
        }
    )

    assert payment_response.status_code == 200
    # Test 14: Payment with Invalid Order ID
def test_payment_invalid_order():
    response = client.post(
        "/payments",
        json={
            "order_id": 99999,
            "amount": 500,
            "payment_method": "UPI"
        }
    )

    assert response.status_code == 404
    # Test 15: Payment with Incorrect Amount
def test_payment_wrong_amount():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    order_response = client.post("/orders")
    order_id = order_response.json()["order"]["order_id"]

    response = client.post(
        "/payments",
        json={
            "order_id": order_id,
            "amount": 100,
            "payment_method": "UPI"
        }
    )

    assert response.status_code == 400
    # Test 16: Duplicate Payment
def test_duplicate_payment():
    client.delete("/cart")

    client.post(
        "/cart",
        json={"food_id": 1, "quantity": 2}
    )

    order_response = client.post("/orders")
    order_id = order_response.json()["order"]["order_id"]

    payment_data = {
        "order_id": order_id,
        "amount": 500,
        "payment_method": "UPI"
    }

    first_payment = client.post(
        "/payments",
        json=payment_data
    )

    second_payment = client.post(
        "/payments",
        json=payment_data
    )

    assert first_payment.status_code == 200
    assert second_payment.status_code == 400
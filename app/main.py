from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI(
    title="Food Ordering API",
    description="API for managing a food ordering workflow",
    version="1.0.0"
)

# Food menu
food_items = [
    {"id": 1, "name": "Pizza", "price": 250, "available": True},
    {"id": 2, "name": "Burger", "price": 150, "available": True},
    {"id": 3, "name": "Pasta", "price": 200, "available": True},
    {"id": 4, "name": "Sandwich", "price": 100, "available": True}
]

# Data storage
cart = []
orders = []
payments = []


# Request models
class CartItem(BaseModel):
    food_id: int
    quantity: int


class PaymentRequest(BaseModel):
    order_id: int
    amount: int
    payment_method: str = "Demo"


# 1. Home
@app.get("/")
def home():
    return {"message": "Welcome to Food Ordering API"}


# 2. Get menu
@app.get("/menu")
def get_menu():
    return food_items


# 3. Add item to cart
@app.post("/cart")
def add_to_cart(item: CartItem):

    food = next(
        (f for f in food_items if f["id"] == item.food_id),
        None
    )

    if food is None:
        raise HTTPException(404, "Food item not found")

    if item.quantity <= 0:
        raise HTTPException(400, "Quantity must be greater than zero")

    if not food["available"]:
        raise HTTPException(400, "Food item is not available")

    for cart_item in cart:
        if cart_item["food_id"] == item.food_id:
            cart_item["quantity"] += item.quantity

            return {
                "message": "Cart quantity updated successfully",
                "cart": cart
            }

    cart.append({
        "food_id": item.food_id,
        "name": food["name"],
        "price": food["price"],
        "quantity": item.quantity
    })

    return {
        "message": "Item added to cart successfully",
        "cart": cart
    }


# 4. View cart
@app.get("/cart")
def get_cart():

    total_price = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    return {
        "cart": cart,
        "total_price": total_price
    }


# 5. Clear cart
@app.delete("/cart")
def clear_cart():

    cart.clear()

    return {"message": "Cart cleared successfully"}


# 6. Place order
@app.post("/orders")
def place_order():

    if not cart:
        raise HTTPException(400, "Cannot place order. Cart is empty")

    total_price = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    order = {
        "order_id": len(orders) + 1,
        "items": [item.copy() for item in cart],
        "total_price": total_price,
        "status": "Confirmed"
    }

    orders.append(order)
    cart.clear()

    return {
        "message": "Order placed successfully",
        "order": order
    }


# 7. View all orders
@app.get("/orders")
def get_orders():
    return orders


# 8. View order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):

    order = next(
        (o for o in orders if o["order_id"] == order_id),
        None
    )

    if order is None:
        raise HTTPException(404, "Order not found")

    return order


# 9. Make payment (Demo simulation)
@app.post("/payments")
def make_payment(payment: PaymentRequest):

    # Find order
    order = next(
        (o for o in orders if o["order_id"] == payment.order_id),
        None
    )

    if order is None:
        raise HTTPException(404, "Order not found")

    # Check payment amount
    if payment.amount != order["total_price"]:
        raise HTTPException(400, "Incorrect payment amount")

    # Prevent duplicate payment
    existing_payment = next(
        (p for p in payments if p["order_id"] == payment.order_id),
        None
    )

    if existing_payment:
        raise HTTPException(400, "Order has already been paid")

    # Create payment record
    payment_record = {
        "payment_id": len(payments) + 1,
        "order_id": payment.order_id,
        "amount": payment.amount,
        "payment_method": payment.payment_method,
        "status": "Successful"
    }

    payments.append(payment_record)

    # Update order status
    order["status"] = "Paid"

    return {
        "message": "Payment successful",
        "payment": payment_record
    }


# 10. View all payments
@app.get("/payments")
def get_payments():
    return payments
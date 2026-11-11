# Food Ordering API Test Suite

An automated API testing project built using Python, FastAPI, Pytest, and HTTPX. This project validates the functionality of a Food Ordering REST API, including menu management, cart operations, order processing, and payment handling.

## Features

- Automated REST API testing
- GET, POST, and DELETE request validation
- Cart and order management testing
- Payment validation
- Positive and negative test scenarios
- HTML test report generation

## Technologies Used

- Python
- FastAPI
- Pytest
- HTTPX
- Pytest-HTML

## Project Structure

```text
food-ordering-api-test-suite/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_api.py
│
├── reports/
│   └── report.html
│
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints Tested

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home |
| GET | /menu | Get food menu |
| GET | /cart | Get cart |
| POST | /cart | Add item to cart |
| DELETE | /cart | Clear cart |
| GET | /orders | Get all orders |
| POST | /orders | Place order |
| GET | /orders/{order_id} | Get order by ID |
| POST | /payments | Make payment |
| GET | /payments | Get payments |

## Installation

Clone the repository:

```bash
git clone https://github.com/mrakshitham63604-sudo/-food-ordering-api-test-suite.git
```

Navigate to the project directory:

```bash
cd food-ordering-api-test-suite
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Run Automated Tests

```bash
python -m pytest -v
```

## Generate HTML Test Report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in your browser to view the test results.

## Test Results

**Latest test execution:**

- Total test cases: 16
- Passed: 16
- Failed: 0
- Skipped: 0

All 16 automated test cases passed successfully.

## Author

Created as a Python API testing project to practice REST API validation and automated software testing. 
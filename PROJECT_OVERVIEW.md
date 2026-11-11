# Food Ordering API Test Suite

## Project Overview
The Food Ordering API Test Suite is an automated API testing project developed using Python, FastAPI, and Pytest.

It tests the functionality, reliability, and error handling of a food ordering application through automated test cases.

## Features
- Automated API testing using Pytest.
- Testing GET, POST, and DELETE requests.
- Menu retrieval and cart management testing.
- Order placement and retrieval testing.
- Payment processing validation.
- Negative testing for invalid inputs.
- HTML test report generation.

## Technologies Used
- Python
- FastAPI
- Pytest
- Requests
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
└── PROJECT_OVERVIEW.md
```

## API Endpoints Tested

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home |
| GET | /menu | Get food menu |
| GET | /cart | Get cart |
| POST | /cart | Add items to cart |
| DELETE | /cart | Clear cart |
| GET | /orders | Get all orders |
| POST | /orders | Place an order |
| GET | /orders/{order_id} | Get order details |
| POST | /payments | Process payment |
| GET | /payments | Get payments |

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd food-ordering-api-test-suite
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## Running Automated Tests

Execute the following command:

```bash
python -m pytest -v
```

## Generate HTML Test Report

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to view the test results.

## Test Results

- Total test cases: 16
- Passed: 16
- Failed: 0

All 16 automated test cases passed successfully in the latest test run.

## Learning Outcomes

- Understanding REST API testing.
- Writing automated test cases using Pytest.
- Validating API responses and HTTP status codes.
- Testing positive and negative scenarios.
- Generating HTML test reports.
- Managing projects using Git and GitHub.

## Author

Developed as a Python API testing portfolio project.
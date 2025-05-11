# Pydantic Validation Examples

This project demonstrates various use cases of Pydantic for data validation in Python applications. It includes examples ranging from basic to advanced validation scenarios, along with a FastAPI implementation.

## Project Structure

- `pydantic_example_1.py`: Basic Pydantic model with simple validation
- `pydantic_example_2.py`: Nested models and email validation
- `pydantic_example_3.py`: Custom validators and error handling
- `main.py`: FastAPI implementation with Pydantic models

## Examples Overview

### 1. Basic Model Validation (`pydantic_example_1.py`)
Demonstrates:
- Simple model definition with required and optional fields
- Basic type validation
- Error handling for invalid data
- Model serialization and deserialization

### 2. Nested Models (`pydantic_example_2.py`)
Shows:
- Complex nested data structures
- Email validation using `EmailStr`
- List of nested models
- Model validation and serialization

### 3. Custom Validators (`pydantic_example_3.py`)
Features:
- Custom validation rules using `@validator` decorator
- Complex validation logic
- Error handling with custom error messages
- Type hints and validation

### 4. FastAPI Integration (`main.py`)
Implements:
- RESTful API endpoints
- Complex Pydantic models for request/response validation
- Automatic timestamp and UUID generation
- Error handling with HTTP exceptions

## Requirements

- Python 3.8+
- Pydantic
- FastAPI
- Email-validator (for email validation)

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Examples

Each example file can be run independently:
```bash
python pydantic_example_1.py
python pydantic_example_2.py
python pydantic_example_3.py
```

### Running the FastAPI Application

To run the FastAPI application:
```bash
uvicorn main:app --reload
```

Then visit:
- API documentation: http://localhost:8000/docs
- Alternative documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /`: Welcome message
- `GET /users/{user_id}`: Get user information
- `POST /chat/`: Send a chat message and receive a response

## Features

- Type validation
- Custom validation rules
- Nested data structures
- Email validation
- Automatic data serialization/deserialization
- Error handling
- FastAPI integration
- Automatic API documentation

## Best Practices Demonstrated

1. Type hints and validation
2. Error handling
3. Optional fields with defaults
4. Custom validation rules
5. Nested model structures
6. API documentation
7. Clean code organization

## Contributing

Feel free to submit issues and enhancement requests!

# FastAPI Project Setup with UV

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Development Guide](#development-guide)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)

## Overview

This project demonstrates how to set up a FastAPI application using UV (Python package installer and resolver). FastAPI is a modern, fast web framework for building APIs with Python 3.11+ based on standard Python type hints.

### Key Features
- FastAPI framework for high-performance API development
- UV for dependency management
- Interactive API documentation
- Type checking and validation
- Automatic OpenAPI (Swagger) documentation
- Easy-to-use development server

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.11 or higher
- UV package manager
- Git (optional, for version control)

## Installation

### Step 1: Project Setup

1. Create and initialize the project:
```bash
uv init fastdca-p1
cd fastdca-p1
```

### Step 2: Virtual Environment Setup

#### For macOS/Linux:
```bash
uv venv
source .venv/bin/activate
```

#### For Windows:
```bash
uv venv
.venv\Scripts\activate
```

> **Note**: With PEP 582 support (Python 3.11+), uv may not require manual activation for running commands.

### Step 3: Install Dependencies

1. Install FastAPI and standard dependencies:
```bash
uv add "fastapi[standard]"
```

This command installs:
- `fastapi`: The web framework
- `uvicorn`: ASGI server for running the application
- `httpx`: HTTP client for testing

2. Install development dependencies:
```bash
uv add --dev pytest pytest-asyncio
```

## Project Structure

```
fastdca-p1/
├── .venv/                  # Virtual environment
├── main.py                 # Main application file
├── pyproject.toml          # Project configuration
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## API Documentation

### Available Endpoints

#### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Returns a simple greeting message
- **Response**: 
  ```json
  {
    "Hello": "World"
  }
  ```

#### 2. Items Endpoint
- **URL**: `/items/{item_id}`
- **Method**: GET
- **Description**: Retrieves item information
- **Parameters**:
  - `item_id` (path parameter): Integer
  - `q` (query parameter, optional): String
- **Response**: 
  ```json
  {
    "item_id": <item_id>,
    "q": <query_value>
  }
  ```

### Interactive Documentation

FastAPI automatically generates interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Development Guide

### Running the Application

You can run the server in two ways:

1. Using FastAPI CLI:
```bash
fastapi dev main.py
```

2. Using Uvicorn directly:
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will be available at `http://localhost:8000`

### Development Best Practices

1. **Code Organization**
   - Keep route handlers in separate modules
   - Use Pydantic models for data validation
   - Implement proper error handling

2. **API Design**
   - Use appropriate HTTP methods
   - Implement proper status codes
   - Follow RESTful conventions

## Testing

The project includes testing setup with:
- pytest for unit testing
- pytest-asyncio for async test support

### Running Tests
```bash
pytest
```

## Troubleshooting

Common issues and solutions:

1. **FastAPI Command Not Found**
   - Ensure FastAPI is not installed globally
   - Remove global installation if present
   - Use `uv run` prefix for commands

2. **Port Already in Use**
   - Change the port number in the run command
   - Kill the process using the port
   - Use a different port number

3. **Module Not Found Errors**
   - Ensure virtual environment is activated
   - Check if dependencies are installed
   - Verify Python path settings


For more information about FastAPI, visit the [official documentation](https://fastapi.tiangolo.com/).

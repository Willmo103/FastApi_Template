# FastAPI Template

A FastAPI-based Python package template with essential features for building robust APIs.

## Features

- **Endpoints:**
  - `GET /api/v1/test`: Protected endpoint requiring an API key.
  - `GET /api/v1/uptime`: Check the uptime status of the API.
  - `POST /api/v1/generate-api-key`: Generate a new API key for users.

- **Authentication:**
  - API Key generation and validation.
  - API keys are stored in a SQLite database.

- **Database:**
  - SQLite for simplicity (can be replaced with other databases).
  - Logging of all requests and responses.

- **Middleware:**
  - Logging middleware to capture request and response details.

- **Documentation:**
  - Interactive API docs available at `/api/v1/docs`.

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` package manager

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/fastapi-template.git
    cd fastapi-template
    ```
2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 5050
    The API will be accessible at http://localhost:5050.
    ```

### Usage

1. **Generate an API Key:**

    ```bash
    POST http://localhost:5050/api/v1/generate-api-key
    Content-Type: application/json
    {
        "owner": "your_name"
    }
    ```

2. **Access Protected Endpoint:**

    ```bash
    GET http://localhost:5050/api/v1/test?api_key=YOUR_API_KEY
    ```

3. **Check Uptime:**

    ```bash
    GET http://localhost:5050/api/v1/uptime
    Running Tests
    ```

4. **Ensure you have pytest installed, then run:**

    ```bash
    pytest
    ```
### Configuration

Configuration settings can be modified in app/core/config.py. You can also use a .env file to override default settings.

### Database
The default database is SQLite (app.db). To change the database, update the DATABASE_URL in app/core/config.py.

### Logging
All requests and responses are logged in the logs table within the SQLite database.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

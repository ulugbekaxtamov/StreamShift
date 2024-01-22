# StreamShift

## Getting Started

These instructions will help you run a copy of the project on your local machine for development and testing.

### Prerequisites

Install the following tools:

- Docker
- Docker Compose

### Installation and Launch

1. **Cloning the repository**:
    ```
    git clone https://github.com/ulugbekaxtamov/StreamShift.git
    ```

2. **Navigate to the project directory**:
    ```
    cd StreamShift
    ```

3. **Create `.env` files using examples**:
    ```
    cat example.env > .env
    ```

4. **Run Docker Compose**:
    ```
    docker-compose up --build
    ```

### API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI. You can access and interact with your
API's endpoints, view the expected request formats, and try out the API calls directly from the browser.

To view the Swagger UI documentation, navigate to:

```
http://127.0.0.1:8000/docs/
```



### Project Structure

```
StreamShift/
│
├── app/                  # Main application module
│   ├── __init__.py
│   ├── crud.py           # Implementation of CRUD operations
│   ├── models.py         # SQLAlchemy models Model for API call logging
│   ├── schemas.py        # Pydantic schemas for data validation and serialization
│   ├── services.py       # Business logic and service layer functionalities RTSP to HLS
│   └── views.py          # API endpoints and route handlers
│
├── alembic/              # Directory for Alembic migrations
│   ├── versions/         # Generated migration scripts
│   └── env.py            # Alembic environment file
│
├── core/                 # Configuration and helper classes
│   ├── __init__.py
│   └── config.py         # Application configuration
│
├── .env                  # Environment variables file
├── example.env           # Example environment variables file
├── alembic.ini           # Configuration for Alembic
├── Dockerfile            # For building Docker containers
├── docker-compose.yml    # Manage containers with Docker Compose
├── run.sh                # Script for initializing and starting the application in a Docker container
├── requirements.txt      # Project dependencies
│── main.py               # FastAPI application entry point
└── README.md             # Instructions for installation and running

```
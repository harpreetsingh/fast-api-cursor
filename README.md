# Minimal FastAPI Server

A simple FastAPI server with a health check endpoint.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

### Option 1: Using the run script
```bash
python run.py
```

### Option 2: Using uvicorn directly
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Option 3: Using the main module
```bash
python main.py
```

## Endpoints

- `GET /health` - Health check endpoint that returns server status

## Accessing the Server

Once running, you can access:
- Server: http://localhost:8000
- Health endpoint: http://localhost:8000/health
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc



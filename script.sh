#!/bin/bash

# List contents of the working directory
echo "Listing contents of /app directory:"
ls -la /app

# Run the FastAPI app using Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

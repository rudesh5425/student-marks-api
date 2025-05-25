# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from a local JSON file or dictionary
marks_data = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40,
    "Eve": 50
}

@app.get("/api")
async def get_marks(name: List[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}

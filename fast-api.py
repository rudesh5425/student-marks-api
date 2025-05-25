# main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks once (you can replace with actual file read logic)
marks_data = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 82
}

@app.get("/api")
async def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}

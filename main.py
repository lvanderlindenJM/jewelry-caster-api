from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json

app = FastAPI()

# Enable CORS for all origins (important for frontend or chatbot access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the JSON data
with open("jewelry_casters.json") as f:
    casters = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Jewelry Caster API. Use /casters to search."}

@app.get("/casters")
def get_casters(
    state: Optional[str] = None,
    city: Optional[str] = None,
    keyword: Optional[str] = None
):
    results = casters
    if state:
        results = [c for c in results if c["State"].lower() == state.lower()]
    if city:
        results = [c for c in results if c["City"].lower() == city.lower()]
    if keyword:
        results = [c for c in results if keyword.lower() in c["Services/Metals"].lower()]
    return results



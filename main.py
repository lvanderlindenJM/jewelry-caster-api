from fastapi import FastAPI, Query
from typing import Optional
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]  
    allow_credentials=True,
    allow_methods=[*],
    allow_headers=[*],
)

# Load the JSON data
with open("jewelry_casters.json") as f:
    casters = json.load(f)

# Root route to prevent 404 on GET /
@app.get("/")
def read_root():
    return {"message": "Welcome to the Jewelry Caster API. Use /casters to search."}

# Main API route
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


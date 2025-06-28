from fastapi import FastAPI
from app.service import spotify_token_manager
import httpx
import os

if os.environ.get("DEBUG", "0") == "1":
    import debugpy
    debugpy.listen(("0.0.0.0", 5678))
    print("Waiting for debugger attach...")
    debugpy.wait_for_client()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from backend"}


@app.get("/api/test")
async def read_root():
    token = await spotify_token_manager.get_token()

    async with httpx.AsyncClient() as client:
        client.headers["Authorization"] = f"Bearer {token}"
        response = await client.get('https://api.spotify.com/v1/artists/3YQKmKGau1PzlVlkL1iodx')

    return response.json()

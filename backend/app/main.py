from typing import Annotated

from fastapi import FastAPI, Path
from app.service import spotify_token_manager
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from backend"}


@app.get("/artist/{artist_id}")
async def read_root(
        artist_id: Annotated[str, Path(title="Artist ID")],
):
    token = await spotify_token_manager.get_token()

    async with httpx.AsyncClient() as client:
        client.headers["Authorization"] = f"Bearer {token}"
        response = await client.get(f'https://api.spotify.com/v1/artists/{artist_id}')

    return response.json()

@app.get("/artist/search/{query}")
async def read_root(
        query: Annotated[str, Path(title='Query to look up the artist by')],
):
    token = await spotify_token_manager.get_token()
    async with httpx.AsyncClient() as client:
        client.headers["Authorization"] = f"Bearer {token}"
        response = await client.get(f'https://api.spotify.com/v1/search?q={query}&type=artist&limit=5')

    return response.json()
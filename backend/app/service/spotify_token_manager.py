from datetime import datetime, timedelta
import httpx
import os

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

class SpotifyTokenManager:
    def __init__(self):
        self.access_token = None
        self.expires_at = datetime.now()

    async def get_token(self):
        if self.access_token and datetime.now() < self.expires_at:
            return self.access_token

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://accounts.spotify.com/api/token",
                data={
                    "grant_type": 'client_credentials',
                    "client_id": client_id,
                    "client_secret": client_secret
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )

        response.raise_for_status()
        data = response.json()
        self.access_token = data['access_token']
        self.expires_at = datetime.now() + timedelta(seconds=data["expires_in"])
        return self.access_token
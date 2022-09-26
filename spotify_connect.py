import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotipy:
    def connect(
        self,
        username="",
        password="",
    ) -> None:
        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=f"{username}",
                client_secret=f"{password}",
                # pesquisar sobre redirect_uri for users
                redirect_uri="http://localhost:8080",
                scope=[
                    "user-library-read",
                    "user-top-read",
                    "user-follow-read",
                    "playlist-read-private",
                    "user-read-recently-played",
                ],
            )
        )

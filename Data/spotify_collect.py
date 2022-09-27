class SpotifyDataCollector:
    def set_spotify_auth(self, spotipy):
        self._sp = spotipy

    def get_user_data(self) -> dict[str, str]:
        """Get profile information about the current user."""
        user = self._sp.current_user()

        return {
            "id": user["id"],
            "name": user["display_name"],
            "type": user["type"],
            "image_path": user["images"][0]["url"],
            "external_url": user["external_urls"]["spotify"],
        }

    def get_recently_played(self) -> list[dict]:
        """Get current user's recently played tracks."""
        data: dict = self._sp.current_user_recently_played(limit=50)
        if len(data["items"]) > 0:
            raw_recently_played: list[dict] = data["items"]
            clean_recently_played: list[dict] = []

            for track in raw_recently_played:
                track = track["track"]
                clean_recently_played.append(
                    {
                        "id": track["id"],
                        "name": track["name"],
                        "type": track["type"],
                        "duration": track["duration_ms"],
                        "external_url": track["external_urls"]["spotify"],
                        "user_liking": 5,
                    }
                )
        else:
            clean_recently_played = "No recently played tracks."

        return clean_recently_played

    def get_top_tracks(self) -> list[dict]:
        """Get the current user's top tracks based on calculated affinity."""
        data: dict = self._sp.current_user_top_tracks(limit=50)
        if len(data["items"]) > 0:
            raw_top_tracks: list[dict] = data["items"]
            clean_top_tracks: list[dict] = []

            for track in raw_top_tracks:
                clean_top_tracks.append(
                    {
                        "id": track["id"],
                        "name": track["name"],
                        "type": track["type"],
                        "duration": track["duration_ms"],
                        "external_url": track["external_urls"]["spotify"],
                        "user_liking": 5 * 3,
                    }
                )
        else:
            clean_top_tracks = "No top tracks."

        return clean_top_tracks

    def get_saved_tracks(self) -> list[dict]:
        """Get a list of the songs saved in the current user's 'Your Music' library."""
        data: dict = self._sp.current_user_saved_tracks(limit=50)
        if len(data["items"]) > 0:
            raw_saved_tracks: list[dict] = data["items"]
            clean_saved_tracks: list[dict] = []

            for track in raw_saved_tracks:
                track = track["track"]
                clean_saved_tracks.append(
                    {
                        "id": track["id"],
                        "name": track["name"].strip(),
                        "type": track["type"],
                        "duration": track["duration_ms"],
                        "external_url": track["external_urls"]["spotify"],
                        "user_liking": 5 * 2,
                    }
                )
        else:
            clean_saved_tracks = "No saved tracks."

        return clean_saved_tracks

    def get_playlists(self) -> list[dict]:
        """Get a list of the playlists owned or followed by the current Spotify user."""
        data: dict = self._sp.current_user_playlists(limit=50)
        if len(data["items"]) > 0:
            raw_playlists: list[dict] = data["items"]
            clean_playlists: list[dict] = []
            tracks_ids: set[str] = set()

            for playlist in raw_playlists:
                # Get full details of the tracks of a playlist.
                tracks: dict = self._sp.playlist_tracks(playlist["id"], limit=100)
                for track in tracks["items"]:
                    if track["track"]["id"]:
                        tracks_ids.add(track["track"]["id"])

                clean_playlists.append(
                    {
                        "id": playlist["id"],
                        "name": playlist["name"].strip(),
                        "type": playlist["type"],
                        "image_path": playlist["images"][0]["url"],
                        "external_url": playlist["external_urls"]["spotify"],
                        "tracks_ids": tracks_ids.copy(),
                        "user_liking": 5,
                    }
                )
                tracks_ids.clear()
        else:
            clean_playlists = "No playlists."

        return clean_playlists

    def get_top_artists(self) -> list[dict]:
        """Get the current user's top artists based on calculated affinity."""
        data: dict = self._sp.current_user_top_artists(limit=50)
        if len(data["items"]) > 0:
            raw_top_artists: list[dict] = data["items"]
            clean_top_artists: list[dict] = []
            artist_genres: set[str] = set()

            for artist in raw_top_artists:
                for genre in artist["genres"]:
                    artist_genres.add(genre)

                clean_top_artists.append(
                    {
                        "id": artist["id"],
                        "name": artist["name"].strip(),
                        "type": artist["type"],
                        "genres": artist_genres.copy(),
                        "image_path": artist["images"][0]["url"],
                        "external_url": artist["external_urls"]["spotify"],
                        "user_liking": 5 * 3,
                    }
                )
                artist_genres.clear()
        else:
            clean_top_artists = "No top artists."

        return clean_top_artists

    def get_followed_artists(self) -> list[dict]:
        """Get the current user's followed artists."""
        data: dict = self._sp.current_user_followed_artists(limit=50)
        if len(data["artists"]["items"]) > 0:
            raw_followed_artists: list[dict] = data["artists"]["items"]
            clean_followed_artists: list[dict] = []
            artist_genres: set[str] = set()

            for artist in raw_followed_artists:
                for genre in artist["genres"]:
                    artist_genres.add(genre)

                clean_followed_artists.append(
                    {
                        "id": artist["id"],
                        "name": artist["name"].strip(),
                        "type": artist["type"],
                        "genres": artist_genres.copy(),
                        "image_path": artist["images"][0]["url"],
                        "external_url": artist["external_urls"]["spotify"],
                        "user_liking": 5 * 2,
                    }
                )
                artist_genres.clear()
        else:
            clean_followed_artists = "No followed artists."

        return clean_followed_artists

    def get_saved_albums(self) -> list[dict]:
        """Get a list of the albums saved in the current user's 'Your Music' library."""
        data: dict = self._sp.current_user_saved_albums(limit=50)
        if len(data["items"]) > 0:
            raw_saved_albums: list[dict] = data["items"]
            clean_saved_albums: list[dict] = []
            tracks_ids: set[str] = set()
            artists_ids: set[str] = set()

            for album in raw_saved_albums:
                album = album["album"]
                # Get id of artists.
                for artist in album["artists"]:
                    if artist["id"]:
                        artists_ids.add(artist["id"])

                # Get id of tracks.
                for track in album["tracks"]["items"]:
                    if track["id"]:
                        tracks_ids.add(track["id"])

                clean_saved_albums.append(
                    {
                        "id": album["id"],
                        "name": album["name"].strip(),
                        "type": album["type"],
                        "release_date": album["release_date"],
                        "image_path": album["images"][0]["url"],
                        "external_url": album["external_urls"]["spotify"],
                        "artists_ids": artists_ids.copy(),
                        "tracks_ids": tracks_ids.copy(),
                        "user_liking": 5 * 2,
                    }
                )
                tracks_ids.clear()
                artists_ids.clear()
        else:
            clean_saved_albums = "No saved albums."

        return clean_saved_albums

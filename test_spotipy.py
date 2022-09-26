import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="6e749bf8f1de42e8a3ce17507f40ca7c",
        client_secret="67c5ec0b43724a4cba0f4e34e458bd38",
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

# user data to display in gui
user = sp.current_user()
print("### Current user data ###")
print(
    f"""User id: {user["id"]}
User name: {user["display_name"]}
User type: {user["type"]}
User images: {user["images"][0]["url"]}
User e_url: {user['external_urls']['spotify']}
"""
)

# recommendation_genres = sp.recommendation_genre_seeds()
# print(f"""{recommendation_genres}""")


# user recently played tracks
recently_played = sp.current_user_recently_played()
print("\n### Current user recently played tracks ###")
data: dict = sp.current_user_recently_played(limit=50)
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
                "external_url": track["external_urls"]["spotify"],
            }
        )
else:
    clean_recently_played = "No recently played tracks."
print(clean_recently_played)

# if len(recently_played["items"]) > 0:
#     print(
#         f"""Recently played track id: {recently_played["items"][0]['track']['id']}
# Recently played track name: {recently_played["items"][0]['track']['name']}
# Recently played artists name: {recently_played["items"][0]['track']['artists'][0]['name']}
# Recently played album name: {recently_played["items"][0]['track']['album']['name']}
# Recently played track e_url: {recently_played["items"][0]['track']['external_urls']['spotify']}
#     """
#     )
# else:
#     print("No recently played tracks.")


# user followed artists
print("\n### Current user followed artists ###")
data: dict = sp.current_user_followed_artists(limit=50)
if len(data["artists"]["items"]) > 0:
    raw_followed_artists: list[dict] = data["artists"]["items"]
    clean_followed_artists: list[dict] = []

    for artist in raw_followed_artists:
        clean_followed_artists.append(
            {
                "id": artist["id"],
                "name": artist["name"],
                "type": artist["type"],
                "genres": artist["genres"],
                "image_path": artist["images"][0]["url"],
                "external_url": artist["external_urls"]["spotify"],
            }
        )
else:
    clean_followed_artists = "No followed artists."
print(clean_followed_artists)

# user playlists
print("\n### Current user playlists ###")
data: dict = sp.current_user_playlists(limit=50)
if len(data["items"]) > 0:
    raw_playlists: list[dict] = data["items"]
    clean_playlists: list[dict] = []
    tracks_ids: set[str] = set()

    for playlist in raw_playlists:
        # Get full details of the tracks of a playlist.
        tracks: dict = sp.playlist_tracks(playlist["id"], limit=100)
        for track in tracks["items"]:
            if track["track"]["id"]:
                tracks_ids.add(track["track"]["id"])

        clean_playlists.append(
            {
                "id": playlist["id"],
                "name": playlist["name"],
                "type": playlist["type"],
                "image_path": playlist["images"][0]["url"],
                "external_url": playlist["external_urls"]["spotify"],
                "tracks_ids": tracks_ids,
            }
        )
else:
    clean_playlists = "No playlists."
print(clean_playlists)

# user saved albums
print("\n### Current user saved albums ###")
data: dict = sp.current_user_saved_albums(limit=50)
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
                "name": album["name"],
                "type": album["type"],
                "release_date": album["release_date"],
                "image_path": album["images"][0]["url"],
                "external_url": album["external_urls"]["spotify"],
                "artists_ids": artists_ids,
                "tracks_ids": tracks_ids,
            }
        )
else:
    clean_saved_albums = "No saved albums."
print(clean_saved_albums)

# user saved episodes
# saved_episodes = sp.current_user_saved_episodes()
# print("### Current user saved episodes ###")
# if len(saved_episodes["items"]) > 0:
#     print(
#         f"""Episode show id: {saved_episodes["items"][0]['episode']['show']['id']}
# Episode show name: {saved_episodes["items"][0]['episode']['show']['name']}
# Episode show publisher: {saved_episodes["items"][0]['episode']['show']['publisher']}
# Episode id: {saved_episodes["items"][0]['episode']['id']}
# Episode name: {saved_episodes["items"][0]['episode']['name']}
# Episode type: {saved_episodes["items"][0]['episode']['type']}
# Episode description: {saved_episodes["items"][0]['episode']['description']}
# Episode language: {saved_episodes["items"][0]['episode']['language']}
# Episode release date: {saved_episodes["items"][0]['episode']['release_date']}
# Episode images: {saved_episodes["items"][0]['episode']['images'][0]['url']}
# Episode e_urls: {saved_episodes["items"][0]['episode']['external_urls']['spotify']}
#     """
#     )
# else:
#     print("No saved episodes.")


# user saved shows
# saved_shows = sp.current_user_saved_shows()
# print("### Current user saved shows ###")
# if len(saved_shows["items"]) > 0:
#     print(
#         f"""Show id: {saved_shows["items"][0]['show']['id']}
# Show name: {saved_shows["items"][0]['show']['name']}
# Show type: {saved_shows["items"][0]['show']['type']}
# Show description: {saved_shows["items"][0]['show']['description']}
# Show publisher: {saved_shows["items"][0]['show']['publisher']}
# Show total epis: {saved_shows["items"][0]['show']['total_episodes']}
# Show languages: {saved_shows["items"][0]['show']['languages']}
# Show images: {saved_shows["items"][0]['show']['images'][0]['url']}
# Show e_urls: {saved_shows["items"][0]['show']['external_urls']['spotify']}
#     """
#     )
# else:
#     print("No saved shows.")

# user saved tracks
print("\n### Current user saved tracks ###")
data: dict = sp.current_user_saved_tracks(limit=50)
if len(data["items"]) > 0:
    raw_saved_tracks: list[dict] = data["items"]
    clean_saved_tracks: list[dict] = []

    for track in raw_saved_tracks:
        track = track["track"]
        clean_saved_tracks.append(
            {
                "id": track["id"],
                "name": track["name"],
                "type": track["type"],
                "external_url": track["external_urls"]["spotify"],
            }
        )
else:
    clean_saved_tracks = "No saved tracks."
print(clean_saved_tracks)

# user top artists
print("\n### Current user top artists ###")
data: dict = sp.current_user_top_artists(limit=50)
if len(data["items"]) > 0:
    raw_top_artists: list[dict] = data["items"]
    clean_top_artists: list[dict] = []

    for top_artist in raw_top_artists:
        clean_top_artists.append(
            {
                "id": top_artist["id"],
                "name": top_artist["name"],
                "type": top_artist["type"],
                "genres": top_artist["genres"],
                "image_path": top_artist["images"][0]["url"],
                "external_url": top_artist["external_urls"]["spotify"],
            }
        )
else:
    clean_top_artists = "No top artists."
print(clean_top_artists)

# user top tracks
print("\n### Current user top tracks ###")
data: dict = sp.current_user_top_tracks(limit=50)
if len(data["items"]) > 0:
    raw_top_tracks: list[dict] = data["items"]
    clean_top_tracks: list[dict] = []

    for track in raw_top_tracks:
        clean_top_tracks.append(
            {
                "id": track["id"],
                "name": track["name"],
                "type": track["type"],
                "external_url": track["external_urls"]["spotify"],
            }
        )
else:
    clean_top_tracks = "No top tracks."
print(clean_top_tracks)

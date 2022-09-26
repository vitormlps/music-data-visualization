from dataclasses import dataclass
from spotify_collect import SpotifyDataCollector
from data_type import *


class Model:
    def __init__(self) -> None:
        self._collector = SpotifyDataCollector()
        self._factory = DataFactory()
        self._database = Database()

    def set_authorization(self, spotipy):
        self._collector.set_spotify_auth(spotipy)

    def create_user(self):
        user_data = self._collector.get_user_data()
        self._database.user = self._factory.create_user(user_data)

    def collect_tracks(self):
        recent_tracks = self._collector.get_recently_played()
        top_tracks = self._collector.get_top_tracks()
        saved_tracks = self._collector.get_saved_tracks()

        all_tracks = recent_tracks + top_tracks + saved_tracks

        obj_tracks = self._factory.create_tracks(all_tracks)
        self._database.tracks = obj_tracks

    def collect_playlists(self):
        playlists = self._collector.get_playlists()

        obj_playlists = self._factory.create_playlists(playlists)
        self._database.playlists = obj_playlists

    def collect_artists(self):
        top_artists = self._collector.get_top_artists()
        followed_artists = self._collector.get_followed_artists()

        all_artists = top_artists + followed_artists

        obj_artists = self._factory.create_artists(all_artists)
        self._database.artists = obj_artists

    def collect_albums(self):
        albums = self._collector.get_saved_albums()

        obj_albums = self._factory.create_albums(albums)
        self._database.albums = obj_albums

    def create_relations(self):
        for track in self._database.tracks:
            # for each playlist tracks set
            for playlist in self._database.playlists:
                for pl_track_id in playlist.tracks:
                    if pl_track_id == track.id:
                        playlist.tracks.remove(pl_track_id)
                        playlist.tracks.add(track)

            # for each album tracks set
            for album in self._database.albums:
                for alb_track_id in album.tracks:
                    if alb_track_id == track.id:
                        album.tracks.remove(alb_track_id)
                        album.tracks.add(track)

        for artist in self._database.artists:
            for album in self._database.albums:
                for alb_artist_id in album.artists:
                    if alb_artist_id == artist.id:
                        album.artists.remove(alb_artist_id)
                        album.artists.add(artist)


@dataclass
class Database:
    def __init__(self):
        self._user: User = None
        self._tracks: set[Track] = set()
        self._playlists: set[Playlist] = set()
        self._artists: set[Artist] = set()
        self._albums: set[Album] = set()

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def tracks(self):
        return self._tracks

    @tracks.setter
    def tracks(self, tracks):
        self._tracks = tracks

    @property
    def playlists(self):
        return self._playlists

    @playlists.setter
    def playlists(self, playlists):
        self._playlists = playlists

    @property
    def artists(self):
        return self._artists

    @artists.setter
    def artists(self, artists):
        self._artists = artists

    @property
    def albums(self):
        return self._albums

    @albums.setter
    def albums(self, albums):
        self._albums = albums


class DataFactory:
    def create_user(self, user_data: dict[str, str]) -> User:
        return User(user_data)

    def create_tracks(self, all_tracks: list[dict]) -> set[Track]:
        temp_tracks = all_tracks
        obj_tracks = set()

        for track in all_tracks:
            for temp in temp_tracks:
                if (
                    track["id"] == temp["id"]
                    and track["user_liking"] != temp["user_liking"]
                ):
                    track["user_liking"] += temp["user_liking"]
            obj_tracks.add(Track(track))

        return obj_tracks

    def create_playlists(self, playlists: list[dict]) -> set[Playlist]:
        obj_playlists = set()

        for playlist in playlists:
            obj_playlists.add(Playlist(playlist))

        return obj_playlists

    def create_artists(self, artists: list[dict]) -> set[Artist]:
        obj_artists = set()

        for artist in artists:
            obj_artists.add(Artist(artist))

        return obj_artists

    def create_albums(self, albums: list[dict]) -> set[Album]:
        obj_albums = set()

        for album in albums:
            obj_albums.add(Album(album))

        return obj_albums

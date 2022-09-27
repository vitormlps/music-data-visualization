from Data.data_model import Model
from .spotify_connect import Spotipy


class Controller:
    def __init__(self):
        self._model = Model()
        self.user_logged = False

    def verify_entries(self, user, password):
        if (
            # depois refatorar com regex
            user == "id"
            and password == "secret"
        ):
            return self.connect_user(user, password)
        raise AttributeError("Not valid entries.")

    def connect_user(self, user, password) -> None:
        # Connect user input with spotify account
        spotipy = Spotipy().connect(user, password)
        if not spotipy:
            # Pesquisar "raise error"
            raise ConnectionError("Unable to connect.")

        self.user_logged = True
        self._model.set_authorization(spotipy)
        self._model.create_user()

    def data_collect(self):
        self._model.collect_tracks()
        self._model.collect_playlists()
        self._model.collect_artists()
        self._model.collect_albums()

        self._model.create_relations()

        # for track in self._model._database.tracks:
        #     print(f"{track.id}, {track._name}, {track._duration}")
        # print("")

        # for playlist in self._model._database.playlists:
        #     print(f"{playlist.id}, {playlist._name}, {playlist.tracks}")
        # print("")

        # for artist in self._model._database.artists:
        #     print(f"{artist.id}, {artist._name}, {artist._genres}")
        # print("")

        # for album in self._model._database.albums:
        #     print(f"{album.id}, {album._name}, {album.artists}, {album.tracks}")

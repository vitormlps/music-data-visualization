class Base:
    _id: str
    _type: str
    _name: str
    _external_url: str
    _image_path: str
    _user_liking: int

    def __init__(self, data: dict[str, str]) -> None:
        self._id = data["id"]
        self._type = data["type"]
        self._name = data["name"]
        self._external_url = data["external_url"]

    @property
    def id(self):
        return self._id


class User(Base):
    def __init__(self, user_data: dict) -> None:
        super().__init__(user_data)
        self._image_path = user_data["image_path"]


class Track(Base):
    def __init__(self, track_data: dict) -> None:
        super().__init__(track_data)
        self._duration: float = float(round(track_data["duration"] / 60000, 2))
        self._user_liking = track_data["user_liking"]


class Playlist(Base):
    def __init__(self, playlist_data: dict) -> None:
        super().__init__(playlist_data)
        self._tracks: set[Track] = playlist_data["tracks_ids"]
        self._image_path = playlist_data["image_path"]
        self._user_liking = playlist_data["user_liking"]

    @property
    def tracks(self):
        return self._tracks


class Artist(Base):
    def __init__(self, artist_data: dict) -> None:
        super().__init__(artist_data)
        self._genres: set[str] = artist_data["genres"]
        self._image_path = artist_data["image_path"]
        self._user_liking = artist_data["user_liking"]


class Album(Base):
    def __init__(self, album_data: dict) -> None:
        super().__init__(album_data)
        self._release_date: str = album_data["release_date"]
        self._tracks: set[Track] = album_data["tracks_ids"]
        self._artists: set[Artist] = album_data["artists_ids"]
        self._image_path = album_data["image_path"]
        self._user_liking = album_data["user_liking"]

    @property
    def tracks(self):
        return self._tracks

    @property
    def artists(self):
        return self._artists

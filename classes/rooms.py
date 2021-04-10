class Rooms:

    def __init__(self, name: str, playlist: str):
        self.name = name
        self.playlist = playlist


    #add a list of songs, initially referred to with a single keyword eg "disco"
    def add_playlist_to_room(self, name_of_playlist):
        self.playlist.append(name_of_playlist)
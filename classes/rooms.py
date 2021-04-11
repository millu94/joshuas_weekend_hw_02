class Rooms:

    def __init__(self, name: str, playlist: str, occupied: bool):
        self.name = name
        self.playlist = playlist
        self.occupied  = occupied


    #add a list of songs, initially referred to with a single keyword eg "disco"
    def add_playlist_to_room(self, name_of_playlist):
        self.playlist.append(name_of_playlist)

    def check_in(self,):
        #if room is occupied (true) then print message "choose another room"
        if self.occupied == True:
            return "Choose another room"
        #if false then change occupied status to True
        else:
            self.occupied = True

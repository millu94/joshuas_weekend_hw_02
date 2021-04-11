class Rooms:

    def __init__(self, name, playlist, occupied):
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

    def check_out(self,):
        #if room isn't occupied (false) then print message "choose another room"
        if self.occupied == False:
            return "Room is already vacant"
        #if True then change occupied status to False, AND clear the playlist
        else:
            self.occupied = False
            self.playlist = []

class Guests:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def book_room(self, da_club):
        if da_club.available_rooms > 0:
            self.wallet -= 1000
            da_club.till += 1000
            da_club.available_rooms -= 1
            return "Thank you, have fun!"
        return "Sorry we're full!"

    def whoop_whoop():
        pass
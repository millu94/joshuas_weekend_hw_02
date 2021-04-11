import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestClubMatrix(unittest.TestCase):

    def setUp(self):
        self.karaoke_den = ClubMatrix("Karaoke Den", 12000.50, 5)

        self.room_a =  Rooms("Room A", [])
        self.room_b =  Rooms("Room B", [])
        self.room_c =  Rooms("Room C", [])
        self.room_d =  Rooms("Room D", [])
        self.room_e =  Rooms("Room E", [])

        self.retsuko = Guests("Retsuko", 6000, "Ace Of Spades by Motörhead")
        self.fenneko = Guests("Fenneko", 4500, "Stayin Alive by The Bee Gees")
        self.haida = Guests("Haida", 5000, "It Was A Good Day by Ice Cube")
        self.gori = Guests("Gori", 8000, "Single Ladies by Beyonce")
        self.washimi = Guests("Washimi", 10000, "Believe by Cher")
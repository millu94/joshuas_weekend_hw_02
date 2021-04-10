import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestClubMatrix(unittest.TestCase):

    def setUp(self):
        self.karaoke_den = ClubMatrix("Karaoke Den", 12000.50, 5)

        self.room_a =  Rooms("Room A")
        self.room_b =  Rooms("Room B")
        self.room_c =  Rooms("Room C")
        self.room_d =  Rooms("Room D")
        self.room_e =  Rooms("Room E")
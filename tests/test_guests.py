import unittest

from classes.club_matrix import ClubMatrix
#from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.retsuko = Guests("Retsuko", 6000, Songs("Ace Of Spades by Motörhead", "Metal"))
        self.fenneko = Guests("Fenneko", 4500, Songs("Stayin Alive by The Bee Gees", "Disco"))
        self.haida = Guests("Haida", 5000, Songs("It Was A Good Day by Ice Cube", "Hip Hop"))
        self.gori = Guests("Gori", 8000, Songs("Single Ladies by Beyonce", "Pop"))
        self.washimi = Guests("Washimi", 10000, Songs("Believe by Cher", "Dance" ))


    def test_guest_has_name(self):
        self.assertEqual("Fenneko", self.fenneko.name)

    def test_guest_has_cash(self):
        self.assertEqual(6000, self.retsuko.wallet)
    
    
    # def test_guests_fav_song(self):
    #     self.assertEqual("Single Ladies by Beyonce Pop", self.gori.fav_song)
import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.karaoke_den = ClubMatrix("Karaoke Den", 120000, 5)
        self.full_karaoke_den = ClubMatrix("Full Karaoke Den", 120000, 0)

        self.retsuko = Guests("Retsuko", 6000, "Ace Of Spades by Motörhead")
        self.fenneko = Guests("Fenneko", 4500, "Stayin Alive by The Bee Gees")
        self.haida = Guests("Haida", 5000, "It Was A Good Day by Ice Cube")
        self.gori = Guests("Gori", 8000, "Single Ladies by Beyonce")
        self.washimi = Guests("Washimi", 10000, "Believe by Cher")


    def test_guest_has_name(self):
        self.assertEqual("Fenneko", self.fenneko.name)

    def test_guest_has_cash(self):
        self.assertEqual(6000, self.retsuko.wallet)
    
    def test_guests_fav_song(self):
        self.assertEqual("Single Ladies by Beyonce", self.gori.fav_song)

    def test_guest_can_book_room(self):
        self.washimi.book_room(self.karaoke_den)
        self.assertEqual(9000, self.washimi.wallet)
        self.assertEqual(121000, self.karaoke_den.till)
        self.assertEqual(4, self.karaoke_den.available_rooms)

    def test_guest_cant_book_room(self):
        message = self.fenneko.book_room(self.full_karaoke_den)
        self.assertEqual("Sorry we're full!", message)

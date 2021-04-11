import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestClubMatrix(unittest.TestCase):

    def setUp(self):
        self.karaoke_den = ClubMatrix("Karaoke Den", 120000, 5)

        self.room_a =  Rooms("Room A", [], False)
        self.room_b =  Rooms("Room B", [], False)
        self.room_c =  Rooms("Room C", [], False)
        self.room_d =  Rooms("Room D", [], False)
        self.room_e =  Rooms("Room E", [], False)

        self.retsuko = Guests("Retsuko", 6000, "Ace Of Spades by Motörhead")
        self.fenneko = Guests("Fenneko", 4500, "Stayin Alive by The Bee Gees")
        self.haida = Guests("Haida", 5000, "It Was A Good Day by Ice Cube")
        self.gori = Guests("Gori", 8000, "Single Ladies by Beyonce")
        self.washimi = Guests("Washimi", 10000, "Believe by Cher")

    def test_whole_process_start_to_finish(self):
        #guest tries to book
        self.retsuko.book_room(self.karaoke_den)
        self.assertEqual(5000, self.retsuko.wallet)
        self.assertEqual(121000, self.karaoke_den.till)
        self.assertEqual(4, self.karaoke_den.available_rooms)
        #club checks them in

        #guest selects playlist
        #guest has a good time
        #club checks them out
        
import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.room_a = Rooms("Room A", [], False)
        self.room_b = Rooms("Room B", [], False)
        self.room_c = Rooms("Room C", [], False)
        self.room_d = Rooms("Room D", [], False)
        self.room_e = Rooms("Room E", [], True)

    def test_room_has_name(self):
        self.assertEqual("Room C", self.room_c.name)

    def test_room_has_empty_playlist(self):
        self.assertEqual([], self.room_d.playlist)

    def test_add_playlist_to_room(self):
        self.room_b.add_playlist_to_room("Funk")
        self.assertEqual(["Funk"], self.room_b.playlist)

    def test_check_in(self):
        self.room_d.check_in()
        self.assertEqual(True, self.room_d.occupied)

    def test_check_in_error(self):
        message = self.room_e.check_in()
        self.assertEqual("Choose another room", message)
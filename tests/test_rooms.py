import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.select_music = Songs("Choose playlist from songs.py")

        self.room_a = Rooms("Room A", [self.select_music.playlist["Disco"]], True)
        self.room_b = Rooms("Room B", [], False)
        self.room_c = Rooms("Room C", [], False)
        self.room_d = Rooms("Room D", [], False)
        self.room_e = Rooms("Room E", [], True)

    def test_room_has_name(self):
        self.assertEqual("Room C", self.room_c.name)

    def test_room_has_empty_playlist(self):
        self.assertEqual([], self.room_d.playlist)

    def test_room_has_playlist(self):
        self.assertEqual(
            [
                "Shining Star by Earth Wind & Fire",
                "Good Times by Chic",
                "This Time Baby by Jackie Moore",
                "Hollywood Swinging by Kool & The Gang",
                "Stayin Alive by The Bee Gees"
            ], 
            self.select_music.playlist["Disco"])

    def test_add_playlist_to_room(self):
        self.room_b.add_playlist_to_room("Funk")
        self.assertEqual(["Funk"], self.room_b.playlist)

    def test_check_in(self):
        self.room_d.check_in()
        self.assertEqual(True, self.room_d.occupied)

    def test_check_in_error(self):
        message = self.room_e.check_in()
        self.assertEqual("Choose another room", message)

    def test_check_out(self):
        self.room_a.check_out()
        self.assertEqual(False, self.room_a.occupied)
        self.assertEqual([], self.room_a.playlist)

    def test_check_out_error(self):
        message = self.room_b.check_out()
        self.assertEqual("Room is already vacant", message)
import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestSong(unittest.TestCase):
    def setUp(self):
        self.good_day = Songs("It Was A Good Day by Ice Cube")

    def test_song_has_name(self):
        self.assertEqual("It Was A Good Day by Ice Cube", self.good_day.name)

    def test_display_playlist(self):
        self.assertEqual(
            [
                "Highway To Hell by AC/DC",
                "You Can't Always Get What You Want by The Rolling Stones",
                "Foxy Lady by Jimi Hendrix",
                "Ace Of Spades by Motörhead",
                "Come As You Are by Nirvana",
            ], 
            self.good_day.playlist["Rock"])
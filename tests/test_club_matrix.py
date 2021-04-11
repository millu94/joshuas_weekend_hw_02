import unittest

from classes.club_matrix import ClubMatrix
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestClubMatrix(unittest.TestCase):

    def setUp(self):
        self.karaoke_den = ClubMatrix("Karaoke Den", 120000, 5)

        self.select_music = Songs("Choose playlist from songs.py")

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
        self.room_a.check_in()
        self.assertEqual(True, self.room_a.occupied)
        #guest selects playlist that is added to room
        music_selection = self.select_music.playlist["Rock"]
        self.room_a.add_playlist_to_room(music_selection)
        self.assertEqual(
            [
                "Highway To Hell by AC/DC",
                "You Can't Always Get What You Want by The Rolling Stones",
                "Foxy Lady by Jimi Hendrix",
                "Ace Of Spades by Motörhead",
                "Come As You Are by Nirvana",
            ],
            music_selection
        )
        self.assertEqual(
            [[
                "Highway To Hell by AC/DC",
                "You Can't Always Get What You Want by The Rolling Stones",
                "Foxy Lady by Jimi Hendrix",
                "Ace Of Spades by Motörhead",
                "Come As You Are by Nirvana",
            ]],
        self.room_a.playlist    
        )
        # guest has a good time
        message = self.retsuko.whoop_whoop()
        self.assertEqual("I'm having fun, these complimentary drinks are satisfactory.", message)
        # club checks them out
        self.room_a.check_out()
        self.assertEqual(False, self.room_a.occupied)
        self.assertEqual([], self.room_a.playlist)
        
        
import data
from data import Point, Rectangle, Duration, Song
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_case_1(self):
        p1 = Point(2, 2)
        p2 = Point(10, 10)
        rect = hw2.create_rectangle(p1, p2)
        self.assertEqual(rect.top_left.x, 2)
        self.assertEqual(rect.top_left.y, 10)
        self.assertEqual(rect.bottom_right.x, 10)
        self.assertEqual(rect.bottom_right.y, 2)

    def test_create_rectangle_case_2(self):
        p1 = Point(5, 5)
        p2 = Point(5, 10)
        rect = hw2.create_rectangle(p1, p2)
        self.assertEqual(rect.top_left.x, 5)
        self.assertEqual(rect.top_left.y, 10)
        self.assertEqual(rect.bottom_right.x, 5)
        self.assertEqual(rect.bottom_right.y, 5)

    # Part 2
    def test_shorter_duration_than_1(self):
        self.assertTrue(hw2.shorter_duration_than(Duration(3, 30), Duration(4, 0)))

    def test_shorter_duration_than_2(self):
        self.assertFalse(hw2.shorter_duration_than(Duration(5, 0), Duration(4, 59)))

    # Part 3
    def test_songs_shorter_than_1(self):
        songs = [
            Song("Artist A", "Song A", Duration(3, 30)),
            Song("Artist B", "Song B", Duration(4, 0)),
            Song("Artist C", "Song C", Duration(2, 45))
        ]
        result = hw2.songs_shorter_than(songs, Duration(4, 0))

        expected = [
            Song("Artist A", "Song A", Duration(3, 30)),
            Song("Artist C", "Song C", Duration(2, 45))
        ]
        self.assertEqual(result, expected)

    def test_songs_shorter_than_2(self):
        songs = [
            Song("Artist D", "Song D", Duration(5, 0)),
            Song("Artist E", "Song E", Duration(4, 30)),
            Song("Artist F", "Song F", Duration(4, 0))
        ]
        result = hw2.songs_shorter_than(songs, Duration(4, 0))

        self.assertEqual(result, [])

    # Part 4
    def test_running_time_1(self):
        songs = [
            Song("The Decemberists", "June Hymn", Duration(4, 30)),
            Song("Broken Bells", "October", Duration(3, 40)),
            Song("Kansas", "Dust in the Wind", Duration(3, 29)),
            Song("Local Natives", "Airplanes", Duration(3, 58))
        ]
        playlist = [0, 2, 1, 3, 0]
        result = hw2.running_time(songs, playlist)
        expected_duration = Duration(20, 7)
        self.assertEqual(result, expected_duration)

    def test_running_time_2(self):
        songs = [
            Song("Artist X", "Song X", Duration(2, 45)),
            Song("Artist Y", "Song Y", Duration(3, 15)),
            Song("Artist Z", "Song Z", Duration(1, 55))
        ]
        playlist = [0, 1, 2]
        result = hw2.running_time(songs, playlist)
        expected_duration = Duration(7, 55)
        self.assertEqual(result, expected_duration)

    # Part 5
    def test_validate_route_1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        self.assertTrue(hw2.validate_route(city_links, ['san luis obispo', 'santa margarita', 'atascadero']))

    def test_validate_route_2(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        self.assertFalse(hw2.validate_route(city_links, ['san luis obispo', 'atascadero']))

    # Part 6
    def test_longest_repetition_1(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 1, 1, 1, 3]), 4)

    def test_longest_repetition_2(self):
        self.assertEqual(hw2.longest_repetition([]), None)



if __name__ == '__main__':
    unittest.main()

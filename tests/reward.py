import unittest
from reward import *;

class MyTest(unittest.TestCase):
    def test_get_distance_from_edge(self):
        # Nearside
        self.assertEqual(
            get_distance_from_edge(60, 12, True),
            18
        )

        # Farside
        self.assertEqual(
            get_distance_from_edge(60, 12, False),
            42
        )

        # Sum near + far is track size
        track_size = 60
        sum = get_distance_from_edge(track_size, 12, False) + get_distance_from_edge(track_size, 12, True)

        self.assertEqual(
            sum,
            track_size
        )

if __name__ == '__main__':
    unittest.main()

import unittest
import sqlite3
from seat_assign_12450428_13537123_16200240 import *


class TestAirline(unittest.TestCase):

    def setUp(self):

        conn = sqlite3.connect("airline_seating.db")
        self.c = conn.cursor()

    def test_count_seats(self):
        """Return values for n_avail and total_rows"""

        plane_dimensions = count_seats(self.c)
        self.assertEqual(plane_dimensions, (58, 15))

        """working"""

    def test_empty_seats_check(self):
        """Return a dictionary with the values being a list of empty seats in each row"""

        conn1 = sqlite3.connect("1_empty_seat.db")
        c = conn1.cursor()
        total_rows = 1
        check = empty_seats_check(total_rows, c)
        self.assertDictEqual(check, {1: ['F']})

        conn2 = sqlite3.connect("empty_seat.db")
        d = conn2.cursor()
        total_rows = 1
        check = empty_seats_check(total_rows, d)
        self.assertDictEqual(check, {1: ['A', 'C', 'D', 'F']})

    def test_seat_rows(self):
        """Return a list of the keys from the empty_seats dictionary"""

        empty_seats = {1: ['A', 'C', 'D', 'F'], 2: ['A', 'C', 'F'], 3: ['A', 'C', 'D', 'F']}
        keys = seat_rows(empty_seats)
        self.assertEqual(keys, [1, 2, 3])

    def test_max_seats(self):
        """Return an integer indicating the largest number of seats available on the plane in one row"""

        seat_keys = [1, 2, 3]
        empty_seats = {1: ['A', 'C', 'D', 'F'], 2: ['A', 'C', 'F'], 3: ['A', 'C', 'D', 'F']}
        max_number_seats = max_seats(seat_keys, empty_seats)
        self.assertEqual(max_number_seats, 4)

    def test_refused_separated(self):
        """Return 2 integers: 1) the number of passengers refused, 2)the number of passengers separated from a member"""

        ref_sep = refused_separated(self.c)
        self.assertEqual(ref_sep, (0,0))

        conn = sqlite3.connect("5_ref_7_sep.db")
        c = conn.cursor()
        ref_sep_2 = refused_separated(c)
        self.assertEqual(ref_sep_2, (5, 7))





if __name__ == '__main__':
    unittest.main()

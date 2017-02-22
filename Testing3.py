import unittest
import sqlite3
from seat_assign_12450428_13537123_16200240 import *


class Test_Airline(unittest.TestCase):

    def test_count_seats(self):
        """Return values for n_avail and total_rows"""

        conn = sqlite3.connect("airline_seating.db")
        c = conn.cursor()

        plane_dimensions = count_seats(c)
        self.assertEqual(plane_dimensions, (58, 15))



if __name__ == '__main__':
    unittest.main()

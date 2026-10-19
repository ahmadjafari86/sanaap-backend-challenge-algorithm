import unittest

from circular_ones import has_four_consecutive_ones


class CircularOnesTests(unittest.TestCase):
    def test_valid_inputs(self):
        cases = [
            ("1010111", True),   # Three at the end, one at the start.
            ("1100011", True),   # Two at each boundary.
            ("1110001", True),   # One at the end, three at the start.
            ("0111100", True),   # Four inside the string.
            ("1111111", True),
            ("0000000", False),
            ("1110000", False),
            ("1010101", False),
            ("1100010", False),
        ]

        for bits, expected in cases:
            with self.subTest(bits=bits):
                self.assertEqual(has_four_consecutive_ones(bits), expected)

    def test_rejects_invalid_inputs(self):
        for bits in ("", "1111", "11111111", "1010201", "101 111"):
            with self.subTest(bits=bits), self.assertRaises(ValueError):
                has_four_consecutive_ones(bits)


if __name__ == "__main__":
    unittest.main()

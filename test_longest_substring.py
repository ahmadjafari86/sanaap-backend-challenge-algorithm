import unittest

from longest_substring import longest_unique_substring_length


class LongestUniqueSubstringTests(unittest.TestCase):
    def test_longest_unique_substring_length(self):
        cases = [
            ("", 0),
            ("A", 1),
            ("AAAA", 1),
            ("ABCDE", 5),
            ("ABCABCFKAB", 5),
            ("abba", 2),
            ("dvdf", 3),
            ("a b a", 3),
            ("سلام", 4),
        ]

        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(
                    longest_unique_substring_length(text),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
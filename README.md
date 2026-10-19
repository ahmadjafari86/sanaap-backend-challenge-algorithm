# Sanaap Backend Challenge — Algorithms

Python solutions to the two algorithm problems in the Sanaap backend assessment.

## Requirements

- Python 3.10+
- No third-party dependencies

## Run Tests

From the repository root:

```bash
python3 -m unittest discover -v
```

## 1. Longest Substring Without Repeated Characters

Returns the length of the longest contiguous substring containing no repeated
characters.

```python
from longest_substring import longest_unique_substring_length

print(longest_unique_substring_length("ABCABCFKAB"))  # 5
```

### Approach

A sliding window tracks a substring without repeated characters. A dictionary
stores the last index of each character. When a repeated character occurs inside
the current window, its start moves past the previous occurrence.

- Expected time complexity: O(n), assuming average O(1) dictionary operations.
- Space complexity: O(k), where k is the number of distinct input characters.
- An empty string returns 0.
- Characters are compared case-sensitively as Python Unicode code points.

## 2. Four Consecutive Ones in a Circular Binary String

Checks whether a seven-digit binary string contains at least four consecutive
ones, including sequences crossing the end-to-start boundary.

```python
from circular_ones import has_four_consecutive_ones

print(has_four_consecutive_ones("1010111"))  # True
print(has_four_consecutive_ones("1010101"))  # False
```

### Approach

Append the first three characters to the input, then search for `1111`.
This covers every possible four-character window crossing the circular boundary.

- The input must contain exactly seven characters, each either `0` or `1`.
- Invalid string inputs raise ValueError.
- Time and space complexity are O(1) for the fixed seven-digit input.
- For variable-length input, this approach takes O(n) time and O(n) extra space.

## Test Coverage

Tests cover empty strings, repeated characters, unique characters, Unicode,
sliding-window boundaries, circular matches, absent matches, and invalid binary
string inputs.
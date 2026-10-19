def longest_unique_substring_length(text: str) -> int:
    """Return the length of the longest substring without repeated characters."""
    last_seen: dict[str, int] = {}
    start = 0
    longest = 0

    for end, character in enumerate(text):
        previous_index = last_seen.get(character)

        if previous_index is not None and previous_index >= start:
            start = previous_index + 1

        last_seen[character] = end
        longest = max(longest, end - start + 1)

    return longest
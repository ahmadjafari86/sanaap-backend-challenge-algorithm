def has_four_consecutive_ones(bits: str) -> bool:
    """Check a seven-digit circular binary string for four consecutive ones."""
    if len(bits) != 7 or any(character not in "01" for character in bits):
        raise ValueError("Expected exactly seven binary digits.")

    return "1111" in bits + bits[:3]
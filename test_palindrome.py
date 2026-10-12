"""
Test Suite for Palindrome Checker
=================================
Tests `is_palindrome` function using plain Python assert statements.
Covers valid, invalid, mixed-case, extra-space/punctuation, and empty-string cases.
"""

from palindrome_checker import is_palindrome


def test_valid_palindromes():
    """Test standard single-word and numeric valid palindromes."""
    assert is_palindrome("madam") is True, "Failed on 'madam'"
    assert is_palindrome("racecar") is True, "Failed on 'racecar'"
    assert is_palindrome("noon") is True, "Failed on 'noon'"
    assert is_palindrome("kayak") is True, "Failed on 'kayak'"
    assert is_palindrome("level") is True, "Failed on 'level'"
    assert is_palindrome("12321") is True, "Failed on '12321'"
    assert is_palindrome("a") is True, "Failed on single character 'a'"


def test_invalid_palindromes():
    """Test standard invalid palindromes."""
    assert is_palindrome("hello") is False, "Failed on 'hello'"
    assert is_palindrome("Python programming") is False, "Failed on 'Python programming'"
    assert is_palindrome("OpenAI is great") is False, "Failed on 'OpenAI is great'"
    assert is_palindrome("world") is False, "Failed on 'world'"
    assert is_palindrome("123456") is False, "Failed on '123456'"


def test_mixed_case():
    """Test palindromes with mixed uppercase and lowercase letters."""
    assert is_palindrome("Racecar") is True, "Failed on 'Racecar'"
    assert is_palindrome("Madam") is True, "Failed on 'Madam'"
    assert is_palindrome("rAcEcAr") is True, "Failed on 'rAcEcAr'"
    assert is_palindrome("AbBa") is True, "Failed on 'AbBa'"
    assert is_palindrome("Rotator") is True, "Failed on 'Rotator'"


def test_extra_spaces_and_punctuation():
    """Test sentences with spaces, tabs, and punctuation marks."""
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("A man, a plan, a canal: Panama!") is True
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome("Was it a car or a cat I saw") is True
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("No 'x' in Nixon") is True
    assert is_palindrome("Step on no pets.") is True
    assert is_palindrome("   deified   ") is True
    assert is_palindrome("top spot") is True


def test_empty_string_and_edge_cases():
    """Test empty string and strings containing only whitespace or punctuation."""
    # An empty string reads identically forwards and backwards (trivial palindrome)
    assert is_palindrome("") is True, "Failed on empty string"
    assert is_palindrome("   ") is True, "Failed on whitespace-only string"
    assert is_palindrome("!@#$%^&*()") is True, "Failed on punctuation-only string"


def run_all_tests():
    """Run all test functions and report results."""
    print("Running Palindrome Checker test suite...")

    test_valid_palindromes()
    print("  [PASS] Valid palindromes")

    test_invalid_palindromes()
    print("  [PASS] Invalid palindromes")

    test_mixed_case()
    print("  [PASS] Mixed case normalization")

    test_extra_spaces_and_punctuation()
    print("  [PASS] Spaces and punctuation handling")

    test_empty_string_and_edge_cases()
    print("  [PASS] Empty strings and edge cases")

    print("\nAll tests passed successfully! (100% assertions verified)")


if __name__ == "__main__":
    run_all_tests()

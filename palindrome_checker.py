"""
Palindrome Checker
==================
A Python program that determines whether a word or sentence is a palindrome
after normalizing case and ignoring spaces and punctuation.
"""

import string


def is_palindrome(text: str) -> bool:
    """
    Check whether a given word or sentence is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward (e.g., 'madam' or 'Racecar').

    Steps performed:
    1. Normalization: Convert all characters to lowercase.
    2. Filtering: Keep only alphanumeric characters (letters and digits),
       removing spaces and punctuation.
    3. Reversal & Comparison: Reverse the cleaned string using Python's
       slice notation `[::-1]` and compare it to the original cleaned string.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the normalized text is a palindrome, False otherwise.
    """
    # Step 1 & 2: Normalize case to lowercase and remove spaces/punctuation.
    # We use a generator expression with `char.isalnum()` to retain only
    # letters and digits, and `.lower()` to ensure case-insensitivity.
    cleaned = "".join(char.lower() for char in text if char.isalnum())

    # Step 3: Compare cleaned string with its reverse using slicing.
    # Slicing syntax: [start:stop:step].
    # A step of -1 traverses the string from right to left (reversing it).
    return cleaned == cleaned[::-1]


def run_demo() -> None:
    """
    Run a built-in demonstration showcasing predefined valid and invalid palindromes.
    """
    print("=" * 60)
    print("           PALINDROME CHECKER - BUILT-IN DEMO")
    print("=" * 60)

    demo_cases = [
        # Valid palindromes
        ("madam", True),
        ("Racecar", True),
        ("A man a plan a canal Panama", True),
        ("Never odd or even", True),
        ("Was it a car or a cat I saw", True),
        # Invalid palindromes
        ("hello", False),
        ("Python programming", False),
        ("OpenAI is great", False),
    ]

    print("\nDemonstrating Sample Inputs:\n")
    for phrase, expected in demo_cases:
        result = is_palindrome(phrase)
        status = "Palindrome" if result else "Not a palindrome"
        label = "VALID" if expected else "INVALID"
        print(f"  [{label:7}] \"{phrase}\" -> {status}")

    print("\n" + "=" * 60 + "\n")


def main() -> None:
    """
    Main interactive loop for the Palindrome Checker.

    Prompts the user for input, checks if it is a palindrome,
    handles empty input gracefully, and allows exiting via 'quit'.
    """
    # Display built-in demo first
    run_demo()

    print("Welcome to the Interactive Palindrome Checker!")
    print("Type any word or sentence to check, or type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("Enter text: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye! Thanks for using Palindrome Checker.")
            break

        # Check if user wants to exit
        if user_input.strip().lower() in ("quit", "exit", "q"):
            print("Exiting Palindrome Checker. Goodbye!")
            break

        # Handle empty or whitespace-only input gracefully
        if not user_input.strip():
            print("(!) Friendly notice: Input is empty. Please enter a word or sentence.\n")
            continue

        # Check if the input contains at least one alphanumeric character
        if not any(char.isalnum() for char in user_input):
            print(
                "(!) Notice: Input contains no letters or numbers. "
                "Please include at least one alphanumeric character.\n"
            )
            continue

        # Evaluate palindrome
        if is_palindrome(user_input):
            print(f" -> \"{user_input}\" IS a palindrome! [YES]\n")
        else:
            print(f" -> \"{user_input}\" IS NOT a palindrome. [NO]\n")


if __name__ == "__main__":
    main()

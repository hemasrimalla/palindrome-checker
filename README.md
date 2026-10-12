# Palindrome Checker

A lightweight, beginner-friendly Python program that determines whether a word or sentence is a palindrome after normalizing case, removing spaces, and stripping punctuation.

---

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [Running Tests](#running-tests)
- [Sample Inputs and Outputs](#sample-inputs-and-outputs)
- [Interview Questions & Answers](#interview-questions--answers)
- [Project Structure](#project-structure)

---

## Overview

A **palindrome** is a word, phrase, number, or other sequence of characters that reads the same forward and backward (e.g., *madam*, *racecar*, or *A man, a plan, a canal: Panama!*).

This project demonstrates core string manipulation and comparison techniques in Python using only the standard library.

---

## How It Works

The core algorithm consists of three simple steps:

```
+--------------------+      +--------------------+      +--------------------+
|  1. Normalize Case | ---> | 2. Filter Alphanum | ---> |  3. Slice & Compare|
|     (lower())      |      |   (char.isalnum()) |      | (cleaned[::-1] ==) |
+--------------------+      +--------------------+      +--------------------+
```

1. **Normalize Case**:
   Convert the entire string to lowercase using `.lower()`. This ensures case-insensitivity so `"Racecar"` is treated identically to `"racecar"`.

2. **Remove Spaces & Punctuation**:
   Use a comprehension with `char.isalnum()` to filter out whitespace, commas, periods, apostrophes, and punctuation marks, keeping only alphanumeric characters:
   ```python
   cleaned = "".join(char.lower() for char in text if char.isalnum())
   ```

3. **Reverse with String Slicing & Compare**:
   Reverse the cleaned string using Python's slice syntax `[::-1]`, and check if it is equal to the original cleaned string:
   ```python
   return cleaned == cleaned[::-1]
   ```

---

## How to Run

Ensure you have Python 3 installed. No external packages are required.

Run the interactive program:
```bash
python palindrome_checker.py
```

### Interactive Commands:
- Enter any phrase or word to test whether it is a palindrome.
- Empty inputs are handled gracefully with a friendly warning.
- Type `quit` or `exit` to terminate the program.

---

## Running Tests

Run the built-in test suite to verify all test cases:

```bash
python test_palindrome.py
```

The test suite uses plain `assert` statements covering:
- Valid palindromes (words, numbers, single characters)
- Invalid words and phrases
- Mixed-case variations
- Extra spaces, tabs, and punctuation
- Empty string and whitespace-only edge cases

---

## Sample Inputs and Outputs

| Input | Normalized String | Result | Status |
| :--- | :--- | :--- | :--- |
| `"madam"` | `madam` | `Palindrome` | Valid |
| `"Racecar"` | `racecar` | `Palindrome` | Valid |
| `"A man a plan a canal Panama"` | `amanaplanacanalpanama` | `Palindrome` | Valid |
| `"Never odd or even"` | `neveroddoreven` | `Palindrome` | Valid |
| `"Was it a car or a cat I saw"` | `wasitacaroracatisaw` | `Palindrome` | Valid |
| `"No 'x' in Nixon"` | `noxinnixon` | `Palindrome` | Valid |
| `"hello"` | `hello` | `Not a palindrome` | Invalid |
| `"Python programming"` | `pythonprogramming` | `Not a palindrome` | Invalid |
| `"OpenAI is great"` | `openaiisgreat` | `Not a palindrome` | Invalid |

---

## Interview Questions & Answers

### 1. What is string slicing?
String slicing is a feature in Python that allows you to extract a subset of characters from a sequence (such as a string, list, or tuple).

- **Syntax:** `sequence[start:stop:step]`
  - `start` (inclusive): The index where the slice begins (defaults to `0`).
  - `stop` (exclusive): The index where the slice ends (defaults to sequence length).
  - `step`: The stride or direction of the slice (defaults to `1`).
- **Example:**
  ```python
  text = "Python"
  print(text[0:4])    # "Pyth"
  print(text[::2])     # "Pto" (every second character)
  print(text[::-1])    # "nohtyP" (reversed)
  ```

---

### 2. How can you reverse a string in Python?
There are several standard ways to reverse a string in Python:

1. **Extended Slicing (`[::-1]`) [Recommended & Idiomatic]:**
   ```python
   reversed_str = text[::-1]
   ```
   *Fastest and most concise because it executes directly at the C level.*

2. **Using `reversed()` and `str.join()`:**
   ```python
   reversed_str = "".join(reversed(text))
   ```
   *Creates an iterator that yields characters from right to left, joined into a new string.*

3. **Using a loop / accumulator (Manual):**
   ```python
   reversed_str = ""
   for char in text:
       reversed_str = char + reversed_str
   ```

---

### 3. Are strings mutable in Python?
**No, strings in Python are immutable.**

Once a string object is created, its contents cannot be modified in place.
- Attempting to modify an index raises a `TypeError`:
  ```python
  s = "hello"
  s[0] = "y"  # TypeError: 'str' object does not support item assignment
  ```
- Every string method (such as `.lower()`, `.replace()`, `.strip()`, or slicing `[::-1]`) creates and returns a **new string object** in memory rather than altering the existing one.
- Immutability provides several benefits in Python:
  - **Thread-safety:** Multiple threads can safely read strings without locks.
  - **Hashability:** Because strings cannot change, their hash value is constant, allowing them to be used as dictionary keys and set elements.
  - **Memory optimization (String Interning):** Python can reuse identical string literals in memory to save space.

---

## Project Structure

```
palindrome-checker/
├── palindrome_checker.py   # Main application with core logic, demo, and CLI loop
├── test_palindrome.py       # Comprehensive unit tests using plain assert statements
└── README.md                # Documentation, guide, and interview answers
```

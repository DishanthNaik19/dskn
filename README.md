# Python Palindrome Checker

This repository contains comprehensive Python implementations for checking palindromes using different approaches.

## Files

- `palindrome.py` - Comprehensive implementation with multiple algorithms
- `simple_palindrome.py` - Simple, concise implementation for quick use

## What is a Palindrome?

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

Examples:
- "racecar"
- "A man a plan a canal Panama"
- "Madam, I'm Adam"
- "12321"

## Algorithms Implemented

### 1. Simple Method (`is_palindrome_simple`)
- Uses string slicing with `[::-1]` to reverse the string
- Time Complexity: O(n)
- Space Complexity: O(n)

### 2. Two Pointers (`is_palindrome_two_pointers`)
- Uses two pointers starting from both ends
- Time Complexity: O(n)
- Space Complexity: O(n) for cleaning the string

### 3. Recursive Method (`is_palindrome_recursive`)
- Recursively checks first and last characters
- Time Complexity: O(n)
- Space Complexity: O(n) due to recursion stack

### 4. Stack Method (`is_palindrome_stack`)
- Uses a stack to store the first half
- Time Complexity: O(n)
- Space Complexity: O(n)

## Additional Functions

### Find Longest Palindrome (`find_longest_palindrome`)
- Finds the longest palindrome substring in a given string
- Uses the "expand around center" technique
- Time Complexity: O(n²)
- Space Complexity: O(1)

### Count Palindromes (`count_palindromes`)
- Counts all palindrome substrings in a given string
- Time Complexity: O(n²)
- Space Complexity: O(1)

## Usage

### Quick Start
```python
from simple_palindrome import is_palindrome

# Check if a string is a palindrome
result = is_palindrome("racecar")  # True
result = is_palindrome("hello")    # False
```

### Comprehensive Usage
```python
from palindrome import (
    is_palindrome_simple,
    is_palindrome_two_pointers,
    is_palindrome_recursive,
    is_palindrome_stack,
    find_longest_palindrome,
    count_palindromes
)

# Check palindrome using different methods
text = "A man a plan a canal Panama"
print(is_palindrome_simple(text))      # True
print(is_palindrome_two_pointers(text)) # True
print(is_palindrome_recursive(text))    # True
print(is_palindrome_stack(text))        # True

# Find longest palindrome
longest = find_longest_palindrome("babad")  # "bab"
print(longest)

# Count palindromes
count = count_palindromes("aaa")  # 6 (a, a, a, aa, aa, aaa)
print(count)
```

## Running the Examples

### Run the comprehensive example:
```bash
python palindrome.py
```

### Run the simple example:
```bash
python simple_palindrome.py
```

## Features

- **Case Insensitive**: Ignores uppercase/lowercase differences
- **Punctuation Ignored**: Removes spaces, punctuation, and special characters
- **Multiple Algorithms**: Different approaches for educational purposes
- **Interactive Mode**: Test your own strings
- **Comprehensive Testing**: Includes various test cases
- **Documentation**: Well-documented functions with examples

## Test Cases Included

- Simple palindromes: "racecar", "12321"
- Phrases with spaces: "A man a plan a canal Panama"
- Phrases with punctuation: "Madam, I'm Adam"
- Non-palindromes: "hello", "ab"
- Edge cases: empty string, single character, two characters

## Performance Comparison

For most practical purposes, the simple method using string slicing (`[::-1]`) is the most readable and efficient. The two-pointers approach might be preferred in interviews or when you want to show algorithmic thinking.

All methods handle the same edge cases and produce identical results for valid inputs.
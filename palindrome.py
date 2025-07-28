def is_palindrome_simple(text):
    """
    Simple palindrome checker that ignores case and spaces.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Convert to lowercase and remove spaces
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointers(text):
    """
    Palindrome checker using two pointers approach.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    if not cleaned:
        return True
    
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


def is_palindrome_recursive(text):
    """
    Recursive palindrome checker.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    def check_palindrome(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return check_palindrome(s[1:-1])
    
    return check_palindrome(cleaned)


def is_palindrome_stack(text):
    """
    Palindrome checker using stack approach.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    if not cleaned:
        return True
    
    # Push first half to stack
    stack = []
    mid = len(cleaned) // 2
    
    for i in range(mid):
        stack.append(cleaned[i])
    
    # Start from middle (or middle + 1 for odd length)
    start = mid if len(cleaned) % 2 == 0 else mid + 1
    
    # Compare with stack
    for i in range(start, len(cleaned)):
        if not stack or stack.pop() != cleaned[i]:
            return False
    
    return True


def find_longest_palindrome(text):
    """
    Find the longest palindrome substring in a given string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The longest palindrome substring
    """
    if not text:
        return ""
    
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    
    for i in range(len(text)):
        # Check odd length palindromes
        palindrome1 = expand_around_center(text, i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
        # Check even length palindromes
        palindrome2 = expand_around_center(text, i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
    
    return longest


def count_palindromes(text):
    """
    Count the number of palindrome substrings in a given string.
    
    Args:
        text (str): The input string
        
    Returns:
        int: Number of palindrome substrings
    """
    if not text:
        return 0
    
    def expand_around_center(s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total_count = 0
    
    for i in range(len(text)):
        # Count odd length palindromes
        total_count += expand_around_center(text, i, i)
        
        # Count even length palindromes
        total_count += expand_around_center(text, i, i + 1)
    
    return total_count


# Test cases and examples
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "Madam, I'm Adam",
        "Was it a car or a cat I saw?",
        "hello",
        "12321",
        "Never odd or even",
        "",
        "a",
        "aa",
        "ab"
    ]
    
    print("Palindrome Checker Results:")
    print("=" * 50)
    
    for test in test_cases:
        print(f"Input: '{test}'")
        print(f"  Simple method: {is_palindrome_simple(test)}")
        print(f"  Two pointers: {is_palindrome_two_pointers(test)}")
        print(f"  Recursive: {is_palindrome_recursive(test)}")
        print(f"  Stack method: {is_palindrome_stack(test)}")
        print()
    
    print("Longest Palindrome Examples:")
    print("=" * 50)
    
    test_strings = [
        "babad",
        "cbbd",
        "racecar",
        "hello world"
    ]
    
    for test in test_strings:
        longest = find_longest_palindrome(test)
        count = count_palindromes(test)
        print(f"String: '{test}'")
        print(f"  Longest palindrome: '{longest}'")
        print(f"  Total palindromes: {count}")
        print()
    
    # Interactive mode
    print("Interactive Palindrome Checker")
    print("=" * 50)
    print("Enter strings to check (type 'quit' to exit):")
    
    while True:
        user_input = input("\nEnter a string: ").strip()
        if user_input.lower() == 'quit':
            break
        
        if is_palindrome_simple(user_input):
            print(f"'{user_input}' is a palindrome!")
        else:
            print(f"'{user_input}' is not a palindrome.")
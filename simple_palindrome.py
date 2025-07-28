def is_palindrome(text):
    """
    Check if a string is a palindrome.
    Ignores case, spaces, and punctuation.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Clean the text: lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if it reads the same forwards and backwards
    return cleaned == cleaned[::-1]


# Example usage
if __name__ == "__main__":
    # Test cases
    test_strings = [
        "racecar",
        "A man a plan a canal Panama",
        "Madam, I'm Adam",
        "hello",
        "12321",
        "Never odd or even"
    ]
    
    print("Palindrome Checker")
    print("=" * 30)
    
    for text in test_strings:
        result = is_palindrome(text)
        print(f"'{text}' -> {'✓' if result else '✗'}")
    
    # Interactive mode
    print("\nEnter your own strings to test (type 'quit' to exit):")
    while True:
        user_input = input("\nEnter a string: ").strip()
        if user_input.lower() == 'quit':
            break
        
        if is_palindrome(user_input):
            print(f"✓ '{user_input}' is a palindrome!")
        else:
            print(f"✗ '{user_input}' is not a palindrome.")
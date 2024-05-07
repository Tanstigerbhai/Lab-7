def reverse_string(s):
    # Base case: If the string is empty or contains only one character, return it as is
    if len(s) <= 1:
        return s
    
    # Recursive case: Separate the first character from the remaining characters
    first_char = s[0]
    remaining_chars = s[1:]
    
    # Recursively call reverse_string on the remaining characters
    reversed_remaining = reverse_string(remaining_chars)
    
    # Append the first character to the end of the reversed remaining string
    return reversed_remaining + first_char

# Example usage
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("Python"))  # Output: "nohtyp"
print(reverse_string(""))  # Output: ""

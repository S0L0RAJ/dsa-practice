# Check palindrome
def is_palindrome(s):
    return s == s[::-1]

# Count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Reverse string
def reverse_string(s):
    return s[::-1]

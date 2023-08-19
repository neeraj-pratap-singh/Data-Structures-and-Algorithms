# WAP to check if given string is palindrome or not
def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitivity
    length = len(s)
    is_palindrome = True
    
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            is_palindrome = False
            break
    
    return is_palindrome

# Test cases
string1 = "kayak"
string2 = "hello"
string3 = "Testing"

print(is_palindrome(string1))  # Output: True
print(is_palindrome(string2))  # Output: False
print(is_palindrome(string3))  # Output: True

def is_palindrome(s):
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same
    elif s[0] == s[-1]:
        # If they are the same, check if the substring excluding these characters is a palindrome
        return is_palindrome(s[1:-1])
    else:
        # If the first and last characters are not the same, it's not a palindrome
        return False

# Test the function
test_string = "racecar"
if is_palindrome(test_string):
    print(test_string, "is a palindrome.")
else:
    print(test_string, "is not a palindrome.")

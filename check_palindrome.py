def is_palindrome(string):
    return string == string[::-1]

string = input("Enter the string: ")

print(is_palindrome(string))

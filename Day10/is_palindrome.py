'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(str):
    return "".join(str[::-1].split()).lower() == "".join(str.split()).lower()

print(is_palindrome('testing'))
print(is_palindrome('tacocat'))
print(is_palindrome('hannah'))
print(is_palindrome('a man a plan a canal Panama'))

# str = "Bla True False"
# print("".join(str.split()).lower())
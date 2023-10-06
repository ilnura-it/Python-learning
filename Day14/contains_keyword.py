import keyword

def contains_keyword(*arg):
     for word in arg:
        if keyword.iskeyword(word):
           return True
     return False


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))
print(contains_keyword("four", "for", "if"))
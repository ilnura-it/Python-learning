def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    
    return "Not sure who you are..."

print(ensure_correct_info()) # Not sure who you are...
print(ensure_correct_info(1, True, "Steele", "Colt")) # Welcome back Colt!

def contains_purple(*args):
    if "purple" in args:
        return True
    return False

print(contains_purple(25, "purple"))
print(contains_purple("green", False, 37, "blue", "hello world"))
print(contains_purple("purple"))
print(contains_purple("a", 99, "blah blah blah", 1, True, False, "purple"))
print(contains_purple(1,2,3))

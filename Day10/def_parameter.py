def add(a,b):
    return a + b

def math(a, b, fn=add):
    return fn(a,b)

def substract(a,b):
    return a - b

print(math(2,2))

print(math(2,2, substract))
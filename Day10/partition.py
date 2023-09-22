'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(list, fn):
    newList = []
    newList.append([val for val in list if fn(val)])
    newList.append([val for val in list if fn(val) == False])
    return newList

# Second solution

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

# Third solution

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

# Fourth solution

def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]
'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

# Write a function called yes_or_no, which returns a generator that first yields yes , then no , then yes , then no , and so on.

def yes_or_no():
    answer = ['yes', 'no']
    while True:
        yield answer[0]
        answer[0], answer[1] = answer[1], answer[0] 

# def yes_or_no():
#     answer = "yes"
#     while True:
#         yield answer
#         answer = "no" if answer == "yes" else "yes"
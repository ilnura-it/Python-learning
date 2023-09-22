def multiple_letter_count(str):
    return {x:str.count(x) for x in str}

print(multiple_letter_count("awesome"))
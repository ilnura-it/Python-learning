'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
def single_letter_count(str, char):
        return str.lower().count(char.lower())

print(single_letter_count("Hello World", "h"))
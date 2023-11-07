# Write a function called make_song, which takes a count and a beverage, and returns a generator that yields verses from a popular song about a the beverage. The number of verses in the song is determined by the count. Each verse of the song should involve one fewer beverage, until there are no beverages remaining. (Check the examples for details on the structure of the lyrics.)The default count should be 99, and the default beverage should be soda.

def make_song(num=99, str="soda"):
    for i in range(num, -1, -1):
        if i > 1:
            yield f"{i} bottles of {str} on the wall."
        elif i == 1:
            yield f"Only 1 bottle of {str} left!"
        else:
            yield f"No more {str}!"
        i -= 1
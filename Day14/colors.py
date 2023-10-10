import termcolor 
# print(dir(termcolor)) # ['ATTRIBUTES', 'COLORS', 'HIGHLIGHTS', 'RESET', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'annotations', 'colored', 'cprint', 'termcolor'] - not very useful


# help(termcolor)

text = termcolor.colored("Hi There!", color="cyan")
text2 = termcolor.colored("This text will be printed in colors!", color = "yellow",on_color="on_magenta", attrs=['blink'])
print(text)
print(text2)

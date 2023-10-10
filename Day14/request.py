import pyfiglet
import termcolor 

text = input("What message do you want to print? ")
user_color = input("What Color? ")

color_list = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan')

if user_color not in color_list:
   user_color = "magenta"

print(termcolor.colored(pyfiglet.figlet_format(text, font="slant"), color=user_color) )

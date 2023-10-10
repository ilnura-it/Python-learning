import pyfiglet
import termcolor 

color_list = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan')

text = input("What message do you want to print? ")
color = input("What Color? ")

def print_art(msg, color):
   if color not in color_list:
      color = "magenta"
   print(termcolor.colored(pyfiglet.figlet_format(text, font="slant"), color=color) )

print_art(text, color)







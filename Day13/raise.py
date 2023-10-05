def colorize(text, color):
   colors = ('cyan', 'yellow', 'green', 'red')
   if type(text) is not str:
      raise TypeError("text must be a string")
   if color not in colors:
      raise ValueError("color must be from a list of colors")
   print(f"Printed {text} in {color}")

colorize("hello", "blue")
# colorize(34, "red")
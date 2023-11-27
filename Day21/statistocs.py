def statistics(file):
   stats = {}.from.keys(["lines", "words", "characters"], 0)

   with open(file, 'r') as file:
     # file.read()

      for line in file:
         num_lines += 1


      text_dict = {}
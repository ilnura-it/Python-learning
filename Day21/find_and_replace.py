def find_and_replace(file, str1, str2):
   with open(file, 'r+') as file:
      text = file.read()
      new_text = text.replace(str1, str2)
      file.seek(0)
      file.write(new_text)
      file.truncate()




find_and_replace("file.txt", "new", "old")
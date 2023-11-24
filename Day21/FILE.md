# Working with files

## Reading Files

- You can read a file with the ***open*** function
- ***open*** returns a file object to you

         file = open("file.txt")
         file
         # <_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>
         file.read()
         # 'This is a file.txt file.'

## Cursor Movement

- Python reds files by using a cursor
- This is like the cursor you see when you're typing
- After a file is read, the cursor is at the end
- To move the cursor, use the ***seek*** method

         # Update our file.txt file
         file.read()
         # "\nNow I'm updating this file.\nAdding new lines."

         file.seek(0)
         # 0 is the zero character
         file.read()
         "This is a file.txt file.\nNow I'm updating this file.\nAdding new lines."

         file.readline() # to read individual lines
         # 'This is a file.txt file.\n'

         file.readlines() # to read all lines

## Closing a file

 - You can close a file with the ***close*** method
 - You can check if a file is closed with the closed attribute
 - Once closed, a file can't be read again
 - Always close files - it frees up the system resources!!!

            file.closed
            # False
            file.close()
            file.closed
            # True

## Option II to open files. It closes files automatically! Used more often

            with open("file.txt") as file:
               file.read()

## Writing to Text Files

- You can also use ***open*** to write to a file
-  Need to specify the "w" flag as the second argument to write

            with open("file.txt", "w") as file:
               file.write("Writing files is great.\n")
               file.write("Knowing Python is great.\n")
               file.write("Having an interesting job is great.\n")

## Modes for Opening Files

- ***r*** - Read a file(no writing) - this is default
- ***w*** - Write to a file (previous contents removed)
- ***a*** - Append to a file
- ***r+*** - Read and write to a file (writing based on cursor, overwrite previous content)
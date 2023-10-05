# Common Error Types in Python
 - SyntaxError
 - TypeError
 - NameError
 - ValueError
 - IndexError
 - KeyError
 - AttributeError

 ## Raise keyword

 In python we can also throw errors using the **raise** keyword. This is helpful when creating your own kinds of exception and error messages.

      raise ValueError ('invalid value' )

## Handle Errors

In Python, it is strongly encouraged to use ***try/except*** blocks, to catch exceptions when we can do something about them. 

      try:
         foobar
      except NameError as err:
         print(err) 

## Debugging with pdb

pdb - python debugger, module

      import pdb, pdb.set_trace()
### Common pdb commands
l = list
n = next line
p = print
c = continue, finish debugging

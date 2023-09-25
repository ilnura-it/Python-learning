def calculate(**kwargs):
    # print(args)

   operation_lookup = {
   'add': kwargs.get('first', 0) + kwargs.get('second', 0),
   'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
   'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
   'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
   }
   operation_value = operation_lookup[kwargs.get('operation', '')]
   message = kwargs.get("message", 'The result is')

   if kwargs["make_float"] == False:
      return f"{message} {int(operation_value)}"
   else:
      return f"{message} {float(operation_value)}"

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))

print(calculate(make_float=True, operation='divide', first=3.5, second=5))
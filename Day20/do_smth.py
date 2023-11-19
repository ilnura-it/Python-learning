def do_something_bad(user):
   assert user.is_admin, "Only admins can do bad things!"
   destroy_a_bunch_of_stuff()
   return "Mua ha ha ha!"

def destroy_a_bunch_of_stuff():
   print("Destroyed")
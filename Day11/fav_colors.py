def fav_colors(**kwargs):
    # 1 print(kwargs)
    for person, color in kwargs.items():
      print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby='red', ethel="teal") # 1 {'colt': 'purple', 'ruby': 'red', 'ethel': 'teal'}
# 2 colt's favorite color is purple
# ruby's favorite color is red
# ethel's favorite color is teal
for num in range(1, 21):
    if num == 4 or num == 13:
        print(f"Number {num} is UNLUCKY")
    elif num % 2 == 0:
        print(f"Number {num} is even")
    else:
        print(f"Number {num} is odd")

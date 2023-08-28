# Nested List
coords = [[10.423, 9.132], [21.546, 7.32], [14.69, -15.987]]

# for loc in coords:
#     for coord in loc:
#         print(coord)

[[print(val) for val in l] for l in coords]

###########
board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

###########
[["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]

# [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]

[[num for num in range(3)] for num in range(1, 4)] #[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
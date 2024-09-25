# nested slicing:
h = [5, ([2, [9, 5], 'o'], (5, [2, '*'], 99, ["$", ("#", [(11)]), ['4'], 3]), 0), 2, 1]
# 'o',11,9,99,'4' - positive,negative

# positive slicing:
h = [5, ([2, [9, 5], 'o'], (5, [2, '*'], 99, ["$", ("#", [(11)]), ['4'], 3]), 0), 2, 1]
print(h[1][0][2])  # o
print(h[1][1][3][1][1][0])  # 11
print(h[1][0][1][0])  # 9
print(h[1][1][2])  # 99
print(h[1][1][3][2][0])  # 4

# negative slicing:
h = [5, ([2, [9, 5], 'o'], (5, [2, '*'], 99, ["$", ("#", [(11)]), ['4'], 3]), 0), 2, 1]
print(h[-3][-3][-1])  # o
print(h[-3][-2][-1][-3][-1][-1])  # 11
print(h[-3][-3][-2][-2])  # 9
print(h[-3][-2][-2])  # 99
print(h[-3][-2][-1][-2][-1])  # 4

h = [5, ([2, [9, 5], 'o'], (5, [2, '*'], 99, ["$", ("#", [(11)]), ['4'], 3]), 0), 2, 1]
# 9
print(h[1][0][1][0]) #9
print(h[1][1][2]) #99
print(h[1][1][3][3]) #3
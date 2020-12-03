file = open('map.txt')
map_list = file.read().splitlines()

# PROGRAM RUNS 3 RIGHT, 1 DOWN (323 times)
x = 0
y = 0
trees = 0

while y != 322:
    x += 3
    if x > 30:
        x -= 31
    y += 1
    if map_list[y][x] == '#':
        trees += 1

print(trees)

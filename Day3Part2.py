file = open('map.txt')
map_list = file.read().splitlines()

def treeSearch(right_val, down_val):
    x, y, trees = 0, 0, 0
    while y != 322:
        x += right_val
        if x > 30:
            x -= 31
        y += down_val
        if map_list[y][x] == '#':
            trees += 1
    return trees

tree_counts = [treeSearch(1,1), treeSearch(3,1), treeSearch(5,1), treeSearch(7,1), treeSearch(1,2)]

result = 1
for count in tree_counts:
    result *= count

print(result)

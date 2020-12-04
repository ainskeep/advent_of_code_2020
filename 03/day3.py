import helpers

lines = helpers.read_input()

tree_map = []

for line in lines:
    tree_map.append([char for char in line])

map_width = len(tree_map[0])


def tree_on_slope(tree_map, rise, run):
    x, y = 0, 0
    tree_count = 0

    while y < len(tree_map) - 1:
        x += run
        y += rise
        if tree_map[y][x % map_width] == '#':
            tree_count += 1

    return tree_count
# part 1
tree_count = tree_on_slope(tree_map, 1, 3)

print(f"Part 1: {tree_count}")

# part 2
slopes = [
    [1, 1],
    [1, 3],
    [1, 5],
    [1, 7],
    [2, 1]
]

total = 1
for slope in slopes:
    total *= tree_on_slope(tree_map, slope[0], slope[1])

print(f"Part 2: {total}")
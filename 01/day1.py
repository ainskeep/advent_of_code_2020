IN_FILE = 'input.txt'


def read_input():
    input = []
    with open('input.txt', 'r') as infile:
        input = infile.read().splitlines()
    return input

def part_one(input):
    for i in input:
        for j in input:
            if int(i) + int(j) == 2020:

                return int(i), int(j)

def part_two(input):
    for i in input:
        for j in input:
            for k in input:
                if int(i) + int(j) + int(k) == 2020:

                    return int(i), int(j), int(k)

input = read_input()

# part 1
i, j = part_one(input)
print(f"Part 1:\n\t{i} * {j} = {i * j}")

# part 2
i, j, k = part_two(input)
print(f"Part 2:\n\t{i} * {j} * {k} = {i * j * k}")

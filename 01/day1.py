import helpers


def part_one(lines):
    for i in lines:
        for j in lines:
            if int(i) + int(j) == 2020:

                return int(i), int(j)


def part_two(lines):
    for i in lines:
        for j in lines:
            for k in lines:
                if int(i) + int(j) + int(k) == 2020:

                    return int(i), int(j), int(k)


lines = helpers.read_input()

# part 1
i, j = part_one(lines)
print(f"Part 1:\n\t{i} * {j} = {i * j}")

# part 2
i, j, k = part_two(lines)
print(f"Part 2:\n\t{i} * {j} * {k} = {i * j * k}")

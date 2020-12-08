import helpers

lines = helpers.read_input('input.txt')

grouped_lines = helpers.blank_line_group(lines)

def count_group_total(group):
    group_set = set()
    for person in group:
        for question in person:
            group_set.add(question)

    return len(group_set)

def count_all_yes_total(group):
    group_set_list = []
    for person in group:
        person_set = set()
        for question in person:
            person_set.add(question)
        group_set_list.append(person_set)

    return len(set.intersection(*group_set_list))

total = 0
for group in grouped_lines:
    total += count_group_total(group)

print(f"Part 1: {total}")

total = 0
for group in grouped_lines:
    total += count_all_yes_total(group)

print(f"Part 2: {total}")

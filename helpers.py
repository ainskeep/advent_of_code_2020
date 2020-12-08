IN_FILE = 'input.txt'


def read_input(file_name=IN_FILE):
    lines = []
    with open(file_name, 'r') as infile:
        lines = infile.read().splitlines()
    return lines


def blank_line_group(lines):
    grouped_lines = []

    tmp_group = []
    for line in lines:
        if line:
            tmp_group.append(line)
        else:
            grouped_lines.append(tmp_group)
            tmp_group = []

    # add the last group
    grouped_lines.append(tmp_group)

    return grouped_lines
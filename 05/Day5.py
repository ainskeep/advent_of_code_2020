import helpers
import re

MAX_ROWS = 128
MAX_COLUMNS = 8

lines = helpers.read_input('input.txt')

def decode_seat(seat_code):
    row_code = line[:-3]
    column_code = line[-3:]

    row_list = list(range(MAX_ROWS))
    column_list = list(range(MAX_COLUMNS))

    for c in row_code:
        half_idex = int(len(row_list)/2)
        if c == 'B':
            row_list = row_list[half_idex:]
        elif c == 'F':
            row_list = row_list[:half_idex]

    row_num = row_list[0]

    for c in column_code:
        half_idex = int(len(column_list)/2)
        if c == 'R':
            column_list = column_list[half_idex:]
        elif c == 'L':
            column_list = column_list[:half_idex]

    col_num = column_list[0]

    return row_num, col_num


seat_id_list = []
for line in lines:
    row, col = decode_seat(line)
    seat_id_list.append(row * 8 + col)

print(f"Part 1: {max(seat_id_list)} ")

i = 0
while True:
    if i-1 in seat_id_list and i+1 in seat_id_list and i not in seat_id_list:
        print(f"Part 2: Seat_id: {i}")
        break
    else:
        i += 1
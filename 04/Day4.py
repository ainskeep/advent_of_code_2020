import helpers
import re

lines = helpers.read_input('input.txt')

EXPECTED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def parse_passport_str(passport_str):
    passport_dict = {}
    passport_str = passport_str.strip()

    for keyVal in passport_str.split():
        key, val = keyVal.split(':')
        passport_dict[key] = val

    return passport_dict


def parse_input(lines):
    passport_str = ''
    passport_list = []

    for line in lines:
        if line == '':
            # end of passport
            passport_list.append(parse_passport_str(passport_str))
            passport_str = ''
        else:
            passport_str += line + ' '

    # need to parse the last passport
    passport_list.append(parse_passport_str(passport_str))

    return passport_list


def test_passport_part_1(passport):
    for key in EXPECTED_FIELDS:
        if key == 'cid':
            # ignore cid
            continue

        if key not in passport:
            return False

    return True


def test_passport_part_2(passport):
    for key in EXPECTED_FIELDS:
        if key == 'cid':
            # ignore cid
            continue

        if key not in passport:
            return False

        if key == 'byr':
            val = passport[key]
            val = int(val)
            if val < 1920 or val > 2002:
                return False

        if key == 'iyr':
            val = passport[key]
            val = int(val)
            if val < 2010 or val > 2020:
                return False

        if key == 'eyr':
            val = passport[key]
            val = int(val)
            if val < 2020 or val > 2030:
                return False

        if key == 'hgt':
            val = passport[key]

            if not re.match('\d+(cm|in)', val):
                return False

            num = val[:-2]
            unit = val[-2:]
            num = int(num)

            if unit == 'cm':
                if num < 150 or num > 193:
                    return False

            if unit == 'in':
                if num < 59 or num > 76:
                    return False

        if key == 'hcl':
            val = passport[key]
            if not re.match('^#[0-9a-f]{6}$', val):
               return False

        if key == 'ecl':
            val = passport[key]
            if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False

        if key == 'pid':
            val = passport[key]
            if not re.match('^[0-9]{9}$', val):
                return False

    return True


passport_list = parse_input(lines)
# PART 1
valid_passport_count = 0
for passport in passport_list:
    if test_passport_part_1(passport):
        valid_passport_count +=1

print(f"Part 1:\n\t{valid_passport_count}")

# PART 2
valid_passport_count = 0
for passport in passport_list:
    if test_passport_part_2(passport):
        valid_passport_count +=1

print(f"Part 2:\n\t{valid_passport_count}")

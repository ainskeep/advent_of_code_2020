import re

import helpers

lines = helpers.read_input()

exctract_range_regex = re.compile(r'^[0-9]+-[0-9]+')
exctract_policy_regex = re.compile(r' [a-zA-Z]+:')
exctract_password_regex = re.compile(r': .*')


def exctract_range(line):
    range_str = exctract_range_regex.search(line)
    low, high = range_str[0].split('-')
    return int(low), int(high)  # +1 so we are inclusive on the high

def exctract_policy(line):

    policy_str = exctract_policy_regex.search(line)
    policy_str = policy_str[0].strip()
    policy_str = policy_str.replace(':', '')
    return policy_str

def exctract_password(line):
    password_str = exctract_password_regex.search(line)
    password_str = password_str[0].strip()
    password_str = password_str.replace(':', '')
    return password_str

# part1
valid_count = 0
for line in lines:
    policy_range_low, policy_range_high = exctract_range(line)
    policy_range = range(policy_range_low, policy_range_high + 1 )

    policy = exctract_policy(line)

    password = exctract_password(line)

    if len(re.findall(policy, password)) in policy_range:
        valid_count +=1

print(f"Part 1:\n\t Valid password Count: {valid_count}")


# part2
valid_count = 0
for line in lines:
    policy_range_low, policy_range_high = exctract_range(line)
    policy = exctract_policy(line)

    password = exctract_password(line)

    if ( (password[policy_range_low] == policy) != (password[policy_range_high] == policy) ):
        valid_count +=1

print(f"Part 2:\n\t Valid password Count: {valid_count}")
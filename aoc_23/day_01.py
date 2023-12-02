from load_data import get_data
import re

day = "01"


def part_1(data) -> int:
    # split data into array
    data_split = data.split("\n")
    # initialising a 0 value
    running_total = 0
    # re string
    match_re = r"\d{1}"

    for line in data_split:
        integer_str = ""

        line_reverse = line[::-1]

        re_index = re.search(match_re, line)
        re_index_reverse = re.search(match_re, line_reverse)

        integer_str += line[re_index.start()]
        integer_str += line_reverse[re_index_reverse.start()]

        running_total += int(integer_str)

    return running_total

def part_2(data):
    num_str_to_value = {
        "ONE": "O1NE",
        "TWO": "T2WO",
        "THREE": "T3HREE",
        "FOUR": "F4OUR",
        "FIVE": "F5IVE",
        "SIX": "S6IX",
        "SEVEN": "S7EVEN",
        "EIGHT": "E8IGHT",
        "NINE": "N9INE",
    }

    # split data into array
    data_split = data.split("\n")
    # initialising a 0 value
    running_total = 0
    # re string
    match_re = r"\d{1}"

    # find and replace these values in line
    for line in data_split:

        integer_str = ""
        line_fix = str.upper(line)
        for k, v in num_str_to_value.items():
            line_fix = line_fix.replace(k, v)

        line_fix_reverse = line_fix[::-1]

        re_index = re.search(match_re, line_fix)
        re_index_reverse = re.search(match_re, line_fix_reverse)

        integer_str += line_fix[re_index.start()]
        integer_str += line_fix_reverse[re_index_reverse.start()]

        running_total += int(integer_str)

    return running_total

### Uncomment the lines below when your function passes the test!
raw_data = get_data(day)
print(f"part 1 solution = {part_1(raw_data)}")
print(f"part 2 solution = {part_2(raw_data)}")
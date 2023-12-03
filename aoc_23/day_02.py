from load_data import get_data

import re
from functools import reduce

day = "02"


def part_1(data) -> int:

    game_id_total = 0
    data_by_line = data.replace(";", ",").split("\n")

    limits = {"blue": 14, "red": 12, "green": 13}

    game_id_re = r"Game\s(\d{1,3}):.*"
    game_result_re = r"(\d*)\s(red|green|blue)"

    for line in data_by_line:
        impossible_result = False

        # capture the number after "Game "
        game_id = re.search(game_id_re, line)

        # strip the "Game ##: " from data
        line_scores = line[line.index(":") + 2 :]

        line_data = line_scores.split(", ")
        for result in line_data:
            re_match = re.search(game_result_re, result)
            if limits[re_match[2]] < int(re_match.group(1)):
                impossible_result = True

        if not impossible_result:
            game_id_total += int(game_id.group(1))

    return game_id_total


def part_2(data) -> int:

    game_power = 0

    data_by_line = data.replace(";", ",").split("\n")

    game_result_re = r"(\d*)\s(red|green|blue)"

    for line in data_by_line:
        colour_buckets = {"blue": [], "red": [], "green": []}

        greatest_collection = []
        line_power = 0

        # strip the "Game ##: " from data
        line_scores = line[line.index(":") + 2 :]

        line_data = line_scores.split(", ")
        for result in line_data:
            re_match = re.search(game_result_re, result)
            colour_buckets[re_match.group(2)].append(int(re_match.group(1)))

        for v in colour_buckets.values():
            greatest_collection.append(max(v))

        line_power = reduce(lambda x, y: x * y, greatest_collection)

        game_power += line_power

    return game_power


### Uncomment the lines below when your function passes the test!
raw_data = get_data(day)
print(f"part 1 solution = {part_1(raw_data)}")
print(f"part 2 solution = {part_2(raw_data)}")

def get_calibartion_value_sum(input_file: str):
    file = open(input_file, "r")
    sum = 0
    while line:= file.readline():
        first, last = get_first_last_digit(line)
        calibration_value = int(first + last)
        sum += calibration_value
    file.close()

    return sum


def get_first_last_digit(s: str):
    DIGIT_MAP = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    first_occ = len(s)
    last_occ = -1
    first_digit_str = None
    last_digit_str = None
    for digit_str in DIGIT_MAP:
        left_index = s.find(digit_str)
        right_index = s.rfind(digit_str)
        if (left_index > -1) and (left_index < first_occ):
            first_digit_str = digit_str
            first_occ = min(left_index, first_occ)
        if (right_index > -1) and (right_index > last_occ):
            last_occ = max(right_index, last_occ)
            last_digit_str = digit_str

    return DIGIT_MAP[first_digit_str], DIGIT_MAP[last_digit_str]


if __name__ == "__main__":
    from pathlib import Path
    input_file = Path(__file__) / "../input"
    result = get_calibartion_value_sum(input_file)
    print(result)



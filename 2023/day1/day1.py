import re 

digit_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
}

sample_input1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

sample_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

re_digit = '\d'

re_digit_or_word = f"(?=({'|'.join(digit_mapping.keys())}|\d))"

def map_to_int(chars):
    if len(chars) ==1 and chars[0].isdigit():
        return int(chars[0])
    else:
        return digit_mapping[chars]

def process(lines, pattern, debug = False):
    values = []
    lines = lines.split('\n')
    for line in lines:
        numbers = re.findall(pattern, line)
        val = 10*map_to_int(numbers[0]) + map_to_int(numbers[-1])
        values.append(val)

        if debug:
            print(line, numbers, val)

    print(values)
    print(len(values))
    total = sum(values)
    return total

if __name__ == '__main__':
    
    sample_output1 = process(sample_input1, re_digit)
    print(sample_output1)
    assert sample_output1 == 142

    with open('input.txt', 'r') as rfile:
        lines = rfile.read()

    # Part 1
    res1 = process(lines, re_digit)
    print(res1)
    # Result: 55002

    # Part 2

    sample_output2 = process(sample_input2, re_digit_or_word, debug=True)
    print(sample_output2)
    assert sample_output2 == 281

    res2 = process(lines, re_digit_or_word)
    print(res2)
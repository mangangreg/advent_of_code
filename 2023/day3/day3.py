def read_input(fpath):
    with open(fpath, 'r') as rfile:
        text = [list(row.strip()) for row in rfile.readlines()]
    return text

def get_symbols(rows):
    ''' Make a dict that maps co-ordinates to symbols'''
    symbols = {}
    for i,row in enumerate(rows):
        for j,char in enumerate(row):
            if not char=='.' and not char.isdigit():
                symbols[(i,j)] = char
    return symbols

def get_numbers(rows):
    ''' Make a dict that maps number ids to metadata about the number'''
    numbers = {}
    num_id = 0
    for i, row in enumerate(rows):
        found_no = False 
        num = ''
        num_start, num_end = 0,0

        for j, char in enumerate(row):
            if found_no and char.isdigit():
                num+=char
            elif char.isdigit():
                found_no = True 
                num_id += 1
                num += char
                num_start = j
            else:
                if found_no:
                    num_end = j-1
                    numbers[num_id] = {'id':num_id, 'num':int(num),'row_i':i, 'start_j':num_start, 'end_j':num_end}
                num = ''
                found_no = False

        if found_no:
            num_end = len(row)-1
            numbers[num_id] = {'id':num_id, 'num':int(num),'row_i':i, 'start_j':num_start, 'end_j':num_end}
    return numbers
            
def number_dict_fill(numbers):
    ''' Fill a dictionary that maps co-ordinates to number ids'''
    new_dict = {}
    for num in numbers.values():
        for ind in range(num['start_j'], num['end_j']+1):
            new_dict[(num['row_i'],ind)] = num['id']

    return new_dict

def check_for_valid_numbers(lookup_dict, symbols):
    valid_nums = set()
    valid_gears = []
    for (sym_i, sym_j), symbol in symbols.items():
        ids_for_this_symbol = set()

        for i in range(sym_i-1, sym_i+2):
            for j in range(sym_j-1, sym_j+2):
                num_id = lookup_dict.get((i,j), None)
                if num_id is not None:
                    valid_nums.add(num_id)
                    ids_for_this_symbol.add(num_id)
                
        if len(ids_for_this_symbol) == 2 and symbol=='*':
            valid_gears.append(ids_for_this_symbol)

    return valid_nums, valid_gears


def process_input(fpath):
    text = read_input(fpath)

    symbols = get_symbols(text)
    numbers = get_numbers(text)
    numbers_lookup = number_dict_fill(numbers)
    valid_num_ids, gear_ids = check_for_valid_numbers(numbers_lookup, symbols)

    answer_1 =  sum([numbers[num_id]['num'] for num_id in valid_num_ids] )
    answer_2 = sum([numbers[gear1_id]['num']*numbers[gear2_id]['num'] for gear1_id, gear2_id in gear_ids ])
    print(f"Answer_1: {answer_1}; Answer_2: {answer_2}")

    return answer_1, answer_2

def main():
    # answer_1, answer_2 = process_input('sample.txt')
    answer_1, answer_2 = process_input('input.txt')

if __name__ == '__main__':
    main()
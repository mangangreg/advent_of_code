def part1():
    new_elf = True
    max_elf_cals = -1
    current_elf_cals = -1

    with open('day1_input.txt', 'r') as rfile:
        for line in rfile:
            line = line.strip()
            if not len(line):
                new_elf = True
                max_elf_cals = max(max_elf_cals, current_elf_cals)
                continue 

            if new_elf:
                current_elf_cals = 0
                new_elf = False

            current_elf_cals += int(line)

    max_elf_cals = max(max_elf_cals, current_elf_cals)
    print(max_elf_cals)

def part2():
    new_elf = True
    all_elf_cals = []
    current_elf_cals = -1

    with open('day1_input.txt', 'r') as rfile:
        for line in rfile:
            line = line.strip()
            if not len(line):
                new_elf = True
                all_elf_cals.append(current_elf_cals)
                continue 

            if new_elf:
                current_elf_cals = 0
                new_elf = False

            current_elf_cals += int(line)

    all_elf_cals.append(current_elf_cals)

    ordered_cals = sorted(all_elf_cals, reverse=True)
    top_three = ordered_cals[:3]
    # print(top_three)
    
    total = sum(top_three)
    print(total)
                

if __name__ == '__main__':
    part1()
    part2()
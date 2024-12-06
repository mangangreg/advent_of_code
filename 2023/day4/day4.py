
def parse_file(fpath):
    results = []
    with open(fpath, 'r') as rfile:
        for ind, line in enumerate(rfile.readlines()):
            winning, mine = [num_block.split() for num_block in line.split(':')[-1].split('|')]
            results.append({
                'card': ind+1,
                'winning': set([int(x) for x in winning]),
                'mine': set([int(x) for x in mine])
            })
    return results

def part1_card_score(winning: set[int], mine:set[int]):

    number_of_matches = len( winning.intersection(mine))
    score = 2**(number_of_matches-1) if number_of_matches > 0 else 0
    
    return score

def part2_card_score(winning: set[int], mine:set[int]):

    return len( winning.intersection(mine))
    
def part2_algo(scores:dict):
    counts_of_cards = {card_id: 1 for card_id in scores.keys()}
    n = len(counts_of_cards)

    print(scores)

    for ind in range(1, n+1):
        
        multiplier = counts_of_cards[ind]
        winning_count = scores[ind]
        print(f"{ind=} {winning_count=} {counts_of_cards=}")
        for just_won in range(ind+1, ind+1+winning_count):
            if just_won <= n:
               counts_of_cards[just_won] += 1*multiplier

    return counts_of_cards

def part1(fpath):
    parsed = parse_file(fpath)
    
    scores = {card_results['card']: part1_card_score(winning=card_results['winning'], mine=card_results['mine']) for card_results in parsed}
    print(scores)
    result = sum(scores.values())
    return result

def part2(fpath):

    parsed = parse_file(fpath)
    scores = {card_results['card']: part2_card_score(winning=card_results['winning'], mine=card_results['mine']) for card_results in parsed}
    winning_cards = part2_algo(scores)
    result = sum(winning_cards.values())
    return result


def main():
    res1 = part1('sample.txt')
    print(res1)

    res1 = part1('input.txt')
    print(res1)

    res2 = part2('sample.txt')
    print(res2)

    res2 = part2('input.txt')
    print(res2)


if __name__ == '__main__':
    main()
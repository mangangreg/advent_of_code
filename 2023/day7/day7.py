from pathlib import Path
from collections import Counter
from dataclasses import dataclass
HERE = (Path.home()/'pdev/advent_of_code/2023/day7').resolve()

CARD_VALUE = { card:val for val,card in enumerate("23456789TJQKA", start=1)}

class Card:
    label: str
    value: int
    def __init__(self, label, wildcard=False):
        self.label = label
        self.value = 0 if wildcard and label=='J' else CARD_VALUE[label]

    def __str__(self) -> str:
        return self.label


class Hand:
    cards: list[Card]
    raw: str
    type: int
    bid: int
    value: int

    def __init__(self, hand_raw, bid, wildcard=False):
        self.raw = hand_raw
        self.cards = [Card(label, wildcard=wildcard) for label in hand_raw]
        self.type = self.get_type(wildcard=wildcard)
        self.bid = bid
        self.value = self.hand_value()

    def get_type(self, wildcard=False):
        # Get counts of each card and order by most common
        original_counts = Counter([card.label for card in self.cards])
        counter = Counter(original_counts)
        most_common_pairs = counter.most_common()

        if wildcard and 'J' in counter and len(counter)>1:

            most_common = most_common_pairs[0][0]
            second_most_common = most_common_pairs[1][0] if len(most_common_pairs)>1 else None
            if most_common == 'J' and second_most_common is not None:
                getting_the_bonus = second_most_common

            else:
                getting_the_bonus = most_common

            counter[getting_the_bonus] += counter['J']
            del counter['J'] 

        card_counts = counter.most_common()

        # Step through the various scenarios, assign arbitrary values
        if card_counts[0][1] == 5:
            return 7
        elif card_counts[0][1]==4:
            return 6
        elif card_counts[0][1]==3 and card_counts[1][1]==2:
            return 5
        elif card_counts[0][1]==3 and card_counts[1][1]==1:
            return 4
        elif card_counts[0][1]==2 and card_counts[1][1]==2:
            return 3
        elif card_counts[0][1]==2 and card_counts[1][1]==1:
            return 2
        elif card_counts[0][1]==1:
            return 1
        
    def hand_value(self):
        # Intialize value string with hand type
        val_str = f"{self.type}"
        # Add zero-padded values of cards
        for card in self.cards:
            val_str += f"{card.value:02d}"    
        return int(val_str)

    def beats(self, other_hand):
        if self.type > other_hand.type:
            return True
        elif self.type < other_hand.type: 
            return False
        else:
            for i in range(5):
                if self.cards[i].value > other_hand.cards[i].value:
                    return True
                elif self.cards[i].value < other_hand.cards[i].value:
                    return False
            return None
    
    def __repr__(self) -> str:
        cards = [str(card) for card in self.cards]
        return f'Hand({"".join(cards)}, value={self.value})'


def parse_input(fpath):
    rows = []
    with open(fpath, 'r') as f:
        for line in f:
            hand_raw, bid = line.strip().split()
            bid = int(bid)
            rows.append({"hand_raw": hand_raw, "bid": bid})
    return rows

# Solution functions
def part1(fpath, wildcard=False):
    parsed = parse_input(fpath)
    
    hands = [
        Hand(row["hand_raw"], row["bid"], wildcard=wildcard)
        for row in parsed
    ]

    # Sort by hand value
    hands.sort(key=lambda x:x.value)
    
    # Check that every hand beats the previous one
    assert all( hands[i+1].beats(hands[i]) for i in range(len(hands)-1))

    winnings = sum(rank*hand.bid for rank,hand in enumerate(hands,start=1))
    return winnings, hands

def part2(fpath):
    return part1(fpath, wildcard=True)

def main():
    winnings_1s, hands_1s = part1(HERE/'sample.txt')
    assert winnings_1s == 6440
    print(winnings_1s)

    winnings_1p, hands_1p = part1(HERE/'input.txt')
    assert len(hands_1p) == 1000
    print(winnings_1p)
    # assert res1 == 457535844

    winnings_2s, hands_2s = part2(HERE/'sample.txt')
    print(hands_2s)
    print(winnings_2s)
    assert winnings_2s == 5905

    winnings_2p, hands_2p = part2(HERE/'input.txt')
    print(winnings_2p)
    assert winnings_2p == 251515496


if __name__ == '__main__':
    main()

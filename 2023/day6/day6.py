from pathlib import Path
HERE = (Path.home()/'pdev/advent_of_code/2023/day6').resolve()
from dataclasses import dataclass

@dataclass
class Race:
    time: int
    distance_record: int

    def completed_distance(self, hold_time):
        """ How far a competitor travels in the given time if they hold button for `hold_time`"""
        return hold_time * (self.time - hold_time)
    
    def outcome(self, hold_time):
        completed_distance = self.completed_distance(hold_time)
        margin = completed_distance - self.distance_record
        win = margin>0
        return {
            "completed_distance": completed_distance,
            "margin": margin,
            "win": win
        }
    def race_possibilities(self):
        mappings = {
            hold_time: self.outcome(hold_time)
            for hold_time in range(0,self.time +1)
        }
        number_of_wins = sum([1 for x in mappings.values() if x["win"]])
        return mappings, number_of_wins

def parse_input(fpath, only_one = False):
    with open(fpath, 'r') as f:
        text = f.read().strip()
    time_line, distance_line = text.split('\n')
    times_digits = [int(x) for x in time_line.split(":")[-1].strip().split()]
    distances_digits = [int(x) for x in distance_line.split(":")[-1].strip().split()]
    
    times = [ int("".join([str(x) for x in times_digits]))] if only_one else times_digits
    distances = [ int("".join([str(x) for x in distances_digits]))] if only_one else distances_digits
    return [
        Race(time=times[ind], distance_record=distances[ind])
        for ind in range(len(times))
    ]


# Solution functions
def part1(fpath, only_one = False):
    parsed = parse_input(fpath, only_one=only_one)
    multiplier = 1
    for race in parsed:
        print(race)
        poss, number_of_wins = race.race_possibilities()
        multiplier *= number_of_wins
    return multiplier

def part2(fpath):
    return part1(fpath, only_one=True)

def main():
    # res1 = part1(HERE/'sample.txt')
    # assert res1 == 288
    # print(res1)

    # res1 = part1(HERE/'input.txt')
    # # assert res1 == 457535844
    # print(res1)

    res2 = part2(HERE/'sample.txt')
    print(res2)
    # assert res2 == 46

    res2 = part2(HERE/'input.txt')
    print(res2)
    # 41222968



if __name__ == '__main__':
    main()
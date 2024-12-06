from pathlib import Path
HERE = (Path.home() /'pdev/advent_of_code/2023/day5').resolve()
from dataclasses import dataclass

@dataclass
class MapRow:
    dest_range_start: int
    source_range_start: int
    range_length: int

def parse_input(fpath):
    with open(fpath, 'r') as f:
        lines = f.readlines()

    seeds = []
    multimap = {}
    types_list = ["seed"]
    for line in lines:
        line = line.strip()

        if "seeds:" in line:
            seeds = [int(x) for x in line.split(":")[-1].split()]

        elif "map:" in line:
            map_label = line.split()[0]
            source, _, dest = map_label.split('-')
            multimap[(source,dest)] = []
            types_list.append(dest)

        elif len(line):
            dest_range_start, source_range_start, range_length = [int(x) for x in line.split()]
            multimap[(source,dest)].append(
                MapRow(
                    dest_range_start = dest_range_start,
                    source_range_start = source_range_start,
                    range_length = range_length
                )
            )

    results = {
        "seeds": seeds,
        "maps": multimap,
        "types_list": types_list
    }
    return results

def read_single_map(map:list[MapRow], value:int) -> int:
    for row in map:
        diff = value - row.source_range_start
        if diff >= 0 and diff < row.range_length:
            return row.dest_range_start + diff
    return value


def read_multimap(multimap, source_type, dest_type, source_id, types_list):
    if (source_type, dest_type) in multimap:
        return read_single_map(multimap[(source_type, dest_type)], source_id)
    else:
        source_index_in_types_list = types_list.index(source_type)
        post_source_type = types_list[source_index_in_types_list+1]
        post_source_id = read_single_map(multimap[(source_type,post_source_type)], source_id)
        return read_multimap(multimap, post_source_type, dest_type, post_source_id, types_list)

def get_locations(seeds, multimap, types_list):
    """ Seeds should be a list of range objects"""
    locations = {}
    print(f"{seeds=}")
    for (seed_start, seed_length) in seeds:
        locations.update({
        seed_id: read_multimap(multimap, "seed", "location", seed_id, types_list)
        for seed_id in range(seed_start, seed_start+seed_length)
    })
    return locations

def extrapolate_seeds_part2(seeds):
    """ Process the pairs of (seed, seed_length) into a list of pairs of (seed_start, seed_end)"""
    seed_pairs = []
    for i in range(0,len(seeds),2):
        seed_pairs.append((seeds[i], seeds[i]+seeds[i+1]-1))
    return seed_pairs


def range_overlap(a,b, x,y):
    
    return (max(a,x), min(b,y)) if a <= y and b >= x else []

def range_non_overlap(a,b,x,y):
    "The parts of a,b that are not in x,y"
    non_overlap_pairs = []
    if a<x:
        non_overlap_pairs.append((a,x-1))
        if b>y:
            non_overlap_pairs.append((y+1,b))
    elif a>x:
        if a>y:
            non_overlap_pairs.append((a,b))
        elif b>y:
            non_overlap_pairs.append((y+1,b))
    return non_overlap_pairs


def mapped_onto(map, domain):
    """ Find the subset of the range that is actually mapped onto by the given domain"""

    mapped_onto = []
    for domain_start, domain_end in domain:
        this_domain_chunk_overlaps = []
        for row in map:
            overlap =  range_overlap(row.source_range_start, row.source_range_start+row.range_length, domain_start, domain_end)
            if len(overlap):
                this_domain_chunk_overlaps.append(overlap)
                overlap_offset = overlap[0] - row.source_range_start
                overlap_length = overlap[1] - overlap[0] 
                mapped_onto_start = row.dest_range_start + overlap_offset
                mapped_onto_end = mapped_onto_start + overlap_length
                mapped_onto.append(  (mapped_onto_start, mapped_onto_end) )
        
        # Check for non overlapping sections

        # If there is zero overlap that means the domain maps to "itself", so add that to the mapped_onto
        if len(this_domain_chunk_overlaps) == 0:
            mapped_onto.append( (domain_start, domain_end) )

        # Otherwise take the min and max of left and right index respectively across the list of pairs 
        else:
            min_left_ind = min([x[0] for x in this_domain_chunk_overlaps])
            max_right_ind = max([x[1] for x in this_domain_chunk_overlaps])
            if min_left_ind > domain_start:
                mapped_onto.append( (domain_start, min_left_ind-1) )
            if max_right_ind < domain_end:
                mapped_onto.append( (max_right_ind+1, domain_end) )
    return mapped_onto

def mapped_onto_multi(multimap, source_type_ind, types_list, seeds):
    """ Take the multimap and recursively apply it to find the range of values that are mapped onto by the given seeds"""
    source_type, target_type = types_list[source_type_ind], types_list[source_type_ind+1]
    if source_type_ind == 0:
        domain = seeds 
    else:
        domain = mapped_onto_multi(multimap, source_type_ind-1, types_list, seeds)

    return mapped_onto(multimap[(source_type,target_type)], domain)


# Solution functions
def part1(fpath):
    parsed = parse_input(fpath)
    seeds = [(x,1) for x in parsed['seeds']]
    locations = get_locations(seeds, parsed['maps'], parsed['types_list'])
    ans1 = min(locations.values())
    return ans1

def part2(fpath):
    parsed = parse_input(fpath)
    seeds = extrapolate_seeds_part2(parsed['seeds'])
    print(f"{seeds=}")

    # The initial source type index is the one just before locations
    source_type_index = len(parsed['types_list'])-2

    # Recursively find the range of values in locations that are mapped onto by seeds
    mapped_onto = mapped_onto_multi(parsed['maps'], source_type_index, parsed['types_list'], seeds)

    ans2 = min(x[0] for x in mapped_onto)
    return ans2

def main():
    # res1 = part1('sample.txt')
    # assert res1 == 35
    # print(res1)

    # res1 = part1('input.txt')
    # assert res1 == 457535844
    # print(res1)

    res2 = part2(HERE/'sample.txt')
    print(res2)
    assert res2 == 46

    res2 = part2(HERE/'input.txt')
    print(res2)
    # 41222968



if __name__ == '__main__':
    main()
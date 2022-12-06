INPUT = open('day6_input.txt').read().strip()

def all_different(arr):
    return len(arr) == len(set(arr))

def find_first_n_unique(arr, n):
    for ind in range(n, len(arr)):
        if all_different(arr[ind-n:ind]):
            return ind

res1 = find_first_n_unique(INPUT, 4)
print(res1)

res2 = find_first_n_unique(INPUT, 14)
print(res2)
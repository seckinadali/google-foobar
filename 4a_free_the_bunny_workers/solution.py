from itertools import combinations

def solution(num_buns, num_required):
    result = [[] for i in range(num_buns)]

    # Each key must be owned by num_buns - num_required + 1 bunnies;
    # we distribute keys to combinations of bunnies accordingly

    key_holders = num_buns - num_required + 1
    comb = combinations(range(num_buns), key_holders)

    key = 0
    for buns in comb:
        for i in buns:
            result[i].append(key)
        key += 1
    
    return result
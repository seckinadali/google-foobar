def solution(M, F):
    m, f = int(M), int(F)
    t = sorted([m, f])
    counter = 0

    while t[0] * t[1] > 1:
        if t[0] == 1:
            return str(counter + t[1] - 1)

        q, r = divmod(t[1], t[0])
        t = sorted([r, t[0]])
        counter += q
    
    if t == [1, 1]:
        return str(counter)
    return 'impossible'
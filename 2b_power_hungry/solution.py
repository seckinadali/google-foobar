def solution(xs):
    '''Given a list of integers, returns the largest possible product of a subset

    xs: list
    Returns: string
    '''
    if len(xs) == 1:
        return str(xs[0])

    pos, neg = [], []
    for i in xs:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
    
    if len(pos) == 0 and (len(neg) in [0, 1]):
        return str(0)
    
    if neg == []:
        t = pos
    elif len(neg) % 2 == 1:
        neg.remove(max(neg))
        t = pos + neg
    else:
        t = pos + neg
    
    res = t[0]
    for i in t[1:]:
        res *= i
    
    return str(res)
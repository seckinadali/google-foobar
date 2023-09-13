def xor_till(n):
    '''Returns the XOR product of integers from 1 to n
    '''
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

def xor_between(m, n):
    '''Returns the XOR product of integers from m to n
    '''
    return xor_till(m - 1) ^ xor_till(n)

def solution(start, length):
    A = []
    for i in range(length):
        first = start + i * length
        last = first + length - i - 1
        A.append(xor_between(first, last))
    
    res = 0
    for i in A:
        res = res ^ i
    
    return res
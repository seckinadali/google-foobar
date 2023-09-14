import math

def solution(n):
    n = int(n)
    count = 0

    while True:
        if n == 3:
            return count + 2

        check = math.log(n, 2)
        if check == int(check):
            return count + int(check)
        
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            if (n + 1) % 4 == 0:
                n = (n + 1) / 2
            else:
                n = (n - 1) / 2
            count += 2
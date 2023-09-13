def solution(n):
    result = []
    while n > 0:
        largest_square = int(n ** 0.5) ** 2
        result.append(largest_square)
        n -= largest_square
    return result
def hanoi(num, start, temp, end):
    if num == 1:
        return [[start, end]]
    return hanoi(num - 1, start, end, temp) + [[start, end]] + hanoi(num - 1, temp, start, end)

def solution(n):
    return hanoi(n, 1, 2, 3)
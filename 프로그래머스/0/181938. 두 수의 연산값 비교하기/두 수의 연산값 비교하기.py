def solution(a, b):
    answer = 0
    c = f'{a}{b}'
    d = 2 * a * b
    return max(int(c), d)
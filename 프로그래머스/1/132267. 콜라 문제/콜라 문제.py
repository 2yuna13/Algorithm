def solution(a, b, n):
    answer = 0
    
    while n >= a:
        n, mod = divmod(n, a)
        n = n * b
        answer += n
        n += mod
    
    return answer
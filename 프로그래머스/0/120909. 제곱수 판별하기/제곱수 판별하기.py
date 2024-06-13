def solution(n):
    for i in range(n):
        if i ** 2 == n:
            return 1
    
    return 2
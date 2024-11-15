def solution(n):
    answer = 0
    num = 1
    
    while answer < n:
        answer = num ** 2
        if answer == n:
            return (num + 1) ** 2
        num += 1
        
    return -1
def solution(n):
    answer = [True] * (n + 1)
    answer[0], answer[1] = False, False
    
    for i in range(2, n + 1):
        if answer[i]:
            for j in range(i * i, n + 1, i):
                answer[j] = False
    
    return sum(answer)
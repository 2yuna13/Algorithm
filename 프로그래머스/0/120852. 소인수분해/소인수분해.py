def solution(n):
    answer = []
    # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    # 2, 3, 
    for i in range(2, n + 1):
        # 2
        cnt = 0
        for j in range(2, i + 1):
            if i % j == 0:
                cnt += 1
        
        if cnt == 1:
            if n % i == 0:
                answer.append(i)
                
    return answer
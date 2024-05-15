def solution(num_list, n):
    m = len(num_list) // n
    answer = [[0] * n for _ in range(m)]
    
    k = 0
    
    for i in range(m):
        for j in range(n):
            answer[i][j] = num_list[k]
            k += 1
    
    return answer
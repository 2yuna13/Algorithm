def solution(rank, attendance):
    answer = []
    
    for i, v in enumerate(rank):
        if attendance[i] == True:
            answer.append((v, i))
            
    answer.sort()
    
    return 10000 * answer[0][1] + 100 * answer[1][1] + answer[2][1]
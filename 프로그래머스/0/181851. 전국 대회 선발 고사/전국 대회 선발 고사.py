def solution(rank, attendance):
    answer = []
    for i, p  in zip(rank, attendance):
        if p == True:
            answer.append(i)
            
    answer.sort()
    
    a = rank.index(answer[0])
    b = rank.index(answer[1])
    c = rank.index(answer[2])
    
    return 10000 * a + 100 * b + c
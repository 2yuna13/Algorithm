def solution(a, d, included):
    answer = 0
    length = len(included)
    seq = [(a + d * i) for i in range(length)]
    
    for j in range(length):
        if included[j]:
            answer += seq[j]
    
    return answer
def solution(numLog):
    answer = ''
    c = {1 : "w", -1 : "s", 10 : "d", -10: "a"}
    
    for i in range(len(numLog) - 1):
        answer += c[numLog[i + 1] - numLog[i]]
    
    return answer
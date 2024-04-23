def solution(arr, k):
    answer = []
    
    for i in arr:
        if i not in answer:
            answer.append(i)
        
        if len(answer) == k:
            return answer
    
    while len(answer) < k:
        answer.append(-1)
    
    return answer
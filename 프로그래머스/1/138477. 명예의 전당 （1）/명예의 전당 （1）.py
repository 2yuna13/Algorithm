def solution(k, score):
    answer = []
    temp = []
    
    for num in score:
        temp.append(num)
        temp.sort(reverse=True)
        
        if len(temp) > k:
            temp.pop()
        
        answer.append(min(temp))
        
        
    return answer
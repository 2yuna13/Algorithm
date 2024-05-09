def solution(emergency):
    answer = []
    dic = {}
    
    sort_emergency = sorted(emergency, reverse = True)
    
    for i, v in enumerate(sort_emergency):
        dic[v] = i + 1
        
    for i in emergency:
        answer.append(dic[i])
        
    return answer
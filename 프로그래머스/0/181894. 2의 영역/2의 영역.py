def solution(arr):
    answer = []
    for i, v in enumerate(arr):
        if v == 2:
            answer.append(i)
    
    if not answer:
        return [-1]
    else:
        return arr[answer[0] : answer[-1] + 1]
            
    return answer
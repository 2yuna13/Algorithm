def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        temp = []
        for i in arr[s : e + 1]:
            if i > k:
                temp.append(i)
        
        answer.append(-1 if not temp else min(temp))
            
    return answer
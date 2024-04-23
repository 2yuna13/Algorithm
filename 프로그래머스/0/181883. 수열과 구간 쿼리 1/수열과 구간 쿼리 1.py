def solution(arr, queries):    
    for s, e in queries:
        i = list(range(s, e + 1))
        for j in i:
            arr[j] += 1
        
    return arr
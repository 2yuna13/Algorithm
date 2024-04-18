def solution(arr, queries):    
    for n, m in queries:
        arr[n], arr[m] = arr[m], arr[n]
    
    return arr
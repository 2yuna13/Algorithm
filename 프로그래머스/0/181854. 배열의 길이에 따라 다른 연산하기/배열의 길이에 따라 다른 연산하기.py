def solution(arr, n):
    answer = []
    length = len(arr)
    
    if length % 2:
        for i, v in enumerate(arr):
            if not i % 2:
                arr[i] = v + n
            
    else:
         for i, v in enumerate(arr):
            if i % 2:
                arr[i] = v + n
    
    return arr
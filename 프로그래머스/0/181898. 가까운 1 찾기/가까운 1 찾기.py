def solution(arr, idx):
    answer = -1
    
    for i, v in enumerate(arr):
        if i + 1 > idx and v == 1:
            return i  
        
    return answer
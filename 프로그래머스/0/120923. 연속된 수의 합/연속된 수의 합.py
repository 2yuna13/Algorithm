def solution(num, total):
    
    mid = total // num
    start = mid - ((num - 1) // 2)
        
    return [start + i for i in range(num)]
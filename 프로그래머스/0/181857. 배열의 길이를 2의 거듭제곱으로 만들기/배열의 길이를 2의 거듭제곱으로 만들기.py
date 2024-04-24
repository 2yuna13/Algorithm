def solution(arr):
    cnt = 0
    l = len(arr)
    
    while l > 1:
        l /= 2
        cnt += 1
    
    return arr + [0] * (2 ** cnt - len(arr))
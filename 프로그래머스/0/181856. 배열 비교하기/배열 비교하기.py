def solution(arr1, arr2):
    answer = 0
    len1 = len(arr1)
    len2 = len(arr2)
    
    if len1 == len2:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
    else:
        if len1 > len2:
            return 1
        else:
            return -1
            
    return answer
def solution(n, lost, reserve):
    # 교집합 제외
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    
    return n - len(lost_set)
def solution(nums):
    n = int(len(nums) / 2)
    n_set = set(nums)
    
    if n < len(n_set):
        return n
    else:
        return len(n_set)
    
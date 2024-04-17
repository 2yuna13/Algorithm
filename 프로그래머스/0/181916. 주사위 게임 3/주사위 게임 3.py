def solution(a, b, c, d):    
    nums = [a, b, c, d]
    # 각 숫자가 리스트에 몇개 있는지 확인
    counts = [nums.count(i) for i in nums]
    
    # 네 주사위에서 나온 숫자가 모두 같을 때
    if max(counts) == 4:
        return 1111 * a
    # 세 주사위에서 나온 숫자가 같을 때
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        # 두 개씩 같은 값
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        # 두 주사위 같고, 나머지 각각 다를 때
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p ** 2
    else:
        return min(nums)
            
            
    
        
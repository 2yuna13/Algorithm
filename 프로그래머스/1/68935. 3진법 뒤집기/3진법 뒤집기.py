# n -> 100,000,000 이하 / n, logn
  
def solution(n):
    answer = 0
    
    # 3진법 변환
    nums = []
    while n:
        nums.append(n % 3)
        n //= 3
    
    # 뒤집고 10진법으로 표현
    for i, v in enumerate(nums[::-1]):
        answer += v * (3 ** i)
    
    # nums.reverse()
    # for i in range(len(nums)):
    #     answer += nums[i] * (3 ** i)
    
    return answer
# n -> 100,000,000 이하 / n, logn

# 3진법으로 변환 
# 3진법 뒤집기 
# 10진법으로 표현 (변환한거 이용하기..?)

# 진법 변환         
def solution(n):
    answer = 0
    
    if n == 0:
        return 0
    
    nums = []
    while n:
        remainder = n % 3
        n //= 3
        nums.append(remainder)
        
    for i, v in enumerate(nums[::-1]):
        if i == 0:
            answer += v
        else:
            answer += v * (3 ** i)
    
    return answer
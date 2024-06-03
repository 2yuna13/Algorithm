from itertools import permutations

# 소수찾기
def prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    per_num = set()
    
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(numbers, i))
        per_num.update(int(''.join(j)) for j in temp)
    
    for num in per_num:
        if prime(num):
            answer += 1
            
    return answer
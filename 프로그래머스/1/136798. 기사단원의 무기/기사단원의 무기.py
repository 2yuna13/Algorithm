def solution(number, limit, power):
    divisor = []
    
    # 1. 약수 구하기
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 1
                if j != i//j:
                    cnt += 1
        divisor.append(cnt)
        
    # 2. limit 확인
    for i, v in enumerate(divisor):
        if v > limit:
            divisor[i] = power
    
    return sum(divisor)
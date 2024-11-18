def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        # 제곱수 -> 약수의 개수 홀수
        if int(i**0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
                
    return answer
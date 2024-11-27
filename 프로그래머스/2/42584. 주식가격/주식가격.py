def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        # 현재 숫자가 마지막 가격보다 작을 때 -> 초 기록
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
              
        stack.append(i)
    
    for idx in stack:
        answer[idx] = len(prices) - idx - 1
    
    return answer
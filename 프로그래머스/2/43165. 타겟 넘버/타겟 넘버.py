from collections import deque

def solution(numbers, target):
    answer = 0
    # 시작 지점 => 현재까지 합, 인덱스
    q = deque([(numbers[0], 0), (-numbers[0], 0)])
    
    while q:
        current_sum, idx = q.popleft()
        idx += 1
        
        if idx < len(numbers):
            q.append((current_sum + numbers[idx], idx))
            q.append((current_sum - numbers[idx], idx))
        else:
            if current_sum == target:
                answer += 1    
    
    return answer
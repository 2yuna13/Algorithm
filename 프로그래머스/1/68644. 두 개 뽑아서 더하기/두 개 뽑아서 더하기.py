def solution(numbers):
    answer = []
    
    for i, v1 in enumerate(numbers):
        for j, v2 in enumerate(numbers[i + 1:]):
            v = v1 + v2
            if v not in answer:
                answer.append(v)          
    
    return sorted(answer)
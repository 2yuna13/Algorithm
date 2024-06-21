def solution(lines):
    answer = 0
    count = [set([]) for _ in range(200)]
    
    for index, value in enumerate(lines):
        a, b = value
        for i in range(a, b):
            count[i + 100].add(index)
            
    for line in count:
        if len(line) > 1:
            answer += 1
    
    return answer
def solution(sides):
    answer = 0
    
    sides.sort()
    a, b = sides
    
    #b가 가장 긴 변의 길이일 경우
    for i in range(b - a + 1, b + 1):
        answer += 1
        
    #나머지 한 변이 가장 긴 변일 경우
    for i in range(b + 1, a + b):
        answer += 1   
    
    return answer
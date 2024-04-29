def solution(hp):
    ants = [5, 3, 1]
    answer = 0
    
    
    for ant in ants:
        answer += hp // ant
        hp %= ant
    
    return answer
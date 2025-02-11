from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    #모든 던전 탐색
    for dungeon in permutations(dungeons):
        fatigue = k
        cnt = 0
        
        for minimum, consume in dungeon:
            if fatigue >= minimum:
                fatigue -= consume
                cnt += 1
            else:
                break
    
        answer = max(answer, cnt)
            
    return answer
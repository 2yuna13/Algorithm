def solution(N, stages):
    answer = []
    stage_count = [0] * (N + 2)
    
    # 각 스테이지에 머무르고 있는 사람
    for stage in stages:
        stage_count[stage] += 1
    
    failure_rates = []
    remaining_players = len(stages) # 전체 도전자 수
    
    for i in range(1, N + 1):
        current_players = stage_count[i] # 현재 스테이지 머무르고 있는 사람 수 
        
        if remaining_players > 0:
            failure_rate = current_players / remaining_players
        else:
            failure_rate = 0
        
        failure_rates.append((failure_rate, i))
        remaining_players -= current_players # 남은 도전자 수 업데이트
    
    failure_rates.sort(key=lambda x: (-x[0], x[1]))
    for failure_rate in failure_rates:
        answer.append(failure_rate[1])
    
    return answer
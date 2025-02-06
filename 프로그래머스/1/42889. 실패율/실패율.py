def solution(N, stages):
    answer = []
    stage_count = [0] * (N + 2)
    failure_rates = []
    
    for stage in stages:
        stage_count[stage] += 1
    
    for i in range(N):
        current_players = stage_count[i + 1]
        remaining_players = sum(stage_count[i + 1:])
        
        if current_players > 0:
            failure_rates.append((current_players / remaining_players, i + 1))
        else:
            failure_rates.append((0, i + 1))
    
    failure_rates.sort(key=lambda x: (-x[0], x[1]))
    for failure_rate in failure_rates:
        answer.append(failure_rate[1])
    
    return answer
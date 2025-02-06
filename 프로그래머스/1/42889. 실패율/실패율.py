def solution(N, stages):
    answer = []
    stage_count = []
    
    for i in range(1, N + 2):
        stage_count.append(stages.count(i))
    
    failure_rates = []
    for j in range(N):
        if stage_count[j] > 0:
            failure_rate = stage_count[j] / sum(stage_count[j:])
            answer.append((failure_rate, j + 1))
        else:
            answer.append((0, j + 1))
    
    answer.sort(key=lambda x: (-x[0], x[1]))
    
    return [stage for failure_rate, stage in answer]
def solution(score):
    answer = []
    avg_score = []
    for i in score:
        avg_score.append(sum(i) / 2)
    
    # 평균 점수 정렬
    sort_score = sorted(avg_score, reverse=True)

    for j in avg_score:
        answer.append(sort_score.index(j) + 1)
    
    return answer
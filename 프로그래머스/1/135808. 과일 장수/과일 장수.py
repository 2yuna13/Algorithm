def solution(k, m, score):
    answer = 0
    box = []
    score.sort(reverse=True)
    for i in range(len(score)//m):
        box = score[i * m : m * (i + 1)]
        answer += min(box) * m
    return answer
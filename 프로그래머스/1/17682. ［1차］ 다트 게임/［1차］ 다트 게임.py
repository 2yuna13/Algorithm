def solution(dartResult):
    score = []
    num = ''
    
    for i in dartResult:
        # S, D(**2), T(***3)
        if i == 'S':
            score.append(int(num))
            num = ''
        elif i == 'D':
            score.append(int(num) ** 2)
            num = ''
        elif i == 'T':
            score.append(int(num) ** 3)
            num = ''
        # * => 현재, 직전 점수 * 2 / # => 현재 점수 마이너스
        elif i == '*':
            if len(score) == 1:
                score[0] *= 2
            else:
                score[-1] *= 2
                score[-2] *= 2
        elif i == '#':
            score[-1] *= -1
        else:
            num += i
        
    return sum(score)
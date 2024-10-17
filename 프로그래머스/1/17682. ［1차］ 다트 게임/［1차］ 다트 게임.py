def solution(dartResult):
    score = 0
    answer = []
    dartResult = dartResult.replace("10", "t")
    
    for i in dartResult:
        # 점수인지 확인
        if i.isnumeric():
            score += int(i)
            continue
        # 10점
        elif i == 't': 
            score += 10
            continue
        # S, D(**2), T(***3)
        elif i == 'S':
            answer.append(score)
        elif i == 'D':
            answer.append(score ** 2)
        elif i == 'T':
            answer.append(score ** 3)
        # * => 계산식에서 * 2 / # => 점수 마이너스
        elif i == '*':
            # 한 판
            if len(answer) == 1:
                answer[0] *= 2
            # 두 판
            else:
                answer[-1] *= 2
                answer[-2] *= 2
        elif i == '#':
            answer[-1] *= -1
            
        #점수 초기화
        score = 0
        
    return sum(answer)
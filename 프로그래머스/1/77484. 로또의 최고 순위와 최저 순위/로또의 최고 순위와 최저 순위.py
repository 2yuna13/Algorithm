def solution(lottos, win_nums):
    answer = []
    cnt = 0
    cnt_zero = 0
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
        if i == 0:
            cnt_zero += 1
    
    #최고 순위
    answer.append(min(7 - (cnt + cnt_zero), 6))
    #최저 순위
    answer.append(min(7 - cnt, 6))
    
    return answer
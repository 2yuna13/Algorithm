def solution(s):
    answer = 0
    cnt_x, cnt_notx = 0, 0
    x = ""
    
    for i in s:
        if cnt_x == cnt_notx:
            x = i
            cnt_x += 1
            answer += 1
        elif x == i:
            cnt_x += 1
        else:
            cnt_notx += 1
        
    return answer
def solution(s):
    answer = 0
    cnt_x, cnt_notx = 0, 0
    x = s[0]
    
    for i in range(len(s)):
        if s[i] == x:
            cnt_x += 1
        else:
            cnt_notx += 1
            
        if cnt_x == cnt_notx:
            answer += 1
            cnt_x, cnt_notx = 0, 0
            if i + 1 < len(s):
                x = s[i+1]
    
    if cnt_x != 0 or cnt_notx != 0:
        answer += 1
        
    return answer
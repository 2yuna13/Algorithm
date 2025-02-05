def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    mcount, hcount = 0, 0
    t1 = h1 * 60 * 60 + m1 * 60 + s1
    t2 = h2 * 60 * 60 + m2 * 60 + s2
    
    #시작이 0, 12시인 경우
    if t1 == 0 or t1 == 60 * 60 * 12:
        answer += 1
        
    for i in range(t1, t2):
        s = (i * 6) % 360
        m = (i / 10) % 360
        h = (i / 120) % 360
        
        ns = 360 if ((i + 1) * 6) % 360 == 0 else ((i + 1) * 6) % 360
        nm = 360 if ((i + 1) / 10) % 360 == 0 else ((i + 1) / 10) % 360
        nh = 360 if ((i + 1) / 120) % 360 == 0 else ((i + 1) / 120) % 360
        
        if s < m and ns >= nm:
            mcount += 1
        if s < h and ns >= nh:
            hcount += 1
        # 0, 12시 인 경우 -1
        if ns == nm == nh:
            answer -= 1
        
    answer += (mcount + hcount)
        
    return answer
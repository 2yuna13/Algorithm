# 모든 0 제거
# x의 길이를 2진법으로 표현

def solution(s):    
    cnt_1 = 0
    cnt_2 = 0
    
    while s != '1':
        x = ''
        for i in s:
            if i == '0':
                cnt_2 += 1
                continue
            x += i

        s = bin(len(x))[2:]
        cnt_1 += 1
        
    return [cnt_1, cnt_2]
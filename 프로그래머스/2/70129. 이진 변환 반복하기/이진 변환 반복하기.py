# 모든 0 제거
# x의 길이를 2진법으로 표현

def solution(s):    
    cnt_1 = 0
    cnt_2 = 0
    
    while s != '1':
        cnt_1 += 1
        x = s.count('1')
        cnt_2 += len(s) - x
        s = bin(x)[2:]
        
    return [cnt_1, cnt_2]
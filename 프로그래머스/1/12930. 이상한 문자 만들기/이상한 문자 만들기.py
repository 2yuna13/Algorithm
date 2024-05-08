def solution(s):
    answer = ''
    cnt = 0
    
    for i in s:
        if cnt % 2:
            answer += i.lower()
            cnt += 1
        elif i == " ":
            answer += " "
            cnt = 0
        else:
            answer += i.upper()
            cnt += 1
    
    return answer
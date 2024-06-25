def solution(my_string):
    answer = 0
    num = ''
    for i in my_string:
        if i.isdigit():
            num += i
        else:
            num += ' '
            
    for j in num.split(' '):
        if j.isdigit():
            answer += int(j)
    
    return answer
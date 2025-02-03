def solution(s):
    answer = []
    
    temp = []
    for i in s:
        temp.append(ord(i))
        
    for j in temp:
        answer.append(chr(j))
        
    answer.sort(reverse = True)
        
    return ''.join(answer)
def solution(my_string):
    answer = []
    
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, '')
    
    for j in my_string:
        answer.append(int(j))
        
    answer.sort()
    
    return answer
def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    
    for i, v in enumerate(my_string):
        if v == "+":
            answer += int(my_string[i + 1])
        elif v == "-":
            answer -= int(my_string[i + 1])
    
    return answer
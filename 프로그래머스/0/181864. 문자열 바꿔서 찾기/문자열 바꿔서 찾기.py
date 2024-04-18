def solution(myString, pat):
    answer = ''
    for str in myString:
        if str == "A":
            answer += "B"
        else:
            answer += "A"
    
    return 1 if pat in answer else 0
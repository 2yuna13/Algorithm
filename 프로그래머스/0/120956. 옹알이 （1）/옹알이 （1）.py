def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for babble in lst:
            word = word.replace(babble, " ")
        
        if word.strip() == "":
            answer += 1      
        
    return answer
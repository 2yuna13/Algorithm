import re

def solution(babbling):
    answer = 0
    
    pattern = re.compile('^(aya|ye|woo|ma)+$')
    
    for word in babbling:
        if pattern.match(word):
            answer += 1
        
    return answer
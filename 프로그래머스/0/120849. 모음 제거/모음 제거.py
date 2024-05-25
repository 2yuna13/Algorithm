def solution(my_string):
    answer = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    for i in my_string:
        if i in vowel:
            continue
        answer += i    
    
    return answer
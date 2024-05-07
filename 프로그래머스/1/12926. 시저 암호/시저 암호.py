def solution(s, n):
    answer = ''
    for i in s:
        if i.islower():
            answer += chr((ord(i) + n - ord('a')) % 26 + ord('a'))
        elif i.isupper():
            answer += chr((ord(i) + n - ord('A')) % 26 + ord('A'))
        else:
            answer += " "
            
    return answer
def solution(s):
    s = [int(i) for i in s.split(" ")]
    s.sort()
    
    return str(s[0]) + " " + str(s[-1])
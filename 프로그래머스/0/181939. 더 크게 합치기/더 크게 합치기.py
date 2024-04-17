def solution(a, b):
    c = str(a) + str(b)
    d = str(b) + str(a)
    
    return max(int(c), int(d))
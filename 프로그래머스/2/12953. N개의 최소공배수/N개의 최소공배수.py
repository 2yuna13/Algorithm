import math

def lmc(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    answer = arr[0]
    
    for i in arr:
        answer = lmc(answer, i)
        
    return answer
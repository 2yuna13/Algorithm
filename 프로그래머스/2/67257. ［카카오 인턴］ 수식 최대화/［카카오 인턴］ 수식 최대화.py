# 숫자, 연산자 분리
# 연산자 우선순위 정하기 => 순열 사용
# 우선순위 기반 계산
# 결과 중 가장 큰 숫자 반환
import re
from itertools import permutations

def calc(tokens):
    num1, exp, num2 = tokens
    if exp == '*':
        return int(num1) * int(num2)
    elif exp == '+':
        return int(num1) + int(num2)
    else:
        return int(num1) - int(num2)
            
def solution(expression):
    answer = []
    operators = ['-', '*', '+']
    
    for operator in permutations(operators):
        temp = re.split("([-*+])", expression)
        for exp in operator:
            while exp in temp:
                idx = temp.index(exp)
                temp[idx-1] = str(calc(temp[idx-1:idx+2]))
                temp[idx] = temp[idx + 1] = ''
                temp = [i for i in temp if i]
        answer.append(abs(int(temp[0])))
        
    return max(answer)
# 숫자, 연산자 분리
# 연산자 우선순위 정하기 => 순열 사용
# 우선순위 기반 계산
# 결과 중 가장 큰 숫자 반환
import re
from itertools import permutations

def toPostFix(tokens, priority):
    stack = [] # 연산자 스택
    postfix = [] # 출력 배열(문자열)
    
    for token in tokens:
        if token.isdigit(): postfix.append(token) # 숫자는 바로 추가
        else:
            if not stack: stack.append(token)
            else:
                while stack:
                    if priority[token] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else: break
                        
                stack.append(token)
                
    while stack:
        postfix.append(stack.pop())

    return postfix

def calc(tokens):
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue
        
        num1 = stack.pop()
        num2 = stack.pop()
        
        if token == '*':
            stack.append(num2 * num1)
        elif token == '+':
            stack.append(num2 + num1)
        else:
            stack.append(num2 - num1)
            
    return stack.pop()
            
def solution(expression):
    answer = 0
    
    # 숫자, 연산자 분리
    tokens = re.split("([-*+])", expression)
    operators = ['-', '*', '+']
    
    # 연산자 우선순위 -> {'-': 0, '*': 1, '+': 2}, ..., {'+': 0, '*': 1, '-': 2}
    for i in map(list, permutations(operators)):
        priority = {o:p for p, o in enumerate(list(i))}
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))
        
    return answer
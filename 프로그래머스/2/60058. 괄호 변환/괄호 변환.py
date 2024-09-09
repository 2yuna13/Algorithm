#2. 균형잡힌 괄호 문자열 u, v 분리
def balanced_index(p):
    cnt = 0 #왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        #균형잡힌 문자열
        if cnt == 0:
            return i

#올바른 괄호 문자열 확인
def check_proper(p):
    cnt = 0 #왼쪽 괄호 개수
    for i in p:
        if i == '(':
            cnt += 1
        else:
            #짝이 맞지 않는 경우
            if  cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    answer = ''
    #1. 입력이 빈 문자열인 경우
    if p == '':
        return answer
    
    idx = balanced_index(p)
    u = p[:idx + 1]
    v = p[idx + 1:]
    
    #3. 올바른 괄호 문자열인 경우 v에 대해 다시 수행한 결과 붙인 후 반환
    if check_proper(u):
        answer = u + solution(v)
    #4. 올바른 괄호 문자열이 아닌 경우
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) #첫 번째와 마지막 문자 제거
        #괄호 방향 뒤집어서 붙이기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
        
    return answer
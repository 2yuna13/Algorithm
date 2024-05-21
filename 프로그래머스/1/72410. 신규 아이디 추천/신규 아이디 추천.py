import re

def solution(new_id):
    answer = []
    change = ""
    # 가능한 요소
    check = ["-", "_", "."]
    # 연속된 마침표 세기
    dot_count = 0
    
    for i in range(len(new_id)):
        # 1. 모든 대문자를 소문자로 치환한다.
        l = new_id[i].lower()
        # 2. 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
        if not l.isalnum() and l not in check:
            continue
        answer.append(l)
        
    changed = ''.join(answer)
    #3단계
    while ".." in changed:
        changed = changed.replace('..','.')
    
    # 4. 마침표가 처음이나 끝에 위치한다면 제거합니다.
    changed = changed.strip('.')
        
    # 5. 빈 문자열이라면, "a"대입
    if len(changed) == 0:
        changed += "a"
    
    # 6. 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    changed = changed[:15].strip('.')
    
    # 7. 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해 붙인다.
    while len(changed) < 3:
        changed += changed[-1]
        
    return changed
import re

def solution(new_id):
    # 소문자 치환
    answer = new_id.lower()
    # 문자, 숫자, -, _, . 제외 모두 제거
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    # ..... -> . 치환
    answer = re.sub('\.{2,}', '.', answer)
    # . 처음이나 끝 제거
    answer = answer.strip('.')
    # 빈 문자열이면 -> a
    if len(answer) == 0:
        answer = 'a'
    # 길이가 16 이상이면 15개까지만, 끝에 . 제거
    answer = answer[:15].strip('.')
    # 길이가 2 이하라면 마지막 문자를 3이 될때까지 반복
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer
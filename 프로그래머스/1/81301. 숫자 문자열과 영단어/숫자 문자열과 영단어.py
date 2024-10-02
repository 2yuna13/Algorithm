def solution(s):
    # 딕셔너리 선언 (영단어 -> 숫자)
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    answer = ''
    temp = ''
    
    for i in s:
        #숫자인 경우
        if i.isdigit():
            answer += i
        #문자인 경우
        else:
            temp += i
            #영단어에 해당하면 숫자로 변경
            if temp in dic:
                answer += dic[temp]
                temp = ''
            
    return int(answer)
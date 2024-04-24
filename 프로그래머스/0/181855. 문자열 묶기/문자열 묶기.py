def solution(strArr):
    answer = 0
    len_dic = {}
    
    for i in strArr:
        l = len(i)
        if l not in len_dic:
            len_dic[l] = 0
        len_dic[l] += 1
    
    for cnt in len_dic.values():
        if cnt > answer:
            answer = cnt    
    
    return answer
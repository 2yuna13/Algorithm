def solution(s):
    answer = []
    s = s.strip("{}")
    s_list = s.split("},{")
    s_list = sorted(s_list, key=lambda x: len(x))
    
    for i in s_list:
        i = list(map(int, i.split(",")))
        for j in i:
            if j not in answer:
                answer.append(j)
            
    return answer
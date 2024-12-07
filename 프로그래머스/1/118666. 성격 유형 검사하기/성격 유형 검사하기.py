def solution(survey, choices):
    answer = ''
    types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for s, c in zip(survey, choices):
        if c <= 3:
            types[s[0]] += 4 - c
        elif c >= 5:
            types[s[1]] += c - 4
    
    type_list = list(types.items())
    for i in range(0, 8, 2):
        if type_list[i][1] >= type_list[i + 1][1]:
            answer += type_list[i][0]
        else:
            answer += type_list[i + 1][0]
                    
    return answer
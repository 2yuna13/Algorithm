def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for name, type in clothes:
        clothes_dict[type] = clothes_dict.get(type, 0) + 1
    
    for i in clothes_dict.values():
        answer *= (i + 1)
    
    return answer - 1
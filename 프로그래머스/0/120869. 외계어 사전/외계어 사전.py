def solution(spell, dic):
    for i in dic:
        if set(i) == set(spell):
            return 1
    
    return 2
# A(1), AA, AAA, AAAA, AAAAA
# AAAAE(6), AAAAI, ..., AAAAU
# AAAE(10), ..., AAAUU(30)
# AAE(31), ...
# E(782) ..?
# I(1563)

def solution(word):
    preset = {
        'A' : [1, 1, 1, 1, 1],
        'E' : [782, 157, 32, 7, 2],
        'I' : [1563, 313, 63, 13, 3],
        'O' : [2344, 469, 94, 19, 4],
        'U' : [3125, 625, 125, 25, 5],
    }
    
    answer = 0
    for i, v in enumerate(word):
        answer += preset[v][i]    
    
    return answer
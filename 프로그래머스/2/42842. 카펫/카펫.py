# 가로 > 세로
# brown = (yellow 가로 * 2) + (yellow 세로 * 2) + 4

def solution(brown, yellow):    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            width = yellow // i
            height = i
            if brown == (width * 2) + (height * 2) + 4:
                return [width + 2, height + 2]



# 두 점의 기울기 = 나머지 두 점의 기울기

def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    def slope(x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)
    
    if slope(x1, y1, x2, y2) == slope(x3, y3, x4, y4):
        return 1
    if slope(x1, y1, x3, y3) == slope(x2, y2, x4, y4):
        return 1
    if slope(x1, y1, x4, y4) == slope(x2, y2, x3, y3):
        return 1
    
    return 0
def solution(dots):
    dots.sort()
    length = dots[1][1] - dots[0][1]
    width = dots[2][0] - dots[0][0]
    return abs(width) * abs(length)
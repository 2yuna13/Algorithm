def solution(line):
    # 1. 교점 구하기
    # x 좌표 = BF - ED / AD - BC
    # y 좌표 = EC - AF / AD - BC
    # AD - BC = 0, 평행 또는 일치
    # 2. 구한 교점 정수 확인
    # 3. 가로, 세로 범위 구해서 별찍기 (x, y 좌표 최대, 최소 이용하면 될듯?)
    answer = []
    
    points = set()
    
    # 교점 구하기
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if (a * d) - (b * c) != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
            
            # 정수 확인
            if int(x) == x and int(y) == y:
                x = int(x)
                y = int(y)
                points.add((x, y))
                
    # 그림 그릴 범위 구하기
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    
    # 그림 그리기
    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                row += "*"
            else:
                row += "."
        answer.append(row)
                    
    return answer
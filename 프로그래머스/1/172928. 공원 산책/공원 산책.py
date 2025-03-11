def solution(park, routes):
    H = len(park)
    W = len(park[0])
    directions = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    
    # 시작 위치
    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                x, y = i, j
                break
    
    # 명령 수행
    for route in routes:
        d, n = route.split()
        dx, dy = directions[d]
        nx, ny = x, y
        
        for _ in range(int(n)):
            nx += dx
            ny += dy
            
            if nx < 0 or nx >= H or ny < 0 or ny >= W or park[nx][ny] == "X":
                break
        
        else:
            x, y = nx, ny
            
    return [x, y]
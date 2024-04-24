def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    # 우, 하, 좌, 상
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    num = 1
    x, y = 0, 0
    index = 0
    
    while num <= n * n:
        answer[x][y] = num
        num += 1
        
        nx, ny = x + dir[index][0], y + dir[index][1]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            index = (index + 1) % 4
            nx, ny = x + dir[index][0], y + dir[index][1]
        
        x, y = nx, ny
    
    return answer
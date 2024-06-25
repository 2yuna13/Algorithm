def solution(board):
    answer = 0
    n = len(board)
    #상, 하, 좌, 우, 대각선
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    danger = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # 지뢰 위치 표시 & 주변 8칸을 위험으로 표시
            if board[i][j] == 1:
                danger[i][j] = 1
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        danger[nx][ny] = 1

    # 지뢰가 있는 위치를 포함하여 주변 8칸을 위험으로 표시
    # for x, y in danger:
    #     for i in range(8):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #         if 0 <= nx < n and 0 <= ny < n:
    #             board[nx][ny] = 1
    
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                answer += 1
                
    return answer
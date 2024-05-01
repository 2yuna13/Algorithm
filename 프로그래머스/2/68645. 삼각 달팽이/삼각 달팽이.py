# x + 1, y + 1, x - 1 & y - 1
# 방향전환.. 
# 최대값 => 1 + 2 + ... + n 

def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    
    # 아래, 오른쪽, 대각선
    dir = [(1, 0), (0, 1), (-1, -1)]
    
    num = 1
    x, y, index = 0, 0, 0
    max_num = sum(range(n + 1))
    
    while num <= max_num:
        answer[x][y] = num        
        num += 1 
        
        nx, ny = x + dir[index][0], y + dir[index][1]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            index = (index + 1) % 3
            nx, ny = x + dir[index][0], y + dir[index][1]
            
        x, y = nx, ny      

    return [j for i in answer for j in i]


#         # 아래
#         for x in range(n - 1):
#             answer[x][0] = num
#             num += 1

#         # 오른쪽
#         for y in range(n - 1):
#             answer[n - 1][y] = num
#             num += 1

#         # 대각선
#         for x in range(n - 1, 0, -1):
#             answer[x][x] = num
#             num += 1
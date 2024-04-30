def solution(rows, columns, queries):
    answer = []
    graph = [[0] * columns for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            graph[i][j] += i * columns + (j + 1)
    
    # 1. y1 에서 y2 , (0, 1)
    # 2. x1 에서 x2, (1, 0)
    # 3. y2 에서 y1, (0, -1)
    # 4. x2 에서 x1, (-1, 0)
    # x1, y1 => 회전하면서 rotate_list 저장
    for query in queries:
        x1, y1, x2, y2 = query
        
        rotate_list = []        
        temp = graph[x1 - 1][y1 - 1]
        rotate_list.append(temp)
        
        # 1. y1 에서 y2 , (0, 1)
        for i in range(y1, y2):
            cur = graph[x1 - 1][i]
            rotate_list.append(cur)
            
            graph[x1 - 1][i] = temp
            temp = cur
            
        # 2. x1 에서 x2, (1, 0)
        for i in range(x1, x2):
            cur = graph[i][y2 - 1]
            rotate_list.append(cur)
            
            graph[i][y2 - 1] = temp
            temp = cur
        
        # 3. y2 에서 y1, (0, -1)
        for i in range(y2 - 2, y1 - 2, -1):
            cur = graph[x2 - 1][i]
            rotate_list.append(cur)
            
            graph[x2 - 1][i] = temp
            temp = cur
            
        # 4. x2 에서 x1, (-1, 0)
        for i in range(x2 - 2, x1 - 1, -1):
            cur = graph[i][y1 - 1]
            rotate_list.append(cur)
            
            graph[i][y1 - 1] = temp
            temp = cur
        
        graph[x1 - 1][y1 - 1] = temp
        
        answer.append(min(rotate_list))
        
    return answer
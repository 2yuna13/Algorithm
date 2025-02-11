def dfs(k, dungeons, visited, count):
    global answer
    answer = max(answer, count)
        
    for i in range(len(dungeons)):
        if not visited[i]:
            minimum, consume = dungeons[i]
            
            if k >= minimum:
                visited[i] = True
                dfs(k - consume, dungeons, visited, count + 1)
                visited[i] = False
        

def solution(k, dungeons):
    global answer
    answer = 0
    
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
            
    return answer
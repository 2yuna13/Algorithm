import sys
input = sys.stdin.readline

# 컴퓨터의 수
n = int(input())

#바이러스 걸리게 되는 컴퓨터의 수
m = int(input())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(n+1)]

# 모든 간선 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 저장할 리스트 초기화
visited = [0] * (n + 1)

def dfs(v):
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

dfs(1)

print(sum(visited)-1)
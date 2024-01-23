from collections import deque
import sys
input = sys.stdin.readline

def bfs(weight):
    q = deque()
    q.append(num1)
    visited = [False] * (n + 1)
    visited[num1] = True

    while q:
        now = q.popleft()

        for node, w in bridges[now]:
        # 현재 중량으로 건널 수 있는 다리만 탐색
            if not visited[node] and w >= weight:
                visited[node] = True
                q.append(node)
                
   # num2 에 도달할 수 있는 지 반환
    if visited[num2]:
        return True
    else:
        return False


n, m = map(int, input().split())
bridges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridges[a].append([b, c])
    bridges[b].append([a, c])

# 공장이 위치한 두 섬
num1, num2 = map(int, input().split())

start = 0
end = int(1e9)

result = 0
while start <= end:
    mid = (start + end) // 2
	
    # 중량(mid)으로 num1 에서 num2 까지 도달 가능한지 확인
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
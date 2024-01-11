from collections import deque

def bfs(n):
    q = deque([0])
    count = 0

    while q:
        value = q.popleft()
        
        for i in range(1, 4):
            new_value = value + i
            if new_value <= n:
                if new_value == n:
                    count += 1
                else:
                    q.append(new_value)
    return count

t = int(input())

for _ in range(t):
    n = int(input())
    result = bfs(n)
    print(result)
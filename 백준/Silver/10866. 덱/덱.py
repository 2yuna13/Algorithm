from collections import deque
from sys import stdin

input = stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    order = input().split()
    cmd = order[0]
    
    if cmd == 'push_front':
        x = order[1]
        d.appendleft(int(x))
    
    elif cmd == 'push_back':
        x = order[1]
        d.append(int(x))

    elif cmd == 'pop_front':
        if not d:
            print(-1)
        else:
            print(d.popleft())

    elif cmd == 'pop_back':
        if not d:
            print(-1)
        else:
            print(d.pop())

    elif cmd == 'size':
        print(len(d))

    elif cmd == 'empty':
        if not d:
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])

    elif cmd == 'back':
        if not d:
            print(-1)
        else:
            print(d[-1])
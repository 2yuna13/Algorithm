from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    queue = deque(map(int, input().split()))
    queue = deque([(value, idx) for idx, value in enumerate(queue)])

    count = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())
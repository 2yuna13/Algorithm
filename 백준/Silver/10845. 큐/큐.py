from collections import deque
import sys 
input = sys.stdin.readline

def push(queue, x):
    queue.append(x)

def pop(queue):
    if len(queue) > 0:
        n = queue.popleft()
        return n
    else:
        return -1

def size(queue):
    return len(queue)

def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0

def front(queue):
    if len(queue) > 0:
        return queue[0]
    else:
        return -1

def back(queue):
    if len(queue) > 0:
        return queue[-1]
    else:
        return -1

n = int(input())
queue = deque()

for _ in range(n):
    user_input = input().split()

    if user_input[0] == "push":
        x = int(user_input[1])
        push(queue, x)

    elif user_input[0] == "pop":
        print(pop(queue))

    elif user_input[0] == "size":
        print(size(queue))

    elif user_input[0] == "empty":
        print(empty(queue))

    elif user_input[0] == "front":
        print(front(queue))

    elif user_input[0] == "back":
        print(back(queue))
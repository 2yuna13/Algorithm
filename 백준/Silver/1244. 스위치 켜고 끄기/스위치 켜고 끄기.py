import sys

input = sys.stdin.readline

n = int(input())
switch = [-1] + list(map(int, input().split()))
m = int(input())
for _ in range(m):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, n + 1, num):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    if sex == 2:
        if switch[num] == 1:
            switch[num] = 0
        else:
            switch[num] = 1
        left, right = num - 1, num + 1
        while left > 0 and right <= n and switch[left] == switch[right]:
            if switch[left] == 1:
                switch[left], switch[right] = 0, 0
            else:
                switch[left], switch[right] = 1, 1
            left = left - 1
            right = right + 1

for i in range(1, n + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()
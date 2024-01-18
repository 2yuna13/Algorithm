import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

distance = []
for i in range(n - 1):
    distance.append(sensor[i + 1] - sensor[i])
distance.sort(reverse=True)

print(sum(distance[k - 1:]))
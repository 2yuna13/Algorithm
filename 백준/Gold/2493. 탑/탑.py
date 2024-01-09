n = int(input())
height = list(map(int, input().split()))

ans = [0] * n
stack = []

for i in range(n):
    while stack and height[i] >= height[stack[-1]]:
        stack.pop()

    if stack:
        ans[i] = stack[-1] + 1

    stack.append(i)

# 결과 출력
print(*ans)
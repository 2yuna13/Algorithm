import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums.sort()

    answer = True
    for i in range(n - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            answer = False
            break

    if answer:
        print("YES")
    else:
        print("NO")
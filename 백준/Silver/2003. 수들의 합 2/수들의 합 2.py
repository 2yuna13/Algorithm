N, M = map(int, input().split())
nums = list(map(int, input().split()))

total_sum = nums[0]
left, right = 0, 0
cnt = 0

while True:
    if total_sum < M:
        right += 1
        if right >= N:
            break
        total_sum += nums[right]
    elif total_sum == M:
        cnt += 1
        total_sum -= nums[left]
        left += 1
    else:
        total_sum -= nums[left]
        left += 1

print(cnt)
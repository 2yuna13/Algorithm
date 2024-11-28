N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = N + 1
total_sum = 0
left = 0

for right in range(N):
    total_sum += nums[right]

    while total_sum >= S:
        answer = min(answer, right - left + 1)
        total_sum -= nums[left]
        left += 1
        
if answer == N + 1:
    print(0)
else:
    print(answer)
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

# 산술평균
print(round(sum(nums) / len(nums)))

# 중앙값
print(nums[len(nums) // 2])

# 최빈값
counter = Counter(nums).most_common()
max_cnt = counter[0][1]
max_list = []
for i in counter:
    if i[1] == max_cnt:
        max_list.append(i[0])

if len(max_list) == 1:
    print(max_list[0])
else:
    print(max_list[1])

# 범위
print(nums[-1] - nums[0])
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            lo = i + 1
            hi = len(numbers) - 1

            while lo <= hi:
                mid = (lo + hi) // 2

                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] < target - numbers[i]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
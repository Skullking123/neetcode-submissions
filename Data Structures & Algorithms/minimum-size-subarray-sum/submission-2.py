class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0

        currWindowSum = 0
        res = float('inf')
        for right in range(len(nums)):
            # print(left, right)

            currWindowSum += nums[right]

            if currWindowSum >= target:
                while left <= right and currWindowSum >= target:
                    res = min(res, right - left + 1)
                    currWindowSum -= nums[left]
                    left += 1

        return res if res != float('inf') else 0
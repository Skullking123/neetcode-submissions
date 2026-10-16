class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        res = -1
        while left <= right:
            median = int((left + right) / 2)

            if target == nums[median]:
                res = median
                break
            elif target < nums[median]:
                right = median - 1
            else: # target > nums[median]
                left = median + 1

        return res
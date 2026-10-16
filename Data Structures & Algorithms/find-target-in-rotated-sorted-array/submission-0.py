class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target == nums[0]:
            return 0

        while left <= right:
            median = int((right + left) / 2)

            if nums[median] == target:
                return median

            if nums[median] >= nums[left]: # in the left sorted portion
                if target >= nums[median] or target < nums[left]:
                    left = median + 1
                else:
                    right = median - 1
            else: # in the right sorted portion
                if target < nums[median] or target > nums[right]:
                    right = median - 1
                else:
                    left = median + 1

        return -1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = float("infinity")
        while left <= right:
            median = int((right + left)/ 2)
            res = min(res, nums[median])
            if nums[median] >= nums[0]:
                left = median + 1
            elif nums[median] < nums[0]:
                right = median - 1
        
        return min(res, nums[0])
            


        

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Given an int arr where nums[i] = max jump len at ith pos
        # return true if you can reach the last index starting from index 0 or false
        reach = 0

        for idx in range(len(nums)):
            if idx > reach:
                break
            
            reach = max(reach, nums[idx] + idx)
        
        return reach >= len(nums) - 1
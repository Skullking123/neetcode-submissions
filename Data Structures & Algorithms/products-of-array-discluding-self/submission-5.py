class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given an int arr nums, return an arr where output[i] is the product of all elms of nums except nums[i]
        # try to solve in O(n) without using division
        n = len(nums)
        left = [0] * n
        right = [0] * n 
        # since the elms on the ends are missing a side, set the missing side to 1 to make it unconsequential
        left[0] = 1
        right[n - 1] = 1

        for idx in range(1, n):
            left[idx] = left[idx - 1] * nums[idx - 1]
        
        for idx in range(n - 2, -1, -1):
            right[idx] = right[idx + 1] * nums[idx + 1]
        
        res = []
        for idx in range(n):
            res.append(left[idx] * right[idx])
        
        return res
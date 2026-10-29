class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)):
            num = nums[idx]
            if num > 0:
                break
            left = idx + 1
            right = len(nums) - 1
            if idx != 0 and nums[idx - 1] == nums[idx]:
                continue
            
            while left < right:
                if num + nums[left] + nums[right] == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1    
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else: # num + nums[left] + nums[right] < 0
                    left += 1
        
        return res
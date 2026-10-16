class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []

        for numIndex in range(len(nums)):
            left = numIndex + 1
            right = len(nums) - 1
            if numIndex != 0 and nums[numIndex] == nums[numIndex - 1]:
                continue
            while left < right:
                if nums[numIndex] + nums[left] + nums[right] == 0:
                    print(f"Appending {[nums[numIndex], nums[left], nums[right]]}")
                    res.append([nums[numIndex], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif nums[numIndex] + nums[left] + nums[right] < 0:
                    left += 1
                else: # nums[numIndex] + nums[left] + nums[right] > 0
                    right -= 1
        
        return res
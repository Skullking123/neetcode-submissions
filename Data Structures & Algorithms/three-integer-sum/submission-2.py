class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, num in enumerate(nums):

            left = index + 1
            right = len(nums) - 1

            if index > 0 and num == nums[index - 1]:
                continue

            while left < right:
                threeSum = num + nums[left] + nums[right]
                print(f"({index}, {left}, {right})")
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return res
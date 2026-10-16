class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            diff[target - nums[i]] = i
        
        res = []
        for i in range(len(nums)):
            if nums[i] in diff and i != diff[nums[i]]:
                res = [min(i, diff[nums[i]]), max(i, diff[nums[i]])]
                break
        print(diff)
        return res
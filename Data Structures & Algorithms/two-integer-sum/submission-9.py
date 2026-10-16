class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for idx in range(len(nums)):
            diff[nums[idx]] = idx
        
        for idx in range(len(nums)):
            currDiff = target - nums[idx]
            if currDiff in diff and idx != diff[currDiff]:
                return [min(idx, diff[currDiff]), max(idx, diff[currDiff])]
        
        return [0, 1]
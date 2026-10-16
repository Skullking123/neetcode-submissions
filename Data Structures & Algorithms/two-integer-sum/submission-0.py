class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addends = dict()
        for numIndex in range(0, len(nums)):
            remaining = target - nums[numIndex]
            if remaining in addends:
                return [min(numIndex, addends[remaining]), max(numIndex, addends[remaining])]
            else: 
                addends[nums[numIndex]] = numIndex
        return []
        
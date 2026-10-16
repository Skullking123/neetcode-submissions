class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[:(len(nums) - 1)]), self.robHelper(nums[1:len(nums)]))

    def robHelper(self, nums: List[int]) -> int:
        prevPrevRob = 0
        prevRob = 0

        for i in range(len(nums)):
            currRob = max(prevPrevRob + nums[i], prevRob)
            prevPrevRob = prevRob
            prevRob = currRob
        
        return prevRob
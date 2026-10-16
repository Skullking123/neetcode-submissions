class Solution:
    def rob(self, nums: List[int]) -> int:
        prevPrevRob = 0
        prevRob = 0

        for i in range(len(nums)):
            currRob = max(prevPrevRob + nums[i], prevRob)
            prevPrevRob = prevRob
            prevRob = currRob
        
        return prevRob
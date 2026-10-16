class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elms = {}

        for idx in range(len(nums)):
            if target - nums[idx] in elms:
                return [elms[target - nums[idx]], idx]
            elms[nums[idx]] = idx

        return [-1, -1]


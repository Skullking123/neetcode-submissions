class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLen = 0
        for num in nums:
            if num - 1 not in unique:
                length = 1
                while num + length in unique:
                    length += 1
                maxLen = max(length, maxLen)
        
        return maxLen
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        ptr = 1

        while ptr < len(nums):
            if nums[ptr] == nums[ptr - 1]:
                nums.pop(ptr)
            else: # we have found a unique elm
                k += 1
                ptr += 1
        
        return k

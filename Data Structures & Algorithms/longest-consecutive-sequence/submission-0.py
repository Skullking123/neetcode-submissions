class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set(nums)

        res = 0

        for num in unique:
            if num - 1 not in unique:
                temp = 1
                while num + temp in unique:
                    temp += 1
                res = max(temp, res)

        return res

        # for num in nums:
        #     if num in seq:
        #         seq[num] = seq[num] + 1
        #     else:
        #         seq[num] = 1

        # for i in range(max(nums)):
        #     if i in seq:
        #         if i - 1 in seq:
        #             seq[i] = seq[i - 1] + 1
        
        # return max(seq.values())

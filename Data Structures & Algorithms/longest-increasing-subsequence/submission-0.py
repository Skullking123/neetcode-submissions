class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return the length of the longest increasing subsequence

        # an elm is either part of a increasing subsequence that is composed of elms before it
        # or is its own increasing subsequence

        # need a way to keep track of current subsequences that have been found
        
        # for each element, evaluate if it is greater than the last elm of any subsequence seen b4
            # if it is, update it and add to subseq and reevaluate longest len
            # if not add it as its own subsequence and reeval longest len
        
        # lengths[i] = longest increasing subseq made ending at i inclusively
        lengths = [0] * len(nums)
        lengths[0] = 1

        for idx in range(len(nums)):
            max_sub_len = 1
            for l_idx in range(idx):
                if nums[l_idx] < nums[idx]:
                    max_sub_len = max(max_sub_len, lengths[l_idx] + 1)
            lengths[idx] = max_sub_len
        print(lengths)
        return max(lengths)

        

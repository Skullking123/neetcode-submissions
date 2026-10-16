class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # given an int arr nums, find a subarr that has the largest product, and return the product
        # subarr is a contigous non-empty sequence of elements within an arr
        

        # multiplying neg numbers, only gets bigger if we have an even number of negatives
        # multipling any number of positives gets bigger
        # 0 just kills, so 0 should never be part of our contiguous subarr unless the entire thing is 0 
        # -1 


        # this solution doesn't work for the case: [-2,3,-4]
        # this alg is too greedy/too short sighted, once it gets to 3, it will attempt to do -2 * 3 and see that its -6, but
        # its less than 3, so it saves 3 thinking that its better to keep 3 three as the standalone product
        # But it doesn't see that there is a -4 to turn the -6 back to positive and thus get a bigger product of 24. 
        
        # [-10, -10, -10] odd number of negs
        # [] + [-10] = -10
        # [-10] + [-10] = 100
        # [-10, -10] + [-10] = -1000 X so we keep 100
        # What if we have [-10, -10, -10, -10] even number of negs
        # [] + [-10] = -10
        # [-10] + [-10] = 100
        # [-10, -10] + [-10] = -1000 X so we keep 100
        # [-10, -10, -10, -10] = 10000 
        # we should only look at subarrs seperated by 0s
        
        # multiplying two pos gets you a bigger pos number
        # multipying two negs gets you a bigger pos number
        # multiplying a neg and a pos gets you a smaller neg number


        # maintain three values:
            # result
            # curr max 
            # most neg number
        # iterate over nums:
            # update most neg number 
            # update max by including num into our current max 
            # if neg number becomes positive
                # replace curr_max with most neg number
            # update result with curr_max
            
        # return result

        res = curr_max = curr_min = nums[0]
        
        for num in nums[1:]:
            temp_max = curr_max
            temp_min = curr_min
            curr_max = max(curr_max * num, num, temp_min * num)
            curr_min = min(curr_min * num, num, temp_max * num)
            res = max(res, curr_max)
            # print(f"temp_max: {temp_max}, curr_max: {curr_max}, temp_min: {temp_min}, curr_min: {curr_min}, res: {res}")



        return res




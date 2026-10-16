class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        res = []

        prefix.append(nums[0])
        postfix.append(nums[len(nums) - 1])

        for num in range(1, len(nums)):
            prefix.append(prefix[num - 1] * nums[num])

        for num in range(len(nums) - 2, -1, -1):

            postfix.insert(0, postfix[0] * nums[num])
        

        for i in range(len(nums)):
            if i == 0 and len(nums) > 1:
                res.append(postfix[i + 1])
            elif i == len(nums) - 1 and len(nums) > 1:
                res.append(prefix[i - 1])
            else:
                res.append(postfix[i + 1] * prefix[i - 1])

        return res
            


        


        
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodEntireArr = 1
        res = []
        zeroCount = 0
        nonZeroProd = 1
        for num in nums:
            if num == 0:
                zeroCount = zeroCount + 1
            else:
                nonZeroProd = nonZeroProd * num
            
            prodEntireArr = prodEntireArr * num
        
        for num in nums:
            if zeroCount > 1:
                res.append(0)
            elif num == 0:
                res.append(int(nonZeroProd))
            else:
                res.append(int(prodEntireArr / num))
        return res
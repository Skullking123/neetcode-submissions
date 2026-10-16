class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l < r:
            if maxL <= maxR:
                # do something
                res += max(0, maxL - height[l])
                l += 1
                maxL = max(height[l], maxL)
            else: # maxL > maxR
                res += max(0, maxR - height[r])
                r -= 1
                maxR = max(height[r], maxR)
        
        return res
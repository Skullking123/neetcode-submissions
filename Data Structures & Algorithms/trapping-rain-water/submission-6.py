class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        res = 0

        while left < right:
            if leftMax <= rightMax:
                left += 1
                res += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                res += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])

        return res
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0] * len(heights)
        right = [0] * len(heights)
        stack = [(heights[0], 0)] # (height, idx)
        for idx in range(1, len(heights)):
            print(stack)
            while stack and heights[idx] < stack[-1][0]:
                _, prevIdx = stack.pop()
                right[prevIdx] = idx - 1
            stack.append((heights[idx], idx))
        
        while stack:
            _, prevIdx = stack.pop()
            right[prevIdx] = len(heights) - 1
        
        stack = [(heights[len(heights) - 1], len(heights) - 1)] # (height, idx)
        for idx in range(len(heights) - 2, -1, -1):
            while stack and heights[idx] < stack[-1][0]:
                _, prevIdx = stack.pop()
                left[prevIdx] = idx + 1
            stack.append((heights[idx], idx))
        
        while stack:
            _, prevIdx = stack.pop()
            left[prevIdx] = 0
        res = 0
        for idx in range(len(heights)):
            height = heights[idx]
            leftB = left[idx]
            rightB = right[idx]
            res = max(res, height * (rightB - leftB + 1))
        print(left)
        print(right)
        return res

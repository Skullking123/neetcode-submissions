class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for char in s:
            if char != "*":
                stack.append(char)
                continue
            elif stack:
                stack.pop()

        return "".join(stack)
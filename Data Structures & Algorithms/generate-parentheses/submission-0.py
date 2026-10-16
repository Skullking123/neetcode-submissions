class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(openP: int, closedP: int):
            if openP == closedP and closedP == n:
                res.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                backTrack(openP + 1, closedP)
                stack.pop()
            
            if closedP < openP:
                stack.append(")")
                backTrack(openP, closedP + 1)
                stack.pop()

        backTrack(0, 0)
        return res
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for brkt in s:
            if brkt in ["(", "{", "["]:
                stack.append(brkt)
            elif brkt in [")", "}", "]"]:
                top = stack[-1] if stack else ""
                if (top, brkt) in [("(", ")"), ("{", "}"), ("[", "]")]:
                    stack.pop()
                else:
                    return False
        
        return not stack
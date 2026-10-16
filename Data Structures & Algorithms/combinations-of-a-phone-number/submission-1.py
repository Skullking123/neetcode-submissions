class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        digitToChars = {}
        digitToChars[2] = ['a', 'b', 'c']
        digitToChars[3] = ['d', "e", 'f']
        digitToChars[4] = ['g', "h", "i"]
        digitToChars[5] = ['j', 'k', 'l']
        digitToChars[6] = ['m', 'n', 'o']
        digitToChars[7] = ['p', 'q', 'r', 's']
        digitToChars[8] = ['t', 'u', 'v']
        digitToChars[9] = ['w', 'x', 'y', 'z']
        
        stack = []
        res = []
        def dfs(idx):
            if idx == len(digits):
                res.append("".join(stack))
                return

            digit = int(digits[idx])

            for letter in digitToChars[digit]:
                stack.append(letter)
                dfs(idx + 1)
                stack.pop()
        
        dfs(0)
        return res
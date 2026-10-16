class Solution:
    def countSubstrings(self, s: str) -> int:
        # given a string s, return the number of substrings within s that are palindromes

        queue = deque()
        n = len(s)
        for i in range(n):
            queue.append((i, i))

            if i + 1 < n:
                queue.append((i, i + 1))
        
        res = 0
        while queue:
            cl, cr = queue.popleft()
            
            if cl < 0 or cr >= n:
                continue


            if s[cl] == s[cr]:
                res += 1
                queue.append((cl - 1, cr + 1))
        
        return res
class Solution:
    def countSubstrings(self, s: str) -> int:
        # given a string s, return the number of substrings within s that are palindromes
        n = len(s)
        palindromes = [[False] * n for i in range(n)]

        # set base cases
        for i in range(n):
            palindromes[i][i] = True

        res = n
        for size in range(1, n):
            # print(f"size {size}") 
            for idx in range(n):
                if idx + size >= n:
                    break

                # print(idx)
                if s[idx] == s[idx + size] and(palindromes[idx + 1][idx + size - 1] or size + 1 == 2):
                    palindromes[idx][idx + size] = True
                    # print("come here")
                    res += 1
        # print(palindromes)
        return res


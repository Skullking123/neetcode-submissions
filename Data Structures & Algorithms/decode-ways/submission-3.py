class Solution:
    def numDecodings(self, s: str) -> int:
        # return the number of ways to that the string can be decoded
        # a string consiting of uppercase english chars can be encoded to a number using mapping from A -> 1 to Z -> 26
        # To decode a message, digits must be groouped and then mapped back into letters using the reverse of the mapping
        # There are mutiple ways to decode a message: For example, "1012" can be mapped into:
            # "JAB" with the grouping (10 1 2)
            # "JL" with the grouping (10 12)
        # But the grouping (1 01 2) is invalid because 01 has a leading zero


        n = len(s)
        # reverse = {}
        # for i in range(26):
        #     reverse[i + 1] = chr(ord("A") + i)
        
        # we can do a dynamic programming alg emulating coin changing alg
        # we have an arr where each ith index stores the number of ways we can decode indices 0-i inclusive
        # at each index i, we add:
            # arr[i - 1] + 1 # if s[i] != 0
            # arr[i - 2] + 1# if s[i-1:i] inclusive is a valid number        
        ways = [0] * n
    
        # base cases
        if s[0] != "0":
            ways[0] = 1
            if n > 1 and s[1] == "0":
                ways[0] = 0
        
        if n > 1 and ((s[0] == "1") or (s[0] == "2" and s[1] <= "6")):
            ways[1] += ways[0] + 1
        elif n > 1 and s[1] != 0:
            ways[1] += ways[0]
        print(ways)
        # dynamic step
        for i in range(2, n):

            if s[i] != "0":
                ways[i] += ways[i - 1]
            
            if (s[i - 1] == "1") or (s[i - 1] == "2" and s[i] <= "6"):
                ways[i] += ways[i - 2]

            print(ways)

        return ways[n - 1]
class Solution:
    def compress(self, chars: List[str]) -> int:
        # given an arr of characters, compress it using the following alg:
            # start with an emptry string s, for each group of consecutive repeating characters:
                # if the groups len is 1, appeand the character to s
            # the compress string s should not be returned separately, but instead stored in the input character array
            # return the len of the compressed string
        


        # chars=["a","1","1","a","a","a","a","a","a","a","a"]
        # 
        ow = 0 # ptr for overwriting the original array with the compressed str
        n = len(chars)
        prev = 0
        for idx in range(n):
            if idx >= n - 1 or chars[idx] != chars[idx + 1]:
                groupSize = "" if idx - prev + 1 == 1 else str(idx - prev + 1)
                substr = chars[idx] + groupSize
                for c in substr:
                    chars[ow] = c
                    ow += 1
                prev = idx + 1
        
        for _ in range(n - ow):
            chars.pop()

        return ow + 1


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + f"{len(word)}&" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        not_done = True
        letter = 0
        while not_done:
            # check if theres any left 
            if letter >= len(s):
                break
            word = ""
            length = 0
            #get the length of the word
            if s[letter].isdecimal():
                num_str = ""
                while s[letter] != "&":
                    num_str = num_str + s[letter]
                    letter = letter + 1
                length = int(num_str)
            letter = letter + 1 # move pointer past the '&' seperator 
            # construct the word
            for letter_in_word in range(length):
                word = word + s[letter]
                letter = letter + 1
            # add the word to our result
            res.append(word)
            
        return res
        





                
        


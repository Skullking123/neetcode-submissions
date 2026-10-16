class Solution:
    def checkValidString(self, s: str) -> bool:
        # given a string s, s contains only ( ) and *
        # return true if s is valid
        # * can be ( ) or ""
        
        # (*****)
        # (*****(
        # )*****)
        # )*****(

        left = []
        stars = []
        for idx in range(len(s)):
            c = s[idx]
            if c == "(":
                left.append(idx)
            elif c == "*":
                stars.append(idx)
            else:
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            
        while left:
            while stars and stars[-1] < left[-1]:
                stars.pop()
            
            if stars: # there is a star that comes after our left that can be turned into a ) paren
                left.pop()
                stars.pop()
            else: # there is no star to be a )
                return False
        
        return True


        # s="(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        # false
        #"(((((*(((((*((**(((*)*((((**))*)*)))))))()()))((*(((((*()*(**)()"
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Given three strs s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or 
        # false otherwise
        # Interleaving two strs s and t is done by dividing s and t into n and m substrings respectively, where the following conditions
        # are met:
        # abs(n - m) <= 1
        # s = s1 + s2 + ... + sn
        # t = t1 + t2 + ... + tm
        # interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2

        # Test cases by hand
        # s1 = aaaa
        # s2 = bbbb
        # s3 = aabbbbbaa
        # s3 = aa(s1) + bbbbb(s2) + aa(s1)

        # s1=""
        # s2=""
        # s3=""
        # ""(s1) + ""(s2)

        # s1="abc"
        # s2="xyz"
        # s3="abc"
        # This is false, you must use all parts of both s1 and s2

        # s1="abc"
        # s2="cde"
        # s3="abcde"
        # This is false, because you must use parts of both s1 and s2 (The only way to get abcde is to leave the c from s1 out)

        # first thought:
        # we maintain three ptrs called ptr1, ptr2, ptr3
        # we first try to interleave starting with s1
        # Check to see if s1 and s3 share a prefix of n chars
            # if it does, move ptr3 to n and ptr1 to n
                # recurse but with s2 and ptr2 instead of ptr2
                #  otherwise immediately return false
        # repeat the same process but starting at s2
        
        # s1 = ac
        # s2 = ab
        # s3 = aabc
        # ptr1 = 0
        # ptr2 = 0
        # ptr3 = 0

        # start with s1
        # the shared prefix between s1 and s3 starting at ptr1 and ptr3 respectively is a
        # update ptr1 = 1 and s3 = 1
        # recurse but now with s2
        # the shared prefix between s2 and s3 starting at ptr2 and ptr3 respectively is a
        # update ptr2 = 1 and s3 = 2
        # recurse but now with s1
        # there is no shared prefix between s1 and s3 starting at ptr1 and ptr3 respectively
        # return False

        # start with s2 now
        # the shared prefix between s2 and s3 starting at ptr2 and ptr3 respectively is a
        # update ptr2 = 1 and s3 = 1
        # recurse but now with s1
        # the shared prefix between s1 and s3 starting at ptr1 and ptr3 respectively is a
        # update ptr1 = 1 and s3 = 2
        # recurse with s2
        # shared prefix at ptr2 and ptr3 is b
        # update ptr2 = 2 and ptr3 = 3
        # recurse with s1
        # the shared prefix between s1 and s3 starting at ptr1 and ptr3 respectively is c
        # update ptr1 = 2 and ptr3 = 4
        # at this stage we've ended s3. so check if we used up all letters in s1 and s2. which we did
        # so return True
        
        # contains (ptr1, ptr2, ptr3) pairings that we have explored
        
        if len(s1) + len(s2) != len(s3):
            return False


        mem = set()    

        def interleave(ptr1, ptr2):
            if ptr1 > len(s1) or ptr2 > len(s2):
                return False
            
            if (ptr1, ptr2) in mem:
                return False

            ptr3 = ptr1 + ptr2

            if ptr3 == len(s3):
                return True

            if ptr1 < len(s1) and s1[ptr1] == s3[ptr3] and interleave(ptr1 + 1, ptr2):
                return True
            
            if ptr2 < len(s2) and s2[ptr2] == s3[ptr3] and interleave(ptr1, ptr2 + 1):
                return True
            
            mem.add((ptr1, ptr2))
            return False

            

        return interleave(0, 0)
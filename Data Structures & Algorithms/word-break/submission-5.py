class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # given a string s and a dictionary of strings wordDIct, return true if s can be segmented into a space-separated sequence of dict
        # words

        # we maintain an array that keeps track of what lengths of the string we have explored to prevent repetitive work
        # for ex: if we know that we have explored all possibilities of word break of a string with the first m chars, then
            # in the future, we don't explore other permutations of words that start with the first m chars
        
        # maintain a length arr of size (n + 1) of False values initially
        # start at the index 0
        # for every index:
            # for every word in wordDict, where wl is the length of that word:
                # check to see if the first wl characters starting at the index equal the word
                    # if it is check length[index + wl] 
                        # if True, do nothing. it was already explored
                        # if False, explore index + wl and recurse
            # set length[index] = True
        n = len(s)
        length = [False] * (n + 1)
        def breakHelper(idx):
            if idx == n:
                length[idx] = True
                # return True to end the search early
                return True
            
            for word in wordDict:
                wl = len(word)
                # bounds check
                if idx + wl > n:
                    continue
                # recurse if s starts with word at idx and we haven't explored length[idx + wl]
                if word == s[idx:(idx + wl)] and not length[idx + wl]:
                    if breakHelper(idx + wl):
                        # we alr reached the end, no point exploring more
                        return True

            # mark this idx as explored            
            length[idx] = True
            # we haven't reached the end
            return False
        breakHelper(0)

        return length[-1] 


        # try a naive solution, brute force with a recursive alg
        # a string s can be segemented by seeing if s starts with any one of the words, then seeing if the rest
        # can be composed of words from dict
        # base case
        if s == "":
            return True

        for word in wordDict:
            # index check
            if len(word) > len(s):
                continue
            # recursive step
            if s[:len(word)] == word and self.wordBreak(s[len(word):], wordDict):
                return True

        # our string doesn't start with any of the words so impossible
        return False
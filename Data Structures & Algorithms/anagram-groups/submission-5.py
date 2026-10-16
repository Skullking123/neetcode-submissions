class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group all anagrams together into sublists
        # the order of the output does not matter
        # an anagram is a string that contains exact same chars as another string
        # need a way to efficiently keep track of previous anagrams found
        # use a hashmap? Would need to figure out a key since lists and dicts are not hashable... maybe a tuple?
            # map a tuple containing char counts to index of the right sublist in our res
        # for every word
            # create a count of every letter 
            # check to see if we had alr come across anagrams of the word b4
            # if so, insert into that sublist
            # if not, make a new sublist containing the word

        anagrams = {}
        res = []
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            counts = tuple(counts)
            if counts in anagrams:
                idx = anagrams[counts]
                res[idx].append(word)
            else:
                anagrams[counts] = len(res)
                res.append([word])
        
        return res

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

        for word in strs:
            key = [0] * 26
            for letter in word:
                idx = ord(letter) - ord('a')
                key[idx] += 1
            key = tuple(key)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        
        res = []
        for sublist in anagrams.values():
            res.append(sublist)
        return res
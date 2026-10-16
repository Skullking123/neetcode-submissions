class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord('a')] += 1
            sublist = anagrams.get(tuple(key), [])
            sublist.append(word)
            anagrams[tuple(key)] = sublist
        return list(anagrams.values())

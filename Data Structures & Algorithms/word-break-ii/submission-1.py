class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isWord = False


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        trie = TrieNode("")

        for word in wordDict:
            curr = trie # start at the head
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = TrieNode(letter)
                
                curr = curr.children[letter]
            
            curr.isWord = True

        # stack = []
        # def dfs(curr):
        #     stack.append(curr.letter)

        #     if curr.isWord:
        #         print("".join(stack))
            
        #     for letter, node in curr.children.items():
        #         dfs(node)
            
        #     stack.pop()

        # dfs(trie)



        res = []
        subres = []
        # curr = current node in the trie that we are at
        # idx = idx of the next letter that we need to get to
        def dfs(curr, idx):
            
            # append the current letter to subres
            subres.append(curr.letter)
            # print(subres, idx)
            # check to see if we have constructed a sentence
            if idx == len(s):
                if curr.isWord:
                    res.append("".join(subres))
                subres.pop()
                return 

            if curr.isWord:
                subres.append(" ")
                if s[idx] in trie.children:
                    dfs(trie.children[s[idx]], idx + 1)
                subres.pop() # pop the space
            
            next = s[idx]
            
            if next in curr.children:
                dfs(curr.children[next], idx + 1)
            
            subres.pop()

        dfs(trie, 0)
        return res            

                








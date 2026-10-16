class TrieNode:
    def __init__(self):
        self.letter = ""
        self.isWord = False
        self.children = [None] * 26

class Solution:


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # need a trie
        # given a board and list of words, find all words that are present in the board
        # same cell cannot be used more than once in a word
        # board is square
        # building a trie dynamically as we iterate through the board is too much memory (4^(n^2))
        # build a trie out of the words that we need to find

        # build a trie out of the list of the words that we need to find
        # Traverse through board following the trie 
        # The root of the trie will represent the empty string
        # Each node will have at most 26 children (1 for each letter)
        # Each node has a boolean flag to say that its the final letter in a word, important for words that are a prefix of another
        # iterate through the list of words to build it, and insert each word into the trie
        # Go through the board
        # Use a visitedSet to keep track of whats used
        

        # Build our trie out of our list of words
        root = TrieNode()
        for word in words:
            curr = root # start at the root of the trie
            for letter in word:
                child = curr.children[ord(letter) - ord('a')]
                if child is None: # make a new node whenever a child is missing
                    newChild = TrieNode()
                    curr.children[ord(letter) - ord('a')] = newChild
                    newChild.letter = letter
                    child = newChild

                curr = child # prepare for next iteration
            curr.isWord = True # curr would be pointing at the last letter in the word
        
        # Traverse through the board checking our trie
        res = []
        curr = []
        visited = set()
        def dfs(x, y, trie):
            # bounds check
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return
            if (x, y) in visited:
                return

            # process current
            letter = board[y][x]
            idx = ord(letter) - 97
            nextNode = trie.children[idx]

            # go back 
            if nextNode is None:
                return

            curr.append(letter)
            visited.add((x, y))

            # add the word
            if nextNode.isWord:
                res.append("".join(curr))
                nextNode.isWord = False
            
            # traverse 
            dfs(x - 1, y, nextNode)
            dfs(x + 1, y, nextNode)
            dfs(x, y - 1, nextNode)
            dfs(x, y + 1, nextNode)

            # prepare to go back
            curr.pop()
            visited.remove((x, y))

            # prune the trie 
            if not nextNode.isWord and all(c is None for c in nextNode.children):
                trie.children[idx] = None
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                print(f"Starting dfs from ({x}, {y})")
                dfs(x, y, root)
        
        return res




        # iterative, backtracking would be a pain
        for y in range(len(board)):
            for x in range(len(board[0])):
                letterIdx = ord(board[y][x]) - ord('a')
                if root.children[letterIdx] is None:
                    continue
                stack = [(x, y)]
                word = [board[y][x]]
                trieStack = [root.children[letterIdx]] 
                visited = set() # keeps track of the cells being used in our word
                seen = set() # keeps track of cells that we have fully processed
                visited.add((x, y))
                while stack:
                    trieCurr = trieStack[-1]
                    currX, currY = stack[-1]

                    if trieCurr.isWord:
                        res.append("".join(word))

                    # go up
                    if currY > 0 and trieCurr.children(ord(board[y - 1][x]) - ord('a')) is not None and (x, y - 1) not in visited:
                        pass
                    # go down 
                    elif currY < len(board) - 1 and trieCurr.children[ord(board[y + 1][x]) - ord('a')] is not None and (x, y + 1) not in visited:
                        pass
                    # go left
                    elif currX > 0 and trieCurr.children[ord(board[y][x - 1])] is not None and (x - 1, y) not in visited:
                        pass
                    # go right
                    elif currX < len(board[0]) - 1 and trieCurr.children[ord(board[y][x + 1])] is not None and (x + 1, y) not in visited:
                        pass
                    # go back
                    else:
                        pass
                        

        # naive solution
        res = []
        buckets = {} # put each word into a bucket corresponding to their first letter
        for word in words:
            if word[0] not in buckets:
                buckets[word[0]] = set()
            buckets[word[0]].add(word)
        print(buckets)

        for x in range(len(board)):
            for y in range(len(board[0])):
                entry = board[x][y]
                if entry in buckets: # we found a letter that a word starts with, traverse it
                    found = []
                    for word in buckets[entry]:
                        print(f"searching for word {word}")
                        # do a depth first search starting at our current (x, y) to look for our each word
                        stack = [(x ,y)]
                        seen = set()
                        entriesUsed = set() # just keeps track of whats in our stack, but as a set, prevent us from reusing a letter in our search
                        entriesUsed.add((x, y))
                        cPtr = 1
                        while stack:
                            currX, currY = stack[-1]
                            print(f"{currX}, {currY}")
                            if cPtr == len(word): # we have reached the end of the word, we found it
                                found.append(word)
                                break
                            # traverse to an adj cord if they have the letter we're looking for, otherwise go back
                            if currX > 0 and board[currX - 1][currY] == word[cPtr] and (currX - 1, currY) not in seen and (currX - 1, currY) not in entriesUsed: # go left
                                stack.append((currX - 1, currY))
                                entriesUsed.add((currX - 1, currY))
                                cPtr += 1
                            elif currX < len(board) - 1 and board[currX + 1][currY] == word[cPtr] and (currX + 1, currY) not in seen and (currX + 1, currY) not in entriesUsed: # go right
                                stack.append((currX + 1, currY))
                                entriesUsed.add((currX + 1, currY))
                                cPtr += 1
                            elif currY > 0 and board[currX][currY - 1] == word[cPtr] and (currX, currY - 1) not in seen and (currX, currY - 1) not in entriesUsed: # go up
                                stack.append((currX, currY - 1))
                                entriesUsed.add((currX, currY - 1))
                                cPtr += 1
                            elif currY < len(board[0]) - 1 and board[currX][currY + 1] == word[cPtr] and (currX, currY + 1) not in seen and (currX, currY + 1) not in entriesUsed: # go down
                                stack.append((currX, currY + 1))
                                entriesUsed.add((currX, currY + 1))
                                cPtr += 1
                            else: # go back
                                seen.add((currX, currY))
                                entriesUsed.remove((currX, currY))
                                cPtr -= 1
                                stack.pop()
                    print("finished depth")
                    # clean up the bucket
                    for word in found:
                        res.append(word)
                        buckets[entry].remove(word)
                    # if we found all the words in that bucket, delete the bucket
                    if len(buckets[entry]) == 0:
                        del buckets[entry]
        
        return res




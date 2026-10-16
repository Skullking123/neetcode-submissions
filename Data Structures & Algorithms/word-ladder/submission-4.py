class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # given two words, beginWord and endWord, and a list of words wordList
        # all words are of the same length, all lowercase, and distinct
        # Transform beginWord into endWord by:
            # changing exactly one letter to another character
            # keep recursing with the new word you obtained
        
        # init our dictionary for O(1) lookup
        dictionary = set()
        for word in wordList:
            dictionary.add(word)
        
        
        # we do a layer-by-layer bfs
        queue = deque()
        queue.append(beginWord)
        tfs = 0
        while queue:

            layer = len(queue)
            tfs += 1
            # print(f"transformations: {tfs}")
            for _ in range(layer):
                curr = queue.popleft()
                # print(curr)

                if curr == endWord:
                    return tfs
                
                # make all possible transformations from curr
                for idx in range(len(curr)):
                    for ac in range(ord('a'), ord('z') + 1):
                        next = curr[:idx] + chr(ac) + curr[(idx + 1):]

                        if next in dictionary:
                            queue.append(next)
                            # remove it so we don't come back to this word again
                            dictionary.remove(next)
            
        return 0

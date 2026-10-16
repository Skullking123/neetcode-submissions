class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # We are given a list of string sthat are in some kind of alien alphabetical order
        # If its not in some kind of order, return ""
        # Otherwise return a string that lists the letters in their alien order
        # Standard alphabetical rules apply

        # ["aab","aac","ad","aef"]
        # "a"
        # ade
        # bc
        # abdce

        # ["aab","aac","ad","aef"]
        # maintain a list that represents the order we're building
        

        
        # ["hrn","hrf","er","enn","rfnn"]
        # [hernf]


        # ["aba", "ada", "aca", "add"]
        # [abdc] # we know that d has to come before c, but here its showing between aca and add that c has to come before d. impossible

        # we need to construct the graph in order to generate a topo-sort from it
        # we iterate over consecutive pairs of words
            # for each pair:
                # we traverse through the words until we find the first letter they differ by
                # save the dependency ex: hrn and hrf: first letter they differ by is n, f in the third idx. Save n -> f
                # if one of them is a prefix of the other, we gain nothing
        

        # we construct the graph 
        adj = {c: set() for w in words for c in w}
        inDegrees = {c: 0 for c in adj}
        n = len(words)

        # a string a is less than a string b if either is true:
        # the first letter where they differ is smaller in a than in b
        # a is a prefix of b and a.length < b.length
        for idx in range(n):
            word1 = words[idx]
            word2 = word1
            if idx + 1 < n:
                word2 = words[idx + 1]

            minLen = min(len(word1), len(word2))

            # quick check to see if this is a valid ordering:
            if len(word1) > len(word2) and word1[:minLen] == word2:
                # word2 should never be a prefix of word1
                return ""
            
            for widx in range(minLen):
                if word1[widx] != word2[widx]:
                    if word2[widx] not in adj[word1[widx]]: 
                        adj[word1[widx]].add(word2[widx])
                        inDegrees[word2[widx]] += 1
                    break
                
        res = []
        queue = deque()
        for elm, degree in inDegrees.items():
            if degree == 0:
                queue.append(elm)
        print(adj)
        print(inDegrees)
        visited = set()
        # do topo bfs
        while queue:
            elm = queue.popleft()
            # visited.add(elm)
            res.append(elm)

            # reduce the in-degrees of its neighbors
            for neighbor in adj[elm]:
                # if neighbor in visited:
                #     continue
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(res) == len(adj):
            return "".join(res)
        else:
            return ""
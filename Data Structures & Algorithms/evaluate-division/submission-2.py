class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # equations is a list of variable piars 
        # values is an arr of real numbers
        # equations[i] = [Ai, Bi] and values[i] = Ai / Bi
        # Also given some queries, where queries[j] = [Cj, Dj]
        # Return the answer to all queries. If a single answer cannot be determined, return -1

        # Input: equations = [["a","b"],["b","c"],["ab","bc"]], 
        # values = [4.0,1.0,3.25], 
        # queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]
        # Output: [4.00000,0.25000,1.00000,-1.00000,-1.00000]


        adj = defaultdict(dict)
        for idx in range(len(equations)):
            num, denom = equations[idx]
            val = values[idx]
            adj[num][denom] = val
            adj[denom][num] = 1 / val

        print(adj)
        def dfs(a, b, seen):
            # found b
            print(a, b)
            if b in adj[a]:
                return adj[a][b]
            if a in seen:
                return -1

            seen.add(a)
            # default value for if we aren't able to find b
            res = -1
            for denom, val in adj[a].items():
                search = dfs(denom, b, seen)
                if search != -1:
                    res = val * search
                    break
            return res


        res = []
        for a, b in queries:
            # check to see if those variables are available
            if a not in adj or b not in adj:
                res.append(-1)
            elif a == b:
                res.append(1)
            else:
                # print(f"{a} / {b}:")
                res.append(dfs(a, b, set()))

        return res
            





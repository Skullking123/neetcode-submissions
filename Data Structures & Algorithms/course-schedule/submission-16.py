class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # given an array of prereqs where prequisities[i] = [a, b] indicates you must take course b first if you want to take course a
        # there are a total of numCoureses courses you are required to take, labeled from 0 to numCourses - 1
        # a class can only have 1 prereq
        # return true if it is possible to finish all courses, otherwise return false
        
        # it is only impossible if we have circular prerequisites:
        # ex: [0,1],[1,2],[2,3],[3,0]  0 -> 1 -> 2 -> 3 -> 0
        # how to detect cycles?

        # we could do a dfs on every class an see if we somehow revisit a class we had prev alr  
        # there would be no need for backtracking as every class has only one prereq, we just drill down as far as we can

        # make the lookup of prereqs O(1)
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        seen = set()
        stack = set()
        def dfs(course) -> bool:
            # we found a loop
            if course in stack:
                return False

            # drill down
            stack.add(course)
            
            for prereq in prereqs[course]:
                if prereq in seen:
                    continue
                if not dfs(prereq):
                    return False
            
            # cleanup this frame
            stack.remove(course)
            # make sure we don't revisit this course again since we've cleared it
            seen.add(course)
            return True

        for a, _ in prerequisites:
            # check if it is something we have alr cleared
            if a in seen:
                continue
            
            if not dfs(a):
                return False

                
        
        return True
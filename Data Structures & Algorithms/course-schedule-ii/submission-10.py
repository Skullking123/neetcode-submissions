class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # given an array of prereqs where prequisities[i] = [a, b] indicates you must take course b first if you want to take course a
        # there are a total of numCoureses courses you are required to take, labeled from 0 to numCourses - 1
        # a class can only have 1 prereq
        # return a valid path that contains all the prereqs
        
        # it is only impossible if we have circular prerequisites:
        # ex: [0,1],[1,2],[2,3],[3,0]  0 -> 1 -> 2 -> 3 -> 0
        # how to detect cycles?

        # we could do a dfs on every class an see if we somehow revisit a class we had prev alr  
        # there would be no need for backtracking as every class has only one prereq, we just drill down as far as we can

        # make the lookup of prereqs O(1)
        prereqs = defaultdict(list)
        # set of courses that don't have prereqs and are not prereqs of another course

        for a, b in prerequisites:
            prereqs[a].append(b)


        stack = set()
        visited = set()
        def dfs(course) -> List[int]:
            # there is a circular dependency
            if course in stack:
                return []
            
            # drill down
            stack.add(course)
            
            schedule = []
            # traverse to prereqs
            for prereq in prereqs[course]:
                # don't reprocess prereqs we have alr traversed to during this dfs
                if prereq in visited:
                    continue
                prereq_path = dfs(prereq)
                # propagate that we found a cycle somewhere
                if not prereq_path:
                    return []
                schedule.extend(prereq_path)

            schedule.append(course)

            # cleanup
            visited.add(course)
            stack.remove(course)
            return schedule
        
        schedule = []
        for course in range(numCourses):
            if course in visited:
                continue
            
            sub_sched = dfs(course)
            if not sub_sched:
                return []
            else: 
                schedule.extend(sub_sched)
        
        return schedule
        













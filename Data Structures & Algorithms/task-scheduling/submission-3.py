class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # return the minimum number of CPU cycles required to complete all tasks
        # A single task is done in 1 cycle
        # idential tasks must be speerated by at least n CPU cycles
        
        # elements that appear more often should be prioritized
        heap = [] # elms are (soonest next cycle, task)

        counts = {}
        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1
        
        for task, count in (counts.items()):
            heapq.heappush(heap, (-count, task))


        cycle = 0
        cd = deque() # (nextCycle, task)
        while heap or cd:
            if heap:
                cycle += 1
                count, task = heapq.heappop(heap)
                # print(task)
                count += 1
                if count != 0:
                    cd.append((cycle + n + 1, count, task))
            else:
                cycle = cd[0][0] - 1
                # print(f"skip to cycle: {cycle}")
    
            while cd and cd[0][0] - 1 <= cycle:
                _, count, task = cd.popleft()
                heapq.heappush(heap, (count, task))
            

            
        
        return cycle
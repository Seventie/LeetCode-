from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)

        maxheap = [-x for x in freq.values()]
        heapq.heapify(maxheap)

        q = deque()   # [count, available_time]

        time = 0

        while maxheap or q:
            time += 1
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt != 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
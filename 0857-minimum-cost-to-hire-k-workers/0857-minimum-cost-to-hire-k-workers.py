class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        n = len(wage)
        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i]))
        workers.sort()
        _h = []
        _qAcc = 0
        ans = float('inf')
        for rate, q in workers:
            heapq.heappush(_h, -q)
            _qAcc += q
            if len(_h) > k:
                _qAcc += heapq.heappop(_h)
            if len(_h) == k:
                ans = min(ans, rate * _qAcc)
        return ans
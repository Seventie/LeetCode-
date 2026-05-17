class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        _h = []
        _q = deque()
        for x, y in freq.items():
            heapq.heappush(_h, -y)
        ans = 0
        while _h or _q:
            ans += 1
            if _h:
                curr = heapq.heappop(_h)
                curr += 1
                if curr < 0:
                    _q.append((ans + n, curr))
            if _q and _q[0][0] == ans:
                _, val = _q.popleft()
                heapq.heappush(_h, val)
        return ans
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:
            return 0
        _seen = 0
        _q = []
        n = len(stations)
        tank = startFuel
        ans = 0
        for x in range(n):
            dist = stations[x][0] - _seen
            tank -= dist
            while tank < 0:
                if not _q:
                    return -1
                tank += abs(heapq.heappop(_q))
                ans += 1
            heapq.heappush(_q, -stations[x][1])
            _seen = stations[x][0]
        tank -= (target - _seen)
        while tank < 0:
            if not _q:
                return -1
            tank += abs(heapq.heappop(_q))
            ans += 1
        return ans
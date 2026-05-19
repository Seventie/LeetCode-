class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        tank = startFuel
        ans = 0
        _m = []
        stations.append([target, 0])
        for pos, fuel in stations:
            while tank < pos and _m:
                tank += -heapq.heappop(_m)
                ans += 1
            if tank < pos:
                return -1
            heapq.heappush(_m, -fuel)
        return ans
from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_bus = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].append(bus)
        q = deque([source])
        visited_stops = set([source])
        visited_buses = set()
        buses_taken = 0
        while q:
            buses_taken += 1
            for _ in range(len(q)):
                stop = q.popleft()
                for bus in stop_to_bus[stop]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop == target:
                            return buses_taken
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            q.append(next_stop)
        return -1
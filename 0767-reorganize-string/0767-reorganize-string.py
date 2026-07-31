class Solution:
    def reorganizeString(self, s: str) -> str:
        store = Counter(s)
        h = []
        for x, y in store.items() :
            heapq.heappush(h, (-y, x))
        ans = ""
        prev = (None, None)

        while h :
            a, b = heapq.heappop(h)
            ans += b
            a += 1 
            if prev[0] is not None :
                heapq.heappush(h,prev)
                prev = (None, None)
            if a < 0 :
                prev = (a, b)
        if len(ans) != len(s) : return ""
        return ans 
                


class Solution:
    def candy(self, ratings: List[int]) -> int:
        _sum = [0] * len(ratings)
        n = len(ratings)
        if n == 1 : return 1 
        _heap = []
        for x in range(n) :
            heapq.heappush(_heap,(ratings[x], x))
        ans = 0 
        while _heap :
            rating , idx = heapq.heappop(_heap)
            req = 1
            if idx == 0 :
                if ratings[idx] > ratings[idx + 1]:
                    req += _sum[idx + 1]

            elif idx == n - 1 :
                if ratings[idx] > ratings[idx - 1]:
                    req += _sum[idx - 1]

            else :
                print("Hi")
                _max = 0
                if ratings[idx] > ratings[idx + 1] and ratings[idx] > ratings[idx - 1] :
                    _max = max(_sum[idx + 1], _sum[idx - 1])     
                elif ratings[idx] > ratings[idx + 1] :
                    _max = _sum[idx + 1]
                elif ratings[idx] > ratings[idx - 1] :
                    _max = _sum[idx - 1]
                req += _max 
            _sum[idx] = req
            ans += req 
           
        return ans 

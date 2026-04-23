class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy = prices[0]

        for x in range(1, len(prices)) :
            temp = prices[x]
            if temp < buy :
                buy = temp 
            else :
                curr = temp - buy
                profit = max(profit, curr)
        
        return profit
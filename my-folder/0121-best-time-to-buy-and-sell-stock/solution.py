class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = prices[0]
        for s in prices:
            if s > b:
                profit = max(s-b, profit)
            else:
                b=s
        return profit

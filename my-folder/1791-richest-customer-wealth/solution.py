class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for item in accounts:
            if sum(item) > maxWealth:
                maxWealth = sum(item)
        return maxWealth

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        diff = []
        for i in range(len(candies)):
            diff.append(maxCandy - candies[i])
        ans = []
        for i in range(len(candies)):
            if extraCandies >= diff[i]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
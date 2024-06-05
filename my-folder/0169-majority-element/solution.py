class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            d[i] = d.get(i,0) + 1
        return max(d, key=d.get)

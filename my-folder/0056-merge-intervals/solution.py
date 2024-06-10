class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 1:
            return intervals
        prev = intervals[0]
        for item in intervals[1::]:
            if item[0] <= prev[1]:
                prev[1] = max(prev[1],item[1])
            else:
                ans.append(prev)
                prev = item
        ans.append(prev)
        return ans
        


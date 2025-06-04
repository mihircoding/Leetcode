class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        i=0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                removed = intervals.pop(i+1)
            else:
                i += 1
        return intervals

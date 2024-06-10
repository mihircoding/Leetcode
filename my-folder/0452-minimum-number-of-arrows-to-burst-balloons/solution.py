class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        overlap = []
        points.sort(key=lambda x: x[0])
        arr=1
        end = points[0][1]
        for b in points[1::]:
            if b[0] > end:
                arr+=1
                end = b[1]
            else:
                end=min(end,b[1])
        return arr



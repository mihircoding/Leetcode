import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        largestSquare = int(math.sqrt(c)) + 1
        for i in range(largestSquare):
            b = math.sqrt(c-i*i)
            if b == int(b):
                return True
        return False

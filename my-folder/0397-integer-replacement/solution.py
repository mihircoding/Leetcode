import math
class Solution:
    def integerReplacement(self, n: int) -> int:
        d = {}
        return self.recur(n,d)
    def recur(self,n, d):
        if n == 1:
            return 0
        if n in d:
            return d[n]
        if n%2 == 0:
            d[n] = 1+ self.recur(n/2,d)
        else:
            d[n] = 1+ min(self.recur(n+1, d), self.recur(n-1, d))
        
        return d[n]
        

class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        def climber(N):
            if N in cache:
                return cache[N]
            elif N < 4:
                res = N
            else:
                res = climber(N-2) + climber(N-1)
            cache[N] = res
            return res
        return climber(n)

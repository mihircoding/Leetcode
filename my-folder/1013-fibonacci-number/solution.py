class Solution:
    def fib(self, n: int) -> int:
        
        cache = {}
        def recur(N):
            if N in cache:
                return cache[N]
            elif N < 2:
                res = N
            else:
                res = recur(N-1) + recur(N-2)
            cache[N] = res
            return res
        return recur(n)
            

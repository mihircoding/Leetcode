class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        i=5
        while i <= n:
            ans += n//i
            i*=5
        return ans

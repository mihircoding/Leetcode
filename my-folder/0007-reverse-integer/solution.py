class Solution:
    def reverse(self, x: int) -> int:
        rev = str(x)
        if rev[0] == '-':
            print(rev[:0:-1])
            rev = '-' + rev[:0:-1]
        else:
            rev = rev[::-1]
        rev = int(rev)
        if rev > (2**31) -1 or rev < -2**31:
            return 0
        return int(rev)

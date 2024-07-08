class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        ans = ''
        for i in range(len(s)):
            if s[0].isnumeric() is False and i==0:
                if s[0] == '-' or s[0] == '+':
                    ans += s[0]
                    continue
                return 0
            elif s[i] == 0:
                if s[i-1].isnumeric() is False or s[i-1] == 0:
                    continue
            elif s[i].isnumeric() is False:
                break
            else:
                ans  += s[i]
        if ans.isnumeric() is False and len(ans) < 2:
            return 0
        ans=int(ans)
        if ans > (2**31)-1:
            return (2**31)-1
        elif ans < -2**31:
            return -2**31
        else:
            return ans


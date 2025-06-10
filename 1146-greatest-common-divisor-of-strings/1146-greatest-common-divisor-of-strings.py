class Solution:
    def hcfnaive(self, a, b):
        if(b == 0):
            return abs(a)
        else:
            return self.hcfnaive(b, a % b)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallerLen = min(len(str1),len(str2))
        if str1+str2 != str2 + str1:
            return ""
        gcd = self.hcfnaive(len(str1),len(str2) )
        print(gcd)
        return "".join(str1[:gcd:])
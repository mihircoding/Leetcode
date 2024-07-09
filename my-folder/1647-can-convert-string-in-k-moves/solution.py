class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26

        for i in range(len(s)):
            if t[i] != s[i]:
                diff = ( ord(t[i]) - ord(s[i]) ) % 26
                b = diff + 26 * counter[diff]
                counter[diff] += 1
                if b > k:
                    return False
        return True
            

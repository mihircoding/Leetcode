import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = [x for x in s.strip().lower() if x.isalpha() or x.isnumeric()]
        print(L)
        if L == L[::-1]:
            return True
        return False

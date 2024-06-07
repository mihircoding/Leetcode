class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        ans=''
        for item in words[::-1]:
            ans += item + ' '
        return ans.strip()


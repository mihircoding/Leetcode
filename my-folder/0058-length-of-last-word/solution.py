class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(s.strip().split())[-1]) 
        

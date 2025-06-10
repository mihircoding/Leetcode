class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        order = []
        for i in range(len(s)):
            if s[i] in vowels:
                order.append(s[i])
        word = [c for c in s]
        for i in range(len(s)):
            if word[i] in vowels:
                word[i] = order.pop(-1)
        return "".join(word)
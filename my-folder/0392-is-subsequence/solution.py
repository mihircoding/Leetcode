class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        currentind = 0
        done=False
        for i in s:
            for x in range(currentind, len(t)):
                print(t[x])
                if i == t[x]:
                    print('fwf')
                    currentind = x+1
                    done=True
                    break
            if done is False:
                return False
            done=False
        return True


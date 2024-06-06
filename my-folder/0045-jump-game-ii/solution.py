class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        maxjump = 0
        nextmaxjump = 0
        lenList = len(nums) - 1
        for i in range(lenList):
            nextmaxjump = max(nextmaxjump, nums[i] + i)
            if i == maxjump:
                jump+=1
                maxjump = nextmaxjump
        return jump


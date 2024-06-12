class Solution:
    def rob(self, nums: List[int]) -> int:
        money = 0
        n =len(nums)
        if n==1: return nums[0]
        addList = [0]*n
        addList[0] = nums[0]
        addList[1] = max(nums[0],nums[1])

        for i in range(2,n):
            addList[i] = max(addList[i-1], nums[i] + addList[i-2])
        return addList[-1]
            

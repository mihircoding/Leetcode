class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=2
        while i < len(nums):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums.pop(i)
                i-=1
            i+=1
        return i
        

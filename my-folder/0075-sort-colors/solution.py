class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeros = 0
        ones = 0
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros,ones+zeros):
            nums[i] = 1
        for i in range(zeros+ones,n):
            nums[i] = 2
        return nums

        

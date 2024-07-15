class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 10**32
        second = 10**32
        for i in range(len(nums)):
            if nums[i] <= first:
                first= nums[i]
            elif nums[i] <= second and nums[i] > first:
                second = nums[i]
            elif nums[i] > first and nums[i] > second:
                return True
        return False

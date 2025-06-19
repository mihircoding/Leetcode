class Solution:
    def maxDiff(self, arr):
        return max(arr) - min(arr)
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        smallest = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] - nums[smallest] > k:
                counter += 1
                smallest = i
        return counter+1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefixProducts = [1] * n
        suffixProducts = [1] * n
        

        for i in range(1,n):
            prefixProducts[i] = nums[i-1] * prefixProducts[i-1]
        for i in range(n-2,-1,-1):
            suffixProducts[i] = nums[i+1] * suffixProducts[i+1]
        ans = []
        for i in range(n):
            ans.append(prefixProducts[i] * suffixProducts[i])
        return ans



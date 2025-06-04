class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans[nums[i]] = i
            elif abs(ans[nums[i]] - i) <= k:
                print(abs(ans[nums[i]] - i))
                return True
            else:
                ans[nums[i]] = i
        return False
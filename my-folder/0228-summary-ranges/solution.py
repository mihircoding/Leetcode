class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        end = 0
        ans = []
        done = True

        for i in range(len(nums)):
            if done == True:
                start = nums[i]
                end = nums[i]
            if i != len(nums) -1:
                if nums[i] + 1 == nums[i+1]:
                    end = nums[i+1]
                    done = False
                elif start != end:
                    ans.append(str(start) + '->'+ str(end))
                    done = True
                else:
                    ans.append(str(start))
                    done = True
            else:
                if start != end:
                    ans.append(str(start) + '->'+ str(end))
                else:
                    ans.append(str(start))
        return ans

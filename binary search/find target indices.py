# https://leetcode.com/problems/find-target-indices-after-sorting-array/submissions/

# O(nlogn)
class Solution:
    def targetIndices(self, nums, target: int):
        nums.sort()
        test = []
        for i in range(len(nums)):
            if nums[i] == target:
                test.append(i)
        return test
        
s = Solution()
print(s.targetIndices([1,2,5,2,3],2))
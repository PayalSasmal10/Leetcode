# https://leetcode.com/problems/find-peak-element/

# index function has linear time complexity
class Solution:
    def findPeakElement(self, nums) -> int:
        max_element = nums[0]
        for i in range(len(nums)):
            if nums[i] > max_element:
                       max_element = nums[i]
        return nums.index(max_element)

s = Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))
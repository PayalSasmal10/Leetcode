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


# 2nd way as Binary search
class Solution1:
    def findPeakElement(self, nums) -> int:
        s, e = 0, len(nums) -1

        while(s<e):
            mid = s + (e -s) // 2
            if nums[mid] < nums[mid + 1]:
                s = mid + 1
            else:
                e = mid
        return s

s1 = Solution1()
print(s1.findPeakElement([1,2,1,3,5,6,4]))

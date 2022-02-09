# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        new_result = nums1_set.intersection(nums2_set)
        return list(new_result)

s = Solution
print(s.intersection([1,2,2,1],[2,2]))
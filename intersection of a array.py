# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set.intersection(nums2_set))

s = Solution
print(s.intersection([1,2,2,1],[2,2]))

class Solution2:
    def intersection2(nums1, nums2):
        new_result = []
        for i in nums1:
            if i in nums2 and i not in new_result:
                new_result.append(i)
        return list(new_result)

s2 = Solution2
print(s2.intersection2([1,2,2,1],[2,2]))
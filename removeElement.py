# https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        print(len(nums))
        
s = Solution
s.removeElement([0,1,2,2,3,0,4,2],2)
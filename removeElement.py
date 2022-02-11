# https://leetcode.com/problems/remove-element/

# 1st way- o(n^2) as remove function has O(n) time complexity
class Solution:
    def removeElement(nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        print(len(nums))
        
s = Solution
s.removeElement([0,1,2,2,3,0,4,2],2)

# 2nd way - same way for this approach

class Solution:
    def removeElement(nums, val: int) -> int:
        for i in range(len(nums)):
            if nums.count(val):
                nums.remove(val)
        return len(nums)
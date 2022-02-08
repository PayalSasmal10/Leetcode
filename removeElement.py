# https://leetcode.com/problems/remove-element/

# 1st way
class Solution:
    def removeElement(nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        print(len(nums))
        
s = Solution
s.removeElement([0,1,2,2,3,0,4,2],2)

# 2nd way

class Solution:
    def removeElement(nums, val: int) -> int:
        for i in range(len(nums)):
            if nums.count(val):
                nums.remove(val)
        return len(nums)
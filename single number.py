# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(nums) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
        

s = Solution
print(s.singleNumber([2,2,1]))
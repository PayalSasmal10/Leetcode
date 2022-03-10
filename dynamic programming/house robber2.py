# https://leetcode.com/problems/house-robber-ii/

# O(n) solution

class Solution:
    def rob(self, nums) -> int:
        a=b=c=d=0
        if len(nums) <= 1:
            return nums[0]
        
        for i in range(len(nums)-1):
            b_new = b if b>a else a
            a = b+nums[i]
            b = b_new
        new_val = b if b>a else a
        
        for j in range(1,len(nums)):
            c_new = c if c> d else d
            d  = c+nums[j]
            c = c_new
        new_val2 = c if c>d else d
        return max(new_val, new_val2)
        
    
s = Solution()
print(s.rob([1,2,3,1]))
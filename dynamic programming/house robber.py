# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums) -> int:
        a = b=0
        for i in nums:
            b_new = b if b>a else a
            a = b+i
            b = b_new
        return b if b>a else a
                
s = Solution()
print(s.rob([2,1,1,2]))
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums) -> int:
        i=0
        j=i+1
        max_num=current_val=0
        while(i<len(nums)):
            if j < len(nums):
                current_val = ((nums[i] - 1) * (nums[j] - 1))
                j += 1
            else:
                i += 1
                j = i+1
            
            max_num = max(max_num,current_val)
        return max_num
            
        
s = Solution()
print(s.maxProduct([3,4,5,2]))
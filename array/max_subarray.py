# kaden's algorithms
# https://leetcode.com/problems/maximum-subarray/

# 1st approach
# o(n^3) time complexity and space complexity is O(1)
nums = [-2,1,-3,4,-1,2,1,-5,4]
class Solution:
     def maxSubArray(self, nums):
         sum = 0
         max_val = nums[0]
         for i in range(len(nums)):
             for j in range(len(nums)):
                 for k in range(i,j):
                     sum += nums[k]
                     max_val = max(sum,max_val)
        
                     #print(f"{i} and {j} value", nums[k], "max_val", max_val)
                 sum = 0
         return max_val


s = Solution()
print(s.maxSubArray(nums))

# 2nd approach
class Solution1:
     def maxSubArray(self, nums):
         sum = 0
         max_sum = nums[0]

         for i in range(len(nums)):
            
            for j in range(i,len(nums)):
                sum += nums[j]
                max_sum = max(sum, max_sum)
            sum = 0
         return max_sum


s1 = Solution1()
print(s1.maxSubArray(nums))
             

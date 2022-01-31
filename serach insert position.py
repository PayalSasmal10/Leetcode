# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(nums, target: int) -> int:
        
        s = 0
        e = len(nums) - 1
        
        while(s<=e):
            mid = (s+e)//2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                e = mid -1
            else:
                s = mid + 1
        
        return s


sol = Solution
print(sol.searchInsert([1,3,5,6],2))
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(nums, target: int) -> int:
        s = 0
        e = len(nums) -1
        
        while(s<e):
            mid = s+ (e-s)//2
            if target> nums[e] >= nums[mid] or (target <= nums[mid] <= nums[e]) or (nums[s] <= target <= nums[mid]):
                e = mid
            else:
                s = mid + 1
        return s if nums[s] == target else -1


s = Solution
print(s.search([4,5,6,7,0,1,2],0))
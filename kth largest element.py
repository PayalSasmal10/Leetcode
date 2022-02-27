# https://leetcode.com/problems/kth-largest-element-in-an-array/
from heapq import nlargest


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
       print(nlargest(k, nums)[-1])

s = Solution()
s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)



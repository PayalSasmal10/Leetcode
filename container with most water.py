# https://leetcode.com/problems/container-with-most-water/

# Brute force algorithms with O(n^2)
class Solution:
    def maxArea(self, height) -> int:
        area = 0
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                currentArea = min(height[i], height[j])*(j-i)
                area = max(area,currentArea)
        return area
        

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))

# Two pointer solution with O(n) time complexity and O(1) space complexity
class Solution1:
    def maxArea(self, height) -> int:
        area = 0
        s = 0
        e = len(height) - 1
        while(s<e):
            area = max(area, min(height[e], height[s])*(e-s))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return area
        

s1 = Solution1()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
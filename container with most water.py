# https://leetcode.com/problems/container-with-most-water/

# Brute force algorithms with O(n^2)
class Solution:
    def maxArea(self, height) -> int:
        area = 0
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                currentArea = min(height[i], height[j])*(j-i)
                print("i :", i, "j:", j)
                print("currentarea:",currentArea)
                area = max(area,currentArea)
        return area
        

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid) -> int:
        s = 0
        e = len(grid[0]) -1
        countt = 0
        while(s<len(grid)-1 and e>=0):
            if grid[s][e] >= 0:
                s += 1
            elif grid[s][e] < 0:
                countt += len(grid) - s
                e -= 1
        return countt

s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
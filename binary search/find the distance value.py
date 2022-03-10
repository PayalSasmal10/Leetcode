
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# O(n^2)
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        result = len(arr1)
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    result -= 1
                    break           
        return result
        
s = Solution()
print(s.findTheDistanceValue([4,5,8],[10,9,1,8],2))
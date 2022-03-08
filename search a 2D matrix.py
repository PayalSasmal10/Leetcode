# https://leetcode.com/problems/search-a-2d-matrix/
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# O(n)

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        s = 0
        e = len(matrix[s]) - 1
        
        while(s<len(matrix) and e >=0):
            
            if matrix[s][e] == target:
                return True
            elif matrix[s][e] < target:
                s += 1
                
            else:
                e -= 1
                 
                
        return False
        
s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
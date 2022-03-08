# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        i = 0
        s = 0
        e = len(matrix) - 1
        
        while(i<len(matrix)):
            j = len(matrix[i])
            print("j:", j)
            if j > 0:
                mid = (s+j) // 2
                if matrix[i][mid] == target:
                    return mid
                elif matrix[i][mid] < target:
                    s += 1
                    j -= 1
                else:
                    e -= 1
                    j -= 1
            else:
                i += 1
                
        return -1
        
s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
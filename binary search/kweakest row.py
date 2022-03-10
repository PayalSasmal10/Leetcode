# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/submissions/

class Solution:
    def kWeakestRows(self, mat, k: int):
        return sorted(range(len(mat)), key = mat.__getitem__)[:k]


s = Solution()
print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))
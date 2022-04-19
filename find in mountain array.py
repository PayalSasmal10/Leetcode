# https://leetcode.com/problems/find-in-mountain-array/

class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        s = 0
        e = mountain_arr.length() - 1
        
        while(s<e):
            mid = s + (e-s) // 2
            
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) < target:
                s += 1
            else:
                e -= 1
        return -1
            

s = Solution()
print(s.findInMountainArray([1,2,3,4,5,3,1], 3))
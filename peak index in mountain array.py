# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        max_element = arr[0]
        for i in arr:
            if i > max_element:
                max_element = i
                
        return arr.index(max_element)
        



# binary solution O(n)

class Solution1:
    def peakIndexInMountainArray(self, arr) -> int:
        s = 0
        e = len(arr) - 1
        while(s<e):
            mid = s + (e-s) // 2
            if arr[mid] < arr[mid+1]:
                s = mid+1
            else:
                e = mid
        return s 

s1 = Solution1()
print(s1.peakIndexInMountainArray([0,2,1,0]))
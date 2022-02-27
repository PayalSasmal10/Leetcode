# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        max_element = arr[0]
        for i in arr:
            if i > max_element:
                max_element = i
                
        return arr.index(max_element)
        


# https://leetcode.com/problems/merge-sorted-array/


# 1st way using return and modifying everything
class Solution1:
    def mergeSortedarray(nums1, m, nums2, n):
        newList1 = []
        newList2 = []
        for i in range(m):
           newList1.append(nums1[i])
        for j in range(n):
            newList2.append(nums2[j])
        
        mergeList = newList1+newList2
        mergeList.sort()
        return mergeList

s = Solution1
print(s.mergeSortedarray([1,2,3,0,0,0],3,[2,5,6],3))

# 2nd way using return function
class Solution2:
    def mergeSortedarray(nums1, m, nums2, n):
        newList1 = []
        newList2 = []
        
        mergeList = nums1[:m] + nums2[:n]
        mergeList.sort()
        return mergeList

s = Solution2
print(s.mergeSortedarray([1,2,3,0,0,0],3,[2,5,6],3))

#3rd way to solve it. without return and without extra changes only modifed nums1
class Solution3:
    def mergeSortedarray(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        nums1.extend(nums2[:n])
        nums1.sort()
        return nums1

s = Solution2
print(s.mergeSortedarray([1,2,3,0,0,0],3,[2,5,6],3))





class Solution:
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

s = Solution
print(s.mergeSortedarray([1,2,3,0,0,0],3,[2,5,6],3))



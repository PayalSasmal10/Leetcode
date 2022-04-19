#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
test = [1,1,1,1]

for j in range(test):
    print(j)
    print

print("...................................")

class Solution:
    def removeDuplicates(nums):
        countt = 0
        while countt != len(nums):
            # print(nums.count(nums[i]))
            if (nums.count(nums[countt]) != 1):
                nums.remove(nums[countt])
                print(nums)
            
            else:
                countt += 1
        return len(nums)

s = Solution
print(s.removeDuplicates([1,1,1,1]))

print("----------------------------second solution started-------------------")
# 2nd way

class Solution1:
    def removeDuplicates(self,nums):
        i = 0
        j = 1
        size = len(nums)
        while(j<size):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return nums


nums = [0,0,1,1,1,2,2,3,3,4]
s1 = Solution1()
print(s1.removeDuplicates(nums))


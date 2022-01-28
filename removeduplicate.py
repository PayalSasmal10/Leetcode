#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
test = [1,1,1,1]
for j in range(1):
    print(j)

print("...................................")

class Solution:
    def removeDuplicates(nums):
        print("length=", len(nums))
        print("before for........................")
        countt = 0
        while countt != len(nums):
            print("length=",len(nums))
            # print(nums.count(nums[i]))
            if (nums.count(nums[countt]) != 1):
                nums.remove(nums[countt])
            
            else:
                countt += 1
        return len(nums)

s = Solution
print(s.removeDuplicates([1,1,1,1]))
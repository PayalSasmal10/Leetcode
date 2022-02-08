# https://leetcode.com/problems/remove-element/

test = [0,1,2,2,3,0,4,2]
print("t:",test[7])
class Solution:
    def removeElement(nums, val: int) -> int:
        length = len(nums)
        for i in range(length-1):
            print("i:",i)
            if nums[i] == val:
                print(nums[i])
                nums.remove(nums[i])
                print(nums)
                length = len(nums)
                print("length:", length)
        
s = Solution
s.removeElement([0,1,2,2,3,0,4,2],2)
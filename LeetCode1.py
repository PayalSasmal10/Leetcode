# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
class Solution:
    def containsDuplicate(self, nums):
        sett = set(nums)
        if len(nums) != len(sett):
            return True
        else:
            return False

print(Solution().containsDuplicate([1,2,3,4]))

test = ['a', 'b', 'c']
test1 = ['d', 'b', 'e']

for i in test:
    if i in test1:
        del test[test.index(i)]

print(test)
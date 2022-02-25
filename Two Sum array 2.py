# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1
        while(i<=j):
            if numbers[i] + numbers[j] > target:
                j -= 1 
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                print("test")
                return ([i, j])

s = Solution()
print(s.twoSum([2,7,11,15], 9))
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# 1st way:

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
                return ([i+1, j+1])

s = Solution()
print(s.twoSum([2,7,11,15], 9))

# 2md way
class Solution1:
    def twoSum1(self, numbers, target: int):
        dictt = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dictt:
                
                return [dictt[target - numbers[i]], i+1]
                
            else:
                dictt[numbers[i]] = i+1


s1 = Solution1()
print(s1.twoSum1([2,7,11,15],9))
                
        
        
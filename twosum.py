# https://leetcode.com/problems/two-sum/
nums = [3, 2, 4]
class solution:
    def twoSum(self,nums,target):
        dictt = {}
        for i,j in enumerate(nums):
            if target-nums[i] in dictt:
                return [dictt[target-nums[i]],1]
            else:
                dictt[nums[i]] = i
            print(dictt)

s = solution()
s.twoSum(nums,6)


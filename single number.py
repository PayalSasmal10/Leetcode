# https://leetcode.com/problems/single-number/
# https://leetcode.com/problems/single-number-ii/

# o(n^2) complexity, as count function time complexity is O(n) and it is inside for loops so two inner loop. so O(n^2)
class Solution:
    def singleNumber(nums) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
        

s = Solution
print(s.singleNumber([2,2,1]))


# 2nd way:
class Solution2:
    def singleNumber2(nums) -> int:
        test = {}
        k= 1
        for i,j in enumerate(nums):
            if nums[i] in test:
                test[nums[i]] = k+1
            else:
                test[nums[i]] = k
        for m in test:
            if test.get(m) == 1:
                return m

s2 = Solution2
print(s2.singleNumber2([0,1,0,1,0,1,99]))
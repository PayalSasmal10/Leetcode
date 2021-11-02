# question: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in operations:
            if "++" in i:
                print(i)
                x += 1
            else:
                x -= 1
        print(x)


s = Solution()
s.finalValueAfterOperations(["--X","X++","X++"])
print()
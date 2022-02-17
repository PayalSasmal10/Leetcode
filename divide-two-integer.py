# https://leetcode.com/problems/divide-two-integers/
x = 10
x = 20
y = x
if(id(x) == id(y)):
    print("x and y id's are same")

import math
class Solution:
    def divide(dividend: int, divisor: int) -> int:
        print(dividend)
        print(divisor)
        if (dividend) or (divisor) > 0:
            test = int(dividend / divisor)
            print("i am here")
            return test
        else:
            test = dividend / divisor
            return math.ceil(test)



s  = Solution
print(s.divide(7,-3))
        
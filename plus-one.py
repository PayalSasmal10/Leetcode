

from string import digits


class Solution:
    def plusOne(digitss):
        t = ""
        for i in digitss:
            t += str(i)
        addt = int(t)+1
        plusone = [int(j) for j in str(addt)]
        return plusone

so = Solution
print(so.plusOne([4,3,2,1]))




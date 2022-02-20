# https://leetcode.com/problems/reverse-string/

s = ["hi","there"]
print(s[::-1])

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]

sw = Solution()
print(sw.reverseString(['h','e','l','l','o']))
# https://leetcode.com/problems/implement-strstr/
test = ""
print(len(test))

class Solution:
    def strStr(haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in needle:
            if needle in haystack:
                return haystack.index(i)
            else:
                return -1


s = Solution
print(s.strStr("hello", "ll"))
            
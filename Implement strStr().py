# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            print(i)
            if needle[0] == haystack[i]:
                if haystack[i: (i + len(needle))] == needle:
                    
                    return i
        return -1


s = Solution
print(s.strStr("hello", "ll"))

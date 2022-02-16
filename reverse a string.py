# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        remove_space = s.split()
        remove_space.reverse()
        return " ".join(remove_space)
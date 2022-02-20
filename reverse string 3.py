# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        convert_to_list = s.split()
        newlist = []
        for i in convert_to_list:
            newlist.append(i[::-1])
        return ' '.join(newlist)
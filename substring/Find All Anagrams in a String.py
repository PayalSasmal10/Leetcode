# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = j = 0
        dictt = {}
        new_list = []
        for d in p:
            if d in dictt:
                dictt[d] = dictt[d] + 1
            else:
                dictt[d] = 1
        count = len(dictt)
        while(j<len(s)):
            if s[j] in dictt:
                dictt[s[j]] = dictt[s[j]] - 1
                if dictt[s[j]] == 0:
                    count -= 1
            
            if (j-i+1 < len(p)):
                j += 1
            
            elif (j-i+1 == len(p)):
                if count == 0:
                    new_list.append(i)
                
                if s[i] in dictt:
                    dictt[s[i]] = dictt[s[i]] + 1
                    if dictt[s[i]] == 1:
                        count += 1
                i += 1
                j += 1
        return new_list
                
            

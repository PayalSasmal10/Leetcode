# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = j = 0
        ans = False
        dictt = {}
        for p in s1:
            if p in dictt:
                dictt[p] += 1
            else:
                dictt[p] = 1
        
        count = len(dictt)
        
        while(j<len(s2)):
            if s2[j] in dictt:
                dictt[s2[j]] -= 1
                if dictt[s2[j]] == 0:
                    count -= 1
                    
            if j-i+1 < len(s1):
                j += 1
            elif j-i+1 == len(s1):
                if count == 0:
                    ans = True
                
                if s2[i] in dictt:
                    dictt[s2[i]] += 1
                    if dictt[s2[i]] == 1:
                        count += 1
                i += 1
                j += 1
        return ans
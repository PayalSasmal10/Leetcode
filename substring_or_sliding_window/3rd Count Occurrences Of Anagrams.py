# Count Occurrences Of Anagrams
"""
str = "aabaabaa"
ptr = "aaba"
"""

strr = "aabaabaa"
ptr = "aaba"

class A:
    def anagrams(self,strr,ptr):
        i = j = ans = 0
        k = len(ptr)
        dictt = {}
       
        for t in ptr:
            if t in dictt:
                dictt[t] = dictt[t] + 1
            else:
                dictt[t] = 1
        count = len(dictt) # count is created so that we should not traverse the dictt everytime
        while(j<len(strr)):
            # calculation
            if strr[j] in dictt:
                
                dictt[strr[j]] = dictt[strr[j]] - 1
                if dictt[strr[j]] == 0:
                    count -= 1

            if (j-i+1 < k):
                j += 1
            
            elif (j-i+1 == k):
                #Calculation
                if count == 0:
                    ans += 1
                # sliding window
                if strr[i] in dictt:
                    dictt[strr[i]] = dictt[strr[i]] + 1
                    if dictt[strr[i]] == 1:
                        count += 1
                i += 1
                j += 1
        return ans


a = A()
print(a.anagrams(strr,ptr))
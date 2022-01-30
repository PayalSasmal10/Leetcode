
def longestCommonPrefix(S):
    if (len(S) == 0):
        return ""
    for i in range(len(S[0])):
        #print(i)
        c = S[0][i]
        #print(c) 
        for j in range(len(S)):
            if i == len(S[j]) or  S[j][i] != c:
                return S[0][0:i]           
    return S[0]

print(longestCommonPrefix(["dog","racecar","car"]))


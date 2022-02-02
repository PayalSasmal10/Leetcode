# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(s: str) -> str:
        res = sorted(s.split(), key=lambda x: int(x[-1]))
        print(res)
        for i in range(len(res)):
            res[i] = res[i][:-1]
        
        return ' '.join(res)


sol = Solution
sol.sortSentence("is2 sentence4 This1 a3")



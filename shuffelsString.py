#https://leetcode.com/problems/shuffle-string/
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        make_dict = {i:j for i,j in zip(indices, list(s))}
        test = ""
        
        for i in range(len(indices)):
            test += make_dict[i]
            
        return test
            
        
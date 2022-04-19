# write a program to print the all permutation of a string
"""
i/p: ABC
o/p: 
ABC
ACB
BAC
BCA
CBA
CAB
"""

class permu:
    ans = []
    def permutationss(self,strr,answer):
        
        if len(strr) == 0:
            self.ans.append([int(j) for j in answer])
            return 
    
        for i in range(len(strr)):
            cur_val = strr[i]
            left_subset = strr[0:i]
            right_subset = strr[i+1:]
            result = left_subset + right_subset
            self.permutationss(result, str(answer)+str(cur_val))
        
        

strr = [1,2,3]
answer = ""
p = permu()
p.permutationss(strr,answer)
print()
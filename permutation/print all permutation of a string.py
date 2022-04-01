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

from multiprocessing.connection import answer_challenge


class permu:
    
    def permutationss(self,strr,answer):
        
        if len(strr) == 0:
            print(answer, end=" ")
            return 
        
        for i in range(len(strr)):
            cur_val = strr[i]
            left_subset = strr[0:i]
            right_subset = strr[i+1:]
            result = left_subset + right_subset
            self.permutationss(result, answer+cur_val)
        

strr = "abc"
answer = ""
p = permu()
p.permutationss(strr,answer)
print()

def recur(n): #------------> T(n) [Total time taken]
    if n == 0: #-----------> O(1)
        return # ----------> O(1)
    else:
        recur(n-1) #-------> T(n-1)
        print(n)   # ------> O(1)

recur(5)

output:
1
2
3
4
5

#How to iterate without using loops.

T(n) = O(1) + T(n-1)
        = 1 + T(n-1) [suppose O(1) =1]
        = 1 + 1 + T((n-1)-1) [from the above eq]
        = 2 + T(n-2)
        = 2+ 1 + T((n-2)-1)
        = 3 + T(n-3)
        .
        . 
        = a + T(n-a) [same kind of pattern]

